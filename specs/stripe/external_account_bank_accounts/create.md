# Create a bank account

When you create a new bank account, you must specify a [connected account](create.md#accounts) to create it on. You can only specify connected accounts where [account.controller.requirement_collection](../accounts/object.md#account_object-controller-requirement_collection) is `application` (includes [Custom accounts](https://docs.stripe.com/connect/custom-accounts.md)).

If the bank account’s owner has no other external account in the bank account’s currency, the new bank account will become the default for that currency. However, if the owner already has a bank account for that currency, the new account will become the default only if the `default_for_currency` parameter is set to `true`.

## Returns

Returns the bank account object

## Parameters

- `external_account` (object | string, required)
  Either a token, like the ones returned by [Stripe.js](https://docs.stripe.com/docs/js.md), or a dictionary containing a user’s bank account details (with the options shown below).

  - `external_account.account_number` (string, required)
    The account number for the bank account, in string form. Must be a checking account.

  - `external_account.country` (string, required)
    The country in which the bank account is located.

  - `external_account.currency` (string, required)
    The currency the bank account is in. This must be a country/currency pairing that [Stripe supports](https://docs.stripe.com/docs/payouts.md).

  - `external_account.object` (string, required)
    The type of external account. Should be `bank_account`

  - `external_account.account_holder_name` (string, optional)
    The name of the person or business that owns the bank account. This field is required when attaching the bank account to a `Customer` object.

  - `external_account.account_holder_type` (enum, optional)
    The type of entity that holds the account. This field is required when attaching the bank account to a `Customer` object.
Possible enum values:
    - `company`
    - `individual`

  - `external_account.documents` (object, optional)
    Documents that may be submitted to satisfy various informational requests.

    - `external_account.documents.bank_account_ownership_verification` (object, optional)
      One or more documents that support the [Bank account ownership verification](https://support.stripe.com/questions/bank-account-ownership-verification) requirement. Must be a document associated with the bank account that displays the last 4 digits of the account number, either a statement or a voided check.

      - `external_account.documents.bank_account_ownership_verification.files` (array of strings, optional)
        One or more document ids returned by a [file upload](create.md#create_file) with a `purpose` value of `account_requirement`.

  - `external_account.routing_number` (string, optional)
    The routing number, sort code, or other country-appropriate institution number for the bank account. For US bank accounts, this is required and should be the ACH routing number, not the wire routing number. If you are providing an IBAN for `account_number`, this field is not required.

- `default_for_currency` (boolean, optional)
  When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d external_account=btok_1NAiJy2eZvKYlo2Cnh6bIs9c
```

### Response

```json
{
  "id": "ba_1NAiJy2eZvKYlo2CvChQKz5k",
  "object": "bank_account",
  "account": "acct_1032D82eZvKYlo2C",
  "account_holder_name": "Jane Austen",
  "account_holder_type": "company",
  "account_type": null,
  "bank_name": "STRIPE TEST BANK",
  "country": "US",
  "currency": "usd",
  "fingerprint": "1JWtPxqbdX5Gamtc",
  "last4": "6789",
  "metadata": {},
  "routing_number": "110000000",
  "status": "new"
}
```
