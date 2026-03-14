# Delete a person

Deletes an existing person’s relationship to the account’s legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the `account_opener`. If your integration is using the `executive` parameter, you cannot delete the only verified `executive` on file.

## Returns

Returns the deleted [`person`](object.md) object.

```curl
curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/persons/person_1MqjB62eZvKYlo2CaeEJzKVR \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "person_1MqjB62eZvKYlo2CaeEJzKVR",
  "object": "person",
  "deleted": true
}
```
