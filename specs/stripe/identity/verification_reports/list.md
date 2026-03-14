# List VerificationReports

List all verification reports.

## Returns

List of VerificationInent objects that match the provided filter criteria.

## Parameters

- `client_reference_id` (string, optional)
  A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- `created` (object, optional)
  Only return VerificationReports that were created during the given date interval.

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

- `type` (enum, optional)
  Only return VerificationReports of this type
Possible enum values:
  - `document`
    Perform a document check.

  - `id_number`
    Perform an ID number check.

- `verification_session` (string, optional)
  Only return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID.

```curl
curl -G https://api.stripe.com/v1/identity/verification_reports \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/identity/verification_reports",
  "has_more": false,
  "data": [
    {
      "id": "vr_1MwBlH2eZvKYlo2C91hOpFMf",
      "object": "identity.verification_report",
      "created": 1681337011,
      "livemode": false,
      "options": {
        "document": {}
      },
      "type": "document",
      "verification_session": "vs_NhaxYCqOE27AqaUTxbIZOnHw",
      "document": {
        "status": "verified",
        "error": null,
        "first_name": "Jenny",
        "last_name": "Rosen",
        "address": {
          "line1": "1234 Main St.",
          "city": "San Francisco",
          "state": "CA",
          "zip": "94111",
          "country": "US"
        },
        "type": "driving_license",
        "files": [
          "file_NhaxRCXT8Iuu8apSuci00UC4",
          "file_NhaxDeWKGAOTc8Uec7UY9Ljj"
        ],
        "expiration_date": {
          "month": 12,
          "day": 1,
          "year": 2025
        },
        "issued_date": {
          "month": 12,
          "day": 1,
          "year": 2020
        },
        "issuing_country": "US"
      }
    }
  ]
}
```
