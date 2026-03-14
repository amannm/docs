# Request to send money

Create a "request to send money" that will require approval based on your organization's approval policies.

**Scope:** Send Money with Approval (does not require an IP whitelist)

For an implementation guide and acceptable uses for this endpoint, refer to
[the Create Transaction docs](createtransaction.md#/).

#### Note:

This endpoint provides a way to queue payments that require approval from the web interface. The user approving the payment will need to be different than the user who created the API Token, and the approving user will need to have proper send money permissions.

Since this endpoint requires approval to send money, an IP whitelist is not required if using this endpoint with a Custom token. Thus, this endpoint may be useful in situations where a static IP is not available.

# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "PositiveDollar": {
        "description": "A positive dollar amount with at least 1 cent.",
        "format": "double",
        "minimum": 0.01,
        "type": "number"
      },
      "RequestSendMoneyPaymentMethod": {
        "enum": [
          "ach",
          "check",
          "domesticWire",
          "internationalWire"
        ],
        "type": "string"
      },
      "ReviewRequestStatus": {
        "enum": [
          "pendingApproval",
          "approved",
          "rejected",
          "cancelled"
        ],
        "type": "string"
      },
      "SendMoneyAPIRequest": {
        "properties": {
          "amount": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PositiveDollar"
              }
            ],
            "description": "Amount of USD you want to send, must be a positive number."
          },
          "externalMemo": {
            "description": "Optional external memo",
            "type": "string"
          },
          "idempotencyKey": {
            "description": "Unique string identifying the transaction",
            "type": "string"
          },
          "note": {
            "description": "Optional note",
            "type": "string"
          },
          "paymentMethod": {
            "allOf": [
              {
                "$ref": "#/components/schemas/RequestSendMoneyPaymentMethod"
              }
            ],
            "description": "Payment method to use."
          },
          "recipientId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              }
            ],
            "description": "Recipient ID from the /recipients endpoint."
          }
        },
        "required": [
          "recipientId",
          "amount",
          "paymentMethod",
          "idempotencyKey"
        ],
        "type": "object"
      },
      "SendMoneyApprovalRequestResponse": {
        "description": " Extremely close to the internal type, but strips out potentially unwanted fields",
        "properties": {
          "accountId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              }
            ]
          },
          "amount": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PositiveDollar"
              }
            ]
          },
          "memo": {
            "nullable": true,
            "type": "string"
          },
          "paymentMethod": {
            "allOf": [
              {
                "$ref": "#/components/schemas/RequestSendMoneyPaymentMethod"
              }
            ]
          },
          "recipientId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              }
            ]
          },
          "requestId": {
            "type": "string"
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ReviewRequestStatus"
              }
            ]
          }
        },
        "required": [
          "accountId",
          "requestId",
          "recipientId",
          "paymentMethod",
          "amount",
          "status"
        ],
        "type": "object"
      },
      "TransactionPartyId": {
        "description": "ID for a Mercury account.",
        "format": "uuid",
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
    "/account/{accountId}/request-send-money": {
      "post": {
        "description": "Create a \"request to send money\" that will require approval based on your organization's approval policies.",
        "operationId": "requestSendMoney",
        "parameters": [
          {
            "in": "path",
            "name": "accountId",
            "required": true,
            "schema": {
              "description": "ID for a Mercury account.",
              "format": "uuid",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SendMoneyAPIRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SendMoneyApprovalRequestResponse"
                }
              }
            },
            "description": ""
          },
          "400": {
            "description": "Invalid `body`"
          },
          "404": {
            "description": "`accountId` not found"
          }
        },
        "summary": "Request to send money",
        "tags": [
          "Accounts"
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
      "description": "Manage bank accounts",
      "name": "Accounts"
    }
  ]
}
```