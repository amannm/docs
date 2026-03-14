# Vendor

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/vendor
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Vendor
> Canonical entity: `Vendor`

The Vendor object represents the seller from whom your company purchases any service or product.

### Business Rules

- The `DisplayName`, `Title`, `GivenName`, `MiddleName`, `FamilyName`, `Suffix`, and `PrintOnCheckName` attributes must not contain colon (:), tab (\t), or newline (\n) characters.
- The `DisplayName` attribute must be unique across all other Customer, Employee, and Vendor objects.
- The `PrimaryEmailAddress` attribute must contain an at sign (@) and dot (.).
- The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required during object create.

## The vendor object

### vendorresponse

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

#### `Title`

Required: Conditionally required
Type: `String`
Max length: Maximum of 16 chars

Title of the person. This tag supports i18n, all locales. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes are required during create.

#### `GivenName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

Given name or first name of a person. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

#### `MiddleName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

Middle name of the person. The person can have zero or more middle names. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

#### `Suffix`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 16 chars

Suffix of the name. For example, `Jr`. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

#### `FamilyName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

Family name or the last name of the person. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

#### `Balance`

Type: `Decimal`
Traits: read only, filterable, sortable

Specifies the open balance amount or the amount unpaid by the customer. For the create operation, this represents the opening balance for the customer. When returned in response to the query request it represents the current open balance (unpaid amount) for that customer. Write-on-create, read-only otherwise.

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
Max length: Maximum of 500 chars

The name of the vendor as displayed. Must be unique across all Vendor, Customer, and Employee objects. Cannot be removed with sparse update. If not supplied, the system generates `DisplayName` by concatenating vendor name components supplied in the request from the following list: `Title`, `GivenName`, `MiddleName`, `FamilyName`, and `Suffix`.

#### `OtherContactInfo`

Required: Optional
Type: `ContactInfo`

List of ContactInfo entities of any contact info type.

<details>
<summary>Child attributes for `OtherContactInfo`</summary>

##### contactinfo

Model type: `object`

###### `Type`

Required: Optional
Type: `String`

The type of contact information. Valid values: `TelephoneNumber`

###### `Telephone`

Required: Optional
Type: `TelephoneNumber`

</details>

#### `APAccountRef`

Required: Optional
Type: `ReferenceType`
Minor version: 3
Locales: FR

Identifies the accounts payable account to be used for this supplier. Each supplier must have his own AP account. Applicable for France companies, only. Available when endpoint is evoked with the `minorversion=3` query parameter. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `APAccountRef.value` and `APAccountRef.name`, respectively.

<details>
<summary>Child attributes for `APAccountRef`</summary>

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

#### `TermRef`

Required: Optional
Type: `ReferenceType`

Reference to a default Term associated with this Vendor object. Query the Term name list resource to determine the appropriate Term object for this reference. Use `Term.Id` and `Term.Name` from that object for `TermRef.value` and `TermRef.name`, respectively.

<details>
<summary>Child attributes for `TermRef`</summary>

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

#### `Source`

Required: Optional
Type: `String`
Minor version: 59

The Source type of the transactions created by QuickBooks Commerce. Valid values include: `QBCommerce`

#### `GSTIN`

Required: Optional
Type: `String`
Max length: maximum of 15 chars
Minor version: 33
Locales: IN

GSTIN is an identification number assigned to every GST registered business.

#### `T4AEligible`

Required: Optional
Type: `Boolean`
Minor version: 56
Locales: CA

True if vendor is T4A eligible. Valid for CA locale

#### `Fax`

Required: Optional
Type: `TelephoneNumber`

Fax number.

<details>
<summary>Child attributes for `Fax`</summary>

##### telephonenumber30

Model type: `object`

###### `FreeFormNumber`

Required: Optional
Type: `String`
Max length: Maximum of 30 chars

Specifies the telephone number in free form.

</details>

#### `BusinessNumber`

Required: Optional
Type: `String`
Max length: maximum of 10 chars
Minor version: 33
Locales: IN

Also called, PAN (in India) is a code that acts as an identification for individuals, families and corporates, especially for those who pay taxes on their income.

#### `CurrencyRef`

Required: Optional
Type: `CurrencyRef`
Traits: read only

Reference to the currency in which all amounts associated with this vendor are expressed. Once set, it cannot be changed. If specified currency is not currently in the company's currency list, it is added. If not specified, currency for this vendor is the home currency of the company, as defined by `Preferences.CurrencyPrefs.HomeCurrency`. Read-only after object is created.

<details>
<summary>Child attributes for `CurrencyRef`</summary>

##### currencyref

Model type: `object`

###### `value`

Required: Required
Type: `String`

A three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on.

###### `name`

Required: Optional
Type: `String`

The full name of the currency.

</details>

#### `HasTPAR`

Required: Optional
Type: `Boolean`
Minor version: 40
Locales: AU

Indicate if the vendor has TPAR enabled. TPAR stands for Taxable Payments Annual Report. The TPAR is mandated by ATO to get the details payments that businesses make to contractors for providing services. Some government entities also need to report the grants they have paid in a TPAR.

#### `TaxReportingBasis`

Required: Optional
Type: `String`
Minor version: 3
Locales: FR

The method in which the supplier tracks their income. Applicable for France companies, only. Available when endpoint is evoked with the `minorversion=3` query parameter. Valid values include: `Cash` and `Accrual`.

#### `Mobile`

Required: Optional
Type: `TelephoneNumber`

Mobile phone number.

<details>
<summary>Child attributes for `Mobile`</summary>

##### telephonenumber30

Model type: `object`

###### `FreeFormNumber`

Required: Optional
Type: `String`
Max length: Maximum of 30 chars

