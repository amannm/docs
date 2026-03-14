# Test mode: Fail an InboundTransfer

Transitions a test mode created InboundTransfer to the `failed` status. The InboundTransfer must already be in the `processing` state.

## Returns

Returns the InboundTransfer object in the returned state. Returns an error if the InboundTransfer has already failed or cannot be failed.

## Parameters

- `failure_details` (object, optional)
  Details about a failed InboundTransfer.

  - `failure_details.code` (enum, optional)
    Reason for the failure.
Possible enum values:
    - `account_closed`
      The bank account has been closed.

    - `account_frozen`
      The bank account has been frozen.

    - `bank_account_restricted`
      The bank account has restrictions on either the type or number of transfers allowed. This normally indicates that the bank account is a savings or other non-checking account.

    - `bank_ownership_changed`
      The bank account is no longer valid because its branch has changed ownership.

    - `debit_not_authorized`
      Debit transactions are not approved on the bank account.

    - `incorrect_account_holder_address`
      The bank notified us that the bank account holder address on file is incorrect.

    - `incorrect_account_holder_name`
      The bank notified us that the bank account holder name on file is incorrect.

    - `incorrect_account_holder_tax_id`
      The bank notified us that the bank account holder tax ID on file is incorrect.

    - `insufficient_funds`
      The bank account has insufficient funds to cover the debit transaction.

    - `invalid_account_number`
      The bank account details on file are probably incorrect. The routing number seems correct, but the account number is invalid.

    - `invalid_currency`
      The bank was unable to process this transfer because of its currency. This is probably because the bank account can’t accept payments in that currency.

    - `no_account`
      The bank account details on file are probably incorrect. No bank account exists with these details.

    - `other`
      The bank could not process this transfer.

```curl
curl https://api.stripe.com/v1/test_helpers/treasury/inbound_transfers/ibt_1MtaDN2eZvKYlo2CxcxF1Qwi/fail \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "failure_details[code]"=insufficient_funds
```

### Response

```json
{
  "id": "ibt_1MtaDN2eZvKYlo2CxcxF1Qwi",
  "object": "treasury.inbound_transfer",
  "amount": 10000,
  "cancelable": true,
  "created": 1680716025,
  "currency": "usd",
  "description": "InboundTransfer from my external bank account",
  "failure_details": {
    "code": "insufficient_funds"
  },
  "financial_account": "fa_1MtaDM2eZvKYlo2CvXrQknN4",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKPnhtqEGMgZ09q__wJA6NpPUfXQX0PUpgdTTpcHXdViKIK3-mEuzKM_CrltWFzRyKdq8OhPb6676H32JwPak4k0jonMLYA",
  "linked_flows": {
    "received_debit": null
  },
  "livemode": false,
  "metadata": {},
  "origin_payment_method": "pm_1MtaDN2eZvKYlo2CObQW5Wkv",
  "origin_payment_method_details": {
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
  "returned": false,
  "statement_descriptor": "transfer",
  "status": "failed",
  "status_transitions": {
    "failed_at": 1680716025,
    "succeeded_at": null
  },
  "transaction": "trxn_1MtaDM2eZvKYlo2CKxgPNzLa"
}
```
