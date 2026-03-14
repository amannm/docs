# CompanyInfo

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/companyinfo
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Most commonly used](index.md) / CompanyInfo
> Canonical entity: `CompanyInfo`

The CompanyInfo object contains basic company information. In QuickBooks, company info and preferences are displayed in the same place under preferences, so it may be confusing to figure out from user interface which fields may belong to this object. But in general, properties such as company addresses or name are considered company information. Some attributes may exist in both CompanyInfo and Preferences objects.

## The companyinfo object

### companyinforesponse

Model type: `object`

#### `Id`

Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `CompanyName`

Required: Required for update
Type: `String`
Max length: Maximum of 1024 chars

The name of the company.

#### `CompanyAddr`

Required: Required for update
Type: `PhysicalAddress`

Company Address as described in preference.
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
<summary>Child attributes for `CompanyAddr`</summary>

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

#### `CompanyStartDate`

Type: `DateTime`
Traits: read only, system defined

DateTime when company file was created. This field and `Metadata.CreateTime`contain the same value.

<details>
<summary>Child attributes for `CompanyStartDate`</summary>

##### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

#### `LegalAddr`

Required: Optional
Type: `PhysicalAddress`

Legal Address given to the government for any government communication.
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
<summary>Child attributes for `LegalAddr`</summary>

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

#### `SupportedLanguages`

Required: Optional
Type: `String`

Comma separated list of languages.

#### `Country`

Required: Optional
Type: `String`

Country name to which the company belongs for financial calculations.

#### `Email`

Required: Optional
Type: `EmailAddress`
Max length: max 100 chars

Default email address.

<details>
<summary>Child attributes for `Email`</summary>

##### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

</details>

#### `WebAddr`

Required: Optional
Type: `WebSiteAddress`
Max length: max 1000 chars

Website address.

<details>
<summary>Child attributes for `WebAddr`</summary>

##### websiteaddress

Model type: `object`

###### `URI`

Required: Optional
Type: `String`
Max length: Maximum of 1000 chars

Uniform Resource Identifier for the web site.

</details>

#### `NameValue [0..n]`

Required: Optional
Type: `NameValue pairs`

Any other preference not covered with the standard set of attributes. See Data Services Extensions, below, for special reserved name/value pairs. NameValue.Name--Name of the element. NameValue.Value--Value of the element.

<details>
<summary>Show Data Services Extensions</summary>

#### ATTRIBUTES

| Name | Description |
| --- | --- |
| **EXTENSIONS** | **DESCRIPTION** |
| NeoEnabled | The type of company, classic or Harmony. <br>`NameValue.Name="NeoEnabled"` <br>`NameValue.Value="neoFlag"` <br>where *neoFlag* is defined as: <br>`true` for Harmony company <br>`false` for Classic company |
| firstTxnDate | The date of the first transaction for the company. <br>`NameValue.Name="firsttxndate"` <br>`NameValue.Value="date"` <br> where date is of the format `yyyy-mm-dd` <br>This extension is avaliable when the `include=firsttxndate`query parameter is include in the endpoint URI: <br>A GET request looks like the following <br> `baseURL/company <br>/213316401/companyinfo/213316401? <br>include=firsttxndate` <br>A Query Request looks like the following <br>baseURL/company/213316401/query?query=select * from CompanyInfo include=firsttxndate |
| IndustryType | The industry type for the company. This is defined when the company is first created. |
| IndustryCode | The NAICS/SIC industry code for the company. This is defined when the company is first created. |
| CompanyType | The company type as defined when the company is first created. Possible values include: <br> <br>`Sole Proprietor` <br>`Partnership` <br>`Limited Liability` <br>`Corporation` <br>`Organization` |
| OfferingSKU | The specific QuickBooks Online product. Possible values include: <br> <br>`QuickBooks Online Plus` <br>`QuickBooks Online Simple Start` <br>`QuickBooks Online Essentials` <br>When CompanyInfo endpoint is invoked with `minorversion=29`, possible values include: <br>`QuickBooks Online Advanced` - Advanced companies will return `QuickBooks Online Plus` as OfferingSKU if minor version lower than 29 is used. |
| SubscriptionStatus | The QuickBooks subscription status. <br>Possible values, prior to minor version 3: <br>`TRIAL`-Company is in trial <br>`PAID`-For any other state <br>When CompanyInfo endpoint is invoked with `minorversion=3`, possible values include: <br>`TRIAL`-Company is in trial. <br>`SUBSCRIBED`-Company is subscribed. <br>`TRIALOPTIN`-Company is in trial and user has provided credit card info. <br>`RESTRICTED`-The customer's subscription payment failed and QuickBooks services is waiting for the customer to update their payment information. During this state, customers have read and write access to their company file. If the customer does not update the payment information within a week, the state moves to suspended and write access is revoked. <br>`SUSPENDED`-Company in a lock-out mode, for instance due to payment failure. <br>`EXPIRED`-Company in a lock-out mode due to missing payment information. <br>`CANCELLED`-Company is cancelled by the user or support agent. <br>`UNKNOWN`-Context of the company is not available. |
| PayrollFeature | Whether subscription is enabled for the payroll feature. `true` is Enabled. `false` is Disabled. |
| AccountantFeature | Whether subscription is enabled for the accountant feature. `true` is Enabled. `false` is Disabled. |
| ItemCategoriesFeature | Whether a company is category enabled. Currently available for sandbox companies, only. This functionality will be rolled out to all companies in the coming months. `true` is Enabled. `false` is Disabled. |
| NonTracking | Property to determine whether the company is 'NonTracking' enabled. Based on this flag, the appropriate fields should be used while querying General Ledger or Profilt and Loss Detail report. `true` is Enabled. `false` is Disabled. |
| QBOIndustryType | The industry type for the company. This is defined when the company is first created. |
| AssignedTime | Company creation time, where date and time is of the format `YYYY-MM-DDTHH:mm:ssZ`. |
| IsQbdtMigrated | Whether the CompanyInfo data was originally imported into QuickBooks Online from QuickBooks Desktop. `true` was imported. `false` was not imported. |
| MigrationDate | If CompanyInfo data was imported from QuickBooks Desktop, the date and time of the import, where date and time is of the format `YYYY-MM-DDTHH:mm:ssZ`. |

