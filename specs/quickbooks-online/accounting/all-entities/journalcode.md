# JournalCode

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/journalcode
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / JournalCode
> Canonical entity: `JournalCode`

Applicable only for France-locale companies (FR locale). Journal Code is a compliance requirement for a France-locale company. A journal code is assigned to each transaction and it depends on whether it is an income or an expense. To access this entity, invoke the endpoints with the `minorversion=3` query parameter.

## The journalcode object

### journalcoderesponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `IdType`
Traits: read only, system defined, filterable, sortable

Unique Identifier for an Intuit entity (object). Required for the update operation.

#### `Name`

Required: Required
Type: `String`
Max length: 2 to 20 characters in length

A name representing the journal code.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the entity. Required for the update operation.

#### `Description`

Required: Optional
Type: `String`

A free-form description of the journal code.

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

#### `Type`

Required: Optional
Type: `String`

The type of this journal code. The value cannot be changed once the object is created. Valid types include: `Expenses` `Sales` `Bank` `Nouveaux` `Wages` `Cash` `Others`

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`
Traits: filterable, sortable

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
  "JournalCode": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "VT",
    "sparse": false,
    "time": "2015-12-16T11:01:37.346-07:00",
    "Active": true,
    "MetaData": {
      "CreateTime": "2015-10-30T11:06:19-07:00",
      "LastUpdatedTime": "2015-10-30T11:06:19-07:00"
    },
    "Type": "Sales",
    "Id": "2",
    "Description": "Sales"
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T14:55:06.451-07:00">
    <JournalCode domain="QBO" sparse="false">
        <Id>3</Id>
        <SyncToken>5</SyncToken>
        <MetaData>
            <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
            <LastUpdatedTime>2015-10-30T13:55:24-07:00</LastUpdatedTime>
        </MetaData>
        <Name>ABCDEFGHIJKLMNO</Name>
        <Type>Report A Nouveaux</Type>
        <Description>Report A Nouveaux</Description>
        <Active>true</Active>
    </JournalCode>
    <JournalCode domain="QBO" sparse="false">
        <Id>5</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
            <LastUpdatedTime>2015-10-30T11:06:20-07:00</LastUpdatedTime>
        </MetaData>
        <Name>CA</Name>
        <Type>Cash</Type>
        <Description>Cash</Description>
        <Active>true</Active>
    </JournalCode>
</IntuitResponse>
```

## Create a journalcode

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/journalcode`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The elements to create a journalcode object are listed here.

Schema: `journalcoderequest`

<details>
<summary>Show schema for `journalcoderequest`</summary>

#### journalcoderequest

Model type: `object`

##### `Name`

Required: Required
Type: `String`
Max length: 2 to 20 characters in length

A name representing the journal code.

</details>

#### Example

```json
{
  "Type": "Sales",
  "Name": "VT"
}
```

#### XML example

```xml
       <JournalCode domain="QBO" sparse="false">
            <Name>CA</Name>
            <Type>Cash</Type>
        </JournalCode>
```

### Returns

Returns the newly created journalcode object.

#### Example

```json
{
  "JournalCode": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "VT",
    "sparse": false,
    "time": "2015-12-16T11:01:37.346-07:00",
    "Active": true,
    "MetaData": {
      "CreateTime": "2015-10-30T11:06:19-07:00",
      "LastUpdatedTime": "2015-10-30T11:06:19-07:00"
    },
    "Type": "Sales",
    "Id": "2",
    "Description": "Sales"
  }
}
```

#### XML example

```xml
 <IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-12-16T11:19:56.688-08:00">
    <JournalCode domain="QBO" sparse="false">
        <Id>5</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
            <LastUpdatedTime>2015-10-30T11:06:20-07:00</LastUpdatedTime>
        </MetaData>
        <Name>CA</Name>
        <Type>Cash</Type>
        <Description>Cash</Description>
        <Active>true</Active>
    </JournalCode>
