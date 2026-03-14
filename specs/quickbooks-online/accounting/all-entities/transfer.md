# Transfer

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/transfer
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Transfer
> Canonical entity: `Transfer`

A Transfer represents a transaction where funds are moved between two accounts from the company's QuickBooks chart of accounts.

### Business Rules

A transfer must have `FromAccountRef`, `ToAccountRef`, and `Amount` attributes.

## The transfer object

### transferresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `ToAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the asset account to which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `ToAccountRef.value` and `ToAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

<details>
<summary>Child attributes for `ToAccountRef`</summary>

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

#### `FromAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the asset account from which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `FromAccountRef.value` and `FromAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

<details>
<summary>Child attributes for `FromAccountRef`</summary>

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

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `Transfer` was created from.

<details>
<summary>Child attributes for `RecurDataRef`</summary>

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

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Memo field on the Invoice form.

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
  "Transfer": {
    "SyncToken": "0",
    "domain": "QBO",
    "TxnDate": "2015-02-06",
    "ToAccountRef": {
      "name": "Savings",
      "value": "36"
    },
    "Amount": 120.0,
    "sparse": false,
    "Id": "170",
    "FromAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "MetaData": {
      "CreateTime": "2015-02-06T11:06:12-08:00",
      "LastUpdatedTime": "2015-02-06T11:06:12-08:00"
    }
  },
  "time": "2015-02-06T11:06:12.017-08:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-06T13:25:03.406-08:00">
    <Transfer domain="QBO" sparse="false">
        <Id>169</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-02-06T11:04:28-08:00</CreateTime>
            <LastUpdatedTime>2015-02-06T11:04:28-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-02-06</TxnDate>
        <FromAccountRef name="Checking">35</FromAccountRef>
        <ToAccountRef name="Savings">36</ToAccountRef>
        <Amount>120.00</Amount>
    </Transfer>
</IntuitResponse>
```

## Create an transfer

### Definition

- **Content type:** `application/json, application/xml`
- **Operation:** `POST /v3/company/<realmID>/transfer`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create a Transfer object are listed here.

Schema: `transferrequest`

<details>
<summary>Show schema for `transferrequest`</summary>

#### transferrequest

Model type: `object`

##### `Amount`

Required: Required
Type: `Decimal`

Indicates the total amount of the transaction.

##### `ToAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the asset account to which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `ToAccountRef.value` and `ToAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

<details>
<summary>Child attributes for `ToAccountRef`</summary>

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

##### `FromAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the asset account from which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `FromAccountRef.value` and `FromAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

<details>
<summary>Child attributes for `FromAccountRef`</summary>

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

#### Example

```json
{
  "Amount": "120.00",
  "ToAccountRef": {
    "name": "Savings",
    "value": "36"
  },
  "FromAccountRef": {
    "name": "Checking",
    "value": "35"
  }
}
```

#### XML example

```xml
<Transfer xmlns="http://schema.intuit.com/finance/v3" sparse="false" domain="QBO">
    <FromAccountRef name="Checking">35</FromAccountRef>
    <ToAccountRef name="Savings">36</ToAccountRef>
    <Amount>320.00</Amount>
</Transfer>
```

### Returns

The transfer response body.

#### Example

```json
{
  "Transfer": {
    "SyncToken": "0",
    "domain": "QBO",
    "TxnDate": "2015-02-06",
    "ToAccountRef": {
      "name": "Savings",
      "value": "36"
    },
    "Amount": 120.0,
    "sparse": false,
    "Id": "170",
    "FromAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "MetaData": {
      "CreateTime": "2015-02-06T11:06:12-08:00",
      "LastUpdatedTime": "2015-02-06T11:06:12-08:00"
    }
  },
  "time": "2015-02-06T11:06:12.017-08:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-06T13:30:39.230-08:00">
    <Transfer domain="QBO" sparse="false">
        <Id>171</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-02-06T13:30:39-08:00</CreateTime>
            <LastUpdatedTime>2015-02-06T13:30:39-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-02-06</TxnDate>
        <FromAccountRef name="Checking">35</FromAccountRef>
        <ToAccountRef name="Savings">36</ToAccountRef>
        <Amount>320.00</Amount>
    </Transfer>
</IntuitResponse>
```

## Delete an transfer

### Definition

- **Content type:** `application/json, application/xml`
- **Operation:** `POST /v3/company/<realmID>/transfer?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the Transfer object specified in the request body. The request body must include the full payload of the transfer as returned in a read response.

### Request Body

