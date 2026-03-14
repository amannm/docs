# Retrieve a Session

Retrieves the details of a Financial Connections `Session`

## Returns

Returns a `Session` object if a valid identifier was provided, and raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/financial_connections/sessions/fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "fcsess_1MwtnGLkdIwHu7ixs7NPQ7dq",
  "object": "financial_connections.session",
  "account_holder": {
    "customer": "cus_NiKSWdaFz2F6I0",
    "type": "customer"
  },
  "accounts": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/financial_connections/accounts"
  },
  "client_secret": "fcsess_client_secret_KRJTKvCY3IKoYTrW18EazcO3",
  "filters": {
    "countries": [
      "US"
    ]
  },
  "livemode": false,
  "permissions": [
    "balances",
    "payment_method"
  ]
}
```
