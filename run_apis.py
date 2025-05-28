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
        easeapi.set_auth_token("eyJraWQiOiJmWTdRYVhEYlR6TGtwYXlzMWR1Qk1kTHViSzFHcWlhZnlGd1RQWFQ1V1dZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI5NTg4MTg4Yy0yZWYxLTQ1MzktYWM0NC1kZmU1NzY4OGQyNTAiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX3Njc1VQdFM1QiIsImNsaWVudF9pZCI6IjUwdWVjOXJwN241cGVjaDliaDIxcTU3N3RjIiwib3JpZ2luX2p0aSI6Ijc5NTA2M2IxLWMzOWYtNDZjNi04NDFmLTdlMmFhNmJiNTdhYSIsImV2ZW50X2lkIjoiNmFkZTJmYjUtODM5Zi00NmVjLTgxNjQtN2MzODMyZWY3ZmIzIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0MDQ2Mjc0NSwiZXhwIjoxNzQwNTQ5MTQ1LCJpYXQiOjE3NDA0NjI3NDUsImp0aSI6IjY5NWU0NGUyLTY2MjItNGQzMi1hZGQwLTEzNjk0ZTlmMzEwMSIsInVzZXJuYW1lIjoiYWEwNjA1In0.boFJN0mV2cxya7T_P5zrbcaJpVuMbsIgLZLf8uio-klgyC2I3zXq_LgAeabw_hpxbl-D7G_sARfQp1oldQsKONrctqdufv-WO40tVOc6-FNwnJa4WQBWmKxGh9QJPh1q1aIspQwAxgzOG8xGPqrC1GP7PCFGUWPgbJUJeS0jWgDCfq3iPFtprL4B-aDePxncgR4nkIWbO3ycQJLNoR61g6dHMHskWEztv-nX_hXzScixW7iFSA5mH9lFUkkjPVcLjih64MXIsRCsfsbo6y4LnpyrhZbJT4hHKQwpozumK148bWhrblDofSmvt_NYd8w0DOMc-PyEoMa4cb0QI-2WhA")
        easeapi.set_refresh_token("eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.YdQlKhaTMU8EqKPw-s6c1fMGS6SoQkmqRs6m-Nh7rATg_LG-5G9sv2Br3XWZlJ2iLZrsD9j9PTW2N9JfckZlJLDHIW-qHc6J51gZ5IYdt48QdzRtjLNnNYnqMRw0ZubIr0jLuYRDaWlaNThmtGWhsvCKHAVNuq0F8gsrUoHXhnCFBu5i3ojByDUibE_HGF6QJlmwPI4amzdCtN-trVHQUVimx9E86JW8Smin5q9eRehhgd2Rkf4is-dCSHKtkcyN0Ra0_7PiMZp61jgqGZBSFTM97AZu-_mnGniqkFl8jIuwEJcezNu4-MlucWp5f1rj4lBL-eM_b8pwQew5mwD1QA.LwSiwTWKGPEGUUhB.X7CGwwYPZXOGONdEacYDs1TtYH5i48grucG-4fky12bEkcOSTHkPvoWQD7aIePth2eImPHGxQ4XueR8HglHWTjSQ-8rU0J93sllsTgLL6Y5EAmqhR7Ojy7d0LTuLET7nInPMzMVBPHEwabXeF8DLWJrcIEOmITZi1K9JK9NdkLvq2p0IStEHJyUaSgxSHuifZGEtVDUSdBNwByxkQEehA6uVjI4VwcFwU-25PAozgswRPWpyoRRPgB0lvZ5g2aY896u6czGFSiUEoRepmzi1xvYO5XAoeyECcT1sdOespKGESJSTKVDHN8pgxzWx6IkWjmJvFap0pr-S48dCLpCY_Qej824KYgxsIAvtV4oNrzb5MyYGU8-uHetlx-Kyb6JtDUPOo70g0mgo8wwl6K-9h5LkAc3M6NY72W6YjgLzFMVTuPuPT2YHMVwmxzjijsFD9bkIHLU2Oji8qBMWKddqJiufP2Vtb4-0149XBAIBizuSeq2PRzSDoIsH3Y0fLi8bodzAqdV_9DrvdyhhRSxFJQMzt-0gGx_fHpq7X_8xgYVqIZdQfoS9bnJP81FdAeI86fp2dpABh8d8Jc8P9wI_VAyvPabmdZQpGbzM1sg1tlnxRcMW3XYweRHbLKR5uqXOjdYVshtugNJKKSlYzsiSCSNTZehZnlVUfN-jelmtT6rd0QOgeOwuKsNRmaFNXEq6cgEniVS3aqiqo9xb8Etw8KmilGYCjmS0i_Qqc6dP1_Ofs-viyHzeB99dxc_j3btvVBNlU0mC6KdtDAyLMIzlOZYwPal1kzJygpgEFx32hQ8jiQ3Nvi8TEkoZbZ5UvwV3Zj_1jZk5WMsSh7nD_7tW8drYp8ZPI1iYCD4aHANu1ecJl35iwGmFwhlqaVKke68--4xxgSnoaAsUvjddSm37WltBYMIkd2Tl_XUsttMj_We5zaxINLvnJ0xrybvx5UVhF7_5NfYUZXSIJO0gTxPOiarE77WlCv00cHMBr8yod0vya21GRUSS5fHSW31_GcObqRW8or8t_5ge-Ji9BXCfmfe7R_LTk3lQMDT0djbkUiwT4B6taQibQZKsDaOoCL-24SgT1owbhqxUpN5bqSk9ZcDvULLooeBVfIkrEOe5iS5K-URplUn2cd6fpgUaRqFuhf9Pgi-ZtOMoH6DgqLw7eS8js3qwHpkzLoxosQlNqGLUz36NVqAS2E0m3X02c7u2wJvn-UU8LFV9sBF6NfdYMuy-ol7cd6oA-NzJL8m3akEtmdrgBnOWzijfup6gYmDRXBkZencCBg.Nm4LJ_tzk0t1Wq7tSeACjw")

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
