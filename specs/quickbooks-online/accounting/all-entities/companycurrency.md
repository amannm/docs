# CompanyCurrency

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/companycurrency
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / CompanyCurrency
> Canonical entity: `CompanyCurrency`

Applicable only for those companies that enable multicurrency, a companycurrency object defines a currency that is active in the QuickBooks Online company. One or more companycurrency objects are active based on the company's multicurrency business requirements and correspond to the list displayed by the Currency Center in the QuickBooks Online UI. [Click here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies) for more information about managing currency settings with the QuickBooks API.

### Delete a companycurrency

Delete is achieved by setting the `Active` attribute to `false` in an entity update request; thus, making it inactive. In this type of delete, the record is not permanently deleted, but is hidden for display purposes. References to inactive objects are left intact.

## The companycurrency object

### companycurrencyresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Code`

Required: Required
Type: `String`
Max length: maximum of 100 chars

A three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on. [Click here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies) for a list of supported currency codes.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `Name`

Required: Optional
Type: `String`
Traits: system defined

The full name of the currency.

#### `CustomField `

Required: Optional
Type: `CustomField`

One of, up to three custom fields for the transaction. Available for custom fields so configured for the company. Check `Preferences.SalesFormsPrefs.CustomField` and `Preferences.VendorAndPurchasesPrefs.POCustomField` for custom fields currenly configured. [Click here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/create-custom-fields) to learn about managing custom fields.

<details>
<summary>Child attributes for `CustomField `</summary>

##### customfield

Model type: `object`

###### `DefinitionId`

Required: Required
Type: `String`
Traits: read only, system defined

Unique identifier of the CustomFieldDefinition that corresponds to this CustomField.

###### `Type`

Type: `CustomFieldTypeEnum`
Traits: read only

Data type of custom field. Only one type is currently supported: `StringType`.

###### `StringValue`

Required: Optional
Type: `String`

The value for the `StringType`custom field.

###### `Name`

Required: Optional
Type: `String`
Traits: read only

Name of the custom field.

</details>

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable, sortable
Default: true

Indicates whether this currency is active in the company or not. `true`--This currency is active and enabled for use by QuickBooks. `false`--This currency is inactive, is hidden from most display purposes, and is not availble for use with financial transactions.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`
Traits: filterable, sortable

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
  "CompanyCurrency": {
    "SyncToken": "0",
    "domain": "QBO",
    "Code": "EUR",
    "Name": "Euro",
    "sparse": false,
    "Active": true,
    "Id": "2",
    "MetaData": {
      "CreateTime": "2015-06-05T13:59:42-07:00",
      "LastUpdatedTime": "2015-06-05T13:59:42-07:00"
    }
  },
  "time": "2015-07-06T13:30:04.123-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-06T13:30:22.930-07:00">
    <CompanyCurrency domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-06-05T13:59:42-07:00</CreateTime>
            <LastUpdatedTime>2015-06-05T13:59:42-07:00</LastUpdatedTime>
        </MetaData>
        <Code>EUR</Code>
        <Name>Euro</Name>
        <Active>true</Active>
    </CompanyCurrency>
</IntuitResponse>
```

