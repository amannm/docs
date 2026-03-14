# Customer

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/customer
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Most commonly used](index.md) / Customer
> Canonical entity: `Customer`

A customer is a consumer of the service or product that your business offers. An individual customer can have an underlying nested structure, with a parent customer (the top-level object) having zero or more sub-customers and jobs associated with it.

- Sub-customer examples:
- Job examples:

Use the Customer resource to create parent customer objects, sub-customer objects, and job objects according to your business requirements. Use the `ParentRef` and `Job` attributes in the customer object to designate whether the object is a parent, nested job or nested sub-customer.

- First, create parent customer objects: Set `Job` to `false` (default) and do not define `ParentRef`.
- Then, create sub-customer and job objects: Set `Job` to `true` and set `ParentRef` to reference parent customer object.

Going forward, specify an individual parent customer object, sub-customer object, or job object in sales transactions via the transaction's CustomerRef attribute, based on your business requirements.See QuickBooks product documentation for more about sub-customers and jobs.

### Business Rules

- The `DisplayName`, `Title`, `GivenName`, `MiddleName`, `FamilyName`, `Suffix`, and `PrintOnCheckName` attributes must not contain colon (:), tab (\t), or newline (\n) characters.
- The `DisplayName` attribute must be unique across all other customer, employee, and vendor objects.
- The `PrimaryEmailAddress` attribute must contain an at sign (@) and dot (.).
- Nested Customer objects can be used to define sub-customers, jobs, or a combination of both, under a parent.
- Up to four levels of nesting can be defined under a top-level parent Customer object.
- The `Job` attribute defines whether the object is a parent customer or nested sub-customer/job.
- The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required during object create.

## The Customer object

### customerresponse

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

#### `DisplayName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 500 chars

The name of the person or organization as displayed. Must be unique across all Customer, Vendor, and Employee objects. Cannot be removed with sparse update. If not supplied, the system generates `DisplayName` by concatenating customer name components supplied in the request from the following list: `Title`, `GivenName`, `MiddleName`, `FamilyName`, and `Suffix`.

#### `Title`

Required: Conditionally required
Type: `String`
Max length: maximum of 16 chars

Title of the person. This tag supports i18n, all locales. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required.

#### `GivenName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Given name or first name of a person. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required.

#### `MiddleName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Middle name of the person. The person can have zero or more middle names. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required.

#### `Suffix`

Required: Conditionally required
Type: `String`
Max length: maximum of 16 chars

Suffix of the name. For example, `Jr`. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required.

#### `FamilyName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Family name or the last name of the person. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required.

#### `FullyQualifiedName`

Type: `String`
Traits: read only, system defined, filterable, sortable

Fully qualified name of the object. The fully qualified name prepends the topmost parent, followed by each sub element separated by colons. Takes the form of `Customer:Job:Sub-job`. System generated. Limited to 5 levels.

#### `Level`

Type: `Integer`
Traits: read only, system defined
Default: 0

Specifies the level of the hierarchy in which the entity is located. Zero specifies the top level of the hierarchy; anything above will be level with respect to the parent. Constraints:up to 5 levels

#### `TaxExemptionReasonId`

Type: `Numeric Id`
Minor version: 10

The tax exemption reason associated with this customer object. Applicable if automated sales tax is enabled (`Preferences.TaxPrefs.PartnerTaxEnabled` is set to `true`) for the company. Set `TaxExemptionReasonId:` to one of the following:

| Id | Reason |
| --- | --- |
| 1 | Federal government |
| 2 | State government |
| 3 | Local government |
| 4 | Tribal government |
| 5 | Charitable organization |
| 6 | Religious organization |
| 7 | Educational organization |
| 8 | Hospital |
| 9 | Resale |
| 10 | Direct pay permit |
| 11 | Multiple points of use |
| 12 | Direct mail |
| 13 | Agricultural production |
| 14 | Industrial production / manufacturing |
| 15 | Foreign diplomat |

#### `PrimaryEmailAddr`

Required: Optional
Type: `EmailAddress`
Traits: filterable

Primary email address.

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

#### `ResaleNum`

Required: Optional
Type: `String`
Max length: 16 chars

Resale number or some additional info about the customer.

#### `SecondaryTaxIdentifier`

Required: Optional
Type: `String`
Minor version: 3
Locales: IN, GB

Also called UTR No. in ( UK ) , CST Reg No. ( IN ) also represents the tax registration number of the Person or Organization. This value is masked in responses, exposing only last five characters. For example, the ID of `123-45-6789` is returned as `XXXXXX56789`.

#### `ARAccountRef`

Required: Optional
Type: `ReferenceType`
Minor version: 3
Locales: FR

