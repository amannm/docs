# Delete a bank account

You can delete destination bank accounts from a connected account where [account.controller.requirement_collection](../accounts/object.md#account_object-controller-requirement_collection) is `application` (includes [Custom accounts](https://docs.stripe.com/connect/custom-accounts.md)).

There are restrictions for deleting a bank account with `default_for_currency` set to true. You cannot delete a bank account if any of the following apply:

- The bank account’s `currency` is the same as the connected account’s [default_currency](../accounts/object.md#account_object-default_currency).
- There is another external account (card or bank account) with the same currency as the bank account.

To delete a bank account, you must first replace the default external account by setting `default_for_currency` with another external account in the same currency.

## Returns

Returns the deleted bank account object.

## Parameters

- `id` (string, required)
  Unique identifier for the external account to be deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/ba_1NAz2w2eZvKYlo2CgeR2w6yU \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ba_1NAz2w2eZvKYlo2CgeR2w6yU",
  "object": "bank_account",
  "deleted": true
}
```
