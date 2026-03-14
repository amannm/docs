# Retrieve a tax code

Retrieves the details of an existing tax code. Supply the unique tax code ID and Stripe will return the corresponding tax code information.

## Returns

Returns a tax code object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/tax_codes/txcd_99999999 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "txcd_99999999",
  "object": "tax_code",
  "description": "Any tangible or physical good. For jurisdictions that impose a tax, the standard rate is applied.",
  "name": "General - Tangible Goods"
}
```
