# Create a value list item

Creates a new `ValueListItem` object, which is added to the specified parent value list.

## Returns

Returns a `ValueListItem` object if creation succeeds.

## Parameters

- `value` (string, required)
  The value of the item (whose type must match the type of the parent value list).

  The maximum length is 800 characters.

- `value_list` (string, required)
  The identifier of the value list which the created item will be added to.

```curl
curl https://api.stripe.com/v1/radar/value_list_items \
  -u "<<YOUR_SECRET_KEY>>" \
  -d value_list=rsl_1MxxosLkdIwHu7ixNiiD01Kj \
  -d value="1.2.3.4"
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