Identifies the accounts receivable account to be used for this customer. Each customer must have his own AR account. Applicable for France companies, only. Available when endpoint is evoked with the `minorversion=3` query parameter. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType=Accounts Receivable`. Use `Account.Id` and `Account.Name` from that object for `ARAccountRef.value` and `ARAccountRef.name`, respectively.

<details>
<summary>Child attributes for `ARAccountRef`</summary>

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

#### `DefaultTaxCodeRef`

Required: Optional
Type: `ReferenceType`

Reference to a default tax code associated with this Customer object. Reference is valid if `Customer.Taxable` is set to true; otherwise, it is ignored. If automated sales tax is enabled (`Preferences.TaxPrefs.PartnerTaxEnabled` is set to `true`) the default tax code is set by the system and can not be overridden. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `DefaultTaxCodeRef.value` and `DefaultTaxCodeRef.name`, respectively.

<details>
<summary>Child attributes for `DefaultTaxCodeRef`</summary>

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

#### `PreferredDeliveryMethod`

Required: Optional
Type: `String`

Preferred delivery method. Values are Print, Email, or None.

#### `GSTIN`

Required: Optional
Type: `String`
Max length: maximum of 15 chars
Minor version: 33
Locales: IN

GSTIN is an identification number assigned to every GST registered business.

#### `SalesTermRef`

Required: Optional
Type: `ReferenceType`

Reference to a SalesTerm associated with this Customer object. Query the Term name list resource to determine the appropriate Term object for this reference. Use `Term.Id` and `Term.Name` from that object for `SalesTermRef.value` and `SalesTermRef.name`, respectively.

<details>
<summary>Child attributes for `SalesTermRef`</summary>

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

#### `CustomerTypeRef`

Required: Optional
Type: `String`

Reference to the customer type assigned to a customer. This field is only returned if the customer is assigned a customer type.

<details>
<summary>Child attributes for `CustomerTypeRef`</summary>

##### customertyperef

Model type: `object`

###### `value`

Required: Required
Type: `String`

The unique numeric Id of the customer type. This maps to the CustomerType entity: `CustomerType.Id`.

</details>

#### `Fax`

Required: Optional
Type: `TelephoneNumber`
Max length: maximum of 30 chars

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

#### `BillWithParent`

Required: Optional
Type: `Boolean`
Default: false

If true, this Customer object is billed with its parent. If false, or null the customer is not to be billed with its parent. This attribute is valid only if this entity is a Job or sub Customer.

#### `CurrencyRef`

Required: Optional
Type: `CurrencyRef`
Traits: read only
Max length: 16 chars

Reference to the currency in which all amounts associated with this customer are expressed. Once set, it cannot be changed. If specified currency is not currently in the company's currency list, it is added. If not specified, currency for this customer is the home currency of the company, as defined by `Preferences.CurrencyPrefs.HomeCurrency`.

<details>
<summary>Child attributes for `CurrencyRef`</summary>

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

#### `Mobile`

Required: Optional
Type: `TelephoneNumber`
Max length: maximum of 30 chars

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

#### `Job`

Required: Optional
Type: `Boolean`
Default: false or null

If true, this is a Job or sub-customer. If false or null, this is a top level customer, not a Job or sub-customer.

#### `BalanceWithJobs`

Required: Optional
Type: `Decimal`
Traits: sortable

Cumulative open balance amount for the Customer (or Job) and all its sub-jobs. Cannot be written to QuickBooks.

#### `PrimaryPhone`

Required: Optional
Type: `TelephoneNumber`
Max length: maximum of 30 chars

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

#### `OpenBalanceDate`

Required: Optional
Type: `Date`

Date of the Open Balance for the create operation. Write-on-create.

<details>
<summary>Child attributes for `OpenBalanceDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `Taxable`

Required: Optional
Type: `Boolean`

If true, transactions for this customer are taxable. Default behavior with minor version 10 and above: true, if `DefaultTaxCodeRef` is defined or false if `TaxExemptionReasonId` is set.

#### `AlternatePhone`

Required: Optional
Type: `TelephoneNumber`
Max length: maximum of 30 chars

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

#### `ParentRef`

Required: Optional
Type: `ReferenceType`

A reference to a Customer object that is the immediate parent of the Sub-Customer/Job in the hierarchical Customer:Job list. Required for the create operation if this object is a sub-customer or Job. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `ParentRef.value` and `ParentRef.name`, respectively.

<details>
<summary>Child attributes for `ParentRef`</summary>

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

#### `Notes`

Required: Optional
Type: `String`
Max length: maximum of 2000 chars

Free form text describing the Customer.

#### `WebAddr`

Required: Optional
Type: `WebSiteAddress`
Max length: maximum of 1000 chars

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

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable, sortable
Default: true

If true, this entity is currently enabled for use by QuickBooks. If there is an amount in `Customer.Balance` when setting this Customer object to inactive through the QuickBooks UI, a CreditMemo balancing transaction is created for the amount.

#### `CompanyName`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

The name of the company associated with the person or organization.

#### `Balance`

Required: Optional
Type: `Decimal`
Traits: filterable, sortable

Specifies the open balance amount or the amount unpaid by the customer. For the create operation, this represents the opening balance for the customer. When returned in response to the query request it represents the current open balance (unpaid amount) for that customer. Write-on-create.

#### `ShipAddr`

Required: Optional
Type: `PhysicalAddress`

Default shipping address. If a physical address is updated from within the transaction object, the QuickBooks Online API flows individual address components differently into the Line elements of the transaction response then when the transaction was first created:

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
<summary>Child attributes for `ShipAddr`</summary>

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

#### `PaymentMethodRef`

Required: Optional
Type: `ReferenceType`

Reference to a PaymentMethod associated with this Customer object. Query the PaymentMethod name list resource to determine the appropriate PaymentMethod object for this reference. Use `PaymentMethod.Id` and `PaymentMethod.Name` from that object for `PaymentMethodRef.value` and `PaymentMethodRef.name`, respectively.

