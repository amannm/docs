# TimeActivity

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/timeactivity
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / TimeActivity
> Canonical entity: `TimeActivity`

The TimeActivity object represents a record of time worked by a vendor or employee.

## The TimeActivity object

### timeactivityresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `NameOf`

Required: Required
Type: `String`

Enumeration of time activity types. Required in conjunction with either `EmployeeRef`or `VendorRef`attributes for create operations. Valid values: `Vendor`or `Employee`.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `TxnDate`

Required: Conditionally required
Type: `Date`
Traits: filterable, sortable
Default: Current server date

The date for the time activity. This is the posting date that affects financial statements. If the date is not supplied, the current date on the server is used. Sort order is ASC by default. If you provide the StartTime and EndTime without including the timeZone offset, then you would need to pass the TxnDate for any historical or future dates. Lets say if you want to create a historical time activity then pass the TxnDate as the date and pass StartTime and EndTime as Hours without including the timeZone offset.

<details>
<summary>Child attributes for `TxnDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `BreakHours BreakMinutes`

Required: Conditionally required
Type: `Integer`
Max length: Maximum of 8760 hours
59 minutes; if hours is 8760
minutes must be 0

Hours and minutes of break taken between `StartTime` and `EndTime`. use when StartTime and `EndTime` are specified

#### `EndTime`

Required: Conditionally required
Type: `DateTime`

Time that work starts and ends, respectively. Required if `Hours` and `Minutes` not specified. Note: Kindly consider only the Hours without including the timeZone offset as it does not impact time activity hours calculation.

<details>
<summary>Child attributes for `EndTime`</summary>

##### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

#### `Hours`

Required: Conditionally required
Type: `Integer`
Max length: Maximum of 8760 hours
59 minutes; If hours is 8760
minutes must be 0

Hours and minutes worked. Required if `StartTime` and `EndTime` not specified

#### `VendorRef`

Required: Conditionally required
Type: `ReferenceType`

Specifies the vendor whose time is being recorded. Query the Vendor name list resource to determine the appropriate Vendor object for this reference. Use `Vendor.Id` and `Vendor.Name` from that object for `VendorRef.value` and `VendorRef.name`, respectively. Required if `NameOf` is set to `Vendor`

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

#### `ProjectRef`

Required: Conditionally required
Type: `ReferenceType`
Traits: filterable
Minor version: 69

Reference to the `Project` ID associated with this transaction. Available with Minor Version 69 and above

<details>
<summary>Child attributes for `ProjectRef`</summary>

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

#### `HourlyRate`

Required: Conditionally required
Type: `Decimal`
Max length: 0 to 99999999999 hours
Default: 0

Hourly bill rate of the employee or vendor for this time activity. Required if `BillableStatus` is set to `Billable`

#### `CustomerRef`

Required: Conditionally required
Type: `ReferenceType`

Reference to a customer or job. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively. Required if `BillableStatus` is set to `Billable`

<details>
<summary>Child attributes for `CustomerRef`</summary>

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

#### `EmployeeRef`

Required: Conditionally required
Type: `ReferenceType`

Specifies the employee whose time is being recorded. Query the Employee name list resource to determine the appropriate Employee object for this reference. Use `Employee.Id` and `Employee.DisplayName` from that object for `EmployeerRef.value` and `EmployeeRef.Name`, respectively. Required if `NameOf` is set to `Employee`

<details>
<summary>Child attributes for `EmployeeRef`</summary>

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

#### `StartTime`

Required: Conditionally required
Type: `DateTime`

Time that work starts and ends, respectively. Required if `Hours` and `Minutes` not specified. Note: Kindly consider only the Hours without including the timeZone offset as it does not impact time activity hours calculation.

<details>
<summary>Child attributes for `StartTime`</summary>

##### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

#### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with this object. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerTxn` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

<details>
<summary>Child attributes for `ClassRef`</summary>

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

#### `Description`

Required: Optional
Type: `String`
Max length: maximum 4000 characters

Description of work completed during time activity.

#### `Taxable`

