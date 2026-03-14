# Unarchive an invoice rendering template

Unarchive an invoice rendering template so it can be used on new Stripe objects again.

## Returns

The updated template object is returned if successful. Otherwise, this call raises [an error](unarchive.md#errors).

```curl
curl -X POST https://api.stripe.com/v1/invoice_rendering_templates/inrtem_abc/unarchive \
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
