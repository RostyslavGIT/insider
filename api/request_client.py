import requests
from config.logger import logger as log


class SessionClientJSON:
    headers = {
        'Content-Type': 'application/json',
    }


    def __init__(self, base_url: str):
        self._session = requests.Session()
        self.base_url = base_url
        self._session.headers.update(self.headers)


    def _send_request(self, method, url, **kwargs):
        try:
            response = method(url, **kwargs)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json() if response.content else response.status_code
        except requests.exceptions.RequestException as e:
            log.error(f"Request failed: {e}")
            return {"status": response.status_code, "error": str(e)}


    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        log.debug(f"Making GET request to {url}")
        return self._send_request(self._session.get, url, params=params)


    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        log.debug(f"Making POST request to {url} with payload {json}")
        return self._send_request(self._session.post, url, json=json)


    def put(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        log.debug(f"Making PUT request to {url} with payload {json}")
        return self._send_request(self._session.put, url, json=json)


    def delete(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        log.debug(f"Making DELETE request to {url}")
        return self._send_request(self._session.delete, url, json=json)