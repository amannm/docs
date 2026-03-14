# Retrieve a webhook endpoint

Retrieves the webhook endpoint with the given ID.

## Returns

Returns a webhook endpoint if a valid webhook endpoint ID was provided. Raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",
  "object": "webhook_endpoint",
  "api_version": null,
  "application": null,
  "created": 1680122196,
  "description": null,
  "enabled_events": [
    "charge.succeeded",
    "charge.failed"
  ],
  "livemode": false,
  "metadata": {},
  "status": "enabled",
  "url": "https://example.com/my/webhook/endpoint"
}
```
