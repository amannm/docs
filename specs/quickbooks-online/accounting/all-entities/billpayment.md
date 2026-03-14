# BillPayment

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/billpayment
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / BillPayment
> Canonical entity: `BillPayment`

A BillPayment object represents the payment transaction for a bill that the business owner receives from a vendor for goods or services purchased from the vendor. QuickBooks Online supports bill payments through a credit card or a checking account.
`BillPayment.TotalAmt` is the total amount associated with this payment. This includes the total of all the payments from the payment line details. If `TotalAmt` is greater than the total on the lines being paid, the overpayment is treated as a credit and exposed as such on the QuickBooks UI. The total amount cannot be negative.

## The billpayment object

### billpaymentresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique Identifier for an Intuit entity (object). Sort order is ASC by default.

#### `VendorRef`

Required: Required
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the vendor for this transaction. Query the Vendor name list resource to determine the appropriate Vendor object for this reference. Use `Vendor.Id` and `Vendor.Name` from that object for `VendorRef.value` and `VendorRef.name`, respectively.

<details>
<summary>Child attributes for `VendorRef`</summary>

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

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items representing zero or more `Bill`, `VendorCredit`, and `JournalEntry` objects linked to this BillPayment object. Use `Line.LinkedTxn.TxnId` as the ID in a separate Bill, VendorCredit, or JournalEntry read request to retrieve details of the linked object.
 LinkedTxnLine:

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

#### `TotalAmt`

Required: Required
Type: `BigDecimal`
Traits: filterable, sortable

Indicates the total amount associated with this payment. This includes the total of all the payments from the payment line details. If `TotalAmt` is greater than the total on the lines being paid, the overpayment is treated as a credit and exposed as such on the QuickBooks UI. It cannot be negative.

#### `PayType`

Required: Required
Type: `BillPaymentTypeEnum`

The payment type. Valid values include: `Check`, `CreditCard`

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies).Required if multicurrency is enabled for the company

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

#### `CheckPayment`

Type: `BillPaymentCheck`
Traits: filterable, sortable

Information about a check payment for the transaction. Not applicable to Estimate and SalesOrder. Used when PayType is `Check`.

<details>
<summary>Child attributes for `CheckPayment`</summary>

##### billpaymentcheck

Model type: `object`

###### `BankAccountRef`

Required: Required
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the bank account. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `APAccountRef.value` and `APAccountRef.name`, respectively. The specified account must have `Account.AccountType` set to `Bank` and `Account.AccountSubType` set to `Checking`.

<details>
<summary>Child attributes for `BankAccountRef`</summary>

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

###### `PrintStatus`

Required: Optional
Type: `PrintStatusEnum`
Default: NeedToPrint

`NeedToPrint` Printing status of the invoice. Valid values: `NotSet`, `NeedToPrint`, `PrintComplete`.

</details>

#### `CreditCardPayment`

Type: `BillPaymentCreditCard`
Traits: filterable, sortable

Information about a credit card payment for the transaction. Not applicable to Estimate and SalesOrder. Used when PayType is `CreditCard`.

<details>
<summary>Child attributes for `CreditCardPayment`</summary>

##### billpaymentcreditcard

Model type: `object`

###### `CCAccountRef`

Required: Required
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the credit card account. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `CCAccountRef.value` and `CCAccountRef.name`, respectively. The specified account must have `Account.AccountType` set to `Credit Card` and `Account.AccountSubType` set to `CreditCard`. Inject with data only if the payment was transacted through Intuit Payments API.

<details>
<summary>Child attributes for `CCAccountRef`</summary>

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

</details>

#### `DocNumber`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 21 chars

Reference number for the transaction. If not explicitly provided at create time, a custom value can be provided. If no value is supplied, the resulting DocNumber is null. Throws an error when duplicate DocNumber is sent in the request. Recommended best practice: check the setting of `Preferences:OtherPrefs` before setting DocNumber. If a duplicate DocNumber needs to be supplied, add the query parameter name/value pair, `include=allowduplicatedocnum` to the URI. Sort order is ASC by default.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Memo field on the form.

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: current server date

The date entered by the user when this transaction occurred. For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.
Sort order is ASC by default.

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1, applicable if multicurrency is enabled for the company

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

