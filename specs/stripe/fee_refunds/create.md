# Create an application fee refund

Refunds an application fee that has previously been collected but not yet refunded. Funds will be refunded to the Stripe account from which the fee was originally collected.

You can optionally refund only part of an application fee. You can do so multiple times, until the entire fee has been refunded.

Once entirely refunded, an application fee can’t be refunded again. This method will raise an error when called on an already-refunded application fee, or when trying to refund more money than is left on an application fee.

## Returns

Returns the `Application Fee Refund` object if the refund succeeded. Raises [an error](create.md#errors) if the fee has already been refunded, or if an invalid fee identifier was provided.

## Parameters

- `amount` (integer, optional)
  A positive integer, in *cents*, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

```curl
curl -X POST https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",
  "object": "fee_refund",
  "amount": 100,
  "balance_transaction": null,
  "created": 1680651573,
  "currency": "usd",
  "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",
  "metadata": {}
}
```
