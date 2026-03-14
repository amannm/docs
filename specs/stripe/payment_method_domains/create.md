# Create a payment method domain

Creates a payment method domain.

## Returns

Returns a payment method domain object.

## Parameters

- `domain_name` (string, required)
  The domain name that this payment method domain object represents.

- `enabled` (boolean, optional)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

```curl
curl https://api.stripe.com/v1/payment_method_domains \
  -u "<<YOUR_SECRET_KEY>>" \
  -d domain_name="example.com"
```

### Response

```json
{
  "id": "pmd_1Nnrer2eZvKYlo2Cips79tWl",
  "object": "payment_method_domain",
  "apple_pay": {
    "status": "active"
  },
  "created": 1694129445,
  "domain_name": "example.com",
  "enabled": true,
  "google_pay": {
    "status": "active"
  },
  "link": {
    "status": "active"
  },
  "livemode": false,
  "paypal": {
    "status": "active"
  }
}
```
