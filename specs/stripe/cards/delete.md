# Delete a card

You can delete cards from a customer. If you delete a card that is currently the default source, then the most recently added source will become the new default. If you delete a card that is the last remaining source on the customer, then the default_source attribute will become null.

For recipients: if you delete the default card, then the most recently added card will become the new default. If you delete the last remaining card on a recipient, then the default_card attribute will become null.

Note that for cards belonging to customers, you might want to prevent customers on paid subscriptions from deleting all cards on file, so that there is at least one default card for the next invoice payment attempt.

## Returns

```curl
curl -X DELETE https://api.stripe.com/v1/customers/acct_1032D82eZvKYlo2C/sources/card_1NGTaT2eZvKYlo2CZWSctn5n \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "card_1NGTaT2eZvKYlo2CZWSctn5n",
  "object": "card",
  "deleted": true
}
```
