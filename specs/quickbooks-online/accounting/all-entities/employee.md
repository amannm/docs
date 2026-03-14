# Employee

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/employee
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Employee
> Canonical entity: `Employee`

An Employee object represents a person working for the company. If you are looking to create a Contractor via API, refer how to create a Vendor object, with Vendor1099 field set to true.

- The `DisplayName`, `Title`, `GivenName`, `MiddleName`, `FamilyName`, `Suffix`, and `PrintOnCheckName` attributes must not contain colon (:), tab (\t), or newline (\n) characters.
- The `DisplayName` attribute must be unique across all other customer, employee, and vendor objects.
- The `GivenName` and `FamilyName` attributes are required.
- The `PrimaryEmailAddress` attribute must contain an at sign (@) and dot (.).

The full complement of read, create, delete via deactivation (`active=false`), and update operations are available both with and without QuickBooks Payroll enabled. However, when Payroll is enabled, support for some attributes is limited:

- `Title`—Not supported when QuickBooks Payroll is enabled.
- `Suffix`—Not supported when QuickBooks Payroll is enabled.
- `DisplayName` —It’s read only when QuickBooks Payroll is enabled and a concatenation of `GivenName` `MiddleName` `FamilyName`.
- `PrintOnCheckName`—Not supported when QuickBooks Payroll is enabled.
- `BillRate`—Not supported when QuickBooks Payroll is enabled.
- `SSN`—Masked SSNs, as is returned in a response, cannot be passed in a request when QuickBooks Payroll is enabled. Code for this field must be removed before submitting.

### Determine if company is payroll enabled

Query the CompanyInfo endpoint to determine if the company is payroll enabled.

1. Issue a Get operation to the endpoint and scan the response code for the following: { "Name": "PayrollFeature", "Value": "true" },
2. Note the value of *`PayrollFeature`*. Payroll is enabled if *`Value`* is set to `true`.

## The employee object

### employeeresponse

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

#### `PrimaryAddr`

Required: Conditionally required
Type: `PhysicalAddress`
Max length: maximum 30 characters

Represents the physical street address for this employee. If QuickBooks Payroll is enabled for the company, the following PhysicalAddress fields are required:

`City`, maximum of 255 chars

`CountrySubDivisionCode`, maximum of 255 chars

`PostalCode`

Required when QuickBooks Payroll is enabled.
 If a physical address is updated from within the transaction object, the QuickBooks Online API flows individual address components differently into the Line elements of the transaction response then when the transaction was first created:

- `Line1` and `Line2` elements are populated with the customer name and company name.
- Original `Line1` through `Line 5` contents, `City`, `SubDivisionCode`, and `PostalCode` flow into `Line3` through `Line5`as a free format strings.

<details>
<summary>Show more details</summary>

#### AFTER CREATE

| Name | Description |
| --- | --- |
| Line1 | address 1 |
| Line2 | address 2 |
| Line3..5 | address 3..5, as needed |
| City | City |
| CountrySubDivisionCode | subdivision code |
| PostalCode | postal code |
| Lat | latitude |
| Long | longitude |
| Customer name | determine from `CustomerRef` element |
| Company name | determine from `CustomerRef` |

#### AFTER UPDATE

| Name | Description |
| --- | --- |
| Line1 | customer name |
| Line2 | customer name |
| Line3..5 | address 1..5, city, subdivision code, postal code |
| City | not returned |
| CountrySubDivisionCode | not returned |
| Lat | not returned |
| Long | not returned |
| Customer name | determine from `CustomerRef` element |
| Company name | determine from `CustomerRef` element |

</details>

<details>
<summary>Child attributes for `PrimaryAddr`</summary>

##### physicaladdress

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

Unique identifier of the QuickBooks object for the address, autoincremented when the address is changed. This is an internal value included for backwards compatibility and can be ignored.

###### `PostalCode`

Required: Optional
Type: `String`
Max length: Maximum of 30 chars

Postal code. For example, zip code for USA and Canada

###### `City`

Required: Optional
Type: `String`
Max length: Maximum of 255 chars

City name.

###### `Country`

Required: Optional
Type: `String`
Max length: Maximum of 255 chars

Country name. For international addresses - countries should be passed as 3 ISO alpha-3 characters or the full name of the country.

