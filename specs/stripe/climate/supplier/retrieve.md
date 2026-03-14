# Retrieve a supplier

Retrieves a Climate supplier object.

## Returns

A Climate supplier object.

```curl
curl https://api.stripe.com/v1/climate/suppliers/climsup_charm_industrial \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "climsup_charm_industrial",
  "object": "climate.supplier",
  "info_url": "https://frontierclimate.com/portfolio/charm-industrial",
  "livemode": false,
  "locations": [
    {
      "city": "San Francisco",
      "country": "US",
      "latitude": 37.7749,
      "longitude": -122.4194,
      "region": "CA"
    }
  ],
  "name": "Charm Industrial",
  "removal_pathway": "biomass_carbon_removal_and_storage"
}
```
