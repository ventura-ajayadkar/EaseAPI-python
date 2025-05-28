# example.py

from constants import (
    EXCHANGE_NSE,
    EXCHANGE_BSE,
    SEGMENT_DERIVATIVE,
    SEGMENT_EQUITY,
    PRODUCT_CASH,
    PRODUCT_INTRADAY,
    ORDER_TYPE_MARKET,
    VALIDITY_DAY,
    ORDER_TYPE_LIMIT,
    OFF_MKT_FLAG_ACTIVE,
    PRODUCT_MARGIN
)


class ExampleApi:
    def __init__(self):
        print("Example initialized")

    def sso_url(self, easeapi):
        try:
            print("getting sso url, call this URL in browser to initiate SSO flow")
            state_variable = "abcde"  # this is (optional) user defined state variable, SSO flow will return this variable after successful completion of client login.
            sso_url = easeapi.get_sso_url(state_variable)
            print(f"Sso URL : {sso_url}")
        except Exception as e:
            print(f"Failed to generate sso url: {e}")

    def auth_token(self, easeapi, request_token, secret_key):
        try:
            print("generating auth token")
            auth_token, refresh_token = easeapi.generate_auth_token(request_token, secret_key)
            print(f"Auth token generated: {auth_token}")
            print(f"Refresh Token: {refresh_token}")
        except Exception as e:
            print(f"Failed to generate auth token : {e}")

    def instruments(self, easeapi):
        print("calling Instruments")
        instruments = easeapi.get_instruments()
        print(f"Instrument list downloaded, total items: {len(instruments)}")

    def fund_details(self, easeapi):
        try:
            print("Fetching fund details")
            fund_details = easeapi.get_fund_details()
            print(f"Fund available to trade: {fund_details}")
        except Exception as e:
            print(f"Failed to fetch fund details: {e}")

    def orderbook(self, easeapi):
        try:
            print("Fetching orderbook")
            orderbook = easeapi.get_orderbook()
            print(f"Order Book Data: {orderbook}")
        except Exception as e:
            print(f"Failed to fetch orderbook: {e}")

    def tradebook(self, easeapi):
        try:
            print("Fetching tradebook")
            data = easeapi.get_tradebook()
            print(f"Trade Book Data: {data}")
        except Exception as e:
            print(e)

    def holdings(self, easeapi):
        try:
            print("Fetching holdings")
            data = easeapi.get_holdings()
            print(f"Holdings Data: {data}")
        except Exception as e:
            print(e)

    def positions(self, easeapi):
        try:
            print("Fetching positions")
            data = easeapi.get_positions()
            print(f"Positions Data: {data}")
        except Exception as e:
            print(e)

    def user_profile(self, easeapi):
        try:
            print("Fetching user profile")
            data = easeapi.get_user_profile()
            print(f"User Profile Data: {data}")
        except Exception as e:
            print(e)

    def logout(self, easeapi):
        try:
            print("Logging out user")
            data = easeapi.logout(easeapi)
            print(f"Logout Data: {data}")
        except Exception as e:
            print(e)

    def place_delivery_order(self, easeapi):
        try:
            # Limit Order
            # payload = {
            #     "instrument_id": 14366,
            #     "exchange": EXCHANGE_NSE,
            #     "segment": SEGMENT_EQUITY,
            #     "transaction_type": "B",
            #     "order_type": ORDER_TYPE_LIMIT,
            #     "quantity": 1,
            #     "price": 8.1,
            #     "trigger_price": 0.0,
            #     "product": PRODUCT_CASH,
            #     "validity": VALIDITY_DAY,
            #     "disclosed_quantity": 0,
            #     "off_market_flag": OFF_MKT_FLAG_ACTIVE,
            #     "remarks": "",
            # }

            # Market Order
            payload = {
                "instrument_id": 14366,
                "exchange": EXCHANGE_NSE,
                "segment": SEGMENT_EQUITY,
                "transaction_type": "B",
                "order_type": ORDER_TYPE_MARKET,
                "quantity": 1,
                "price": 0.0,
                "trigger_price": 0.0,
                "product": PRODUCT_CASH,
                "validity": VALIDITY_DAY,
                "disclosed_quantity": 0,
                "off_market_flag": OFF_MKT_FLAG_ACTIVE,
                "remarks": "",
            }

            print("Placing delivery order")
            order_response = easeapi.place_delivery_order(payload)
            print(f"place order response :{order_response}")
        except Exception as e:
            print(f"Failed to place delivery order: {e}")

    def place_intraday_regular_order(self, easeapi):
        print("Placing intraday regular order")
        payload = {
            "transaction_type": "B",
            "exchange": EXCHANGE_NSE,
            "segment": SEGMENT_EQUITY,
            "product": PRODUCT_INTRADAY,
            "instrument_id": 7406,
            "quantity": 1,
            "price": 0.0,
            "validity": VALIDITY_DAY,
            "order_type": ORDER_TYPE_MARKET,
            "disclosed_quantity": 0,
            "trigger_price": 0.0,
            "off_market_flag": OFF_MKT_FLAG_ACTIVE,
            "remarks": "",
        }
        result = easeapi.place_intraday_regular_order(payload)
        print(f"Intraday regular order response: {result}")

    def place_intraday_derivative_regular_order(self, easeapi):
        print("Placing intraday derivative regular order")
        payload = {
            "transaction_type": "B",
            "exchange": EXCHANGE_NSE,
            "segment": SEGMENT_EQUITY,
            "product": PRODUCT_INTRADAY,
            "instrument_id": 7406,
            "quantity": 1,
            "price": 0.0,
            "validity": VALIDITY_DAY,
            "order_type": ORDER_TYPE_MARKET,
            "disclosed_quantity": 0,
            "trigger_price": 0.0,
            "off_market_flag": OFF_MKT_FLAG_ACTIVE,
            "remarks": "",
        }
        result = easeapi.place_intraday_derivative_regular_order(payload)
        print(f"Intraday derivative regular order response: {result}")

    def place_delivery_derivative_order(self, easeapi):
        print("Placing derivative order")
        payload = {
            "transaction_type": "B",
            "exchange": EXCHANGE_NSE,
            "segment": SEGMENT_DERIVATIVE,
            "product": PRODUCT_MARGIN,
            "instrument_id": 7406,
            "quantity": 1,
            "price": 0.0,
            "validity": VALIDITY_DAY,
            "order_type": ORDER_TYPE_MARKET,
            "disclosed_quantity": 0,
            "trigger_price": 0.0,
            "off_market_flag": OFF_MKT_FLAG_ACTIVE,
            "remarks": "",
        }
        result = easeapi.place_delivery_derivative_order(payload)
        print(f"Derivative order response: {result}")

    def cancel_order(self, easeapi):
        print("Canceling order")
        payload = {"order_no": "2151250528107"}
        result = easeapi.cancel_order(payload)
        print(f"Cancel order response: {result}")

    def modify_order(self, easeapi):
        try:
            print("Modifying order")
            payload = {
                "order_type": ORDER_TYPE_LIMIT,
                "quantity": 2,
                "price": 1662,
                "trigger_price": 0.0,
                "disc_quantity": 0,
                "remarks": "",
                "order_no": "2161250528104",
                "validity": VALIDITY_DAY,
            }
            response = easeapi.modify_order(payload)
            print(f"Order modified successfully. Response: {response}")
        except Exception as e:
            print(f"Failed to modify order: {e}")
