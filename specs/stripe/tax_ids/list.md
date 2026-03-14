# List all tax IDs

Returns a list of tax IDs.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` tax IDs, starting after tax ID `starting_after`. Each entry in the array is a separate `tax_id` object. If no more tax IDs are available, the resulting array will be empty.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `owner` (object, optional)
  The account or customer the tax ID belongs to. Defaults to `owner[type]=self`.

  - `owner.type` (enum, required)
    Type of owner referenced.
Possible enum values:
    - `account`
      Indicates an account is being referenced.

    - `application`
      Indicates an application is being referenced.

    - `customer`
      Indicates a customer is being referenced.

    - `self`
      Indicates that the account being referenced is the account making the API request.

  - `owner.account` (string, optional)
    Connected Account the tax ID belongs to. Required when `type=account`

  - `owner.customer` (string, optional)
    Customer the tax ID belongs to. Required when `type=customer`

  - `owner.customer_account` (string, optional)
    ID of the Account representing the customer that the tax ID belongs to. Can be used in place of `customer` when `type=customer`

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/tax_ids \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/tax_ids",
  "has_more": false,
  "data": [
    {
      "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",
      "object": "tax_id",
      "country": "DE",
      "created": 123456789,
      "customer": null,
      "livemode": false,
      "type": "eu_vat",
      "value": "DE123456789",
      "verification": null,
      "owner": {
        "type": "self",
        "customer": null
      }
    }
  ]
}
```
