# List all Report Runs

Returns a list of Report Runs, with the most recent appearing first.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` Report Runs, starting after the argument `starting_after` if it is provided. Each entry in the array is a separate `ReportRun` object. If no more Report Runs are available, the resulting array will be empty.

## Parameters

- `created` (object, optional)
  Only return Report Runs that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/reporting/report_runs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/reporting/report_runs",
  "has_more": false,
  "data": [
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
  ]
}
```