</details>

#### `FiscalYearStartMonth`

Required: Optional
Type: `MonthEnum`

The start month of fiscal year.

#### `CustomerCommunicationAddr`

Required: Optional
Type: `PhysicalAddress`

Address of the company as given to their customer, sometimes the address given to the customer mail address is different from Company address. If a physical address is updated from within the transaction object, the QuickBooks Online API flows individual address components differently into the Line elements of the transaction response then when the transaction was first created:

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
<summary>Child attributes for `CustomerCommunicationAddr`</summary>

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

#### `PrimaryPhone`

Required: Optional
Type: `TelephoneNumber`

Primary phone number.

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

#### `LegalName`

Required: Optional
Type: `String`
Max length: Maximum of 1024 chars

The legal name of the company.

#### `EmployerId`

Required: Optional
Type: `String`

If your QuickBooks company has defined an EIN in company settings, this value is returned.

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
  "CompanyInfo": {
    "SyncToken": "4",
    "domain": "QBO",
    "LegalAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "SupportedLanguages": "en",
    "CompanyName": "Larry's Bakery",
    "Country": "US",
    "CompanyAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "sparse": false,
    "Id": "1",
    "WebAddr": {},
    "FiscalYearStartMonth": "January",
    "CustomerCommunicationAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "PrimaryPhone": {
      "FreeFormNumber": "(650)944-4444"
    },
    "LegalName": "Larry's Bakery",
    "CompanyStartDate": "2015-06-05",
    "EmployerId": "123456789",
    "Email": {
      "Address": "donotreply@intuit.com"
    },
    "NameValue": [
      {
        "Name": "NeoEnabled",
        "Value": "true"
      },
      {
        "Name": "IndustryType",
        "Value": "Bread and Bakery Product Manufacturing"
      },
      {
        "Name": "IndustryCode",
        "Value": "31181"
      },
      {
        "Name": "SubscriptionStatus",
        "Value": "PAID"
      },
      {
        "Name": "OfferingSku",
        "Value": "QuickBooks Online Plus"
      },
      {
        "Name": "PayrollFeature",
        "Value": "true"
      },
      {
        "Name": "AccountantFeature",
        "Value": "false"
      },
      {
        "Name": "IsQbdtMigrated",
        "Value": "true"
      },
      {
        "Name": "MigrationDate",
        "Value": "2024-09-14T01:47:34-07:00"
      },
      {
        "Name": "QBOIndustryType",
        "Value": "Manufacturing Businesses"
      },
      {
        "Name": "AssignedTime",
        "Value": "2024-09-14T01:47:34-07:00"
      }
    ],
    "MetaData": {
      "CreateTime": "2015-06-05T13:55:54-07:00",
      "LastUpdatedTime": "2015-07-06T08:51:50-07:00"
    }
  },
  "time": "2015-07-10T09:38:58.155-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-10T11:59:43.740-07:00">
    <QueryResponse maxResults="1">
        <CompanyInfo domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>3</SyncToken>
            <MetaData>
                <CreateTime>2015-06-05T13:55:54-07:00</CreateTime>
                <LastUpdatedTime>2015-07-06T08:51:50-07:00</LastUpdatedTime>
            </MetaData>
            <CompanyName>Larry's Bakery</CompanyName>
            <LegalName>Larry's Bakery</LegalName>
            <CompanyAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </CompanyAddr>
            <CustomerCommunicationAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </CustomerCommunicationAddr>
            <LegalAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </LegalAddr>
            <PrimaryPhone>
                <FreeFormNumber>(650)944-4444</FreeFormNumber>
            </PrimaryPhone>
            <CompanyStartDate>2015-06-05</CompanyStartDate>
            <EmployerId>123456789</EmployerId>
            <FiscalYearStartMonth>January</FiscalYearStartMonth>
            <Country>US</Country>
            <Email>
                <Address>donotreply@intuit.com</Address>
            </Email>
            <WebAddr/>
            <SupportedLanguages>en</SupportedLanguages>
            <NameValue>
                <Name>NeoEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>IndustryType</Name>
                <Value>Bread and Bakery Product Manufacturing</Value>
            </NameValue>
            <NameValue>
                <Name>IndustryCode</Name>
                <Value>31181</Value>
            </NameValue>
            <NameValue>
                <Name>SubscriptionStatus</Name>
                <Value>PAID</Value>
            </NameValue>
            <NameValue>
                <Name>OfferingSku</Name>
                <Value>QuickBooks Online Plus</Value>
            </NameValue>
            <NameValue>
                <Name>PayrollFeature</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>AccountantFeature</Name>
                <Value>false</Value>
            </NameValue>
        </CompanyInfo>
    </QueryResponse>
