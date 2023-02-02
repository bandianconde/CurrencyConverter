import requests

currency_code = input()
cache = {}
r = requests.get(f"http://www.floatrates.com/daily/{currency_code}.json")
if currency_code != 'usd':
    cache['usd'] = r.json()['usd']['rate']
if currency_code != 'eur':
    cache['eur'] = r.json()['eur']['rate']
while True:
    target_currency = input().lower()
    if not target_currency:
        break
    amount = int(input())

    print("Checking the cache...")
    if target_currency in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[target_currency] = r.json()[target_currency]['rate']
    
    converted_amount = round(amount * cache[target_currency], 2)
    print(f'You received {converted_amount} {target_currency}.')