Specifies the telephone number in free form.

</details>

#### `PrimaryPhone`

Required: Optional
Type: `TelephoneNumber`

Primary phone number.

<details>
<summary>Child attributes for `PrimaryPhone`</summary>

##### telephonenumber30

Model type: `object`

###### `FreeFormNumber`

Required: Optional
Type: `String`
Max length: Maximum of 30 chars

Specifies the telephone number in free form.

</details>

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable, sortable
Default: true

If true, this object is currently enabled for use by QuickBooks.

#### `AlternatePhone`

Required: Optional
Type: `TelephoneNumber`

Alternate phone number.

<details>
<summary>Child attributes for `AlternatePhone`</summary>

##### telephonenumber30

Model type: `object`

###### `FreeFormNumber`

Required: Optional
Type: `String`
Max length: Maximum of 30 chars

Specifies the telephone number in free form.

</details>

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

#### `Vendor1099`

Required: Optional
Type: `Boolean`

This vendor is an independent contractor; someone who is given a 1099-MISC form at the end of the year. A 1099 vendor is paid with regular checks, and taxes are not withheld on their behalf.

#### `CostRate`

Required: Optional
Type: `BigDecimal`

Pay rate of the vendor

#### `BillRate`

Required: Optional
Type: `Decimal`

BillRate can be set to specify this vendor's hourly billing rate.

#### `WebAddr`

Required: Optional
Type: `WebSiteAddress`

`Website address.`

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

#### `T5018Eligible`

Required: Optional
Type: `Boolean`
Minor version: 56
Locales: CA

True if vendor is T5018 eligible. Valid for CA locale

#### `CompanyName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

The name of the company associated with the person or organization.

#### `VendorPaymentBankDetail`

Required: Optional
Type: `VendorPaymentBankDetail`
Minor version: 40
Locales: AU

`Vendor Payment Bank Detail.`

<details>
<summary>Child attributes for `VendorPaymentBankDetail`</summary>

##### vendorpaymentbankdetail

Model type: `object`

###### `BankAccountName`

Required: Required if VendorPaymentBankDetail is present in the request.
Type: `String`

Name on the Bank Account

###### `BankBranchIdentifier`

Required: Required if VendorPaymentBankDetail is present in the request
Type: `String`

bank identification number used to identify the Bank Branch. 6 digit value in format xxx-xxx.

###### `BankAccountNumber`

Required: Required if VendorPaymentBankDetail is present in the request. In reponse the value is masked and last four digit is only returned
Type: `String`

Vendor's Bank Account number.

###### `StatementText`

Type: `String`
Max length: The maximum length of this field is 18 characters.

Text/note/comment for Remmittance

</details>

#### `TaxIdentifier`

Required: Optional
Type: `String`
Max length: Max 20 characters

The tax ID of the Person or Organization. The value is masked in responses, exposing only last four characters. For example, the ID of `123-45-6789` is returned as `XXXXXXX6789`.

#### `AcctNum`

Required: Optional
Type: `String`
Max length: Maximum of 100 chars

Name or number of the account associated with this vendor.

#### `GSTRegistrationType`

Required: Optional
Type: `String`
Max length: maximum of 15 chars
Minor version: 33
Locales: IN

For the filing of GSTR, transactions need to be classified depending on the type of vendor from whom the purchase is made. To facilitate this, we have introduced a new field as 'GST registration type'. Possible values are listed below:

`GST_REG_REG` GST registered- Regular. Customer who has a business which is registered under GST and has a GSTIN (doesn’t include customers registered under composition scheme, as an SEZ or as EOU's, STP's EHTP's etc.).

`GST_REG_COMP` GST registered-Composition. Customer who has a business which is registered under the composition scheme of GST and has a GSTIN.

`GST_UNREG` GST unregistered. Customer who has a business which is not registered under GST and does not have a GSTIN.

`CONSUMER` Consumer. Customer who is not registered under GST and is the final consumer of the service or product sold.

`OVERSEAS` Overseas. Customer who has a business which is located out of India.

`SEZ` SEZ. Customer who has a business which is registered under GST, has a GSTIN and is located in a SEZ or is a SEZ Developer.

`DEEMED` Deemed exports- EOU's, STP's EHTP's etc. Customer who has a business which is registered under GST and falls in the category of companies (EOU's, STP's EHTP's etc.), to which supplies are made they are termed as deemed exports.

#### `PrintOnCheckName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

Name of the person or organization as printed on a check. If not provided, this is populated from `DisplayName`. Cannot be removed with sparse update.

#### `BillAddr`

Required: Optional
Type: `PhysicalAddress`

`Default billing address.`
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
<summary>Child attributes for `BillAddr`</summary>

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

#### Example

