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
        easeapi = EaseApiGateway(app_key="Ox2vExSRL2TGKUYv11Ao", disable_ssl=False, debug=False)

        # Begin Trading Journey: Authentication Process
        print("\n🔑 Starting Authentication Process")
        print("=================================")

        # # Generate login URL
        sso_url = easeapi.get_sso_url(state_variable="abcd12345")
        print("📱 Login URL Generated:", sso_url)

        # # Authenticate the user and set up the trading session.
        # print("\n🔐 Authenticating User...")
        # response = easeapi.generate_auth_token(
        #     request_token="n0QFgT2nQ7", secret_key="y5J58qaROG"
        # )

        # # print("\n🔐 Authenticating User using TOTP...")
        response = easeapi.generate_auth_token_with_otpt(
            client_id="AA0605", password="1234", totp="345261", secret_key="y5J58qaROG"
        )

        client_id = response.get("client_id", None)
        auth_token = response.get("auth_token", None)
        refresh_token = response.get("refresh_token", None)

        # Print authentication details in a copy-friendly format
        print("\n========== Authentication Response ==========")
        print("\n🆔 Client ID")
        print("----------------")
        print(client_id)
        print("\n🔑 Auth Token")
        print("----------------")
        print(auth_token)
        print("\n🔄 Refresh Token")
        print("----------------")
        print(refresh_token)
        print("\n===========================================\n")

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
        easeapi.set_auth_token("eyJraWQiOiJlMDc0TUpqYnJLTXhEU3lSN2tWY25xY0x1TXFhUG92TlBNQ0FKM0VwRTBFPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI4MGNjZmVjZC0yODg3LTRmOWQtYTMwMS05ZDlkNWI5M2FjMmQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX0ZUc1JPTmNWYSIsImNsaWVudF9pZCI6IjczaTNodXVsbGllYzkzMHZobjZzbGo0YWs4Iiwib3JpZ2luX2p0aSI6IjI1ZDc1NWY4LTFlMWItNGRkNC1iNzg5LWZlYzU0YmQ3OTMzZCIsImV2ZW50X2lkIjoiYzdiZjg2N2EtNjEwOS00YjVlLWJmYjctOTUyMGMxOWEwY2NmIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc1NTkzNzAzNSwiZXhwIjoxNzU2MDIzNDM1LCJpYXQiOjE3NTU5MzcwMzUsImp0aSI6IjI3NjJmNzA0LWZkY2EtNGMwMC1hODU0LWU4MzQ2MDRhMGM2OCIsInVzZXJuYW1lIjoiYWEwNjA1In0.PTRo2klhvb1YPwo2D1LM8vfgIcCf3TOlgfGdgMQs4a-MbHdz3uh74bvFxBVxYQdnG3i6hwCtMPIqUqWc9vKHxLJ_9_CuILX_l8_2oDwE_wUWhgB8HVznak8hteXS0s87PIKU79HcYdAxrBwYO94fYPFLXJ1Z6-ukKPIB8K2UkAr5LQ2ZHXl2XSHUI9JrFqg5mbjFo4QtpTRdE4tRi27jjx3-dFfaP5bT6gG8wCF15iA_CDKAwVH6GfskWCQZV1CDX2Vqub8bwy00AAN9ngWs0sw_Ldo_IKqMMLKbgH7pw6ITcXj-4awp1Y4NkQRkMUZTLhFQwXYgNc-9FZgNPd4zow")
        easeapi.set_refresh_token("eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.uWiglnhsaUFmuGHcdJZTTSB-yDAgd8ucQFs45sAnEbUGaGlRVFqSTWEHKXaBDSRsDOJ1c2buLAsJO7-Oq2flECZ-Tk8S5JMV4t4Ie29d8uGXpCaMmIxl05MCHjaUv5XMzwIlUlujNB2nytbh_Awq66M60MYmMi0JkvyM6hZGmCBm-Nx5PXxNilxj2FIpaEYEeJ48J4XV1Zt9QOA_LZNYXH4R8guVeknPcOa4NYXiyeTPCCBRD6Pr-ARwLF9z1o6PBvhCJsuuvyo0TBYbnVafDFLz_jyzM5LkhvYsy77mQ08Sp7q0cxHK5jD2UgJJnxzlQc2xbxfTtsJ-Y3KWSQCcRQ.mI5vnDfmWM4Bkp3j.JdQ-w-p0ih-O1Y3aeqVS-hi2IfCr2toEp2PLvXnxwfK5pKOgWxwkPo1IwNXThoAHWxdECNCJnllpxFt-Pq47mZgn7xIvqPD6GBw2a9dBBExlONeWs8l9P_AjziXCzpzrt2y4do6789h0fhtDAgSaQfSYaKpJkIvKGRyqea8HBAG2pVf5yTtFK9-z9lbJISuxyW0UYQrPOU7Wu_SBZrRo-r2DfZj-bLZXXwQV4Si7lZM7j1y7Q3oTDg1pdLqOn9ASpW_-O39fLvC-BPP3xNI_ZuJkwWuYNZkyQyFziJE4fPbRNOjfe8AIFxvh0Tn40ZjDDTjzp6mGA2ZIFQyJaaqOYOhNC0kWXfOATIPyKlaIsfFX90JYBforsjIFAjvVbn8p_7SmO4JnuzD2bNH8-FblfrvGTkJrQx7m1dih9S_Db2jWTr9-CiP4kHXZ3PTx6B2xXIwgBxD1g1zDOw9RIYm2El-C8XdzSfoHEdSdCeyqFVyUNL7iLQbSsqcSFIPl4iKtKR39vehDhufbrwOjHdhfqqg83nMDkpS674ajMwsxlio6Ydmo0GuOLuAeX5GVtivWwqJLkKSSdtiKPZbZ2LINmfP21dc3vkde5kTTAaqpvCFhEbto43gG-nCuNm2ipm9EmQBGJn3qOh5HL_W9CwPh6I19NeB7kXXHNcC-pGArHiQ2u9ApO9xtUxa7R4k7Bu1LS1mohxNuQKRXssZiuV0n7sCMeb6QXGYK9ExLWo4Qw-oc_jkeqmDi9uWUgAOev2sg4Jipj4RK-PIKdIYLbtbicSQEnrxiQt-FdyGLx58Y0DnK-YZ1aFN6sWThi1QJpAdD_LfA8M1jDwJk6JY3UoXHNWztl0b38jyNBQGTVdQHOlTphuB3xaxZuhbuQ0BzixZPGwx2dPmPTQ5A_7m0QpbpUOt69MO4FmFDgCbY7wtf7fuM7Z5G-8np2UGm89GzytmcKWvT6Y4J7ufrjyBS4lvfL_yXM50cMSTaqpe4bWiaI55_Xg1pZp9AsSRfftQBFX3DdZ7HHcBAVm-zpWTVsOcvEk78MEsnbSB4Fw3ewhGsUm-yv9TIpma_HiawBiXMplWIbjw_I8T9jWTgU0oaiI2mrdt9ughG_tXXAUwTtE6LC9ePdaRZXLLUe_xpSgfevaR3CcsABqZjJMCbP4gEk-IzUCxtOJ6viMvCvNCU1wIVTkEfqg79Ce_0W29AtR2aGhzlaTrI5kiL7ZkYRmbDSt-qVXxYLQMkMkQcl7eXB2rXu0h50Oe6BY_Jypw7zZdYyhW4MRJY4zef_w.iLO2QETKNORNiq-4ki65qg")

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
        
        ohlcv_payload = {
            "exchange":"NSE",
            "tokens":["2885"]
        }
        ohlcv = easeapi.get_l1_market_quotes(ohlcv_payload)
        print(f"L1 Market Quote Response: {ohlcv}")

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

        # # Modify Existing Order
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
