import requests, typing

class Panel:

    def __init__(self):
        self.api_key = "your own api key"
        self.base_url = "https://panelyz.com/api/v2"

    #---    get user balance   ---#
    def getBalance(self):
        try:

            p = {
                "key": self.api_key,
                "action": "balance"
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)



    #---    add order   ---#
    def addOrder(self, service: int, quantity: int, link: str):
        try:
            p = {
                "key": self.api_key,
                "action": "add",
                "service": service,
                "link": link,
                "quantity": quantity
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)



    #---    get order status   ---#
    def getOrderStat(self, order: int):
        try:
            p = {
                "key": self.api_key,
                "action": "status",
                "order": order
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)



    #---    get multiple order status   ---#
    def getMultOrderStat(self, orders: typing.Union[list, int]):
        try:
            p = {
                "key": self.api_key,
                "action": "status",
            }

            if type(orders) == int:
                p["order"] = orders
            else:
                p["orders"] = orders

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)



    #---    gets services   ---#
    def getServices(self):
        try:
            p = {
                "key": self.api_key,
                "action": "services"
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)



    #---    create refill   ---#
    def createRefill(self, order: int):
        try:
            p = {
                "key": self.api_key,
                "action": "refill",
                "order": order
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)



    #---    get refill status   ---#
    def getRefillStat(self, refill_id: int):
            try:
                p = {
                    "key": self.api_key,
                    "action": "refill_status",
                    "refill": refill_id
                }

                re = requests.post(self.base_url, params=p)

                if re.status_code == 200:
                    print(re.text)

            except Exception as e:
                print(e)
