import requests

from shared.abstract_classes.Request import Request

class GetRequest(Request):
    def send(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None