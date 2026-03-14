# Payment

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/payment
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Payment
> Canonical entity: `Payment`

A Payment object records a payment in QuickBooks. The payment can be applied for a particular customer against multiple Invoices and Credit Memos. It can also be created without any Invoice or Credit Memo, by just specifying an amount.

- A Payment can be updated as a full update or a sparse update.
- A Payment can be linked to multiple Invoices and Credit Memos.
- A Payment can be created as unapplied to any Invoice or Credit Memo, in which case it is recorded as a credit.
- If any element in any line needs to be updated, all the `Line` elements of the Payment object have to be provided. This is true for full or sparse update. Lines can be updated only ALL or NONE.
- To remove all lines, send an empty `Line` element.
- To remove some of the lines, send all the Lines that need to be present MINUS the lines that need to be removed.
- To add some lines, send all existing and new Lines that need to be present.
- The sequence in which the lines are received is the sequence in which lines are preserved.
- If you have a large number of invoice and corresponding payment records that you wish to import to the QuickBooks Online company, sort the invoice and payment records in chronological order and use the batch resource to send invoice and payments batches of 10, one after the other, to ensure any open invoices get credited with their payments.

## The payment object

### paymentresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `TotalAmt`

Required: Required
Type: `Decimal`

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes. If you process a linked refund transaction against a specific transaction, the `totalAmt` value won't change. It will remain the same. However, voiding the linked refund will change the `totalAmt` value to O.

#### `CustomerRef`

Required: Required
Type: `ReferenceType`
Traits: filterable

Reference to a customer or job. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

<details>
<summary>Child attributes for `CustomerRef`</summary>

##### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company.

<details>
<summary>Child attributes for `CurrencyRef`</summary>

##### currencyref

Model type: `object`

###### `value`

Required: Required
Type: `String`

A three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on.

###### `name`

Required: Optional
Type: `String`

The full name of the currency.

</details>

#### `ProjectRef`

Required: Conditionally required
Type: `ReferenceType`
Traits: filterable
Minor version: 69

Reference to the `Project` ID associated with this transaction. Available with Minor Version 69 and above

<details>
<summary>Child attributes for `ProjectRef`</summary>

##### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

#### `PaymentRefNum`

Required: Conditionally Required
Type: `String`
Traits: filterable, sortable
Locales: FR

The reference number for the payment received. For example, Â Check # for a check, envelope # for a cash donation. Required for France locales.

#### `TaxExemptionRef`

Type: `ReferenceType`
Traits: read only, system defined
Minor version: 21

