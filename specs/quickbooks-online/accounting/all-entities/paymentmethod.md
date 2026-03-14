# PaymentMethod

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/paymentmethod
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / PaymentMethod
> Canonical entity: `PaymentMethod`

The PaymentMethod resource provides the method of payment for received goods. Delete is achieved by setting the `Active` attribute to `false` in an object update request; thus, making it inactive. In this type of delete, the record is not permanently deleted, but is hidden for display purposes. References to inactive objects are left intact.

## The paymentmethod object

### paymentmethodresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Name`

Required: Required
Type: `String`
Max length: Maximum of 31 chars

User recognizable name for the payment method.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable, sortable
Default: true

If true, this entity is currently enabled for use by QuickBooks.

#### `Type`

Required: Optional
Type: `String`

Defines the type of payment. Valid values include `CREDIT_CARD` or `NON_CREDIT_CARD`.

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
  "PaymentMethod": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "Diners Club",
    "sparse": false,
    "Active": true,
    "Type": "CREDIT_CARD",
    "Id": "7",
    "MetaData": {
      "CreateTime": "2014-09-11T14:42:05-07:00",
      "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
    }
  },
  "time": "2015-07-24T15:29:33.401-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T15:29:08.469-07:00">
  <PaymentMethod domain="QBO" sparse="false">
    <Id>7</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
      <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Diners Club</Name>
    <Active>true</Active>
    <Type>CREDIT_CARD</Type>
  </PaymentMethod>
</IntuitResponse>
```

## Create a paymentmethod

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/paymentmethod`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The elements to create a paymentmethod are listed here.

Schema: `paymentmethodrequest`

<details>
<summary>Show schema for `paymentmethodrequest`</summary>

#### paymentmethodrequest

Model type: `object`

##### `Name`

Required: Required
Type: `String`
Max length: Maximum of 31 chars

User recognizable name for the payment method.

</details>

#### Example

```json
{
  "Name": "Business Check"
}
```

#### XML example

```xml
<PaymentMethod xmlns="http://schema.intuit.com/finance/v3">
   <Name>Cashier's Check</Name>
</PaymentMethod>
```

### Returns

Returns the newly created paymentmethod object.

#### Example

```json
{
  "PaymentMethod": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "Business Check",
    "sparse": false,
    "Active": true,
    "Type": "NON_CREDIT_CARD",
    "Id": "10",
    "MetaData": {
      "CreateTime": "2015-07-24T15:37:44-07:00",
      "LastUpdatedTime": "2015-07-24T15:37:44-07:00"
    }
  },
  "time": "2015-07-24T15:37:44.79-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T15:38:39.094-07:00">
  <PaymentMethod domain="QBO" sparse="false">
    <Id>11</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-24T15:38:39-07:00</CreateTime>
      <LastUpdatedTime>2015-07-24T15:38:39-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Cashier's Check</Name>
    <Active>true</Active>
    <Type>NON_CREDIT_CARD</Type>
  </PaymentMethod>
</IntuitResponse>
```

## Query a paymentmethod

### Definition