```json
{
  "Vendor": {
    "PrimaryEmailAddr": {
      "Address": "Books@Intuit.com"
    },
    "Vendor1099": false,
    "domain": "QBO",
    "GivenName": "Bessie",
    "DisplayName": "Books by Bessie",
    "BillAddr": {
      "City": "Palo Alto",
      "Line1": "15 Main St.",
      "PostalCode": "94303",
      "Lat": "37.445013",
      "Long": "-122.1391443",
      "CountrySubDivisionCode": "CA",
      "Id": "31"
    },
    "SyncToken": "0",
    "PrintOnCheckName": "Books by Bessie",
    "FamilyName": "Williams",
    "PrimaryPhone": {
      "FreeFormNumber": "(650) 555-7745"
    },
    "AcctNum": "1345",
    "CompanyName": "Books by Bessie",
    "WebAddr": {
      "URI": "http://www.booksbybessie.co"
    },
    "sparse": false,
    "Active": true,
    "Balance": 0,
    "Id": "30",
    "MetaData": {
      "CreateTime": "2014-09-12T10:07:56-07:00",
      "LastUpdatedTime": "2014-09-17T11:13:46-07:00"
    }
  },
  "time": "2015-07-28T13:33:09.453-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T13:33:32.082-07:00">
    <Vendor domain="QBO" sparse="false">
        <Id>30</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-12T10:07:56-07:00</CreateTime>
            <LastUpdatedTime>2014-09-17T11:13:46-07:00</LastUpdatedTime>
        </MetaData>
        <GivenName>Bessie</GivenName>
        <FamilyName>Williams</FamilyName>
        <CompanyName>Books by Bessie</CompanyName>
        <DisplayName>Books by Bessie</DisplayName>
        <PrintOnCheckName>Books by Bessie</PrintOnCheckName>
        <Active>true</Active>
        <PrimaryPhone>
            <FreeFormNumber>(650) 555-7745</FreeFormNumber>
        </PrimaryPhone>
        <PrimaryEmailAddr>
            <Address>Books@Intuit.com</Address>
        </PrimaryEmailAddr>
        <WebAddr>
            <URI>http://www.booksbybessie.co</URI>
        </WebAddr>
        <BillAddr>
            <Id>31</Id>
            <Line1>15 Main St.</Line1>
            <City>Palo Alto</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94303</PostalCode>
            <Lat>37.445013</Lat>
            <Long>-122.1391443</Long>
        </BillAddr>
        <Balance>0</Balance>
        <AcctNum>1345</AcctNum>
        <Vendor1099>false</Vendor1099>
    </Vendor>
</IntuitResponse>
```

## Create a vendor

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/vendor`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Either the `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes are required during create.

### Request Body

The minimum elements to create a Vendor are listed here.

Schema: `vendorrequest`

<details>
<summary>Show schema for `vendorrequest`</summary>

#### vendorrequest

Model type: `object`

##### `Suffix`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 16 chars

Suffix of the name. For example, `Jr`. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

##### `Title`

Required: Conditionally required
Type: `String`
Max length: Maximum of 16 chars

Title of the person. This tag supports i18n, all locales. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, `Suffix`, or `FullyQualifiedName` attributes are required during create.

##### `MiddleName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

Middle name of the person. The person can have zero or more middle names. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

##### `FamilyName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

Family name or the last name of the person. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

##### `GivenName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

Given name or first name of a person. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

##### `DisplayName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 500 chars

The name of the vendor as displayed. Must be unique across all Vendor, Customer, and Employee objects. Cannot be removed with sparse update. If not supplied, the system generates `DisplayName` by concatenating vendor name components supplied in the request from the following list: `Title`, `GivenName`, `MiddleName`, `FamilyName`, and `Suffix`.

</details>

#### Example

```json
{
  "PrimaryEmailAddr": {
    "Address": "dbradley@myemail.com"
  },
  "WebAddr": {
    "URI": "http://DiannesAutoShop.com"
  },
  "PrimaryPhone": {
    "FreeFormNumber": "(650) 555-2342"
  },
  "DisplayName": "Dianne's Auto Shop",
  "Suffix": "Sr.",
  "Title": "Ms.",
  "Mobile": {
    "FreeFormNumber": "(650) 555-2000"
  },
  "FamilyName": "Bradley",
  "TaxIdentifier": "99-5688293",
  "AcctNum": "35372649",
  "CompanyName": "Dianne's Auto Shop",
  "BillAddr": {
    "City": "Millbrae",
    "Country": "U.S.A",
    "Line3": "29834 Mustang Ave.",
    "Line2": "Dianne Bradley",
    "Line1": "Dianne's Auto Shop",
    "PostalCode": "94030",
    "CountrySubDivisionCode": "CA"
  },
  "GivenName": "Dianne",
  "PrintOnCheckName": "Dianne's Auto Shop"
}
```

#### XML example

```xml
<Vendor xmlns="http://schema.intuit.com/finance/v3" sparse="false">
  <Title>Mr.</Title>
  <GivenName>John</GivenName>
  <MiddleName>S.</MiddleName>
  <FamilyName>Bradley</FamilyName>
  <Suffix>Jr.</Suffix>
  <CompanyName>John's Cakes</CompanyName>
  <DisplayName>John's Cakes and Pies</DisplayName>
  <PrintOnCheckName>John's Cakes</PrintOnCheckName>
  <PrimaryPhone>
    <FreeFormNumber>(650) 555-2000</FreeFormNumber>
  </PrimaryPhone>
  <Mobile>
    <FreeFormNumber>(650) 555-2001</FreeFormNumber>
  </Mobile>
  <PrimaryEmailAddr>
    <Address>john.bradley@intuit.com</Address>
  </PrimaryEmailAddr>
</Vendor>
```

### Returns

Returns the newly created Vendor object.

#### Example

