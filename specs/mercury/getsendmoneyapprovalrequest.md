# Get send money approval request by ID

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
    "/request-send-money/{requestId}": {
      "get": {
        "operationId": "getSendMoneyApprovalRequest",
        "parameters": [
          {
            "in": "path",
            "name": "requestId",
            "required": true,
            "schema": {
              "description": "ID for the send money approval request",
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
                  "$ref": "#/components/schemas/SendMoneyApprovalRequestResponse"
                }
              }
            },
            "description": ""
          },
          "404": {
            "description": "`requestId` not found"
          }
        },
        "summary": "Get send money approval request by ID",
        "tags": [
          "Send Money"
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
      "description": "Manage send money approval requests",
      "name": "Send Money"
    }
  ]
}
```