# Retrieve an invoice rendering template

Retrieves an invoice rendering template with the given ID. It by default returns the latest version of the template. Optionally, specify a version to see previous versions.

## Returns

Returns an [invoice_payment](https://docs.stripe.com/docs/api/invoices/payments.md) object if a valid invoice payment ID and matching invoice ID were provided. Otherwise, this call raises [an error](retrieve.md#errors).

```curl
curl https://api.stripe.com/v1/invoice_rendering_templates/inrtem_abc \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "inrtem_abc",
  "object": "invoice_rendering_template",
  "nickname": "My Invoice Template",
  "status": "active",
  "version": 1,
  "created": 1678942624,
  "livemode": false
}
```