Reference to the `TaxExepmtion` ID associated with this object. Available for companies that have [automated sales tax](https://developer.intuit.com/hub/blog/2017/12/11/using-quickbooks-online-api-automated-sales-tax) enabled.

`TaxExemptionRef.Name`: The Tax Exemption Id for the customer to which this object is associated. This Id is typically issued by the state.

`TaxExemptionRef.value`: The system-generated Id of the exemption type.

For internal use only

<details>
<summary>Child attributes for `TaxExemptionRef`</summary>

##### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: Max of 4000 chars

User entered, organization-private note about the transaction.

#### `PaymentMethodRef`

Required: Optional
Type: `ReferenceType`

Reference to a PaymentMethod associated with this transaction. Query the PaymentMethod name list resource to determine the appropriate PaymentMethod object for this reference. Use `PaymentMethod.Id` and `PaymentMethod.Name` from that object for `PaymentMethodRef.value` and `PaymentMethodRef.name`, respectively.

<details>
<summary>Child attributes for `PaymentMethodRef`</summary>

##### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

#### `UnappliedAmt`

Required: Optional
Type: `Decimal`
Traits: read only

Indicates the amount that has not been applied to pay amounts owed for sales transactions.

#### `DepositToAccountRef`

Required: Optional
Type: `ReferenceType`
Default: Undeposited Funds account

Identifies the account to be used for this payment. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType` is `Other Current Asset` or `Bank`. Use `Account.Id` and `Account.Name` from that object for `DepositToAccountRef.value` and `DepostiToAccountRef.name`, respectively.
If you do not specify this account, payment is applied to the Undeposited Funds account.

<details>
<summary>Child attributes for `DepositToAccountRef`</summary>

##### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company

#### `Line [0..n]`

Required: Optional
Type: `Line`

Zero or more transactions accounting for this payment. Values for `Line.LinkedTxn.TxnType`can be one of the following:

`Expense`--Payment is reimbursement for expense paid by cash made on behalf of the customer

`Check`--Payment is reimbursement for expense paid by check made on behalf of the customer

`CreditCardCredit`--Payment is reimbursement for a credit card credit made on behalf of the customer

`JournalEntry`--Payment is linked to the representative journal entry

`CreditMemo`--Payment is linked to the credit memo the customer has with the business

`Invoice`--The invoice to which payment is applied

Use `Line.LinkedTxn.TxnId` as the ID in a separate read request for the specific resource to retrieve details of the linked object.

<details>
<summary>Child attributes for `Line [0..n]`</summary>

##### linelinkedtxn

Model type: `object`

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item.

###### `LinkedTxn [0..n]`

Required: Required

Transaction to which the current entity is related. For example, a billpayment line links to the originating bill object for which the billpayment is applied.

<details>
<summary>Child attributes for `LinkedTxn [0..n]`</summary>

###### linkedtxn

Model type: `object`

###### `TxnId`

Required: Required
Type: `String`

Transaction Id of the related transaction.

###### `TxnType`

Required: Required
Type: `String`

Transaction type of the linked object.

###### `TxnLineId`

Required: Conditionally required
Type: `String`

Required for Deposit and Bill entities. The line number of a specific line of the linked transaction. If supplied, the `TxnId` and `TxnType` attributes of the linked transaction must also be populated.

</details>

</details>

#### `TxnSource`

Required: Optional
Type: `String`

Used internally to specify originating source of a credit card transaction.

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: current server date

The date entered by the user when this transaction occurred. For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.
Sort order is ASC by default.

#### `CreditCardPayment`

Required: Optional
Type: `CreditCardPayment`

Information about a payment received by credit card. Inject with data only if the payment was transacted through Intuit Payments API.

<details>
<summary>Child attributes for `CreditCardPayment`</summary>

##### creditcardpayment

Model type: `object`

###### `CreditChargeResponse`

Required: Optional
Type: `CreditChargeResponse`

Holds credit-card transaction response information from a merchant account service.

<details>
<summary>Child attributes for `CreditChargeResponse`</summary>

###### creditchargeresponse

Model type: `object`

###### `Status`

Required: Optional
Type: `CCPaymentStatusEnum`

Indicates the status of the payment transaction. Possible values include `Completed`, `Unknown`.

###### `AuthCode`

Required: Optional
Type: `String`
Max length: maximum 100 characters

Code returned from the credit card processor to indicate that the charge will be paid by the card issuer.

###### `TxnAuthorizationTime`

Required: Optional
Type: `DateTime`

Timestamp indicating the time in which the card processor authorized the transaction.

<details>
<summary>Child attributes for `TxnAuthorizationTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `CCTransId`

Required: Optional
Type: `String`
Max length: maximum 100 characters

Unique identifier of the payment transaction. It can be used to track the status of transactions, or to search transactions.

</details>

###### `CreditChargeInfo`

Required: Optional
Type: `CreditChargeInfo`

Holds creditcard information to request a credit card payment from a merchant account service.

<details>
<summary>Child attributes for `CreditChargeInfo`</summary>

###### creditchargeinfo

Model type: `object`

###### `CcExpiryMonth`

Required: Optional
Type: `Integer`

Expiration Month on card, expressed as a number: `1`=January, `2`=February, etc.

###### `ProcessPayment`

Required: Optional
Type: `Boolean`

-`false` or no value-Store credit card information only. Do not store QuickBooks Payment transaction information in CreditChargeResponse. -`true`-Store credit card payment transaction information in CreditChargeResponse below. Use this setting when QuickBooks Payments is configured to process credit card charges.

###### `PostalCode`

Required: Optional
Type: `String`
Max length: maximum 30 characters

Credit card holder billing postal code. Five digits in the USA.

###### `Amount`

Required: Optional
Type: `Decimal`

The amount processed using the credit card.

###### `NameOnAcct`

Required: Optional
Type: `String`

Account holder name, as printed on the card.

###### `CcExpiryYear`

Required: Optional
Type: `Integer`
Default: current year

Expiration Year on card, expressed as a 4 digit number `1999`, `2003`, etc.

###### `Type`

Required: Optional
Type: `String`

Type of credit card. For example, MasterCard, Visa, Discover, American Express, and so on.

###### `BillAddrStreet`

Required: Optional
Type: `String`
Max length: maximum 255 characters

Credit card holder billing address of record: the street address to which credit card statements are sent.

</details>

</details>

#### `TransactionLocationType`

Required: Optional
Type: `String`
Default: <span class="literal">WithinFrance</span>
Minor version: 4
Locales: FR

The account location. Valid values include:

`WithinFrance`

`FranceOverseas`

`OutsideFranceWithEU`

`OutsideEU`

For France locales, only.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the entity. The MetaData values are set by Data Services and are read only for all applications.

<details>
<summary>Child attributes for `MetaData`</summary>

##### modificationmetadata

Model type: `object`

###### `CreateTime`

Type: `DateTime`
Traits: read only, system defined, filterable, sortable

Time the entity was created in the source domain.

<details>
<summary>Child attributes for `CreateTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `LastUpdatedTime`

Type: `DateTime`
Traits: read only, system defined, filterable, sortable

Time the entity was last updated in the source domain.

<details>
<summary>Child attributes for `LastUpdatedTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

</details>

#### Example

```json
{
  "Payment": {
    "SyncToken": "0",
    "domain": "QBO",
    "DepositToAccountRef": {
      "value": "4"
    },
    "UnappliedAmt": 10.0,
    "TxnDate": "2015-01-16",
    "TotalAmt": 65.0,
    "ProjectRef": {
      "value": "39298034"
    },
    "ProcessPayment": false,
    "sparse": false,
    "Line": [
      {
        "Amount": 55.0,
        "LineEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnId",
                "Value": "70"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            },
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnOpenBalance",
                "Value": "71.00"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            },
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnReferenceNumber",
                "Value": "1024"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "LinkedTxn": [
          {
            "TxnId": "70",
            "TxnType": "Invoice"
          }
        ]
      }
    ],
    "CustomerRef": {
      "name": "Red Rock Diner",
      "value": "20"
    },
    "Id": "163",
    "MetaData": {
      "CreateTime": "2015-01-16T15:08:12-08:00",
      "LastUpdatedTime": "2015-01-16T15:08:12-08:00"
    }
  },
  "time": "2015-07-28T15:16:15.435-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T15:16:38.467-07:00">
  <Payment domain="QBO" sparse="false">
    <Id>163</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-01-16T15:08:12-08:00</CreateTime>
      <LastUpdatedTime>2015-01-16T15:08:12-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-01-16</TxnDate>
    <Line>
      <Amount>55.00</Amount>
      <LinkedTxn>
        <TxnId>70</TxnId>
        <TxnType>Invoice</TxnType>
      </LinkedTxn>
      <LineEx>
        <NameValue>
          <Name>txnId</Name>
          <Value>70</Value>
        </NameValue>
        <NameValue>
          <Name>txnOpenBalance</Name>
          <Value>71.00</Value>
        </NameValue>
        <NameValue>
          <Name>txnReferenceNumber</Name>
          <Value>1024</Value>
        </NameValue>
      </LineEx>
    </Line>
    <CustomerRef name="Red Rock Diner">20</CustomerRef>
    <ProjectRef>39298034</ProjectRef>
    <DepositToAccountRef>4</DepositToAccountRef>
    <TotalAmt>65.00</TotalAmt>
    <UnappliedAmt>10.00</UnappliedAmt>
    <ProcessPayment>false</ProcessPayment>
  </Payment>
</IntuitResponse>
```

## Create a payment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/payment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create a Payment object are listed here.

Schema: `paymentrequest`

<details>
<summary>Show schema for `paymentrequest`</summary>

#### paymentrequest

Model type: `object`

##### `TotalAmt`

Required: Required
Type: `Decimal`
Traits: filterable, sortable

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes.

##### `CustomerRef`

Required: Required
Type: `ReferenceType`
Traits: filterable

Reference to a customer or job. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

<details>
<summary>Child attributes for `CustomerRef`</summary>

###### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

##### `ProjectRef`

Required: Conditionally required
Type: `ReferenceType`
Traits: filterable
Minor version: 69

Reference to the `Project` ID associated with this transaction. Available with Minor Version 69 and above

<details>
<summary>Child attributes for `ProjectRef`</summary>

###### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

##### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company.

<details>
<summary>Child attributes for `CurrencyRef`</summary>

###### currencyref

Model type: `object`

###### `value`

Required: Required
Type: `String`

A three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on.

###### `name`

Required: Optional
Type: `String`

The full name of the currency.

</details>

</details>

#### Example

```json
{
  "TotalAmt": 25.0,
  "CustomerRef": {
    "value": "20"
  }
}
```

#### XML example

```xml
<Payment xmlns="http://schema.intuit.com/finance/v3">
    <CustomerRef name="Red Rock Diner">20</CustomerRef>
    <TotalAmt>20</TotalAmt>
</Payment>
```

### Returns

The Payment response body.

#### Example

```json
{
  "Payment": {
    "SyncToken": "0",
    "domain": "QBO",
    "DepositToAccountRef": {
      "value": "4"
    },
    "UnappliedAmt": 25.0,
    "TxnDate": "2014-12-30",
    "TotalAmt": 25.0,
    "ProjectRef": {
      "value": "39298034"
    },
    "ProcessPayment": false,
    "sparse": false,
    "Line": [],
    "CustomerRef": {
      "name": "Red Rock Diner",
      "value": "20"
    },
    "Id": "154",
    "MetaData": {
      "CreateTime": "2014-12-30T10:26:03-08:00",
      "LastUpdatedTime": "2014-12-30T10:26:03-08:00"
    }
  },
  "time": "2014-12-30T10:26:03.668-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-30T10:13:54.219-08:00">
    <Payment domain="QBO" sparse="false">
        <Id>151</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-12-30T10:13:54-08:00</CreateTime>
            <LastUpdatedTime>2014-12-30T10:13:54-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-12-30</TxnDate>
        <CustomerRef name="Red Rock Diner">20</CustomerRef>
        <ProjectRef>39298034</ProjectRef>
        <DepositToAccountRef>4</DepositToAccountRef>
        <TotalAmt>20.00</TotalAmt>
        <UnappliedAmt>20.00</UnappliedAmt>
        <ProcessPayment>false</ProcessPayment>
    </Payment>
</IntuitResponse>
```

## Delete a payment

### Definition

- **Content type:** `application/json or application/xml`
- **Operation:** `POST /v3/company/<realmID>/payment?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the Payment object specified in the request body. Include a minimum of `Payment.Id` and `Payment.SyncToken` in the request body.

### Request Body

Schema: `deleterequest`

<details>
<summary>Show schema for `deleterequest`</summary>

#### deleterequest

Model type: `object`

##### `SyncToken`

Required: Required
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

##### `id`

Required: Required
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object.

</details>

#### Example

```json
{
  "SyncToken": "2",
  "Id": "73"
}
```

#### XML example

```xml
<Payment xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
   <Id>8748</Id>
   <SyncToken>0</SyncToken>
</Payment>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "Payment": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "73"
  },
  "time": "2013-03-14T11:57:42.849-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T08:30:33.626-07:00">
  <Payment domain="QBO" status="Deleted">
  <Id>8748</Id>
  </Payment>
