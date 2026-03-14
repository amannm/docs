# Void a credit grant

Voids a credit grant.

## Returns

Returns the voided credit grant.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

```curl
curl -X POST https://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae/void \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "credgr_test_61R9rnNTDmZ657a2r41L6nFOS1ekD5Ae",
  "object": "billing.credit_grant",
  "amount": {
    "monetary": {
      "currency": "usd",
      "value": 1000
    },
    "type": "monetary"
  },
  "applicability_config": {
    "scope": {
      "price_type": "metered"
    }
  },
  "category": "paid",
  "created": 1726688817,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688817,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688829,
  "voided_at": 1726688829
}
```
