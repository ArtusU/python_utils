import cbpro
import time

public_client = cbpro.PublicClient()

result = public_client.get_product_ticker('ADA-USD')
result_st = public_client.get_product_24hr_stats('ADA-USD')

print(result)
print(result_st)


data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]

auth_client = cbpro.AuthenticatedClient(public, passphrase, secret)

auth_client.buy(price='500', size='1000', order_type='limit', product_id='ADA-USD')
auth_client.sell(price='50000000', size='1000', order_type='limit', product_id='ADA-USD')


sell_price = 500000
sell_amount = 500

buy_price = 1000
buy_amount = 1000

while True:
    price = float(auth_client.get_product_ticker(product_id='ADA-USD')['price'])
    if price <= buy_price:
        print('Buying ADA')
        auth_client.buy(size=buy_amount, order_type='market', product_id='ADA-USD')
    elif price >= sell_price:
        print('Selling ADA')
        auth_client.sell(size=sell_amount, order_type='market', product_id='ADA-USD')
    else:
        print('Nothing... Price is {price:,}')
    time.sleep(10)