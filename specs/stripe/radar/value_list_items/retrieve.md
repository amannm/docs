# Retrieve a value list item

Retrieves a `ValueListItem` object.

## Returns

Returns a `ValueListItem` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/radar/value_list_items/rsli_1MxxosLkdIwHu7ixxvA1yKiZ \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "rsli_1MxxosLkdIwHu7ixxvA1yKiZ",
  "object": "radar.value_list_item",
  "created": 1681760074,
  "created_by": "API",
  "livemode": false,
  "value": "1.2.3.4",
  "value_list": "rsl_1MxxosLkdIwHu7ixNiiD01Kj"
}
```
