# Get an invoice

Retrieve details of an invoice by its ID

# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "ApiV1ArInvoiceResponse": {
        "description": " The response type for an invoice in the api.",
        "properties": {
          "achDebitEnabled": {
            "description": " Whether or not the invoice can be paid via ach debit.",
            "type": "boolean"
          },
          "amount": {
            "allOf": [
              {
                "$ref": "#/components/schemas/NonNegativeDollar"
              },
              {
                "description": " The total amount of the invoice line items plus taxes."
              }
            ]
          },
          "canceledAt": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              },
              {
                "description": " The time when the invoice was canceled."
              }
            ],
            "nullable": true
          },
          "ccEmails": {
            "description": " Emails to be CCed on invoice notifications/reminders.",
            "items": {
              "$ref": "#/components/schemas/Email"
            },
            "type": "array"
          },
          "createdAt": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              },
              {
                "description": " The timestamp when the invoice was created."
              }
            ]
          },
          "creditCardEnabled": {
            "description": " Whether or not the invoice can be paid via credit card. Requires stripe to be\n setup for the Mercury account.",
            "type": "boolean"
          },
          "customerId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerId"
              },
              {
                "description": " Id of the customer the invoice was sent to."
              }
            ]
          },
          "destinationAccountId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              },
              {
                "description": " The Mercury account where invoice payments will be deposited. Use the /api/v1/accounts endpoint to list your accounts and find the corresponding id. Only checking and savings accounts are supported."
              }
            ]
          },
          "dueDate": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Day"
              },
              {
                "description": " The due date the invoice should be paid by."
              }
            ]
          },
          "id": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InvoiceId"
              },
              {
                "description": " The ID of the invoice."
              }
            ]
          },
          "internalNote": {
            "description": " Internal note for the invoice, visible by users in the\n mercury organization but not visible to payers.",
            "nullable": true,
            "type": "string"
          },
          "invoiceDate": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Day"
              },
              {
                "description": " The date of the invoice, set by the invoice creator\n and likely to be context specific to the type of transaction.\n i.e. it could be a date a service was performed, it does not need\n to be the date the invoice was created."
              }
            ]
          },
          "invoiceNumber": {
            "description": " The payer facing invoice number/identifier.",
            "type": "string"
          },
          "lineItems": {
            "description": " The line items for the invoice.",
            "items": {
              "$ref": "#/components/schemas/ApiV1ArLineItemData"
            },
            "type": "array"
          },
          "payerMemo": {
            "description": " Memo for the payer of the invoice.",
            "nullable": true,
            "type": "string"
          },
          "poNumber": {
            "description": " Purchase order number for the invoice if applicable.",
            "nullable": true,
            "type": "string"
          },
          "servicePeriodEndDate": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Day"
              },
              {
                "description": " The end date for the service period this invoice covers, if applicable. YYYY-MM-DD"
              }
            ],
            "nullable": true
          },
          "servicePeriodStartDate": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Day"
              },
              {
                "description": " The start date for the service period this invoice covers, if applicable. YYYY-MM-DD"
              }
            ],
            "nullable": true
          },
          "slug": {
            "description": " Public slug for an invoice. Used to construct the pay page URL\n as well as the URL to retrieve the PDF of the invoice.",
            "type": "string"
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PaymentLinkStatus"
              },
              {
                "description": " The status of the invoice."
              }
            ]
          },
          "updatedAt": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              },
              {
                "description": " The timestamp when the invoice was updated."
              }
            ]
          },
          "useRealAccountNumber": {
            "description": " Whether or not the invoice payment instructions will show the real\n account and routing number for the destination account or use\n virtual account numbers instead.",
            "type": "boolean"
          }
        },
        "required": [
          "id",
          "dueDate",
          "invoiceDate",
          "invoiceNumber",
          "customerId",
          "ccEmails",
          "slug",
          "status",
          "amount",
          "destinationAccountId",
          "creditCardEnabled",
          "achDebitEnabled",
          "useRealAccountNumber",
          "createdAt",
          "updatedAt",
          "lineItems"
        ],
        "type": "object"
      },
      "ApiV1ArLineItemData": {
        "description": " Data for an invoice line item",
        "properties": {
          "name": {
            "description": " the name of the line item",
            "type": "string"
          },
          "quantity": {
            "description": " the quantity of this item",
            "format": "double",
            "type": "number"
          },
          "salesTaxRate": {
            "description": " the sales tax applied to this item",
            "format": "double",
            "nullable": true,
            "type": "number"
          },
          "unitPrice": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Dollar"
              },
              {
                "description": " the price of one unit of the item before sales tax"
              }
            ]
          }
        },
        "required": [
          "name",
          "unitPrice",
          "quantity"
        ],
        "type": "object"
      },
      "CustomerId": {
        "description": "The customer who will receive the invoice. Use the /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or create a new customer first.",
        "format": "uuid",
        "type": "string"
      },
      "Day": {
        "example": "2016-07-22",
        "format": "date",
        "type": "string"
      },
      "Dollar": {
        "description": "A dollar amount",
        "format": "double",
        "type": "number"
      },
      "Email": {
        "type": "string"
      },
      "InvoiceId": {
        "description": "ID for the invoice.",
        "format": "uuid",
        "type": "string"
      },
      "NonNegativeDollar": {
        "description": "A positive dollar amount with at least 1 cent.",
        "format": "double",
        "minimum": 0.01,
        "type": "number"
      },
      "PaymentLinkStatus": {
        "enum": [
          "Unpaid",
          "Paid",
          "Cancelled",
          "Processing"
        ],
        "type": "string"
      },
      "TransactionPartyId": {
        "description": "ID for a Mercury account.",
        "format": "uuid",
        "type": "string"
      },
      "UTCTime": {
        "example": "2016-07-22T00:00:00Z",
        "format": "yyyy-mm-ddThh:MM:ssZ",
        "type": "string"
      }
    },
    "securitySchemes": {
      "basicAuth": {
        "description": "Basic authentication for Mercury API.\n\nUse your API token as the username with an empty password.\n\nExample:\nUsername: `secret-token:mercury_production_wma_24SCp4G81X3yHL4Wq8FgzuaP9ye3VKf2mgTDctXyRg5HY_yrucrem`\nPassword: (empty)\n",
        "scheme": "basic",
        "type": "http"
      },
      "bearerAuth": {
        "description": "Bearer token authentication for Mercury API.\n\nUse your API token in the Authorization header:\n`Authorization: Bearer TOKEN`\n\nExample:\n`Authorization: Bearer secret-token:mercury_production_wma_24SCp4G81X3yHL4Wq8FgzuaP9ye3VKf2mgTDctXyRg5HY_yrucrem`\n\nYour Mercury API token should include the 'secret-token:' prefix.\nTokens can be generated from your Mercury dashboard settings.\n",
        "scheme": "bearer",
        "type": "http"
      }
    }
  },
  "info": {
    "description": "Streamline financial tasks with secure account management and transaction processing. Enables user registration, balance tracking, and payment handling.",
    "title": "Mercury API",
    "version": "1.0.0"
  },
  "openapi": "3.0.0",
  "paths": {
    "/ar/invoices/{invoiceId}": {
      "get": {
        "description": "Retrieve details of an invoice by its ID",
        "operationId": "getInvoice",
        "parameters": [
          {
            "in": "path",
            "name": "invoiceId",
            "required": true,
            "schema": {
              "description": "ID for the invoice.",
              "format": "uuid",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ApiV1ArInvoiceResponse"
                }
              }
            },
            "description": ""
          },
          "404": {
            "description": "`invoiceId` not found"
          }
        },
        "summary": "Get an invoice",
        "tags": [
          "Invoices"
        ]
      }
    }
  },
  "security": [
    {
      "bearerAuth": []
    },
    {
      "basicAuth": []
    }
  ],
  "servers": [
    {
      "description": "Mercury API URL",
      "url": "https://api.mercury.com/api/v1"
    }
  ],
  "tags": [
    {
      "description": "Manage invoices",
      "name": "Invoices"
    }
  ]
}
```