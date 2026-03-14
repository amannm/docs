# Delete a customer discount

Removes the currently applied discount on a customer.

## Returns

An object with a deleted flag set to true upon success. This call returns [an error](delete.md#errors) otherwise, such as if no discount exists on this customer.

```curl
curl -X DELETE https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/discount \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "discount",
  "deleted": true
}
```
