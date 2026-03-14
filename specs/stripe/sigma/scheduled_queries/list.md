# List all scheduled query runs

Returns a list of scheduled query runs.

## Returns

A paginated list of all scheduled query runs.

## Parameters

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl -G https://api.stripe.com/v1/sigma/scheduled_query_runs \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/sigma/scheduled_query_runs",
  "has_more": false,
  "data": [
    {
      "object": "list",
      "url": "/v1/sigma/scheduled_query_runs",
      "has_more": false,
      "data": [
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
      ]
    }
  ]
}
```