</IntuitResponse>
```

## Void a payment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/payment?operation=update&include=void`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use a sparse update operation with `include=void` to void an existing Payment object; include a minimum of `Payment.Id` and `Payment.SyncToken`.The transaction remains active but all amounts and quantities are zeroed and the string, `Voided`, is injected into `Payment.PrivateNote`, prepended to existing text if present. If funds for the payment have been deposited, you must delete the associated deposit object before voiding the payment object.

### Request Body

Schema: `voidrequest`

<details>
<summary>Show schema for `voidrequest`</summary>

#### voidrequest

Model type: `object`

##### `SyncToken`

Required: Required
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

##### `id`

Required: Required
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object.

##### `sparse`

Required: Required
Type: `String`

Include and set to true to void an object.

</details>

#### Example

```json
{
  "SyncToken": "1",
  "Id": "33",
  "sparse": true
}
```

#### XML example

```xml
<Payment xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>61</Id>
    <SyncToken>0</SyncToken>
</Payment>
```

### Returns

The Payment object response body.

#### Example

```json
{
  "Payment": {
    "SyncToken": "2",
    "domain": "QBO",
    "PaymentMethodRef": {
      "value": "2"
    },
    "DepositToAccountRef": {
      "value": "35"
    },
    "UnappliedAmt": 0,
    "TxnDate": "2014-11-07",
    "TotalAmt": 0,
    "ProjectRef": {
      "value": "39298234"
    },
    "ProcessPayment": false,
    "PrivateNote": "Voided",
    "sparse": false,
    "Line": [],
    "CustomerRef": {
      "name": "Freeman Sporting Goods:55 Twin Lane",
      "value": "9"
    },
    "Id": "33",
    "MetaData": {
      "CreateTime": "2014-11-07T11:07:19-08:00",
      "LastUpdatedTime": "2015-02-23T12:52:07-08:00"
    }
  },
  "time": "2015-02-23T12:52:06.954-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-23T12:58:21.959-08:00">
    <Payment domain="QBO" sparse="false">
        <Id>61</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2014-11-07T15:21:23-08:00</CreateTime>
            <LastUpdatedTime>2015-02-23T12:58:22-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-11-02</TxnDate>
        <PrivateNote>Voided</PrivateNote>
        <CustomerRef name="Cool Cars">3</CustomerRef>
        <ProjectRef>39298033</ProjectRef>
        <DepositToAccountRef>35</DepositToAccountRef>
        <PaymentMethodRef>2</PaymentMethodRef>
        <PaymentRefNum>1886</PaymentRefNum>
        <TotalAmt>0</TotalAmt>
        <UnappliedAmt>0</UnappliedAmt>
        <ProcessPayment>false</ProcessPayment>
    </Payment>
</IntuitResponse>
```

