# Increment a test-mode authorization

Increment a test-mode Authorization.

## Returns

An Authorization object

## Parameters

- `increment_amount` (integer, required)
  The amount to increment the authorization by. This amount is in the authorization currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

- `is_amount_controllable` (boolean, optional)
  If set `true`, you may provide [amount](https://docs.stripe.com/docs/api/issuing/authorizations/approve.md#approve_issuing_authorization-amount) to control how much to hold for the authorization.

```curl
curl https://api.stripe.com/v1/test_helpers/issuing/authorizations/iauth_1DPc772eZvKYlo2C6avLyZ25/increment \
  -u "<<YOUR_SECRET_KEY>>" \
  -d increment_amount=1000
```

### Response

```json
{
  "id": "iauth_1DPc772eZvKYlo2C6avLyZ25",
  "object": "issuing.authorization",
  "amount": 1000,
  "amount_details": {
    "atm_fee": null,
    "cashback_amount": null
  },
  "approved": true,
  "authorization_method": "keyed_in",
  "balance_transactions": [],
  "card": "ic_1Nsse72eZvKYlo2CWBGm2WQ5",
  "cardholder": "ich_1Ccy6F2eZvKYlo2ClnIm9bs4",
  "created": 1540586461,
  "currency": "usd",
  "livemode": false,
  "merchant_amount": 0,
  "merchant_currency": "usd",
  "merchant_data": {
    "category": "taxicabs_limousines",
    "category_code": "4121",
    "city": "San Francisco",
    "country": "US",
    "name": "Rocket Rides",
    "network_id": "1234567890",
    "postal_code": "94107",
    "state": "CA",
    "terminal_id": null
  },
  "metadata": {},
  "network_data": null,
  "pending_request": null,
  "redaction": null,
  "request_history": [],
  "status": "reversed",
  "transactions": [],
  "verification_data": {
    "address_line1_check": "not_provided",
    "address_postal_code_check": "match",
    "cvc_check": "match",
    "expiry_check": "match"
  },
  "wallet": null
}
```
