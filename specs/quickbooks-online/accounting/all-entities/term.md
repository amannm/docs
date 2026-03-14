# Term

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/term
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Term
> Canonical entity: `Term`

A Term object represents the terms under which a sale is made, typically expressed in the form of days due after the goods are received. Optionally, a discount of the total amount may be applied if payment is made within a stipulated time. For example, net 30 indicates that payment is due within 30 days. A term of 2%/15 net 60 indicates that payment is due within 60 days, with a discount of 2% if payment is made within 15 days. This resource also supports:

- An absolute due date.
- A number of days from a start date.
- A percent discount.
- An absolute discount.

## The term object

### termresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Name`

Required: Required
Type: `String`
Traits: filterable, sortable
Max length: max 31 characters

User recognizable name for the term. For example, `Net 30`.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `DayOfMonthDue`

Type: `Integer`
Max length: Range is 1 through 31

Payment must be received by this day of the month. Used only if `DueDays` is not specified. Required if `DueDays` not present

#### `DiscountDayOfMonth`

Type: `Positive Integer`
Max length: Range is 0 through 31

Discount applies if paid before this day of month. Required if `DueDays` not present

#### `DueNextMonthDays`

Type: `Positive Integer`
Max length: Range is 0 through 999

Payment due next month if issued that many days before the `DayOfMonthDue`. Required if `DueDays` not present.

#### `DueDays`

Type: `Integer`
Max length: Range is 0 through 999

Number of days from delivery of goods or services until the payment is due. Required if `DayOfMonthDue` not present

#### `DiscountPercent`

Required: Optional
Type: `Decimal`
Max length: Range is 0 through 100

Discount percentage available against an amount if paid within the days specified by `DiscountDays`.

#### `DiscountDays`

Required: Optional
Type: `Integer`
Max length: Range is 0 through 999

Discount applies if paid within this number of days. Used only when `DueDays` is specified.

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable, sortable
Default: true

If true, this entity is currently enabled for use by QuickBooks.

#### `Type`

Required: Optional
Type: `String`
Traits: system defined

Type of the Sales Term. Valid values: `STANDARD`--Used if `DueDays` is not null. `DATE_DRIVEN`--Used if `DueDays` is null.

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
  "Term": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "Net 60",
    "DiscountPercent": 0,
    "DiscountDays": 0,
    "Type": "STANDARD",
    "sparse": false,
    "Active": true,
    "DueDays": 60,
    "Id": "4",
    "MetaData": {
      "CreateTime": "2014-09-11T14:41:49-07:00",
      "LastUpdatedTime": "2014-09-11T14:41:49-07:00"
    }
  },
  "time": "2015-07-28T08:52:57.63-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T08:53:15.475-07:00">
  <Term domain="QBO" sparse="false">
    <Id>4</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T14:41:49-07:00</CreateTime>
      <LastUpdatedTime>2014-09-11T14:41:49-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Net 60</Name>
    <Active>true</Active>
    <Type>STANDARD</Type>
    <DiscountPercent>0</DiscountPercent>
    <DueDays>60</DueDays>
    <DiscountDays>0</DiscountDays>
  </Term>
</IntuitResponse>
```

## Create a term

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/term`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create a term are listed here.

Schema: `termrequest`

<details>
<summary>Show schema for `termrequest`</summary>

#### termrequest

Model type: `object`

##### `Name`

Required: Required
Type: `String`

User recognizable name for the term. For example, `Net 30`.

##### `DayOfMonthDue`

Required: Conditionally required
Type: `Integer`
Max length: Range is 1 through 31

Payment must be received by this day of the month. Required if `DueDays` not present

##### `DueDays`

Required: Conditionally required
Type: `Integer`
Max length: Range is 0 through 999

Number of days from delivery of goods or services until the payment is due. Required if `DayOfMonthDue` not present

</details>

#### Example

```json
{
  "DueDays": "120",
  "Name": "Term120"
}
```

#### XML example

```xml
<Term xmlns="http://schema.intuit.com/finance/v3">
            <Name>Net 45</Name>
            <DueDays>45</DueDays>
</Term>
```

### Returns

Returns the newly created term object.

#### Example

```json
{
  "Term": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "Term120",
    "DiscountPercent": 0,
    "Type": "STANDARD",
    "sparse": false,
    "Active": true,
    "DueDays": 120,
    "Id": "8",
    "MetaData": {
      "CreateTime": "2015-07-28T08:50:59-07:00",
      "LastUpdatedTime": "2015-07-28T08:50:59-07:00"
    }
  },
  "time": "2015-07-28T08:51:00.627-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T08:48:33.773-07:00">
    <Term domain="QBO" sparse="false">
        <Id>7</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T08:48:32-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T08:48:32-07:00</LastUpdatedTime>
        </MetaData>
        <Name>Net 45</Name>
        <Active>true</Active>
        <Type>STANDARD</Type>
        <DiscountPercent>0</DiscountPercent>
        <DueDays>45</DueDays>
    </Term>
</IntuitResponse>
```