###### `Line5`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

Fifth line of the address.

###### `Line4`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

Fourth line of the address.

###### `Line3`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

Third line of the address.

###### `Line2`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

Second line of the address.

###### `Line1`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

First line of the address.

###### `Lat`

Required: Optional
Type: `String`
Traits: read only, system defined

Latitude coordinate of Geocode (Geospacial Entity Object Code). `INVALID`is returned for invalid addresses.

###### `Long`

Required: Optional
Type: `String`
Traits: read only, system defined

Longitude coordinate of Geocode (Geospacial Entity Object Code). `INVALID`is returned for invalid addresses.

###### `CountrySubDivisionCode`

Required: Optional
Type: `String`
Max length: Maximum of 255 chars

Region within a country. For example, state name for USA, province name for Canada.

</details>

#### `V4IDPseudonym`

Type: `String`
Traits: read only
Minor version: 26

Employee reference number. For internal use only.

#### `PrimaryEmailAddr`

Required: Optional
Type: `EmailAddress`

`Primary email address.`

<details>
<summary>Child attributes for `PrimaryEmailAddr`</summary>

##### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

</details>

#### `DisplayName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 500 chars

The name of the person or organization as displayed. Default Value: If not supplied, the system generates `DisplayName` by concatenating employee name components supplied in the request from the following list: `Title`, `GivenName`, `MiddleName`, `FamilyName`, and `Suffix`. When QuickBooks Payroll is enabled, this attribute is read-only and a concatenation of `GivenName`, `MiddleName`, and `FamilyName`.

#### `Title`

Required: Optional
Type: `String`
Max length: maximum 16 chars

Title of the person. This tag supports i18n, all locale. Not supported when QuickBooks Payroll is enabled.

#### `BillableTime`

Required: Optional
Type: `Boolean`
Default: false

If true, this entity is currently enabled for use by QuickBooks.

#### `GivenName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Given name or family name of a person. At least one of `GivenName` or `FamilyName` attributes is required.

#### `BirthDate`

Required: Optional
Type: `Date`

Birth date of the employee.

<details>
<summary>Child attributes for `BirthDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `MiddleName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Middle name of the person. The person can have zero or more middle names.

#### `SSN`

Required: Optional
Type: `String`
Max length: max 100 chars

Social security number (SSN) of the employee. If SSN is set, it is masked in the response with XXX-XX-XXXX. If XXX-XX-XXXX is sent in the create or update request, XXX-XX-XXXX is ignored and the old value is preserved. This attribute cannot be passed in a request when QuickBooks Payroll is enabled. Code for this field must be removed before submitting.

#### `PrimaryPhone`

Required: Optional
Type: `TelephoneNumber`
Max length: maximum of 20 chars

`Primary phone number.`

<details>
<summary>Child attributes for `PrimaryPhone`</summary>

##### telephonenumber

Model type: `object`

###### `FreeFormNumber`

Required: Optional
Type: `String`
Max length: Maximum of 20 chars

Specifies the telephone number in free form.

</details>

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable
Default: true

If true, this entity is currently enabled for use by QuickBooks.

#### `ReleasedDate`

Required: Optional
Type: `Date`

Release date of the employee.

<details>
<summary>Child attributes for `ReleasedDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the object. The MetaData values are set by Data Services and are read only for all applications.

#### `CostRate`

Required: Optional
Type: `BigDecimal`

Pay rate of the employee

#### `Mobile`

Required: Optional
Type: `TelephoneNumber`
Max length: maximum of 20 chars

Mobile phone number.

<details>
<summary>Child attributes for `Mobile`</summary>

##### telephonenumber

Model type: `object`

###### `FreeFormNumber`

Required: Optional
Type: `String`
Max length: Maximum of 20 chars

Specifies the telephone number in free form.

</details>

#### `Gender`

Required: Optional
Type: `String`

Gender of the employee. To clear the gender value, set to Null in a full update request. Supported values include: `Male` or `Female`.

#### `HiredDate`

Required: Optional
Type: `Date`

Hire date of the employee.

<details>
<summary>Child attributes for `HiredDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `BillRate`

Required: Optional
Type: `BigDecimal`