#### `APAccountRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable, sortable

Specifies to which AP account the bill is credited. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `APAccountRef.value` and `APAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Liability` and `Account.AccountSubType` set to `AccountsPayable`.
If the company has a single AP account, the account is implied. However, it is recommended that the AP Account be explicitly specified in all cases to prevent unexpected errors when relating transactions to each other.

<details>
<summary>Child attributes for `APAccountRef`</summary>

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

#### `DepartmentRef`

Required: Optional
Type: `ReferenceType`

A reference to a Department object specifying the location of the transaction, as defined using location tracking in QuickBooks Online. Query the Department name list resource to determine the appropriate department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

<details>
<summary>Child attributes for `DepartmentRef`</summary>

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

#### `TransactionLocationType`

Required: Optional
Type: `String`
Default: WithinFrance
Minor version: 4
Locales: FR

The account location. Valid values include:

`WithinFrance`

`FranceOverseas`

`OutsideFranceWithEU`

`OutsideEU`

For France locales, only.

#### `ProcessBillPayment`

Required: Optional
Type: `Boolean`

Indicates that the payment should be processed by merchant account service. Valid for QuickBooks companies with credit card processing.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the object. The MetaData values are set by Data Services and are read only for all applications.

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
  "BillPayment": {
    "SyncToken": "0",
    "domain": "QBO",
    "VendorRef": {
      "name": "Bob's Burger Joint",
      "value": "56"
    },
    "TxnDate": "2015-07-14",
    "TotalAmt": 200.0,
    "PayType": "Check",
    "PrivateNote": "Acct. 1JK90",
    "sparse": false,
    "Line": [
      {
        "Amount": 200.0,
        "LinkedTxn": [
          {
            "TxnId": "234",
            "TxnType": "Bill"
          }
        ]
      }
    ],
    "Id": "236",
    "CheckPayment": {
      "PrintStatus": "NeedToPrint",
      "BankAccountRef": {
        "name": "Checking",
        "value": "35"
      }
    },
    "MetaData": {
      "CreateTime": "2015-07-14T12:34:04-07:00",
      "LastUpdatedTime": "2015-07-14T12:34:04-07:00"
    }
  },
  "time": "2015-07-14T12:34:03.964-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-14T12:37:57.599-07:00">
  <BillPayment domain="QBO" sparse="false">
    <Id>237</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-14T12:37:57-07:00</CreateTime>
      <LastUpdatedTime>2015-07-14T12:37:57-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-07-14</TxnDate>
    <VendorRef name="Bob's Burger Joint">56</VendorRef>
    <PayType>Check</PayType>
    <CheckPayment>
      <BankAccountRef name="Checking">35</BankAccountRef>
      <PrintStatus>NotSet</PrintStatus>
    </CheckPayment>
    <TotalAmt>110.00</TotalAmt>
  </BillPayment>