```json
{
  "Vendor": {
    "domain": "QBO",
    "PrimaryEmailAddr": {
      "Address": "dbradley@myemail.com"
    },
    "DisplayName": "Dianne's Auto Shop",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "GivenName": "Dianne",
    "Title": "Ms.",
    "PrimaryPhone": {
      "FreeFormNumber": "(650) 555-2342"
    },
    "Active": true,
    "MetaData": {
      "CreateTime": "2015-07-28T12:51:21-07:00",
      "LastUpdatedTime": "2015-07-28T12:51:21-07:00"
    },
    "Vendor1099": false,
    "BillAddr": {
      "City": "Millbrae",
      "Country": "U.S.A",
      "Line3": "29834 Mustang Ave.",
      "Line2": "Dianne Bradley",
      "Line1": "Dianne's Auto Shop",
      "PostalCode": "94030",
      "CountrySubDivisionCode": "CA",
      "Id": "423"
    },
    "Mobile": {
      "FreeFormNumber": "(650) 555-2000"
    },
    "WebAddr": {
      "URI": "http://DiannesAutoShop.com"
    },
    "Balance": 0,
    "SyncToken": "0",
    "Suffix": "Sr.",
    "CompanyName": "Dianne's Auto Shop",
    "FamilyName": "Bradley",
    "TaxIdentifier": "99-5688293",
    "AcctNum": "35372649",
    "PrintOnCheckName": "Dianne's Auto Shop",
    "sparse": false,
    "Id": "137"
  },
  "time": "2015-07-28T12:51:21.326-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T13:22:59.616-07:00">
    <Vendor domain="QBO" sparse="false">
        <Id>139</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T13:22:58-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T13:22:58-07:00</LastUpdatedTime>
        </MetaData>
        <Title>Mr.</Title>
        <GivenName>John</GivenName>
        <MiddleName>S.</MiddleName>
        <FamilyName>Bradley</FamilyName>
        <Suffix>Jr.</Suffix>
        <CompanyName>John's Cakes</CompanyName>
        <DisplayName>John's Cakes and Pies</DisplayName>
        <PrintOnCheckName>John's Cakes</PrintOnCheckName>
        <Active>true</Active>
        <PrimaryPhone>
            <FreeFormNumber>(650) 555-2000</FreeFormNumber>
        </PrimaryPhone>
        <Mobile>
            <FreeFormNumber>(650) 555-2001</FreeFormNumber>
        </Mobile>
        <PrimaryEmailAddr>
            <Address>john.bradley@intuit.com</Address>
        </PrimaryEmailAddr>
        <Balance>0</Balance>
        <Vendor1099>false</Vendor1099>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
    </Vendor>
</IntuitResponse>
```

