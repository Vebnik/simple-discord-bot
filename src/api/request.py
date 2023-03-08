import requests, logging, json


class Request:

    def __init__(self, user_agent: str, token: str) -> None:
        self.headers = {
            'User-Agent': user_agent, 
            'Authorization': f'Bot {token}' 
            }

    def post(self, url: str, body):
        logging.info(url)

        try:
            response = requests.post(url=url, json=body, headers=self.headers)
            print(response)
            return response.json()
        except Exception as ex:
            logging.critical(ex)
            return {'ok': False, 'status': response.status_code, 'message': ex}

    def get(self, url: str):
        logging.info(url)

        try:
            response = requests.get(url=url, headers=self.headers)
            return response.json()
        except Exception as ex:
            logging.critical(ex)
            return {'ok': False, 'status': response.status_code, 'message': ex}