</IntuitResponse>
```

## Create a billpayment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/billpayment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create an billpayment are listed here.

Schema: `billpaymentrequest`

<details>
<summary>Show schema for `billpaymentrequest`</summary>

#### billpaymentrequest

Model type: `object`

##### `VendorRef`

Required: Required
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the vendor for this transaction.

<details>
<summary>Child attributes for `VendorRef`</summary>

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

##### `TotalAmt`

Required: Required
Type: `BigDecimal`
Traits: filterable, sortable

Indicates the total amount of the associated with this payment. This includes the total of all the payments from the BillPayment Details.

##### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items representing zero or more `Bill`, `VendorCredit`, and `JournalEntry` objects linked to this BillPayment object. Valid `Line` types include:
 LinkedTxnLine:

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### linelinkedtxn

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

##### `PayType`

Required: Required
Type: `BillPaymentTypeEnum`

The payment type. Valid values include: `Check`, `CreditCard`

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

##### `CreditCardPayment`

Required: Conditionally required
Type: `BillPaymentCreditCard`
Traits: filterable, sortable

Information about a credit card payment for the transaction. Not applicable to Estimate and SalesOrder. Required when `PayType` is `CreditCard`.

<details>
<summary>Child attributes for `CreditCardPayment`</summary>

###### billpaymentcreditcard

Model type: `object`

###### `CCAccountRef`

Required: Required
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the credit card account. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `CCAccountRef.value` and `CCAccountRef.name`, respectively. The specified account must have `Account.AccountType` set to `Credit Card` and `Account.AccountSubType` set to `CreditCard`. Inject with data only if the payment was transacted through Intuit Payments API.

<details>
<summary>Child attributes for `CCAccountRef`</summary>

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

</details>

##### `CheckPayment`

Required: Conditionally required
Type: `BillPaymentCheck`

Reference to the vendor for this transaction. Required when `PayType` is `Check`.

<details>
<summary>Child attributes for `CheckPayment`</summary>

###### billpaymentcheck

Model type: `object`

###### `BankAccountRef`

Required: Required
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the bank account. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `APAccountRef.value` and `APAccountRef.name`, respectively. The specified account must have `Account.AccountType` set to `Bank` and `Account.AccountSubType` set to `Checking`.

<details>
<summary>Child attributes for `BankAccountRef`</summary>

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

###### `PrintStatus`

Required: Optional
Type: `PrintStatusEnum`
Default: NeedToPrint

`NeedToPrint` Printing status of the invoice. Valid values: `NotSet`, `NeedToPrint`, `PrintComplete`.

</details>

</details>

#### Example

```json
{
  "PrivateNote": "Acct. 1JK90",
  "VendorRef": {
    "name": "Bob's Burger Joint",
    "value": "56"
  },
  "TotalAmt": 200.0,
  "PayType": "Check",
  "Line": [
    {
      "Amount": 200.0,
      "LinkedTxn": [
        {
          "TxnId": "234",
          "TxnType": "Bill"
        }
      ]
    }
  ],
  "CheckPayment": {
    "BankAccountRef": {
      "name": "Checking",
      "value": "35"
    }
  }
}
```

#### XML example

```xml
<BillPayment xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Line>
        <Amount>110.00</Amount>
        <LinkedTxn>
            <TxnId>234</TxnId>
            <TxnType>Bill</TxnType>
        </LinkedTxn>
    </Line>
    <VendorRef name="Bob's Burger Joint">56</VendorRef>
    <PayType>Check</PayType>
    <CheckPayment>
        <BankAccountRef name="Checking">35</BankAccountRef>
        <PrintStatus>NotSet</PrintStatus>
    </CheckPayment>
    <TotalAmt>110.00</TotalAmt>
</BillPayment>
```

### Returns

The billpayment response body.

#### Example

```json
{
  "BillPayment": {
    "SyncToken": "0",
    "domain": "QBO",
    "VendorRef": {
      "name": "Bob's Burger Joint",
      "value": "56"
    },
    "TxnDate": "2015-07-14",
    "TotalAmt": 200.0,
    "PayType": "Check",
    "PrivateNote": "Acct. 1JK90",
    "sparse": false,
    "Line": [
      {
        "Amount": 200.0,
        "LinkedTxn": [
          {
            "TxnId": "234",
            "TxnType": "Bill"
          }
        ]
      }
    ],
    "Id": "236",
    "CheckPayment": {
      "PrintStatus": "NeedToPrint",
      "BankAccountRef": {
        "name": "Checking",
        "value": "35"
      }
    },
    "MetaData": {
      "CreateTime": "2015-07-14T12:34:04-07:00",
      "LastUpdatedTime": "2015-07-14T12:34:04-07:00"
    }
  },
  "time": "2015-07-14T12:34:03.964-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-14T12:37:57.599-07:00">
  <BillPayment domain="QBO" sparse="false">
    <Id>237</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-14T12:37:57-07:00</CreateTime>
      <LastUpdatedTime>2015-07-14T12:37:57-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-07-14</TxnDate>
    <VendorRef name="Bob's Burger Joint">56</VendorRef>
    <PayType>Check</PayType>
    <CheckPayment>
      <BankAccountRef name="Checking">35</BankAccountRef>
      <PrintStatus>NotSet</PrintStatus>
    </CheckPayment>
    <TotalAmt>110.00</TotalAmt>
  </BillPayment>
</IntuitResponse>
```

## Void a billpayment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/billpayment?operation=update&include=void`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use a sparse update operation with `include=void` to void an existing BillPayment object; include a minimum of `BillPayment.Id` and `BillPayment.SyncToken`. The transaction remains active but all amounts and quantities are zeroed, all lines are cleared, and the string, `Voided`, is injected into `BillPayment.PrivateNote`, prepended to existing text if present.

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
  "SyncToken": "0",
  "Id": "104",
  "sparse": true
}
```

#### XML example

```text
Sample request not available.
```

### Returns

The BillPayment response body.

#### Example

```json
{
  "BillPayment": {
    "DocNumber": "11",
    "SyncToken": "1",
    "domain": "QBO",
    "VendorRef": {
      "name": "Hall Properties",
      "value": "40"
    },
    "TxnDate": "2016-08-18",
    "TotalAmt": 0,
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "PayType": "Check",
    "PrivateNote": "Voided",
    "sparse": false,
    "Line": [],
    "Id": "104",
    "CheckPayment": {
      "PrintStatus": "NotSet",
      "BankAccountRef": {
        "name": "Cash on hand",
        "value": "9"
      }
    },
    "MetaData": {
      "CreateTime": "2016-08-18T13:11:14-07:00",
      "LastUpdatedTime": "2016-08-18T13:27:13-07:00"
    }
  },
  "time": "2016-08-18T13:27:13.323-07:00"
}
```

#### XML example

```text
Sample response not available.
```

## Delete a billpayment

### Definition

- **Operation:** `POST /v3/company/<realmID>/billpayment?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the billpayment object specified in the request body. Include a minimum of `BillPayment.Id` and `BillPayment.SyncToken` in the request body.

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
  "SyncToken": "0",
  "Id": "117"
}
```

#### XML example

```xml
<BillPayment xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>118</Id>
    <SyncToken>0</SyncToken>
