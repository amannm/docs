# The Report Run object

## Attributes

- `id` (string)
  The unique identifier of the `ReportRun` object.

- `object` (string, value is "v2.reporting.report_run")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `created` (timestamp)
  Time at which the object was created.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `report` (string)
  The unique identifier of the `Report` object which was run.

- `report_name` (string)
  The human-readable name of the `Report` which was run.

- `report_parameters` (map)
  The parameters used to customize the generation of the report.

- `result` (object, nullable)
  Details how to retrieve the results of a successfully completed `ReportRun`.

  - `result.file` (object)
    Contains metadata about the file produced by the `ReportRun`, including its content type, size, and a URL to download its contents.

    - `result.file.content_type` (enum)
      The content type of the file.
Possible enum values:
      - `csv`
        CSV content type. Mime type of `text/csv`.

      - `zip`
        ZIP content type. Mime type of `application/zip`.

    - `result.file.download_url` (object)
      A pre-signed URL that allows secure, time-limited access to download the file.

      - `result.file.download_url.expires_at` (timestamp, nullable)
        The time that the URL expires.

      - `result.file.download_url.url` (string)
        The URL that can be used for accessing the file.

    - `result.file.size` (integer)
      The total size of the file in bytes.

  - `result.type` (enum)
    The type of the `ReportRun` result.
Possible enum values:
    - `file`
      File result type.

- `result_options` (object, nullable)
  The options specified for customizing the output file of the `ReportRun`.

  - `result_options.compress_file` (boolean, nullable)
    If set, the generated report file will be compressed into a ZIP folder. This is useful for reducing file size and download time for large reports.

- `status` (enum)
  The current status of the `ReportRun`.
Possible enum values:
  - `failed`
    Report has failed to complete due to an error.

  - `running`
    Report generation is in progress.

  - `succeeded`
    Report has successfully generated.

- `status_details` (map)
  Additional details about the current state of the `ReportRun`. The field is currently only populated when a `ReportRun` is in the `failed` state, providing more information about why the report failed to generate successfully.

### The Report Run object

```json
{
  "created": "2025-08-26T00:00:00.000Z",
  "id": "reprun_test_xxx",
  "object": "v2.reporting.report_run",
  "report": "report_test_xxx",
  "report_name": "test report name",
  "report_parameters": {
    "interval_start": "2025-08-18T00:00:00.000Z",
    "interval_end": "2025-08-25T00:00:00.000Z"
  },
  "result": null,
  "result_options": {
    "compress_file": false
  },
  "status": "running",
  "status_details": {},
  "livemode": false
}
```
