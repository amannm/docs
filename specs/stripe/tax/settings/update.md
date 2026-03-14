# Update settings

Updates Tax `Settings` parameters used in tax calculations. All parameters are editable but none can be removed once set.

## Returns

A Tax `Settings` object.

## Parameters

- `defaults` (object, optional)
  Default configuration to be used on Stripe Tax calculations.

  - `defaults.tax_behavior` (enum, optional)
    Specifies the default [tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#tax-behavior) to be used when the item’s price has unspecified tax behavior. One of inclusive, exclusive, or inferred_by_currency. Once specified, it cannot be changed back to null.
Possible enum values:
    - `exclusive`
    - `inclusive`
    - `inferred_by_currency`

  - `defaults.tax_code` (string, optional)
    A [tax code](https://docs.stripe.com/docs/tax/tax-categories.md) ID.

- `head_office` (object, optional)
  The place where your business is located.

  - `head_office.address` (object, required)
    The location of the business for tax purposes.

    - `head_office.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `head_office.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `head_office.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `head_office.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `head_office.address.postal_code` (string, optional)
      ZIP or postal code.

    - `head_office.address.state` (string, optional)
      State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix, such as “NY” or “TX”.

```curl
curl https://api.stripe.com/v1/tax/settings \
  -u "<<YOUR_SECRET_KEY>>" \
  -d "defaults[tax_behavior]"=inclusive \
  -d "defaults[tax_code]"=txcd_10000000 \
  -d "head_office[address][country]"=DE
```

### Response

```json
{
  "object": "tax.settings",
  "defaults": {
    "tax_behavior": "inclusive",
    "tax_code": "txcd_10000000"
  },
  "head_office": {
    "address": {
      "city": null,
      "country": "DE",
      "line1": null,
      "line2": null,
      "postal_code": null,
      "state": null
    }
  },
  "livemode": false,
  "status": "active",
  "status_details": {
    "active": {}
  }
}
```
