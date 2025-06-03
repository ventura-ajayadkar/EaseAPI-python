import logging
import json
from easeapi.easeapigateway import EaseApiGateway

logging.basicConfig(level=logging.DEBUG)

def get_demo_instruments(instruments):
    """
    Filters and selects demo instruments from the full instruments list.
    Returns a list of instrument dictionaries used for the demo.
    """
    # Filter instruments matching 'RELIANCE'
    reliance_instruments = list(filter(lambda inst: 
        (inst.get('name') and inst.get('name').strip() == 'RELIANCE') or
        (inst.get('trading_symbol') and 'RELIANCE' in inst.get('trading_symbol').strip()),
        instruments
    ))
    
    # Pick instruments from different exchanges/segments
    reliance_nse_eq = next((inst for inst in reliance_instruments if inst.get('exchange', '').strip() == 'NSE'), None)
    reliance_bse_eq = next((inst for inst in reliance_instruments if inst.get('exchange', '').strip() == 'BSE'), None)
    reliance_fut = next((inst for inst in reliance_instruments if inst.get('instrument', '').strip().upper() == 'FUT' and float(inst.get('last_price', 0)) != 0), None)
    reliance_ce = next((inst for inst in reliance_instruments if inst.get('instrument', '').strip().upper() == 'CE' and float(inst.get('last_price', 0)) != 0), None)
    reliance_pe = next((inst for inst in reliance_instruments if inst.get('instrument', '').strip().upper() == 'PE' and float(inst.get('last_price', 0)) != 0), None)

    return [
        {
            "Type": "RELIANCE NSE EQ",
            "Trading Symbol": reliance_nse_eq.get("trading_symbol") if reliance_nse_eq else None,
            "Instrument ID": reliance_nse_eq.get("exchange_token") if reliance_nse_eq else None,
            "Last Price": reliance_nse_eq.get("last_price") if reliance_nse_eq else None,
            "Lot Size": reliance_nse_eq.get("lot_size") if reliance_nse_eq else None,
        },
        {
            "Type": "RELIANCE BSE EQ",
            "Trading Symbol": reliance_bse_eq.get("trading_symbol") if reliance_bse_eq else None,
            "Instrument ID": reliance_bse_eq.get("exchange_token") if reliance_bse_eq else None,
            "Last Price": reliance_bse_eq.get("last_price") if reliance_bse_eq else None,
            "Lot Size": reliance_bse_eq.get("lot_size") if reliance_bse_eq else None,
        },
        {
            "Type": "RELIANCE FUT",
            "Trading Symbol": reliance_fut.get("trading_symbol") if reliance_fut else None,
            "Instrument ID": reliance_fut.get("exchange_token") if reliance_fut else None,
            "Last Price": reliance_fut.get("last_price") if reliance_fut else None,
            "Lot Size": reliance_fut.get("lot_size") if reliance_fut else None,
        },
        {
            "Type": "RELIANCE CE",
            "Trading Symbol": reliance_ce.get("trading_symbol") if reliance_ce else None,
            "Instrument ID": reliance_ce.get("exchange_token") if reliance_ce else None,
            "Last Price": reliance_ce.get("last_price") if reliance_ce else None,
            "Lot Size": reliance_ce.get("lot_size") if reliance_ce else None,
        },
        {
            "Type": "RELIANCE PE",
            "Trading Symbol": reliance_pe.get("trading_symbol") if reliance_pe else None,
            "Instrument ID": reliance_pe.get("exchange_token") if reliance_pe else None,
            "Last Price": reliance_pe.get("last_price") if reliance_pe else None,
            "Lot Size": reliance_pe.get("lot_size") if reliance_pe else None,
        },
    ]

