# Budget

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/budget
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Budget
> Canonical entity: `Budget`

The Budget endpoint allows you to retrieve the current state of budgets already set up in the user's company file. A budget allows for an amount to be assigned on a monthly, quarterly, or annual basis for a specific account or customer and are created to give a business measurable expense goals. This amount represents how much should be spent against that account or customer in the give time period.

## The budget object

### budgetresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `EndDate`

Required: Required
Type: `DateTime`

Budget end date.

<details>
<summary>Child attributes for `EndDate`</summary>

##### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

#### `StartDate`

Required: Required
Type: `DateTime`

Budget begin date.

<details>
<summary>Child attributes for `StartDate`</summary>

##### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `BudgetEntryType`

Required: Optional
Type: `BudgetEntryTypeEnum`
Traits: read only

Period that this budget detail covers.. Valid values include: `Monthly`, `Quarterly`, `Annually`.

#### `Name`

Required: Optional
Type: `String`
Traits: read only, filterable, sortable

User recognizable name for the Account. `Account.Name` attribute must not contain double quotes (") or colon (:).

#### `BudgetDetail [0..n]`

Required: Optional
Type: `BudgetDetail`

Container for the budget items.

<details>
<summary>Child attributes for `BudgetDetail [0..n]`</summary>

##### budgetdetail

Model type: `object`

###### `ClassRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

Reference to the Class associated with the transaction. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

<details>
<summary>Child attributes for `ClassRef`</summary>

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

###### `DepartmentRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

A reference to a Department object specifying the location of the transaction, as defined using location tracking in QuickBooks Online. Query the Department name list resource to determine the appropriate department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

<details>
<summary>Child attributes for `DepartmentRef`</summary>

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

###### `Amount`

Required: Optional
Type: `BigDecimal`
Traits: read only

Amount assigned to a BudgetDetail.

###### `BudgetDate`

Required: Optional
Type: `DateTime`
Traits: read only

Date of the individual BudgetDetail.

<details>
<summary>Child attributes for `BudgetDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `AccountRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

Reference to the Account associated with this BudgetDetail. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType=Expense`. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively.

<details>
<summary>Child attributes for `AccountRef`</summary>

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

###### `CustomerRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

Reference to the Customer associated with this BudgetDetail. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

<details>
<summary>Child attributes for `CustomerRef`</summary>

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

#### `BudgetType`

Required: Optional
Type: `BudgetTypeEnum`
Traits: read only, filterable, sortable

Budget types. The only value currently supported is `ProfitAndLoss`.

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable
Default: true

Whether or not active inactive accounts may be hidden from most display purposes and may not be posted to.

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
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 1,
    "Budget": [
      {
        "StartDate": "2014-01-01",
        "BudgetEntryType": "Monthly",
        "EndDate": "2014-12-31",
        "Name": "Sandbox Budget",
        "SyncToken": "1",
        "BudgetType": "ProfitAndLoss",
        "domain": "QBO",
        "sparse": false,
        "Active": true,
        "BudgetDetail": [
          {
            "Amount": 0,
            "AccountRef": {
              "name": "Services",
              "value": "1"
            },
            "BudgetDate": "2014-01-01"
          },
          {
            "Amount": 0,
            "AccountRef": {
              "name": "Services",
              "value": "1"
            },
            "BudgetDate": "2014-02-01"
          },
          {
            "Amount": 71.0,
            "AccountRef": {
              "name": "Unapplied Cash Payment Income",
              "value": "87"
            },
            "BudgetDate": "2014-12-01"
          }
        ],
        "Id": "1",
        "MetaData": {
          "CreateTime": "2015-07-14T13:59:45-07:00",
          "LastUpdatedTime": "2015-07-14T13:59:59-07:00"
        }
      }
    ],
    "maxResults": 1
  },
  "time": "2015-07-14T14:14:07.394-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-14T14:17:29.138-07:00">
  <QueryResponse startPosition="1" maxResults="1" totalCount="1">
    <Budget domain="QBO" sparse="false">
      <Id>1</Id>
      <SyncToken>1</SyncToken>
      <MetaData>
        <CreateTime>2015-07-14T13:59:45-07:00</CreateTime>
        <LastUpdatedTime>2015-07-14T13:59:59-07:00</LastUpdatedTime>
      </MetaData>
      <Name>Sandbox Budget</Name>
      <StartDate>2014-01-01</StartDate>
      <EndDate>2014-12-31</EndDate>
      <BudgetType>ProfitAndLoss</BudgetType>
      <BudgetEntryType>Monthly</BudgetEntryType>
      <Active>true</Active>
      <BudgetDetail>
        <BudgetDate>2014-01-01</BudgetDate>
        <Amount>0</Amount>
        <AccountRef name="Services">1</AccountRef>
      </BudgetDetail>
      <BudgetDetail>
        <BudgetDate>2014-02-01</BudgetDate>
        <Amount>0</Amount>
        <AccountRef name="Services">1</AccountRef>
      </BudgetDetail>
