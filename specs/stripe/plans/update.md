# Update a plan

Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.

## Returns

The updated plan object is returned upon success. Otherwise, this call raises [an error](update.md#errors).

## Parameters

- `active` (boolean, optional)
  Whether the plan is currently available for new subscriptions.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `nickname` (string, optional)
  A brief description of the plan, hidden from customers.

- `product` (string, optional)
  The product the plan belongs to. This cannot be changed once it has been used in a subscription or subscription schedule.

- `trial_period_days` (integer, optional)
  Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://docs.stripe.com/docs/api.md#create_subscription-trial_from_plan).

```curl
curl https://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "metadata[order_id]"=6735
```

### Response

```json
{
  "id": "plan_NjpIbv3g3ZibnD",
  "object": "plan",
  "active": true,
  "amount": 1200,
  "amount_decimal": "1200",
  "billing_scheme": "per_unit",
  "created": 1681851647,
  "currency": "usd",
  "interval": "month",
  "interval_count": 1,
  "livemode": false,
  "metadata": {
    "order_id": "6735"
  },
  "nickname": null,
  "product": "prod_NjpI7DbZx6AlWQ",
  "tiers_mode": null,
  "transform_usage": null,
  "trial_period_days": null,
  "usage_type": "licensed"
}
```
