# TaxAgency

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxagency
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / TaxAgency
> Canonical entity: `TaxAgency`

A TaxAgency object is associated with a tax rate and identifies the agency to which that tax rate applies, that is, the entity that collects those taxes. QuickBooks companies based in the US will only display system-created tax agencies. They also only display the associated tax rates available and visible via the QuickBooks UI.

## The taxagency object

### taxagencyresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `DisplayName`

Required: Required
Type: `String`
Traits: sortable
Max length: Maximum of 100 chars

Name of the agency.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `TaxAgencyConfig`

Type: `String`
Traits: read only
Minor version: 46

Flag to identify whether the TaxAgency is system defined by Automated Sales Tax engine or user generated. Valid values include `USER_DEFINED`, `SYSTEM_GENERATED`SYSTEM_GENERATED.

#### `TaxTrackedOnSales`

Required: Optional
Type: `Boolean`
Traits: read only
Default: true

Denotes whether this tax agency is used to track tax on sales.

#### `TaxTrackedOnPurchases`

Required: Optional
Type: `Boolean`
Traits: read only
Default: false

Denotes whether this tax agency is used to track tax on purchases.

#### `LastFileDate`

Required: Optional
Type: `Date`
Traits: read only
Minor version: 6
Locales: FR, GB, AU, IN, CA

The last tax filing date for this tax agency. This field is automatically populated by QuickBooks business logic at tax filing time.

#### `TaxRegistrationNumber`

Required: Optional
Type: `String`
Traits: read only

Registration number for the agency.

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
  "time": "2015-07-27T14:30:33.478-07:00",
  "TaxAgency": {
    "SyncToken": "0",
    "domain": "QBO",
    "DisplayName": "Arizona Dept. of Revenue",
    "TaxTrackedOnSales": true,
    "TaxTrackedOnPurchases": false,
    "sparse": false,
    "Id": "1",
    "MetaData": {
      "CreateTime": "2014-09-18T12:17:04-07:00",
      "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
    }
  }
}
```

## Create a taxagency

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/taxagency`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

A TaxAgency object must have a `DisplayName` attribute.

### Request Body

The minimum elements to create a taxagency object are listed here.

Schema: `taxagencyrequest`

<details>
<summary>Show schema for `taxagencyrequest`</summary>

#### taxagencyrequest

Model type: `object`

##### `DisplayName`

Required: Required
Type: `String`
Traits: sortable
Max length: Maximum of 100 chars

Name of the agency.

</details>

#### Example

```json
{
  "DisplayName": "CityTaxAgency"
}
```

#### XML example

```text
XML requests not supported.
```

### Returns

Returns the newly created taxagency object.

#### Example

```json
{
  "time": "2015-07-27T14:32:27.116-07:00",
  "TaxAgency": {
    "SyncToken": "0",
    "domain": "QBO",
    "DisplayName": "CityTaxAgency",
    "TaxTrackedOnSales": true,
    "TaxTrackedOnPurchases": false,
    "sparse": false,
    "Id": "3",
    "MetaData": {
      "CreateTime": "2015-07-27T14:32:27-07:00",
      "LastUpdatedTime": "2015-07-27T14:32:27-07:00"
    }
  }
}
```

## Query a taxagency

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from TaxAgency"
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 2,
    "maxResults": 2,
    "TaxAgency": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DisplayName": "Arizona Dept. of Revenue",
        "TaxTrackedOnSales": true,
        "TaxTrackedOnPurchases": false,
        "sparse": false,
        "Id": "1",
        "MetaData": {
          "CreateTime": "2014-09-18T12:17:04-07:00",
          "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DisplayName": "Board of Equalization",
        "TaxTrackedOnSales": true,
        "TaxTrackedOnPurchases": false,
        "sparse": false,
        "Id": "2",
        "MetaData": {
          "CreateTime": "2014-09-18T12:17:04-07:00",
          "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
        }
      }
    ]
  },
  "time": "2015-07-27T14:26:19.454-07:00"
}
```

## Read a taxagency

### Definition

- **Operation:** `GET /v3/company/<realmID>/taxagency/<taxagencyId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a TaxAgency object that has been previously created.

### Returns

Returns the TaxAgency object.

#### Example

```json
{
  "time": "2015-07-27T14:30:33.478-07:00",
  "TaxAgency": {
    "SyncToken": "0",
    "domain": "QBO",
    "DisplayName": "Arizona Dept. of Revenue",
    "TaxTrackedOnSales": true,
    "TaxTrackedOnPurchases": false,
    "sparse": false,
    "Id": "1",
    "MetaData": {
      "CreateTime": "2014-09-18T12:17:04-07:00",
      "LastUpdatedTime": "2014-09-18T12:17:04-07:00"
    }
  }
}
```
