# Delete an invoice item

Deletes an invoice item, removing it from an invoice. Deleting invoice items is only possible when they’re not attached to invoices, or if it’s attached to a draft invoice.

## Returns

An object with the deleted invoice item’s ID and a deleted flag upon success. Otherwise, this call raises [an error](delete.md#errors), such as if the invoice item has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",
  "object": "invoiceitem",
  "deleted": true
}
```
