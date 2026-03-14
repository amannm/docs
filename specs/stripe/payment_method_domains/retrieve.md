# Retrieve a payment method domain

Retrieves the details of an existing payment method domain.

## Returns

Returns a payment method domain object.

```curl
curl https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \
  -u "<<YOUR_SECRET_KEY>>"
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
