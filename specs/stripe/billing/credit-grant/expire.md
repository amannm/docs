# Expire a credit grant

Expires a credit grant.

## Returns

Returns the expired credit grant.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

```curl
curl -X POST https://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim/expire \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "credgr_test_61R9rm9vto9SMMvt041L6nFOS1ekDCim",
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
  "created": 1726688741,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688741,
  "expires_at": 1726688796,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688796,
  "voided_at": null
}
```
