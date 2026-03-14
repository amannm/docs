# Retrieve an Account Capability

Retrieves information about the specified Account Capability.

## Returns

Returns an Account Capability object.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
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
  "requested_at": 1688491010,
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
```