Required: Optional
Type: `Boolean`
Default: <span class="literal">false</span>

True if the time recorded is both billable and taxable.

#### `TransactionLocationType`

Required: Optional
Type: `String`
Default: WithinFrance
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

#### `CostRate`

Required: Optional
Type: `BigDecimal`

Pay rate of the employee or vendor for this time activity.

#### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to the service item associated with this object. Query the Item name list resource, where `Item.Type` is set to `Service`, to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively. For France locales: The account associated with the referenced Item object is looked up in the account category list.

If this account has same location as specified in the transaction by the `TransactionLocationType` attribute and the same VAT as in the line item `TaxCodeRef` attribute, then the item account is used.

If there is a mismatch, then the account from the account category list that matches the transaction location and VAT is used.

If this account is not present in the account category list, then a new account is created with the new location, new VAT code, and all other attributes as in the default account.

<details>
<summary>Child attributes for `ItemRef`</summary>

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

#### `PayrollItemRef`

Required: Optional
Type: `ReferenceType`

Specifies how much the employee should be paid for doing the work specified by the Compensation Id. Query the EmployeeCompensation resource to determine the appropriate PayrollCompensation object for an employee. Use `EmployeeCompensation.Id` and `EmployerCompensation.Name` from that object for `PayrollItemRef.value` and `PayrollItemRef.name`, respectively. This field is available only for a closed group of developers.

<details>
<summary>Child attributes for `PayrollItemRef`</summary>

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

#### `BillableStatus`

Required: Optional
Type: `BillableStatusEnum`
Traits: read only, filterable
Default: <span class="literal">NotBillable</span>

Billable status of the time recorded. This field is not updatable through an API request. The value automatically changes when an invoice is created. Valid values: `Billable`, `NotBillable`, `HasBeenBilled`. You cannot directly update the status to `HasBeenBilled`. To set the status to `HasBeenBilled`, create an Invoice object and attach this TimeActivity object as a linked transaction to that Invoice.

#### `DepartmentRef`

Required: Optional
Type: `ReferenceType`

A reference to a Department object specifying the location of this object. Available if `Preferences.AccountingInfoPrefs.TrackDepartments` is set to `true`.
Query the Department name list resource to determine the appropriate department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

<details>
<summary>Child attributes for `DepartmentRef`</summary>

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

#### Example

```json
{
  "TimeActivity": {
    "TxnDate": "2014-09-17",
    "domain": "QBO",
    "NameOf": "Employee",
    "Description": "Garden Lighting",
    "ItemRef": {
      "name": "Lighting",
      "value": "8"
    },
    "Minutes": 0,
    "ProjectRef": {
      "value": "39298045"
    },
    "Hours": 3,
    "BillableStatus": "HasBeenBilled",
    "sparse": false,
    "HourlyRate": 15,
    "Taxable": false,
    "EmployeeRef": {
      "name": "Emily Platt",
      "value": "55"
    },
    "SyncToken": "0",
    "CustomerRef": {
      "name": "Rondonuwu Fruit and Vegi",
      "value": "21"
    },
    "Id": "5",
    "MetaData": {
      "CreateTime": "2014-09-17T11:55:25-07:00",
      "LastUpdatedTime": "2014-09-18T13:45:12-07:00"
    }
  },
  "time": "2015-07-28T10:35:07.663-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T10:34:50.450-07:00">
  <TimeActivity domain="QBO" sparse="false">
    <Id>5</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-17T11:55:25-07:00</CreateTime>
      <LastUpdatedTime>2014-09-18T13:45:12-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-09-17</TxnDate>
    <NameOf>Employee</NameOf>
    <EmployeeRef name="Emily Platt">55</EmployeeRef>
    <CustomerRef name="Rondonuwu Fruit and Vegi">21</CustomerRef>
    <ProjectRef>39298045</ProjectRef>
    <ItemRef name="Lighting">8</ItemRef>
    <BillableStatus>HasBeenBilled</BillableStatus>
    <Taxable>false</Taxable>
    <HourlyRate>15</HourlyRate>
    <Hours>3</Hours>
    <Minutes>0</Minutes>
    <Description>Garden Lighting</Description>
  </TimeActivity>
</IntuitResponse>
```