This attribute can only be set if `BillableTime` is true. Not supported when QuickBooks Payroll is enabled.

#### `Organization`

Required: Optional
Type: `Boolean`
Default: false or null

`true`--the object represents an organization. `false`--the object represents a person.

#### `Suffix`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 16 chars

Suffix of the name. For example, `Jr`. Not supported when QuickBooks Payroll is enabled.

#### `FamilyName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Family name or the last name of the person. At least one of `GivenName` or `FamilyName` attributes is required.

#### `PrintOnCheckName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Name of the person or organization as printed on a check. If not provided, this is populated from `DisplayName`. Cannot be removed with sparse update. Not supported when QuickBooks Payroll is enabled.

#### `EmployeeNumber`

Required: Optional
Type: `String`
Max length: max 100 chars

Specifies the ID number of the employee in the employer's directory.

#### Example

```json
{
  "Employee": {
    "SyncToken": "0",
    "domain": "QBO",
    "DisplayName": "Bill Miller",
    "PrimaryPhone": {
      "FreeFormNumber": "234-525-1234"
    },
    "PrintOnCheckName": "Bill Miller",
    "FamilyName": "Miller",
    "Active": true,
    "SSN": "XXX-XX-XXXX",
    "PrimaryAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Middlefield",
      "PostalCode": "93242",
      "Id": "116",
      "Line1": "45 N. Elm Street"
    },
    "sparse": false,
    "BillableTime": false,
    "GivenName": "Bill",
    "Id": "71",
    "MetaData": {
      "CreateTime": "2015-07-24T09:34:35-07:00",
      "LastUpdatedTime": "2015-07-24T09:34:35-07:00"
    }
  },
  "time": "2015-07-24T09:35:54.805-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T09:35:27.461-07:00">
  <Employee domain="QBO" sparse="false">
    <Id>71</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-24T09:34:35-07:00</CreateTime>
      <LastUpdatedTime>2015-07-24T09:34:35-07:00</LastUpdatedTime>
    </MetaData>
    <GivenName>Bill</GivenName>
    <FamilyName>Miller</FamilyName>
    <DisplayName>Bill Miller</DisplayName>
    <PrintOnCheckName>Bill Miller</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
      <FreeFormNumber>234-525-1234</FreeFormNumber>
    </PrimaryPhone>
    <SSN>XXX-XX-XXXX</SSN>
    <PrimaryAddr>
      <Id>116</Id>
      <Line1>45 N. Elm Street</Line1>
      <City>Middlefield</City>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>93242</PostalCode>
    </PrimaryAddr>
    <BillableTime>false</BillableTime>
  </Employee>
</IntuitResponse>
```

