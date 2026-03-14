# Retrieve a scheduled query run

Retrieves the details of an scheduled query run.

## Returns

Returns the scheduled query run object if a valid identifier was provided.

```curl
curl https://api.stripe.com/v1/sigma/scheduled_query_runs/sqr_1NpIuH2eZvKYlo2CP72f3rLR \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "sqr_1NpIuH2eZvKYlo2CP72f3rLR",
  "object": "scheduled_query_run",
  "created": 1694472517,
  "data_load_time": 1694217600,
  "file": {
    "id": "file_1BE4yZ2eZvKYlo2C9MeXgqcB",
    "object": "file",
    "created": 1508284799,
    "expires_at": null,
    "filename": "path",
    "links": {
      "object": "list",
      "data": [],
      "has_more": false,
      "url": "/v1/file_links?file=file_1BE4yZ2eZvKYlo2C9MeXgqcB"
    },
    "purpose": "sigma_scheduled_query",
    "size": 500,
    "title": null,
    "type": "csv",
    "url": "https://files.stripe.com/v1/files/file_1BE4yZ2eZvKYlo2C9MeXgqcB/contents"
  },
  "livemode": false,
  "result_available_until": 1726012800,
  "sql": "SELECT count(*) from charges",
  "status": "completed",
  "title": "Count all charges"
}
```