## Create a timeactivity object

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/timeactivity`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create a TimeActivity object are listed here.

Schema: `timeactivityrequest`

<details>
<summary>Show schema for `timeactivityrequest`</summary>

#### timeactivityrequest

Model type: `object`

##### `NameOf`

Required: Required
Type: `String`

Enumeration of time activity types. Required in conjunction with either `EmployeeRef`or `VendorRef`attributes for create operations. Valid values: `Vendor`or `Employee`.

##### `TxnDate`

Required: Conditionally required
Type: `Date`
Traits: filterable, sortable
Default: Current server date

The date for the time activity. This is the posting date that affects financial statements. If the date is not supplied, the current date on the server is used. Sort order is ASC by default. If you provide the StartTime and EndTime without including the timeZone offset, then you would need to pass the TxnDate for any historical or future dates. Lets say if you want to create a historical time activity then pass the TxnDate as the date and pass StartTime and EndTime as Hours without including the timeZone offset.

<details>
<summary>Child attributes for `TxnDate`</summary>

###### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

##### `ProjectRef`

Required: Conditionally required
Type: `ReferenceType`
Minor version: 69

Reference to the `Project` ID associated with this transaction. Available with Minor Version 69 and above

<details>
<summary>Child attributes for `ProjectRef`</summary>

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

##### `Hours`

Required: Conditionally required
Type: `Integer`
Max length: Maximum of 8760 hours
59 minutes; if hours is 8760
minutes must be 0

Hours and minutes worked. Required if `StartTime` and `EndTime` not specified

##### `StartTime`

Required: Conditionally required
Type: `DateTime`

Time that work starts. Required if `Hours` and `Minutes` not specified. Note: Kindly consider only the Hours without including the timeZone offset as it does not impact time activity hours calculation.

If `TnxDate` is provided then consider passing the `StartTime` and `EndTime` wihtout including the timeZone offset, then the the date passed on the TxnDate is used.

If `TnxDate` is NOT provided, passing the `StartTime` and `EndTime` with/wihtout including the timeZone offset, then the the current date on the server is used.

For any transactions with historical/future dates kindly include TxnDate in YYYY-MM-DD format and StartTime and EndTime in Hours and Minutes

<details>
<summary>Child attributes for `StartTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

##### `HourlyRate`

Required: Conditionally required
Type: `Decimal`
Max length: 0 to 99999999999 hours
Default: 0

Hourly bill rate of the employee or vendor for this time activity. Required if `BillableStatus` is set to `Billable`

##### `VendorRef`

Required: Conditionally required
Type: `ReferenceType`

Specifies the vendor whose time is being recorded. Query the Vendor name list resource to determine the appropriate Vendor object for this reference. Use `Vendor.Id` and `Vendor.Name` from that object for `VendorRef.value` and `VendorRef.name`, respectively.

<details>
<summary>Child attributes for `VendorRef`</summary>

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

##### `EndTime`

Required: Conditionally required
Type: `DateTime`

Time that work ends. Required if `Hours` and `Minutes` not specified. Note: Kindly consider only the Hours without including the timeZone offset as it does not impact time activity hours calculation.

If `TnxDate` is provided then consider passing the `StartTime` and `EndTime` wihtout including the timeZone offset, then the the date passed on the TxnDate is used.

If `TnxDate` is NOT provided, passing the `StartTime` and `EndTime` with/wihtout including the timeZone offset, then the the current date on the server is used.

For any transactions with historical/future dates kindly include TxnDate in YYYY-MM-DD format and StartTime and EndTime in Hours and Minutes

