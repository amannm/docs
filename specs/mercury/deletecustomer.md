# Delete a customer

Delete a customer. This action cannot be undone.

This endpoint soft deletes the customer with the given ID.

# OpenAPI definition

```json
{
  "components": {
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
    "/ar/customers/{customerId}": {
      "delete": {
        "description": "Delete a customer. This action cannot be undone.",
        "operationId": "deleteCustomer",
        "parameters": [
          {
            "in": "path",
            "name": "customerId",
            "required": true,
            "schema": {
              "description": "The customer who will receive the invoice. Use the /api/v1/ar/customers endpoint to list your customers and find the corresponding id, or create a new customer first.",
              "format": "uuid",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {}
            },
            "description": ""
          },
          "404": {
            "description": "`customerId` not found"
          }
        },
        "summary": "Delete a customer",
        "tags": [
          "Customers"
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
      "description": "Manage customers",
      "name": "Customers"
    }
  ]
}
```