</BillPayment>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "BillPayment": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "117"
  },
  "time": "2015-05-26T13:17:25.316-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-05-26T13:31:36.761-07:00">
    <BillPayment domain="QBO" status="Deleted">
        <Id>118</Id>
    </BillPayment>
</IntuitResponse>
```

## Query a billpayment

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from billpayment Where Metadata.LastUpdatedTime>'2014-12-12T14:50:22-08:00' Order By Metadata.LastUpdatedTime"
```

#### XML example

```sql
select * from billpayment Where Metadata.LastUpdatedTime>'2014-12-12T14:50:22-08:00' Order By Metadata.LastUpdatedTime
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "BillPayment": [
      {
        "DocNumber": "1",
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "PG&E",
          "value": "48"
        },
        "TxnDate": "2015-01-16",
        "TotalAmt": 86.44,
        "CurrencyRef": {
          "name": "United States Dollar",
          "value": "USD"
        },
        "PayType": "CreditCard",
        "PrivateNote": "00649587213",
        "sparse": false,
        "CreditCardPayment": {
          "CCAccountRef": {
            "name": "Mastercard",
            "value": "41"
          }
        },
        "Line": [
          {
            "Amount": 86.44,
            "LinkedTxn": [
              {
                "TxnId": "78",
                "TxnType": "Bill"
              }
            ]
          }
        ],
        "Id": "165",
        "MetaData": {
          "CreateTime": "2015-01-16T15:36:20-08:00",
          "LastUpdatedTime": "2015-01-16T15:36:20-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Bob's Burger Joint",
          "value": "56"
        },
        "TxnDate": "2015-01-16",
        "TotalAmt": 200.0,
        "PayType": "CreditCard",
        "sparse": false,
        "CreditCardPayment": {
          "CCAccountRef": {
            "name": "Mastercard",
            "value": "41"
          }
        },
        "Line": [
          {
            "Amount": 200.0,
            "LinkedTxn": [
              {
                "TxnId": "157",
                "TxnType": "Bill"
              }
            ]
          }
        ],
        "Id": "166",
        "MetaData": {
          "CreateTime": "2015-01-16T15:40:26-08:00",
          "LastUpdatedTime": "2015-01-16T15:40:26-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Norton Lumber and Building Materials",
          "value": "46"
        },
        "TxnDate": "2015-01-16",
        "TotalAmt": 205.0,
        "PayType": "CreditCard",
        "sparse": false,
        "CreditCardPayment": {
          "CCAccountRef": {
            "name": "Mastercard",
            "value": "41"
          }
        },
        "Line": [
          {
            "Amount": 205.0,
            "LinkedTxn": [
              {
                "TxnId": "126",
                "TxnType": "Bill"
              }
            ]
          }
        ],
        "Id": "169",
        "MetaData": {
          "CreateTime": "2015-01-16T16:00:29-08:00",
          "LastUpdatedTime": "2015-01-16T16:00:29-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Robertson & Associates",
          "value": "49"
        },
        "TxnDate": "2015-06-30",
        "TotalAmt": 110.0,
        "PayType": "Check",
        "PrivateNote": "Acct. 1JK90",
        "sparse": false,
        "Line": [
          {
            "Amount": 110.0,
            "LinkedTxn": [
              {
                "TxnId": "108",
                "TxnType": "Bill"
              }
            ]
          }
        ],
        "Id": "231",
        "CheckPayment": {
          "PrintStatus": "NeedToPrint",
          "BankAccountRef": {
            "name": "Checking",
            "value": "35"
          }
        },
        "MetaData": {
          "CreateTime": "2015-06-30T15:05:30-07:00",
          "LastUpdatedTime": "2015-06-30T15:05:30-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Robertson & Associates",
          "value": "49"
        },
        "TxnDate": "2015-06-30",
        "TotalAmt": 110.0,
        "PayType": "Check",
        "PrivateNote": "Acct. 1JK90",
        "sparse": false,
        "Line": [
          {
            "Amount": 110.0,
            "LinkedTxn": [
              {
                "TxnId": "108",
                "TxnType": "Bill"
              }
            ]
          }
        ],
        "Id": "232",
        "CheckPayment": {
          "PrintStatus": "NeedToPrint",
          "BankAccountRef": {
            "name": "Checking",
            "value": "35"
          }
        },
        "MetaData": {
          "CreateTime": "2015-06-30T15:09:06-07:00",
          "LastUpdatedTime": "2015-06-30T15:09:06-07:00"
        }
      },
      {
        "DocNumber": "1",
        "SyncToken": "2",
        "domain": "QBO",
        "VendorRef": {
          "name": "Brosnahan Insurance Agency",
          "value": "31"
        },
        "TxnDate": "2014-09-16",
        "TotalAmt": 2000.0,
        "PayType": "Check",
        "PrivateNote": "Add private note",
        "sparse": false,
        "Line": [
          {
            "Amount": 2000.0,
            "LinkedTxn": [
              {
                "TxnId": "1",
                "TxnType": "Bill"
              }
            ]
          }
        ],
        "Id": "22",
        "CheckPayment": {
          "PrintStatus": "NotSet",
          "BankAccountRef": {
            "name": "Checking",
            "value": "35"
          }
        },
        "MetaData": {
          "CreateTime": "2014-09-16T15:28:48-07:00",
          "LastUpdatedTime": "2015-06-30T15:24:40-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Bob's Burger Joint",
          "value": "56"
        },
        "TxnDate": "2015-07-14",
        "TotalAmt": 200.0,
        "PayType": "Check",
        "PrivateNote": "Acct. 1JK90",
        "sparse": false,
        "Line": [
          {
            "Amount": 200.0,
            "LinkedTxn": [
              {
                "TxnId": "234",
                "TxnType": "Bill"
              }
            ]
          }
        ],
        "Id": "236",
        "CheckPayment": {
          "PrintStatus": "NeedToPrint",
          "BankAccountRef": {
            "name": "Checking",
            "value": "35"
          }
        },
        "MetaData": {
          "CreateTime": "2015-07-14T12:34:04-07:00",
          "LastUpdatedTime": "2015-07-14T12:34:04-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Bob's Burger Joint",
          "value": "56"
        },
        "TxnDate": "2015-07-14",
        "TotalAmt": 110.0,
        "PayType": "Check",
        "sparse": false,
        "Line": [],
        "Id": "237",
        "CheckPayment": {
          "PrintStatus": "NotSet",
          "BankAccountRef": {
            "name": "Checking",
            "value": "35"
          }
        },
        "MetaData": {
          "CreateTime": "2015-07-14T12:37:57-07:00",
          "LastUpdatedTime": "2015-07-14T12:37:57-07:00"
        }
      }
    ],
    "startPosition": 1,
    "maxResults": 8,
    "totalCount": 8
  },
  "time": "2015-07-14T12:48:36.854-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-14T12:49:11.070-07:00">
    <QueryResponse startPosition="1" maxResults="8" totalCount="8">
        <BillPayment domain="QBO" sparse="false">
            <Id>165</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-01-16T15:36:20-08:00</CreateTime>
                <LastUpdatedTime>2015-01-16T15:36:20-08:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>1</DocNumber>
            <TxnDate>2015-01-16</TxnDate>
            <CurrencyRef name="United States Dollar">USD</CurrencyRef>
            <PrivateNote>00649587213</PrivateNote>
            <Line>
                <Amount>86.44</Amount>
                <LinkedTxn>
                    <TxnId>78</TxnId>
                    <TxnType>Bill</TxnType>
                </LinkedTxn>
            </Line>
            <VendorRef name="PG&amp;E">48</VendorRef>
            <PayType>CreditCard</PayType>
            <CreditCardPayment>
                <CCAccountRef name="Mastercard">41</CCAccountRef>
            </CreditCardPayment>
            <TotalAmt>86.44</TotalAmt>
        </BillPayment>
        <BillPayment domain="QBO" sparse="false">
            <Id>166</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-01-16T15:40:26-08:00</CreateTime>
                <LastUpdatedTime>2015-01-16T15:40:26-08:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2015-01-16</TxnDate>
            <Line>
                <Amount>200.00</Amount>
                <LinkedTxn>
                    <TxnId>157</TxnId>
                    <TxnType>Bill</TxnType>
                </LinkedTxn>
            </Line>
            <VendorRef name="Bob's Burger Joint">56</VendorRef>
            <PayType>CreditCard</PayType>
            <CreditCardPayment>
                <CCAccountRef name="Mastercard">41</CCAccountRef>
            </CreditCardPayment>
            <TotalAmt>200.00</TotalAmt>
        </BillPayment>
        <BillPayment domain="QBO" sparse="false">
            <Id>169</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-01-16T16:00:29-08:00</CreateTime>
                <LastUpdatedTime>2015-01-16T16:00:29-08:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2015-01-16</TxnDate>
            <Line>
                <Amount>205.00</Amount>
                <LinkedTxn>
                    <TxnId>126</TxnId>
                    <TxnType>Bill</TxnType>
                </LinkedTxn>
            </Line>
            <VendorRef name="Norton Lumber and Building Materials">46</VendorRef>
            <PayType>CreditCard</PayType>
            <CreditCardPayment>
                <CCAccountRef name="Mastercard">41</CCAccountRef>
            </CreditCardPayment>
            <TotalAmt>205.00</TotalAmt>
        </BillPayment>
        <BillPayment domain="QBO" sparse="false">
            <Id>231</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-06-30T15:05:30-07:00</CreateTime>
                <LastUpdatedTime>2015-06-30T15:05:30-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2015-06-30</TxnDate>
            <PrivateNote>Acct. 1JK90</PrivateNote>
            <Line>
                <Amount>110.00</Amount>
                <LinkedTxn>
                    <TxnId>108</TxnId>
                    <TxnType>Bill</TxnType>
                </LinkedTxn>
            </Line>
            <VendorRef name="Robertson &amp; Associates">49</VendorRef>
            <PayType>Check</PayType>
            <CheckPayment>
                <BankAccountRef name="Checking">35</BankAccountRef>
                <PrintStatus>NeedToPrint</PrintStatus>
            </CheckPayment>
            <TotalAmt>110.00</TotalAmt>
        </BillPayment>
        <BillPayment domain="QBO" sparse="false">
            <Id>232</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-06-30T15:09:06-07:00</CreateTime>
                <LastUpdatedTime>2015-06-30T15:09:06-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2015-06-30</TxnDate>
            <PrivateNote>Acct. 1JK90</PrivateNote>
            <Line>
                <Amount>110.00</Amount>
                <LinkedTxn>
                    <TxnId>108</TxnId>
                    <TxnType>Bill</TxnType>
                </LinkedTxn>
            </Line>
            <VendorRef name="Robertson &amp; Associates">49</VendorRef>
            <PayType>Check</PayType>
            <CheckPayment>
                <BankAccountRef name="Checking">35</BankAccountRef>
                <PrintStatus>NeedToPrint</PrintStatus>
            </CheckPayment>
            <TotalAmt>110.00</TotalAmt>
        </BillPayment>
        <BillPayment domain="QBO" sparse="false">
            <Id>22</Id>
            <SyncToken>2</SyncToken>
            <MetaData>
                <CreateTime>2014-09-16T15:28:48-07:00</CreateTime>
                <LastUpdatedTime>2015-06-30T15:24:40-07:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>1</DocNumber>
            <TxnDate>2014-09-16</TxnDate>
            <PrivateNote>Add private note</PrivateNote>
            <Line>
                <Amount>2000.00</Amount>
                <LinkedTxn>
                    <TxnId>1</TxnId>
                    <TxnType>Bill</TxnType>
                </LinkedTxn>
            </Line>
            <VendorRef name="Brosnahan Insurance Agency">31</VendorRef>
            <PayType>Check</PayType>
            <CheckPayment>
                <BankAccountRef name="Checking">35</BankAccountRef>
                <PrintStatus>NotSet</PrintStatus>
            </CheckPayment>
            <TotalAmt>2000.00</TotalAmt>
        </BillPayment>
        <BillPayment domain="QBO" sparse="false">
            <Id>236</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-07-14T12:34:04-07:00</CreateTime>
                <LastUpdatedTime>2015-07-14T12:34:04-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2015-07-14</TxnDate>
            <PrivateNote>Acct. 1JK90</PrivateNote>
            <Line>
                <Amount>200.00</Amount>
                <LinkedTxn>
                    <TxnId>234</TxnId>
                    <TxnType>Bill</TxnType>
                </LinkedTxn>
            </Line>
            <VendorRef name="Bob's Burger Joint">56</VendorRef>
            <PayType>Check</PayType>
            <CheckPayment>
                <BankAccountRef name="Checking">35</BankAccountRef>
                <PrintStatus>NeedToPrint</PrintStatus>
            </CheckPayment>
            <TotalAmt>200.00</TotalAmt>
        </BillPayment>
        <BillPayment domain="QBO" sparse="false">
            <Id>237</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-07-14T12:37:57-07:00</CreateTime>
                <LastUpdatedTime>2015-07-14T12:37:57-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2015-07-14</TxnDate>
            <VendorRef name="Bob's Burger Joint">56</VendorRef>
            <PayType>Check</PayType>
            <CheckPayment>
                <BankAccountRef name="Checking">35</BankAccountRef>
                <PrintStatus>NotSet</PrintStatus>
            </CheckPayment>
            <TotalAmt>110.00</TotalAmt>
        </BillPayment>
    </QueryResponse>
</IntuitResponse>
```