<details>
<summary>Child attributes for `EndTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

##### `EmployeeRef`

Required: Condtionally required
Type: `ReferenceType`

Specifies the employee whose time is being recorded. Query the Employee name list resource to determine the appropriate Employee object for this reference. Use `Employee.Id` and `Employee.DisplayName` from that object for `EmployeerRef.value` and `EmployeeRef.Name`, respectively.

<details>
<summary>Child attributes for `EmployeeRef`</summary>

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

##### `CustomerRef`

Type: `ReferenceType`

Reference to a customer or job. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

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

#### Example

```json
{
  "TxnDate": "2021-02-02",
  "EndTime": "17:00:00-08:00",
  "EmployeeRef": {
    "name": "Emily Platt",
    "value": "55"
  },
  "StartTime": "08:00:00-08:00",
  "NameOf": "Employee"
}
```

#### XML example

```xml
<TimeActivity xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
   <NameOf>Employee</NameOf>
   <EmployeeRef name="Emily Platt">55</EmployeeRef>
   <StartTime>2015-07-06T08:00:00-08:00</StartTime>
   <EndTime>2015-07-06T17:00:00-08:00</EndTime>
</TimeActivity>
```

### Returns

The TimeActivity response body.

#### Example

```json
{
  "TimeActivity": {
    "TxnDate": "2015-07-28",
    "domain": "QBO",
    "NameOf": "Employee",
    "sparse": false,
    "ItemRef": {
      "name": "Hours",
      "value": "2"
    },
    "ProjectRef": {
      "value": "39298034"
    },
    "BillableStatus": "NotBillable",
    "StartTime": "2015-07-28T09:00:00-07:00",
    "HourlyRate": 0,
    "Taxable": false,
    "EmployeeRef": {
      "name": "Emily Platt",
      "value": "55"
    },
    "EndTime": "2015-07-28T18:00:00-07:00",
    "CustomerRef": {
      "name": "Cool Cars",
      "value": "3"
    },
    "Id": "6",
    "SyncToken": "0",
    "MetaData": {
      "CreateTime": "2015-07-28T10:26:25-07:00",
      "LastUpdatedTime": "2015-07-28T10:26:25-07:00"
    }
  },
  "time": "2015-07-28T10:26:26.952-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T10:30:43.457-07:00">
  <TimeActivity domain="QBO" sparse="false">
    <Id>7</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-28T10:30:41-07:00</CreateTime>
      <LastUpdatedTime>2015-07-28T10:30:41-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-07-28</TxnDate>
    <NameOf>Employee</NameOf>
    <EmployeeRef name="Emily Platt">55</EmployeeRef>
    <CustomerRef name="Cool Cars">3</CustomerRef>
    <ProjectRef>39298034</ProjectRef>
    <ItemRef name="Hours">2</ItemRef>
    <BillableStatus>NotBillable</BillableStatus>
    <Taxable>false</Taxable>
    <HourlyRate>0</HourlyRate>
    <StartTime>2015-07-28T09:00:00-07:00</StartTime>
    <EndTime>2015-07-28T18:00:00-07:00</EndTime>
  </TimeActivity>
</IntuitResponse>
```

## Delete a timeactivity object

### Definition

- **Operation:** `POST /v3/company/<realmID>/timeactivity?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the TimeActivity object specified in the request body. Include a minimum of `TimeActivity.Id` and `TimeActivity.SyncToken` in the request body.

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
  "SyncToken": "0",
  "Id": "5"
}
```

#### XML example

```xml
<TimeActivity xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
   <Id>2</Id>
   <SyncToken>0</SyncToken>
</TimeActivity>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "TimeActivity": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "5"
  },
  "time": "2015-05-27T10:37:58.279-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T10:33:55.840-07:00">
    <TimeActivity domain="QBO" status="Deleted">
        <Id>7</Id>
    </TimeActivity>
</IntuitResponse>
```

## Query a timeactivity object

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from TimeActivity where TxnDate > '2014-09-14'"
```

#### XML example

