# Approve a review

Approves a `Review` object, closing it and removing it from the list of reviews.

## Returns

Returns the approved `Review` object.

```curl
curl -X POST https://api.stripe.com/v1/reviews/prv_1NVyFt2eZvKYlo2CjubqF1xm/approve \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "prv_1NVyFt2eZvKYlo2CjubqF1xm",
  "object": "review",
  "billing_zip": null,
  "charge": null,
  "closed_reason": null,
  "created": 1689864901,
  "ip_address": null,
  "ip_address_location": null,
  "livemode": false,
  "open": true,
  "opened_reason": "rule",
  "payment_intent": "pi_3NVy8c2eZvKYlo2C055h7pkd",
  "reason": "rule",
  "session": null
}
```