def demonstrate_easeapi_capabilities():
    try:
        # Welcome Message
        print("\n🚀 Welcome to EaseAPI Demo!")
        print("Let's explore the power of automated trading...\n")

        # Initialize Trading Environment
        print("🔧 Setting up trading environment...")
        easeapi = EaseApiGateway(app_key="CVnSgBwRhGhOCt6mjmUo", disable_ssl=True, debug=False)

        # Begin Trading Journey: Authentication Process
        print("\n🔑 Starting Authentication Process")
        print("=================================")

        # Generate login URL
        sso_url = easeapi.get_sso_url(state_variable="abcd12345")
        print("📱 Login URL Generated:", sso_url)

        # # Authenticate the user and set up the trading session.
        # print("\n🔐 Authenticating User...")
        # client_id, auth_token, refresh_token = easeapi.generate_auth_token(
        #     request_token="9Yz0LfHPQH", secret_key="5KzWbIZFQn"
        # )

        # # Print authentication details in a copy-friendly format
        # print("\n========== Authentication Response ==========")
        # print("\n🆔 Client ID")
        # print("----------------")
        # print(client_id)
        # print("\n🔑 Auth Token")
        # print("----------------")
        # print(auth_token)
        # print("\n🔄 Refresh Token")
        # print("----------------")
        # print(refresh_token)
        # print("\n===========================================\n")

        # # Set up Trading Session
        # print("✨ Setting up your trading session...")
        # easeapi.set_client_id(client_id)
        # easeapi.set_auth_token(auth_token)
        # easeapi.set_refresh_token(refresh_token)

        # ------------------------------------------------------------------
        # * For development, using hardcoded authentication credentials *
        # ------------------------------------------------------------------
        print("\n✨ Setting up your trading session (development mode)...")
        easeapi.set_client_id("AA0605")
        easeapi.set_auth_token("eyJraWQiOiJmWTdRYVhEYlR6TGtwYXlzMWR1Qk1kTHViSzFHcW...")
        easeapi.set_refresh_token("eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.Yd...")

        # Market Overview
        print("\n📊 Fetching Market Overview")
        print("=========================")
        print("\nFetching User Profile...")
        profile = easeapi.get_user_profile()
        print("User Profile:")
        print(profile)

        print("\nFetching Fund Details...")
        funds = easeapi.get_fund_details()
        print("Available Funds:")
        print(funds)

        print("\nFetching Instruments...")
        instruments = easeapi.get_instruments()
        print(f"Total Instruments: {len(instruments)}")
        
        demo_instruments = get_demo_instruments(instruments)
        print("\n🎉 Selected Instruments for Demo:")
        print(demo_instruments)

        # Trading Operations
        print("\n💹 Trading Operations")
        print("===================")

        # 1. Place Order (Cash Segment)
        print("\n💵💵💵 Placing Cash Order...")
        cash_order_payload = {
            "instrument_id": int(demo_instruments[0]["Instrument ID"]) if demo_instruments and demo_instruments[0]["Instrument ID"] else 0,
            "exchange": "NSE",
            "segment": "E",            # E for Equity
            "transaction_type": "B",
            "order_type": "MKT",       # Market order
            "quantity": 1,
            "price": 0.0,
            "trigger_price": 0.0,
            "product": "C",            # C for Cash and Carry
            "validity": "DAY",
            "disclosed_quantity": 0,
            "off_market_flag": 0,
        }
        delivery_order = easeapi.place_delivery_order(cash_order_payload)
        print("Delivery Order Response:")
        print(delivery_order)

        # 2. Place NSE FUT Order (NSE F&O Segment)
        print("\n💵💵💵 Placing NSE FUT Order...")
        fut_order_payload = {
            "instrument_id": int(demo_instruments[2]["Instrument ID"]) if demo_instruments and demo_instruments[2]["Instrument ID"] else 0,
            "exchange": "NSE",
            "segment": "D",            # D for F&O
            "transaction_type": "B",
            "order_type": "MKT",
            "quantity": int(demo_instruments[2]["Lot Size"]) if demo_instruments and demo_instruments[2]["Lot Size"] else 1,
            "price": 0.0,
            "trigger_price": 0.0,
            "product": "M",            # M for Margin
            "validity": "DAY",
            "disclosed_quantity": 0,
            "off_market_flag": 0,
        }
        nse_fut_order = easeapi.place_delivery_order(fut_order_payload)
        print("Delivery NSE FUT Order Response:")
        print(nse_fut_order)

        # 3. Place NSE Call Option Order (NSE F&O Segment)
        print("\n💵💵💵 Placing NSE Call Option Order...")
        ce_order_payload = {
            "instrument_id": int(demo_instruments[3]["Instrument ID"]) if demo_instruments and demo_instruments[3]["Instrument ID"] else 0,
            "exchange": "NSE",
            "segment": "D",
            "transaction_type": "B",
            "order_type": "MKT",
            "quantity": int(demo_instruments[3]["Lot Size"]) if demo_instruments and demo_instruments[3]["Lot Size"] else 1,
            "price": 0.0,
            "trigger_price": 0.0,
            "product": "M",
            "validity": "DAY",
            "disclosed_quantity": 0,
            "off_market_flag": 0,
        }
        nse_ce_order = easeapi.place_delivery_order(ce_order_payload)
        print("Delivery NSE Call Option Order Response:")
        print(nse_ce_order)

        # 4. Place NSE Put Option Order (NSE F&O Segment)
        print("\n💵💵💵 Placing NSE Put Option Order...")
        pe_order_payload = {
            "instrument_id": int(demo_instruments[4]["Instrument ID"]) if demo_instruments and demo_instruments[4]["Instrument ID"] else 0,
            "exchange": "NSE",
            "segment": "D",
            "transaction_type": "B",
            "order_type": "MKT",
            "quantity": int(demo_instruments[4]["Lot Size"]) if demo_instruments and demo_instruments[4]["Lot Size"] else 1,
            "price": 0.0,
            "trigger_price": 0.0,
            "product": "M",
            "validity": "DAY",
            "disclosed_quantity": 0,
            "off_market_flag": 0,
        }
        nse_pe_order = easeapi.place_delivery_order(pe_order_payload)
        print("Delivery NSE Put Option Order Response:")
        print(nse_pe_order)

        # 5. Place Intraday Order (Cash Segment)
        print("\n💵💵💵 Placing Intraday Equity Order...")
        intraday_payload = {
            "instrument_id": int(demo_instruments[0]["Instrument ID"]) if demo_instruments and demo_instruments[0]["Instrument ID"] else 0,
            "exchange": "NSE",
            "segment": "E",
            "transaction_type": "B",
            "order_type": "LMT",  # Limit order
            "quantity": 1,
            "price": float(demo_instruments[0]["Last Price"]) if demo_instruments and demo_instruments[0]["Last Price"] else 0.0,
            "trigger_price": 0.0,
            "product": "I",       # I for Intraday
            "validity": "DAY",
            "disclosed_quantity": 0,
            "off_market_flag": 0,
        }
        intraday_order = easeapi.place_intraday_order(intraday_payload)
        print("Intraday Order Response:")
        print(intraday_order)

        # Modify Existing Order
        print("\nModifying Order...")
        modify_order_payload = {
            "order_type": "LMT",
            "quantity": 1,
            "price": float(demo_instruments[0]["Last Price"]) if demo_instruments and demo_instruments[0]["Last Price"] else 0.0,
            "trigger_price": 0.0,
            "disc_quantity": 0,
            "order_no": str(json.loads(intraday_order).get("order_no")),
            "validity": "DAY"
        }
        modify_order_response = easeapi.modify_order(modify_order_payload)
        print("Modify Order Response:")
        print(modify_order_response)

        # Cancel Existing Order
        print("\nCancelling Order...")
        cancel_order_payload = {
            "order_no": str(json.loads(intraday_order).get("order_no")),
        }
        cancel_order_response = easeapi.cancel_order(cancel_order_payload)
        print("Cancel Order Response:")
        print(cancel_order_response)

        # Portfolio Management
        print("\n📈 Portfolio Management")
        print("=====================")

        print("\nFetching Trade Book...")
        trade_book = easeapi.get_tradebook()
        print("Trade Book:")
        print(trade_book)

        print("\nFetching Positions...")
        positions = easeapi.get_positions()
        print("Positions:")
        print(positions)

        print("\nFetching Order Book...")
        order_book = easeapi.get_orderbook()
        print("Order Book:")
        print(order_book)

        print("\nFetching Holdings...")
        holdings = easeapi.get_holdings()
        print("Holdings:")
        print(holdings)

        # Cleanup and Logout
        print("\n👋 Wrapping Up Session")
        print("===================")
        logout_response = easeapi.logout()
        print("✅ Successfully logged out. Thank you for using EaseAPI!")

    except Exception as error:
        print("\n❌ Oops! Something went wrong:", str(error))
        raise error

if __name__ == "__main__":
    print("🎯 Initializing EaseAPI Demo...")
    try:
        demonstrate_easeapi_capabilities()
        print("\n🎉 Demo completed successfully!")
    except Exception as err:
        print("\n💥 Demo encountered an error:", str(err))
