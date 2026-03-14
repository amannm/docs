# Test mode: Update an OutboundPayment

Updates a test mode created OutboundPayment with tracking details. The OutboundPayment must not be cancelable, and cannot be in the `canceled` or `failed` states.

## Returns

Returns the OutboundPayment object with the updated tracking details. Returns an error if the OutboundPayment is in an invalid state or if `tracking_details` has already been set.

## Parameters

- `tracking_details` (object, required)
  Details about network-specific tracking information.

  - `tracking_details.type` (enum, required)
    The US bank account network used to send funds.
Possible enum values:
    - `ach`
    - `us_domestic_wire`

  - `tracking_details.ach` (object, optional)
    ACH network tracking details.

    - `tracking_details.ach.trace_id` (string, required)
      ACH trace ID for funds sent over the `ach` network.

  - `tracking_details.us_domestic_wire` (object, optional)
    US domestic wire network tracking details.

    - `tracking_details.us_domestic_wire.chips` (string, optional)
      CHIPS System Sequence Number (SSN) for funds sent over the `us_domestic_wire` network.

    - `tracking_details.us_domestic_wire.imad` (string, optional)
      IMAD for funds sent over the `us_domestic_wire` network.

    - `tracking_details.us_domestic_wire.omad` (string, optional)
      OMAD for funds sent over the `us_domestic_wire` network.

```curl
curl https://api.stripe.com/v1/test_helpers/treasury/outbound_payments/obp_1MtaD72eZvKYlo2C36lgqC6Y \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "tracking_details[type]"=ach \
  -d "tracking_details[ach][trace_id]"=841042400123450
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
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOrhtqEGMgawWNwbI_w6NZNOI4y6vNpfIP-oQAT5mkBRbOHJN1f08r7jF-UumeywdupuJr7P2cxF8L5JRSVPMmttq_kA",
  "livemode": false,
  "metadata": {},
  "returned_details": null,
  "statement_descriptor": "payment",
  "status": "posted",
  "status_transitions": {
    "failed_at": null,
    "posted_at": 1680716010,
    "returned_at": null,
    "canceled_at": null
  },
  "tracking_details": {
    "type": "ach",
    "ach": {
      "trace_id": "841042400123450"
    }
  },
  "transaction": "trxn_1MtaD72eZvKYlo2CmUu4Vs5c"
}
```
