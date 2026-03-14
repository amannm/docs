# Delete a draft invoice

Permanently deletes a one-off invoice draft. This cannot be undone. Attempts to delete invoices that are no longer in a draft state will fail; once an invoice has been finalized or if an invoice is for a subscription, it must be [voided](delete.md#void_invoice).

## Returns

A successfully deleted invoice. Otherwise, this call raises [an error](delete.md#errors), such as if the invoice has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
  "object": "invoice",
  "deleted": true
}
```