...
      <BudgetDetail>
        <BudgetDate>2014-10-01</BudgetDate>
        <Amount>0</Amount>
        <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
      </BudgetDetail>
      <BudgetDetail>
        <BudgetDate>2014-11-01</BudgetDate>
        <Amount>0</Amount>
        <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
      </BudgetDetail>
      <BudgetDetail>
        <BudgetDate>2014-12-01</BudgetDate>
        <Amount>71.00</Amount>
        <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
      </BudgetDetail>
    </Budget>
  </QueryResponse>
</IntuitResponse>
```

## Create a budget

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/budget`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create an budget are listed here.

Schema: `budgetrequest`

<details>
<summary>Show schema for `budgetrequest`</summary>

#### budgetrequest

Model type: `object`

##### `EndDate`

Required: Required
Type: `DateTime`

Budget end date.

<details>
<summary>Child attributes for `EndDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

##### `StartDate`

Required: Required
Type: `DateTime`

Budget begin date.

<details>
<summary>Child attributes for `StartDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

##### `BudgetDetail [0..n]`

Required: Optional
Type: `BudgetDetail`

Container for the budget items.

<details>
<summary>Child attributes for `BudgetDetail [0..n]`</summary>

###### budgetdetail

Model type: `object`

###### `ClassRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

Reference to the Class associated with the transaction. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

<details>
<summary>Child attributes for `ClassRef`</summary>

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

###### `DepartmentRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

A reference to a Department object specifying the location of the transaction, as defined using location tracking in QuickBooks Online. Query the Department name list resource to determine the appropriate department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

<details>
<summary>Child attributes for `DepartmentRef`</summary>

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

###### `Amount`

Required: Optional
Type: `BigDecimal`
Traits: read only

Amount assigned to a BudgetDetail.

###### `BudgetDate`

Required: Optional
Type: `DateTime`
Traits: read only

Date of the individual BudgetDetail.

<details>
<summary>Child attributes for `BudgetDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `AccountRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

Reference to the Account associated with this BudgetDetail. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType=Expense`. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively.

<details>
<summary>Child attributes for `AccountRef`</summary>

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

###### `CustomerRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

Reference to the Customer associated with this BudgetDetail. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

<details>
<summary>Child attributes for `CustomerRef`</summary>

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

##### `BudgetEntryType`

Required: Optional
Type: `BudgetEntryTypeEnum`
Traits: read only

Period that this budget detail covers.. Valid values include: `Monthly`, `Quarterly`, `Annually`.

##### `Name`

Required: Optional
Type: `String`
Traits: read only, filterable, sortable