## Query a vendor

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from vendor where MetaData.LastUpdatedTime > '2014-09-17T15:28:48-07:00'"
```

#### XML example

```sql
select * from vendor where MetaData.LastUpdatedTime > '2014-09-17T15:28:48-07:00'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Vendor": [
      {
        "Vendor1099": false,
        "domain": "QBO",
        "DisplayName": "Bob's Burger Joint",
        "SyncToken": "0",
        "PrintOnCheckName": "Bob's Burger Joint",
        "sparse": false,
        "Active": true,
        "Balance": 390.0,
        "Id": "56",
        "MetaData": {
          "CreateTime": "2014-10-03T14:28:52-07:00",
          "LastUpdatedTime": "2015-07-14T12:37:57-07:00"
        }
      },
      {
        "Vendor1099": false,
        "domain": "QBO",
        "DisplayName": "Cal Telephone",
        "BillAddr": {
          "City": "Palo Alto",
          "Line1": "10 Main St.",
          "PostalCode": "94303",
          "Lat": "37.445013",
          "Long": "-122.1391443",
          "CountrySubDivisionCode": "CA",
          "Id": "33"
        },
        "SyncToken": "0",
        "CompanyName": "Cal Telephone",
        "TermRef": {
          "value": "1"
        },
        "PrimaryPhone": {
          "FreeFormNumber": "(650) 555-1616"
        },
        "PrintOnCheckName": "Cal Telephone",
        "sparse": false,
        "Active": true,
        "Balance": 0,
        "Id": "32",
        "MetaData": {
          "CreateTime": "2014-09-12T10:13:24-07:00",
          "LastUpdatedTime": "2014-09-19T12:55:23-07:00"
        }
      },
      {
        "Vendor1099": false,
        "domain": "QBO",
        "GivenName": "Melanie",
        "DisplayName": "Hall Properties",
        "sparse": false,
        "SyncToken": "0",
        "Mobile": {
          "FreeFormNumber": "(973) 888-6222"
        },
        "PrintOnCheckName": "Hall Properties",
        "PrimaryPhone": {
          "FreeFormNumber": "(973) 555-3827"
        },
        "FamilyName": "Hall",
        "TaxIdentifier": "XXXXXXXX2222",
        "AcctNum": "55642",
        "CompanyName": "Hall Properties",
        "WebAddr": {
          "URI": "http://www.hallproperties.intuit.org"
        },
        "BillAddr": {
          "City": "South Orange",
          "Line1": "P.O.Box 357",
          "PostalCode": "07079",
          "Lat": "40.7489277",
          "Long": "-74.2609903",
          "CountrySubDivisionCode": "NJ",
          "Id": "36"
        },
        "Active": true,
        "Balance": 0,
        "Id": "40",
        "MetaData": {
          "CreateTime": "2014-09-12T10:24:28-07:00",
          "LastUpdatedTime": "2014-09-18T13:43:08-07:00"
        }
      },
      {
        "Vendor1099": false,
        "domain": "QBO",
        "GivenName": "Geoff",
        "DisplayName": "Hicks Hardware",
        "BillAddr": {
          "City": "Middlefield",
          "Line1": "42 Main St.",
          "PostalCode": "94303",
          "Lat": "37.445013",
          "Long": "-122.1391443",
          "CountrySubDivisionCode": "CA",
          "Id": "37"
        },
        "SyncToken": "0",
        "Mobile": {
          "FreeFormNumber": "(650) 445-6666"
        },
        "PrintOnCheckName": "Hicks Hardware",
        "FamilyName": "Hicks",
        "PrimaryPhone": {
          "FreeFormNumber": "(650) 554-1973"
        },
        "AcctNum": "556223",
        "CompanyName": "Hicks Hardware",
        "WebAddr": {
          "URI": "http://Hickshardware.co"
        },
        "sparse": false,
        "Active": true,
        "Balance": 0,
        "Id": "41",
        "MetaData": {
          "CreateTime": "2014-09-12T10:26:56-07:00",
          "LastUpdatedTime": "2014-09-18T13:01:57-07:00"
        }
      },
      {
        "PrimaryEmailAddr": {
          "Address": "Materials@intuit.com"
        },
        "Vendor1099": false,
        "domain": "QBO",
        "GivenName": "Julie",
        "DisplayName": "Norton Lumber and Building Materials",
        "BillAddr": {
          "City": "Middlefield",
          "Line1": "4528 Country Road",
          "PostalCode": "94303",
          "Lat": "37.3752919",
          "Long": "-122.1692159",
          "CountrySubDivisionCode": "CA",
          "Id": "40"
        },
        "SyncToken": "0",
        "PrintOnCheckName": "Norton Lumber and Building Materials",
        "FamilyName": "Norton",
        "PrimaryPhone": {
          "FreeFormNumber": "(650) 363-6578"
        },
        "AcctNum": "32980256",
        "CompanyName": "Norton Lumber and Building Materials",
        "sparse": false,
        "Active": true,
        "Balance": 0,
        "Id": "46",
        "MetaData": {
          "CreateTime": "2014-09-12T10:32:55-07:00",
          "LastUpdatedTime": "2015-01-16T16:00:29-08:00"
        }
      },
      {
        "Vendor1099": false,
        "domain": "QBO",
        "PrimaryEmailAddr": {
          "Address": "utilities@noemail.com"
        },
        "DisplayName": "PG&E",
        "BillAddr": {
          "City": "Palo Alto",
          "Line1": "4 Main St.",
          "PostalCode": "94303",
          "Lat": "37.445013",
          "Long": "-122.1391443",
          "CountrySubDivisionCode": "CA",
          "Id": "42"
        },
        "SyncToken": "1",
        "CompanyName": "PG&E",
        "PrimaryPhone": {
          "FreeFormNumber": "(888) 555-9465"
        },
        "AcctNum": "00649587213",
        "PrintOnCheckName": "PG&E",
        "sparse": false,
        "Active": true,
        "Balance": 0,
        "Id": "48",
        "MetaData": {
          "CreateTime": "2014-09-12T10:36:57-07:00",
          "LastUpdatedTime": "2015-01-16T15:36:20-08:00"
        }
      },
      {
        "Vendor1099": false,
        "domain": "QBO",
        "DisplayName": "QuickBooks Payments",
        "SyncToken": "0",
        "PrintOnCheckName": "QuickBooks Payments",
        "sparse": false,
        "Active": true,
        "Balance": 0,
        "Id": "63",
        "MetaData": {
          "CreateTime": "2015-04-13T13:42:23-07:00",
          "LastUpdatedTime": "2015-04-13T13:42:23-07:00"
        }
      },
      {
        "Vendor1099": false,
        "domain": "QBO",
        "GivenName": "Jenny",
        "DisplayName": "Robertson & Associates",
        "BillAddr": {
          "City": "Bayshore",
          "Line1": "P.O. Box 147",
          "PostalCode": "94326",
          "Lat": "45.2720537",
          "Long": "-79.7935909",
          "CountrySubDivisionCode": "CA",
          "Id": "43"
        },
        "SyncToken": "0",
        "PrintOnCheckName": "Robertson & Associates",
        "FamilyName": "Robertson",
        "PrimaryPhone": {
          "FreeFormNumber": "(650) 557-1111"
        },
        "AcctNum": "000005641",
        "CompanyName": "Robertson & Associates",
        "sparse": false,
        "Active": true,
        "Balance": 95.0,
        "Id": "49",
        "MetaData": {
          "CreateTime": "2014-09-12T10:38:12-07:00",
          "LastUpdatedTime": "2015-06-30T15:09:07-07:00"
        }
      },
      {
        "Vendor1099": false,
        "domain": "QBO",
        "DisplayName": "Squeaky Kleen Car Wash",
        "SyncToken": "0",
        "PrintOnCheckName": "Squeaky Kleen Car Wash",
        "sparse": false,
        "Active": true,
        "Balance": 0,
        "Id": "57",
        "MetaData": {
          "CreateTime": "2014-10-03T14:29:35-07:00",
          "LastUpdatedTime": "2014-10-03T14:29:35-07:00"
        }
      },
      {
        "PrimaryEmailAddr": {
          "Address": "tim.philip@timphilipmasonry.com"
        },
        "Vendor1099": false,
        "domain": "QBO",
        "GivenName": "Tim",
        "DisplayName": "Tim Philip Masonry",
        "sparse": false,
        "SyncToken": "0",
        "Mobile": {
          "FreeFormNumber": "(650) 555-1549"
        },
        "PrintOnCheckName": "Tim Philip Masonry",
        "PrimaryPhone": {
          "FreeFormNumber": "(800) 556-1254"
        },
        "FamilyName": "Philip",
        "TaxIdentifier": "XXXXXXXX5555",
        "AcctNum": "0078965",
        "CompanyName": "Tim Philip Masonry",
        "WebAddr": {
          "URI": "http://www.bricksbytim4less.co"
        },
        "BillAddr": {
          "City": "Middlefield",
          "Line1": "3948 Elm St.",
          "PostalCode": "94482",
          "Lat": "37.4604972",
          "Long": "-122.1547528",
          "CountrySubDivisionCode": "CA",
          "Id": "45"
        },
        "Active": true,
        "Balance": 0,
        "Id": "51",
        "MetaData": {
          "CreateTime": "2014-09-12T10:42:31-07:00",
          "LastUpdatedTime": "2014-09-18T13:06:58-07:00"
        }
      }
    ],
    "maxResults": 10
  },
  "time": "2015-07-28T13:29:10.643-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T13:28:28.395-07:00">
    <QueryResponse startPosition="1" maxResults="10">
        <Vendor domain="QBO" sparse="false">
            <Id>56</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-10-03T14:28:52-07:00</CreateTime>
                <LastUpdatedTime>2015-07-14T12:37:57-07:00</LastUpdatedTime>
            </MetaData>
            <DisplayName>Bob's Burger Joint</DisplayName>
            <PrintOnCheckName>Bob's Burger Joint</PrintOnCheckName>
            <Active>true</Active>
            <Balance>390.00</Balance>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>32</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-12T10:13:24-07:00</CreateTime>
                <LastUpdatedTime>2014-09-19T12:55:23-07:00</LastUpdatedTime>
            </MetaData>
            <CompanyName>Cal Telephone</CompanyName>
            <DisplayName>Cal Telephone</DisplayName>
            <PrintOnCheckName>Cal Telephone</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(650) 555-1616</FreeFormNumber>
            </PrimaryPhone>
            <BillAddr>
                <Id>33</Id>
                <Line1>10 Main St.</Line1>
                <City>Palo Alto</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94303</PostalCode>
                <Lat>37.445013</Lat>
                <Long>-122.1391443</Long>
            </BillAddr>
            <TermRef>1</TermRef>
            <Balance>0</Balance>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>40</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-12T10:24:28-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T13:43:08-07:00</LastUpdatedTime>
            </MetaData>
            <GivenName>Melanie</GivenName>
            <FamilyName>Hall</FamilyName>
            <CompanyName>Hall Properties</CompanyName>
            <DisplayName>Hall Properties</DisplayName>
            <PrintOnCheckName>Hall Properties</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(973) 555-3827</FreeFormNumber>
            </PrimaryPhone>
            <Mobile>
                <FreeFormNumber>(973) 888-6222</FreeFormNumber>
            </Mobile>
            <WebAddr>
                <URI>http://www.hallproperties.intuit.org</URI>
            </WebAddr>
            <BillAddr>
                <Id>36</Id>
                <Line1>P.O.Box 357</Line1>
                <City>South Orange</City>
                <CountrySubDivisionCode>NJ</CountrySubDivisionCode>
                <PostalCode>07079</PostalCode>
                <Lat>40.7489277</Lat>
                <Long>-74.2609903</Long>
            </BillAddr>
            <TaxIdentifier>22-2222222</TaxIdentifier>
            <Balance>0</Balance>
            <AcctNum>55642</AcctNum>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>41</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-12T10:26:56-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T13:01:57-07:00</LastUpdatedTime>
            </MetaData>
            <GivenName>Geoff</GivenName>
            <FamilyName>Hicks</FamilyName>
            <CompanyName>Hicks Hardware</CompanyName>
            <DisplayName>Hicks Hardware</DisplayName>
            <PrintOnCheckName>Hicks Hardware</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(650) 554-1973</FreeFormNumber>
            </PrimaryPhone>
            <Mobile>
                <FreeFormNumber>(650) 445-6666</FreeFormNumber>
            </Mobile>
            <WebAddr>
                <URI>http://Hickshardware.co</URI>
            </WebAddr>
            <BillAddr>
                <Id>37</Id>
                <Line1>42 Main St.</Line1>
                <City>Middlefield</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94303</PostalCode>
                <Lat>37.445013</Lat>
                <Long>-122.1391443</Long>
            </BillAddr>
            <Balance>0</Balance>
            <AcctNum>556223</AcctNum>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>46</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-12T10:32:55-07:00</CreateTime>
                <LastUpdatedTime>2015-01-16T16:00:29-08:00</LastUpdatedTime>
            </MetaData>
            <GivenName>Julie</GivenName>
            <FamilyName>Norton</FamilyName>
            <CompanyName>Norton Lumber and Building Materials</CompanyName>
            <DisplayName>Norton Lumber and Building Materials</DisplayName>
            <PrintOnCheckName>Norton Lumber and Building Materials</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(650) 363-6578</FreeFormNumber>
            </PrimaryPhone>
            <PrimaryEmailAddr>
                <Address>Materials@intuit.com</Address>
            </PrimaryEmailAddr>
            <BillAddr>
                <Id>40</Id>
                <Line1>4528 Country Road</Line1>
                <City>Middlefield</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94303</PostalCode>
                <Lat>37.3752919</Lat>
                <Long>-122.1692159</Long>
            </BillAddr>
            <Balance>0</Balance>
            <AcctNum>32980256</AcctNum>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>48</Id>
            <SyncToken>1</SyncToken>
            <MetaData>
                <CreateTime>2014-09-12T10:36:57-07:00</CreateTime>
                <LastUpdatedTime>2015-01-16T15:36:20-08:00</LastUpdatedTime>
            </MetaData>
            <CompanyName>PG&amp;E</CompanyName>
            <DisplayName>PG&amp;E</DisplayName>
            <PrintOnCheckName>PG&amp;E</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(888) 555-9465</FreeFormNumber>
            </PrimaryPhone>
            <PrimaryEmailAddr>
                <Address>utilities@noemail.com</Address>
            </PrimaryEmailAddr>
            <BillAddr>
                <Id>42</Id>
                <Line1>4 Main St.</Line1>
                <City>Palo Alto</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94303</PostalCode>
                <Lat>37.445013</Lat>
                <Long>-122.1391443</Long>
            </BillAddr>
            <Balance>0</Balance>
            <AcctNum>00649587213</AcctNum>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>63</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-04-13T13:42:23-07:00</CreateTime>
                <LastUpdatedTime>2015-04-13T13:42:23-07:00</LastUpdatedTime>
            </MetaData>
            <DisplayName>QuickBooks Payments</DisplayName>
            <PrintOnCheckName>QuickBooks Payments</PrintOnCheckName>
            <Active>true</Active>
            <Balance>0</Balance>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>49</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-12T10:38:12-07:00</CreateTime>
                <LastUpdatedTime>2015-06-30T15:09:07-07:00</LastUpdatedTime>
            </MetaData>
            <GivenName>Jenny</GivenName>
            <FamilyName>Robertson</FamilyName>
            <CompanyName>Robertson &amp; Associates</CompanyName>
            <DisplayName>Robertson &amp; Associates</DisplayName>
            <PrintOnCheckName>Robertson &amp; Associates</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(650) 557-1111</FreeFormNumber>
            </PrimaryPhone>
            <BillAddr>
                <Id>43</Id>
                <Line1>P.O. Box 147</Line1>
                <City>Bayshore</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94326</PostalCode>
                <Lat>45.2720537</Lat>
                <Long>-79.7935909</Long>
            </BillAddr>
            <Balance>95.00</Balance>
            <AcctNum>000005641</AcctNum>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>57</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-10-03T14:29:35-07:00</CreateTime>
                <LastUpdatedTime>2014-10-03T14:29:35-07:00</LastUpdatedTime>
            </MetaData>
            <DisplayName>Squeaky Kleen Car Wash</DisplayName>
            <PrintOnCheckName>Squeaky Kleen Car Wash</PrintOnCheckName>
            <Active>true</Active>
            <Balance>0</Balance>
            <Vendor1099>false</Vendor1099>
        </Vendor>
        <Vendor domain="QBO" sparse="false">
            <Id>51</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-12T10:42:31-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T13:06:58-07:00</LastUpdatedTime>
            </MetaData>
            <GivenName>Tim</GivenName>
            <FamilyName>Philip</FamilyName>
            <CompanyName>Tim Philip Masonry</CompanyName>
            <DisplayName>Tim Philip Masonry</DisplayName>
            <PrintOnCheckName>Tim Philip Masonry</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(800) 556-1254</FreeFormNumber>
            </PrimaryPhone>
            <Mobile>
                <FreeFormNumber>(650) 555-1549</FreeFormNumber>
            </Mobile>
            <PrimaryEmailAddr>
                <Address>tim.philip@timphilipmasonry.com</Address>
            </PrimaryEmailAddr>
            <WebAddr>
                <URI>http://www.bricksbytim4less.co</URI>
            </WebAddr>
            <BillAddr>
                <Id>45</Id>
                <Line1>3948 Elm St.</Line1>
                <City>Middlefield</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94482</PostalCode>
                <Lat>37.4604972</Lat>
                <Long>-122.1547528</Long>
            </BillAddr>
            <TaxIdentifier>55-5555555</TaxIdentifier>
            <Balance>0</Balance>
            <AcctNum>0078965</AcctNum>
            <Vendor1099>false</Vendor1099>
        </Vendor>
    </QueryResponse>
