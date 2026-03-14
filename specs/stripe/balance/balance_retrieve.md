# Retrieve balance

Retrieves the current account balance, based on the authentication that was used to make the request. For a sample request, see [Accounting for negative balances](https://docs.stripe.com/docs/connect/account-balances.md#accounting-for-negative-balances).

## Returns

Returns a balance object for the account that was authenticated in the request.

```curl
curl https://api.stripe.com/v1/balance \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "balance",
  "available": [
    {
      "amount": 666670,
      "currency": "usd",
      "source_types": {
        "card": 666670
      }
    }
  ],
  "connect_reserved": [
    {
      "amount": 0,
      "currency": "usd"
    }
  ],
  "livemode": false,
  "pending": [
    {
      "amount": 61414,
      "currency": "usd",
      "source_types": {
        "card": 61414
      }
    }
  ]
}
```
