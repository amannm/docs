# The Report object

## Attributes

- `id` (string)
  The unique identifier of the `Report` object.

- `object` (string, value is "v2.reporting.report")
  String representing the object’s type. Objects of the same type share the same value of the object field.

- `livemode` (boolean)
  Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.

- `name` (string)
  The human-readable name of the `Report`.

- `parameters` (map)
  Specification of the parameters that the `Report` accepts. It details each parameter’s name, description, whether it is required, and any validations performed.

### The Report object

```json
{
  "id": "report_test_xxx",
  "name": "test report name",
  "object": "v2.reporting.report",
  "parameters": {
    "columns": {
      "array_details": {
        "element_type": "enum",
        "enum_details": {
          "allowed_values": [
            "column_1",
            "column_2"
          ]
        }
      },
      "description": "Set of output columns requested for inclusion in the report.",
      "enum_details": false,
      "required": true,
      "timestamp_details": null,
      "type": "array"
    },
    "interval_start": {
      "array_details": null,
      "description": "",
      "enum_details": null,
      "required": true,
      "timestamp_details": {
        "max": "2025-08-26T14:00:00.000Z",
        "min": "2025-03-11T00:00:00.000Z"
      },
      "type": "timestamp"
    },
    "interval_end": {
      "array_details": null,
      "description": "",
      "enum_details": null,
      "required": true,
      "timestamp_details": {
        "max": "2025-08-26T14:00:00.000Z",
        "min": "2025-03-11T00:00:00.000Z"
      },
      "type": "timestamp"
    },
    "category": {
      "array_details": null,
      "description": "",
      "enum_details": {
        "allowed_values": [
          "enum_value_1",
          "enum_value_2"
        ]
      },
      "required": false,
      "timestamp_details": null,
      "type": "enum"
    }
  },
  "livemode": false
}
```