</IntuitResponse>
```

## Read a vendor

### Definition

- **Operation:** `GET /v3/company/<realmID>/vendor/<vendorId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Vendor object that has been previously created.

### Returns

Returns the Vendor object.

#### Example

```json
{
  "Vendor": {
    "PrimaryEmailAddr": {
      "Address": "Books@Intuit.com"
    },
    "Vendor1099": false,
    "domain": "QBO",
    "GivenName": "Bessie",
    "DisplayName": "Books by Bessie",
    "BillAddr": {
      "City": "Palo Alto",
      "Line1": "15 Main St.",
      "PostalCode": "94303",
      "Lat": "37.445013",
      "Long": "-122.1391443",
      "CountrySubDivisionCode": "CA",
      "Id": "31"
    },
    "SyncToken": "0",
    "PrintOnCheckName": "Books by Bessie",
    "FamilyName": "Williams",
    "PrimaryPhone": {
      "FreeFormNumber": "(650) 555-7745"
    },
    "AcctNum": "1345",
    "CompanyName": "Books by Bessie",
    "WebAddr": {
      "URI": "http://www.booksbybessie.co"
    },
    "sparse": false,
    "Active": true,
    "Balance": 0,
    "Id": "30",
    "MetaData": {
      "CreateTime": "2014-09-12T10:07:56-07:00",
      "LastUpdatedTime": "2014-09-17T11:13:46-07:00"
    }
  },
  "time": "2015-07-28T13:33:09.453-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T13:33:32.082-07:00">
    <Vendor domain="QBO" sparse="false">
        <Id>30</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-12T10:07:56-07:00</CreateTime>
            <LastUpdatedTime>2014-09-17T11:13:46-07:00</LastUpdatedTime>
        </MetaData>
        <GivenName>Bessie</GivenName>
        <FamilyName>Williams</FamilyName>
        <CompanyName>Books by Bessie</CompanyName>
        <DisplayName>Books by Bessie</DisplayName>
        <PrintOnCheckName>Books by Bessie</PrintOnCheckName>
        <Active>true</Active>
        <PrimaryPhone>
            <FreeFormNumber>(650) 555-7745</FreeFormNumber>
        </PrimaryPhone>
        <PrimaryEmailAddr>
            <Address>Books@Intuit.com</Address>
        </PrimaryEmailAddr>
        <WebAddr>
            <URI>http://www.booksbybessie.co</URI>
        </WebAddr>
        <BillAddr>
            <Id>31</Id>
            <Line1>15 Main St.</Line1>
            <City>Palo Alto</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94303</PostalCode>
            <Lat>37.445013</Lat>
            <Long>-122.1391443</Long>
        </BillAddr>
        <Balance>0</Balance>
        <AcctNum>1345</AcctNum>
        <Vendor1099>false</Vendor1099>
    </Vendor>
</IntuitResponse>
```

