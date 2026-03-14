# Test mode: Return an OutboundTransfer

Transitions a test mode created OutboundTransfer to the `returned` status. The OutboundTransfer must already be in the `processing` state.

## Returns

Returns the OutboundTransfer object in the returned state. Returns an error if the OutboundTransfer has already been returned or cannot be returned.

## Parameters

- `returned_details` (object, optional)
  Details about a returned OutboundTransfer.

  - `returned_details.code` (enum, optional)
    Reason for the return.
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
      The destination has declined this OutboundTransfer.

    - `incorrect_account_holder_name`
      The destination bank notified us that the bank account holder name on file is incorrect.

    - `invalid_account_number`
      The destination bank account details on file are probably incorrect. The routing number seems correct, but the account number is invalid.

    - `invalid_currency`
      The destination was unable to process this OutboundTransfer because of its currency.

    - `no_account`
      The destination bank account details on file are probably incorrect. No bank account exists with these details.

    - `other`
      The destination could not process this OutboundTransfer.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/treasury/outbound_transfers/obt_1Mtaaz2eZvKYlo2CUu1tWGAl/return \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "obt_1Mtaaz2eZvKYlo2CUu1tWGAl",
  "object": "treasury.outbound_transfer",
  "amount": 10000,
  "cancelable": false,
  "created": 1680717489,
  "currency": "usd",
  "description": "OutboundTransfer to my external bank account",
  "destination_payment_method": "pm_1Mtaaz2eZvKYlo2C235TqrIn",
  "destination_payment_method_details": {
    "billing_details": {
      "address": {
        "city": "San Francisco",
        "country": "US",
        "line1": "1234 Fake Street",
        "line2": null,
        "postal_code": "94102",
        "state": "CA"
      },
      "email": null,
      "name": "Jane Austen"
    },
    "type": "us_bank_account",
    "us_bank_account": {
      "account_holder_type": "company",
      "account_type": "checking",
      "bank_name": "STRIPE TEST BANK",
      "fingerprint": "AP24Iso0btGp4N10",
      "last4": "6789",
      "network": "ach",
      "routing_number": "110000000"
    }
  },
  "expected_arrival_date": 1680825600,
  "financial_account": "fa_1Mtaaz2eZvKYlo2CUf56sIA1",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKLHttqEGMgYdpKbb3Ec6NpO9f9jLUpJTCJGYDld0WR6lbibijEBPoyU4abErSxnN1ZB_JwosN4Krvqn2WLglRwEeAIzg4g",
  "livemode": false,
  "metadata": {},
  "returned_details": {
    "code": "declined",
    "transaction": "trxn_1Mtaaz2eZvKYlo2CRvn5ac2X"
  },
  "statement_descriptor": "transfer",
  "status": "returned",
  "status_transitions": {
    "returned_at": 1680717489,
    "failed_at": null,
    "canceled_at": null,
    "posted_at": 1680717489
  },
  "transaction": "trxn_1Mtaaz2eZvKYlo2Cn9D12psR"
}
```
