# Delete an account

With [Connect](https://docs.stripe.com/connect.md), you can delete accounts you manage.

Test-mode accounts can be deleted at any time.

Live-mode accounts that have access to the standard dashboard and Stripe is responsible for negative account balances cannot be deleted, which includes Standard accounts. All other Live-mode accounts, can be deleted when all [balances](../balance/balance_object.md) are zero.

If you want to delete your own account, use the [account information tab in your account settings](https://dashboard.stripe.com/settings/account) instead.

## Returns

Returns an object with a deleted parameter if the call succeeds. If the account ID does not exist, this call raises [an error](delete.md#errors).

```curl
curl -X DELETE https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "acct_1Nv0FGQ9RKHgCVdK",
  "object": "account",
  "deleted": true
}
```