</IntuitResponse>
```

## Query companyinfo

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from CompanyInfo\n"
```

#### XML example

```sql
select * from CompanyInfo
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "CompanyInfo": {
    "SyncToken": "4",
    "domain": "QBO",
    "LegalAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "SupportedLanguages": "en",
    "CompanyName": "Larry's Bakery",
    "Country": "US",
    "CompanyAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "sparse": false,
    "Id": "1",
    "WebAddr": {},
    "FiscalYearStartMonth": "January",
    "CustomerCommunicationAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "PrimaryPhone": {
      "FreeFormNumber": "(650)944-4444"
    },
    "LegalName": "Larry's Bakery",
    "CompanyStartDate": "2015-06-05",
    "EmployerId": "123456789",
    "Email": {
      "Address": "donotreply@intuit.com"
    },
    "NameValue": [
      {
        "Name": "NeoEnabled",
        "Value": "true"
      },
      {
        "Name": "IndustryType",
        "Value": "Bread and Bakery Product Manufacturing"
      },
      {
        "Name": "IndustryCode",
        "Value": "31181"
      },
      {
        "Name": "SubscriptionStatus",
        "Value": "PAID"
      },
      {
        "Name": "OfferingSku",
        "Value": "QuickBooks Online Plus"
      },
      {
        "Name": "PayrollFeature",
        "Value": "true"
      },
      {
        "Name": "AccountantFeature",
        "Value": "false"
      },
      {
        "Name": "IsQbdtMigrated",
        "Value": "true"
      },
      {
        "Name": "MigrationDate",
        "Value": "2024-09-14T01:47:34-07:00"
      },
      {
        "Name": "QBOIndustryType",
        "Value": "Manufacturing Businesses"
      },
      {
        "Name": "AssignedTime",
        "Value": "2024-09-14T01:47:34-07:00"
      }
    ],
    "MetaData": {
      "CreateTime": "2015-06-05T13:55:54-07:00",
      "LastUpdatedTime": "2015-07-06T08:51:50-07:00"
    }
  },
  "time": "2015-07-10T09:38:58.155-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-10T11:59:43.740-07:00">
    <QueryResponse maxResults="1">
        <CompanyInfo domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>3</SyncToken>
            <MetaData>
                <CreateTime>2015-06-05T13:55:54-07:00</CreateTime>
                <LastUpdatedTime>2015-07-06T08:51:50-07:00</LastUpdatedTime>
            </MetaData>
            <CompanyName>Larry's Bakery</CompanyName>
            <LegalName>Larry's Bakery</LegalName>
            <CompanyAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </CompanyAddr>
            <CustomerCommunicationAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </CustomerCommunicationAddr>
            <LegalAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </LegalAddr>
            <PrimaryPhone>
                <FreeFormNumber>(650)944-4444</FreeFormNumber>
            </PrimaryPhone>
            <CompanyStartDate>2015-06-05</CompanyStartDate>
            <EmployerId>123456789</EmployerId>
            <FiscalYearStartMonth>January</FiscalYearStartMonth>
            <Country>US</Country>
            <Email>
                <Address>donotreply@intuit.com</Address>
            </Email>
            <WebAddr/>
            <SupportedLanguages>en</SupportedLanguages>
            <NameValue>
                <Name>NeoEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>IndustryType</Name>
                <Value>Bread and Bakery Product Manufacturing</Value>
            </NameValue>
            <NameValue>
                <Name>IndustryCode</Name>
                <Value>31181</Value>
            </NameValue>
            <NameValue>
                <Name>SubscriptionStatus</Name>
                <Value>PAID</Value>
            </NameValue>
            <NameValue>
                <Name>OfferingSku</Name>
                <Value>QuickBooks Online Plus</Value>
            </NameValue>
            <NameValue>
                <Name>PayrollFeature</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>AccountantFeature</Name>
                <Value>false</Value>
            </NameValue>
        </CompanyInfo>
    </QueryResponse>
</IntuitResponse>
```

