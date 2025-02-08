import requests

class BCPCharger:
    def __init__(self, api_url):
        self.api_url = api_url

    def start_charging(self):
        return requests.post(f"{self.api_url}/start").json()

    def stop_charging(self):
        return requests.post(f"{self.api_url}/stop").json()

    def get_status(self):
        return requests.get(f"{self.api_url}/status").json()
