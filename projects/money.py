import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        return data["rates"].get(to_currency, None)
    else:
        print("Error: Could not fetch exchange rate.")
        return None

amount = float(input("Enter amount: "))
from_currency = input("Enter source currency (e.g., USD): ").upper()
to_currency = input("Enter target currency (e.g., INR): ").upper()

rate = get_exchange_rate(from_currency, to_currency)
if rate:
    print(f"{amount} {from_currency} is equal to {amount * rate:.2f} {to_currency}")