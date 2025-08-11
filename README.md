# 🚀 EaseAPI Python SDK

[![PyPI version](https://badge.fury.io/py/ventura-easeapi.svg)](https://badge.fury.io/py/ventura-easeapi)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> The official Python client for communicating with [EaseAPI](https://www.venturasecurities.com/easeapi/) - Your gateway to complete investment and trading solutions.

## ✨ Features

- 🔐 Secure authentication flow
- 📊 Real-time order execution
- 💼 Portfolio management
- 📈 Market data access
- 🔄 Order modification and cancellation
- 📱 User profile management

## 📦 Installation

> 🔜 Coming Soon! The EaseAPI SDK will be available on PyPI shortly.
> 
> Once published, you'll be able to install it using:
```bash
pip install ventura-easeapi
```

## 🚀 Quick Start

1. **Register for API Keys**
   - Visit [EaseAPI Portal](https://easeapi.venturasecurities.com/portal)
   - Create an account and obtain your `app_key` and `secret_key`

2. **Initialize the SDK**

```python
from easeapi import EaseApiGateway

easeapi = EaseApiGateway(
    app_key="YOUR_APP_KEY",
    disable_ssl=False,
    debug=False
)
```

## 🔑 Authentication Flow

```python
# Step 1: Generate SSO URL
sso_url = easeapi.get_sso_url(state_variable="STATE_VARIABLE")
print(f"Open this URL in browser: {sso_url}")

# Step 2: Generate auth token
response = easeapi.generate_auth_token(
    request_token="YOUR_REQUEST_TOKEN",
    secret_key="YOUR_SECRET_KEY"
)

client_id = response.get("client_id", None)
auth_token = response.get("auth_token", None)
refresh_token = response.get("refresh_token", None)

# Step 3: Set credentials
easeapi.set_client_id(client_id=client_id)
easeapi.set_auth_token(auth_token=auth_token)
easeapi.set_refresh_token(refresh_token=refresh_token)
```

## 🔑 Authentication Flow Using TOTP

```python
# Step 1: Generate auth token using TOTP
response = easeapi.generate_auth_token_with_otpt(
    client_id="YOUR_CLIENT_ID", password="YOUR_PIN", totp="YOUR_TOTP", secret_key="YOUR_SECRET_KEY"
)

client_id = response.get("client_id", None)
auth_token = response.get("auth_token", None)
refresh_token = response.get("refresh_token", None)

# Step 2: Set credentials
easeapi.set_client_id(client_id=client_id)
easeapi.set_auth_token(auth_token=auth_token)
easeapi.set_refresh_token(refresh_token=refresh_token)
```



## 💡 Usage Examples

### 👤 Get User Profile
```python
user_profile = easeapi.get_user_profile()
print(f"User Profile Data:\n {user_profile}")
```

### 📈 Place Delivery Order
```python
response = easeapi.place_delivery_order({
    "instrument_id": 2885,
    "exchange": "NSE",
    "segment": "E",
    "transaction_type": "B",
    "order_type": "MKT",
    "quantity": 1,
    "price": 1224.0,
    "product": "C",
    "validity": "DAY"
})
```

## 📚 Documentation

For detailed API documentation and more examples:
- [EaseAPI Documentation](https://easeapi.venturasecurities.com/docs)
- [Sample Code](run_apis.py)

## 🧪 Running Examples

```bash
python run_apis.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐️ If you find this SDK helpful, please consider giving it a star on GitHub!

_Built with ❤️ by Engineering at [Ventura Securities Ltd.](https://www.ventura1.com)_
