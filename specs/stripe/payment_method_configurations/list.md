# List payment method configurations

List payment method configurations

## Returns

A list of all payment method configuration objects

## Parameters

- `application` (string, optional)
  The Connect application to filter by.

  The maximum length is 100 characters.

- `ending_before` (string, optional)
  A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.

- `limit` (integer, optional)
  A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- `starting_after` (string, optional)
  A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.

```curl
curl https://api.stripe.com/v1/payment_method_configurations \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "object": "list",
  "has_more": false,
  "data": [
    {
      "id": "pmc_1JwXwt2eZvKYlo2CHV7mUH3p",
      "object": "payment_method_configuration",
      "acss_debit": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "active": true,
      "affirm": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "afterpay_clearpay": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "alipay": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "apple_pay": {
        "available": true,
        "display_preference": {
          "overridable": null,
          "preference": "on",
          "value": "on"
        }
      },
      "bancontact": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "card": {
        "available": true,
        "display_preference": {
          "overridable": null,
          "preference": "on",
          "value": "on"
        }
      },
      "cartes_bancaires": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "eps": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "giropay": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "google_pay": {
        "available": true,
        "display_preference": {
          "overridable": null,
          "preference": "on",
          "value": "on"
        }
      },
      "ideal": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "is_default": true,
      "klarna": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "link": {
        "available": true,
        "display_preference": {
          "overridable": null,
          "preference": "on",
          "value": "on"
        }
      },
      "livemode": false,
      "name": "Default",
      "p24": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "sepa_debit": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "sofort": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "us_bank_account": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      },
      "wechat_pay": {
        "available": false,
        "display_preference": {
          "overridable": null,
          "preference": "off",
          "value": "off"
        }
      }
    }
  ]
}
```
