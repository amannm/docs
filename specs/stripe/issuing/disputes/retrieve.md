# Retrieve a dispute

Retrieves an Issuing `Dispute` object.

## Returns

Returns an Issuing `Dispute` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ \
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
  "status": "unsubmitted",
  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"
}
```
