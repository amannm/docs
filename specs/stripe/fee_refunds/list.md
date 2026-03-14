# List all application fee refunds

You can see a list of the refunds belonging to a specific application fee. Note that the 10 most recent refunds are always available by default on the application fee object. If you need more than those 10, you can use this API method and the `limit` and `starting_after` parameters to page through additional refunds.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` refunds, starting after `starting_after`. Each entry in the array is a separate application fee refund object. If no more refunds are available, the resulting array will be empty. If you provide a non-existent application fee ID, this call raises [an error](list.md#errors).

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/application_fees/fr_1MtJRpKbnvuxQXGuM6Ww0D24/refunds \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/application_fees/fr_1MtJRpKbnvuxQXGuM6Ww0D24/refunds",
  "has_more": false,
  "data": [
    {
      "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
      "object": "fee_refund",
      "amount": 100,
      "balance_transaction": null,
      "created": 1680651573,
      "currency": "usd",
      "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
      "metadata": {}
    }
  ]
}
```