## Get a payment as PDF

### Definition

- **Content type:** `application/pdf`
- **Operation:** `GET /v3/company/<realmID>/payment/<paymentId>/pdf`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Returns

This resource returns the specified object in the response body as an Adobe Portable Document Format (PDF) file. The resulting PDF file is formatted according to custom form styles in the company settings.

## Query a payment

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Payment Where Metadata.LastUpdatedTime>'2015-01-16' Order By Metadata.LastUpdatedTime"
```

#### XML example

```sql
select * from Payment Where Metadata.LastUpdatedTime>'2015-01-16' Order By Metadata.LastUpdatedTime
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Payment": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "value": "4"
        },
        "UnappliedAmt": 55.0,
        "TxnDate": "2015-01-16",
        "TotalAmt": 55.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "ProcessPayment": false,
        "sparse": false,
        "Line": [],
        "CustomerRef": {
          "name": "Red Rock Diner",
          "value": "20"
        },
        "Id": "161",
        "MetaData": {
          "CreateTime": "2015-01-16T14:58:32-08:00",
          "LastUpdatedTime": "2015-01-16T14:58:32-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "value": "4"
        },
        "UnappliedAmt": 65.0,
        "TxnDate": "2015-01-16",
        "TotalAmt": 65.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "ProcessPayment": false,
        "sparse": false,
        "Line": [],
        "CustomerRef": {
          "name": "Red Rock Diner",
          "value": "20"
        },
        "Id": "162",
        "MetaData": {
          "CreateTime": "2015-01-16T14:58:59-08:00",
          "LastUpdatedTime": "2015-01-16T14:58:59-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "value": "4"
        },
        "UnappliedAmt": 10.0,
        "TxnDate": "2015-01-16",
        "TotalAmt": 65.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "ProcessPayment": false,
        "sparse": false,
        "Line": [
          {
            "Amount": 55.0,
            "LineEx": {
              "any": [
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnId",
                    "Value": "70"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                },
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnOpenBalance",
                    "Value": "71.00"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                },
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnReferenceNumber",
                    "Value": "1024"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                }
              ]
            },
            "LinkedTxn": [
              {
                "TxnId": "70",
                "TxnType": "Invoice"
              }
            ]
          }
        ],
        "CustomerRef": {
          "name": "Red Rock Diner",
          "value": "20"
        },
        "Id": "163",
        "MetaData": {
          "CreateTime": "2015-01-16T15:08:12-08:00",
          "LastUpdatedTime": "2015-01-16T15:08:12-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "value": "4"
        },
        "UnappliedAmt": 245.0,
        "TxnDate": "2015-01-16",
        "TotalAmt": 300.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "ProcessPayment": false,
        "sparse": false,
        "Line": [
          {
            "Amount": 55.0,
            "LineEx": {
              "any": [
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnId",
                    "Value": "70"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                },
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnOpenBalance",
                    "Value": "71.00"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                },
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnReferenceNumber",
                    "Value": "1024"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                }
              ]
            },
            "LinkedTxn": [
              {
                "TxnId": "70",
                "TxnType": "Invoice"
              }
            ]
          }
        ],
        "CustomerRef": {
          "name": "Red Rock Diner",
          "value": "20"
        },
        "Id": "164",
        "MetaData": {
          "CreateTime": "2015-01-16T15:09:22-08:00",
          "LastUpdatedTime": "2015-01-16T15:09:22-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "value": "4"
        },
        "UnappliedAmt": 0,
        "TxnDate": "2015-02-04",
        "TotalAmt": 15.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "ProcessPayment": false,
        "sparse": false,
        "Line": [
          {
            "Amount": 15.0,
            "LineEx": {
              "any": [
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnId",
                    "Value": "70"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                },
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnOpenBalance",
                    "Value": "31.00"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                },
                {
                  "name": "{http://schema.intuit.com/finance/v3}NameValue",
                  "nil": false,
                  "value": {
                    "Name": "txnReferenceNumber",
                    "Value": "1024"
                  },
                  "declaredType": "com.intuit.schema.finance.v3.NameValue",
                  "scope": "javax.xml.bind.JAXBElement$GlobalScope",
                  "globalScope": true,
                  "typeSubstituted": false
                }
              ]
            },
            "LinkedTxn": [
              {
                "TxnId": "70",
                "TxnType": "Invoice"
              }
            ]
          }
        ],
        "CustomerRef": {
          "name": "Red Rock Diner",
          "value": "20"
        },
        "Id": "170",
        "MetaData": {
          "CreateTime": "2015-02-04T10:42:16-08:00",
          "LastUpdatedTime": "2015-02-04T10:42:16-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "value": "4"
        },
        "UnappliedAmt": 55.0,
        "TxnDate": "2015-02-04",
        "TotalAmt": 55.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "ProcessPayment": false,
        "sparse": false,
        "Line": [],
        "CustomerRef": {
          "name": "Red Rock Diner",
          "value": "20"
        },
        "Id": "171",
        "MetaData": {
          "CreateTime": "2015-02-04T10:42:33-08:00",
          "LastUpdatedTime": "2015-02-04T10:42:33-08:00"
        }
      }
    ],
    "maxResults": 6
  },
  "time": "2015-07-28T15:15:25.802-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T15:14:56.605-07:00">
  <QueryResponse startPosition="1" maxResults="6">
    <Payment domain="QBO" sparse="false">
      <Id>161</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2015-01-16T14:58:32-08:00</CreateTime>
        <LastUpdatedTime>2015-01-16T14:58:32-08:00</LastUpdatedTime>
      </MetaData>
      <TxnDate>2015-01-16</TxnDate>
      <CustomerRef name="Red Rock Diner">20</CustomerRef>
      <ProjectRef>39298034</ProjectRef>
      <DepositToAccountRef>4</DepositToAccountRef>
      <TotalAmt>55.00</TotalAmt>
      <UnappliedAmt>55.00</UnappliedAmt>
      <ProcessPayment>false</ProcessPayment>
    </Payment>
    <Payment domain="QBO" sparse="false">
      <Id>162</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2015-01-16T14:58:59-08:00</CreateTime>
        <LastUpdatedTime>2015-01-16T14:58:59-08:00</LastUpdatedTime>
      </MetaData>
      <TxnDate>2015-01-16</TxnDate>
      <CustomerRef name="Red Rock Diner">20</CustomerRef>
      <ProjectRef>39298034</ProjectRef>
      <DepositToAccountRef>4</DepositToAccountRef>
      <TotalAmt>65.00</TotalAmt>
      <UnappliedAmt>65.00</UnappliedAmt>
      <ProcessPayment>false</ProcessPayment>
    </Payment>
    <Payment domain="QBO" sparse="false">
      <Id>163</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2015-01-16T15:08:12-08:00</CreateTime>
        <LastUpdatedTime>2015-01-16T15:08:12-08:00</LastUpdatedTime>
      </MetaData>
      <TxnDate>2015-01-16</TxnDate>
      <Line>
        <Amount>55.00</Amount>
        <LinkedTxn>
          <TxnId>70</TxnId>
          <TxnType>Invoice</TxnType>
        </LinkedTxn>
        <LineEx>
          <NameValue>
            <Name>txnId</Name>
            <Value>70</Value>
          </NameValue>
          <NameValue>
            <Name>txnOpenBalance</Name>
            <Value>71.00</Value>
          </NameValue>
          <NameValue>
            <Name>txnReferenceNumber</Name>
            <Value>1024</Value>
          </NameValue>
        </LineEx>
      </Line>
      <CustomerRef name="Red Rock Diner">20</CustomerRef>
      <ProjectRef>39298034</ProjectRef>
      <DepositToAccountRef>4</DepositToAccountRef>
      <TotalAmt>65.00</TotalAmt>
      <UnappliedAmt>10.00</UnappliedAmt>
      <ProcessPayment>false</ProcessPayment>
    </Payment>
    <Payment domain="QBO" sparse="false">
      <Id>164</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2015-01-16T15:09:22-08:00</CreateTime>
        <LastUpdatedTime>2015-01-16T15:09:22-08:00</LastUpdatedTime>
      </MetaData>
      <TxnDate>2015-01-16</TxnDate>
      <Line>
        <Amount>55.00</Amount>
        <LinkedTxn>
          <TxnId>70</TxnId>
          <TxnType>Invoice</TxnType>
        </LinkedTxn>
        <LineEx>
          <NameValue>
            <Name>txnId</Name>
            <Value>70</Value>
          </NameValue>
          <NameValue>
            <Name>txnOpenBalance</Name>
            <Value>71.00</Value>
          </NameValue>
          <NameValue>
            <Name>txnReferenceNumber</Name>
            <Value>1024</Value>
          </NameValue>
        </LineEx>
      </Line>
      <CustomerRef name="Red Rock Diner">20</CustomerRef>
      <ProjectRef>39298034</ProjectRef>
      <DepositToAccountRef>4</DepositToAccountRef>
      <TotalAmt>300.00</TotalAmt>
      <UnappliedAmt>245.00</UnappliedAmt>
      <ProcessPayment>false</ProcessPayment>
    </Payment>
    <Payment domain="QBO" sparse="false">
      <Id>170</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2015-02-04T10:42:16-08:00</CreateTime>
        <LastUpdatedTime>2015-02-04T10:42:16-08:00</LastUpdatedTime>
      </MetaData>
      <TxnDate>2015-02-04</TxnDate>
      <Line>
        <Amount>15.00</Amount>
        <LinkedTxn>
          <TxnId>70</TxnId>
          <TxnType>Invoice</TxnType>
        </LinkedTxn>
        <LineEx>
          <NameValue>
            <Name>txnId</Name>
            <Value>70</Value>
          </NameValue>
          <NameValue>
            <Name>txnOpenBalance</Name>
            <Value>31.00</Value>
          </NameValue>
          <NameValue>
            <Name>txnReferenceNumber</Name>
            <Value>1024</Value>
          </NameValue>
        </LineEx>
      </Line>
      <CustomerRef name="Red Rock Diner">20</CustomerRef>
      <ProjectRef>39298034</ProjectRef>
      <DepositToAccountRef>4</DepositToAccountRef>
      <TotalAmt>15.00</TotalAmt>
      <UnappliedAmt>0</UnappliedAmt>
      <ProcessPayment>false</ProcessPayment>
    </Payment>
    <Payment domain="QBO" sparse="false">
      <Id>171</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2015-02-04T10:42:33-08:00</CreateTime>
        <LastUpdatedTime>2015-02-04T10:42:33-08:00</LastUpdatedTime>
      </MetaData>
      <TxnDate>2015-02-04</TxnDate>
      <CustomerRef name="Red Rock Diner">20</CustomerRef>
      <ProjectRef>39298034</ProjectRef>
      <DepositToAccountRef>4</DepositToAccountRef>
      <TotalAmt>55.00</TotalAmt>
      <UnappliedAmt>55.00</UnappliedAmt>
      <ProcessPayment>false</ProcessPayment>
    </Payment>
  </QueryResponse>
