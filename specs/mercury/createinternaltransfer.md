# Create an internal transfer

Transfer funds between two accounts within the same organization. Supports transfers between depository accounts (checking/savings), from a depository account to a treasury/investment account, and from a treasury/investment account to a depository account. Creates paired debit and credit transactions.

# OpenAPI definition

```json
{
  "components": {
    "schemas": {
      "AddressData": {
        "properties": {
          "address1": {
            "type": "string"
          },
          "address2": {
            "nullable": true,
            "type": "string"
          },
          "city": {
            "type": "string"
          },
          "postalCode": {
            "type": "string"
          },
          "state": {
            "allOf": [
              {
                "$ref": "#/components/schemas/USState"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "address1",
          "city",
          "postalCode"
        ],
        "type": "object"
      },
      "AddressWithoutName": {
        "properties": {
          "address1": {
            "type": "string"
          },
          "address2": {
            "nullable": true,
            "type": "string"
          },
          "city": {
            "type": "string"
          },
          "country": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ISO3166Alpha2"
              }
            ]
          },
          "postalCode": {
            "type": "string"
          },
          "region": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Region"
              }
            ]
          }
        },
        "required": [
          "address1",
          "city",
          "region",
          "postalCode",
          "country"
        ],
        "type": "object"
      },
      "CategoryData": {
        "description": " Represents an expense category for transaction classification.",
        "properties": {
          "id": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CategoryId"
              },
              {
                "description": " The ID of the category"
              }
            ]
          },
          "name": {
            "description": " The name of the category",
            "type": "string"
          }
        },
        "required": [
          "id",
          "name"
        ],
        "type": "object"
      },
      "CategoryId": {
        "description": "ID for the category",
        "format": "uuid",
        "type": "string"
      },
      "CreditCardId": {
        "format": "uuid",
        "type": "string"
      },
      "CreditCardInfo": {
        "properties": {
          "email": {
            "nullable": true,
            "type": "string"
          },
          "id": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CreditCardId"
              }
            ]
          },
          "paymentMethod": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "paymentMethod"
        ],
        "type": "object"
      },
      "CurrencyCode": {
        "type": "string"
      },
      "CurrencyExchangeInfo": {
        "properties": {
          "convertedFromAmount": {
            "multipleOf": 0.01,
            "type": "number"
          },
          "convertedFromCurrency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyCode"
              }
            ]
          },
          "convertedToAmount": {
            "multipleOf": 0.01,
            "type": "number"
          },
          "convertedToCurrency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyCode"
              }
            ]
          },
          "exchangeRate": {
            "description": " Exchange rate goes from \"from currency\" to \"to currency\"\n (ie from currency * exchange rate = to currency)",
            "multipleOf": 0.0001,
            "type": "number"
          },
          "feeAmount": {
            "multipleOf": 0.01,
            "type": "number"
          },
          "feePercentage": {
            "multipleOf": 0.0001,
            "type": "number"
          },
          "feeTransactionId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionMetadataId"
              }
            ],
            "nullable": true
          }
        },
        "required": [
          "convertedFromCurrency",
          "convertedToCurrency",
          "convertedFromAmount",
          "convertedToAmount",
          "feeAmount",
          "feePercentage",
          "exchangeRate"
        ],
        "type": "object"
      },
      "DebitCardId": {
        "format": "uuid",
        "type": "string"
      },
      "DebitCardInfo": {
        "properties": {
          "id": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DebitCardId"
              }
            ]
          }
        },
        "required": [
          "id"
        ],
        "type": "object"
      },
      "DomesticWireRoutingInfo": {
        "properties": {
          "accountNumber": {
            "type": "string"
          },
          "address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AddressWithoutName"
              }
            ],
            "nullable": true
          },
          "bankName": {
            "nullable": true,
            "type": "string"
          },
          "routingNumber": {
            "type": "string"
          }
        },
        "required": [
          "accountNumber",
          "routingNumber"
        ],
        "type": "object"
      },
      "ElectronicAccountType": {
        "enum": [
          "businessChecking",
          "businessSavings",
          "personalChecking",
          "personalSavings"
        ],
        "type": "string"
      },
      "ElectronicRoutingInfo": {
        "properties": {
          "accountNumber": {
            "type": "string"
          },
          "address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AddressWithoutName"
              }
            ],
            "nullable": true
          },
          "bankName": {
            "nullable": true,
            "type": "string"
          },
          "electronicAccountType": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ElectronicAccountType"
              }
            ]
          },
          "routingNumber": {
            "type": "string"
          }
        },
        "required": [
          "accountNumber",
          "routingNumber",
          "electronicAccountType"
        ],
        "type": "object"
      },
      "ISO3166Alpha2": {
        "type": "string"
      },
      "InternalTransferAPIRequest": {
        "description": " Request body for POST /api/v1/transfer endpoint.\n Transfers funds between two depository, treasury, or investment accounts belonging to the same organization.",
        "properties": {
          "amount": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PositiveDollar"
              }
            ]
          },
          "destinationAccountId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              }
            ]
          },
          "idempotencyKey": {
            "type": "string"
          },
          "note": {
            "nullable": true,
            "type": "string"
          },
          "sourceAccountId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              }
            ]
          }
        },
        "required": [
          "sourceAccountId",
          "destinationAccountId",
          "amount",
          "idempotencyKey"
        ],
        "type": "object"
      },
      "InternalTransferAPIResponse": {
        "description": " Response for POST /api/v1/transfer endpoint.\n Returns both the credit and debit transactions for the transfer (depository, treasury, or investment).",
        "properties": {
          "creditTransaction": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Transaction"
              }
            ]
          },
          "debitTransaction": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Transaction"
              }
            ]
          }
        },
        "required": [
          "creditTransaction",
          "debitTransaction"
        ],
        "type": "object"
      },
      "InternationalWireAustraliaSpecificData": {
        "properties": {
          "bsbCode": {
            "type": "string"
          }
        },
        "required": [
          "bsbCode"
        ],
        "type": "object"
      },
      "InternationalWireBrazilSpecificData": {
        "properties": {
          "legalId": {
            "type": "string"
          }
        },
        "required": [
          "legalId"
        ],
        "type": "object"
      },
      "InternationalWireCanadaSpecificData": {
        "properties": {
          "bankCode": {
            "type": "string"
          },
          "transitNumber": {
            "type": "string"
          }
        },
        "required": [
          "bankCode",
          "transitNumber"
        ],
        "type": "object"
      },
      "InternationalWireChileSpecificData": {
        "properties": {
          "legalId": {
            "type": "string"
          }
        },
        "required": [
          "legalId"
        ],
        "type": "object"
      },
      "InternationalWireColombiaSpecificData": {
        "properties": {
          "legalId": {
            "type": "string"
          }
        },
        "required": [
          "legalId"
        ],
        "type": "object"
      },
      "InternationalWireCorrespondentInfo": {
        "properties": {
          "bankName": {
            "nullable": true,
            "type": "string"
          },
          "routingNumber": {
            "nullable": true,
            "type": "string"
          },
          "swiftCode": {
            "nullable": true,
            "type": "string"
          }
        },
        "type": "object"
      },
      "InternationalWireCountrySpecificData": {
        "properties": {
          "australia": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireAustraliaSpecificData"
              }
            ],
            "nullable": true
          },
          "brazil": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireBrazilSpecificData"
              }
            ],
            "nullable": true
          },
          "canada": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireCanadaSpecificData"
              }
            ],
            "nullable": true
          },
          "chile": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireChileSpecificData"
              }
            ],
            "nullable": true
          },
          "colombia": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireColombiaSpecificData"
              }
            ],
            "nullable": true
          },
          "dominicanRepublic": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireDominicanRepublicSpecificData"
              }
            ],
            "nullable": true
          },
          "honduras": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireHondurasSpecificData"
              }
            ],
            "nullable": true
          },
          "india": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireIndiaSpecificData"
              }
            ],
            "nullable": true
          },
          "kazakhstan": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireKazakhstanSpecificData"
              }
            ],
            "nullable": true
          },
          "pakistan": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWirePakistanSpecificData"
              }
            ],
            "nullable": true
          },
          "paraguay": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireParaguaySpecificData"
              }
            ],
            "nullable": true
          },
          "philippines": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWirePhilippinesSpecificData"
              }
            ],
            "nullable": true
          },
          "russia": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireRussiaSpecificData"
              }
            ],
            "nullable": true
          },
          "southAfrica": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireSouthAfricaSpecificData"
              }
            ],
            "nullable": true
          }
        },
        "type": "object"
      },
      "InternationalWireDominicanRepublicSpecificData": {
        "properties": {
          "accountType": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SwiftBankAccountType"
              }
            ]
          },
          "legalId": {
            "type": "string"
          }
        },
        "required": [
          "accountType",
          "legalId"
        ],
        "type": "object"
      },
      "InternationalWireHondurasSpecificData": {
        "properties": {
          "accountType": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SwiftBankAccountType"
              }
            ]
          },
          "legalId": {
            "type": "string"
          }
        },
        "required": [
          "accountType",
          "legalId"
        ],
        "type": "object"
      },
      "InternationalWireIndiaSpecificData": {
        "properties": {
          "ifscCode": {
            "type": "string"
          }
        },
        "required": [
          "ifscCode"
        ],
        "type": "object"
      },
      "InternationalWireKazakhstanSpecificData": {
        "properties": {
          "legalId": {
            "type": "string"
          }
        },
        "required": [
          "legalId"
        ],
        "type": "object"
      },
      "InternationalWirePakistanSpecificData": {
        "properties": {
          "legalId": {
            "type": "string"
          },
          "legalIdType": {
            "allOf": [
              {
                "$ref": "#/components/schemas/PakistaniLegalIdType"
              }
            ]
          }
        },
        "required": [
          "legalIdType",
          "legalId"
        ],
        "type": "object"
      },
      "InternationalWireParaguaySpecificData": {
        "properties": {
          "legalId": {
            "type": "string"
          }
        },
        "required": [
          "legalId"
        ],
        "type": "object"
      },
      "InternationalWirePhilippinesSpecificData": {
        "properties": {
          "routingNumber": {
            "type": "string"
          }
        },
        "required": [
          "routingNumber"
        ],
        "type": "object"
      },
      "InternationalWireRoutingInfo": {
        "properties": {
          "address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AddressWithoutName"
              }
            ],
            "nullable": true
          },
          "bankDetails": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SwiftCodeData"
              }
            ],
            "nullable": true
          },
          "correspondentInfo": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireCorrespondentInfo"
              }
            ],
            "nullable": true
          },
          "countrySpecific": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireCountrySpecificData"
              }
            ]
          },
          "emailAddress": {
            "nullable": true,
            "type": "string"
          },
          "iban": {
            "type": "string"
          },
          "phoneNumber": {
            "nullable": true,
            "type": "string"
          },
          "swiftCode": {
            "type": "string"
          }
        },
        "required": [
          "iban",
          "swiftCode",
          "countrySpecific"
        ],
        "type": "object"
      },
      "InternationalWireRussiaSpecificData": {
        "properties": {
          "inn": {
            "type": "string"
          }
        },
        "required": [
          "inn"
        ],
        "type": "object"
      },
      "InternationalWireSouthAfricaSpecificData": {
        "properties": {
          "branchCode": {
            "type": "string"
          }
        },
        "required": [
          "branchCode"
        ],
        "type": "object"
      },
      "MerchantData": {
        "description": " Merchant information for card transactions",
        "properties": {
          "category": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MercuryCategory"
              },
              {
                "description": " Mercury category for the merchant (e.g., \"Restaurants\", \"Software\")"
              }
            ],
            "nullable": true
          },
          "categoryCode": {
            "description": " 4-digit merchant category code (MCC) for card transactions",
            "nullable": true,
            "type": "string"
          },
          "id": {
            "description": " Merchant ID for card transactions",
            "nullable": true,
            "type": "string"
          }
        },
        "type": "object"
      },
      "MercuryCategory": {
        "enum": [
          "Other",
          "Advertising",
          "Airlines",
          "AlcoholAndBars",
          "BooksAndNewspaper",
          "CarRental",
          "Charity",
          "Clothing",
          "Conferences",
          "Education",
          "Electronics",
          "Entertainment",
          "FacilitiesExpenses",
          "Fees",
          "FoodDelivery",
          "FuelAndGas",
          "Gambling",
          "GovernmentServices",
          "Grocery",
          "GroundTransportation",
          "Insurance",
          "InternetAndTelephone",
          "Legal",
          "Lodging",
          "Medical",
          "Memberships",
          "OfficeSupplies",
          "OtherTravel",
          "Parking",
          "Political",
          "ProfessionalServices",
          "Restaurants",
          "Retail",
          "RideshareAndTaxis",
          "Shipping",
          "Software",
          "Taxes",
          "Utilities",
          "VehicleExpenses"
        ],
        "type": "string"
      },
      "MercuryCreditAccountStatementPeriodId": {
        "description": "ID for the credit statement period",
        "format": "uuid",
        "type": "string"
      },
      "PakistaniLegalIdType": {
        "enum": [
          "CNIC",
          "SNIC",
          "Passport",
          "NTN"
        ],
        "type": "string"
      },
      "PositiveDollar": {
        "description": "A positive dollar amount with at least 1 cent.",
        "format": "double",
        "minimum": 0.01,
        "type": "number"
      },
      "Region": {
        "type": "string"
      },
      "RelatedTransactionData": {
        "description": " A Public API version of RelatedTransactionData.",
        "properties": {
          "accountId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              }
            ]
          },
          "amount": {
            "multipleOf": 0.01,
            "type": "number"
          },
          "id": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionMetadataId"
              }
            ]
          },
          "relationKind": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionRelationKind"
              }
            ]
          }
        },
        "required": [
          "id",
          "accountId",
          "relationKind",
          "amount"
        ],
        "type": "object"
      },
      "SwiftBankAccountType": {
        "enum": [
          "checking",
          "savings"
        ],
        "type": "string"
      },
      "SwiftCodeData": {
        "properties": {
          "bankCityState": {
            "type": "string"
          },
          "bankCountry": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ISO3166Alpha2"
              }
            ]
          },
          "bankName": {
            "type": "string"
          }
        },
        "required": [
          "bankName",
          "bankCityState",
          "bankCountry"
        ],
        "type": "object"
      },
      "Transaction": {
        "properties": {
          "accountId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              },
              {
                "description": " The external-facing account identifier for the Mercury account that owns this transaction"
              }
            ]
          },
          "amount": {
            "multipleOf": 0.01,
            "type": "number"
          },
          "attachments": {
            "items": {
              "$ref": "#/components/schemas/TransactionAttachment"
            },
            "type": "array"
          },
          "bankDescription": {
            "nullable": true,
            "type": "string"
          },
          "categoryData": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CategoryData"
              }
            ],
            "nullable": true
          },
          "checkNumber": {
            "description": " Present for check deposits and mailed checks; Nothing otherwise.",
            "nullable": true,
            "type": "string"
          },
          "compliantWithReceiptPolicy": {
            "type": "boolean"
          },
          "counterpartyId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionPartyId"
              }
            ]
          },
          "counterpartyName": {
            "type": "string"
          },
          "counterpartyNickname": {
            "nullable": true,
            "type": "string"
          },
          "createdAt": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              }
            ]
          },
          "creditAccountPeriodId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MercuryCreditAccountStatementPeriodId"
              }
            ],
            "nullable": true
          },
          "currencyExchangeInfo": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyExchangeInfo"
              }
            ],
            "nullable": true
          },
          "dashboardLink": {
            "type": "string"
          },
          "details": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionMethodData"
              }
            ],
            "nullable": true
          },
          "estimatedDeliveryDate": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              }
            ]
          },
          "externalMemo": {
            "nullable": true,
            "type": "string"
          },
          "failedAt": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              }
            ],
            "nullable": true
          },
          "feeId": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionMetadataId"
              }
            ],
            "nullable": true
          },
          "generalLedgerCodeName": {
            "description": " The name of the General Ledger (GL) code assigned to this transaction for accounting\n categorization. GL codes act as \"bins\" that organize transactions into accounting categories.\n This field is present when the transaction has been categorized, either manually by a user,\n via an accounting integration sync, or through auto-categorization rules. Nothing if the\n transaction has not been assigned a GL code.",
            "nullable": true,
            "type": "string"
          },
          "hasGeneratedReceipt": {
            "type": "boolean"
          },
          "id": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionMetadataId"
              }
            ]
          },
          "kind": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionKind"
              }
            ]
          },
          "merchant": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MerchantData"
              },
              {
                "description": " Merchant information for card transactions; Nothing for non-card transactions"
              }
            ],
            "nullable": true
          },
          "mercuryCategory": {
            "allOf": [
              {
                "$ref": "#/components/schemas/MercuryCategory"
              }
            ],
            "nullable": true
          },
          "note": {
            "nullable": true,
            "type": "string"
          },
          "postedAt": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UTCTime"
              }
            ],
            "nullable": true
          },
          "reasonForFailure": {
            "nullable": true,
            "type": "string"
          },
          "relatedTransactions": {
            "items": {
              "$ref": "#/components/schemas/RelatedTransactionData"
            },
            "type": "array"
          },
          "requestId": {
            "nullable": true,
            "type": "string"
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionStatus"
              }
            ]
          },
          "trackingNumber": {
            "description": " Present for transactions that have tracking numbers (e.g., RTP, ACH, wires); Nothing otherwise.",
            "nullable": true,
            "type": "string"
          }
        },
        "required": [
          "id",
          "amount",
          "createdAt",
          "estimatedDeliveryDate",
          "status",
          "counterpartyId",
          "dashboardLink",
          "counterpartyName",
          "kind",
          "compliantWithReceiptPolicy",
          "hasGeneratedReceipt",
          "attachments",
          "relatedTransactions",
          "accountId"
        ],
        "type": "object"
      },
      "TransactionAttachment": {
        "properties": {
          "attachmentType": {
            "allOf": [
              {
                "$ref": "#/components/schemas/TransactionAttachmentType"
              }
            ]
          },
          "fileName": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "fileName",
          "url",
          "attachmentType"
        ],
        "type": "object"
      },
      "TransactionAttachmentType": {
        "enum": [
          "checkImage",
          "receipt",
          "other"
        ],
        "type": "string"
      },
      "TransactionKind": {
        "enum": [
          "externalTransfer",
          "internalTransfer",
          "outgoingPayment",
          "creditCardCredit",
          "creditCardTransaction",
          "debitCardCredit",
          "debitCardTransaction",
          "cardInternationalTransactionFee",
          "cardInternationalTransactionFeeRebate",
          "cardInternationalTransactionFeeReversal",
          "cardInternationalTransactionFeeRebateReversal",
          "incomingDomesticWire",
          "checkDeposit",
          "incomingInternationalWire",
          "treasuryTransfer",
          "currencyCloudReturn",
          "wireFee",
          "personalBankingSubscriptionFee",
          "billingEngineSubscriptionFee",
          "expenseReimbursement",
          "exogenousWireDrawdown",
          "other"
        ],
        "type": "string"
      },
      "TransactionMetadataId": {
        "description": "ID for this transaction",
        "format": "uuid",
        "type": "string"
      },
      "TransactionMethodData": {
        "properties": {
          "address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AddressData"
              }
            ],
            "nullable": true
          },
          "creditCardInfo": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CreditCardInfo"
              }
            ],
            "nullable": true
          },
          "debitCardInfo": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DebitCardInfo"
              }
            ],
            "nullable": true
          },
          "domesticWireRoutingInfo": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DomesticWireRoutingInfo"
              }
            ],
            "nullable": true
          },
          "electronicRoutingInfo": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ElectronicRoutingInfo"
              }
            ],
            "nullable": true
          },
          "internationalWireRoutingInfo": {
            "allOf": [
              {
                "$ref": "#/components/schemas/InternationalWireRoutingInfo"
              }
            ],
            "nullable": true
          }
        },
        "type": "object"
      },
      "TransactionPartyId": {
        "description": "ID for a Mercury account.",
        "format": "uuid",
        "type": "string"
      },
      "TransactionRelationKind": {
        "enum": [
          "ProvisionalCreditReversalToMerchantRefund",
          "MerchantRefundToProvisionalCreditReversal",
          "MerchantRefundToFraudulentCharge",
          "FraudulentChargeToMerchantRefund",
          "PaymentRefundToFailedPayment",
          "FailedPaymentToPaymentRefund",
          "GiftCompensationToOriginalTransaction",
          "FeePaymentToOriginalTransaction",
          "OriginalTransactionToFeePayment",
          "FeePaymentToFeeRebate",
          "FeeRebateToFeePayment",
          "FeePaymentToFeeReversal",
          "FeeReversalToFeePayment",
          "FeeRebateToFeeRebateReversal",
          "FeeRebateReversalToFeeRebate",
          "TreasurySplitLiquidation",
          "ProvisionalCreditToOriginalCharge",
          "OriginalChargeToProvisionalCredit",
          "FeeAtmReimbursementToAtmTransaction",
          "AtmTransactionToFeeAtmReimbursement",
          "AtmTransactionToAtmReimbursementReversal",
          "AtmReimbursementReversalToAtmTransaction",
          "ReturnToOriginalTransaction",
          "OriginalTransactionToReturn",
          "ProvisionalCreditToReversal",
          "ReversalToProvisionalCredit"
        ],
        "type": "string"
      },
      "TransactionStatus": {
        "enum": [
          "pending",
          "sent",
          "cancelled",
          "failed",
          "reversed",
          "blocked"
        ],
        "type": "string"
      },
      "USState": {
        "enum": [
          "AL",
          "AK",
          "AZ",
          "AR",
          "CA",
          "CO",
          "CT",
          "DE",
          "DC",
          "FL",
          "GA",
          "HI",
          "ID",
          "IL",
          "IN",
          "IA",
          "KS",
          "KY",
          "LA",
          "ME",
          "MD",
          "MA",
          "MI",
          "MN",
          "MS",
          "MO",
          "MT",
          "NE",
          "NV",
          "NH",
          "NJ",
          "NM",
          "NY",
          "NC",
          "ND",
          "OH",
          "OK",
          "OR",
          "PA",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VT",
          "VA",
          "WA",
          "WV",
          "WI",
          "WY"
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
    "/transfer": {
      "post": {
        "description": "Transfer funds between two accounts within the same organization. Supports transfers between depository accounts (checking/savings), from a depository account to a treasury/investment account, and from a treasury/investment account to a depository account. Creates paired debit and credit transactions.",
        "operationId": "createInternalTransfer",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/InternalTransferAPIRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InternalTransferAPIResponse"
                }
              }
            },
            "description": ""
          },
          "400": {
            "description": "Invalid `body`"
          }
        },
        "summary": "Create an internal transfer",
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