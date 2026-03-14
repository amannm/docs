# Get account by ID

<br />

# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "Account": {
        "properties": {
          "accountNumber": {
            "type": "string"
          },
          "availableBalance": {
            "multipleOf": 0.01,
            "type": "number"
          },
          "canReceiveTransactions": {
            "nullable": true,
            "type": "boolean"
          },
          "createdAt": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              }
            ]
          },
          "currentBalance": {
            "multipleOf": 0.01,
            "type": "number"
          },
          "dashboardLink": {
            "type": "string"
          },
          "id": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              }
            ]
          },
          "kind": {
            "type": "string"
          },
          "legalBusinessName": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "nickname": {
            "nullable": true,
            "type": "string"
          },
          "routingNumber": {
            "type": "string"
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AccountStatus"
              }
            ]
          },
          "type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AccountType"
              }
            ]
          }
        },
        "required": [
          "id",
          "accountNumber",
          "routingNumber",
          "name",
          "status",
          "type",
          "createdAt",
          "availableBalance",
          "currentBalance",
          "kind",
          "legalBusinessName",
          "dashboardLink"
        ],
        "type": "object"
      },
      "AccountStatus": {
        "enum": [
          "active",
          "deleted",
          "pending",
          "archived"
        ],
        "type": "string"
      },
      "AccountType": {
        "enum": [
          "mercury",
          "external",
          "recipient"
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
    "/account/{accountId}": {
      "get": {
        "operationId": "getAccount",
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
                  "$ref": "#/components/schemas/Account"
                }
              }
            },
            "description": ""
          },
          "404": {
            "description": "`accountId` not found"
          }
        },
        "summary": "Get account by ID",
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