## Read a billpayment

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/billpayment/<billpaymentId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a billpayment that has been previously created.

### Returns

The billpayment response body.

#### Example

```json
{
  "BillPayment": {
    "SyncToken": "0",
    "domain": "QBO",
    "VendorRef": {
      "name": "Bob's Burger Joint",
      "value": "56"
    },
    "TxnDate": "2015-07-14",
    "TotalAmt": 200.0,
    "PayType": "Check",
    "PrivateNote": "Acct. 1JK90",
    "sparse": false,
    "Line": [
      {
        "Amount": 200.0,
        "LinkedTxn": [
          {
            "TxnId": "234",
            "TxnType": "Bill"
          }
        ]
      }
    ],
    "Id": "236",
    "CheckPayment": {
      "PrintStatus": "NeedToPrint",
      "BankAccountRef": {
        "name": "Checking",
        "value": "35"
      }
    },
    "MetaData": {
      "CreateTime": "2015-07-14T12:34:04-07:00",
      "LastUpdatedTime": "2015-07-14T12:34:04-07:00"
    }
  },
  "time": "2015-07-14T12:39:40.606-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-14T12:50:08.532-07:00">
    <BillPayment domain="QBO" sparse="false">
        <Id>236</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-14T12:34:04-07:00</CreateTime>
            <LastUpdatedTime>2015-07-14T12:34:04-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-07-14</TxnDate>
        <PrivateNote>Acct. 1JK90</PrivateNote>
        <Line>
            <Amount>200.00</Amount>
            <LinkedTxn>
                <TxnId>234</TxnId>
                <TxnType>Bill</TxnType>
            </LinkedTxn>
        </Line>
        <VendorRef name="Bob's Burger Joint">56</VendorRef>
        <PayType>Check</PayType>
        <CheckPayment>
            <BankAccountRef name="Checking">35</BankAccountRef>
            <PrintStatus>NeedToPrint</PrintStatus>
        </CheckPayment>
        <TotalAmt>200.00</TotalAmt>
    </BillPayment>
</IntuitResponse>
```

