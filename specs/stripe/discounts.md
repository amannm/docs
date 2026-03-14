# Discounts

A discount represents the actual application of a [coupon](discounts.md#coupons) or [promotion code](discounts.md#promotion_codes). It contains information about when the discount began, when it will end, and what it is applied to.

Related guide: [Applying discounts to subscriptions](https://docs.stripe.com/docs/billing/subscriptions/discounts.md)

## Endpoints

### Delete a customer discount

- [DELETE /v1/customers/:id/discount](discounts/delete.md)

### Delete a subscription discount

- [DELETE /v1/subscriptions/:id/discount](discounts/subscription_delete.md)