Schema: `transferresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "2",
  "domain": "QBO",
  "TxnDate": "2015-02-06",
  "ToAccountRef": {
    "name": "Savings",
    "value": "36"
  },
  "Amount": 6600.0,
  "sparse": false,
  "Id": "170",
  "FromAccountRef": {
    "name": "Checking",
    "value": "35"
  }
}
```

#### XML example

```xml
<Transfer xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>169</Id>
    <SyncToken>2</SyncToken>
    <TxnDate>2015-02-06</TxnDate>
    <FromAccountRef name="Checking">35</FromAccountRef>
    <ToAccountRef name="Savings">36</ToAccountRef>
    <Amount>880.00</Amount>
</Transfer>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "Transfer": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "170"
  },
  "time": "2015-02-06T11:22:26.347-08:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-06T13:41:29.233-08:00">
    <Transfer domain="QBO" status="Deleted">
        <Id>169</Id>
    </Transfer>
</IntuitResponse>
```

## Query an transfer

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Transfer"
```

#### XML example

```sql
select * from Transfer where id = '171'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Transfer": [
      {
        "SyncToken": "2",
        "domain": "QBO",
        "TxnDate": "2015-02-06",
        "ToAccountRef": {
          "name": "Savings",
          "value": "36"
        },
        "Amount": 660.0,
        "sparse": false,
        "Id": "170",
        "FromAccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "MetaData": {
          "CreateTime": "2015-02-06T11:06:12-08:00",
          "LastUpdatedTime": "2015-02-06T11:16:06-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "TxnDate": "2015-02-06",
        "ToAccountRef": {
          "name": "Savings",
          "value": "36"
        },
        "Amount": 120.0,
        "sparse": false,
        "Id": "169",
        "FromAccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "MetaData": {
          "CreateTime": "2015-02-06T11:04:28-08:00",
          "LastUpdatedTime": "2015-02-06T11:04:28-08:00"
        }
      }
    ],
    "maxResults": 2,
    "totalCount": 2
  },
  "time": "2015-02-06T11:17:10.153-08:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-06T13:31:47.938-08:00">
    <QueryResponse startPosition="1" maxResults="1" totalCount="1">
        <Transfer domain="QBO" sparse="false">
            <Id>171</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-02-06T13:30:39-08:00</CreateTime>
                <LastUpdatedTime>2015-02-06T13:30:39-08:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2015-02-06</TxnDate>
            <FromAccountRef name="Checking">35</FromAccountRef>
            <ToAccountRef name="Savings">36</ToAccountRef>
            <Amount>320.00</Amount>
        </Transfer>
    </QueryResponse>
</IntuitResponse>
```

## Read an transfer

### Definition

- **Operation:** `GET /v3/company/<realmID>/transfer/<transferId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Transfer object that has been previously created.

### Returns

The transfer response body.

#### Example

```json
{
  "Transfer": {
    "SyncToken": "0",
    "domain": "QBO",
    "TxnDate": "2015-02-06",
    "ToAccountRef": {
      "name": "Savings",
      "value": "36"
    },
    "Amount": 120.0,
    "sparse": false,
    "Id": "170",
    "FromAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "MetaData": {
      "CreateTime": "2015-02-06T11:06:12-08:00",
      "LastUpdatedTime": "2015-02-06T11:06:12-08:00"
    }
  },
  "time": "2015-02-06T11:06:12.017-08:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-06T13:25:03.406-08:00">
    <Transfer domain="QBO" sparse="false">
        <Id>169</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-02-06T11:04:28-08:00</CreateTime>
            <LastUpdatedTime>2015-02-06T11:04:28-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-02-06</TxnDate>
        <FromAccountRef name="Checking">35</FromAccountRef>
        <ToAccountRef name="Savings">36</ToAccountRef>
        <Amount>120.00</Amount>
    </Transfer>
</IntuitResponse>
```

## Sparse update an transfer

### Definition

- **Content type:** `application/json, application/xml`
- **Operation:** `POST /v3/company/<realmID>/transfer`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Sparse updating provides the ability to update a subset of properties for a given object; only elements specified in the request are updated. Missing elements are left untouched. The ID of the object to update is specified in the request body.​

### Request Body

Schema: `transferrequest`

<details>
<summary>Show schema for `transferrequest`</summary>

#### transferrequest

Model type: `object`

##### `Amount`

Required: Required
Type: `Decimal`

Indicates the total amount of the transaction.

##### `ToAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the asset account to which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `ToAccountRef.value` and `ToAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

<details>
<summary>Child attributes for `ToAccountRef`</summary>

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

