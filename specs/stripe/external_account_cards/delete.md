# Delete a card

You can delete cards from a connected account where [controller.requirement_collection](../accounts/object.md#account_object-controller-requirement_collection) is `application` (includes [Custom accounts](https://docs.stripe.com/connect/custom-accounts.md)).

There are restrictions for deleting a card with `default_for_currency` set to true. You cannot delete a card if any of the following apply:

- The card’s `currency` is the same as the connected account’s [default_currency](../accounts/object.md#account_object-default_currency).
- There is another external account (card or bank account) with the same currency as the card.

To delete a card, you must first replace the default external account by setting `default_for_currency` with another external account in the same currency.

## Returns

Returns the deleted card object.

## Parameters

- `id` (string, required)
  Unique identifier for the external account to be deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAz2x2eZvKYlo2C75wJ1YUs \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "card_1NAz2x2eZvKYlo2C75wJ1YUs",
  "object": "card",
  "deleted": true
}
```