</IntuitResponse>
```

## Read a payment

### Definition

- **Content type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/payment/<paymentId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Payment object that has been previously created.

### Returns

The Payment object response body.

#### Example

```json
{
  "Payment": {
    "SyncToken": "0",
    "domain": "QBO",
    "DepositToAccountRef": {
      "value": "4"
    },
    "UnappliedAmt": 10.0,
    "TxnDate": "2015-01-16",
    "TotalAmt": 65.0,
    "ProjectRef": {
      "value": "39298034"
    },
    "ProcessPayment": false,
    "sparse": false,
    "Line": [
      {
        "Amount": 55.0,
        "LineEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnId",
                "Value": "70"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            },
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnOpenBalance",
                "Value": "71.00"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            },
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnReferenceNumber",
                "Value": "1024"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "LinkedTxn": [
          {
            "TxnId": "70",
            "TxnType": "Invoice"
          }
        ]
      }
    ],
    "CustomerRef": {
      "name": "Red Rock Diner",
      "value": "20"
    },
    "Id": "163",
    "MetaData": {
      "CreateTime": "2015-01-16T15:08:12-08:00",
      "LastUpdatedTime": "2015-01-16T15:08:12-08:00"
    }
  },
  "time": "2015-07-28T15:16:15.435-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T15:16:38.467-07:00">
  <Payment domain="QBO" sparse="false">
    <Id>163</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-01-16T15:08:12-08:00</CreateTime>
      <LastUpdatedTime>2015-01-16T15:08:12-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-01-16</TxnDate>
    <Line>
      <Amount>55.00</Amount>
      <LinkedTxn>
        <TxnId>70</TxnId>
        <TxnType>Invoice</TxnType>
      </LinkedTxn>
      <LineEx>
        <NameValue>
          <Name>txnId</Name>
          <Value>70</Value>
        </NameValue>
        <NameValue>
          <Name>txnOpenBalance</Name>
          <Value>71.00</Value>
        </NameValue>
        <NameValue>
          <Name>txnReferenceNumber</Name>
          <Value>1024</Value>
        </NameValue>
      </LineEx>
    </Line>
    <CustomerRef name="Red Rock Diner">20</CustomerRef>
    <ProjectRef>39298034</ProjectRef>
    <DepositToAccountRef>4</DepositToAccountRef>
    <TotalAmt>65.00</TotalAmt>
    <UnappliedAmt>10.00</UnappliedAmt>
    <ProcessPayment>false</ProcessPayment>
  </Payment>