##### `FromAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the asset account from which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `FromAccountRef.value` and `FromAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

<details>
<summary>Child attributes for `FromAccountRef`</summary>

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

#### Example

```json
{
  "SyncToken": "1",
  "domain": "QBO",
  "ToAccountRef": {
    "name": "Savings",
    "value": "36"
  },
  "Amount": 660.0,
  "sparse": true,
  "Id": "170",
  "FromAccountRef": {
    "name": "Checking",
    "value": "35"
  }
}
```

#### XML example

```xml
<Transfer xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>169</Id>
    <SyncToken>1</SyncToken>
    <FromAccountRef name="Checking">35</FromAccountRef>
    <ToAccountRef name="Savings">36</ToAccountRef>
    <Amount>880.00</Amount>
</Transfer>
```

### Returns

The transfer response body.

#### Example

```json
{
  "Transfer": {
    "SyncToken": "2",
    "domain": "QBO",
    "TxnDate": "2015-02-06",
    "ToAccountRef": {
      "name": "Savings",
      "value": "36"
    },
    "Amount": 660.0,
    "sparse": false,
    "Id": "170",
    "FromAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "MetaData": {
      "CreateTime": "2015-02-06T11:06:12-08:00",
      "LastUpdatedTime": "2015-02-06T11:16:06-08:00"
    }
  },
  "time": "2015-02-06T11:16:06.672-08:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-06T13:38:32.271-08:00">
    <Transfer domain="QBO" sparse="false">
        <Id>169</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2015-02-06T11:04:28-08:00</CreateTime>
            <LastUpdatedTime>2015-02-06T13:38:32-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-02-06</TxnDate>
        <FromAccountRef name="Checking">35</FromAccountRef>
        <ToAccountRef name="Savings">36</ToAccountRef>
        <Amount>880.00</Amount>
    </Transfer>
</IntuitResponse>
```

## Full update an transfer

### Definition

- **Content type:** `application/json, application/xml`
- **Operation:** `POST /v3/company/<realmID>/transfer`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing Transfer object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `transferrequest`

<details>
<summary>Show schema for `transferrequest`</summary>

#### transferrequest

Model type: `object`

##### `Amount`

Required: Required
Type: `Decimal`

Indicates the total amount of the transaction.

##### `ToAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the asset account to which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `ToAccountRef.value` and `ToAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

<details>
<summary>Child attributes for `ToAccountRef`</summary>

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

##### `FromAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the asset account from which funds are transfered. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `FromAccountRef.value` and `FromAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

<details>
<summary>Child attributes for `FromAccountRef`</summary>

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

#### Example

```json
{
  "SyncToken": "0",
  "domain": "QBO",
  "TxnDate": "2015-02-06",
  "ToAccountRef": {
    "name": "Savings",
    "value": "36"
  },
  "Amount": 550.0,
  "sparse": false,
  "Id": "170",
  "FromAccountRef": {
    "name": "Checking",
    "value": "35"
  },
  "MetaData": {
    "CreateTime": "2015-02-06T11:06:12-08:00",
    "LastUpdatedTime": "2015-02-06T11:06:12-08:00"
  }
}
```

#### XML example

```xml
<Transfer xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>169</Id>
    <SyncToken>0</SyncToken>
    <TxnDate>2015-02-06</TxnDate>
    <FromAccountRef name="Checking">35</FromAccountRef>
    <ToAccountRef name="Savings">36</ToAccountRef>
    <Amount>770.00</Amount>
</Transfer>
```

### Returns

The transfer response body.

#### Example

```json
{
  "Transfer": {
    "SyncToken": "1",
    "domain": "QBO",
    "TxnDate": "2015-02-06",
    "ToAccountRef": {
      "name": "Savings",
      "value": "36"
    },
    "Amount": 550.0,
    "sparse": false,
    "Id": "170",
    "FromAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "MetaData": {
      "CreateTime": "2015-02-06T11:06:12-08:00",
      "LastUpdatedTime": "2015-02-06T11:11:36-08:00"
    }
  },
  "time": "2015-02-06T11:11:36.026-08:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-06T13:37:04.807-08:00">
    <Transfer domain="QBO" sparse="false">
        <Id>169</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2015-02-06T11:04:28-08:00</CreateTime>
            <LastUpdatedTime>2015-02-06T13:37:04-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-02-06</TxnDate>
        <FromAccountRef name="Checking">35</FromAccountRef>
        <ToAccountRef name="Savings">36</ToAccountRef>
        <Amount>770.00</Amount>
    </Transfer>
</IntuitResponse>
```
