# Retrieve payment method configuration

Retrieve payment method configuration

## Returns

A payment method configuration object.

```curl
curl https://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \
  -u "<<YOUR_SECRET_KEY>>"
```

### Response

```json
{
  "id": "pmc_abcdef",
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
```
