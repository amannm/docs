# Retrieve an early fraud warning

Retrieves the details of an early fraud warning that has previously been created.

Please refer to the [early fraud warning](retrieve.md#early_fraud_warning_object) object reference for more details.

## Returns

Returns an EarlyFraudWarning if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/radar/early_fraud_warnings/issfr_1NnrwHBw2dPENLoi9lnhV3RQ \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "issfr_1NnrwHBw2dPENLoi9lnhV3RQ",
  "object": "radar.early_fraud_warning",
  "actionable": true,
  "charge": "ch_1234",
  "created": 123456789,
  "fraud_type": "misc",
  "livemode": false
}
```
