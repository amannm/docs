# List all value lists

Returns a list of `ValueList` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` lists, starting after list `starting_after`. Each entry in the array is a separate `ValueList` object. If no more lists are available, the resulting array will be empty.

## Parameters

- `alias` (string, optional)
  The alias used to reference the value list when writing rules.

  The maximum length is 100 characters.

- `contains` (string, optional)
  A value contained within a value list - returns all value lists containing this value.

  The maximum length is 800 characters.

- `created` (object, optional)
  Only return value lists that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/radar/value_lists \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/radar/value_lists",
  "has_more": false,
  "data": [
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
  ]
}
```
