from requests import get
from urllib.parse import quote

class Validate():
    def __init__(self, uuid):
        self.uuid = uuid
        self.id = "123456789"

    def check(self):
        if self.uuid == self.id:
            return True

class DeviceID():
    def __init__(self, UA:str):
        self.UserAgent = quote(UA)
        self.api = 'https://userstack.com/ua_api.php?ua='

    def data(self):
        resp = get(self.api+self.UserAgent, headers={'user-agent':self.UserAgent})
        if resp.status_code == 200:
            return {"status_code":resp.status_code, "response":resp.json()}
        else:
            return {"status_code":resp.status_code,"reason":"API DEPRECATED"}
