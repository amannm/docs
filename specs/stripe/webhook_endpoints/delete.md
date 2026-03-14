# Delete a webhook endpoint

You can also delete webhook endpoints via the [webhook endpoint management](https://dashboard.stripe.com/account/webhooks) page of the Stripe dashboard.

## Returns

An object with the deleted webhook endpoints’s ID. Otherwise, this call raises [an error](delete.md#errors), such as if the webhook endpoint has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
  "object": "webhook_endpoint",
  "deleted": true
}
```
