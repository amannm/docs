# Test mode: Return an OutboundPayment

Transitions a test mode created OutboundPayment to the `returned` status. The OutboundPayment must already be in the `processing` state.

## Returns

Returns the OutboundPayment object in the returned state. Returns an error if the OutboundPayment has already been returned or cannot be returned.

## Parameters

- `returned_details` (object, optional)
  Optional hash to set the return code.

  - `returned_details.code` (enum, optional)
    The return code to be set on the OutboundPayment object.
Possible enum values:
    - `account_closed`
      The destination has been closed.

    - `account_frozen`
      The destination has been frozen.

    - `bank_account_restricted`
      The destination bank account has restrictions on either the type or number of transfers allowed. This normally indicates that the bank account is a savings or other non-checking account.

    - `bank_ownership_changed`
      The destination bank account is no longer valid because its branch has changed ownership.

    - `declined`
      The destination has declined this OutboundPayment.

    - `incorrect_account_holder_name`
      The destination bank notified us that the bank account holder name on file is incorrect.

    - `invalid_account_number`
      The destination bank account details on file are probably incorrect. The routing number seems correct, but the account number is invalid.

    - `invalid_currency`
      The destination was unable to process this OutboundPayment because of its currency.

    - `no_account`
      The destination bank account details on file are probably incorrect. No bank account exists with these details.

    - `other`
      The destination could not process this OutboundPayment.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_payments/obp_1MtaD72eZvKYlo2C36lgqC6Y/return \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "obp_1MtaD72eZvKYlo2C36lgqC6Y",
  "object": "treasury.outbound_payment",
  "amount": 10000,
  "cancelable": false,
  "created": 1680716009,
  "currency": "usd",
  "customer": null,
  "description": "OutboundPayment to a 3rd party",
  "destination_payment_method": null,
  "destination_payment_method_details": {
    "type": "us_bank_account",
    "destination": "ba_1MtaD62eZvKYlo2C8vwjm7bc"
  },
  "end_user_details": {
    "ip_address": null,
    "present": false
  },
  "expected_arrival_date": 1680716009,
  "financial_account": "fa_1MtaD72eZvKYlo2CYKM3DnUI",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgYhogtESYQ6NZMO6Vt0EC3mum1Ote762Q9ymvgfrijWXRfgVjJ5BoXVxeND-NunsJmjcHhb2F_4bmtHHWur",
  "livemode": false,
  "metadata": {},
  "returned_details": {
    "code": "account_closed",
    "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
  },
  "statement_descriptor": "payment",
  "status": "returned",
  "status_transitions": {
    "failed_at": null,
    "posted_at": 1680716010,
    "returned_at": 1680716011,
    "canceled_at": null
  },
  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
}
```
