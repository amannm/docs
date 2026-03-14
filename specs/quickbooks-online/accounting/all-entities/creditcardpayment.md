# CreditCardPayment

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/creditcardpayment
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / CreditCardPayment
> Canonical entity: `CreditCardPayment`

Represents a financial transaction to record a Credit Card balance payment in QuickBooks Online. It provides an easy way for users to move money from a Bank account to a Credit Card account. It is essentially a more limited Transfer form.

### Business Rules

This transaction does not support multi-currency. Only payments made from home currency Bank accounts to home currency Credit Card accounts will be accepted.

## The creditcardpayment object

### creditcardpaymentresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `CreditCardAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the credit card account to which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference.

<details>
<summary>Child attributes for `CreditCardAccountRef`</summary>

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

#### `Amount`

Required: Required
Type: `Decimal`

Indicates the total amount of the transaction.

#### `BankAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the bank account from which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference.

<details>
<summary>Child attributes for `BankAccountRef`</summary>

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

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: Max of 4000 chars

User entered, organization-private note about the transaction. This field maps to the Memo field on the Pay down credit card form.

#### `VendorRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable
Minor version: 54

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

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: Current server date

The date entered by the user when this transaction occurred. For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used. Sort order is ASC by default.

<details>
<summary>Child attributes for `TxnDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `Memo`

Required: Optional
Type: `String`
Max length: Max of 4000 chars
Minor version: 54

User entered, organization-private note about the transaction. This field maps to the Memo field on the Pay down credit card form.

#### `PrintStatus`

Required: Optional
Type: `String`
Default: <span class="literal">NotSet</span>
Minor version: 54

Printing status of the credit-card-payment. Valid values: `NotSet`, `NeedToPrint`, `PrintComplete`.

#### `CheckNum`

Required: Optional
Type: `String`
Minor version: 54

User entered, Check number. This field maps to the Check no. field on the Pay down credit card form.

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
  "CreditCardPaymentTxn": {
    "SyncToken": "0",
    "domain": "QBO",
    "CreditCardAccountRef": {
      "name": "Credit Card",
      "value": "57"
    },
    "TxnDate": "2020-03-27",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "Amount": 10.0,
    "sparse": false,
    "BankAccountRef": {
      "name": "Checking",
      "value": "37"
    },
    "Id": "29",
    "MetaData": {
      "CreateTime": "2020-03-27T07:01:04-07:00",
      "LastUpdatedTime": "2020-03-27T07:01:04-07:00"
    }
  },
  "time": "2020-03-27T07:06:45.630-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-03-27T08:22:33.079-07:00">
    <CreditCardPaymentTxn domain="QBO" sparse="false">
        <Id>29</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2020-03-27T07:01:04-07:00</CreateTime>
            <LastUpdatedTime>2020-03-27T07:59:42-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2020-03-27</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <PrivateNote>This is a corrected memo field.</PrivateNote>
        <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
        <BankAccountRef name="Checking">37</BankAccountRef>
        <Amount>100.00</Amount>
    </CreditCardPaymentTxn>
</IntuitResponse>
```

## Create a creditcardpayment

### Definition

- **Content type:** `application/json, application/xml`
- **Operation:** `POST /v3/company/<realmID>/creditcardpayment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create a CreditCardPayment object are listed here.

Schema: `creditcardpaymentrequest`

<details>
<summary>Show schema for `creditcardpaymentrequest`</summary>

#### creditcardpaymentrequest

Model type: `object`

##### `TxnDate`

Required: Required
Type: `Date`

Date of transaction.

##### `Amount`

Required: Required
Type: `Decimal`

Total amount of the payment. Denominated in the currency of the credit card account.

##### `BankAccountRef`

Required: Required
Type: `ReferenceType`

Bank account used to pay the Credit Card balance. Must be a Bank account.

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

##### `CreditCardAccountRef`

Required: Required
Type: `ReferenceType`

Credit Card account for which a payment is being entered. Must be a Credit Card account.

<details>
<summary>Child attributes for `CreditCardAccountRef`</summary>

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

##### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This field maps to the Memo field on the Pay down credit card form.

</details>

#### Example

```json
{
  "PrivateNote": "This will fill in the memo field.",
  "TxnDate": "2020-03-27",
  "Amount": "100",
  "BankAccountRef": {
    "name": "Checking",
    "value": 37
  },
  "CreditCardAccountRef": {
    "name": "Credit Card",
    "value": 57
  }
}
```

#### XML example

```xml
<CreditCardPaymentTxn xmlns="http://schema.intuit.com/finance/v3" sparse="false" domain="QBO">
    <BankAccountRef name="Checking">37</BankAccountRef>
    <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
    <Amount>320.00</Amount>
	<PrivateNote>This is a memo</PrivateNote>
