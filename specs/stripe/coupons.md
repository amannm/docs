# Coupons

A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to [subscriptions](coupons.md#subscriptions), [invoices](coupons.md#invoices), [checkout sessions](https://docs.stripe.com/docs/api/checkout/sessions.md), [quotes](coupons.md#quotes), and more. Coupons do not work with conventional one-off [charges](coupons.md#create_charge) or [payment intents](https://docs.stripe.com/docs/api/payment_intents.md).

## Endpoints

### Create a coupon

- [POST /v1/coupons](coupons/create.md)

### Update a coupon

- [POST /v1/coupons/:id](coupons/update.md)

### Retrieve a coupon

- [GET /v1/coupons/:id](coupons/retrieve.md)

### List all coupons

- [GET /v1/coupons](coupons/list.md)

### Delete a coupon

- [DELETE /v1/coupons/:id](coupons/delete.md)
