# List all active entitlements

Retrieve a list of active entitlements for a customer

## Returns

Returns a list of active entitlements for a customer

## Parameters

- `customer` (string, required)
  The ID of the customer.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/entitlements/active_entitlements \
  -u "<<YOUR_SECRET_KEY>>" \
  -d customer=cus_9s6XKzkNRiz8i3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/entitlements/active_entitlements",
  "has_more": false,
  "data": [
    {
      "id": "ent_test_61QG5x2cU1GluFTYs41JqiESbLiX8C8O",
      "object": "entitlements.active_entitlement",
      "feature": "feat_test_61QGU1MWyFMSP9YBZ41ClCIKljWvsTgu",
      "lookup_key": "seats-feature",
      "livemode": false
    }
  ]
}
```