## Create an employee

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/employee`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The elements to create an Employee object are listed here.

Schema: `employeerequest`

<details>
<summary>Show schema for `employeerequest`</summary>

#### employeerequest

Model type: `object`

##### `PrimaryAddr`

Required: Conditionally required
Type: `PhysicalAddress`
Max length: maximum 30 characters

Represents the physical street address for this employee. If QuickBooks Payroll is enabled for the company, the following PhysicalAddress fields are required:

`City`, maximum of 255 chars

`CountrySubDivisionCode`, maximum of 255 chars

`PostalCode`

Required when QuickBooks Payroll is enabled. If a physical address is updated from within the transaction object, the QuickBooks Online API flows individual address components differently into the Line elements of the transaction response then when the transaction was first created:

- `Line1` and `Line2` elements are populated with the customer name and company name.
- Original `Line1` through `Line 5` contents, `City`, `SubDivisionCode`, and `PostalCode` flow into `Line3` through `Line5`as a free format strings.

<details>
<summary>Show more details</summary>

#### AFTER CREATE

| Name | Description |
| --- | --- |
| Line1 | address 1 |
| Line2 | address 2 |
| Line3..5 | address 3..5, as needed |
| City | City |
| CountrySubDivisionCode | subdivision code |
| PostalCode | postal code |
| Lat | latitude |
| Long | longitude |
| Customer name | determine from `CustomerRef` element |
| Company name | determine from `CustomerRef` |

#### AFTER UPDATE

| Name | Description |
| --- | --- |
| Line1 | customer name |
| Line2 | customer name |
| Line3..5 | address 1..5, city, subdivision code, postal code |
| City | not returned |
| CountrySubDivisionCode | not returned |
| Lat | not returned |
| Long | not returned |
| Customer name | determine from `CustomerRef` element |
| Company name | determine from `CustomerRef` element |

</details>

<details>
<summary>Child attributes for `PrimaryAddr`</summary>

###### physicaladdress

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

Unique identifier of the QuickBooks object for the address, autoincremented when the address is changed. This is an internal value included for backwards compatibility and can be ignored.

###### `PostalCode`

Required: Optional
Type: `String`
Max length: Maximum of 30 chars

Postal code. For example, zip code for USA and Canada

###### `City`

Required: Optional
Type: `String`
Max length: Maximum of 255 chars

City name.

###### `Country`

Required: Optional
Type: `String`
Max length: Maximum of 255 chars

Country name. For international addresses - countries should be passed as 3 ISO alpha-3 characters or the full name of the country.

###### `Line5`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

Fifth line of the address.

###### `Line4`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

Fourth line of the address.

###### `Line3`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

Third line of the address.

###### `Line2`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

Second line of the address.

###### `Line1`

Required: Optional
Type: `String`
Max length: Individual maximum of 500 chars, up to combined max of 2000 chars

First line of the address.

###### `Lat`

Required: Optional
Type: `String`
Traits: read only, system defined

Latitude coordinate of Geocode (Geospacial Entity Object Code). `INVALID`is returned for invalid addresses.

###### `Long`

Required: Optional
Type: `String`
Traits: read only, system defined

Longitude coordinate of Geocode (Geospacial Entity Object Code). `INVALID`is returned for invalid addresses.

###### `CountrySubDivisionCode`

Required: Optional
Type: `String`
Max length: Maximum of 255 chars

Region within a country. For example, state name for USA, province name for Canada.

</details>

##### `GivenName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Given name or Family name of a person. At least one of `GivenName` or `FamilyName` attributes is required.

##### `FamilyName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Family name or the last name of the person. At least one of `GivenName` or `FamilyName` attributes is required.

</details>

#### Example

```json
{
  "GivenName": "John",
  "SSN": "444-55-6666",
  "PrimaryAddr": {
    "CountrySubDivisionCode": "CA",
    "City": "Middlefield",
    "PostalCode": "93242",
    "Id": "50",
    "Line1": "45 N. Elm Street"
  },
  "PrimaryPhone": {
    "FreeFormNumber": "408-525-1234"
  },
  "FamilyName": "Meuller"
}
```

#### XML example

```xml
<Employee xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <GivenName>Bill</GivenName>
    <FamilyName>Miller</FamilyName>
    <DisplayName>John Miller</DisplayName>
    <PrintOnCheckName>John Miller</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
        <FreeFormNumber>234-525-1234</FreeFormNumber>
    </PrimaryPhone>
    <SSN>888-77-6666</SSN>
    <PrimaryAddr>
        <Id>356</Id>
        <Line1>45 N. Elm Street</Line1>
        <City>Middlefield</City>
        <CountrySubDivisionCode>CA</CountrySubDivisionCode>
        <PostalCode>93242</PostalCode>
        <Lat>37.4601027</Lat>
        <Long>-122.1523605</Long>
    </PrimaryAddr>
    <BillableTime>true</BillableTime>
    <BillRate>50</BillRate>
    <HiredDate>2013-11-01</HiredDate>
</Employee>
```

### Returns

Returns the newly created Employee object.

#### Example

