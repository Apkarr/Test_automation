import requests

class MoyKlass:
    def __int__(self):
        self.base_url = "https://api.moyklass.com/v1/company/managers"

    def get_api_manager(self, id, name, phone, email):
        headers = {
            'id': id,
            'name': name,
            'phone': phone,
            'email': email
        }

        res = requests.get(self.base_url + 'api/manager/', headers=headers)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