<details>
<summary>Child attributes for `PaymentMethodRef`</summary>

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

#### `IsProject`

Required: Optional
Type: `Boolean`
Traits: read only
Default: False or null
Minor version: 25

If true, indicates this is a Project.

#### `Source`

Required: Optional
Type: `String`
Minor version: 59

The Source type of the transactions created by QuickBooks Commerce. Valid values include: `QBCommerce`

#### `PrimaryTaxIdentifier`

Required: Optional
Type: `String`
Minor version: 4
Locales: IN, CA, GB, AU

Also called Tax Reg. No in ( UK ) , ( CA ) , ( IN ) , ( AU ) represents the tax ID of the Person or Organization. This value is masked in responses, exposing only last five characters. For example, the ID of `123-45-6789` is returned as `XXXXXX56789`.

#### `GSTRegistrationType`

Required: Optional
Type: `String`
Max length: maximum of 15 chars
Minor version: 33
Locales: IN

For the filing of GSTR, transactions need to be classified depending on the type of customer to whom the sale is done. To facilitate this, we have introduced a new field as 'GST registration type'. Possible values are listed below:

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
Max length: maximum of 110 chars

Name of the person or organization as printed on a check. If not provided, this is populated from DisplayName. Constraints: Cannot be removed with sparse update.

#### `BillAddr`

Required: Optional
Type: `PhysicalAddress`

Default billing address. If a physical address is updated from within the transaction object, the QuickBooks Online API flows individual address components differently into the Line elements of the transaction response then when the transaction was first created:

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
  "Customer": {
    "PrimaryEmailAddr": {
      "Address": "Surf@Intuit.com"
    },
    "SyncToken": "0",
    "domain": "QBO",
    "GivenName": "Bill",
    "DisplayName": "Bill's Windsurf Shop",
    "BillWithParent": false,
    "FullyQualifiedName": "Bill's Windsurf Shop",
    "CompanyName": "Bill's Windsurf Shop",
    "FamilyName": "Lucchini",
    "sparse": false,
    "PrimaryPhone": {
      "FreeFormNumber": "(415) 444-6538"
    },
    "Active": true,
    "Job": false,
    "BalanceWithJobs": 85.0,
    "BillAddr": {
      "City": "Half Moon Bay",
      "Line1": "12 Ocean Dr.",
      "PostalCode": "94213",
      "Lat": "37.4307072",
      "Long": "-122.4295234",
      "CountrySubDivisionCode": "CA",
      "Id": "3"
    },
    "PreferredDeliveryMethod": "Print",
    "Taxable": false,
    "PrintOnCheckName": "Bill's Windsurf Shop",
    "Balance": 85.0,
    "Id": "2",
    "MetaData": {
      "CreateTime": "2014-09-11T16:49:28-07:00",
      "LastUpdatedTime": "2014-09-18T12:56:01-07:00"
    }
  },
  "time": "2015-07-23T11:04:15.496-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T11:03:44.699-07:00">
    <Customer domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-11T16:49:28-07:00</CreateTime>
            <LastUpdatedTime>2014-09-18T12:56:01-07:00</LastUpdatedTime>
        </MetaData>
        <GivenName>Bill</GivenName>
        <FamilyName>Lucchini</FamilyName>
        <FullyQualifiedName>Bill's Windsurf Shop</FullyQualifiedName>
        <CompanyName>Bill's Windsurf Shop</CompanyName>
        <DisplayName>Bill's Windsurf Shop</DisplayName>
        <PrintOnCheckName>Bill's Windsurf Shop</PrintOnCheckName>
        <Active>true</Active>
        <PrimaryPhone>
            <FreeFormNumber>(415) 444-6538</FreeFormNumber>
        </PrimaryPhone>
        <PrimaryEmailAddr>
            <Address>Surf@Intuit.com</Address>
        </PrimaryEmailAddr>
        <Taxable>false</Taxable>
        <BillAddr>
            <Id>3</Id>
            <Line1>12 Ocean Dr.</Line1>
            <City>Half Moon Bay</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94213</PostalCode>
            <Lat>37.4307072</Lat>
            <Long>-122.4295234</Long>
        </BillAddr>
        <Job>false</Job>
        <BillWithParent>false</BillWithParent>
        <Balance>85.00</Balance>
        <BalanceWithJobs>85.00</BalanceWithJobs>
        <PreferredDeliveryMethod>Print</PreferredDeliveryMethod>
    </Customer>
</IntuitResponse>
```

## Create a customer

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/customer`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required during object create.

### Request Body

The minimum elements to create a Customer are listed here.

Schema: `customerrequest`

<details>
<summary>Show schema for `customerrequest`</summary>

#### customerrequest

Model type: `object`

##### `DisplayName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 500 chars

The name of the person or organization as displayed. Must be unique across all Customer, Vendor, and Employee objects. Cannot be removed with sparse update. If not supplied, the system generates `DisplayName` by concatenating customer name components supplied in the request from the following list: `Title`, `GivenName`, `MiddleName`, `FamilyName`, and `Suffix`.

##### `Suffix`

Required: Conditionally required
Type: `String`
Max length: maximum of 16 chars

Suffix of the name. For example, `Jr`. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

##### `Title`

Required: Conditionally required
Type: `String`
Max length: maximum of 16 chars