## Read companyinfo

### Definition

- **Operation:** `GET /v3/company/<realmID>/companyinfo/<realmID>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of the CompanyInfo object.

### Returns

Returns the companyinfo object.

#### Example

```json
{
  "CompanyInfo": {
    "SyncToken": "4",
    "domain": "QBO",
    "LegalAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "SupportedLanguages": "en",
    "CompanyName": "Larry's Bakery",
    "Country": "US",
    "CompanyAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "sparse": false,
    "Id": "1",
    "WebAddr": {},
    "FiscalYearStartMonth": "January",
    "CustomerCommunicationAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "PrimaryPhone": {
      "FreeFormNumber": "(650)944-4444"
    },
    "LegalName": "Larry's Bakery",
    "CompanyStartDate": "2015-06-05",
    "EmployerId": "123456789",
    "Email": {
      "Address": "donotreply@intuit.com"
    },
    "NameValue": [
      {
        "Name": "NeoEnabled",
        "Value": "true"
      },
      {
        "Name": "IndustryType",
        "Value": "Bread and Bakery Product Manufacturing"
      },
      {
        "Name": "IndustryCode",
        "Value": "31181"
      },
      {
        "Name": "SubscriptionStatus",
        "Value": "PAID"
      },
      {
        "Name": "OfferingSku",
        "Value": "QuickBooks Online Plus"
      },
      {
        "Name": "PayrollFeature",
        "Value": "true"
      },
      {
        "Name": "AccountantFeature",
        "Value": "false"
      },
      {
        "Name": "IsQbdtMigrated",
        "Value": "true"
      },
      {
        "Name": "MigrationDate",
        "Value": "2024-09-14T01:47:34-07:00"
      },
      {
        "Name": "QBOIndustryType",
        "Value": "Manufacturing Businesses"
      },
      {
        "Name": "AssignedTime",
        "Value": "2024-09-14T01:47:34-07:00"
      }
    ],
    "MetaData": {
      "CreateTime": "2015-06-05T13:55:54-07:00",
      "LastUpdatedTime": "2015-07-06T08:51:50-07:00"
    }
  },
  "time": "2015-07-10T09:38:58.155-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-10T11:59:43.740-07:00">
    <QueryResponse maxResults="1">
        <CompanyInfo domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>3</SyncToken>
            <MetaData>
                <CreateTime>2015-06-05T13:55:54-07:00</CreateTime>
                <LastUpdatedTime>2015-07-06T08:51:50-07:00</LastUpdatedTime>
            </MetaData>
            <CompanyName>Larry's Bakery</CompanyName>
            <LegalName>Larry's Bakery</LegalName>
            <CompanyAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </CompanyAddr>
            <CustomerCommunicationAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </CustomerCommunicationAddr>
            <LegalAddr>
                <Id>1</Id>
                <Line1>2500 Garcia Ave</Line1>
                <City>Mountain View</City>
                <Country>US</Country>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94043</PostalCode>
            </LegalAddr>
            <PrimaryPhone>
                <FreeFormNumber>(650)944-4444</FreeFormNumber>
            </PrimaryPhone>
            <CompanyStartDate>2015-06-05</CompanyStartDate>
            <EmployerId>123456789</EmployerId>
            <FiscalYearStartMonth>January</FiscalYearStartMonth>
            <Country>US</Country>
            <Email>
                <Address>donotreply@intuit.com</Address>
            </Email>
            <WebAddr/>
            <SupportedLanguages>en</SupportedLanguages>
            <NameValue>
                <Name>NeoEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>IndustryType</Name>
                <Value>Bread and Bakery Product Manufacturing</Value>
            </NameValue>
            <NameValue>
                <Name>IndustryCode</Name>
                <Value>31181</Value>
            </NameValue>
            <NameValue>
                <Name>SubscriptionStatus</Name>
                <Value>PAID</Value>
            </NameValue>
            <NameValue>
                <Name>OfferingSku</Name>
                <Value>QuickBooks Online Plus</Value>
            </NameValue>
            <NameValue>
                <Name>PayrollFeature</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>AccountantFeature</Name>
                <Value>false</Value>
            </NameValue>
        </CompanyInfo>
    </QueryResponse>
