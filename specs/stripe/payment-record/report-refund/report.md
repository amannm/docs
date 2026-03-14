# Report a refund

Report that the most recent payment attempt on the specified Payment Record was refunded.

## Returns

The updated Payment Record object with its most recent payment attempt refunded.

## Parameters

- `id` (string, required)
  The ID of the Payment Record.

- `outcome` (enum, required)
  The outcome of the reported refund.
Possible enum values:
  - `refunded`
    The payment was refunded.

- `processor_details` (object, required)
  Processor information for this refund.

  - `processor_details.type` (enum, required)
    The type of the processor details. An additional hash is included on processor_details with a name matching this value. It contains additional information specific to the processor.
Possible enum values:
    - `custom`
      A custom payment processor that is not included in Stripe’s standard processor types. This allows you to report refunds processed through external payment processors or custom integrations.

  - `processor_details.custom` (object, optional)
    Information about the custom processor used to make this refund.

    - `processor_details.custom.refund_reference` (string, required)
      A reference to the external refund. This field must be unique across all refunds.

- `refunded` (object, required)
  Information about the payment attempt refund.

  - `refunded.refunded_at` (timestamp, required)
    When the reported refund completed. Measured in seconds since the Unix epoch.

- `amount` (object, optional)
  A positive integer in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal) representing how much of this payment to refund. Can refund only up to the remaining, unrefunded amount of the payment.

  - `amount.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `amount.value` (integer, required)
    A positive integer representing the amount in the currency’s [minor unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). For example, `100` can represent 1 USD or 100 JPY.

- `initiated_at` (timestamp, optional)
  When the reported refund was initiated. Measured in seconds since the Unix epoch.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl https://api.stripe.com/v1/payment_records/pr_5RV730PrHyAEi/report_refund \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "processor_details[type]"=custom \
  -d "processor_details[custom][refund_reference]"=refund_12345 \
  -d outcome=refunded \
  -d "refunded[refunded_at]"=1730253453 \
  -d "amount[currency]"=usd \
  -d "amount[value]"=1000 \
  -d initiated_at=1730253450
```

### Response

```json
{
  "id": "pr_5RV730PrHyAEi",
  "object": "payment_record",
  "amount_canceled": {
    "currency": "usd",
    "value": 0
  },
  "amount_failed": {
    "currency": "usd",
    "value": 0
  },
  "amount_guaranteed": {
    "currency": "usd",
    "value": 0
  },
  "amount_refunded": {
    "currency": "usd",
    "value": 1000
  },
  "amount_requested": {
    "currency": "usd",
    "value": 1000
  },
  "created": 1730211363,
  "customer_details": null,
  "customer_presence": "on_session",
  "description": "computer software",
  "latest_payment_attempt_record": "par_1ArV730PrHyQuG",
  "livemode": true,
  "metadata": {},
  "payment_method_details": {
    "billing_details": null,
    "custom": {
      "display_name": "newpay",
      "type": "cpmt_125kjj3hn3sdf"
    },
    "payment_method": "pm_5j23kjksibjlks",
    "type": "custom"
  },
  "processor_details": {
    "type": "custom",
    "custom": {
      "payment_reference": "npp2358872734k"
    }
  },
  "shipping_details": null
}
```
