# Update an Account Capability

Updates an existing Account Capability. Request or remove a capability by updating its `requested` parameter.

## Returns

Returns an Account Capability object.

## Parameters

- `preview` (boolean, optional)
  Passing true assigns the preview onboarding policy to the capability.

- `requested` (boolean, optional)
  To request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the `requirements` arrays.

  If a capability isn’t permanent, you can remove it from the account by passing false. Some capabilities are permanent after they’ve been requested. Attempting to remove a permanent capability returns an error.

```curl
curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \
  -u "<<YOUR_SECRET_KEY>>" \
  -d requested=true
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
