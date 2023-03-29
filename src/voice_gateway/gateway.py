from websockets.legacy import client
import asyncio, json, logging, struct, libnacl

from src.voice_gateway.models import VoiceUpdateEvent, InitMessage, VoiceIndentifyMessage, SelectProtocolMessage


class VoiceGateway:

    connection: client.WebSocketClientProtocol
    config: VoiceUpdateEvent
    voice_identify_data: VoiceIndentifyMessage
    select_protocol: SelectProtocolMessage
    heartbeat_interval: int
    identify_data: dict
    current_packet_num_audio: int = 0

    def __init__(self, config: VoiceUpdateEvent, app) -> None:
        self.config = config
        self.identify_data = {
            "op": 0,
            "d": {
                "server_id": config.d.guild_id,
                "user_id": 965306531476279346,
                "session_id": app.session_id,
                "token": config.d.token
            }
        }

    async def run(self):
        await self._gateway_connect()
        await self._identify()
        await self._select_protocol()
        await self._speaking()
        await asyncio.gather(*[self._event(), self._heartbeat()])

    async def _gateway_connect(self) -> None:
        try:
            logging.info('_voice_gateway_connect')

            self.connection = await client.connect(f'wss://{self.config.d.endpoint}?v=10&encoding=json')
            msg = InitMessage.parse_raw(await self.connection.recv())
            self.heartbeat_interval = msg.d.heartbeat_interval

            print(msg)
        except Exception as ex:
            logging.critical(ex); exit()

    async def _heartbeat(self) -> None:
        while True:
            await asyncio.sleep(self.heartbeat_interval/1000)
            await self.connection.send(json.dumps({ "op": 3, "d": 1501184119561 }))
            logging.info('_voice_heartbeat')
    
    async def _identify(self) -> None:
        logging.info('_voice_identify')

        await self.connection.send(json.dumps(self.identify_data))
        self.voice_identify_data = VoiceIndentifyMessage.parse_raw(await self.connection.recv())

        print(self.voice_identify_data)

    async def _event(self) -> None:
        while True:
            try:
                msg: dict = json.loads(await self.connection.recv())
                logging.info('_voice_event'); logging.info(msg)                
            except Exception as ex:
                logging.critical(ex)
                continue

    async def _select_protocol(self) -> None:
        logging.info('_select_protocol')

        config = {
            "op": 1,
            "d": {
                "protocol": "udp",
                "data": {
                    "address": self.voice_identify_data.d.ip,
                    "port": self.voice_identify_data.d.port,
                    "mode": "xsalsa20_poly1305_lite"
                }
            }
        }

        await self.connection.send(json.dumps(config))
        self.select_protocol = SelectProtocolMessage.parse_raw(await self.connection.recv())
        print(self.select_protocol)

    async def _speaking(self) -> None:
        config = {
            "op": 5,
            "d": {
                "speaking": 5,
                "delay": 0,
                "ssrc": 1
            }
        }

        await self.connection.send(json.dumps(config))
        msg = await self.connection.recv()

        print(msg)

    async def _resume(self) -> None:
        logging.info('_resume')

    async def _send_audio(self, msg) -> None:
        cipher_text = f"\x90\x78{struct.pack('>h', self.current_packet_num_audio)}\x2f\xa5\x6c\xab\x00\x00\x00\x01"
        cipher_text = f'{cipher_text}{self._encrypt(msg)}'
        cipher_text = f"{cipher_text}{struct.pack('<I', self.current_packet_num_audio)}"

        await self.connection.send(cipher_text)
        self.current_packet_num_audio += 1

    def _encrypt(self, plain_text) -> str:
        cipher_text = libnacl.crypto_secretbox(
            plain_text, 
            struct.pack('<I', self.current_packet_num_audio) + "\x00" * 20, 
            ''.join([chr(char) for char in self.select_protocol.d.secret_key])
        )

        if(self.current_packet_num_audio > 32766):
            self.current_packet_num_audio = 0

        return cipher_text