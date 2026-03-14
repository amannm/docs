# Submit a dispute

Submits an Issuing `Dispute` to the card network. Stripe validates that all evidence fields required for the dispute’s reason are present. For more details, see [Dispute reasons and evidence](https://docs.stripe.com/docs/issuing/purchases/disputes.md#dispute-reasons-and-evidence).

## Returns

Returns an Issuing `Dispute` object in `submitted` status if submission succeeds.

## Parameters

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl -X POST https://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ/submit \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",
  "object": "issuing.dispute",
  "amount": 100,
  "created": 1681947753,
  "currency": "usd",
  "evidence": {
    "fraudulent": {
      "additional_documentation": null,
      "dispute_explanation": null,
      "explanation": "This transaction is fraudulent.",
      "uncategorized_file": null
    },
    "reason": "fraudulent"
  },
  "livemode": false,
  "metadata": {},
  "status": "submitted",
  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"
}
```
