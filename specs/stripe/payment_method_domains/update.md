# Update a payment method domain

Updates an existing payment method domain.

## Returns

Returns the updated payment method domain object.

## Parameters

- `enabled` (boolean, optional)
  Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

```curl
curl https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \
  -u "<<YOUR_SECRET_KEY>>" \
  -d enabled=false
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
  "enabled": false,
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
