# Retrieve a ReceivedDebit

Retrieves the details of an existing ReceivedDebit by passing the unique ReceivedDebit ID from the ReceivedDebit list

## Returns

Returns a ReceivedDebit object.

```curl
curl https://api.stripe.com/v1/treasury/received_debits/rd_1MtkUY2eZvKYlo2CT9SYD1AF \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "rd_1MtkUY2eZvKYlo2CT9SYD1AF",
  "object": "treasury.received_debit",
  "amount": 1000,
  "created": 1680755530,
  "currency": "usd",
  "description": "Stripe Test",
  "failure_code": null,
  "financial_account": "fa_1MtkUY2eZvKYlo2CY3s6OQyK",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKMqWuaEGMgaYNwvP2Oc6NpPGJjaET9tspjuPmbhoXvIfQj6YrtJkjCiTFYe59B8Ck4cg5jTS80A9mLSaK_4oF_LBDlNzgg",
  "initiating_payment_method_details": {
    "billing_details": {
      "address": {
        "city": null,
        "country": null,
        "line1": null,
        "line2": null,
        "postal_code": null,
        "state": null
      },
      "email": null,
      "name": "Jane Austen"
    },
    "type": "us_bank_account",
    "us_bank_account": {
      "bank_name": "STRIPE TEST BANK",
      "last4": "6789",
      "routing_number": "110000000"
    }
  },
  "linked_flows": {
    "debit_reversal": null,
    "inbound_transfer": null,
    "issuing_authorization": null,
    "issuing_transaction": null,
    "payout": null
  },
  "livemode": false,
  "network": "ach",
  "reversal_details": {
    "deadline": 1681084800,
    "restricted_reason": null
  },
  "status": "succeeded",
  "transaction": "trxn_1MtkUY2eZvKYlo2ChymLKPp5"
}
```
