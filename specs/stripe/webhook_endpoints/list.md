# List all webhook endpoints

Returns a list of your webhook endpoints.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` webhook endpoints, starting after webhook endpoint `starting_after`. Each entry in the array is a separate webhook endpoint object. If no more webhook endpoints are available, the resulting array will be empty. This request should never raise an error.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/webhook_endpoints \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/webhook_endpoints",
  "has_more": false,
  "data": [
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
  ]
}
```
