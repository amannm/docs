# List all ReceivedCredits

Returns a list of ReceivedCredits.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` ReceivedCredits, starting after ReceivedCredit `starting_after`. Each entry in the array is a separate ReceivedCredit object. If no more ReceivedCredits are available, the resulting array will be empty.

## Parameters

- `financial_account` (string, optional)
  The FinancialAccount that received the funds.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `linked_flows` (object, optional)
  Only return ReceivedCredits described by the flow.

  - `linked_flows.source_flow_type` (enum, required)
    The source flow type.
Possible enum values:
    - `credit_reversal`
      ReceivedCredits that were reversed and have associated CreditReversals.

    - `other`
      ReceivedCredits created from other source flow.

    - `outbound_payment`
      ReceivedCredits created from OutboundPayments.

    - `outbound_transfer`
      ReceivedCredits created from OutboundPayments.

    - `payout`
      ReceivedCredits created from Payouts.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

- `status` (enum, optional)
  Only return ReceivedCredits that have the given status: `succeeded` or `failed`.
Possible enum values:
  - `failed`
    The ReceivedCredit was declined, and no Transaction was created.

  - `succeeded`
    The ReceivedCredit was approved.

```curl
curl -G https://api.stripe.com/v1/treasury/received_credits \
  -u "<<YOUR_SECRET_KEY>>" \
  -d financial_account=fa_1MtkSr2eZvKYlo2CsJozwFWD \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/received_credits",
  "has_more": false,
  "data": [
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
  ]
}
```
