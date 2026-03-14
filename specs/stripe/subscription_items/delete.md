# Delete a subscription item

Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.

## Returns

An subscription item object with a deleted flag upon success. Otherwise, this call raises [an error](delete.md#errors), such as if the subscription item has already been deleted.

## Parameters

- `clear_usage` (boolean, optional)
  Delete all usage for the given subscription item. Allowed only when the current plan’s `usage_type` is `metered`.

- `payment_behavior` (enum, optional)
  Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://docs.stripe.com/docs/billing/migration/strong-customer-authentication.md) for Billing to learn more. This is the default behavior.

  Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://docs.stripe.com/docs/billing/migration/strong-customer-authentication.md), or collecting a mandate for a bank debit payment method.

  Use `pending_if_incomplete` to update the subscription using [pending updates](https://docs.stripe.com/docs/billing/subscriptions/pending-updates.md). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://docs.stripe.com/docs/billing/pending-updates-reference.md#supported-attributes).

  Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://docs.stripe.com/changelog/2019-03-14.md) to learn more.
Possible enum values:
  - `allow_incomplete`
  - `default_incomplete`
  - `error_if_incomplete`
  - `pending_if_incomplete`

- `proration_behavior` (enum, optional)
  Determines how to handle [prorations](https://docs.stripe.com/docs/billing/subscriptions/prorations.md) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item’s `quantity` changes. The default value is `create_prorations`.
Possible enum values:
  - `always_invoice`
    Always invoice immediately for prorations.

  - `create_prorations`
    Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://docs.stripe.com/docs/subscriptions/upgrading-downgrading.md#immediate-payment).

  - `none`
    Disable creating prorations in this request.

- `proration_date` (timestamp, optional)
  If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](delete.md#retrieve_customer_invoice) endpoint.

```curl
curl -X DELETE https://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "si_NcLYdDxLHxlFo7",
  "object": "subscription_item",
  "deleted": true
}
```
