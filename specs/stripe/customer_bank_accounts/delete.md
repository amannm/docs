# Delete a bank account

You can delete bank accounts from a Customer.

## Returns

```curl
curl -X DELETE https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/sources/ba_1NkxyL2eZvKYlo2CwZgb2mzO \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "customer": "cus_9s6XKzkNRiz8i3",
  "id": "ba_1NkxyL2eZvKYlo2CwZgb2mzO",
  "object": "bank_account",
  "deleted": true
}
```
