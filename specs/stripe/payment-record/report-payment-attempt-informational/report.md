# Report payment attempt informational

Report informational updates on the specified Payment Record.

## Returns

The updated Payment Record object.

## Parameters

- `id` (string, required)
  The ID of the Payment Record.

- `customer_details` (object, optional)
  Customer information for this payment.

  - `customer_details.customer` (string, optional)
    The customer who made the payment.

  - `customer_details.email` (string, optional)
    The customer’s phone number.

    The maximum length is 800 characters.

  - `customer_details.name` (string, optional)
    The customer’s name.

  - `customer_details.phone` (string, optional)
    The customer’s phone number.

- `description` (string, optional)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `metadata` (object, optional)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.

- `shipping_details` (object, optional)
  Shipping information for this payment.

  - `shipping_details.address` (object, optional)
    The physical shipping address.

    - `shipping_details.address.city` (string, optional)
      City, district, suburb, town, or village.

    - `shipping_details.address.country` (string, optional)
      Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

    - `shipping_details.address.line1` (string, optional)
      Address line 1, such as the street, PO Box, or company name.

    - `shipping_details.address.line2` (string, optional)
      Address line 2, such as the apartment, suite, unit, or building.

    - `shipping_details.address.postal_code` (string, optional)
      ZIP or postal code.

    - `shipping_details.address.state` (string, optional)
      State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

  - `shipping_details.name` (string, optional)
    The shipping recipient’s name.

  - `shipping_details.phone` (string, optional)
    The shipping recipient’s phone number.

```curl
curl https://api.stripe.com/v1/payment_records/pr_5RV730PrHyAEi/report_payment_attempt_informational \
  -u "<<YOUR_SECRET_KEY>>" \
  -d description="Updated payment description with additional context" \
  -d "metadata[order_id]"=order_12345 \
  -d "metadata[updated_by]"=customer_service \
  -d "metadata[update_reason]"=customer_inquiry \
  -d "customer_details[name]"="Jenny Rosen" \
  --data-urlencode "customer_details[email]"="jenny.rosen@example.com" \
  --data-urlencode "customer_details[phone]"="+15551234567" \
  -d "shipping_details[name]"="Jenny Rosen" \
  -d "shipping_details[address][line1]"="123 Main Street" \
  -d "shipping_details[address][line2]"="Apt 4B" \
  -d "shipping_details[address][city]"="San Francisco" \
  -d "shipping_details[address][state]"=CA \
  -d "shipping_details[address][postal_code]"=94111 \
  -d "shipping_details[address][country]"=US
```

### Response

```json
{
  "id": "pr_5RV730PrHyAEi",
  "object": "payment_record",
  "amount_canceled": {
    "currency": "usd",
    "value": 0
  },
  "amount_failed": {
    "currency": "usd",
    "value": 0
  },
  "amount_guaranteed": {
    "currency": "usd",
    "value": 0
  },
  "amount_refunded": {
    "currency": "usd",
    "value": 0
  },
  "amount_requested": {
    "currency": "usd",
    "value": 1000
  },
  "created": 1730211363,
  "customer_details": {
    "name": "Jenny Rosen",
    "email": "jenny.rosen@example.com",
    "phone": "+15551234567"
  },
  "customer_presence": "on_session",
  "description": "Updated payment description with additional context",
  "latest_payment_attempt_record": "par_1ArV730PrHyQuG",
  "livemode": true,
  "metadata": {
    "order_id": "order_12345",
    "updated_by": "customer_service",
    "update_reason": "customer_inquiry"
  },
  "payment_method_details": {
    "billing_details": null,
    "custom": {
      "display_name": "newpay",
      "type": "cpmt_125kjj3hn3sdf"
    },
    "payment_method": "pm_5j23kjksibjlks",
    "type": "custom"
  },
  "processor_details": {
    "type": "custom",
    "custom": {
      "payment_reference": "npp2358872734k"
    }
  },
  "shipping_details": {
    "name": "Jenny Rosen",
    "address": {
      "line1": "123 Main Street",
      "line2": "Apt 4B",
      "city": "San Francisco",
      "state": "CA",
      "postal_code": "94111",
      "country": "US"
    }
  }
}
```
