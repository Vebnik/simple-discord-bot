

class ChannelEnpoint:

    @staticmethod
    def crud_channel(url: str, channel_id: int) -> str:
        return f'{url}/channels/{channel_id}'


class MessageEnpoint:

    @staticmethod
    def create(url: str, channel_id: int) -> str:
        return f'{url}/channels/{channel_id}/messages'