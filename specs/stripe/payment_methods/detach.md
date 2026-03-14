# Detach a PaymentMethod from a Customer

Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.

## Returns

Returns a PaymentMethod object.

```curl
curl -X POST https://api.stripe.com/v1/payment_methods/pm_1MqLiJLkdIwHu7ixUEgbFdYF/detach \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",
  "object": "payment_method",
  "billing_details": {
    "address": {
      "city": null,
      "country": null,
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "email": null,
    "name": null,
    "phone": null
  },
  "card": {
    "brand": "visa",
    "checks": {
      "address_line1_check": null,
      "address_postal_code_check": null,
      "cvc_check": "unchecked"
    },
    "country": "US",
    "exp_month": 8,
    "exp_year": 2026,
    "fingerprint": "mToisGZ01V71BCos",
    "funding": "credit",
    "generated_from": null,
    "last4": "4242",
    "networks": {
      "available": [
        "visa"
      ],
      "preferred": null
    },
    "three_d_secure_usage": {
      "supported": true
    },
    "wallet": null
  },
  "created": 1679945299,
  "customer": null,
  "livemode": false,
  "metadata": {},
  "type": "card"
}
```