</IntuitResponse>
```

## Full update companyinfo

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/companyinfo`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Available with minor version 11. Use this operation to update any of the writable fields of the companyinfo object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `companyinforesponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "3",
  "domain": "QBO",
  "LegalAddr": {
    "City": "Mountain View",
    "Country": "US",
    "Line1": "2500 Garcia Ave",
    "PostalCode": "94043",
    "CountrySubDivisionCode": "CA",
    "Id": "1"
  },
  "SupportedLanguages": "en",
  "CompanyName": "Larry's Bakery",
  "Country": "US",
  "CompanyAddr": {
    "City": "Mountain View",
    "Country": "US",
    "Line1": "2500 Garcia Ave",
    "PostalCode": "94043",
    "CountrySubDivisionCode": "CA",
    "Id": "1"
  },
  "sparse": false,
  "Id": "1",
  "WebAddr": {},
  "FiscalYearStartMonth": "January",
  "CustomerCommunicationAddr": {
    "City": "Mountain View",
    "Country": "US",
    "Line1": "2500 Garcia Ave",
    "PostalCode": "94043",
    "CountrySubDivisionCode": "CA",
    "Id": "1"
  },
  "PrimaryPhone": {
    "FreeFormNumber": "(650)944-4444"
  },
  "LegalName": "Larry's Bakery",
  "CompanyStartDate": "2015-06-05",
  "Email": {
    "Address": "donotreply@intuit.com"
  },
  "NameValue": [
    {
      "Name": "NeoEnabled",
      "Value": "true"
    },
    {
      "Name": "IndustryType",
      "Value": "Bread and Bakery Product Manufacturing"
    },
    {
      "Name": "IndustryCode",
      "Value": "31181"
    },
    {
      "Name": "SubscriptionStatus",
      "Value": "PAID"
    },
    {
      "Name": "OfferingSku",
      "Value": "QuickBooks Online Plus"
    },
    {
      "Name": "PayrollFeature",
      "Value": "true"
    },
    {
      "Name": "AccountantFeature",
      "Value": "false"
    },
    {
      "Name": "IsQbdtMigrated",
      "Value": "true"
    },
    {
      "Name": "MigrationDate",
      "Value": "2024-09-14T01:47:34-07:00"
    },
    {
      "Name": "QBOIndustryType",
      "Value": "Manufacturing Businesses"
    },
    {
      "Name": "AssignedTime",
      "Value": "2024-09-14T01:47:34-07:00"
    }
  ],
  "MetaData": {
    "CreateTime": "2015-06-05T13:55:54-07:00",
    "LastUpdatedTime": "2015-07-06T08:51:50-07:00"
  }
}
```

#### XML example