</IntuitResponse>
```

## Query a journalcode

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from journalcode"
```

#### XML example

```sql
select * from journalcode
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "JournalCode": [
      {
        "SyncToken": "5",
        "domain": "QBO",
        "Name": "ABCDEFGHIJKLMNO",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2015-10-30T11:06:20-07:00",
          "LastUpdatedTime": "2015-10-30T13:55:24-07:00"
        },
        "Type": "Report A Nouveaux",
        "Id": "3",
        "Description": "Report A Nouveaux"
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "CA",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2015-10-30T11:06:20-07:00",
          "LastUpdatedTime": "2015-10-30T11:06:20-07:00"
        },
        "Type": "Cash",
        "Id": "5",
        "Description": "Cash"
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "HA",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2015-10-30T11:06:19-07:00",
          "LastUpdatedTime": "2015-10-30T11:06:19-07:00"
        },
        "Type": "Expenses",
        "Id": "1",
        "Description": "Expenses"
      },
      {
        "SyncToken": "1",
        "domain": "QBO",
        "Name": "NO",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2015-10-30T11:06:20-07:00",
          "LastUpdatedTime": "2015-10-30T14:26:40-07:00"
        },
        "Type": "Report A Nouveaux",
        "Id": "4",
        "Description": "Report A Nouveaux"
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "OD",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2015-10-30T11:06:20-07:00",
          "LastUpdatedTime": "2015-10-30T11:06:20-07:00"
        },
        "Type": "Others",
        "Id": "6",
        "Description": "Others"
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "VT",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2015-10-30T11:06:19-07:00",
          "LastUpdatedTime": "2015-10-30T11:06:19-07:00"
        },
        "Type": "Sales",
        "Id": "2",
        "Description": "Sales"
      }
    ],
    "maxResults": 6,
    "totalCount": 6
  },
  "time": "2015-12-16T09:16:15.597-08:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-12-16T09:17:50.082-08:00">
    <QueryResponse startPosition="1" maxResults="6" totalCount="6">
        <JournalCode domain="QBO" sparse="false">
            <Id>3</Id>
            <SyncToken>5</SyncToken>
            <MetaData>
                <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
                <LastUpdatedTime>2015-10-30T13:55:24-07:00</LastUpdatedTime>
            </MetaData>
            <Name>ABCDEFGHIJKLMNO</Name>
            <Type>Report A Nouveaux</Type>
            <Description>Report A Nouveaux</Description>
            <Active>true</Active>
        </JournalCode>
        <JournalCode domain="QBO" sparse="false">
            <Id>5</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
                <LastUpdatedTime>2015-10-30T11:06:20-07:00</LastUpdatedTime>
            </MetaData>
            <Name>CA</Name>
            <Type>Cash</Type>
            <Description>Cash</Description>
            <Active>true</Active>
        </JournalCode>
        <JournalCode domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-10-30T11:06:19-07:00</CreateTime>
                <LastUpdatedTime>2015-10-30T11:06:19-07:00</LastUpdatedTime>
            </MetaData>
            <Name>HA</Name>
            <Type>Expenses</Type>
            <Description>Expenses</Description>
            <Active>true</Active>
        </JournalCode>
        <JournalCode domain="QBO" sparse="false">
            <Id>4</Id>
            <SyncToken>1</SyncToken>
            <MetaData>
                <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
                <LastUpdatedTime>2015-10-30T14:26:40-07:00</LastUpdatedTime>
            </MetaData>
            <Name>NO</Name>
            <Type>Report A Nouveaux</Type>
            <Description>Report A Nouveaux</Description>
            <Active>true</Active>
        </JournalCode>
        <JournalCode domain="QBO" sparse="false">
            <Id>6</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
                <LastUpdatedTime>2015-10-30T11:06:20-07:00</LastUpdatedTime>
            </MetaData>
            <Name>OD</Name>
            <Type>Others</Type>
            <Description>Others</Description>
            <Active>true</Active>
        </JournalCode>
        <JournalCode domain="QBO" sparse="false">
            <Id>2</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-10-30T11:06:19-07:00</CreateTime>
                <LastUpdatedTime>2015-10-30T11:06:19-07:00</LastUpdatedTime>
            </MetaData>
            <Name>VT</Name>
            <Type>Sales</Type>
            <Description>Sales</Description>
            <Active>true</Active>
        </JournalCode>
    </QueryResponse>
</IntuitResponse>
```