</CreditCardPaymentTxn>
```

### Returns

The creditcardpayment response body.

#### Example

```json
{
  "CreditCardPaymentTxn": {
    "SyncToken": "0",
    "domain": "QBO",
    "CreditCardAccountRef": {
      "name": "Credit Card",
      "value": "57"
    },
    "TxnDate": "2020-03-27",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "PrivateNote": "This will fill in the memo field.",
    "Amount": 100.0,
    "sparse": false,
    "BankAccountRef": {
      "name": "Checking",
      "value": "37"
    },
    "Id": "31",
    "MetaData": {
      "CreateTime": "2020-03-27T07:18:05-07:00",
      "LastUpdatedTime": "2020-03-27T07:18:05-07:00"
    }
  },
  "time": "2020-03-27T07:18:05.713-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-03-27T08:16:45.852-07:00">
    <CreditCardPaymentTxn domain="QBO" sparse="false">
        <Id>32</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2020-03-27T08:16:45-07:00</CreateTime>
            <LastUpdatedTime>2020-03-27T08:16:45-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2020-03-27</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <PrivateNote>This is a memo</PrivateNote>
        <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
        <BankAccountRef name="Checking">37</BankAccountRef>
        <Amount>320.00</Amount>
    </CreditCardPaymentTxn>
</IntuitResponse>
```

## Delete a creditcardpayment

### Definition

- **Content type:** `application/json, application/xml`
- **Operation:** `POST /v3/company/<realmID>/creditcardpayment?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the CreditCardPayment object specified in the request body. The request body must include the full payload of the CreditCardPayment as returned in a read response.

### Request Body

Schema: `creditcardpaymentresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "TxnDate": "2020-03-27",
  "PrivateNote": "This will fill in the memo field.",
  "CreditCardAccountRef": {
    "name": "Credit Card",
    "value": 57
  },
  "SyncToken": "0",
  "Amount": "100",
  "BankAccountRef": {
    "name": "Checking",
    "value": 37
  },
  "Id": "31"
}
```

#### XML example

```xml
<CreditCardPaymentTxn xmlns="http://schema.intuit.com/finance/v3" sparse="false" domain="QBO">
    <Id>32</Id>
    <SyncToken>0</SyncToken>
    <BankAccountRef name="Checking">37</BankAccountRef>
    <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
    <Amount>320.00</Amount>
	<PrivateNote>This is a memo</PrivateNote>
</CreditCardPaymentTxn>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "CreditCardPaymentTxn": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "31"
  },
  "time": "2020-03-27T07:38:07.499-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-03-27T08:20:02.532-07:00">
    <CreditCardPaymentTxn domain="QBO" status="Deleted">
        <Id>32</Id>
    </CreditCardPaymentTxn>
</IntuitResponse>
```

## Query a creditcardpayment

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from creditcardpayment\n"
```

#### XML example

```sql
select * from creditcardpayment
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 2,
    "CreditCardPaymentTxn": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "CreditCardAccountRef": {
          "name": "Credit Card",
          "value": "57"
        },
        "TxnDate": "2020-03-27",
        "CurrencyRef": {
          "name": "United States Dollar",
          "value": "USD"
        },
        "PrivateNote": "This is a memo",
        "Amount": 15.0,
        "sparse": false,
        "BankAccountRef": {
          "name": "Checking",
          "value": "37"
        },
        "Id": "30",
        "MetaData": {
          "CreateTime": "2020-03-27T07:15:05-07:00",
          "LastUpdatedTime": "2020-03-27T07:15:05-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "CreditCardAccountRef": {
          "name": "Credit Card",
          "value": "57"
        },
        "TxnDate": "2020-03-27",
        "CurrencyRef": {
          "name": "United States Dollar",
          "value": "USD"
        },
        "Amount": 10.0,
        "sparse": false,
        "BankAccountRef": {
          "name": "Checking",
          "value": "37"
        },
        "Id": "29",
        "MetaData": {
          "CreateTime": "2020-03-27T07:01:04-07:00",
          "LastUpdatedTime": "2020-03-27T07:01:04-07:00"
        }
      }
    ],
    "maxResults": 2
  },
  "time": "2020-03-27T07:15:46.750-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-03-27T08:21:25.537-07:00">
    <QueryResponse startPosition="1" maxResults="2" totalCount="2">
        <CreditCardPaymentTxn domain="QBO" sparse="false">
            <Id>29</Id>
            <SyncToken>2</SyncToken>
            <MetaData>
                <CreateTime>2020-03-27T07:01:04-07:00</CreateTime>
                <LastUpdatedTime>2020-03-27T07:59:42-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2020-03-27</TxnDate>
            <CurrencyRef name="United States Dollar">USD</CurrencyRef>
            <PrivateNote>This is a corrected memo field.</PrivateNote>
            <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
            <BankAccountRef name="Checking">37</BankAccountRef>
            <Amount>100.00</Amount>
        </CreditCardPaymentTxn>
        <CreditCardPaymentTxn domain="QBO" sparse="false">
            <Id>30</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2020-03-27T07:15:05-07:00</CreateTime>
                <LastUpdatedTime>2020-03-27T07:15:05-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2020-03-27</TxnDate>
            <CurrencyRef name="United States Dollar">USD</CurrencyRef>
            <PrivateNote>This is a memo</PrivateNote>
            <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
            <BankAccountRef name="Checking">37</BankAccountRef>
            <Amount>15.00</Amount>
        </CreditCardPaymentTxn>
    </QueryResponse>