```xml
<CompanyInfo xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>1</Id>
    <SyncToken>3</SyncToken>
    <MetaData>
        <CreateTime>2015-06-05T13:55:54-07:00</CreateTime>
        <LastUpdatedTime>2015-07-06T08:51:50-07:00</LastUpdatedTime>
    </MetaData>
    <CompanyName>Larry's Bakery</CompanyName>
    <LegalName>Larry's Bakery</LegalName>
    <CompanyAddr>
        <Id>1</Id>
        <Line1>2500 Garcia Ave</Line1>
        <City>Mountain View</City>
        <Country>US</Country>
        <CountrySubDivisionCode>CA</CountrySubDivisionCode>
        <PostalCode>94043</PostalCode>
    </CompanyAddr>
    <CustomerCommunicationAddr>
        <Id>1</Id>
        <Line1>2500 Garcia Ave</Line1>
        <City>Mountain View</City>
        <Country>US</Country>
        <CountrySubDivisionCode>CA</CountrySubDivisionCode>
        <PostalCode>94043</PostalCode>
    </CustomerCommunicationAddr>
    <LegalAddr>
        <Id>1</Id>
        <Line1>2500 Garcia Ave</Line1>
        <City>Mountain View</City>
        <Country>US</Country>
        <CountrySubDivisionCode>CA</CountrySubDivisionCode>
        <PostalCode>94043</PostalCode>
    </LegalAddr>
    <PrimaryPhone>
        <FreeFormNumber>(650)944-4444</FreeFormNumber>
    </PrimaryPhone>
    <CompanyStartDate>2015-06-05</CompanyStartDate>
    <FiscalYearStartMonth>January</FiscalYearStartMonth>
    <Country>US</Country>
    <Email>
        <Address>donotreply@intuit.com</Address>
    </Email>
    <WebAddr/>
    <SupportedLanguages>en</SupportedLanguages>
    <NameValue>
        <Name>NeoEnabled</Name>
        <Value>true</Value>
    </NameValue>
    <NameValue>
        <Name>IndustryType</Name>
        <Value>Bread and Bakery Product Manufacturing</Value>
    </NameValue>
    <NameValue>
        <Name>IndustryCode</Name>
        <Value>31181</Value>
    </NameValue>
    <NameValue>
        <Name>SubscriptionStatus</Name>
        <Value>PAID</Value>
    </NameValue>
    <NameValue>
        <Name>OfferingSku</Name>
        <Value>QuickBooks Online Plus</Value>
    </NameValue>
    <NameValue>
        <Name>PayrollFeature</Name>
        <Value>true</Value>
    </NameValue>
    <NameValue>
        <Name>AccountantFeature</Name>
        <Value>false</Value>
    </NameValue>
</CompanyInfo>
```

### Returns

The invoice response body.

#### Example