```json
{
  "Employee": {
    "SyncToken": "0",
    "domain": "QBO",
    "DisplayName": "John Meuller",
    "PrimaryPhone": {
      "FreeFormNumber": "408-525-1234"
    },
    "PrintOnCheckName": "John Meuller",
    "FamilyName": "Meuller",
    "Active": true,
    "SSN": "XXX-XX-XXXX",
    "PrimaryAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Middlefield",
      "PostalCode": "93242",
      "Id": "115",
      "Line1": "45 N. Elm Street"
    },
    "sparse": false,
    "BillableTime": false,
    "GivenName": "John",
    "Id": "70",
    "MetaData": {
      "CreateTime": "2015-07-24T09:24:57-07:00",
      "LastUpdatedTime": "2015-07-24T09:24:57-07:00"
    }
  },
  "time": "2015-07-24T09:24:57.907-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T09:34:35.235-07:00">
  <Employee domain="QBO" sparse="false">
    <Id>71</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-24T09:34:35-07:00</CreateTime>
      <LastUpdatedTime>2015-07-24T09:34:35-07:00</LastUpdatedTime>
    </MetaData>
    <GivenName>Bill</GivenName>
    <FamilyName>Miller</FamilyName>
    <DisplayName>Bill Miller</DisplayName>
    <PrintOnCheckName>Bill Miller</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
      <FreeFormNumber>234-525-1234</FreeFormNumber>
    </PrimaryPhone>
    <SSN>XXX-XX-XXXX</SSN>
    <PrimaryAddr>
      <Id>116</Id>
      <Line1>45 N. Elm Street</Line1>
      <City>Middlefield</City>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>93242</PostalCode>
    </PrimaryAddr>
    <BillableTime>false</BillableTime>
  </Employee>
</IntuitResponse>
```

## Query an employee

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Employee where DisplayName = 'Emily Platt'"
```

#### XML example

```sql
select * from Employee where DisplayName = 'Emily Platt'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "Employee": [
      {
        "SyncToken": "2",
        "domain": "QBO",
        "DisplayName": "Emily Platt",
        "MiddleName": "Jane",
        "FamilyName": "Platt",
        "Active": true,
        "PrintOnCheckName": "Emily Platt",
        "sparse": false,
        "BillableTime": false,
        "GivenName": "Emily",
        "Id": "55",
        "MetaData": {
          "CreateTime": "2014-09-17T11:21:48-07:00",
          "LastUpdatedTime": "2015-07-01T11:29:40-07:00"
        }
      }
    ],
    "startPosition": 1,
    "maxResults": 1
  },
  "time": "2015-07-24T08:56:55.808-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T08:57:31.352-07:00">
  <QueryResponse startPosition="1" maxResults="1">
    <Employee domain="QBO" sparse="false">
      <Id>55</Id>
      <SyncToken>2</SyncToken>
      <MetaData>
        <CreateTime>2014-09-17T11:21:48-07:00</CreateTime>
        <LastUpdatedTime>2015-07-01T11:29:40-07:00</LastUpdatedTime>
      </MetaData>
      <GivenName>Emily</GivenName>
      <MiddleName>Jane</MiddleName>
      <FamilyName>Platt</FamilyName>
      <DisplayName>Emily Platt</DisplayName>
      <PrintOnCheckName>Emily Platt</PrintOnCheckName>
      <Active>true</Active>
      <BillableTime>false</BillableTime>
    </Employee>
  </QueryResponse>
</IntuitResponse>
```

## Read an employee

### Definition

- **Operation:** `GET /v3/company/<realmID>/employee/<employeeId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Employee object that has been previously created.

### Returns

Returns the Employee object.

#### Example

```json
{
  "Employee": {
    "SyncToken": "0",
    "domain": "QBO",
    "DisplayName": "Bill Miller",
    "PrimaryPhone": {
      "FreeFormNumber": "234-525-1234"
    },
    "PrintOnCheckName": "Bill Miller",
    "FamilyName": "Miller",
    "Active": true,
    "SSN": "XXX-XX-XXXX",
    "PrimaryAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Middlefield",
      "PostalCode": "93242",
      "Id": "116",
      "Line1": "45 N. Elm Street"
    },
    "sparse": false,
    "BillableTime": false,
    "GivenName": "Bill",
    "Id": "71",
    "MetaData": {
      "CreateTime": "2015-07-24T09:34:35-07:00",
      "LastUpdatedTime": "2015-07-24T09:34:35-07:00"
    }
  },
  "time": "2015-07-24T09:35:54.805-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T09:35:27.461-07:00">
  <Employee domain="QBO" sparse="false">
    <Id>71</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-24T09:34:35-07:00</CreateTime>
      <LastUpdatedTime>2015-07-24T09:34:35-07:00</LastUpdatedTime>
    </MetaData>
    <GivenName>Bill</GivenName>
    <FamilyName>Miller</FamilyName>
    <DisplayName>Bill Miller</DisplayName>
    <PrintOnCheckName>Bill Miller</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
      <FreeFormNumber>234-525-1234</FreeFormNumber>
    </PrimaryPhone>
    <SSN>XXX-XX-XXXX</SSN>
    <PrimaryAddr>
      <Id>116</Id>
      <Line1>45 N. Elm Street</Line1>
      <City>Middlefield</City>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>93242</PostalCode>
    </PrimaryAddr>
    <BillableTime>false</BillableTime>
  </Employee>
</IntuitResponse>
```

