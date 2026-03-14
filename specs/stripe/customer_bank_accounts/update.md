# Update a bank account

Updates the `account_holder_name`, `account_holder_type`, and `metadata` of a bank account belonging to a customer. Other bank account details are not editable, by design.

## Returns

Returns the bank account object.

## Parameters

- `account_holder_name` (string, optional)
  The name of the person or business that owns the bank account.

- `account_holder_type` (string, optional)
  The type of entity that holds the account. This can be either `individual` or `company`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/customers/cus_9s6XI9OFIdpjIg/sources/ba_1MvoIJ2eZvKYlo2CO9f0MabO \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

### Response

```json
{
  "id": "ba_1MvoIJ2eZvKYlo2CO9f0MabO",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": "cus_9s6XI9OFIdpjIg",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {
    "order_id": "6735"
  },
  "routing_number": "110000000",
  "status": "new"
}
```
