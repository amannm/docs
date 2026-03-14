# Create a bank account token

Creates a single-use token that represents a bank account’s details. You can use this token with any v1 API method in place of a bank account dictionary. You can only use this token once. To do so, attach it to a [connected account](create_bank_account.md#accounts) where [controller.requirement_collection](../accounts/object.md#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.

## Returns

Returns the created bank account token if it’s successful. Otherwise, this call raises [an error](create_bank_account.md#errors).

## Parameters

- `bank_account` (object, optional)
  The bank account this token will represent.

  - `bank_account.account_number` (string, required)
    The account number for the bank account, in string form. Must be a checking account.

  - `bank_account.country` (string, required)
    The country in which the bank account is located.

  - `bank_account.account_holder_name` (string, optional)
    The name of the person or business that owns the bank account. This field is required when attaching the bank account to a `Customer` object.

  - `bank_account.account_holder_type` (string, optional)
    The type of entity that holds the account. It can be `company` or `individual`. This field is required when attaching the bank account to a `Customer` object.

  - `bank_account.account_type` (string, optional)
    The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.

  - `bank_account.currency` (enum, optional)
    The currency the bank account is in. This must be a country/currency pairing that [Stripe supports.](https://docs.stripe.com/docs/payouts.md)

  - `bank_account.payment_method` (string, optional)
    The ID of a Payment Method with a `type` of `us_bank_account`. The Payment Method’s bank account information will be copied and returned as a Bank Account Token. This parameter is exclusive with respect to all other parameters in the `bank_account` hash. You must include the top-level `customer` parameter if the Payment Method is attached to a `Customer` object. If the Payment Method is not attached to a `Customer` object, it will be consumed and cannot be used again. You may not use Payment Methods which were created by a Setup Intent with `attach_to_self=true`.

  - `bank_account.routing_number` (string, optional)
    The routing number, sort code, or other country-appropriate institution number for the bank account. For US bank accounts, this is required and should be the ACH routing number, not the wire routing number. If you are providing an IBAN for `account_number`, this field is not required.

- `customer` (string, optional)
  Create a token for the customer, which is owned by the application’s account. You can only use this with an [OAuth access token](https://docs.stripe.com/docs/connect/standard-accounts.md) or [Stripe-Account header](https://docs.stripe.com/docs/connect/authentication.md). Learn more about [cloning saved payment methods](https://docs.stripe.com/docs/connect/cloning-saved-payment-methods.md).

```curl
curl https://api.stripe.com/v1/tokens \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "bank_account[country]"=US \
  -d "bank_account[currency]"=usd \
  -d "bank_account[account_holder_name]"="Jenny Rosen" \
  -d "bank_account[account_holder_type]"=individual \
  -d "bank_account[routing_number]"=110000000 \
  -d "bank_account[account_number]"=000123456789
```

### Response

```json
{
  "id": "btok_1N3T00LkdIwHu7ixt44h1F8k",
  "object": "token",
  "bank_account": {
    "id": "ba_1NWScr2eZvKYlo2C8MgV5Cwn",
    "object": "bank_account",
    "account_holder_name": "Jenny Rosen",
    "account_holder_type": "individual",
    "account_type": null,
    "bank_name": "STRIPE TEST BANK",
    "country": "US",
    "currency": "usd",
    "fingerprint": "1JWtPxqbdX5Gamtz",
    "last4": "6789",
    "routing_number": "110000000",
    "status": "new"
  },
  "client_ip": null,
  "created": 1689981645,
  "livemode": false,
  "redaction": null,
  "type": "bank_account",
  "used": false
}
```