Title of the person. This tag supports i18n, all locales. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, `Suffix`, or `FullyQualifiedName` attributes are required during create.

##### `MiddleName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Middle name of the person. The person can have zero or more middle names. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

##### `FamilyName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Family name or the last name of the person. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

##### `GivenName`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Given name or first name of a person. The `DisplayName` attribute or at least one of `Title`, `GivenName`, `MiddleName`, `FamilyName`, or `Suffix` attributes is required for object create.

</details>

#### Example

```json
{
  "FullyQualifiedName": "King Groceries",
  "PrimaryEmailAddr": {
    "Address": "jdrew@myemail.com"
  },
  "DisplayName": "King's Groceries",
  "Suffix": "Jr",
  "Title": "Mr",
  "MiddleName": "B",
  "Notes": "Here are other details.",
  "FamilyName": "King",
  "PrimaryPhone": {
    "FreeFormNumber": "(555) 555-5555"
  },
  "CompanyName": "King Groceries",
  "BillAddr": {
    "CountrySubDivisionCode": "CA",
    "City": "Mountain View",
    "PostalCode": "94042",
    "Line1": "123 Main Street",
    "Country": "USA"
  },
  "GivenName": "James"
}
```

#### XML example

```xml
<Customer xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Title>Mr</Title>
    <GivenName>James</GivenName>
    <MiddleName>B</MiddleName>
    <FamilyName>King</FamilyName>
    <Suffix>Jr</Suffix>
    <FullyQualifiedName>King Crafts</FullyQualifiedName>
    <CompanyName>King Crafts</CompanyName>
    <DisplayName>King Crafts</DisplayName>
    <PrimaryPhone>
        <FreeFormNumber>(555) 555-5555</FreeFormNumber>
    </PrimaryPhone>
    <BillAddr>
        <Id>102</Id>
        <Line1>123 Main Street</Line1>
        <City>Mountain View</City>
        <Country>USA</Country>
        <CountrySubDivisionCode>CA</CountrySubDivisionCode>
        <PostalCode>94042</PostalCode>
    </BillAddr>
</Customer>
```

### Returns

Returns the newly created Customer object.

#### Example

```json
{
  "Customer": {
    "domain": "QBO",
    "PrimaryEmailAddr": {
      "Address": "jdrew@myemail.com"
    },
    "DisplayName": "King's Groceries",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "DefaultTaxCodeRef": {
      "value": "2"
    },
    "PreferredDeliveryMethod": "Print",
    "GivenName": "James",
    "FullyQualifiedName": "King's Groceries",
    "BillWithParent": false,
    "Title": "Mr",
    "Job": false,
    "BalanceWithJobs": 0,
    "PrimaryPhone": {
      "FreeFormNumber": "(555) 555-5555"
    },
    "Taxable": true,
    "MetaData": {
      "CreateTime": "2015-07-23T10:58:12-07:00",
      "LastUpdatedTime": "2015-07-23T10:58:12-07:00"
    },
    "BillAddr": {
      "City": "Mountain View",
      "Country": "USA",
      "Line1": "123 Main Street",
      "PostalCode": "94042",
      "CountrySubDivisionCode": "CA",
      "Id": "112"
    },
    "MiddleName": "B",
    "Notes": "Here are other details.",
    "Active": true,
    "Balance": 0,
    "SyncToken": "0",
    "Suffix": "Jr",
    "CompanyName": "King Groceries",
    "FamilyName": "King",
    "PrintOnCheckName": "King Groceries",
    "sparse": false,
    "Id": "67"
  },
  "time": "2015-07-23T10:58:12.099-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-13T10:11:33.296-08:00">
  <Customer domain="QBO" sparse="false">
    <Id>62</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-02-13T10:13:29-08:00</CreateTime>
      <LastUpdatedTime>2015-02-13T10:13:29-08:00</LastUpdatedTime>
    </MetaData>
    <Title>Mr</Title>
    <GivenName>James</GivenName>
    <MiddleName>B</MiddleName>
    <FamilyName>King</FamilyName>
    <Suffix>Jr</Suffix>
    <FullyQualifiedName>King Crafts</FullyQualifiedName>
    <CompanyName>King Crafts</CompanyName>
    <DisplayName>King Crafts</DisplayName>
    <PrintOnCheckName>King Crafts</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
      <FreeFormNumber>(555) 555-5555</FreeFormNumber>
    </PrimaryPhone>
    <Mobile>
      <FreeFormNumber>555-5555-6666</FreeFormNumber>
    </Mobile>
    <Fax>
      <FreeFormNumber>(555) 555-7777</FreeFormNumber>
    </Fax>
    <PrimaryEmailAddr>
      <Address>jdrew@myemail.com</Address>
    </PrimaryEmailAddr>
    <WebAddr>
      <URI>http://www.drewfurniture.com</URI>
    </WebAddr>
    <DefaultTaxCodeRef>2</DefaultTaxCodeRef>
    <Taxable>true</Taxable>
    <BillAddr>
      <Id>104</Id>
      <Line1>123 Main Street</Line1>
      <City>Mountain View</City>
      <Country>USA</Country>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>94042</PostalCode>
    </BillAddr>
    <ShipAddr>
      <Id>105</Id>
      <Line1>123 Main Street</Line1>
      <City>Mountain View</City>
      <Country>USA</Country>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>94042</PostalCode>
    </ShipAddr>
    <Notes>Here are other details.</Notes>
    <Job>false</Job>
    <BillWithParent>false</BillWithParent>
    <Balance>0</Balance>
    <BalanceWithJobs>0</BalanceWithJobs>
    <PreferredDeliveryMethod>Print</PreferredDeliveryMethod>
  </Customer>
</IntuitResponse>
```

