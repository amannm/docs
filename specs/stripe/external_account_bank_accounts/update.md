# Update a bank account

Updates the metadata, account holder name, account holder type of a bank account belonging to a connected account and optionally sets it as the default for its currency. Other bank account details are not editable by design.

You can only update bank accounts when [account.controller.requirement_collection](../accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes [Custom accounts](https://docs.stripe.com/connect/custom-accounts.md).

You can re-enable a disabled bank account by performing an update call without providing any arguments or changes.

## Returns

Returns the bank account object.

## Parameters

- `account_holder_name` (string, optional)
  The name of the person or business that owns the bank account.

- `account_holder_type` (string, optional)
  The type of entity that holds the account. This can be either `individual` or `company`.

- `account_type` (string, optional)
  The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.

- `default_for_currency` (boolean, optional)
  When set to true, this becomes the default external account for its currency.

- `documents` (object, optional)
  Documents that may be submitted to satisfy various informational requests.

  - `documents.bank_account_ownership_verification` (object, optional)
    One or more documents that support the [Bank account ownership verification](https://support.stripe.com/questions/bank-account-ownership-verification) requirement. Must be a document associated with the bank account that displays the last 4 digits of the account number, either a statement or a check.

    - `documents.bank_account_ownership_verification.files` (array of strings, optional)
      One or more document ids returned by a [file upload](update.md#create_file) with a `purpose` value of `account_requirement`.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAiwl2eZvKYlo2CRdCLZSxO \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

### Response

```json
{
  "id": "ba_1NAiwl2eZvKYlo2CRdCLZSxO",
  "object": "bank_account",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {
    "order_id": "6735"
  },
  "routing_number": "110000000",
  "status": "new",
  "account": "acct_1032D82eZvKYlo2C"
}
```