## Full update a billpayment

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/billpayment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing billpayment object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `billpaymentresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "2",
  "domain": "QBO",
  "VendorRef": {
    "name": "Bob's Burger Joint",
    "value": "56"
  },
  "TxnDate": "2015-07-14",
  "TotalAmt": 200.0,
  "PayType": "Check",
  "PrivateNote": "A new private note",
  "sparse": false,
  "Line": [
    {
      "Amount": 200.0,
      "LinkedTxn": [
        {
          "TxnId": "234",
          "TxnType": "Bill"
        }
      ]
    }
  ],
  "Id": "236",
  "CheckPayment": {
    "PrintStatus": "NeedToPrint",
    "BankAccountRef": {
      "name": "Checking",
      "value": "35"
    }
  },
  "MetaData": {
    "CreateTime": "2015-07-14T12:34:04-07:00",
    "LastUpdatedTime": "2015-07-14T13:17:22-07:00"
  }
}
```

#### XML example

```xml
<BillPayment xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>236</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
        <CreateTime>2015-07-14T12:34:04-07:00</CreateTime>
        <LastUpdatedTime>2015-07-14T12:34:04-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-07-14</TxnDate>
    <PrivateNote>An updated private note</PrivateNote>
    <Line>
        <Amount>200.00</Amount>
        <LinkedTxn>
            <TxnId>234</TxnId>
            <TxnType>Bill</TxnType>
        </LinkedTxn>
    </Line>
    <VendorRef name="Bob's Burger Joint">56</VendorRef>
    <PayType>Check</PayType>
    <CheckPayment>
        <BankAccountRef name="Checking">35</BankAccountRef>
        <PrintStatus>NeedToPrint</PrintStatus>
    </CheckPayment>
    <TotalAmt>200.00</TotalAmt>
</BillPayment>
```