## Query a customer

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Customer Where Metadata.LastUpdatedTime > '2015-03-01'"
```

#### XML example

```sql
select * from Customer Where Metadata.LastUpdatedTime > '2015-03-01'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "Customer": [
      {
        "domain": "QBO",
        "FamilyName": "Lauterbach",
        "DisplayName": "Amy's Bird Sanctuary",
        "DefaultTaxCodeRef": {
          "value": "2"
        },
        "PrimaryEmailAddr": {
          "Address": "Birds@Intuit.com"
        },
        "PreferredDeliveryMethod": "Print",
        "GivenName": "Amy",
        "FullyQualifiedName": "Amy's Bird Sanctuary",
        "BillWithParent": false,
        "Job": false,
        "BalanceWithJobs": 274.0,
        "PrimaryPhone": {
          "FreeFormNumber": "(650) 555-3311"
        },
        "Active": true,
        "MetaData": {
          "CreateTime": "2014-09-11T16:48:43-07:00",
          "LastUpdatedTime": "2015-07-01T10:14:15-07:00"
        },
        "BillAddr": {
          "City": "Bayshore",
          "Line1": "4581 Finch St.",
          "PostalCode": "94326",
          "Lat": "INVALID",
          "Long": "INVALID",
          "CountrySubDivisionCode": "CA",
          "Id": "2"
        },
        "MiddleName": "Michelle",
        "Notes": "Note added via Update operation.",
        "Taxable": true,
        "Balance": 274.0,
        "SyncToken": "5",
        "CompanyName": "Amy's Bird Sanctuary",
        "ShipAddr": {
          "City": "Bayshore",
          "Line1": "4581 Finch St.",
          "PostalCode": "94326",
          "Lat": "INVALID",
          "Long": "INVALID",
          "CountrySubDivisionCode": "CA",
          "Id": "109"
        },
        "PrintOnCheckName": "Amy's Bird Sanctuary",
        "sparse": false,
        "Id": "1"
      },
      {
        "domain": "QBO",
        "PrimaryEmailAddr": {
          "Address": "Consulting@intuit.com"
        },
        "DisplayName": "Weiskopf Consulting",
        "FamilyName": "Weiskopf",
        "PreferredDeliveryMethod": "Print",
        "GivenName": "Nicola",
        "FullyQualifiedName": "Weiskopf Consulting",
        "BillWithParent": false,
        "Job": false,
        "BalanceWithJobs": 390.0,
        "PrimaryPhone": {
          "FreeFormNumber": "(650) 555-1423"
        },
        "Active": true,
        "MetaData": {
          "CreateTime": "2014-09-11T17:29:04-07:00",
          "LastUpdatedTime": "2015-06-24T15:54:02-07:00"
        },
        "BillAddr": {
          "City": "Bayshore",
          "Line1": "45612 Main St.",
          "PostalCode": "94326",
          "Lat": "45.256574",
          "Long": "-66.0943698",
          "CountrySubDivisionCode": "CA",
          "Id": "30"
        },
        "Taxable": false,
        "Balance": 390.0,
        "SyncToken": "0",
        "CompanyName": "Weiskopf Consulting",
        "ShipAddr": {
          "City": "Bayshore",
          "Line1": "45612 Main St.",
          "PostalCode": "94326",
          "Lat": "45.256574",
          "Long": "-66.0943698",
          "CountrySubDivisionCode": "CA",
          "Id": "30"
        },
        "PrintOnCheckName": "Weiskopf Consulting",
        "sparse": false,
        "Id": "29"
      }
    ],
    "startPosition": 1,
    "maxResults": 6
  },
  "time": "2015-07-23T11:02:25.149-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T11:00:41.365-07:00">
    <QueryResponse startPosition="1" maxResults="6">
        <Customer domain="QBO" sparse="false">
            <Id>1</Id>
            <SyncToken>5</SyncToken>
            <MetaData>
                <CreateTime>2014-09-11T16:48:43-07:00</CreateTime>
                <LastUpdatedTime>2015-07-01T10:14:15-07:00</LastUpdatedTime>
            </MetaData>
            <GivenName>Amy</GivenName>
            <MiddleName>Michelle</MiddleName>
            <FamilyName>Lauterbach</FamilyName>
            <FullyQualifiedName>Amy's Bird Sanctuary</FullyQualifiedName>
            <CompanyName>Amy's Bird Sanctuary</CompanyName>
            <DisplayName>Amy's Bird Sanctuary</DisplayName>
            <PrintOnCheckName>Amy's Bird Sanctuary</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(650) 555-3311</FreeFormNumber>
            </PrimaryPhone>
            <PrimaryEmailAddr>
                <Address>Birds@Intuit.com</Address>
            </PrimaryEmailAddr>
            <DefaultTaxCodeRef>2</DefaultTaxCodeRef>
            <Taxable>true</Taxable>
            <BillAddr>
                <Id>2</Id>
                <Line1>4581 Finch St.</Line1>
                <City>Bayshore</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94326</PostalCode>
                <Lat>INVALID</Lat>
                <Long>INVALID</Long>
            </BillAddr>
            <ShipAddr>
                <Id>109</Id>
                <Line1>4581 Finch St.</Line1>
                <City>Bayshore</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94326</PostalCode>
                <Lat>INVALID</Lat>
                <Long>INVALID</Long>
            </ShipAddr>
            <Notes>Note added via Update operation.</Notes>
            <Job>false</Job>
            <BillWithParent>false</BillWithParent>
            <Balance>274.00</Balance>
            <BalanceWithJobs>274.00</BalanceWithJobs>
            <PreferredDeliveryMethod>Print</PreferredDeliveryMethod>
        </Customer>
