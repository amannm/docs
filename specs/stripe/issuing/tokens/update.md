# Update a token status

Attempts to update the specified Issuing `Token` object to the status specified.

## Returns

Returns an updated Issuing `Token` object if a valid identifier was provided.

## Parameters

- `status` (enum, required)
  Specifies which status the token should be updated to.
Possible enum values:
  - `active`
    Token is provisioned and usable for payments.

  - `deleted`
    Terminal state. Token can no longer be used.

  - `suspended`
    Token temporarily cannot be used for payments.

```curl
curl https://api.stripe.com/v1/issuing/tokens/intok_1MzDbE2eZvKYlo2C26a98MDg \
  -u "<<YOUR_SECRET_KEY>>" \
  -d status=suspended
```

### Response

```json
{
  "id": "intok_1MzDbE2eZvKYlo2C26a98MDg",
  "object": "issuing.token",
  "card": "ic_1MytUz2eZvKYlo2CZCn5fuvZ",
  "created": 1682059060,
  "network_updated_at": 1682059060,
  "livemode": false,
  "status": "suspended",
  "last4": "2424",
  "token_service_provider": "visa",
  "wallet_provider": "apple_pay",
  "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
}
```