### Returns

The billpayment response body.

#### Example

```json
{
  "BillPayment": {
    "SyncToken": "3",
    "domain": "QBO",
    "VendorRef": {
      "name": "Bob's Burger Joint",
      "value": "56"
    },
    "TxnDate": "2015-07-14",
    "TotalAmt": 200.0,
    "PayType": "Check",
    "PrivateNote": "A new private note",
    "sparse": false,
    "Line": [
      {
        "Amount": 200.0,
        "LinkedTxn": [
          {
            "TxnId": "234",
            "TxnType": "Bill"
          }
        ]
      }
    ],
    "Id": "236",
    "CheckPayment": {
      "PrintStatus": "NeedToPrint",
      "BankAccountRef": {
        "name": "Checking",
        "value": "35"
      }
    },
    "MetaData": {
      "CreateTime": "2015-07-14T12:34:04-07:00",
      "LastUpdatedTime": "2015-07-30T09:55:19-07:00"
    }
  },
  "time": "2015-07-30T09:55:20.597-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-14T13:13:32.285-07:00">
    <BillPayment domain="QBO" sparse="false">
        <Id>236</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2015-07-14T12:34:04-07:00</CreateTime>
            <LastUpdatedTime>2015-07-14T13:17:22-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-07-14</TxnDate>
        <PrivateNote>An updated private note</PrivateNote>
        <Line>
            <Amount>200.00</Amount>
            <LinkedTxn>
                <TxnId>234</TxnId>
                <TxnType>Bill</TxnType>
            </LinkedTxn>
        </Line>
        <VendorRef name="Bob's Burger Joint">56</VendorRef>
        <PayType>Check</PayType>
        <CheckPayment>
            <BankAccountRef name="Checking">35</BankAccountRef>
            <PrintStatus>NeedToPrint</PrintStatus>
        </CheckPayment>
        <TotalAmt>200.00</TotalAmt>
    </BillPayment>
</IntuitResponse>
```
