# Retrieve an issuing token

Retrieves an Issuing `Token` object.

## Returns

Returns an Issuing `Token` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/issuing/tokens/intok_1MzDbE2eZvKYlo2C26a98MDg \
  -u "<<YOUR_SECRET_KEY>>"
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
  "status": "active",
  "last4": "2424",
  "token_service_provider": "visa",
  "wallet_provider": "apple_pay",
  "device_fingerprint": "intd_1MzDbE2eZvKYcp3095svdf"
}
```
