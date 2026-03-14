# List all account capabilities

Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.

## Returns

A dictionary with a `data` property that contains an array of the capabilities of this account. Each entry in the array is a separate capability object.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "list",
  "url": "/v1/accounts/acct_1032D82eZvKYlo2C/capabilities",
  "has_more": false,
  "data": [
    {
      "id": "card_payments",
      "object": "capability",
      "account": "acct_1032D82eZvKYlo2C",
      "future_requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [],
        "disabled_reason": null,
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
      },
      "requested": true,
      "requested_at": 1693951912,
      "requirements": {
        "alternatives": [],
        "current_deadline": null,
        "currently_due": [],
        "disabled_reason": null,
        "errors": [],
        "eventually_due": [],
        "past_due": [],
        "pending_verification": []
      },
      "status": "inactive"
    }
  ]
}
```