</IntuitResponse>
```

## Send a payment

### Definition

- **Content type:** `application/octet-stream`
- **Operation:** `
POST(Specifying an explicit email address) /v3/company/<realmID>/payment/<paymentId>/send?sendTo=<emailAddr>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- The email address should be explicitly mentioned in the POST request

### Returns

The Payment response body.

#### Example

```json
{
  "Payment": {
    "SyncToken": "0",
    "domain": "QBO",
    "DepositToAccountRef": {
      "value": "4"
    },
    "UnappliedAmt": 10.0,
    "TxnDate": "2015-01-16",
    "TotalAmt": 65.0,
    "ProjectRef": {
      "value": "39298034"
    },
    "ProcessPayment": false,
    "sparse": false,
    "Line": [
      {
        "Amount": 55.0,
        "LineEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnId",
                "Value": "70"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            },
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnOpenBalance",
                "Value": "71.00"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            },
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "txnReferenceNumber",
                "Value": "1024"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "LinkedTxn": [
          {
            "TxnId": "70",
            "TxnType": "Invoice"
          }
        ]
      }
    ],
    "CustomerRef": {
      "name": "Red Rock Diner",
      "value": "20"
    },
    "Id": "163",
    "MetaData": {
      "CreateTime": "2015-01-16T15:08:12-08:00",
      "LastUpdatedTime": "2015-01-16T15:08:12-08:00"
    }
  },
  "time": "2015-07-28T15:16:15.435-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T15:16:38.467-07:00">
  <Payment domain="QBO" sparse="false">
    <Id>163</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-01-16T15:08:12-08:00</CreateTime>
      <LastUpdatedTime>2015-01-16T15:08:12-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-01-16</TxnDate>
    <Line>
      <Amount>55.00</Amount>
      <LinkedTxn>
        <TxnId>70</TxnId>
        <TxnType>Invoice</TxnType>
      </LinkedTxn>
      <LineEx>
        <NameValue>
          <Name>txnId</Name>
          <Value>70</Value>
        </NameValue>
        <NameValue>
          <Name>txnOpenBalance</Name>
          <Value>71.00</Value>
        </NameValue>
        <NameValue>
          <Name>txnReferenceNumber</Name>
          <Value>1024</Value>
        </NameValue>
      </LineEx>
    </Line>
    <CustomerRef name="Red Rock Diner">20</CustomerRef>
    <ProjectRef>39298034</ProjectRef>
    <DepositToAccountRef>4</DepositToAccountRef>
    <TotalAmt>65.00</TotalAmt>
    <UnappliedAmt>10.00</UnappliedAmt>
    <ProcessPayment>false</ProcessPayment>
  </Payment>
</IntuitResponse>
```

