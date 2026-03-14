# List all Report Types

Returns a full list of Report Types.

## Returns

A dictionary with a `data` property that contains an array of Report Types. Each entry is a separate `ReportType` object.

```curl
curl https://api.stripe.com/v1/reporting/report_types \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "list",
  "url": "/v1/reporting/report_types",
  "has_more": false,
  "data": [
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
  ]
}
```
