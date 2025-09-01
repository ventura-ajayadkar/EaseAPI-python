import time
import logging
from easeapi import EaseApiTicker

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ticker = EaseApiTicker(
    app_key="VUz2rue5R0mYqe3jx5Ic",
    client_id="AA0605",
    auth_token="eyJraWQiOiJlMDc0TUpqYnJLTXhEU3lSN2tWY25xY0x1T..."
)

def on_ticks(ws, tick_data):
    logging.info(f"Tick: {tick_data}")

def on_connect(ws, response):
    logging.info("Connected!")
    
    # For market data connection
    if ws.ws_url == ws.market_data_url:

        # Subscribe to instruments
        ws.subscribe(["2885", "11536"], exchange=ws.EXCHANGE_NSE)  # RELIANCE, TCS on NSE
        ws.subscribe(["500570"], exchange=ws.EXCHANGE_BSE)  # TATAMOTORS on BSE
    
    # For order status connection
    elif ws.ws_url == ws.order_status_url:
        logging.info("Connected to order status WebSocket")
        # order status websocket it will push updates automatically

def on_close(ws, code, reason):
    logging.info(f"Disconnected: {reason}")

# Set callbacks for market data
ticker.on_ticks = on_ticks
ticker.on_connect = on_connect
ticker.on_close = on_close

# Example 1: Connect to market data endpoint (default)
ticker.connect()

# Example 2: If you want to connect to order status endpoint instead
# Create a second instance for order status
order_ticker = EaseApiTicker(
    app_key="VUz2rue5R0mYqe3jx5Ic",
    client_id="AA0605",
    auth_token="eyJraWQiOiJlMDc0TUpqYnJLTXhEU3lSN2tWY2..."
)

# Set callbacks for order ticker
order_ticker.on_ticks = on_ticks
order_ticker.on_connect = on_connect
order_ticker.on_close = on_close

# Connect to order status endpoint
order_ticker.connect(use_order_status=True)

# Keep the program running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    ticker.close()
    order_ticker.close()