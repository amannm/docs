# Retrieve a value list

Retrieves a `ValueList` object.

## Returns

Returns a `ValueList` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/radar/value_lists/rsl_1MrQSwLkdIwHu7ixWOGS5c8M \
  -u "<<YOUR_SECRET_KEY>>"
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
  "name": "Custom IP Blocklist"
}
```
