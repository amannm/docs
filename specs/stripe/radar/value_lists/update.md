# Update a value list

Updates a `ValueList` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Note that `item_type` is immutable.

## Returns

Returns an updated `ValueList` object if a valid identifier was provided.

## Parameters

- `alias` (string, optional)
  The name of the value list for use in rules.

  The maximum length is 100 characters.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `name` (string, optional)
  The human-readable name of the value list.

  The maximum length is 100 characters.

```curl
curl https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name="Updated IP Blocklist"
```

### Response

```json
{
  "id": "rsl_1MrQSwLkdIwHu7ixWOGS5c8M",
  "object": "radar.value_list",
  "alias": "custom_ip_blocklist",
  "created": 1680201894,
  "created_by": "API",
  "item_type": "ip_address",
  "list_items": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/radar/value_list_items?value_list=rsl_1MrQSwLkdIwHu7ixWOGS5c8M"
  },
  "livemode": false,
  "metadata": {},
  "name": "Updated IP Blocklist"
}
```
