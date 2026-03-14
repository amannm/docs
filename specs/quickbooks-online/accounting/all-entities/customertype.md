# CustomerType

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customertype
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / CustomerType
> Canonical entity: `CustomerType`

Customer types allow categorizing customers in ways that are meaningful to the business. For example, one could set up customer types so that they indicate which industry a customer represents, a customer's geographic location, or how a customer first heard about the business. The categorization then can be used for reporting or mailings.

## The CustomerType object

### customertyperesponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `Name`

Required: Required for update
Type: `String`
Traits: system defined

The full name of the customer type.

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable, sortable
Default: true

Indicates whether this customer type is active in the company or not. `true`--This customer type is active and enabled for use by QuickBooks. `false`—This customer type is inactive, is hidden from most display purposes, and is not availble for use with financial transactions.

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
  "CustomerType": {
    "SyncToken": "1",
    "domain": "QBO",
    "Name": "ActiveNew",
    "sparse": false,
    "Active": true,
    "Id": "5000000000000003466",
    "MetaData": {
      "CreateTime": "2019-04-10T15:18:04-07:00",
      "LastUpdatedTime": "2019-04-10T15:36:53-07:00"
    }
  },
  "time": "2019-04-12T16:19:36.824-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2019-04-10T15:18:04-07:00">
  <CustomerType>
    <Name>ActiveNew</Name>
    <Active>true</Active>
    <domain>QBO</domain>
    <sparse>false</sparse>
    <Id>5000000000000003466</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2019-04-10T15:18:04-07:00</CreateTime>
      <LastUpdatedTime>2019-04-10T15:36:53-07:00</LastUpdatedTime>
    </MetaData>
  </CustomerType>
  <time>2019-04-12T16:19:36.824-07:00</time>
</IntuitResponse>
```

## Query a customertype

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"Select * From CustomerType"
```

#### XML example

```sql
select * from TaxRate
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "CustomerType": [
      {
        "SyncToken": "1",
        "domain": "QBO",
        "Name": "ActiveNew",
        "sparse": false,
        "Active": true,
        "Id": "5000000000000003466",
        "MetaData": {
          "CreateTime": "2019-04-10T15:18:04-07:00",
          "LastUpdatedTime": "2019-04-10T15:36:53-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Value",
        "sparse": false,
        "Active": true,
        "Id": "5000000000000003467",
        "MetaData": {
          "CreateTime": "2019-04-10T15:24:02-07:00",
          "LastUpdatedTime": "2019-04-10T15:24:02-07:00"
        }
      }
    ],
    "maxResults": 2
  },
  "time": "2019-04-12T16:17:47.414-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T13:10:18.062-07:00">
  <QueryResponse startPosition="1" maxResults="3" totalCount="3">
    <TaxRate domain="QBO" sparse="false">
      <Id>1</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-18T12:17:04-07:00</CreateTime>
        <LastUpdatedTime>2014-09-18T12:17:04-07:00</LastUpdatedTime>
      </MetaData>
      <Name>AZ State tax</Name>
      <Description>Sales Tax</Description>
      <Active>true</Active>
      <RateValue>7.1</RateValue>
      <AgencyRef>1</AgencyRef>
      <SpecialTaxType>NONE</SpecialTaxType>
      <DisplayType>ReadOnly</DisplayType>
    </TaxRate>
    <TaxRate domain="QBO" sparse="false">
      <Id>3</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-18T12:17:04-07:00</CreateTime>
        <LastUpdatedTime>2014-09-18T12:17:04-07:00</LastUpdatedTime>
      </MetaData>
      <Name>California</Name>
      <Description>Sales Tax</Description>
      <Active>true</Active>
      <RateValue>8</RateValue>
      <AgencyRef>2</AgencyRef>
      <SpecialTaxType>NONE</SpecialTaxType>
      <DisplayType>ReadOnly</DisplayType>
    </TaxRate>
    <TaxRate domain="QBO" sparse="false">
      <Id>2</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2014-09-18T12:17:04-07:00</CreateTime>
        <LastUpdatedTime>2014-09-18T12:17:04-07:00</LastUpdatedTime>
      </MetaData>
      <Name>Tucson City</Name>
      <Description>Sales Tax</Description>
      <Active>true</Active>
      <RateValue>2</RateValue>
      <AgencyRef>1</AgencyRef>
      <SpecialTaxType>NONE</SpecialTaxType>
      <DisplayType>ReadOnly</DisplayType>
    </TaxRate>
  </QueryResponse>
</IntuitResponse>
```

## Read a customertype

### Definition

- **Operation:** `GET /v3/company/<realmID>/customertype/<Id>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Customertype object.

### Returns

Returns the Customertype object.

#### Example

```json
{
  "CustomerType": {
    "SyncToken": "1",
    "domain": "QBO",
    "Name": "ActiveNew",
    "sparse": false,
    "Active": true,
    "Id": "5000000000000003466",
    "MetaData": {
      "CreateTime": "2019-04-10T15:18:04-07:00",
      "LastUpdatedTime": "2019-04-10T15:36:53-07:00"
    }
  },
  "time": "2019-04-12T16:19:36.824-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2019-04-10T15:18:04-07:00">
  <CustomerType>
    <Name>ActiveNew</Name>
    <Active>true</Active>
    <domain>QBO</domain>
    <sparse>false</sparse>
    <Id>5000000000000003466</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2019-04-10T15:18:04-07:00</CreateTime>
      <LastUpdatedTime>2019-04-10T15:36:53-07:00</LastUpdatedTime>
    </MetaData>
  </CustomerType>
  <time>2019-04-12T16:19:36.824-07:00</time>
</IntuitResponse>
```
