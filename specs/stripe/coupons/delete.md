# Delete a coupon

You can delete coupons via the [coupon management](https://dashboard.stripe.com/coupons) page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can’t redeem the coupon. You can also delete coupons via the API.

## Returns

An object with the deleted coupon’s ID and a deleted flag upon success. Otherwise, this call raises [an error](delete.md#errors), such as if the coupon has already been deleted.

```curl
curl -X DELETE https://api.stripe.com/v1/coupons/jMT0WJUD \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "jMT0WJUD",
  "object": "coupon",
  "deleted": true
}
```