. . .
        <Customer domain="QBO" sparse="false">
            <Id>29</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-11T17:29:04-07:00</CreateTime>
                <LastUpdatedTime>2015-06-24T15:54:02-07:00</LastUpdatedTime>
            </MetaData>
            <GivenName>Nicola</GivenName>
            <FamilyName>Weiskopf</FamilyName>
            <FullyQualifiedName>Weiskopf Consulting</FullyQualifiedName>
            <CompanyName>Weiskopf Consulting</CompanyName>
            <DisplayName>Weiskopf Consulting</DisplayName>
            <PrintOnCheckName>Weiskopf Consulting</PrintOnCheckName>
            <Active>true</Active>
            <PrimaryPhone>
                <FreeFormNumber>(650) 555-1423</FreeFormNumber>
            </PrimaryPhone>
            <PrimaryEmailAddr>
                <Address>Consulting@intuit.com</Address>
            </PrimaryEmailAddr>
            <Taxable>false</Taxable>
            <BillAddr>
                <Id>30</Id>
                <Line1>45612 Main St.</Line1>
                <City>Bayshore</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94326</PostalCode>
                <Lat>45.256574</Lat>
                <Long>-66.0943698</Long>
            </BillAddr>
            <ShipAddr>
                <Id>30</Id>
                <Line1>45612 Main St.</Line1>
                <City>Bayshore</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94326</PostalCode>
                <Lat>45.256574</Lat>
                <Long>-66.0943698</Long>
            </ShipAddr>
            <Job>false</Job>
            <BillWithParent>false</BillWithParent>
            <Balance>390.00</Balance>
            <BalanceWithJobs>390.00</BalanceWithJobs>
            <PreferredDeliveryMethod>Print</PreferredDeliveryMethod>
        </Customer>
    </QueryResponse>
</IntuitResponse>
```

## Read a customer

### Definition

- **Operation:** `GET /v3/company/<realmID>/customer/<customerId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Customer object that has been previously created.

### Returns

Returns the Customer object.

#### Example

```json
{
  "Customer": {
    "PrimaryEmailAddr": {
      "Address": "Surf@Intuit.com"
    },
    "SyncToken": "0",
    "domain": "QBO",
    "GivenName": "Bill",
    "DisplayName": "Bill's Windsurf Shop",
    "BillWithParent": false,
    "FullyQualifiedName": "Bill's Windsurf Shop",
    "CompanyName": "Bill's Windsurf Shop",
    "FamilyName": "Lucchini",
    "sparse": false,
    "PrimaryPhone": {
      "FreeFormNumber": "(415) 444-6538"
    },
    "Active": true,
    "Job": false,
    "BalanceWithJobs": 85.0,
    "BillAddr": {
      "City": "Half Moon Bay",
      "Line1": "12 Ocean Dr.",
      "PostalCode": "94213",
      "Lat": "37.4307072",
      "Long": "-122.4295234",
      "CountrySubDivisionCode": "CA",
      "Id": "3"
    },
    "PreferredDeliveryMethod": "Print",
    "Taxable": false,
    "PrintOnCheckName": "Bill's Windsurf Shop",
    "Balance": 85.0,
    "Id": "2",
    "MetaData": {
      "CreateTime": "2014-09-11T16:49:28-07:00",
      "LastUpdatedTime": "2014-09-18T12:56:01-07:00"
    }
  },
  "time": "2015-07-23T11:04:15.496-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T11:03:44.699-07:00">
    <Customer domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-11T16:49:28-07:00</CreateTime>
            <LastUpdatedTime>2014-09-18T12:56:01-07:00</LastUpdatedTime>
        </MetaData>
        <GivenName>Bill</GivenName>
        <FamilyName>Lucchini</FamilyName>
        <FullyQualifiedName>Bill's Windsurf Shop</FullyQualifiedName>
        <CompanyName>Bill's Windsurf Shop</CompanyName>
        <DisplayName>Bill's Windsurf Shop</DisplayName>
        <PrintOnCheckName>Bill's Windsurf Shop</PrintOnCheckName>
        <Active>true</Active>
        <PrimaryPhone>
            <FreeFormNumber>(415) 444-6538</FreeFormNumber>
        </PrimaryPhone>
        <PrimaryEmailAddr>
            <Address>Surf@Intuit.com</Address>
        </PrimaryEmailAddr>
        <Taxable>false</Taxable>
        <BillAddr>
            <Id>3</Id>
            <Line1>12 Ocean Dr.</Line1>
            <City>Half Moon Bay</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94213</PostalCode>
            <Lat>37.4307072</Lat>
            <Long>-122.4295234</Long>
        </BillAddr>
        <Job>false</Job>
        <BillWithParent>false</BillWithParent>
        <Balance>85.00</Balance>
        <BalanceWithJobs>85.00</BalanceWithJobs>
        <PreferredDeliveryMethod>Print</PreferredDeliveryMethod>
    </Customer>
</IntuitResponse>
```

