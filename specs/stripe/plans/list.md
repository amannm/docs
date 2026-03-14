# List all plans

Returns a list of your plans.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` plans, starting after plan `starting_after`. Each entry in the array is a separate plan object. If no more plans are available, the resulting array will be empty.

## Parameters

- `active` (boolean, optional)
  Only return plans that are active or inactive (e.g., pass `false` to list all inactive plans).

- `created` (object, optional)
  A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

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

- `product` (string, optional)
  Only return plans for the given product.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/plans \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/plans",
  "has_more": false,
  "data": [
    {
      "id": "plan_NjpIbv3g3ZibnD",
      "object": "plan",
      "active": true,
      "amount": 1200,
      "amount_decimal": "1200",
      "billing_scheme": "per_unit",
      "created": 1681851647,
      "currency": "usd",
      "interval": "month",
      "interval_count": 1,
      "livemode": false,
      "metadata": {},
      "nickname": null,
      "product": "prod_NjpI7DbZx6AlWQ",
      "tiers_mode": null,
      "transform_usage": null,
      "trial_period_days": null,
      "usage_type": "licensed"
    }
  ]
}
```
