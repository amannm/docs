# Create a login link

Creates a login link for a connected account to access the Express Dashboard.

**You can only create login links for accounts that use the [Express Dashboard](https://docs.stripe.com/connect/express-dashboard.md) and are connected to your platform**.

## Returns

Returns a login link object if the call succeeded.

```curl
curl -X POST https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/login_links \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "login_link",
  "created": 1686084879,
  "url": "https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"
}
```
