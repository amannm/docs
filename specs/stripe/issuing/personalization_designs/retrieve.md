# Retrieve a personalization design

Retrieves a personalization design object.

## Returns

Returns the personalization design object.

```curl
curl https://api.stripe.com/v1/issuing/personalization_designs/ipcd_Oiw9GXcFRE81LZ \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ipcd_Oiw9GXcFRE81LZ",
  "object": "issuing.personalization_design",
  "livemode": true,
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
    "card_logo": [],
    "carrier_text": []
  },
  "status": "review"
}
```
