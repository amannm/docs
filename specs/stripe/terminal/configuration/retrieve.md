# Retrieve a Configuration

Retrieves a `Configuration` object.

## Returns

Returns a `Configuration` object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/terminal/configurations/tmc_FQqbaQCiy0m1xc \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tmc_FQqbaQCiy0m1xc",
  "object": "terminal.configuration",
  "is_account_default": false,
  "livemode": false
}
```