</IntuitResponse>
```

## Read a creditcardpayment

### Definition

- **Operation:** `GET /v3/company/<realmID>/creditcardpayment/<creditcardpaymentId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a CreditCardPayment object that has been previously created.

### Returns

The creditcardpayment response body.

#### Example

```json
{
  "CreditCardPaymentTxn": {
    "SyncToken": "0",
    "domain": "QBO",
    "CreditCardAccountRef": {
      "name": "Credit Card",
      "value": "57"
    },
    "TxnDate": "2020-03-27",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "Amount": 10.0,
    "sparse": false,
    "BankAccountRef": {
      "name": "Checking",
      "value": "37"
    },
    "Id": "29",
    "MetaData": {
      "CreateTime": "2020-03-27T07:01:04-07:00",
      "LastUpdatedTime": "2020-03-27T07:01:04-07:00"
    }
  },
  "time": "2020-03-27T07:06:45.630-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-03-27T08:22:33.079-07:00">
    <CreditCardPaymentTxn domain="QBO" sparse="false">
        <Id>29</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2020-03-27T07:01:04-07:00</CreateTime>
            <LastUpdatedTime>2020-03-27T07:59:42-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2020-03-27</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <PrivateNote>This is a corrected memo field.</PrivateNote>
        <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
        <BankAccountRef name="Checking">37</BankAccountRef>
        <Amount>100.00</Amount>
    </CreditCardPaymentTxn>
</IntuitResponse>
```

## Full update a creditcardpayment

### Definition

- **Content type:** `application/json, application/xml`
- **Operation:** `POST /v3/company/<realmID>/creditcardpayment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing CreditCardPayment object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `creditcardpaymentrequest`

<details>
<summary>Show schema for `creditcardpaymentrequest`</summary>

#### creditcardpaymentrequest

Model type: `object`

##### `TxnDate`

Required: Required
Type: `Date`

Date of transaction.

##### `Amount`

Required: Required
Type: `Decimal`

Total amount of the payment. Denominated in the currency of the credit card account.

##### `BankAccountRef`

Required: Required
Type: `ReferenceType`

Bank account used to pay the Credit Card balance. Must be a Bank account.

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

##### `CreditCardAccountRef`

Required: Required
Type: `ReferenceType`

Credit Card account for which a payment is being entered. Must be a Credit Card account.

<details>
<summary>Child attributes for `CreditCardAccountRef`</summary>

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

##### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This field maps to the Memo field on the Pay down credit card form.

</details>

#### Example

```json
{
  "TxnDate": "2020-03-27",
  "PrivateNote": "This will fill in the memo field.",
  "CreditCardAccountRef": {
    "name": "Credit Card",
    "value": 57
  },
  "SyncToken": "0",
  "Amount": "100",
  "BankAccountRef": {
    "name": "Checking",
    "value": 37
  },
  "Id": "29"
}
```

#### XML example

```xml
<CreditCardPaymentTxn xmlns="http://schema.intuit.com/finance/v3" sparse="false" domain="QBO">
    <Id>29</Id>
    <SyncToken>2</SyncToken>
    <BankAccountRef name="Checking">37</BankAccountRef>
    <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
    <Amount>320.00</Amount>
	<PrivateNote>This is a corrected memo field.</PrivateNote>
