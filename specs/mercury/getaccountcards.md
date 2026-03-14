# Get cards for account

Retrieve all debit and credit cards associated with a specific account.

# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "AccountCard": {
        "properties": {
          "cardId": {
            "type": "string"
          },
          "createdAt": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              }
            ]
          },
          "lastFourDigits": {
            "type": "string"
          },
          "nameOnCard": {
            "type": "string"
          },
          "network": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CardNetwork"
              }
            ]
          },
          "physicalCardStatus": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PhysicalCardStatus"
              }
            ],
            "nullable": true
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CardStatus"
              }
            ]
          }
        },
        "required": [
          "cardId",
          "nameOnCard",
          "lastFourDigits",
          "network",
          "status",
          "createdAt"
        ],
        "type": "object"
      },
      "AccountCardsResponse": {
        "properties": {
          "cards": {
            "items": {
              "$ref": "#/components/schemas/AccountCard"
            },
            "type": "array"
          }
        },
        "required": [
          "cards"
        ],
        "type": "object"
      },
      "CardNetwork": {
        "enum": [
          "visa",
          "mastercard"
        ],
        "type": "string"
      },
      "CardStatus": {
        "enum": [
          "active",
          "frozen",
          "cancelled",
          "inactive",
          "expired",
          "suspended"
        ],
        "type": "string"
      },
      "PhysicalCardStatus": {
        "enum": [
          "inactive",
          "active",
          "paused"
        ],
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
    "/account/{accountId}/cards": {
      "get": {
        "description": "Retrieve all debit and credit cards associated with a specific account.",
        "operationId": "getAccountCards",
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
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AccountCardsResponse"
                }
              }
            },
            "description": ""
          },
          "404": {
            "description": "`accountId` not found"
          }
        },
        "summary": "Get cards for account",
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