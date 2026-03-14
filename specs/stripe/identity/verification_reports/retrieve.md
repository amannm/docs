# Retrieve a VerificationReport

Retrieves an existing VerificationReport

## Returns

Returns a VerificationReport object

```curl
curl https://api.stripe.com/v1/identity/verification_reports/vr_1MwBlH2eZvKYlo2C91hOpFMf \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
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
```
