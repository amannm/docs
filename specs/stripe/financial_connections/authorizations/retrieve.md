# Retrieve an Authorization

Retrieves the details of an Financial Connections `Authorization`.

## Returns

Returns an `Authorization` object if a valid identifier was provided, and raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/financial_connections/authorizations/fcauth_1NSlnc2eZvKYlo2CoamIONix \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "fcauth_1NSlnc2eZvKYlo2CoamIONix",
  "object": "financial_connections.authorization",
  "institution_name": "StripeBank",
  "livemode": false,
  "status": "active",
  "status_details": {}
}
```
