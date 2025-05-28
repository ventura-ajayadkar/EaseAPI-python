# EaseAPI 1.0.0 Python client

The official Python client for communicating with [EaseAPI](https://easeapi.venturasecurities.com).

The EaseAPI provides a comprehensive set of APIs that expose many capabilities required to build a complete investment and trading platform. Execute orders in real-time, manage user portfolios, and more, with the simple HTTP API collection.

## Documentation

- [EaseAPI - HTTP API documentation](https://easeapi.venturasecurities.com/docs)

## Run Sample Code

### Step 1 : install library in edit mode

```bash
    pip install -e .
```

### Step 2 : run example

```bash
    python ./example/run_apis.py
```

## API usage

```python
    """
    Initialize EaseApiGateway with your app_key.
    This app_key and secret_key can be obtained by registering at https://easeapi.venturasecurities.com/portal
    """
    easeapi = EaseApiGateway(
        app_key="YOUR_APP_KEY", disable_ssl=False, debug=False
    )

    example_api = ExampleApi()

    # Step 1 :  call this SSO URL in browser and complete the SSO flow
    example_api.sso_url(easeapi)

    # Step 2 :  generate 'auth_token' from request_token received from SSO flow from step 1
    #           this request token is generated on successful login; valid for 10 minutes.
    #           you can find the 'secret_key' by login in your EaseAPI Portal at https://easeapi.venturasecurities.com/portal
    example_api.auth_token(easeapi, request_token="REQUEST_TOKEN", secret_key="YOUR_SECRET_KEY")

    # Step 3 :  set client_id, auth_token, refresh_token received in step 2 after successful login.
    easeapi.set_client_id("YOUR_CLIENT_ID")
    easeapi.set_auth_token("GENERATED_AUTH_TOKEN")
    easeapi.set_refresh_token("GENERATED_REFRESH_TOKEN")

    example_api.place_delivery_order(easeapi)
    example_api.modify_order(easeapi)
    example_api.cancel_order(easeapi)
    example_api.order_history(easeapi)

```

For more details, take a look at **example.py** and **run_apis.py** in the example directory.