## Full update a customer

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/customer`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing Customer object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.Add the query parameter, `include=updateaccountontxns&minorversion=5`, to the endpoint to automatically update the AR account on historical transactions (from soft close date forward) for this customer with that defined by the `ARAccountRef` attribute in the Customer object. Updates on soft closed transacitons will fail.

### Request Body

Schema: `customerresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "domain": "QBO",
  "PrimaryEmailAddr": {
    "Address": "Surf@Intuit.com"
  },
  "DisplayName": "Bill's Windsurf Shop",
  "PreferredDeliveryMethod": "Print",
  "GivenName": "Bill",
  "FullyQualifiedName": "Bill's Windsurf Shop",
  "BillWithParent": false,
  "Job": false,
  "BalanceWithJobs": 85.0,
  "PrimaryPhone": {
    "FreeFormNumber": "(415) 444-6538"
  },
  "Active": true,
  "MetaData": {
    "CreateTime": "2014-09-11T16:49:28-07:00",
    "LastUpdatedTime": "2015-07-23T11:07:55-07:00"
  },
  "BillAddr": {
    "City": "Half Moon Bay",
    "Line1": "12 Ocean Dr.",
    "PostalCode": "94213",
    "Lat": "37.4307072",
    "Long": "-122.4295234",
    "CountrySubDivisionCode": "CA",
    "Id": "3"
  },
  "MiddleName": "Mac",
  "Taxable": false,
  "Balance": 85.0,
  "SyncToken": "3",
  "CompanyName": "Bill's Windsurf Shop",
  "FamilyName": "Lucchini",
  "PrintOnCheckName": "Bill's Wind Surf Shop",
  "sparse": false,
  "Id": "2"
}
```

#### XML example

```xml
<Customer xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2014-09-11T16:49:28-07:00</CreateTime>
            <LastUpdatedTime>2015-07-23T11:09:54-07:00</LastUpdatedTime>
        </MetaData>
        <GivenName>Bill</GivenName>
        <MiddleName>Max</MiddleName>
        <FamilyName>Lucchini</FamilyName>
        <FullyQualifiedName>Bill's Windsurf Shop</FullyQualifiedName>
        <CompanyName>Bill's Windsurf Shop</CompanyName>
        <DisplayName>Bill's Windsurf Shop</DisplayName>
        <PrintOnCheckName>Bill's Wind and Surf Shop</PrintOnCheckName>
        <Active>true</Active>
        <PrimaryPhone>
            <FreeFormNumber>(415) 444-6538</FreeFormNumber>
        </PrimaryPhone>
        <PrimaryEmailAddr>
            <Address>Surf@Intuit.com</Address>
        </PrimaryEmailAddr>
        <Taxable>false</Taxable>
        <BillAddr>
            <Id>3</Id>
            <Line1>12 Ocean Dr.</Line1>
            <City>Half Moon Bay</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94213</PostalCode>
            <Lat>37.4307072</Lat>
            <Long>-122.4295234</Long>
        </BillAddr>
        <Job>false</Job>
        <BillWithParent>false</BillWithParent>
        <Balance>85.00</Balance>
        <BalanceWithJobs>85.00</BalanceWithJobs>
        <PreferredDeliveryMethod>Print</PreferredDeliveryMethod>
