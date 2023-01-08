import requests, typing


class Panel:
    global api_key, base_url
    api_key = "258dffa2acfd0761699f01d030c57aa8"
    base_url = "https://panelyz.com/api/v2"



#---    get user balance   ---#
def getBalance():
    try:

        p = {
            "key": api_key,
            "action": "balance"
        }

        re = requests.post(base_url, params=p)

        if re.status_code == 200:
            print(re.text)

    except Exception as e:
        print(e)



#---    add order   ---#
def addOrder(service: int, quantity: int, link: str):
    try:
        p = {
            "key": api_key,
            "action": "add",
            "service": service,
            "link": link,
            "quantity": quantity
        }

        re = requests.post(base_url, params=p)

        if re.status_code == 200:
            print(re.text)

    except Exception as e:
        print(e)



#---    get order status   ---#
def getOrderStat(order: int):
    try:
        p = {
            "key": api_key,
            "action": "status",
            "order": order
        }

        re = requests.post(base_url, params=p)

        if re.status_code == 200:
            print(re.text)

    except Exception as e:
        print(e)



#---    get multiple order status   ---#
def getMultOrderStat(orders: typing.Union[list, int]):
    try:
        p = {
            "key": api_key,
            "action": "status",
        }

        if type(orders) == int:
            p["order"] = orders
        else:
            p["orders"] = orders

        re = requests.post(base_url, params=p)

        if re.status_code == 200:
            print(re.text)

    except Exception as e:
        print(e)



#---    gets services   ---#
def getServices():
    try:
        p = {
            "key": api_key,
            "action": "services"
        }

        re = requests.post(base_url, params=p)

        if re.status_code == 200:
            print(re.text)

    except Exception as e:
        print(e)



#---    create refill   ---#
def createRefill(order: int):
    try:
        p = {
            "key": api_key,
            "action": "refill",
            "order": order
        }

        re = requests.post(base_url, params=p)

        if re.status_code == 200:
            print(re.text)

    except Exception as e:
        print(e)



#---    get refill status   ---#
def getRefillStat(refill_id: int):
    try:
        p = {
            "key": api_key,
            "action": "refill_status",
            "refill": refill_id
        }

        re = requests.post(base_url, params=p)

        if re.status_code == 200:
            print(re.text)

    except Exception as e:
        print(e)