```json
{
  "CompanyInfo": {
    "SyncToken": "4",
    "domain": "QBO",
    "LegalAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "SupportedLanguages": "en",
    "CompanyName": "Larry's Bakery",
    "Country": "US",
    "CompanyAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "sparse": false,
    "Id": "1",
    "WebAddr": {},
    "FiscalYearStartMonth": "January",
    "CustomerCommunicationAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "PrimaryPhone": {
      "FreeFormNumber": "(650)944-4444"
    },
    "LegalName": "Larry's Bakery",
    "CompanyStartDate": "2015-06-05",
    "EmployerId": "123456789",
    "Email": {
      "Address": "donotreply@intuit.com"
    },
    "NameValue": [
      {
        "Name": "NeoEnabled",
        "Value": "true"
      },
      {
        "Name": "IndustryType",
        "Value": "Bread and Bakery Product Manufacturing"
      },
      {
        "Name": "IndustryCode",
        "Value": "31181"
      },
      {
        "Name": "SubscriptionStatus",
        "Value": "PAID"
      },
      {
        "Name": "OfferingSku",
        "Value": "QuickBooks Online Plus"
      },
      {
        "Name": "PayrollFeature",
        "Value": "true"
      },
      {
        "Name": "AccountantFeature",
        "Value": "false"
      },
      {
        "Name": "IsQbdtMigrated",
        "Value": "true"
      },
      {
        "Name": "MigrationDate",
        "Value": "2024-09-14T01:47:34-07:00"
      },
      {
        "Name": "QBOIndustryType",
        "Value": "Manufacturing Businesses"
      },
      {
        "Name": "AssignedTime",
        "Value": "2024-09-14T01:47:34-07:00"
      }
    ],
    "MetaData": {
      "CreateTime": "2015-06-05T13:55:54-07:00",
      "LastUpdatedTime": "2015-07-06T08:51:50-07:00"
    }
  },
  "time": "2015-07-10T09:38:58.155-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-10T08:30:02.829-07:00">
    <CompanyInfo domain="QBO" sparse="false">
        <Id>1</Id>
        <SyncToken>4</SyncToken>
        <MetaData>
            <CreateTime>2015-06-05T13:55:54-07:00</CreateTime>
            <LastUpdatedTime>2015-07-06T08:51:50-07:00</LastUpdatedTime>
        </MetaData>
        <CompanyName>Larry's Bakery</CompanyName>
        <LegalName>Larry's Bakery</LegalName>
        <CompanyAddr>
            <Id>1</Id>
            <Line1>2500 Garcia Ave</Line1>
            <City>Mountain View</City>
            <Country>US</Country>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94043</PostalCode>
        </CompanyAddr>
        <CustomerCommunicationAddr>
            <Id>1</Id>
            <Line1>2500 Garcia Ave</Line1>
            <City>Mountain View</City>
            <Country>US</Country>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94043</PostalCode>
        </CustomerCommunicationAddr>
        <LegalAddr>
            <Id>1</Id>
            <Line1>2500 Garcia Ave</Line1>
            <City>Mountain View</City>
            <Country>US</Country>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94043</PostalCode>
        </LegalAddr>
        <PrimaryPhone>
            <FreeFormNumber>(650)944-4444</FreeFormNumber>
        </PrimaryPhone>
        <CompanyStartDate>2015-06-05</CompanyStartDate>
        <EmployerId>123456789</EmployerId>
        <FiscalYearStartMonth>January</FiscalYearStartMonth>
        <Country>US</Country>
        <Email>
            <Address>donotreply@intuit.com</Address>
        </Email>
        <WebAddr/>
        <SupportedLanguages>en</SupportedLanguages>
        <NameValue>
            <Name>NeoEnabled</Name>
            <Value>true</Value>
        </NameValue>
        <NameValue>
            <Name>IndustryType</Name>
            <Value>Bread and Bakery Product Manufacturing</Value>
        </NameValue>
        <NameValue>
            <Name>IndustryCode</Name>
            <Value>31181</Value>
        </NameValue>
        <NameValue>
            <Name>SubscriptionStatus</Name>
            <Value>PAID</Value>
        </NameValue>
        <NameValue>
            <Name>OfferingSku</Name>
            <Value>QuickBooks Online Plus</Value>
        </NameValue>
        <NameValue>
            <Name>PayrollFeature</Name>
            <Value>true</Value>
        </NameValue>
        <NameValue>
            <Name>AccountantFeature</Name>
            <Value>false</Value>
        </NameValue>
    </CompanyInfo>
</IntuitResponse>
```

## Sparse update companyinfo

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/companyinfo`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Sparse updating provides the ability to update a subset of properties for a given object; only elements specified in the request are updated. Missing elements are left untouched. The ID of the object to update is specified in the request body.​ Available with minor version 11.

### Request Body

Schema: `companyinforesponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "3",
  "CompanyName": "Larry's Bakery",
  "CompanyAddr": {
    "City": "Mountain View",
    "Country": "US",
    "Line1": "2500 Garcia Ave",
    "PostalCode": "94043",
    "CountrySubDivisionCode": "CA",
    "Id": "1"
  },
  "sparse": true,
  "LegalName": "Larry Smith's Bakery",
  "Id": "1"
}
```

#### XML example

```xml
<Invoice xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>1</Id>
    <SyncToken>3</SyncToken>
    <CompanyName>Larry's Bakery</CompanyName>
    <LegalName>Larry Smith's Bakery</LegalName>
    <CompanyAddr>
        <Id>1</Id>
        <Line1>2500 Garcia Ave</Line1>
        <City>Mountain View</City>
        <Country>US</Country>
        <CountrySubDivisionCode>CA</CountrySubDivisionCode>
        <PostalCode>94043</PostalCode>
    </CompanyAddr>
