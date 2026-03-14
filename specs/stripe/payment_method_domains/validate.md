# Validate an existing payment method domain

Some payment methods might require additional steps to register a domain. If the requirements weren’t satisfied when the domain was created, the payment method will be inactive on the domain. The payment method doesn’t appear in Elements or Embedded Checkout for this domain until it is active.

To activate a payment method on an existing payment method domain, complete the required registration steps specific to the payment method, and then validate the payment method domain with this endpoint.

Related guides: [Payment method domains](https://docs.stripe.com/docs/payments/payment-methods/pmd-registration.md).

## Returns

Returns the updated payment method domain object.

```curl
curl -X POST https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl/validate \
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