## Full update a vendor

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/vendor`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing Vendor object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.Add the query parameter, `include=updateaccountontxns&minorversion=5`, to the endpoint to automatically update the AP account on historical transactions (from soft close date forward) for this vendor with that defined by the `APAccountRef` attribute in the Vendor object. Updates on soft closed transacitons associated will fail.

### Request Body

Schema: `vendorresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "PrimaryEmailAddr": {
    "Address": "Books@Intuit.com"
  },
  "Vendor1099": false,
  "domain": "QBO",
  "GivenName": "Bessie",
  "DisplayName": "Books by Bessie",
  "BillAddr": {
    "City": "Palo Alto",
    "Line1": "15 Main St.",
    "PostalCode": "94303",
    "Lat": "37.445013",
    "Long": "-122.1391443",
    "CountrySubDivisionCode": "CA",
    "Id": "31"
  },
  "SyncToken": "1",
  "PrintOnCheckName": "Books by Bessie and Joan",
  "FamilyName": "Williams",
  "PrimaryPhone": {
    "FreeFormNumber": "(650) 555-7745"
  },
  "AcctNum": "13451234",
  "CompanyName": "Books by Bessie",
  "WebAddr": {
    "URI": "http://www.booksbybessie.co"
  },
  "sparse": false,
  "Active": true,
  "Balance": 0,
  "Id": "30",
  "MetaData": {
    "CreateTime": "2014-09-12T10:07:56-07:00",
    "LastUpdatedTime": "2015-07-28T13:34:38-07:00"
  }
}
```

#### XML example

```xml
<Vendor xmlns="http://schema.intuit.com/finance/v3" sparse="false">
     <Id>30</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-12T10:07:56-07:00</CreateTime>
            <LastUpdatedTime>2014-09-17T11:13:46-07:00</LastUpdatedTime>
        </MetaData>
        <GivenName>Bessie</GivenName>
        <FamilyName>Williams</FamilyName>
        <CompanyName>Books by Bessie</CompanyName>
        <DisplayName>Books by Bessie</DisplayName>
        <PrintOnCheckName>Books by Bessie</PrintOnCheckName>
        <Active>true</Active>
        <PrimaryPhone>
            <FreeFormNumber>(650) 555-7745</FreeFormNumber>
        </PrimaryPhone>
        <PrimaryEmailAddr>
            <Address>Books@Intuit.com</Address>
        </PrimaryEmailAddr>
        <WebAddr>
            <URI>http://www.booksbybessie.co</URI>
        </WebAddr>
        <BillAddr>
            <Id>31</Id>
            <Line1>15 Main St.</Line1>
            <City>Palo Alto</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94303</PostalCode>
            <Lat>37.445013</Lat>
            <Long>-122.1391443</Long>
        </BillAddr>
        <Balance>0</Balance>
        <AcctNum>13451234</AcctNum>
        <Vendor1099>false</Vendor1099>