</Invoice>
```

### Returns

The invoice response body.

#### Example

```json
{
  "CompanyInfo": {
    "SyncToken": "4",
    "domain": "QBO",
    "LegalAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "SupportedLanguages": "en",
    "CompanyName": "Larry's Bakery",
    "Country": "US",
    "CompanyAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "sparse": false,
    "Id": "1",
    "WebAddr": {},
    "FiscalYearStartMonth": "January",
    "CustomerCommunicationAddr": {
      "City": "Mountain View",
      "Country": "US",
      "Line1": "2500 Garcia Ave",
      "PostalCode": "94043",
      "CountrySubDivisionCode": "CA",
      "Id": "1"
    },
    "PrimaryPhone": {
      "FreeFormNumber": "(650)944-4444"
    },
    "LegalName": "Larry Smith's Bakery",
    "CompanyStartDate": "2015-06-05",
    "EmployerId": "123456789",
    "Email": {
      "Address": "donotreply@intuit.com"
    },
    "NameValue": [
      {
        "Name": "NeoEnabled",
        "Value": "true"
      },
      {
        "Name": "IndustryType",
        "Value": "Bread and Bakery Product Manufacturing"
      },
      {
        "Name": "IndustryCode",
        "Value": "31181"
      },
      {
        "Name": "SubscriptionStatus",
        "Value": "PAID"
      },
      {
        "Name": "OfferingSku",
        "Value": "QuickBooks Online Plus"
      },
      {
        "Name": "PayrollFeature",
        "Value": "true"
      },
      {
        "Name": "AccountantFeature",
        "Value": "false"
      },
      {
        "Name": "IsQbdtMigrated",
        "Value": "true"
      },
      {
        "Name": "MigrationDate",
        "Value": "2024-09-14T01:47:34-07:00"
      },
      {
        "Name": "QBOIndustryType",
        "Value": "Manufacturing Businesses"
      },
      {
        "Name": "AssignedTime",
        "Value": "2024-09-14T01:47:34-07:00"
      }
    ],
    "MetaData": {
      "CreateTime": "2015-06-05T13:55:54-07:00",
      "LastUpdatedTime": "2015-07-06T08:51:50-07:00"
    }
  },
  "time": "2015-07-10T09:38:58.155-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-10T08:30:02.829-07:00">
    <CompanyInfo domain="QBO" sparse="false">
        <Id>1</Id>
        <SyncToken>4</SyncToken>
        <MetaData>
            <CreateTime>2015-06-05T13:55:54-07:00</CreateTime>
            <LastUpdatedTime>2015-07-06T08:51:50-07:00</LastUpdatedTime>
        </MetaData>
        <CompanyName>Larry's Bakery</CompanyName>
        <LegalName>Larry Smith's Bakery</LegalName>
        <CompanyAddr>
            <Id>1</Id>
            <Line1>2500 Garcia Ave</Line1>
            <City>Mountain View</City>
            <Country>US</Country>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94043</PostalCode>
        </CompanyAddr>
        <CustomerCommunicationAddr>
            <Id>1</Id>
            <Line1>2500 Garcia Ave</Line1>
            <City>Mountain View</City>
            <Country>US</Country>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94043</PostalCode>
        </CustomerCommunicationAddr>
        <LegalAddr>
            <Id>1</Id>
            <Line1>2500 Garcia Ave</Line1>
            <City>Mountain View</City>
            <Country>US</Country>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94043</PostalCode>
        </LegalAddr>
        <PrimaryPhone>
            <FreeFormNumber>(650)944-4444</FreeFormNumber>
        </PrimaryPhone>
        <CompanyStartDate>2015-06-05</CompanyStartDate>
        <EmployerId>123456789</EmployerId>
        <FiscalYearStartMonth>January</FiscalYearStartMonth>
        <Country>US</Country>
        <Email>
            <Address>donotreply@intuit.com</Address>
        </Email>
        <WebAddr/>
        <SupportedLanguages>en</SupportedLanguages>
        <NameValue>
            <Name>NeoEnabled</Name>
            <Value>true</Value>
        </NameValue>
        <NameValue>
            <Name>IndustryType</Name>
            <Value>Bread and Bakery Product Manufacturing</Value>
        </NameValue>
        <NameValue>
            <Name>IndustryCode</Name>
            <Value>31181</Value>
        </NameValue>
        <NameValue>
            <Name>SubscriptionStatus</Name>
            <Value>PAID</Value>
        </NameValue>
        <NameValue>
            <Name>OfferingSku</Name>
            <Value>QuickBooks Online Plus</Value>
        </NameValue>
        <NameValue>
            <Name>PayrollFeature</Name>
            <Value>true</Value>
        </NameValue>
        <NameValue>
            <Name>AccountantFeature</Name>
            <Value>false</Value>
        </NameValue>
    </CompanyInfo>
</IntuitResponse>
```
