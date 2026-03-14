# List all FinancialAccounts

Returns a list of FinancialAccounts.

## Returns

A dictionary with a `data` property that contains an array of up to `limit` FinancialAccounts, starting after FinancialAccount `starting_after`. Each entry in the array is a separate `FinancialAccount` object. If no more FinancialAccounts are available, the resulting array is empty.

## Parameters

- `created` (object, optional)
  Only return FinancialAccounts that were created during the given date interval.

  - `created.gt` (integer, optional)
    Minimum value to filter by (exclusive)

  - `created.gte` (integer, optional)
    Minimum value to filter by (inclusive)

  - `created.lt` (integer, optional)
    Maximum value to filter by (exclusive)

  - `created.lte` (integer, optional)
    Maximum value to filter by (inclusive)

- `ending_before` (string, optional)
  An object ID cursor for use in pagination.

- `limit` (integer, optional)
  A limit ranging from 1 to 100 (defaults to 10).

- `starting_after` (string, optional)
  An object ID cursor for use in pagination.

- `status` (enum, optional)
  Only return FinancialAccounts that have the given status: `open` or `closed`
Possible enum values:
  - `closed`
    The FinancialAccount is closed.

  - `open`
    The FinancialAccount is open.

```curl
curl -G https://api.stripe.com/v1/treasury/financial_accounts \
  -u "<<YOUR_SECRET_KEY>>" \
  -d limit=3
```

### Response

```json
{
  "object": "list",
  "url": "/v1/treasury/financial_accounts",
  "has_more": false,
  "data": [
    {
      "id": "fa_1MtZmL2eZvKYlo2Cer6cdwEC",
      "object": "treasury.financial_account",
      "active_features": [
        "financial_addresses.aba",
        "outbound_payments.ach",
        "outbound_payments.us_domestic_wire"
      ],
      "balance": {
        "cash": {
          "usd": 0
        },
        "inbound_pending": {
          "usd": 0
        },
        "outbound_pending": {
          "usd": 0
        }
      },
      "country": "US",
      "created": 1680714349,
      "financial_addresses": [
        {
          "aba": {
            "account_holder_name": "Jenny Rosen",
            "account_number_last4": "7890",
            "bank_name": "STRIPE TEST BANK",
            "routing_number": "0000000001"
          },
          "supported_networks": [
            "ach",
            "us_domestic_wire"
          ],
          "type": "aba"
        }
      ],
      "livemode": true,
      "metadata": null,
      "pending_features": [],
      "restricted_features": [],
      "status": "open",
      "status_details": {
        "closed": null
      },
      "supported_currencies": [
        "usd"
      ],
      "features": {}
    }
  ]
}
```
