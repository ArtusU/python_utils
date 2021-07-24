import cbpro
from cbpro import authenticated_client
import config
import pprint
import json



api_url="https://api-public.sandbox.pro.coinbase.com"

authenticated_client = cbpro.AuthenticatedClient(
    config.CBPRO_PUBLIC_KEY, 
    config.CBPRO_SECRET_KEY, 
    config.CBPRO_PASSPHRASE, 
    api_url
    )

# authenticated_client.place_market_order(product_id='BTC-USD', side='buy', size=1)

accounts = authenticated_client.get_accounts()
for acc in accounts:
    currency = acc.get('currency')
    if currency=='BTC':
        acc_id = acc.get('id')
acc_history = authenticated_client.get_account_history(acc_id)
for hist in acc_history:
    print(json.dumps(hist, indent=1))


class TextWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url           = 'wss://ws-feed-public.sandbox.pro.coinbase.com'
        self.message_count = 0
    
    def on_message(self,msg):
        self.message_count += 1
        msg_type = msg.get('type',None)
        if msg_type == 'ticker':
            time_val   = msg.get('time',('-'*27))
            price_val  = msg.get('price',None)
            if price_val is not None:
                price_val = float(price_val)
            product_id = msg.get('product_id',None)
            
            print(f"{time_val:30} \
                {price_val:.3f} \
                {product_id}\tchannel type:{msg_type}")
    
    def on_close(self):
        print(f"<---Websocket connection closed--->\n\tTotal messages: {self.message_count}")

# stream = TextWebsocketClient(products=['BTC-USD'],channels=['ticker'])
# stream.start()