User recognizable name for the Account. `Account.Name` attribute must not contain double quotes (") or colon (:).

##### `BudgetType`

Required: Optional
Type: `BudgetTypeEnum`
Traits: read only, filterable, sortable

Budget types. The only value currently supported is `ProfitAndLoss`.

</details>

#### Example

```json
{
  "StartDate": "2024-01-01",
  "BudgetEntryType": "Quarterly",
  "EndDate": "2024-12-31",
  "Name": "MyBudget",
  "BudgetType": "ProfitAndLoss",
  "BudgetDetail": [
    {
      "Amount": 12.0,
      "CustomerRef": {
        "value": "2"
      },
      "AccountRef": {
        "value": "5"
      },
      "BudgetDate": "2024-01-01"
    }
  ]
}
```

### Returns

The budget response body.

#### Example

```json
{
  "Budget": {
    "StartDate": "2024-01-01",
    "BudgetEntryType": "Quarterly",
    "EndDate": "2024-12-31",
    "Name": "MyBudget",
    "SyncToken": "0",
    "BudgetType": "ProfitAndLoss",
    "domain": "QBO",
    "sparse": false,
    "Active": true,
    "BudgetDetail": [
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-01-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-02-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-03-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-04-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-05-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-06-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-07-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-08-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-09-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-10-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-11-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "CustomerRef": {
          "name": "Seabiscuit",
          "value": "2"
        },
        "BudgetDate": "2024-12-01"
      }
    ],
    "Id": "2",
    "MetaData": {
      "CreateTime": "2024-01-09T14:16:19-08:00",
      "LastUpdatedTime": "2024-01-09T14:19:04-08:00"
    }
  },
  "time": "2024-06-19T13:54:58.396-07:00"
}
```

## Delete a budget

### Definition

- **Operation:** `POST /v3/company/<realmID>/budget?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the budget object specified in the request body. Include a minimum of `budget.Id` and `budget.SyncToken` in the request body.

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
  "SyncToken": "4",
  "Id": "1"
}
```

### Returns

Returns the delete response.

#### Example

```json
{
  "time": "2021-08-05T15:17:32.161-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2021-08-05T15:19:39.782-07:00"/>
```

## Query a budget

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"Select * from Budget"
```

#### XML example

```sql
select * from Budget
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 1,
    "Budget": [
      {
        "StartDate": "2014-01-01",
        "BudgetEntryType": "Monthly",
        "EndDate": "2014-12-31",
        "Name": "Sandbox Budget",
        "SyncToken": "1",
        "BudgetType": "ProfitAndLoss",
        "domain": "QBO",
        "sparse": false,
        "Active": true,
        "BudgetDetail": [
          {
            "Amount": 0,
            "AccountRef": {
              "name": "Services",
              "value": "1"
            },
            "BudgetDate": "2014-01-01"
          },
          {
            "Amount": 0,
            "AccountRef": {
              "name": "Services",
              "value": "1"
            },
            "BudgetDate": "2014-02-01"
          },
          {
            "Amount": 71.0,
            "AccountRef": {
              "name": "Unapplied Cash Payment Income",
              "value": "87"
            },
            "BudgetDate": "2014-12-01"
          }
        ],
        "Id": "1",
        "MetaData": {
          "CreateTime": "2015-07-14T13:59:45-07:00",
          "LastUpdatedTime": "2015-07-14T13:59:59-07:00"
        }
      }
    ],
    "maxResults": 1
  },
  "time": "2015-07-14T14:14:07.394-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-14T14:17:29.138-07:00">
  <QueryResponse startPosition="1" maxResults="1" totalCount="1">
    <Budget domain="QBO" sparse="false">
      <Id>1</Id>
      <SyncToken>1</SyncToken>
      <MetaData>
        <CreateTime>2015-07-14T13:59:45-07:00</CreateTime>
        <LastUpdatedTime>2015-07-14T13:59:59-07:00</LastUpdatedTime>
      </MetaData>
      <Name>Sandbox Budget</Name>
      <StartDate>2014-01-01</StartDate>
      <EndDate>2014-12-31</EndDate>
      <BudgetType>ProfitAndLoss</BudgetType>
      <BudgetEntryType>Monthly</BudgetEntryType>
      <Active>true</Active>
      <BudgetDetail>
        <BudgetDate>2014-01-01</BudgetDate>
        <Amount>0</Amount>
        <AccountRef name="Services">1</AccountRef>
      </BudgetDetail>
      <BudgetDetail>
        <BudgetDate>2014-02-01</BudgetDate>
        <Amount>0</Amount>
        <AccountRef name="Services">1</AccountRef>
      </BudgetDetail>
