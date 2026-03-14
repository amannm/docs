# Retrieve a reversal

By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.

## Returns

Returns the reversal object.

```curl
curl https://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "trr_1Mio2eLkdIwHu7ixN5LPJS4a",
  "object": "transfer_reversal",
  "amount": 400,
  "balance_transaction": "txn_1Mio2eLkdIwHu7ixosfrbjhW",
  "created": 1678147568,
  "currency": "usd",
  "destination_payment_refund": "pyr_1Mio2eQ9PRzxEwkZYewpaIFB",
  "metadata": {},
  "source_refund": null,
  "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"
}
```
