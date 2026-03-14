# List all features attached to a product

Retrieve a list of features for a product

## Returns

Returns a list of features for a product

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/products/prod_NWjs8kKbJWmuuc/features \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/products/prod_NWjs8kKbJWmuuc/features",
  "has_more": false,
  "data": [
    {
      "id": "prodft_BcMBZUWCIOEgEc",
      "object": "product_feature",
      "livemode": false,
      "entitlement_feature": {
        "id": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
        "object": "entitlements.feature",
        "livemode": false,
        "name": "My super awesome feature",
        "lookup_key": "my-super-awesome-feature",
        "metadata": {}
      }
    }
  ]
}
```