## Full update a payment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/payment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing Payment object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `paymentresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "PaymentMethodRef": {
    "value": "16"
  },
  "ProjectRef": {
    "value": "39298045"
  },
  "PaymentRefNum": "123456",
  "sparse": false,
  "Line": [
    {
      "Amount": 300,
      "LinkedTxn": [
        {
          "TxnId": "67",
          "TxnType": "Invoice"
        }
      ]
    },
    {
      "Amount": 300,
      "LinkedTxn": [
        {
          "TxnId": "68",
          "TxnType": "CreditMemo"
        }
      ]
    }
  ],
  "CustomerRef": {
    "value": "16"
  },
  "Id": "69",
  "MetaData": {
    "CreateTime": "2013-03-13T14:49:21-07:00",
    "LastUpdatedTime": "2013-03-13T14:49:21-07:00"
  }
}
```

#### XML example

```xml
<Payment xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
         <Id>8748</Id>
         <SyncToken>0</SyncToken>
         <MetaData>
            <CreateTime>2013-07-11T17:51:41-07:00</CreateTime>
            <LastUpdatedTime>2013-07-11T17:51:41-07:00</LastUpdatedTime>
         </MetaData>
         <TxnDate>2013-07-11</TxnDate>
         <PrivateNote>H60jzmw0Uq</PrivateNote>
         <CustomerRef>25342</CustomerRef>
         <ProjectRef>39298034</ProjectRef>
         <DepositToAccountRef>4</DepositToAccountRef>
         <TotalAmt>40.00</TotalAmt>
         <UnappliedAmt>40.00</UnappliedAmt>
