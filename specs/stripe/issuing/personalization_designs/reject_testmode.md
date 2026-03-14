# Reject a testmode personalization design

Updates the `status` of the specified testmode personalization design object to `rejected`.

## Returns

Returns the updated personalization design object.

## Parameters

- `rejection_reasons` (object, required)
  The reason(s) the personalization design was rejected.

  - `rejection_reasons.card_logo` (array of enums, optional)
    The reason(s) the card logo was rejected.
Possible enum values:
    - `geographic_location`
      It improperly uses the name of a geographic location.

    - `inappropriate`
      It contains inappropriate text or images.

    - `network_name`
      It improperly uses the name of a credit card network.

    - `non_binary_image`
      The file uploaded is a non-binary image.

    - `non_fiat_currency`
      It contains a reference to non-fiat currency.

    - `other`
      Other

    - `other_entity`
      It improperly uses the name of another entity.

    - `promotional_material`
      It contains advertising, promotional material, or a tagline.

  - `rejection_reasons.carrier_text` (array of enums, optional)
    The reason(s) the carrier text was rejected.
Possible enum values:
    - `geographic_location`
      It improperly uses the name of a geographic location.

    - `inappropriate`
      It contains inappropriate text or images.

    - `network_name`
      It improperly uses the name of a credit card network.

    - `non_fiat_currency`
      It contains a reference to non-fiat currency.

    - `other`
      Other

    - `other_entity`
      It improperly uses the name of another entity.

    - `promotional_material`
      It contains advertising, promotional material, or a tagline.

```curl
curl https://api.stripe.com/v1/test_helpers/issuing/personalization_designs/ipcd_Oiw9GXcFRE81LZ/reject \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "rejection_reasons[card_logo][]"=network_name \
  -d "rejection_reasons[card_logo][]"=inappropriate \
  -d "rejection_reasons[carrier_text][]"=other
```

### Response

```json
{
  "id": "ipcd_Oiw9GXcFRE81LZ",
  "object": "issuing.personalization_design",
  "livemode": false,
  "card_logo": "file_1LzR9L2eZvKYlo2CelTpcvKu",
  "carrier_text": null,
  "lookup_key": "my_card_design_lookup_key",
  "metadata": {},
  "name": "My personalization design name",
  "physical_bundle": "ics_Oiw9ahglMfql0U",
  "preferences": {
    "is_default": false
  },
  "rejection_reasons": {
    "card_logo": [
      "network_name",
      "inappropriate"
    ],
    "carrier_text": [
      "other"
    ]
  },
  "status": "rejected"
}
```
