# Retrieve a Report Type

Retrieves the details of a Report Type. (Certain report types require a [live-mode API key](https://stripe.com/docs/keys#test-live-modes).)

## Returns

Returns the specified `ReportType` object if found, and raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/reporting/report_types/balance.summary.1 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "balance.summary.1",
  "object": "reporting.report_type",
  "data_available_end": 1695081600,
  "data_available_start": 1667952000,
  "default_columns": [
    "category",
    "description",
    "net_amount",
    "currency"
  ],
  "livemode": false,
  "name": "Balance summary",
  "updated": 1695109133,
  "version": 1
}
```
