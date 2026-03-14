# Retrieve a credit grant

Retrieves a credit grant.

## Returns

Returns a credit grant.

## Parameters

- `id` (string, required)
  Unique identifier for the object.

```curl
curl https://api.stripe.com/v1/billing/credit_grants/credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "credgr_test_61R9a6NUWsRmOW3RM41L6nFOS1ekDGHo",
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
  "created": 1726620803,
  "customer": "cus_QrvQguzkIK8zTj",
  "effective_at": 1729297860,
  "expires_at": null,
  "livemode": false,
  "metadata": {},
  "name": "Purchased Credits",
  "priority": 50,
  "test_clock": null,
  "updated": 1726620803
}
```
