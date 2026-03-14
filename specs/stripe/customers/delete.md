# Delete a customer

Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.

## Returns

Returns an object with a deleted parameter on success. If the customer ID does not exist, this call raises [an error](delete.md#errors).

Unlike other objects, deleted customers can still be retrieved through the API in order to be able to track their history. Deleting customers removes all credit card details and prevents any further operations to be performed (such as adding a new subscription).

```curl
curl -X DELETE https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "cus_NffrFeUfNV2Hib",
  "object": "customer",
  "deleted": true
}
```
