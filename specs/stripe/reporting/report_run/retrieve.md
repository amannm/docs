# Retrieve a Report Run

Retrieves the details of an existing Report Run.

## Returns

Returns the specified `ReportRun` object if found, and raises [an error](retrieve.md#errors) otherwise.

```curl
curl https://api.stripe.com/v1/reporting/report_runs/frr_1MrQwrLkdIwHu7ixUov4x2b3 \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",
  "object": "reporting.report_run",
  "created": 1680203749,
  "error": null,
  "livemode": false,
  "parameters": {
    "interval_end": 1680100000,
    "interval_start": 1680000000
  },
  "report_type": "balance.summary.1",
  "result": null,
  "status": "pending",
  "succeeded_at": null
}
```
