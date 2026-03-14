# Retrieve a physical bundle

Retrieves a physical bundle object.

## Returns

Returns the physical bundle object.

```curl
curl https://api.stripe.com/v1/issuing/physical_bundles/ics_NLuXJPDYSTjFON \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "ics_NLuXJPDYSTjFON",
  "object": "issuing.physical_bundle",
  "livemode": false,
  "name": "US Visa Credit White",
  "features": {
    "card_logo": "required",
    "carrier_text": "optional"
  },
  "status": "active",
  "type": "standard"
}
```