## Create a companycurrency

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/companycurrency`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The elements to create a CompanyCurrency object are listed here.

Schema: `companycurrencyrequest`

<details>
<summary>Show schema for `companycurrencyrequest`</summary>

#### companycurrencyrequest

Model type: `object`

##### `Code`

Required: Required
Type: `String`
Max length: maximum of 100 chars

A three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on.

</details>

#### Example

```json
{
  "Code": "GBP"
}
```

#### XML example

```xml
<CompanyCurrency xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Code>USD</Code>
</CompanyCurrency>
```

### Returns

Returns the newly created companycurrency object.

#### Example

```json
{
  "CompanyCurrency": {
    "SyncToken": "0",
    "domain": "QBO",
    "Code": "GBP",
    "Name": "British Pound Sterling",
    "sparse": false,
    "Active": true,
    "Id": "7",
    "MetaData": {
      "CreateTime": "2015-07-06T13:34:48-07:00",
      "LastUpdatedTime": "2015-07-06T13:34:48-07:00"
    }
  },
  "time": "2015-07-06T13:34:48.569-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-06T13:32:02.008-07:00">
    <CompanyCurrency domain="QBO" sparse="false">
        <Id>6</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-06T13:32:02-07:00</CreateTime>
            <LastUpdatedTime>2015-07-06T13:32:02-07:00</LastUpdatedTime>
        </MetaData>
        <Code>USD</Code>
        <Name>United States Dollar</Name>
        <Active>true</Active>
    </CompanyCurrency>
</IntuitResponse>
```

## Query a companycurrency

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from companycurrency"
```

#### XML example

```sql
select * from companycurrency
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 5,
    "CompanyCurrency": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Code": "JPY",
        "Name": "Japanese Yen",
        "sparse": false,
        "Active": true,
        "Id": "5",
        "MetaData": {
          "CreateTime": "2015-06-19T09:20:44-07:00",
          "LastUpdatedTime": "2015-06-19T09:20:44-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Code": "ANG",
        "Name": "Dutch Guilder",
        "sparse": false,
        "Active": true,
        "Id": "4",
        "MetaData": {
          "CreateTime": "2015-06-12T14:16:38-07:00",
          "LastUpdatedTime": "2015-06-12T14:16:38-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Code": "AUD",
        "Name": "Australian Dollar",
        "sparse": false,
        "Active": true,
        "Id": "3",
        "MetaData": {
          "CreateTime": "2015-06-05T13:59:43-07:00",
          "LastUpdatedTime": "2015-06-05T13:59:43-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Code": "EUR",
        "Name": "Euro",
        "sparse": false,
        "Active": true,
        "Id": "2",
        "MetaData": {
          "CreateTime": "2015-06-05T13:59:42-07:00",
          "LastUpdatedTime": "2015-06-05T13:59:42-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Code": "CAD",
        "Name": "Canadian Dollar",
        "sparse": false,
        "Active": true,
        "Id": "1",
        "MetaData": {
          "CreateTime": "2015-06-05T13:59:42-07:00",
          "LastUpdatedTime": "2015-06-05T13:59:42-07:00"
        }
      }
    ],
    "maxResults": 5
  },
  "time": "2015-07-06T13:29:01.560-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-06T13:27:49.342-07:00">
    <QueryResponse startPosition="1" maxResults="5" totalCount="5">
        <CompanyCurrency domain="QBO" sparse="false">
            <Id>5</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-06-19T09:20:44-07:00</CreateTime>
                <LastUpdatedTime>2015-06-19T09:20:44-07:00</LastUpdatedTime>
            </MetaData>
            <Code>JPY</Code>
            <Name>Japanese Yen</Name>
            <Active>true</Active>
        </CompanyCurrency>
        <CompanyCurrency domain="QBO" sparse="false">
            <Id>4</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-06-12T14:16:38-07:00</CreateTime>
                <LastUpdatedTime>2015-06-12T14:16:38-07:00</LastUpdatedTime>
            </MetaData>
            <Code>ANG</Code>
            <Name>Dutch Guilder</Name>
            <Active>true</Active>
        </CompanyCurrency>
        <CompanyCurrency domain="QBO" sparse="false">
            <Id>3</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-06-05T13:59:43-07:00</CreateTime>
                <LastUpdatedTime>2015-06-05T13:59:43-07:00</LastUpdatedTime>
            </MetaData>
            <Code>AUD</Code>
            <Name>Australian Dollar</Name>
            <Active>true</Active>
        </CompanyCurrency>
        <CompanyCurrency domain="QBO" sparse="false">
            <Id>2</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-06-05T13:59:42-07:00</CreateTime>
                <LastUpdatedTime>2015-06-05T13:59:42-07:00</LastUpdatedTime>
            </MetaData>
            <Code>EUR</Code>
            <Name>Euro</Name>
            <Active>true</Active>
        </CompanyCurrency>
        <CompanyCurrency domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-06-05T13:59:42-07:00</CreateTime>
                <LastUpdatedTime>2015-06-05T13:59:42-07:00</LastUpdatedTime>
            </MetaData>
            <Code>CAD</Code>
            <Name>Canadian Dollar</Name>
            <Active>true</Active>
        </CompanyCurrency>
    </QueryResponse>
</IntuitResponse>
```

## Read a companycurrency

### Definition

- **Operation:** `GET /v3/company/<realmID>/companycurrency/<companycurrencyId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a CompanyCurrency object that has been previously created.

### Returns

Returns the companycurrency object.

#### Example

```json
{
  "CompanyCurrency": {
    "SyncToken": "0",
    "domain": "QBO",
    "Code": "EUR",
    "Name": "Euro",
    "sparse": false,
    "Active": true,
    "Id": "2",
    "MetaData": {
      "CreateTime": "2015-06-05T13:59:42-07:00",
      "LastUpdatedTime": "2015-06-05T13:59:42-07:00"
    }
  },
  "time": "2015-07-06T13:30:04.123-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-06T13:30:22.930-07:00">
    <CompanyCurrency domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-06-05T13:59:42-07:00</CreateTime>
            <LastUpdatedTime>2015-06-05T13:59:42-07:00</LastUpdatedTime>
        </MetaData>
        <Code>EUR</Code>
        <Name>Euro</Name>
        <Active>true</Active>
    </CompanyCurrency>
</IntuitResponse>
```

## Update a companycurrency

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/companycurrency`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing CompanyCurrency object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `companycurrencyresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "domain": "QBO",
  "Code": "GBP",
  "Name": "British Pound Sterling",
  "sparse": false,
  "Active": false,
  "Id": "7",
  "MetaData": {
    "CreateTime": "2015-07-06T13:34:48-07:00",
    "LastUpdatedTime": "2015-07-06T13:34:48-07:00"
  }
}
```

#### XML example

```xml
<CompanyCurrency xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>3</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
        <CreateTime>2015-06-05T13:59:43-07:00</CreateTime>
        <LastUpdatedTime>2015-06-05T13:59:43-07:00</LastUpdatedTime>
    </MetaData>
    <Code>AUD</Code>
    <Name>Australian Dollar</Name>
    <Active>false</Active>
</CompanyCurrency>
```

### Returns

The companycurrency response body.

#### Example

```json
{
  "CompanyCurrency": {
    "SyncToken": "1",
    "domain": "QBO",
    "Code": "GBP",
    "Name": "British Pound Sterling",
    "sparse": false,
    "Active": false,
    "Id": "7",
    "MetaData": {
      "CreateTime": "2015-07-06T13:34:48-07:00",
      "LastUpdatedTime": "2015-07-06T14:03:40-07:00"
    }
  },
  "time": "2015-07-06T14:03:39.891-07:00"
}
```

#### XML example

```xml
<CompanyCurrency xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>3</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
        <CreateTime>2015-06-05T13:59:43-07:00</CreateTime>
        <LastUpdatedTime>2015-06-05T14:09:43-07:00</LastUpdatedTime>
    </MetaData>
    <Code>AUD</Code>
    <Name>Australian Dollar</Name>
    <Active>false</Active>
</CompanyCurrency>
```