## Query a term

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Term"
```

#### XML example

```sql
select * from Term
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Term": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Due on receipt",
        "DiscountPercent": 0,
        "DiscountDays": 0,
        "Type": "STANDARD",
        "sparse": false,
        "Active": true,
        "DueDays": 0,
        "Id": "1",
        "MetaData": {
          "CreateTime": "2014-09-11T14:41:49-07:00",
          "LastUpdatedTime": "2014-09-11T14:41:49-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Net 10",
        "DiscountPercent": 0,
        "Type": "STANDARD",
        "sparse": false,
        "Active": true,
        "DueDays": 10,
        "Id": "5",
        "MetaData": {
          "CreateTime": "2014-09-16T15:24:26-07:00",
          "LastUpdatedTime": "2014-09-16T15:24:26-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Net 15",
        "DiscountPercent": 0,
        "DiscountDays": 0,
        "Type": "STANDARD",
        "sparse": false,
        "Active": true,
        "DueDays": 15,
        "Id": "2",
        "MetaData": {
          "CreateTime": "2014-09-11T14:41:49-07:00",
          "LastUpdatedTime": "2014-09-11T14:41:49-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Net 30",
        "DiscountPercent": 0,
        "DiscountDays": 0,
        "Type": "STANDARD",
        "sparse": false,
        "Active": true,
        "DueDays": 30,
        "Id": "3",
        "MetaData": {
          "CreateTime": "2014-09-11T14:41:49-07:00",
          "LastUpdatedTime": "2014-09-11T14:41:49-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "Name": "Net 60",
        "DiscountPercent": 0,
        "DiscountDays": 0,
        "Type": "STANDARD",
        "sparse": false,
        "Active": true,
        "DueDays": 60,
        "Id": "4",
        "MetaData": {
          "CreateTime": "2014-09-11T14:41:49-07:00",
          "LastUpdatedTime": "2014-09-11T14:41:49-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DayOfMonthDue": 1,
        "Name": "TermForV3Testing-1373590184130",
        "DiscountPercent": 0,
        "sparse": false,
        "Active": true,
        "Type": "DATE_DRIVEN",
        "Id": "6",
        "MetaData": {
          "CreateTime": "2015-01-29T08:27:32-08:00",
          "LastUpdatedTime": "2015-01-29T08:27:32-08:00"
        }
      }
    ],
    "maxResults": 6
  },
  "time": "2015-07-28T08:26:23.942-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T08:31:48.263-07:00">
    <QueryResponse startPosition="1" maxResults="6">
        <Term domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-11T14:41:49-07:00</CreateTime>
                <LastUpdatedTime>2014-09-11T14:41:49-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Due on receipt</Name>
            <Active>true</Active>
            <Type>STANDARD</Type>
            <DiscountPercent>0</DiscountPercent>
            <DueDays>0</DueDays>
            <DiscountDays>0</DiscountDays>
        </Term>
        <Term domain="QBO" sparse="false">
            <Id>5</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-16T15:24:26-07:00</CreateTime>
                <LastUpdatedTime>2014-09-16T15:24:26-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Net 10</Name>
            <Active>true</Active>
            <Type>STANDARD</Type>
            <DiscountPercent>0</DiscountPercent>
            <DueDays>10</DueDays>
        </Term>
        <Term domain="QBO" sparse="false">
            <Id>2</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-11T14:41:49-07:00</CreateTime>
                <LastUpdatedTime>2014-09-11T14:41:49-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Net 15</Name>
            <Active>true</Active>
            <Type>STANDARD</Type>
            <DiscountPercent>0</DiscountPercent>
            <DueDays>15</DueDays>
            <DiscountDays>0</DiscountDays>
        </Term>
        <Term domain="QBO" sparse="false">
            <Id>3</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-11T14:41:49-07:00</CreateTime>
                <LastUpdatedTime>2014-09-11T14:41:49-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Net 30</Name>
            <Active>true</Active>
            <Type>STANDARD</Type>
            <DiscountPercent>0</DiscountPercent>
            <DueDays>30</DueDays>
            <DiscountDays>0</DiscountDays>
        </Term>
        <Term domain="QBO" sparse="false">
            <Id>4</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-11T14:41:49-07:00</CreateTime>
                <LastUpdatedTime>2014-09-11T14:41:49-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Net 60</Name>
            <Active>true</Active>
            <Type>STANDARD</Type>
            <DiscountPercent>0</DiscountPercent>
            <DueDays>60</DueDays>
            <DiscountDays>0</DiscountDays>
        </Term>
        <Term domain="QBO" sparse="false">
            <Id>6</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-01-29T08:27:32-08:00</CreateTime>
                <LastUpdatedTime>2015-01-29T08:27:32-08:00</LastUpdatedTime>
            </MetaData>
            <Name>TermForV3Testing-1373590184130</Name>
            <Active>true</Active>
            <Type>DATE_DRIVEN</Type>
            <DiscountPercent>0</DiscountPercent>
            <DayOfMonthDue>1</DayOfMonthDue>
        </Term>
    </QueryResponse>
</IntuitResponse>
```

## Read a term

### Definition

- **Operation:** `GET /v3/company/<realmID>/term/<termId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Term object that has been previously created.

### Returns

Returns the term object.

#### Example

```json
{
  "Term": {
    "SyncToken": "0",
    "domain": "QBO",
    "Name": "Net 60",
    "DiscountPercent": 0,
    "DiscountDays": 0,
    "Type": "STANDARD",
    "sparse": false,
    "Active": true,
    "DueDays": 60,
    "Id": "4",
    "MetaData": {
      "CreateTime": "2014-09-11T14:41:49-07:00",
      "LastUpdatedTime": "2014-09-11T14:41:49-07:00"
    }
  },
  "time": "2015-07-28T08:52:57.63-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T08:53:15.475-07:00">
  <Term domain="QBO" sparse="false">
    <Id>4</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T14:41:49-07:00</CreateTime>
      <LastUpdatedTime>2014-09-11T14:41:49-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Net 60</Name>
    <Active>true</Active>
    <Type>STANDARD</Type>
    <DiscountPercent>0</DiscountPercent>
    <DueDays>60</DueDays>
    <DiscountDays>0</DiscountDays>
  </Term>
</IntuitResponse>
```

## Full update a term

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/term`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing Term object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `termrequest`

<details>
<summary>Show schema for `termrequest`</summary>

#### termrequest

Model type: `object`

##### `Name`

Required: Required
Type: `String`

User recognizable name for the term. For example, `Net 30`.

##### `DayOfMonthDue`

Required: Conditionally required
Type: `Integer`
Max length: Range is 1 through 31

Payment must be received by this day of the month. Required if `DueDays` not present

##### `DueDays`

Required: Conditionally required
Type: `Integer`
Max length: Range is 0 through 999

Number of days from delivery of goods or services until the payment is due. Required if `DayOfMonthDue` not present

</details>

#### Example

```json
{
  "SyncToken": "0",
  "domain": "QBO",
  "Name": "Net 30",
  "DiscountPercent": 0,
  "DiscountDays": 10,
  "Type": "STANDARD",
  "sparse": false,
  "Active": true,
  "DueDays": 30,
  "Id": "3",
  "MetaData": {
    "CreateTime": "2014-09-11T14:41:49-07:00",
    "LastUpdatedTime": "2014-09-11T14:41:49-07:00"
  }
}
```

#### XML example

```xml
<Term xmlns="http://schema.intuit.com/finance/v3" sparse="false">
    <Id>4</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T14:41:49-07:00</CreateTime>
      <LastUpdatedTime>2014-09-11T14:41:49-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Net 60</Name>
    <Active>true</Active>
    <Type>STANDARD</Type>
    <DiscountPercent>0</DiscountPercent>
    <DueDays>60</DueDays>
    <DiscountDays>10</DiscountDays>
</Term>
```

### Returns

The term response body.

#### Example

```json
{
  "Term": {
    "SyncToken": "1",
    "domain": "QBO",
    "Name": "Net 30",
    "DiscountPercent": 0,
    "DiscountDays": 10,
    "Type": "STANDARD",
    "sparse": false,
    "Active": true,
    "DueDays": 30,
    "Id": "3",
    "MetaData": {
      "CreateTime": "2014-09-11T14:41:49-07:00",
      "LastUpdatedTime": "2015-07-28T08:55:59-07:00"
    }
  },
  "time": "2015-07-28T08:55:59.916-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T08:54:40.563-07:00">
  <Term domain="QBO" sparse="false">
    <Id>4</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T14:41:49-07:00</CreateTime>
      <LastUpdatedTime>2015-07-28T08:54:40-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Net 60</Name>
    <Active>true</Active>
    <Type>STANDARD</Type>
    <DiscountPercent>0</DiscountPercent>
    <DueDays>60</DueDays>
    <DiscountDays>10</DiscountDays>
  </Term>
</IntuitResponse>
```
