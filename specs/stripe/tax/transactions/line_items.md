# Retrieve a transaction's line items

Retrieves the line items of a committed standalone transaction as a collection.

## Returns

A list of Line Item objects if the Tax Transaction is found. Otherwise returns a ‘not found’ error.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

  The maximum length is 500 characters.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

  The maximum length is 500 characters.

```curl
curl https://api.stripe.com/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",
  "object": "list",
  "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items",
  "has_more": false,
  "data": [
    {
      "id": "tax_li_ONDxh8JZw14sP8",
      "object": "tax.transaction_line_item",
      "amount": 1499,
      "amount_tax": 148,
      "livemode": false,
      "metadata": null,
      "product": null,
      "quantity": 1,
      "reference": "Pepperoni Pizza",
      "reversal": null,
      "tax_behavior": "exclusive",
      "tax_code": "txcd_40060003",
      "type": "transaction"
    }
  ]
}
```
