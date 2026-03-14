# List Account Owners

Lists all owners for a given `Account`

## Returns

A dictionary with a `data` property that contains an array of up to `limit` owners for a given account, starting after owner `starting_after`. Each entry in the array is a separate owner object. If no more owners are available, the resulting array will be empty.

## Parameters

- `ownership` (string, required)
  The ID of the ownership object to fetch owners from.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/financial_connections/accounts/fca_1NoEbE2eZvKYlo2CmmnAn2A1/owners \
  -u "<<YOUR_SECRET_KEY>>" \
  -d ownership=fcaowns_1NoEbE2eZvKYlo2C4Xj7vilA
```

### Response

```json
{
  "object": "list",
  "url": "/v1/financial_connections/accounts/fca_1NoEbE2eZvKYlo2CmmnAn2A1/owners",
  "has_more": false,
  "data": [
    {
      "object": "list",
      "url": "/v1/financial_connections/accounts/fca_1NoDzC2eZvKYlo2CwXpqO27d/owners",
      "has_more": false,
      "data": [
        {
          "id": "fcaown_1NoDzC2eZvKYlo2C1TlEZ0K2",
          "object": "linked_account_owner",
          "email": "nobody+janesmith@stripe.com",
          "name": "Jane Smith",
          "ownership": "fcaowns_1NoDzC2eZvKYlo2CAm1EDKTk",
          "phone": "+1 555-555-5555",
          "raw_address": "123 Main Street, Everytown USA",
          "refreshed_at": null
        }
      ]
    }
  ]
}
```
