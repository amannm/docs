# The Scheduled Query object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `data_load_time` (timestamp)
  When the query was run, Sigma contained a snapshot of your Stripe data at this time.

- `error` (object, nullable)
  If the query run was not successful, this field contains information about the failure.

  - `error.message` (string)
    Information about the run failure.

- `file` (object, nullable)
  The file object representing the results of the query.

  - `file.id` (string)
    Unique identifier for the object.

  - `file.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `file.created` (timestamp)
    Time at which the object was created. Measured in seconds since the Unix epoch.

  - `file.expires_at` (timestamp, nullable)
    The file expires and isn’t available at this time in epoch seconds.

  - `file.filename` (string, nullable)
    The suitable name for saving the file to a filesystem.

  - `file.links` (object, nullable)
    A list of [file links](object.md#file_links) that point at this file.

    - `file.links.object` (string)
      String representing the object’s type. Objects of the same type share the same value. Always has the value `list`.

    - `file.links.data` (array of objects)
      Details about each object.

      - `file.links.data.id` (string)
        Unique identifier for the object.

      - `file.links.data.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `file.links.data.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `file.links.data.expired` (boolean)
        Returns if the link is already expired.

      - `file.links.data.expires_at` (timestamp, nullable)
        Time that the link expires.

      - `file.links.data.file` (string, expandable (can be expanded into an object with the `expand` request parameter))
        The file object this link points to.

      - `file.links.data.livemode` (boolean)
        If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

      - `file.links.data.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `file.links.data.url` (string, nullable)
        The publicly accessible URL to download the file.

    - `file.links.has_more` (boolean)
      True if this list has another page of items after this one that can be fetched.

    - `file.links.url` (string)
      The URL where this list can be accessed.

  - `file.purpose` (enum)
    The [purpose](https://docs.stripe.com/docs/file-upload.md#uploading-a-file) of the uploaded file.
Possible enum values:
    - `account_requirement`
      Additional documentation requirements that can be requested for an account.

    - `additional_verification`
      Additional verification for custom accounts.

    - `business_icon`
      A business icon.

    - `business_logo`
      A business logo.

    - `customer_signature`
      Customer signature image.

    - `dispute_evidence`
      Evidence to submit with a dispute response.

    - `finance_report_run`
      User-accessible copies of query results from the Reporting dataset.

    - `financial_account_statement`
      Financial account statements.

    - `identity_document`
      A document to verify the identity of an account owner during account provisioning.

    - `identity_document_downloadable`
      Image of a document collected by Stripe Identity.

    - `issuing_regulatory_reporting`
      Additional regulatory reporting requirements for Issuing.

    - `pci_document`
      A self-assessment PCI questionnaire.

    - `platform_terms_of_service`
      A copy of the platform’s Terms of Service.

    - `selfie`
      Image of a selfie collected by Stripe Identity.

    - `sigma_scheduled_query`
      Sigma scheduled query file for export and download.

    - `tax_document_user_upload`
      A user-uploaded tax document.

    - `terminal_android_apk`
      Android POS apps to be deployed on Stripe smart readers.

    - `terminal_reader_splashscreen`
      Splashscreen to be displayed on Terminal readers.

    - `terminal_wifi_certificate`
      Certificate used for Enterprise WiFi on Terminal readers.

    - `terminal_wifi_private_key`
      Private key used for Enterprise WiFi on Terminal readers.

  - `file.size` (integer)
    The size of the file object in bytes.

  - `file.title` (string, nullable)
    A suitable title for the document.

  - `file.type` (string, nullable)
    The returned file type (for example, `csv`, `pdf`, `jpg`, or `png`).

  - `file.url` (string, nullable)
    Use your live secret API key to download the file from this URL.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `result_available_until` (timestamp)
  Time at which the result expires and is no longer available for download.

- `sql` (string)
  SQL for the query.

- `status` (string)
  The query’s execution status, which will be `completed` for successful runs, and `canceled`, `failed`, or `timed_out` otherwise.

- `title` (string)
  Title of the query.

### The Scheduled Query object

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