## Read a journalcode

### Definition

- **Operation:** `GET /v3/company/<realmID>/journalcode/<journalcodeId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a journalcode object that has been previously created.

### Returns

Returns the journalcode object.

#### Example

```json
{
  "JournalCode": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "VT",
    "sparse": false,
    "time": "2015-12-16T11:01:37.346-07:00",
    "Active": true,
    "MetaData": {
      "CreateTime": "2015-10-30T11:06:19-07:00",
      "LastUpdatedTime": "2015-10-30T11:06:19-07:00"
    },
    "Type": "Sales",
    "Id": "2",
    "Description": "Sales"
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T14:55:06.451-07:00">
    <JournalCode domain="QBO" sparse="false">
        <Id>3</Id>
        <SyncToken>5</SyncToken>
        <MetaData>
            <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
            <LastUpdatedTime>2015-10-30T13:55:24-07:00</LastUpdatedTime>
        </MetaData>
        <Name>ABCDEFGHIJKLMNO</Name>
        <Type>Report A Nouveaux</Type>
        <Description>Report A Nouveaux</Description>
        <Active>true</Active>
    </JournalCode>
    <JournalCode domain="QBO" sparse="false">
        <Id>5</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
            <LastUpdatedTime>2015-10-30T11:06:20-07:00</LastUpdatedTime>
        </MetaData>
        <Name>CA</Name>
        <Type>Cash</Type>
        <Description>Cash</Description>
        <Active>true</Active>
    </JournalCode>
</IntuitResponse>
```

## Update a journalcode

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/journalcode`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update an active journalcode object or to deactiveate a currently active one, as provided in the request.

### Request Body

Schema: `journalcoderesponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "domain": "QBO",
  "Name": "VT",
  "sparse": false,
  "Active": true,
  "MetaData": {
    "CreateTime": "2015-10-30T11:06:19-07:00",
    "LastUpdatedTime": "2015-10-30T11:06:19-07:00"
  },
  "Type": "Sales",
  "Id": "2",
  "Description": "An updated description"
}
```

#### XML example

```xml
   <JournalCode xmlns="http://schema.intuit.com/finance/v3" sparse="false">
        <Id>5</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
            <LastUpdatedTime>2015-10-30T11:06:20-07:00</LastUpdatedTime>
        </MetaData>
        <Name>CA</Name>
        <Type>Cash</Type>
        <Description>An updated description.</Description>
        <Active>true</Active>
    </JournalCode>
```

### Returns

The journalcode response body.

#### Example

```json
{
  "JournalCode": {
    "SyncToken": "1",
    "domain": "QBO",
    "Name": "VT",
    "sparse": false,
    "time": "2015-12-16T11:06:19-07:00",
    "Active": true,
    "MetaData": {
      "CreateTime": "2015-12-16T11:06:19-07:00",
      "LastUpdatedTime": "2015-12-16T11:06:19-07:00"
    },
    "Type": "Sales",
    "Id": "2",
    "Description": "An updated description"
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-12-16T14:55:06.451-07:00">
    <JournalCode domain="QBO" sparse="false">
        <Id>5</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2015-10-30T11:06:20-07:00</CreateTime>
            <LastUpdatedTime>2015-10-30T11:06:20-07:00</LastUpdatedTime>
        </MetaData>
        <Name>CA</Name>
        <Type>Cash</Type>
        <Description>An updated description</Description>
        <Active>true</Active>
    </JournalCode>
</IntuitResponse>
```
