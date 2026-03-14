# Delete a Customer tax ID

Deletes an existing `tax_id` object.

## Returns

Returns an object with a deleted parameter on success. If the `tax_id` object does not exist, this call raises [an error](customer_delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids/txi_1MoC8zLkdIwHu7ixEhgWcHzJ \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",
  "object": "tax_id",
  "deleted": true
}
```