```sql
select * from TimeActivity where TxnDate > '2014-09-14'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "TimeActivity": [
      {
        "TxnDate": "2014-09-17",
        "domain": "QBO",
        "NameOf": "Employee",
        "Description": "Garden Lighting",
        "ItemRef": {
          "name": "Lighting",
          "value": "8"
        },
        "Minutes": 0,
        "ProjectRef": {
          "value": "39298045"
        },
        "Hours": 3,
        "BillableStatus": "HasBeenBilled",
        "sparse": false,
        "HourlyRate": 15,
        "Taxable": false,
        "EmployeeRef": {
          "name": "Emily Platt",
          "value": "55"
        },
        "SyncToken": "0",
        "CustomerRef": {
          "name": "Rondonuwu Fruit and Vegi",
          "value": "21"
        },
        "Id": "5",
        "MetaData": {
          "CreateTime": "2014-09-17T11:55:25-07:00",
          "LastUpdatedTime": "2014-09-18T13:45:12-07:00"
        }
      },
      {
        "TxnDate": "2014-09-17",
        "domain": "QBO",
        "NameOf": "Employee",
        "Description": "Tree and Shrub Trimming",
        "ItemRef": {
          "name": "Trimming",
          "value": "18"
        },
        "Minutes": 0,
        "ProjectRef": {
          "value": "39298045"
        },
        "Hours": 2,
        "BillableStatus": "HasBeenBilled",
        "sparse": false,
        "HourlyRate": 15,
        "Taxable": false,
        "EmployeeRef": {
          "name": "Emily Platt",
          "value": "55"
        },
        "SyncToken": "0",
        "CustomerRef": {
          "name": "Rondonuwu Fruit and Vegi",
          "value": "21"
        },
        "Id": "4",
        "MetaData": {
          "CreateTime": "2014-09-17T11:54:02-07:00",
          "LastUpdatedTime": "2014-09-18T13:45:12-07:00"
        }
      },
      {
        "TxnDate": "2014-09-16",
        "domain": "QBO",
        "NameOf": "Employee",
        "Description": "Custom Design",
        "ItemRef": {
          "name": "Design",
          "value": "4"
        },
        "Minutes": 0,
        "ProjectRef": {
          "value": "39298003"
        },
        "Hours": 5,
        "BillableStatus": "Billable",
        "sparse": false,
        "HourlyRate": 75,
        "Taxable": false,
        "EmployeeRef": {
          "name": "John Johnson",
          "value": "54"
        },
        "SyncToken": "0",
        "CustomerRef": {
          "name": "Amy's Bird Sanctuary",
          "value": "1"
        },
        "Id": "3",
        "MetaData": {
          "CreateTime": "2014-09-17T11:53:15-07:00",
          "LastUpdatedTime": "2014-09-17T11:53:15-07:00"
        }
      },
      {
        "TxnDate": "2014-09-17",
        "domain": "QBO",
        "NameOf": "Employee",
        "Description": "Gardening",
        "ItemRef": {
          "name": "Hours",
          "value": "2"
        },
        "Minutes": 0,
        "ProjectRef": {
          "value": "39298003"
        },
        "Hours": 4,
        "BillableStatus": "NotBillable",
        "sparse": false,
        "HourlyRate": 0,
        "Taxable": false,
        "EmployeeRef": {
          "name": "John Johnson",
          "value": "54"
        },
        "SyncToken": "0",
        "CustomerRef": {
          "name": "Amy's Bird Sanctuary",
          "value": "1"
        },
        "Id": "2",
        "MetaData": {
          "CreateTime": "2014-09-17T11:47:12-07:00",
          "LastUpdatedTime": "2014-09-17T11:47:12-07:00"
        }
      }
    ],
    "maxResults": 4
  },
  "time": "2015-07-28T10:01:35.141-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T10:00:55.580-07:00">
    <QueryResponse startPosition="1" maxResults="4">
        <TimeActivity domain="QBO" sparse="false">
            <Id>5</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-17T11:55:25-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T13:45:12-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-09-17</TxnDate>
            <NameOf>Employee</NameOf>
            <EmployeeRef name="Emily Platt">55</EmployeeRef>
            <CustomerRef name="Rondonuwu Fruit and Vegi">21</CustomerRef>
            <ItemRef name="Lighting">8</ItemRef>
            <BillableStatus>HasBeenBilled</BillableStatus>
            <Taxable>false</Taxable>
            <HourlyRate>15</HourlyRate>
            <Hours>3</Hours>
            <Minutes>0</Minutes>
            <Description>Garden Lighting</Description>
        </TimeActivity>
        <TimeActivity domain="QBO" sparse="false">
            <Id>4</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-17T11:54:02-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T13:45:12-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-09-17</TxnDate>
            <NameOf>Employee</NameOf>
            <EmployeeRef name="Emily Platt">55</EmployeeRef>
            <CustomerRef name="Rondonuwu Fruit and Vegi">21</CustomerRef>
            <ProjectRef>39298045</ProjectRef>
            <ItemRef name="Trimming">18</ItemRef>
            <BillableStatus>HasBeenBilled</BillableStatus>
            <Taxable>false</Taxable>
            <HourlyRate>15</HourlyRate>
            <Hours>2</Hours>
            <Minutes>0</Minutes>
            <Description>Tree and Shrub Trimming</Description>
        </TimeActivity>
        <TimeActivity domain="QBO" sparse="false">
            <Id>3</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-17T11:53:15-07:00</CreateTime>
                <LastUpdatedTime>2014-09-17T11:53:15-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-09-16</TxnDate>
            <NameOf>Employee</NameOf>
            <EmployeeRef name="John Johnson">54</EmployeeRef>
            <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
            <ProjectRef>39298003</ProjectRef>
            <ItemRef name="Design">4</ItemRef>
            <BillableStatus>Billable</BillableStatus>
            <Taxable>false</Taxable>
            <HourlyRate>75</HourlyRate>
            <Hours>5</Hours>
            <Minutes>0</Minutes>
            <Description>Custom Design</Description>
        </TimeActivity>
        <TimeActivity domain="QBO" sparse="false">
            <Id>2</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-17T11:47:12-07:00</CreateTime>
                <LastUpdatedTime>2014-09-17T11:47:12-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-09-17</TxnDate>
            <NameOf>Employee</NameOf>
            <EmployeeRef name="John Johnson">54</EmployeeRef>
            <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
            <ProjectRef>39298003</ProjectRef>
            <ItemRef name="Hours">2</ItemRef>
            <BillableStatus>NotBillable</BillableStatus>
            <Taxable>false</Taxable>
            <HourlyRate>0</HourlyRate>
            <Hours>4</Hours>
            <Minutes>0</Minutes>
            <Description>Gardening</Description>
        </TimeActivity>
    </QueryResponse>
</IntuitResponse>
```