</Vendor>
```

### Returns

The Vendor response body.

#### Example

```json
{
  "Vendor": {
    "PrimaryEmailAddr": {
      "Address": "Books@Intuit.com"
    },
    "Vendor1099": false,
    "domain": "QBO",
    "GivenName": "Bessie",
    "DisplayName": "Books by Bessie",
    "BillAddr": {
      "City": "Palo Alto",
      "Line1": "15 Main St.",
      "PostalCode": "94303",
      "Lat": "37.445013",
      "Long": "-122.1391443",
      "CountrySubDivisionCode": "CA",
      "Id": "31"
    },
    "SyncToken": "2",
    "PrintOnCheckName": "Books by Bessie and Joan",
    "FamilyName": "Williams",
    "PrimaryPhone": {
      "FreeFormNumber": "(650) 555-7745"
    },
    "AcctNum": "13451234",
    "CompanyName": "Books by Bessie",
    "WebAddr": {
      "URI": "http://www.booksbybessie.co"
    },
    "sparse": false,
    "Active": true,
    "Balance": 0,
    "Id": "30",
    "MetaData": {
      "CreateTime": "2014-09-12T10:07:56-07:00",
      "LastUpdatedTime": "2015-07-28T13:37:05-07:00"
    }
  },
  "time": "2015-07-28T13:37:07.196-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T13:34:39.534-07:00">
  <Vendor domain="QBO" sparse="false">
    <Id>30</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2014-09-12T10:07:56-07:00</CreateTime>
      <LastUpdatedTime>2015-07-28T13:34:38-07:00</LastUpdatedTime>
    </MetaData>
    <GivenName>Bessie</GivenName>
    <FamilyName>Williams</FamilyName>
    <CompanyName>Books by Bessie</CompanyName>
    <DisplayName>Books by Bessie</DisplayName>
    <PrintOnCheckName>Books by Bessie</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
      <FreeFormNumber>(650) 555-7745</FreeFormNumber>
    </PrimaryPhone>
    <PrimaryEmailAddr>
      <Address>Books@Intuit.com</Address>
    </PrimaryEmailAddr>
    <WebAddr>
      <URI>http://www.booksbybessie.co</URI>
    </WebAddr>
    <BillAddr>
      <Id>31</Id>
      <Line1>15 Main St.</Line1>
      <City>Palo Alto</City>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>94303</PostalCode>
      <Lat>37.445013</Lat>
      <Long>-122.1391443</Long>
    </BillAddr>
    <Balance>0</Balance>
    <AcctNum>13451234</AcctNum>
    <Vendor1099>false</Vendor1099>
  </Vendor>
</IntuitResponse>
```
