# Simulate an input collection timeout

Use this endpoint to complete an input collection with a timeout error on a simulated reader.

## Returns

Returns an updated `Reader` resource.

```curl
curl -X POST https://api.stripe.com/v1/test_helpers/terminal/readers/tmr_FDOt2wlRZEdpd7/timeout_input_collection \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "tmr_FDOt2wlRZEdpd7",
  "object": "terminal.reader",
  "action": {
    "failure_code": "collect_inputs_timeout",
    "failure_message": "collect inputs was timed out",
    "collect_inputs": {
      "inputs": [
        {
          "type": "signature",
          "custom_text": {
            "title": "Signature",
            "description": "Please sign below",
            "submit_button": "Submit",
            "skip_button": "Skip"
          },
          "required": false,
          "signature": {
            "value": null
          }
        },
        {
          "type": "selection",
          "custom_text": {
            "title": "Selection",
            "description": "Please select one"
          },
          "required": true,
          "selection": {
            "choices": [
              {
                "style": "primary",
                "value": "choice_1"
              },
              {
                "style": "secondary",
                "value": "choice_2"
              }
            ],
            "value": null
          }
        },
        {
          "type": "email",
          "custom_text": {
            "title": "Enter your email",
            "description": "We'll send updates on your order and occasional deals",
            "submit_button": "Submit",
            "skip_button": "Skip"
          },
          "required": false,
          "email": {
            "value": null
          }
        }
      ]
    },
    "status": "failed",
    "type": "collect_inputs"
  },
  "device_deploy_group": null,
  "device_sw_version": null,
  "device_type": "bbpos_wisepos_e",
  "ip_address": "192.168.2.2",
  "label": "Blue Rabbit",
  "livemode": false,
  "location": null,
  "metadata": {},
  "serial_number": "123-456-789",
  "status": "online"
}
```