## Read a timeactivity object

### Definition

- **Operation:** `GET /v3/company/<realmID>/timeactivity/<timeactivityId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a TimeActivity object that has been previously created.

### Returns

The TimeActivity response body.

#### Example

```json
{
  "TimeActivity": {
    "TxnDate": "2014-09-17",
    "domain": "QBO",
    "NameOf": "Employee",
    "Description": "Garden Lighting",
    "ItemRef": {
      "name": "Lighting",
      "value": "8"
    },
    "Minutes": 0,
    "ProjectRef": {
      "value": "39298045"
    },
    "Hours": 3,
    "BillableStatus": "HasBeenBilled",
    "sparse": false,
    "HourlyRate": 15,
    "Taxable": false,
    "EmployeeRef": {
      "name": "Emily Platt",
      "value": "55"
    },
    "SyncToken": "0",
    "CustomerRef": {
      "name": "Rondonuwu Fruit and Vegi",
      "value": "21"
    },
    "Id": "5",
    "MetaData": {
      "CreateTime": "2014-09-17T11:55:25-07:00",
      "LastUpdatedTime": "2014-09-18T13:45:12-07:00"
    }
  },
  "time": "2015-07-28T10:35:07.663-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T10:34:50.450-07:00">
  <TimeActivity domain="QBO" sparse="false">
    <Id>5</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-09-17T11:55:25-07:00</CreateTime>
      <LastUpdatedTime>2014-09-18T13:45:12-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-09-17</TxnDate>
    <NameOf>Employee</NameOf>
    <EmployeeRef name="Emily Platt">55</EmployeeRef>
    <CustomerRef name="Rondonuwu Fruit and Vegi">21</CustomerRef>
    <ProjectRef>39298045</ProjectRef>
    <ItemRef name="Lighting">8</ItemRef>
    <BillableStatus>HasBeenBilled</BillableStatus>
    <Taxable>false</Taxable>
    <HourlyRate>15</HourlyRate>
    <Hours>3</Hours>
    <Minutes>0</Minutes>
    <Description>Garden Lighting</Description>
  </TimeActivity>
</IntuitResponse>
```

## Full update a timeactivity object

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/timeactivity`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing TimeActivity object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `timeactivityresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "TxnDate": "2014-09-16",
  "domain": "QBO",
  "NameOf": "Employee",
  "Description": "Updated descirption",
  "ItemRef": {
    "name": "Design",
    "value": "4"
  },
  "Minutes": 0,
  "ProjectRef": {
    "value": "39298005"
  },
  "Hours": 5,
  "BillableStatus": "Billable",
  "sparse": false,
  "HourlyRate": 75,
  "Taxable": false,
  "EmployeeRef": {
    "name": "John Johnson",
    "value": "54"
  },
  "SyncToken": "0",
  "CustomerRef": {
    "name": "Amy's Bird Sanctuary",
    "value": "1"
  },
  "Id": "3",
  "MetaData": {
    "CreateTime": "2014-09-17T11:53:15-07:00",
    "LastUpdatedTime": "2014-09-17T11:53:15-07:00"
  }
}
```

#### XML example

```xml
<TimeActivity xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
            <Id>3</Id>
            <SyncToken>1</SyncToken>
            <MetaData>
                <CreateTime>2014-09-17T11:53:15-07:00</CreateTime>
                <LastUpdatedTime>2014-09-17T11:53:15-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-09-16</TxnDate>
            <NameOf>Employee</NameOf>
            <EmployeeRef name="John Johnson">54</EmployeeRef>
            <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
            <ProjectRef>39298005</ProjectRef>
            <ItemRef name="Design">4</ItemRef>
            <BillableStatus>Billable</BillableStatus>
            <Taxable>false</Taxable>
            <HourlyRate>75</HourlyRate>
            <Hours>5</Hours>
            <Minutes>0</Minutes>
            <Description>Another description</Description>
</TimeActivity>
```

### Returns

The timeactivity response body.

#### Example

```json
{
  "TimeActivity": {
    "TxnDate": "2014-09-16",
    "domain": "QBO",
    "NameOf": "Employee",
    "Description": "Updated descirption",
    "ItemRef": {
      "name": "Design",
      "value": "4"
    },
    "Minutes": 0,
    "ProjectRef": {
      "value": "39298005"
    },
    "Hours": 5,
    "BillableStatus": "Billable",
    "sparse": false,
    "HourlyRate": 75,
    "Taxable": false,
    "EmployeeRef": {
      "name": "John Johnson",
      "value": "54"
    },
    "SyncToken": "1",
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "Id": "3",
    "MetaData": {
      "CreateTime": "2014-09-17T11:53:15-07:00",
      "LastUpdatedTime": "2015-07-28T11:59:41-07:00"
    }
  },
  "time": "2015-07-28T11:59:41.178-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T12:06:20.947-07:00">
  <TimeActivity domain="QBO" sparse="false">
    <Id>3</Id>
    <SyncToken>2</SyncToken>
    <MetaData>
      <CreateTime>2014-09-17T11:53:15-07:00</CreateTime>
      <LastUpdatedTime>2015-07-28T12:06:21-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-09-16</TxnDate>
    <NameOf>Employee</NameOf>
    <EmployeeRef name="John Johnson">54</EmployeeRef>
    <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
    <ProjectRef>39298045</ProjectRef>
    <ItemRef name="Design">4</ItemRef>
    <BillableStatus>Billable</BillableStatus>
    <Taxable>false</Taxable>
    <HourlyRate>75</HourlyRate>
    <Hours>5</Hours>
    <Minutes>0</Minutes>
    <Description>Another description</Description>
  </TimeActivity>
</IntuitResponse>
```
