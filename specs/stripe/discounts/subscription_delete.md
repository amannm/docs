# Delete a subscription discount

Removes the currently applied discount on a subscription.

## Returns

An object with a deleted flag set to true upon success. This call returns [an error](subscription_delete.md#errors) otherwise, such as if no discount exists on this subscription.

```curl
curl -X DELETE https://api.stripe.com/v1/subscriptions/sub_1NlcNX2eZvKYlo2CFqnrn9ow/discount \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "discount",
  "deleted": true
}
```
