# Set reader display

Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display.md).

## Returns

Returns an updated `Reader` resource.

## Parameters

- `type` (enum, required)
  Type of information to display. Only `cart` is currently supported.

- `cart` (object, optional)
  Cart details to display on the reader screen, including line items, amounts, and currency.

  - `cart.currency` (enum, required)
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

  - `cart.line_items` (array of objects, required)
    Array of line items to display.

    - `cart.line_items.amount` (integer, required)
      The price of the item in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

    - `cart.line_items.description` (string, required)
      The description or name of the item.

    - `cart.line_items.quantity` (integer, required)
      The quantity of the line item being purchased.

  - `cart.total` (integer, required)
    Total balance of cart due in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

  - `cart.tax` (integer, optional)
    The amount of tax in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

```curl
curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/set_reader_display \
  -u "<<YOUR_SECRET_KEY>>" \
  -d type=cart \
  -d "cart[currency]"=usd \
  -d "cart[line_items][0][amount]"=5100 \
  -d "cart[line_items][0][description]"="Red t-shirt" \
  -d "cart[line_items][0][quantity]"=1 \
  -d "cart[tax]"=100 \
  -d "cart[total]"=5200
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "set_reader_display": {
      "cart": {
        "currency": "usd",
        "line_items": [
          {
            "amount": 5100,
            "description": "Red t-shirt",
            "quantity": 1
          }
        ],
        "tax": 100,
        "total": 5200
      },
      "type": "cart"
    },
    "status": "in_progress",
    "type": "set_reader_display"
  },
  "device_sw_version": "2.37.2.0",
  "device_type": "simulated_wisepos_e",
  "ip_address": "0.0.0.0",
  "label": "Blue Rabbit",
  "last_seen_at": 1695166525506,
  "livemode": false,
  "location": "tml_FDOtHwxAAdIJOh",
  "metadata": {},
  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",
  "status": "online"
}
```
