import logging
from easeapi.easeapigateway import EaseApiGateway
from example import ExampleApi


logging.basicConfig(level=logging.DEBUG)


def main():
    """
    Initialize EaseApiGateway with your app_key.
    This app_key and secret_key can be obtained by registering at https://easeapi.venturasecurities.com/portal
    """
    easeapi = EaseApiGateway(app_key="XlphUa8S3GPEDKt8v8op", disable_ssl=False, debug=False)

    example_api = ExampleApi()

    # Step 1 :  call this SSO URL in browser and complete the SSO flow
    example_api.sso_url(easeapi)

    # Step 2 :  generate 'auth_token' from request_token received from SSO flow from step 1
    #           this request token is generated on successful login; valid for 10 minutes.
    #           you can find the 'secret_key' by login in your EaseAPI Portal at https://easeapi.venturasecurities.com/portal
    # example_api.auth_token(easeapi, request_token="xJwUt3eIRn", secret_key="JVLcV3E7TT")

    # Step 3 :  set client_id, auth_token, refresh_token received in step 2 after successful login.
    easeapi.set_client_id("AA0605")
    easeapi.set_auth_token("eyJraWQiOiJlMDc0TUpqYnJLTXhEU3lSN2tWY25xY0x1TXFhUG92TlBNQ0FKM0VwRTBFPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI4MGNjZmVjZC0yODg3LTRmOWQtYTMwMS05ZDlkNWI5M2FjMmQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX0ZUc1JPTmNWYSIsImNsaWVudF9pZCI6IjczaTNodXVsbGllYzkzMHZobjZzbGo0YWs4Iiwib3JpZ2luX2p0aSI6IjA1MjBjMGMwLTE0ODEtNDlhOS05NjZlLTM3ODJlYjA4NWNmMCIsImV2ZW50X2lkIjoiZTNmNjMxYjMtMmI3Ni00ZGVkLTk4NWUtMWE0OTY5ZjhmZTQyIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0ODQwNjIwNCwiZXhwIjoxNzQ4NDkyNjA0LCJpYXQiOjE3NDg0MDYyMDQsImp0aSI6IjljYjlmNzEwLTA0MjEtNDBhMi04NTZhLWEzNjFlNjFmMDljMSIsInVzZXJuYW1lIjoiYWEwNjA1In0.L0dH1jBFwWfyZzLmOiF7BxQptSKzwN0NKRMIYtfjzZu67NSSIsneYjMTXNPv8ivhNTzMH_cUOKcb1xDk-3kD99gjgFk3jTYqOXJR7sfi6BkH7aYKyTu-_J6OmOOa_4texjVzMNlI1F-RaIjGbItTKQqyNdi1a2XEx4n2_crUPyXdeIb88KC7VsgG05iY6UWoSd8BtXsbmFrwbMCEWiSP-gO_DzPBCPbxQCXYAQKJid6kXSbmb6wpzyArwOFZmx1ky1GUOktzPwIcLQOC2Y3cCbgR49o5vgka6uqhAJlmSjQAXhIXRf2A-vCyVy90v4w213fDXtG1H3NTawhKg_4k2w")
    easeapi.set_refresh_token("eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.pkA3GMFCawAQoTxRL_EKZgG1ekKJqUIYJKYFtpvmzcjdWVRiDFC7eHtiJmGOC_ul9bC3TUB4o6mTzT-uCJtX84jdd8taGCZgzPa_yapZ7Wkiqn-PFABGRjKWuFZPdVkAxfhQugiCiYQ5O2KglYfc0IUr_54Q023-CvTAQSyIarYUamPSLFaEZ1et8YkBvq_rKfb8uziA2-ntMjdimYRV-2r658bJ7xlnSkALxv0jL5QJgWRLwQp-KGhdHx6pH6ay1Zus69SWIjzAuNhds_QixQjp2frIiuvjvFl00tJu8GGzZUfaBuCaGLAjDXZPK-Ky1rWlWAh3raJSOpQSuQa28Q.lCHCtoTkzJPM2B7I.sECMGsGAhKXEnfazeJzDDgWiKpSY6_3T1vlW1rJh8kgb2_cXdQ-XTRD0lVnQr6sWDtE4B8EcbiA4t2DaKXWQTz3JdNGMrskQL7jCE6yjSDXIjEEG4GW7CnC09AsWhK4jSLBL8WEsruGxDHWjJ67HvDu2dia9Kr2ALPq4LbEcyWiuKMb2zePtXRjFmhx5mVc2FyPXsrhAO8MT2_dWbSQiHU9ArptfZN0YYnSI5MBIJy9GmbMd1rKWbASIQbuuchmrQbTWErbse99NhtCzqtfOm3rT-kLEok1FqpreZrzCbvOAKqAScbZ4AVkfQGTRUNzE0Pb1rrE8bFbmdk6_nIqxHwPENe1_Ajyzjp1PZMnayejvIomVtIH3OE4KDB1951AbjHa-OCjeYBwp1XxgRZCBesofZCWHvFpXlVAWnF7DP9M4eAeMNQFp-eUkVSozQ1MtIJ4rSuHMn-cYp_RXg7utmtkQXRLZqTzQR3NbgIanNKiKa39JRZRa2xHft4btn6jJK4hG2cst7iA9JowpyYXNtee1PcqTMeNF9YUfLN6VSu9ZsVlgc_eOJxPCEpuLsDSOO1rTYQBy2oCRrtIMaxc23QisgvKTrUGe8zCaPfgOcjA7oY8m-vmN03Ouz55Qq-YbHG-hcPAldzOtg0TN3T1x9fBJaNh1UJdL3uJFbEoW3D9qa5yG37Bk3FjKjyuS9CNTl-sqWOC_dC7xDFD2To-7_pvHt2QALkJQr02_vOy5ZHrtWKmCXH-qav0TPUrrAMRHUdrUnttHL31quK8fhXhH8qfAdN9VxWQ1UHTGwWcsWL-eZMrTDFjPLyDIT79V7AvER6-jVCwJyM9l04fXLs9iinvnfrTgC2cttOXGKLsgLvytWfVy7DjVm3ujgVkEMJq9cjdqvvOhobcpf2Ti_I6xHi8qiGSSyoKttnFttpN7Qmigs89s5SkCitbOAxv06pjY749wkUc9B3jUWONZ5xGzeXi5ZJxtw_Bj4oU1Xy-pU8jxldwATnOsaMLx1UE1bVwWBrdG452OKSB95SML2rbtXoaYRdtuE1pg86Cl4YP3Jb5crSswrBsAj1KP1pQ7iGqquwxlpksjNv2f5TvpJ-QzUT9HNn46fVUyyw8jqoRYgGcOa0S4FBuWWWfFaGuw_I0QVmum7u1HMtG0DqX_y3dsIKlz0KVCX815uzbO4IaHr4cgJx_haeI9fko66P6zY3CqF-PrjPzaBvx2R_3oFgUA1ibpZhHU4TGeRaZurJrzenAWWXBs2e4V10ZAg5dxjrDCRFbjfbYZYw.DxKq1CLG-gFuSVATnWz8YQ")

    # example_api.instruments(easeapi)
    # example_api.user_profile(easeapi)
    example_api.fund_details(easeapi)

    example_api.tradebook(easeapi)
    example_api.orderbook(easeapi)

    # example_api.place_delivery_order(easeapi)
    # example_api.place_intraday_regular_order(easeapi)
    # example_api.place_intraday_cover_order(easeapi)
    # example_api.place_intraday_derivative_regular_order(easeapi)
    # example_api.place_delivery_derivative_order(easeapi)
    example_api.modify_order(easeapi)
    # example_api.cancel_order(easeapi)
    example_api.holdings(easeapi)
    example_api.positions(easeapi)
    # example_api.logout(easeapi)


if __name__ == "__main__":
    main()
