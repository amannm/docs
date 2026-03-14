# Retrieve a bank account

By default, you can see the 10 most recent external accounts stored on a [connected account](https://docs.stripe.com/connect/accounts.md) directly on the object. You can also retrieve details about a specific bank account stored on the account.

## Returns

Returns the bank account object.

## Parameters

- `id` (string, required)
  Unique identifier for the external account to be retrieved.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAinX2eZvKYlo2CpFGcuuEG \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ba_1NAinX2eZvKYlo2CpFGcuuEG",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "customer": null,
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new"
}
```