</Customer>
```

### Returns

The customer response body.

#### Example

```json
{
  "Customer": {
    "domain": "QBO",
    "PrimaryEmailAddr": {
      "Address": "Surf@Intuit.com"
    },
    "DisplayName": "Bill's Windsurf Shop",
    "PreferredDeliveryMethod": "Print",
    "GivenName": "Bill",
    "FullyQualifiedName": "Bill's Windsurf Shop",
    "BillWithParent": false,
    "Job": false,
    "BalanceWithJobs": 85.0,
    "PrimaryPhone": {
      "FreeFormNumber": "(415) 444-6538"
    },
    "Active": true,
    "MetaData": {
      "CreateTime": "2014-09-11T16:49:28-07:00",
      "LastUpdatedTime": "2015-07-23T11:18:37-07:00"
    },
    "BillAddr": {
      "City": "Half Moon Bay",
      "Line1": "12 Ocean Dr.",
      "PostalCode": "94213",
      "Lat": "37.4307072",
      "Long": "-122.4295234",
      "CountrySubDivisionCode": "CA",
      "Id": "3"
    },
    "MiddleName": "Mac",
    "Taxable": false,
    "Balance": 85.0,
    "SyncToken": "4",
    "CompanyName": "Bill's Windsurf Shop",
    "FamilyName": "Lucchini",
    "PrintOnCheckName": "Bill's Wind Surf Shop",
    "sparse": false,
    "Id": "2"
  },
  "time": "2015-07-23T11:18:37.323-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T11:16:50.611-07:00">
  <Customer domain="QBO" sparse="false">
    <Id>2</Id>
    <SyncToken>3</SyncToken>
    <MetaData>
      <CreateTime>2014-09-11T16:49:28-07:00</CreateTime>
      <LastUpdatedTime>2015-07-23T11:16:50-07:00</LastUpdatedTime>
    </MetaData>
    <GivenName>Bill</GivenName>
    <MiddleName>Max</MiddleName>
    <FamilyName>Lucchini</FamilyName>
    <FullyQualifiedName>Bill's Windsurf Shop</FullyQualifiedName>
    <CompanyName>Bill's Windsurf Shop</CompanyName>
    <DisplayName>Bill's Windsurf Shop</DisplayName>
    <PrintOnCheckName>Bill's Wind and Surf Shop</PrintOnCheckName>
    <Active>true</Active>
    <PrimaryPhone>
      <FreeFormNumber>(415) 444-6538</FreeFormNumber>
    </PrimaryPhone>
    <PrimaryEmailAddr>
      <Address>Surf@Intuit.com</Address>
    </PrimaryEmailAddr>
    <Taxable>false</Taxable>
    <BillAddr>
      <Id>3</Id>
      <Line1>12 Ocean Dr.</Line1>
      <City>Half Moon Bay</City>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>94213</PostalCode>
      <Lat>37.4307072</Lat>
      <Long>-122.4295234</Long>
    </BillAddr>
    <Job>false</Job>
    <BillWithParent>false</BillWithParent>
    <Balance>85.00</Balance>
    <BalanceWithJobs>85.00</BalanceWithJobs>
    <PreferredDeliveryMethod>Print</PreferredDeliveryMethod>
  </Customer>
</IntuitResponse>
```

## Sparse update a customer

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/customer`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Sparse updating provides the ability to update a subset of properties for a given object; only elements specified in the request are updated. Missing elements are left untouched. The ID of the object to update is specified in the request body.​

### Request Body

Schema: `customerresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "MiddleName": "Mark",
  "SyncToken": "0",
  "Id": "2",
  "sparse": true
}
```

#### XML example

```xml
<Customer xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>2</Id>
    <SyncToken>0</SyncToken>
    <MiddleName>Max</MiddleName>
</Customer>
```

### Returns

The customer response body.

#### Example

```json
{
  "Customer": {
    "domain": "QBO",
    "PrimaryEmailAddr": {
      "Address": "Surf@Intuit.com"
    },
    "DisplayName": "Bill's Windsurf Shop",
    "PreferredDeliveryMethod": "Print",
    "GivenName": "Bill",
    "FullyQualifiedName": "Bill's Windsurf Shop",
    "BillWithParent": false,
    "Job": false,
    "BalanceWithJobs": 85.0,
    "PrimaryPhone": {
      "FreeFormNumber": "(415) 444-6538"
    },
    "Active": true,
    "MetaData": {
      "CreateTime": "2014-09-11T16:49:28-07:00",
      "LastUpdatedTime": "2015-07-23T11:07:55-07:00"
    },
    "BillAddr": {
      "City": "Half Moon Bay",
      "Line1": "12 Ocean Dr.",
      "PostalCode": "94213",
      "Lat": "37.4307072",
      "Long": "-122.4295234",
      "CountrySubDivisionCode": "CA",
      "Id": "3"
    },
    "MiddleName": "Mark",
    "Taxable": false,
    "Balance": 85.0,
    "SyncToken": "1",
    "CompanyName": "Bill's Windsurf Shop",
    "FamilyName": "Lucchini",
    "PrintOnCheckName": "Bill's Windsurf Shop",
    "sparse": false,
    "Id": "2"
  },
  "time": "2015-07-23T11:07:55.772-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T11:09:54.602-07:00">
    <Customer domain="QBO" sparse="false">
        <Id>2</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2014-09-11T16:49:28-07:00</CreateTime>
            <LastUpdatedTime>2015-07-23T11:09:54-07:00</LastUpdatedTime>
        </MetaData>
        <GivenName>Bill</GivenName>
        <MiddleName>Max</MiddleName>
        <FamilyName>Lucchini</FamilyName>
        <FullyQualifiedName>Bill's Windsurf Shop</FullyQualifiedName>
        <CompanyName>Bill's Windsurf Shop</CompanyName>
        <DisplayName>Bill's Windsurf Shop</DisplayName>
        <PrintOnCheckName>Bill's Windsurf Shop</PrintOnCheckName>
        <Active>true</Active>
        <PrimaryPhone>
            <FreeFormNumber>(415) 444-6538</FreeFormNumber>
        </PrimaryPhone>
        <PrimaryEmailAddr>
            <Address>Surf@Intuit.com</Address>
        </PrimaryEmailAddr>
        <Taxable>false</Taxable>
        <BillAddr>
            <Id>3</Id>
            <Line1>12 Ocean Dr.</Line1>
            <City>Half Moon Bay</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94213</PostalCode>
            <Lat>37.4307072</Lat>
            <Long>-122.4295234</Long>
        </BillAddr>
        <Job>false</Job>
        <BillWithParent>false</BillWithParent>
        <Balance>85.00</Balance>
        <BalanceWithJobs>85.00</BalanceWithJobs>
        <PreferredDeliveryMethod>Print</PreferredDeliveryMethod>
    </Customer>
</IntuitResponse>
```
