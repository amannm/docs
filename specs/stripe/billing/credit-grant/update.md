# Update a credit grant

Updates a credit grant.

## Returns

Returns the updated credit grant.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

- `expires_at` (timestamp, optional)
  The time when the billing credits created by this credit grant expire. If set to empty, the billing credits never expire.

- `metadata` (object, optional)
  Set of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.

```curl
curl https://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[cost_basis]"="0.9" \
  -d expires_at=1759302000
```

### Response

```json
{
  "id": "credgr_test_61R9rpFu8SZkXPTkU41L6nFOS1ekDKoa",
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
  "created": 1726688933,
  "customer": "cus_QsEHa3GKweMwih",
  "effective_at": 1726688933,
  "expires_at": 1759302000,
  "livemode": false,
  "metadata": {
    "cost_basis": "0.9"
  },
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726688977,
  "voided_at": null
}
```
