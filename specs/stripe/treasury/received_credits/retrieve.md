# Retrieve a ReceivedCredit

Retrieves the details of an existing ReceivedCredit by passing the unique ReceivedCredit ID from the ReceivedCredit list.

## Returns

Returns a ReceivedCredit object.

```curl
curl https://api.stripe.com/v1/treasury/received_credits/rc_1MtkSr2eZvKYlo2CcysvUbEw \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",
  "object": "treasury.received_credit",
  "amount": 1000,
  "created": 1680755425,
  "currency": "usd",
  "description": "Stripe Test",
  "failure_code": null,
  "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",
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
    "credit_reversal": null,
    "issuing_authorization": null,
    "issuing_transaction": null,
    "source_flow": null,
    "source_flow_type": null
  },
  "livemode": false,
  "network": "ach",
  "reversal_details": {
    "deadline": 1681084800,
    "restricted_reason": null
  },
  "status": "succeeded",
  "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"
}
```