</Payment>
```

### Returns

The payment response body.

#### Example

```json
{
  "Payment": {
    "SyncToken": "1",
    "domain": "QBO",
    "PaymentMethodRef": {
      "value": "16"
    },
    "UnappliedAmt": 0,
    "TxnDate": "2013-03-13",
    "TotalAmt": 0,
    "ProjectRef": {
      "value": "39298045"
    },
    "PaymentRefNum": "123456",
    "sparse": false,
    "Line": [
      {
        "Amount": 300,
        "LinkedTxn": [
          {
            "TxnId": "67",
            "TxnType": "Invoice"
          }
        ]
      },
      {
        "Amount": 300,
        "LinkedTxn": [
          {
            "TxnId": "68",
            "TxnType": "CreditMemo"
          }
        ]
      }
    ],
    "CustomerRef": {
      "value": "16"
    },
    "Id": "69",
    "MetaData": {
      "CreateTime": "2013-03-13T14:49:21-07:00",
      "LastUpdatedTime": "2013-03-13T14:49:21-07:00"
    }
  },
  "time": "2013-03-13T14:49:41.512-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T18:10:54.259-07:00">
    <Payment domain="QBO" sparse="false">
         <Id>8748</Id>
         <SyncToken>1</SyncToken>
         <MetaData>
            <CreateTime>2013-07-11T17:51:41-07:00</CreateTime>
            <LastUpdatedTime>2013-07-11T17:51:43-07:00</LastUpdatedTime>
         </MetaData>
         <TxnDate>2013-07-11</TxnDate>
         <PrivateNote>H60jzmw0Uq</PrivateNote>
         <CustomerRef>25342</CustomerRef>
         <ProjectRef>39298034</ProjectRef>
         <DepositToAccountRef>4</DepositToAccountRef>
         <TotalAmt>40.00</TotalAmt>
         <UnappliedAmt>40.00</UnappliedAmt>
    </Payment>
</IntuitResponse>
```