## Full update an employee

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/employee`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing employee object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `employeeresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "domain": "QBO",
  "DisplayName": "Bill Miller",
  "PrimaryPhone": {
    "FreeFormNumber": "234-525-1234"
  },
  "PrintOnCheckName": "Bill Lee Miller",
  "FamilyName": "Miller",
  "Active": true,
  "SSN": "XXX-XX-XXXX",
  "PrimaryAddr": {
    "CountrySubDivisionCode": "CA",
    "City": "Middlefield",
    "PostalCode": "93242",
    "Id": "116",
    "Line1": "45 N. Elm Street"
  },
  "sparse": false,
  "BillableTime": false,
  "GivenName": "Bill",
  "Id": "71",
  "MetaData": {
    "CreateTime": "2015-07-24T09:34:35-07:00",
    "LastUpdatedTime": "2015-07-24T09:34:35-07:00"
  }
}
```

#### XML example

```xml
<Employee xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>71</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2015-07-24T09:34:35-07:00</CreateTime>
      <LastUpdatedTime>2015-07-24T09:34:35-07:00</LastUpdatedTime>
    </MetaData>
    <GivenName>Bill</GivenName>
    <FamilyName>Miller</FamilyName>
    <DisplayName>Bill Miller</DisplayName>
    <PrintOnCheckName>Bill Miller</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
      <FreeFormNumber>234-525-1234</FreeFormNumber>
    </PrimaryPhone>
    <SSN>XXX-XX-XXXX</SSN>
    <PrimaryAddr>
      <Id>116</Id>
      <Line1>45 N. Main Street</Line1>
      <City>Middlefield</City>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>93242</PostalCode>
    </PrimaryAddr>
    <BillableTime>false</BillableTime>
</Employee>
```

### Returns

The Employee object response body.

#### Example

```json
{
  "Employee": {
    "SyncToken": "1",
    "domain": "QBO",
    "DisplayName": "Bill Miller",
    "PrimaryPhone": {
      "FreeFormNumber": "234-525-1234"
    },
    "PrintOnCheckName": "Bill Lee Miller",
    "FamilyName": "Miller",
    "Active": true,
    "SSN": "XXX-XX-XXXX",
    "PrimaryAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Middlefield",
      "PostalCode": "93242",
      "Id": "116",
      "Line1": "45 N. Elm Street"
    },
    "sparse": false,
    "BillableTime": false,
    "GivenName": "Bill",
    "Id": "71",
    "MetaData": {
      "CreateTime": "2015-07-24T09:34:35-07:00",
      "LastUpdatedTime": "2015-07-24T09:37:39-07:00"
    }
  },
  "time": "2015-07-24T09:37:39.399-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T09:39:38.491-07:00">
  <Employee domain="QBO" sparse="false">
    <Id>71</Id>
    <SyncToken>2</SyncToken>
    <MetaData>
      <CreateTime>2015-07-24T09:34:35-07:00</CreateTime>
      <LastUpdatedTime>2015-07-24T09:39:38-07:00</LastUpdatedTime>
    </MetaData>
    <GivenName>Bill</GivenName>
    <FamilyName>Miller</FamilyName>
    <DisplayName>Bill Miller</DisplayName>
    <PrintOnCheckName>Bill Miller</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
      <FreeFormNumber>234-525-1234</FreeFormNumber>
    </PrimaryPhone>
    <SSN>XXX-XX-XXXX</SSN>
    <PrimaryAddr>
      <Id>116</Id>
      <Line1>45 N. Main Street</Line1>
      <City>Middlefield</City>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>93242</PostalCode>
    </PrimaryAddr>
    <BillableTime>false</BillableTime>
  </Employee>
</IntuitResponse>
```