...
      <BudgetDetail>
        <BudgetDate>2014-10-01</BudgetDate>
        <Amount>0</Amount>
        <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
      </BudgetDetail>
      <BudgetDetail>
        <BudgetDate>2014-11-01</BudgetDate>
        <Amount>0</Amount>
        <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
      </BudgetDetail>
      <BudgetDetail>
        <BudgetDate>2014-12-01</BudgetDate>
        <Amount>71.00</Amount>
        <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
      </BudgetDetail>
    </Budget>
  </QueryResponse>
</IntuitResponse>
```

## Read a budget

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/budget/<budgetId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a budget that has been previously created.

### Returns

The budget response body.

#### Example

```json
{
  "Budget": {
    "StartDate": "2014-01-01",
    "BudgetEntryType": "Quarterly",
    "EndDate": "2014-12-31",
    "Name": "MyBudget",
    "SyncToken": "9",
    "BudgetType": "ProfitAndLoss",
    "domain": "QBO",
    "sparse": false,
    "Active": true,
    "BudgetDetail": [
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-01-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-02-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-03-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-04-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-05-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-06-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-07-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-08-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-09-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-10-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-11-01"
      },
      {
        "Amount": 12.0,
        "AccountRef": {
          "name": "Fees Billed",
          "value": "5"
        },
        "BudgetDate": "2014-12-01"
      }
    ],
    "Id": "2",
    "MetaData": {
      "CreateTime": "2014-01-09T14:16:19-08:00",
      "LastUpdatedTime": "2014-01-09T14:19:04-08:00"
    }
  },
  "time": "2014-06-19T13:54:58.396-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2021-08-04T23:26:15.827-07:00">
        <Budget domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>2</SyncToken>
            <MetaData>
                <CreateTime>2021-08-04T15:31:01-07:00</CreateTime>
                <LastUpdatedTime>2021-08-04T15:31:06-07:00</LastUpdatedTime>
            </MetaData>
            <Name>b1</Name>
            <StartDate>2021-01-01</StartDate>
            <EndDate>2021-12-31</EndDate>
            <BudgetType>ProfitAndLoss</BudgetType>
            <BudgetEntryType>Monthly</BudgetEntryType>
            <Active>true</Active>
            <BudgetDetail>
                <BudgetDate>2021-01-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-02-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-03-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-04-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-05-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-06-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-07-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-08-01</BudgetDate>
                <Amount>88.00</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-09-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-10-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-11-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
            <BudgetDetail>
                <BudgetDate>2021-12-01</BudgetDate>
                <Amount>0</Amount>
                <AccountRef name="Landscaping Services">45</AccountRef>
            </BudgetDetail>
        </Budget>
</IntuitResponse>
```

## Full update a budget

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/budget`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing budget object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `budgetresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "3",
  "BudgetEntryType": "Monthly",
  "EndDate": "2015-12-31",
  "Name": "New",
  "StartDate": "2015-01-01",
  "BudgetType": "ProfitAndLoss",
  "Active": "true",
  "BudgetDetail": [
    {
      "Amount": "7.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-01-01"
    },
    {
      "Amount": "22.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-02-01"
    },
    {
      "Amount": "1100.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-03-01"
    },
    {
      "Amount": "100.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-04-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-05-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-06-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-07-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-08-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-09-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-10-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-11-01"
    },
    {
      "Amount": "1500.00",
      "AccountRef": {
        "type": "String",
        "name": "Fees Billed",
        "value": "5"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-12-01"
    },
    {
      "Amount": "30.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-01-01"
    },
    {
      "Amount": "22.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-02-01"
    },
    {
      "Amount": "1100.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-03-01"
    },
    {
      "Amount": "100.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-04-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-05-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-06-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-07-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-08-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-09-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-10-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-11-01"
    },
    {
      "Amount": "800.00",
      "AccountRef": {
        "type": "String",
        "name": "Refunds-Allowances",
        "value": "6"
      },
      "CustomerRef": {
        "type": "String",
        "name": "Fazil",
        "value": "3"
      },
      "BudgetDate": "2015-12-01"
    }
  ],
  "Id": "21"
}
```

### Returns

The budget response body.

#### Example

```text
""
```

#### XML example

```text
"Sample XML response not available."
```
