import requests


def lkmexToTokenViaLockedmexExchange(token, balance=pow(10, 6)):
    url = "https://elrond.api.beeftech.cloud/scQuery"
    token_hex = token.encode("utf-8").hex()
    lkmex_hex = format(int(balance * pow(10, 18)), "x")
    parameters = {
        "scAddress": "erd1qqqqqqqqqqqqqpgqmua7hcd05yxypyj7sv7pffrquy9gf86s535qxct34s",
        "funcName": "simulate_swap_lkmex_to_token",
        "args": [token_hex, lkmex_hex],
    }
    try:
        response = requests.post(url, json=parameters)
        if response.status_code != 200:
            return -200
        data = response.json()
        token = int(data["output"][2]["bigNumber"]) / pow(10, 18)
        return token
    except Exception:
        return -1


joy = lkmexToTokenViaLockedmexExchange("JOY-43bad3", 10)
print(f"10 LKMEX = {joy:.3f} JOY")

egld = lkmexToTokenViaLockedmexExchange("EGLD")
print(f"1m LKMEX = {egld:.3f} EGLD")
