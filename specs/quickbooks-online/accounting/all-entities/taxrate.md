# TaxRate

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxrate
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / TaxRate
> Canonical entity: `TaxRate`

A TaxRate object represents rate applied to calculate tax liability. Use the TaxService entity to create a taxrate. See [Global tax model](https://developer.intuit.com/app/developer/qbo/docs/workflows/calculate-sales-tax/automated-sales-tax-for-non-us-locales) for more information about using TaxRate objects and the tax model in general

### Create a taxrate

Use the `TaxService` resource to create a tax rate.

## The TaxRate object

### taxrateresponse

Model type: `object`

#### `Id`

Required: Optional
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `RateValue`

Required: Optional
Type: `String`
Traits: read only

Value of the tax rate.

#### `Name`

Required: Optional
Type: `String`
Traits: read only, filterable, sortable
Max length: Maximum of 100 chars

User recognizable name for the tax rate.

#### `AgencyRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, filterable, sortable

Reference to the tax agency associated with this object.

<details>
<summary>Child attributes for `AgencyRef`</summary>

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

#### `SpecialTaxType`

Required: Optional
Type: `Sting`
Traits: read only

Special tax type to handle zero rate taxes. Used with VAT registered Businesses who receive goods/services (acquisitions) from other EU countries, will need to calculate the VAT due, but not paid, on these acquisitions. The rate of VAT payable is the same that would have been paid if the goods had been supplied by a UK supplier.

#### `EffectiveTaxRate`

Required: Optional
Type: `EffectiveTaxRateData`
Traits: read only

List of EffectiveTaxRate. An EffectiveTaxRate is used to know which taxrate is applicable on any date.

<details>
<summary>Child attributes for `EffectiveTaxRate`</summary>

##### effectivetaxratedata

Model type: `object`

###### `RateValue`

Type: `Decimal`

Represents rate value.

###### `EndDate`

Type: `String`

End date of this taxrate applicability: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

###### `EffectiveDate`

Type: `String`

Effective starting date for which this taxrate is applicable: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

#### `DisplayType`

Required: Optional
Type: `Sting`
Traits: read only

TaxRate DisplayType enum which acts as display config.

#### `TaxReturnLineRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, filterable, sortable

Reference to the tax return line associated with this object.

<details>
<summary>Child attributes for `TaxReturnLineRef`</summary>

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

#### `Active`

Required: Optional
Type: `Boolean`
Traits: read only, filterable, sortable
Default: true

If true, this object is currently enabled for use by QuickBooks.

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

#### `OriginalTaxRate`

Required: Optional
Type: `String`
Traits: read only
Minor version: 62
Locales: CA

ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities.

#### `Description`

Required: Optional
Type: `String`
Traits: read only, filterable, sortable
Max length: Maximum of 100 chars

User entered description for the tax rate.

#### Example

```json
{
  "TaxRate": {
    "RateValue": 2,
    "AgencyRef": {
      "value": "1"
    },
    "domain": "QBO",
    "Name": "Tucson City",
    "SyncToken": "0",
    "SpecialTaxType": "NONE",
    "DisplayType": "ReadOnly",
    "sparse": false,
    "Active": true,
    "MetaData": {
      "CreateTime": "2014-09-18T12:17:04-07:00",
      "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
    },
    "Id": "2",
    "Description": "Sales Tax"
  },
  "time": "2015-07-27T13:29:41.836-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T13:28:08.935-07:00">
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
</IntuitResponse>
```

## Query a taxrate

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"Select * From TaxRate"
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
    "totalCount": 3,
    "TaxRate": [
      {
        "RateValue": 7.1,
        "AgencyRef": {
          "value": "1"
        },
        "domain": "QBO",
        "Name": "AZ State tax",
        "SyncToken": "0",
        "SpecialTaxType": "NONE",
        "DisplayType": "ReadOnly",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2014-09-18T12:17:04-07:00",
          "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
        },
        "Id": "1",
        "Description": "Sales Tax"
      },
      {
        "RateValue": 8,
        "AgencyRef": {
          "value": "2"
        },
        "domain": "QBO",
        "Name": "California",
        "SyncToken": "0",
        "SpecialTaxType": "NONE",
        "DisplayType": "ReadOnly",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2014-09-18T12:17:04-07:00",
          "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
        },
        "Id": "3",
        "Description": "Sales Tax"
      },
      {
        "RateValue": 2,
        "AgencyRef": {
          "value": "1"
        },
        "domain": "QBO",
        "Name": "Tucson City",
        "SyncToken": "0",
        "SpecialTaxType": "NONE",
        "DisplayType": "ReadOnly",
        "sparse": false,
        "Active": true,
        "MetaData": {
          "CreateTime": "2014-09-18T12:17:04-07:00",
          "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
        },
        "Id": "2",
        "Description": "Sales Tax"
      }
    ],
    "maxResults": 3
  },
  "time": "2015-07-27T13:32:06.76-07:00"
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

## Read a taxrate

### Definition

- **Operation:** `GET /v3/company/<realmID>/taxrate/<taxrateId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a TaxRate object.

### Returns

Returns the TaxRate object.

#### Example

```json
{
  "TaxRate": {
    "RateValue": 2,
    "AgencyRef": {
      "value": "1"
    },
    "domain": "QBO",
    "Name": "Tucson City",
    "SyncToken": "0",
    "SpecialTaxType": "NONE",
    "DisplayType": "ReadOnly",
    "sparse": false,
    "Active": true,
    "MetaData": {
      "CreateTime": "2014-09-18T12:17:04-07:00",
      "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
    },
    "Id": "2",
    "Description": "Sales Tax"
  },
  "time": "2015-07-27T13:29:41.836-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T13:28:08.935-07:00">
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
</IntuitResponse>
```