</CreditCardPaymentTxn>
```

### Returns

The creditcardpayment response body.

#### Example

```json
{
  "CreditCardPaymentTxn": {
    "SyncToken": "1",
    "domain": "QBO",
    "CreditCardAccountRef": {
      "name": "Credit Card",
      "value": "57"
    },
    "TxnDate": "2020-03-27",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "PrivateNote": "This will fill in the memo field.",
    "Amount": 100.0,
    "sparse": false,
    "BankAccountRef": {
      "name": "Checking",
      "value": "37"
    },
    "Id": "29",
    "MetaData": {
      "CreateTime": "2020-03-27T07:01:04-07:00",
      "LastUpdatedTime": "2020-03-27T07:31:22-07:00"
    }
  },
  "time": "2020-03-27T07:31:22.379-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-03-27T08:25:31.669-07:00">
    <CreditCardPaymentTxn domain="QBO" sparse="false">
        <Id>29</Id>
        <SyncToken>3</SyncToken>
        <MetaData>
            <CreateTime>2020-03-27T07:01:04-07:00</CreateTime>
            <LastUpdatedTime>2020-03-27T08:25:31-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2020-03-27</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <PrivateNote>This is a corrected memo field.</PrivateNote>
        <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
        <BankAccountRef name="Checking">37</BankAccountRef>
        <Amount>320.00</Amount>
    </CreditCardPaymentTxn>
</IntuitResponse>
```

## Sparse update a creditcardpayment

### Definition

- **Content type:** `application/json, application/xml`
- **Operation:** `POST /v3/company/<realmID>/creditcardpayment`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Sparse updating provides the ability to update a subset of properties for a given object; only elements specified in the request are updated. Missing elements are left untouched. The ID of the object to update is specified in the request body.​

### Request Body

Schema: `creditcardpaymentrequest`

<details>
<summary>Show schema for `creditcardpaymentrequest`</summary>

#### creditcardpaymentrequest

Model type: `object`

##### `TxnDate`

Required: Required
Type: `Date`

Date of transaction.

##### `Amount`

Required: Required
Type: `Decimal`

Total amount of the payment. Denominated in the currency of the credit card account.

##### `BankAccountRef`

Required: Required
Type: `ReferenceType`

Bank account used to pay the Credit Card balance. Must be a Bank account.

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

##### `CreditCardAccountRef`

Required: Required
Type: `ReferenceType`

Credit Card account for which a payment is being entered. Must be a Credit Card account.

<details>
<summary>Child attributes for `CreditCardAccountRef`</summary>

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

##### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This field maps to the Memo field on the Pay down credit card form.

</details>

#### Example

```json
{
  "TxnDate": "2020-03-27",
  "PrivateNote": "This is a corrected memo field.",
  "CreditCardAccountRef": {
    "name": "Credit Card",
    "value": 57
  },
  "SyncToken": "1",
  "Amount": "100",
  "sparse": true,
  "BankAccountRef": {
    "name": "Checking",
    "value": 37
  },
  "Id": "29"
}
```

#### XML example

```xml
<CreditCardPaymentTxn xmlns="http://schema.intuit.com/finance/v3" sparse="true" domain="QBO">
    <Id>29</Id>
    <SyncToken>3</SyncToken>
    <BankAccountRef name="Checking">37</BankAccountRef>
    <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
    <Amount>150.00</Amount>
	<PrivateNote>This is a corrected memo field.</PrivateNote>
</CreditCardPaymentTxn>
```

### Returns

The creditcardpayment response body.

#### Example

```json
{
  "CreditCardPaymentTxn": {
    "SyncToken": "2",
    "domain": "QBO",
    "CreditCardAccountRef": {
      "name": "Credit Card",
      "value": "57"
    },
    "TxnDate": "2020-03-27",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "PrivateNote": "This is a corrected memo field.",
    "Amount": 100.0,
    "sparse": false,
    "BankAccountRef": {
      "name": "Checking",
      "value": "37"
    },
    "Id": "29",
    "MetaData": {
      "CreateTime": "2020-03-27T07:01:04-07:00",
      "LastUpdatedTime": "2020-03-27T07:59:42-07:00"
    }
  },
  "time": "2020-03-27T07:59:42.418-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-03-27T08:27:05.916-07:00">
    <CreditCardPaymentTxn domain="QBO" sparse="false">
        <Id>29</Id>
        <SyncToken>4</SyncToken>
        <MetaData>
            <CreateTime>2020-03-27T07:01:04-07:00</CreateTime>
            <LastUpdatedTime>2020-03-27T08:27:05-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2020-03-27</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <PrivateNote>This is a corrected memo field.</PrivateNote>
        <CreditCardAccountRef name="Credit Card">57</CreditCardAccountRef>
        <BankAccountRef name="Checking">37</BankAccountRef>
        <Amount>150.00</Amount>
    </CreditCardPaymentTxn>
</IntuitResponse>
```
