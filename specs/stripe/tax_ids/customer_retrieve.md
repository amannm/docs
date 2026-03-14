# Retrieve a Customer tax ID

Retrieves the `tax_id` object with the given identifier.

## Returns

Returns a `tax_id` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids/txi_1MoC8zLkdIwHu7ixEhgWcHzJ \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
  "object": "tax_id",
  "country": "DE",
  "created": 1679431857,
  "customer": "cus_NZKoSNZZ58qtO0",
  "livemode": false,
  "type": "eu_vat",
  "value": "DE123456789",
  "verification": {
    "status": "pending",
    "verified_address": null,
    "verified_name": null
  }
}
```
