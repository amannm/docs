# Find a Secret

Finds a secret in the secret store by name and scope.

## Returns

Returns a secret object.

## Parameters

- `name` (string, required)
  A name for the secret that’s unique within the scope.

- `scope` (object, required)
  Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

  - `scope.type` (enum, required)
    The secret scope type.
Possible enum values:
    - `account`
      A secret scoped to an account. Use this for API keys or other secrets that should be accessible by all UI Extension contexts.

    - `user`
      A secret scoped to a specific user. Use this for oauth tokens or other per-user secrets. If this is set, `scope.user` must also be set.

  - `scope.user` (string, optional)
    The user ID. This field is required if `type` is set to `user`, and should not be provided if `type` is set to `account`.

```curl
curl -G https://api.stripe.com/v1/apps/secrets/find \
  -u "<<YOUR_SECRET_KEY>>" \
  -d name=my-api-key \
  -d "scope[type]"=account
```

### Response

```json
{
  "id": "appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix",
  "object": "apps.secret",
  "created": 1680209063,
  "expires_at": null,
  "livemode": false,
  "name": "my-api-key",
  "scope": {
    "type": "account"
  }
}
```