- **Content type:** `application/text/`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from PaymentMethod"
```

#### XML example

```sql
select * from PaymentMethod
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "PaymentMethod": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "American Express",
        "sparse": false,
        "Active": true,
        "Type": "CREDIT_CARD",
        "Id": "6",
        "MetaData": {
          "CreateTime": "2014-09-11T14:42:05-07:00",
          "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Cash",
        "sparse": false,
        "Active": true,
        "Type": "NON_CREDIT_CARD",
        "Id": "1",
        "MetaData": {
          "CreateTime": "2014-09-11T14:42:05-07:00",
          "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Check",
        "sparse": false,
        "Active": true,
        "Type": "NON_CREDIT_CARD",
        "Id": "2",
        "MetaData": {
          "CreateTime": "2014-09-11T14:42:05-07:00",
          "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Diners Club",
        "sparse": false,
        "Active": true,
        "Type": "CREDIT_CARD",
        "Id": "7",
        "MetaData": {
          "CreateTime": "2014-09-11T14:42:05-07:00",
          "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Discover",
        "sparse": false,
        "Active": true,
        "Type": "CREDIT_CARD",
        "Id": "5",
        "MetaData": {
          "CreateTime": "2014-09-11T14:42:05-07:00",
          "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "MasterCard",
        "sparse": false,
        "Active": true,
        "Type": "CREDIT_CARD",
        "Id": "4",
        "MetaData": {
          "CreateTime": "2014-09-11T14:42:05-07:00",
          "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Visa",
        "sparse": false,
        "Active": true,
        "Type": "CREDIT_CARD",
        "Id": "3",
        "MetaData": {
          "CreateTime": "2014-09-11T14:42:05-07:00",
          "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
        }
      }
    ],
    "maxResults": 7
  },
  "time": "2015-07-24T15:26:51.916-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T15:26:12.990-07:00">
  <QueryResponse startPosition="1" maxResults="7">
    <PaymentMethod domain="QBO" sparse="false">
      <Id>6</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
        <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
      </MetaData>
      <Name>American Express</Name>
      <Active>true</Active>
      <Type>CREDIT_CARD</Type>
    </PaymentMethod>
    <PaymentMethod domain="QBO" sparse="false">
      <Id>1</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
        <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
      </MetaData>
      <Name>Cash</Name>
      <Active>true</Active>
      <Type>NON_CREDIT_CARD</Type>
    </PaymentMethod>
    <PaymentMethod domain="QBO" sparse="false">
      <Id>2</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
        <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
      </MetaData>
      <Name>Check</Name>
      <Active>true</Active>
      <Type>NON_CREDIT_CARD</Type>
    </PaymentMethod>
    <PaymentMethod domain="QBO" sparse="false">
      <Id>7</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
        <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
      </MetaData>
      <Name>Diners Club</Name>
      <Active>true</Active>
      <Type>CREDIT_CARD</Type>
    </PaymentMethod>
    <PaymentMethod domain="QBO" sparse="false">
      <Id>5</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
        <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
      </MetaData>
      <Name>Discover</Name>
      <Active>true</Active>
      <Type>CREDIT_CARD</Type>
    </PaymentMethod>
    <PaymentMethod domain="QBO" sparse="false">
      <Id>4</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
        <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
      </MetaData>
      <Name>MasterCard</Name>
      <Active>true</Active>
      <Type>CREDIT_CARD</Type>
    </PaymentMethod>
    <PaymentMethod domain="QBO" sparse="false">
      <Id>3</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
        <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
      </MetaData>
      <Name>Visa</Name>
      <Active>true</Active>
      <Type>CREDIT_CARD</Type>
    </PaymentMethod>
  </QueryResponse>
</IntuitResponse>
```

## Read a paymentmethod

### Definition

- **Operation:** `GET /v3/company/<realmID>/paymentmethod/<paymentmethodId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a paymentmethod object that has been previously created.

### Returns

Returns the paymentmethod object.

#### Example

```json
{
  "PaymentMethod": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "Diners Club",
    "sparse": false,
    "Active": true,
    "Type": "CREDIT_CARD",
    "Id": "7",
    "MetaData": {
      "CreateTime": "2014-09-11T14:42:05-07:00",
      "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
    }
  },
  "time": "2015-07-24T15:29:33.401-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T15:29:08.469-07:00">
  <PaymentMethod domain="QBO" sparse="false">
    <Id>7</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
      <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Diners Club</Name>
    <Active>true</Active>
    <Type>CREDIT_CARD</Type>
  </PaymentMethod>
</IntuitResponse>
```

## Full update a paymentmethod

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/paymentmethod`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing paymentmethod object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `paymentmethodresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "2",
  "domain": "QBO",
  "Name": "Platinum Diners Club",
  "sparse": false,
  "Active": true,
  "Type": "CREDIT_CARD",
  "Id": "7",
  "MetaData": {
    "CreateTime": "2014-09-11T14:42:05-07:00",
    "LastUpdatedTime": "2014-09-11T14:42:05-07:00"
  }
}
```

#### XML example

```xml
<PaymentMethod xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
   <Id>7</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
      <LastUpdatedTime>2014-09-11T14:42:05-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Business Diners Club</Name>
    <Active>true</Active>
    <Type>CREDIT_CARD</Type>
</PaymentMethod>
```

### Returns

The paymentmethod response body.

#### Example

```json
{
  "PaymentMethod": {
    "SyncToken": "2",
    "domain": "QBO",
    "Name": "Platinum Diners Club",
    "sparse": false,
    "Active": true,
    "Type": "CREDIT_CARD",
    "Id": "7",
    "MetaData": {
      "CreateTime": "2014-09-11T14:42:05-07:00",
      "LastUpdatedTime": "2015-07-24T15:33:48-07:00"
    }
  },
  "time": "2015-07-24T15:33:55.695-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T15:32:02.195-07:00">
  <PaymentMethod domain="QBO" sparse="false">
    <Id>7</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T14:42:05-07:00</CreateTime>
      <LastUpdatedTime>2015-07-24T15:32:02-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Business Diners Club</Name>
    <Active>true</Active>
    <Type>CREDIT_CARD</Type>
  </PaymentMethod>
</IntuitResponse>
```
