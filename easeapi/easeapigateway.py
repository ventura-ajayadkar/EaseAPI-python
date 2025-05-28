import csv
import logging
from datetime import datetime
from urllib.parse import urljoin

import requests
from six import StringIO, PY2
import hashlib

import easeapi.exceptions as ex

log = logging.getLogger(__name__)


class EaseApiGateway:
    """
    The EaseApiGateway API wrapper class.

    In production, you may initialise a single instance of this class per `app_key`.
    """

    _default_root_uri = "https://easeapi.venturasecurities.com"
    _default_login_uri = f"{_default_root_uri}/auth/v1/login"
    _default_timeout = 7  # In seconds

    _routes = {
        "get_sso_url": f"{_default_root_uri}/auth/v1/login",
        "generate_auth_token": f"{_default_root_uri}/login/v1/authorization/token",
        "get_instruments": f"{_default_root_uri}/instrument/v1/instruments",
        "get_fund_details": f"{_default_root_uri}/user/v1/fund_details",
        "get_user_profile": f"{_default_root_uri}/user/v1/profile",
        "logout": f"{_default_root_uri}/user/v1/logout",
        "get_order_book": f"{_default_root_uri}/trade/v1/orders",
        "order_history": f"{_default_root_uri}/trade/v1/order_history",
        "place_delivery_order": f"{_default_root_uri}/trade/v1/delivery",
        "place_intraday_regular_order": f"{_default_root_uri}/trade/v1/intraday/regular",
        "place_intraday_cover_order": f"{_default_root_uri}/trade/v1/intraday/cover",
        "place_delivery_derivative_order": f"{_default_root_uri}/trade/v1/delivery",
        "place_intraday_derivative_regular_order": f"{_default_root_uri}/trade/v1/intraday/regular",
        "place_intraday_derivative_cover_order": f"{_default_root_uri}/trade/v1/intraday/cover",
        "modify_order": f"{_default_root_uri}/trade/v1/modify",
        "cancel_order": f"{_default_root_uri}/trade/v1/cancel",
        "get_tradebook": f"{_default_root_uri}/trade/v1/trades",
        "get_holdings": f"{_default_root_uri}/portfolio/v1/holdings",
        "get_positions": f"{_default_root_uri}/portfolio/v1/positions",
    }

    def __init__(
        self,
        app_key,
        root=None,
        debug=False,
        timeout=None,
        disable_ssl=False,
    ):
        """
        Initialise a new EaseApi Connect client instance.

        - `app_key` is the key issued to you
        - `root` is the API end point root. Unless you explicitly
        want to send API requests to a non-default endpoint, this
        can be ignored.
        - `debug`, if set to True, will serialize and print requests
        and responses to stdout.
        - `timeout` is the time (seconds) for which the API client will wait for
        a request to complete before it fails. Defaults to 7 seconds
        - `disable_ssl` disables the SSL verification while making a request.
        If set requests won't throw SSLError if its set to custom `root` url without SSL.
        """
        self.debug = debug
        self.app_key = app_key
        self.disable_ssl = disable_ssl

        self.root = root or self._default_root_uri
        self.timeout = timeout or self._default_timeout

        self.client_id = None
        self.auth_token = None
        self.refresh_token = None

        # Create requests session by default
        # Same session to be used by pool connections
        self.reqsession = requests.Session()

        # disable requests SSL warning
        requests.packages.urllib3.disable_warnings()

    def set_client_id(self, client_id):
        """Set the `client_id`."""
        self.client_id = client_id

    def set_auth_token(self, auth_token):
        """Set the `auth_token` received after a successful authentication."""
        self.auth_token = auth_token

    def set_refresh_token(self, refresh_token):
        """Set the `refresh_token` received after a successful authentication."""
        self.refresh_token = refresh_token

    def get_sso_url(self, state_variable):
        sso_url = (
            f"{self._default_login_uri}?app_key={self.app_key}&state={state_variable}"
        )
        return sso_url

    def generate_auth_token(self, request_token, secret_key):
        concatenated_keys = self.app_key + secret_key
        hash_object = hashlib.sha256(concatenated_keys.encode("utf-8"))
        hash_hex = hash_object.hexdigest().lower()
        payload = {
            "request_token": request_token,
            "data": hash_hex,
        }
        response = self._post("generate_auth_token", params=payload, is_json=True)
        auth_token = response.get("auth_token")
        refresh_token = response.get("refresh_token")
        return auth_token, refresh_token

    def get_instruments(self):
        return self._parse_instruments(self._get("get_instruments"))

    def get_user_profile(self):
        return self._get("get_user_profile")

    def get_fund_details(self):
        return self._get("get_fund_details")

    def get_orderbook(self):
        return self._get("get_order_book", is_json=False)

    def get_order_history(self, order_id):
        payload = {
            "order_id": order_id,
        }
        return self._post("order_history", params=payload, is_json=True)

    def place_delivery_order(self, payload):
        return self._post("place_delivery_order", params=payload, is_json=True)

    def place_intraday_regular_order(self, payload):
        return self._post("place_intraday_regular_order", params=payload, is_json=True)

    def place_intraday_cover_order(self, payload):
        return self._post("place_intraday_regular_order", params=payload, is_json=True)

    def place_delivery_derivative_order(self, payload):
        return self._post(
            "place_delivery_derivative_order", params=payload, is_json=True
        )

    def place_intraday_derivative_regular_order(self, payload):
        return self._post(
            "place_intraday_derivative_regular_order",
            params=payload,
            is_json=True,
        )

    def modify_order(self, payload):
        return self._post("modify_order", params=payload, is_json=True)

    def cancel_order(self, payload):
        return self._post("cancel_order", params=payload, is_json=True)

    def get_tradebook(self):
        return self._get("get_tradebook")

    def get_holdings(self):
        return self._get("get_holdings")

    def get_positions(self):
        return self._get("get_positions")

    def logout(self, payload):
        payload = {
            "refresh_token": self.refresh_token,
        }
        return self._post("logout", params=payload, is_json=True)

    def _get(self, route, url_args=None, params=None, is_json=False):
        """Alias for sending a GET request."""
        return self._request(
            route, "GET", url_args=url_args, params=params, is_json=is_json
        )

    def _post(
        self, route, url_args=None, params=None, is_json=False, query_params=None
    ):
        """Alias for sending a POST request."""
        return self._request(
            route,
            "POST",
            url_args=url_args,
            params=params,
            is_json=is_json,
            query_params=query_params,
        )

    def _request(
        self,
        route,
        method,
        url_args=None,
        params=None,
        is_json=False,
        query_params=None,
        is_complete_url=True,
    ):
        """Make an HTTP request."""
        if url_args:
            uri = self._routes[route].format(**url_args)
        else:
            uri = self._routes[route]

        if not is_complete_url:
            url = urljoin(self.root, uri)
        else:
            url = uri

        # Custom headers
        headers = {"User-Agent": "EaseApi-python/1.0.0", "X-EaseApi-Version": "1"}
        if self.app_key:
            headers["x-app-key"] = self.app_key

        if self.client_id:
            headers["x-client-id"] = self.client_id

        if self.auth_token:
            headers["Authorization"] = "Bearer {}".format(self.auth_token)

        if self.debug:
            log.debug(
                "Request: {method} {url} {params}".format(
                    method=method, url=url, params=params
                )
            )

        # prepare url query params
        if method in ["GET", "DELETE"]:
            query_params = params

        try:
            r = self.reqsession.request(
                method,
                url,
                json=params if (method in ["POST", "PUT"] and is_json) else None,
                data=params if (method in ["POST", "PUT"] and not is_json) else None,
                params=query_params,
                headers=headers,
                verify=not self.disable_ssl,
                allow_redirects=True,
                timeout=self.timeout,
            )
        except Exception as e:
            raise e

        if self.debug:
            log.debug(
                "Response: {code} {content_type}".format(
                    code=r.status_code, content_type=r.headers["content-type"]
                )
            )

        # Validate the content type.
        if "json" in r.headers["content-type"]:
            try:
                data = r.json()
            except ValueError:
                raise ex.DataException(
                    "Couldn't parse the JSON response received from the server: {content}".format(
                        content=r.content
                    )
                )

            if (
                data is not None
                and "session_expired" in data
                and data["session_expired"]
            ):
                # Call session hook if its registered as session is expired
                if self.session_expiry_hook:
                    self.session_expiry_hook()
                raise ex.AuthTokenException(data["message"], r.status_code)

            return data
        elif "csv" in r.headers["content-type"]:
            return r.content
        else:
            raise ex.DataException(
                "Unknown Content-Type ({content_type}) with response: ({content})".format(
                    content_type=r.headers["content-type"], content=r.content
                )
            )

    def _parse_instruments(self, data):
        d = data
        # Decode unicode data
        if not PY2 and type(d) == bytes:
            d = data.decode("utf-8").strip()

        records = []
        reader = csv.DictReader(StringIO(d))

        for row in reader:
            row["exchange_token"] = int(row["exchange_token"])
            row["last_price"] = float(row["last_price"])
            row["tick_size"] = float(row["tick_size"])
            row["lot_size"] = int(row["lot_size"])

            # # Parse date
            if len(row["expiry"]) == 10:
                row["expiry"] = datetime.strptime(row["expiry"], "%d/%m/%Y").date()

            records.append(row)

        return records
