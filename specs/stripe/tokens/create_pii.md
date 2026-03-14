# Create a PII token

Creates a single-use token that represents the details of personally identifiable information (PII). You can use this token in place of an [id_number](create_pii.md#update_account-individual-id_number) or [id_number_secondary](create_pii.md#update_account-individual-id_number_secondary) in Account or Person Update API methods. You can only use a PII token once.

## Returns

Returns the created PII token if it’s successful. Otherwise, this call raises [an error](create_pii.md#errors).

## Parameters

- `pii` (object, required)
  The PII this token represents.

  - `pii.id_number` (string, optional)
    The `id_number` for the PII, in string form.

```curl
curl https://api.stripe.com/v1/tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "pii[id_number]"=000000000
```

### Response

```json
{
  "id": "pii_18PwbX2eZvKYlo2CzRXgwN3J",
  "object": "token",
  "client_ip": "124.123.76.134",
  "created": 1466783547,
  "livemode": false,
  "redaction": null,
  "type": "pii",
  "used": false
}
```
