# Retrieve a Mandate

Retrieves a Mandate object.

## Returns

Returns a Mandate object.

```curl
curl https://api.stripe.com/v1/mandates/mandate_1MvojA2eZvKYlo2CvqTABjZs \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "mandate_1MvojA2eZvKYlo2CvqTABjZs",
  "object": "mandate",
  "customer_acceptance": {
    "accepted_at": 123456789,
    "online": {
      "ip_address": "127.0.0.0",
      "user_agent": "device"
    },
    "type": "online"
  },
  "livemode": false,
  "multi_use": {},
  "payment_method": "pm_123456789",
  "payment_method_details": {
    "sepa_debit": {
      "reference": "123456789",
      "url": ""
    },
    "type": "sepa_debit"
  },
  "status": "active",
  "type": "multi_use"
}
```
