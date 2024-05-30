from common.httpSession import HttpClient


class ApiTest(object):
    def __init__(self):
        self.http = HttpClient()

    def test(self):
        url = "XXXXXXXXXXXXXXXXXXXX"
        response = self.http.send_request("get", url)
        print(response.text)
    def test2(self):
        url = "XXXXXXXXXXXXXXXXXXXX"
        response = self.http.send_request("get", url)
        print(response.text)
