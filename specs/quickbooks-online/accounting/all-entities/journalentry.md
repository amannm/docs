# JournalEntry

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/journalentry
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / JournalEntry
> Canonical entity: `JournalEntry`

JournalEntry is a transaction in which:

- There are at least one pair of lines, a debit and a credit, called distribution lines.
- Each distribution line has an account from the Chart of Accounts. Query the Account resource for a listing of the Chart of Accounts.
- The total of the debit column equals the total of the credit column.

When you record a transaction with a JournalEntry object, the QuickBooks Online UI labels the transaction as `JRNL` in the register and as `General Journal` on reports that list transactions.

### Business Rules

- Accounts Receivable (A/R) account: needs to have a Customer in the Name Field. The A/R account is visible only after there are A/R transactions such as receive payments from invoices.
- Accounts Payable (A/P) account: needs to have a Vendor in the Name Field. The A/P account is visible only after there are A/P transactions such Bill objects.

Tax Related considerations for global companies:

- There are both Sales Tax and Purchase Tax.
- On the transaction line , if `TaxCodeRef` is specified, `TaxApplicableOn` and `TaxAmount` are required. Each `TaxCodeRef` can result in one or more tax lines. For AU locale : On the transaction line, if `GlobalTaxCalculation` is `TaxInclusive` and`TaxCodeRef` is specified, `TaxInclusiveAmt` is required.
- Any `TxnTaxDetail` lines specified are not overridden. That is, if a user provides incorrect values such that the total amount on debit is not equal to total amount on credit, an error is returned.
- Not SKU specific.

## The journalentry object

### journalentryresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of a transaction. There must be at least one pair of Journal Entry Line elements, representing a debit and a credit, called distribution lines. Valid `Line` types include: `JournalEntryLine` and `DescriptionOnlyLine`

<details>
<summary>Child attributes for `Line [0..n]`</summary>

##### journalentryline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. In requests, if `Id` matches that for an existing line in the transaction the line is updated. Otherwise, a new line is created. Integer as string.

###### `JournalEntryLineDetail`

Required: Required
Type: `JournalEntryLineDetail`

<details>
<summary>Child attributes for `JournalEntryLineDetail`</summary>

###### journalentrylinedetail

Model type: `object`

###### `JournalCodeRef`

Required: Required
Type: `ReferenceType`
Minor version: 5
Locales: FR

For France locales, only. Reference to a JournalCode object. This must be present for both `Credit` and `Debit` posting sides of the JournalEntry object. Query the JournalCode name list resource to determine the appropriate JournalCode object for this reference. Use `JournalCode.Id` and `JournalCode.Name` from that object for `JournalCodeRef.value` and `JournalCodeRef.name`, respectively.

<details>
<summary>Child attributes for `JournalCodeRef`</summary>

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

###### `PostingType`

Required: Required
Type: `PostingTypeEnum`

Indicates whether this JournalEntry line is a debit or credit. Valid values: `Credit`, `Debit`

###### `AccountRef`

Required: Required
Type: `ReferenceType`

Reference to the account associated with this line. Query the Account name list resource to determine the appropriate Account object for this reference, based on the side of the journal entry represented by this line. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively. For France locales: The account associated with the referenced Account object is looked up in the account category list.

If this account has same location as specified in the transaction by the `TransactionLocationType` attribute and the same VAT as in the line item `TaxCodeRef` attribute, then this account is used.

If there is a mismatch, then the account from the account category list that matches the transaction location and VAT is used.

If this account is not present in the account category list, then a new account is created with the new location, new VAT code, and all other attributes as in the default account.

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

###### `TaxApplicableOn`

Required: Conditionally required
Type: `TaxApplicableOnEnum`
Locales: GB, AU, IN

Indicates whether the tax applicable on the line is sales or purchase. Valid value: `Sales`, `Purchase`. Required if `TaxCodeRef` is specified

###### `Entity`

Required: Conditionally required

When you use `Accounts Receivable`, you must choose a `customer` in the Name field. When you use `Accounts Payable`, you must choose a `supplier/vendor` in the Name field.

<details>
<summary>Child attributes for `Entity`</summary>

###### entity

Model type: `object`

###### `EntityRef`

Required: Required
Type: `ReferenceType`

Query the corresponding name list resource as specified by `Entity` to determine the appropriate object for this reference. Use the `Id` and `DisplayName` values from that object for `EntityRef.value` and `EntityRef.name`, respectively.

<details>
<summary>Child attributes for `EntityRef`</summary>

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

###### `Type`

Type: `EntityTypeEnum`

Object type. Output only. Valid values are `Vendor`, `Employee`, or `Customer`.

</details>

###### `TaxAmount`

Type: `Decimal`
Max length: Min: 0, Max:999999999
Locales: GB, AU, IN

Tax amount of the line.

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`
Minor version: 53
Locales: AU

The total amount of the line items including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with the transaction. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerTxn` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

A reference to a Department object specifying the location of the transaction. Available if `Preferences.AccountingInfoPrefs.TrackDepartments` is set to `true`.
Query the Department name list resource to determine the appropriate department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

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

###### `TaxCodeRef`

Required: Optional
Type: `ReferenceType`
Locales: GB, AU, IN

Reference to the `TaxCode`for this item. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively.

<details>
<summary>Child attributes for `TaxCodeRef`</summary>

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

###### `BillableStatus`

Required: Optional
Type: `BillableStatusEnum`
Traits: read only

The billable status of the journal entry line. The line is to be billed to a customer if the account is an expense account and `EntityRef` specifies a Customer object. This field is not updatable through an API request. The value automatically changes when an invoice is created. Valid values: `Billable`, `NotBillable`, `HasBeenBilled`

</details>

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `JournalEntryLineDetail`for this type of line.

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item.

###### `ProjectRef`

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

###### `Description`

Required: Optional
Type: `String`
Max length: Max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer

##### descriptiononlyline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. Its use in requests is as folllows:

If `Id`is greater than zero and exists for the transaction, the request is considered an update operation for the description line item.

If no `Id`is provided, the `Id`provided is less than or equal to zero, or the `Id`provided is greater than zero and does not exist for the transaction then the request is considered a create operation for the description line item.

Available in all objects that use lines and support the update operation.

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `DescriptionOnly`for this type of line.

###### `DescriptionLineDetail`

Required: Required
Type: `DescriptionLineDetail`

<details>
<summary>Child attributes for `DescriptionLineDetail`</summary>

###### descriptiononly

Model type: `object`

###### `TaxCodeRef`

Required: Optional
Type: `ReferenceType`

Reference to the `TaxCode`for this item. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively.

<details>
<summary>Child attributes for `TaxCodeRef`</summary>

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

###### `ServiceDate`

Required: Optional
Type: `Date`

Date when the service is performed.

<details>
<summary>Child attributes for `ServiceDate`</summary>

###### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

</details>

###### `Amount`

Type: `Decimal`
Traits: read only
Minor version: 23

The amount of the line item. Available when `Amount` is set via the QuickBooks UI. Returned only for Description Only line items that have a non-empty amount associated with them.

###### `Description`

Required: Optional
Type: `String`
Max length: max 4000 chars

A string representing one of the following:

Free form text description of the line item that appears in the printed record.

A subtotal line inline with other lines on the sales form and holds the sum of amounts on all lines above it. This is distinct from the overall transaction subtotal represented with a SubTotal detail line.

In create requests, set to `Subtotal:` (case sensitive) to create the subtotal line; the amount is generated by QuickBooks Online business logic.

In read requests, lines with `Subtotal: nn.nn` returned in this field denote subtotal lines in the object.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer.

</details>

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company

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

#### `GlobalTaxCalculation`

Required: Conditionally required
Type: `GlobalTaxCalculationEnum`
Default: <span class="literal">TaxExcluded</span>
Minor version: 53
Locales: AU

Method in which tax is applied. Allowed values are: `TaxExcluded`, `TaxInclusive`. Not applicable to US companies; required for non-US companies.

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `JournalEntry` was created from.

<details>
<summary>Child attributes for `RecurDataRef`</summary>

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

#### `TotalAmt`

Type: `BigDecimal`
Traits: read only, system defined

The value of this field will always be set to zero. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `HomeTotalAmt`

Type: `Decimal`
Traits: read only, system defined

The value of this field will always be set to zero. Applicable if multicurrency is enabled for the company.

#### `DocNumber`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 21 chars

Reference number for the transaction. Throws an error when duplicate DocNumber is sent in the request and if `Preferences:OtherPrefs:NameValue.Name = WarnDuplicateJournalNumber` is true. Recommended best practice: check the setting of `Preferences:OtherPrefs:NameValue.Name = WarnDuplicateJournalNumber` before setting DocNumber. If a duplicate DocNumber needs to be supplied, add the query parameter name/value pair, `include=allowduplicatedocnum` to the URI. Sort order is ASC by default. With this change V3 JournalEntry API will be supporting autoassign docNumber when null in the request only till `minorversion=53`. Starting `minorversion=54` if null value is sent in the request null will be saved. With `minorversion=54` if there is a need to support assigning a `docNumber` when null, it can be achieved through include param, `include=allowautodocnum`

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: Max of 4000 chars

User entered, organization-private note about the transaction.

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: Current server date

The date entered by the user when this transaction occurred. For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used. Sort order is ASC by default.

<details>
<summary>Child attributes for `TxnDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

#### `TaxRateRef`

Required: Optional
Type: `ReferenceType`
Minor version: 49

Reference to the Tax Adjustment Rate Ids for this item. Query the TaxRate list resource to determine the appropriate TaxRate object for this reference. Use `TaxRate.Id` and `TaxRate.Name` from that object for TaxRateRef.value and TaxRateRef.name, respectively.

<details>
<summary>Child attributes for `TaxRateRef`</summary>

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

#### `TransactionLocationType`

Required: Optional
Type: `String`
Default: <span class="literal">WithinFrance</span>
Minor version: 4
Locales: FR

The account location. Valid values include:

`WithinFrance`

`FranceOverseas`

`OutsideFranceWithEU`

`OutsideEU`

For France locales, only.

#### `TxnTaxDetail`

Required: Optional
Type: `TxnTaxDetail`

This data type provides information for taxes charged on the transaction as a whole. It captures the details sales taxes calculated for the transaction based on the tax codes referenced by the transaction. This can be calculated by QuickBooks business logic or you may supply it when adding a transaction. See [Global tax model](https://developer.intuit.com/app/developer/qbo/docs/workflows/calculate-sales-tax/automated-sales-tax-for-non-us-locales) for more information about this element. If sales tax is disabled (`Preferences.TaxPrefs.UsingSalesTax` is set to `false`) then `TxnTaxDetail` is ignored and not stored.

<details>
<summary>Child attributes for `TxnTaxDetail`</summary>

##### txntaxdetail

Model type: `object`

###### `TxnTaxCodeRef`

Required: Optional
Type: `ReferenceType`

Reference to the transaction tax code. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively. If specified and sales tax is disabled (`Preferences.TaxPrefs.UsingSalesTax` is set to `false`), this element is ignored and not returned. For sales transactions, only: if automated sales tax is enabled (`Preferences.TaxPrefs.PartnerTaxEnabled` is set to `true`) the supplied transaction tax code is replaced by the automated sales tax engine recommendation.

<details>
<summary>Child attributes for `TxnTaxCodeRef`</summary>

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

###### `TotalTax`

Required: Optional
Type: `Decimal`

Total tax calculated for the transaction, excluding any tax lines manually inserted into the transaction line list.

###### `TaxLine [0..n]`

Required: Optional
Type: `Line`

<details>
<summary>Child attributes for `TaxLine [0..n]`</summary>

###### taxline

Model type: `object`

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `TaxLineDetail`for this type of line.

###### `TaxLineDetail`

Required: Required
Type: `TaxLineDetail`

**TaxLineDetail**

<details>
<summary>Child attributes for `TaxLineDetail`</summary>

###### taxlinedetail

Model type: `object`

###### `TaxRateRef`

Required: Required
Type: `ReferenceType`

Reference to a TaxRate to apply to the entire transaction. Query the TaxRate name list resource to determine the appropriate TaxRage object for this reference. Use `TaxRate.Id` and `TaxRate.Name` from that object for `TaxRateRef.value` and `TaxRateRef.name`, respectively.
For non-US versions of QuickBooks, the TaxRate referenced here must also be one of the rates in the referenced tax code's rate list—either the SalesTaxRateList or the PurchaseTaxRateList—as applies to the transaction type. Any given rate may only be listed once.

<details>
<summary>Child attributes for `TaxRateRef`</summary>

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

###### `NetAmountTaxable`

Required: Optional
Type: `Decimal`

This is the taxable amount on the total of the applicable tax rates. If TaxRate is applicable on two lines, this attribute represents the total of the two lines for which this rate is applied. This is different from the `Line.Amount` , which represents the final tax amount after the tax has been applied. Default Value: `Null`

###### `PercentBased`

Required: Optional
Type: `Boolean`

`True`—sales tax rate is expressed as a percentage.

`False`—sales tax rate is expressed as a number amount.

###### `TaxInclusiveAmount`

Required: Optional
Type: `Decimal`

This is the total amount, including tax.

###### `OverrideDeltaAmount`

Required: Optional
Type: `Decimal`

The difference between the actual tax and the overridden amount supplied by the user.

###### `TaxPercent`

Required: Optional
Type: `Decimal`

Numerical expression of the sales tax percent. For example, use "8.5" not "0.085".

</details>

###### `Amount`

Required: Optional
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of tax for this tax line. This value is negative for JournalEntry objects with `PostingType` set to `Credit.`

</details>

</details>

#### `Adjustment`

Required: Optional
Type: `Boolean`
Locales: US

Indicates whether this transaction is a journal entry adjustment.

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
  "time": "2015-06-29T12:43:42.132-07:00",
  "JournalEntry": {
    "SyncToken": "0",
    "domain": "QBO",
    "TxnDate": "2015-06-29",
    "sparse": false,
    "Line": [
      {
        "Description": "Four sprinkler heads damaged",
        "JournalEntryLineDetail": {
          "PostingType": "Debit",
          "AccountRef": {
            "name": "Job Expenses:Job Materials:Fountain and Garden Lighting",
            "value": "65"
          },
          "Entity": {
            "Type": "Customer",
            "EntityRef": {
              "name": "Amy's Bird Sanctuary",
              "value": "1"
            }
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "ProjectRef": {
          "value": "39298034"
        },
        "Amount": 25.54,
        "Id": "0"
      },
      {
        "JournalEntryLineDetail": {
          "PostingType": "Credit",
          "AccountRef": {
            "name": "Notes Payable",
            "value": "44"
          },
          "Entity": {
            "Type": "Vendor",
            "EntityRef": {
              "name": "IDX Vendor",
              "value": "2"
            }
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "Amount": 25.54,
        "Id": "1",
        "Description": "Sprinkler Hds - Sprinkler Hds Inventory Adjustment"
      }
    ],
    "Adjustment": false,
    "Id": "227",
    "TxnTaxDetail": {},
    "MetaData": {
      "CreateTime": "2015-06-29T12:33:57-07:00",
      "LastUpdatedTime": "2015-06-29T12:33:57-07:00"
    }
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-06-29T12:42:18.004-07:00">
  <JournalEntry domain="QBO" sparse="false">
    <Id>227</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-06-29T12:33:57-07:00</CreateTime>
      <LastUpdatedTime>2015-06-29T12:33:57-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-06-29</TxnDate>
    <Line>
      <Id>0</Id>
      <Description>Four sprinkler heads damaged</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Debit</PostingType>
        <Entity>
            <Type>Customer</Type>
            <EntityRef>
                <value>1</value>
                <name>Amy's Bird Sanctuary</name>
            </EntityRef>
        </Entity>
        <AccountRef name="Job Expenses:Job Materials:Fountain and Garden Lighting">65</AccountRef>
      </JournalEntryLineDetail>
      <ProjectRef>39298034</ProjectRef>
    </Line>
    <Line>
      <Id>1</Id>
      <Description>Sprinkler Hds - Sprinkler Hds Inventory Adjustment</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Credit</PostingType>
        <Entity>
            <Type>Vendor</Type>
            <EntityRef>
                <value>2</value>
                <name>IDX Vendor</name>
            </EntityRef>
        </Entity>
        <AccountRef name="Notes Payable">44</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <TxnTaxDetail />
    <Adjustment>false</Adjustment>
  </JournalEntry>
</IntuitResponse>
```

## Create a journalentry

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/journalentry`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

A JournalEntry must have at least one set of two `Line` elements that balance each other out: one for the debit side and one for the credit side describing the entry.

The minimum elements to create an JournalEntry are listed here.

Schema: `journalentryrequest`

<details>
<summary>Show schema for `journalentryrequest`</summary>

#### journalentryrequest

Model type: `object`

##### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of a journal entry. Two line items are required: one with `PostingType` set to `Debit` and one with `PostingType` set to `Credit`. Set `Line.DetailType` to `JournalEntryLine` for both lines.

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### journalentryline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. In requests, if `Id` matches that for an existing line in the transaction the line is updated. Otherwise, a new line is created. Integer as string.

###### `JournalEntryLineDetail`

Required: Required
Type: `JournalEntryLineDetail`

<details>
<summary>Child attributes for `JournalEntryLineDetail`</summary>

###### journalentrylinedetail

Model type: `object`

###### `JournalCodeRef`

Required: Required
Type: `ReferenceType`
Minor version: 5
Locales: FR

For France locales, only. Reference to a JournalCode object. This must be present for both `Credit` and `Debit` posting sides of the JournalEntry object. Query the JournalCode name list resource to determine the appropriate JournalCode object for this reference. Use `JournalCode.Id` and `JournalCode.Name` from that object for `JournalCodeRef.value` and `JournalCodeRef.name`, respectively.

<details>
<summary>Child attributes for `JournalCodeRef`</summary>

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

###### `PostingType`

Required: Required
Type: `PostingTypeEnum`

Indicates whether this JournalEntry line is a debit or credit. Valid values: `Credit`, `Debit`

###### `AccountRef`

Required: Required
Type: `ReferenceType`

Reference to the account associated with this line. Query the Account name list resource to determine the appropriate Account object for this reference, based on the side of the journal entry represented by this line. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively. For France locales: The account associated with the referenced Account object is looked up in the account category list.

If this account has same location as specified in the transaction by the `TransactionLocationType` attribute and the same VAT as in the line item `TaxCodeRef` attribute, then this account is used.

If there is a mismatch, then the account from the account category list that matches the transaction location and VAT is used.

If this account is not present in the account category list, then a new account is created with the new location, new VAT code, and all other attributes as in the default account.

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

###### `TaxApplicableOn`

Required: Conditionally required
Type: `TaxApplicableOnEnum`
Locales: GB, AU, IN

Indicates whether the tax applicable on the line is sales or purchase. Valid value: `Sales`, `Purchase`. Required if `TaxCodeRef` is specified

###### `Entity`

Required: Conditionally required

When you use `Accounts Receivable`, you must choose a `customer` in the Name field. When you use `Accounts Payable`, you must choose a `supplier/vendor` in the Name field.

<details>
<summary>Child attributes for `Entity`</summary>

###### entity

Model type: `object`

###### `EntityRef`

Required: Required
Type: `ReferenceType`

Query the corresponding name list resource as specified by `Entity` to determine the appropriate object for this reference. Use the `Id` and `DisplayName` values from that object for `EntityRef.value` and `EntityRef.name`, respectively.

<details>
<summary>Child attributes for `EntityRef`</summary>

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

###### `Type`

Type: `EntityTypeEnum`

Object type. Output only. Valid values are `Vendor`, `Employee`, or `Customer`.

</details>

###### `TaxAmount`

Type: `Decimal`
Max length: Min: 0, Max:999999999
Locales: GB, AU, IN

Tax amount of the line.

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`
Minor version: 53
Locales: AU

The total amount of the line items including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with the transaction. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerTxn` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

A reference to a Department object specifying the location of the transaction. Available if `Preferences.AccountingInfoPrefs.TrackDepartments` is set to `true`.
Query the Department name list resource to determine the appropriate department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

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

###### `TaxCodeRef`

Required: Optional
Type: `ReferenceType`
Locales: GB, AU, IN

Reference to the `TaxCode`for this item. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively.

<details>
<summary>Child attributes for `TaxCodeRef`</summary>

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

###### `BillableStatus`

Required: Optional
Type: `BillableStatusEnum`
Traits: read only

The billable status of the journal entry line. The line is to be billed to a customer if the account is an expense account and `EntityRef` specifies a Customer object. This field is not updatable through an API request. The value automatically changes when an invoice is created. Valid values: `Billable`, `NotBillable`, `HasBeenBilled`

</details>

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `JournalEntryLineDetail`for this type of line.

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item.

###### `ProjectRef`

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

###### `Description`

Required: Optional
Type: `String`
Max length: Max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer

</details>

##### `JournalCodeRef`

Required: Conditionally required
Type: `ReferenceType`
Minor version: 5
Locales: FR

Reference to a JournalCode object. Query the JournalCode name list resource to determine the appropriate JournalCode object for this reference. Use `JournalCode.Id` and `JournalCode.Name` Required for France locales.

<details>
<summary>Child attributes for `JournalCodeRef`</summary>

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

##### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company. Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company.

<details>
<summary>Child attributes for `CurrencyRef`</summary>

###### currencyref

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

</details>

#### Example

```json
{
  "Line": [
    {
      "JournalEntryLineDetail": {
        "PostingType": "Debit",
        "AccountRef": {
          "name": "Opening Bal Equity",
          "value": "39"
        }
      },
      "DetailType": "JournalEntryLineDetail",
      "Amount": 100.0,
      "Id": "0",
      "Description": "nov portion of rider insurance"
    },
    {
      "JournalEntryLineDetail": {
        "PostingType": "Credit",
        "AccountRef": {
          "name": "Notes Payable",
          "value": "44"
        }
      },
      "DetailType": "JournalEntryLineDetail",
      "Amount": 100.0,
      "Description": "nov portion of rider insurance"
    }
  ]
}
```

#### XML example

```xml
<JournalEntry xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
 <Line>
      <Id>0</Id>
      <Description>Four sprinkler heads damaged</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Debit</PostingType>
        <AccountRef name="Landscaping Services:Job Materials:Sprinklers &amp; Drip systems">65</AccountRef>
        <ClassRef name="Landscaping">100000000000368490</ClassRef>
      </JournalEntryLineDetail>
    </Line>
    <Line>
      <Id>1</Id>
      <Description>Sprinkler Hds - Sprinkler Hds Inventory Adjustment</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Credit</PostingType>
        <AccountRef name="Inventory Asset">44</AccountRef>
      </JournalEntryLineDetail>
    </Line>
</JournalEntry>
```

### Returns

The JournalEntry response body.

#### Example

```json
{
  "time": "2015-06-29T12:45:32.183-07:00",
  "JournalEntry": {
    "SyncToken": "0",
    "domain": "QBO",
    "TxnDate": "2015-06-29",
    "sparse": false,
    "Line": [
      {
        "JournalEntryLineDetail": {
          "PostingType": "Debit",
          "AccountRef": {
            "name": "Truck:Depreciation",
            "value": "39"
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "Amount": 100.0,
        "Id": "0",
        "Description": "nov portion of rider insurance"
      },
      {
        "JournalEntryLineDetail": {
          "PostingType": "Credit",
          "AccountRef": {
            "name": "Notes Payable",
            "value": "44"
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "Amount": 100.0,
        "Id": "1",
        "Description": "nov portion of rider insurance"
      }
    ],
    "Adjustment": false,
    "Id": "228",
    "TxnTaxDetail": {},
    "MetaData": {
      "CreateTime": "2015-06-29T12:45:32-07:00",
      "LastUpdatedTime": "2015-06-29T12:45:32-07:00"
    }
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-06-29T12:33:57.095-07:00">
  <JournalEntry domain="QBO" sparse="false">
    <Id>227</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-06-29T12:33:57-07:00</CreateTime>
      <LastUpdatedTime>2015-06-29T12:33:57-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-06-29</TxnDate>
    <Line>
      <Id>0</Id>
      <Description>Four sprinkler heads damaged</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Debit</PostingType>
        <AccountRef name="Job Expenses:Job Materials:Fountain and Garden Lighting">65</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <Line>
      <Id>1</Id>
      <Description>Sprinkler Hds - Sprinkler Hds Inventory Adjustment</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Credit</PostingType>
        <AccountRef name="Notes Payable">44</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <TxnTaxDetail />
    <Adjustment>false</Adjustment>
  </JournalEntry>
</IntuitResponse>
```

## Delete a journalentry

### Definition

- **Operation:** `POST /v3/company/<realmID>/journalentry?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the JournalEntry object specified in the request body. Include a minimum of `JournalEntry.Id` and `JournalEntry.SyncToken` in the request body.

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
  "Id": "228"
}
```

#### XML example

```xml
<JournalEntry xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>227</Id>
    <SyncToken>1</SyncToken>
</JournalEntry>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "time": "2015-05-26T14:03:31.321-07:00",
  "JournalEntry": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "228"
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-05-26T14:04:36.332-07:00">
    <JournalEntry domain="QBO" status="Deleted">
        <Id>227</Id>
    </JournalEntry>
</IntuitResponse>
```

## Query a journalentry

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from JournalEntry Where Metadata.LastUpdatedTime>'2014-09-15T00:00:00-07:00' Order By Metadata.LastUpdatedTime"
```

#### XML example

```sql
select * from JournalEntry where id = '227'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 3,
    "maxResults": 3,
    "JournalEntry": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "TxnDate": "2014-09-16",
        "PrivateNote": "Opening Balance",
        "sparse": false,
        "Line": [
          {
            "JournalEntryLineDetail": {
              "PostingType": "Credit",
              "AccountRef": {
                "name": "Notes Payable",
                "value": "44"
              }
            },
            "DetailType": "JournalEntryLineDetail",
            "Amount": 25000.0,
            "Id": "0",
            "Description": "Opening Balance"
          },
          {
            "JournalEntryLineDetail": {
              "PostingType": "Debit",
              "AccountRef": {
                "name": "Opening Balance Equity",
                "value": "34"
              }
            },
            "DetailType": "JournalEntryLineDetail",
            "Amount": 25000.0,
            "Id": "1",
            "Description": "Opening Balance"
          }
        ],
        "Adjustment": false,
        "Id": "8",
        "TxnTaxDetail": {},
        "MetaData": {
          "CreateTime": "2014-09-16T10:04:24-07:00",
          "LastUpdatedTime": "2014-09-16T10:04:24-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "TxnDate": "2014-09-16",
        "PrivateNote": "Opening Balance",
        "sparse": false,
        "Line": [
          {
            "JournalEntryLineDetail": {
              "PostingType": "Credit",
              "AccountRef": {
                "name": "Loan Payable",
                "value": "43"
              }
            },
            "DetailType": "JournalEntryLineDetail",
            "Amount": 4000.0,
            "Id": "0",
            "Description": "Opening Balance"
          },
          {
            "JournalEntryLineDetail": {
              "PostingType": "Debit",
              "AccountRef": {
                "name": "Opening Balance Equity",
                "value": "34"
              }
            },
            "DetailType": "JournalEntryLineDetail",
            "Amount": 4000.0,
            "Id": "1",
            "Description": "Opening Balance"
          }
        ],
        "Adjustment": false,
        "Id": "7",
        "TxnTaxDetail": {},
        "MetaData": {
          "CreateTime": "2014-09-16T10:03:25-07:00",
          "LastUpdatedTime": "2014-09-16T10:03:25-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "TxnDate": "2014-09-03",
        "PrivateNote": "Opening Balance",
        "sparse": false,
        "Line": [
          {
            "JournalEntryLineDetail": {
              "PostingType": "Debit",
              "AccountRef": {
                "name": "Truck:Original Cost",
                "value": "38"
              }
            },
            "DetailType": "JournalEntryLineDetail",
            "Amount": 13495.0,
            "Id": "0",
            "Description": "Opening Balance"
          },
          {
            "JournalEntryLineDetail": {
              "PostingType": "Credit",
              "AccountRef": {
                "name": "Opening Balance Equity",
                "value": "34"
              }
            },
            "DetailType": "JournalEntryLineDetail",
            "Amount": 13495.0,
            "Id": "1",
            "Description": "Opening Balance"
          }
        ],
        "Adjustment": false,
        "Id": "6",
        "TxnTaxDetail": {},
        "MetaData": {
          "CreateTime": "2014-09-15T12:11:06-07:00",
          "LastUpdatedTime": "2014-09-15T12:11:06-07:00"
        }
      }
    ]
  },
  "time": "2015-01-16T09:05:53.455-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-06-29T12:47:30.982-07:00">
  <QueryResponse startPosition="1" maxResults="1" totalCount="1">
    <JournalEntry domain="QBO" sparse="false">
      <Id>227</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2015-06-29T12:33:57-07:00</CreateTime>
        <LastUpdatedTime>2015-06-29T12:33:57-07:00</LastUpdatedTime>
      </MetaData>
      <DocNumber>1112</DocNumber>
      <TxnDate>2015-06-29</TxnDate>
      <Line>
        <Id>0</Id>
        <Description>Four sprinkler heads damaged</Description>
        <Amount>25.54</Amount>
        <DetailType>JournalEntryLineDetail</DetailType>
        <JournalEntryLineDetail>
          <PostingType>Debit</PostingType>
          <AccountRef name="Job Expenses:Job Materials:Fountain and Garden Lighting">65</AccountRef>
        </JournalEntryLineDetail>
      </Line>
      <Line>
        <Id>1</Id>
        <Description>Sprinkler Hds - Sprinkler Hds Inventory Adjustment</Description>
        <Amount>25.54</Amount>
        <DetailType>JournalEntryLineDetail</DetailType>
        <JournalEntryLineDetail>
          <PostingType>Credit</PostingType>
          <AccountRef name="Notes Payable">44</AccountRef>
        </JournalEntryLineDetail>
      </Line>
      <TxnTaxDetail />
      <Adjustment>false</Adjustment>
    </JournalEntry>
  </QueryResponse>
</IntuitResponse>
```

## Read a journalentry

### Definition

- **Operation:** `GET /v3/company/<realmID>/journalentry/<journalentryId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of an JournalEntry that has been previously created.

### Returns

The JournalEntry response body.

#### Example

```json
{
  "time": "2015-06-29T12:43:42.132-07:00",
  "JournalEntry": {
    "SyncToken": "0",
    "domain": "QBO",
    "TxnDate": "2015-06-29",
    "sparse": false,
    "Line": [
      {
        "Description": "Four sprinkler heads damaged",
        "JournalEntryLineDetail": {
          "PostingType": "Debit",
          "AccountRef": {
            "name": "Job Expenses:Job Materials:Fountain and Garden Lighting",
            "value": "65"
          },
          "Entity": {
            "Type": "Customer",
            "EntityRef": {
              "name": "Amy's Bird Sanctuary",
              "value": "1"
            }
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "ProjectRef": {
          "value": "39298034"
        },
        "Amount": 25.54,
        "Id": "0"
      },
      {
        "JournalEntryLineDetail": {
          "PostingType": "Credit",
          "AccountRef": {
            "name": "Notes Payable",
            "value": "44"
          },
          "Entity": {
            "Type": "Vendor",
            "EntityRef": {
              "name": "IDX Vendor",
              "value": "2"
            }
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "Amount": 25.54,
        "Id": "1",
        "Description": "Sprinkler Hds - Sprinkler Hds Inventory Adjustment"
      }
    ],
    "Adjustment": false,
    "Id": "227",
    "TxnTaxDetail": {},
    "MetaData": {
      "CreateTime": "2015-06-29T12:33:57-07:00",
      "LastUpdatedTime": "2015-06-29T12:33:57-07:00"
    }
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-06-29T12:42:18.004-07:00">
  <JournalEntry domain="QBO" sparse="false">
    <Id>227</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-06-29T12:33:57-07:00</CreateTime>
      <LastUpdatedTime>2015-06-29T12:33:57-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-06-29</TxnDate>
    <Line>
      <Id>0</Id>
      <Description>Four sprinkler heads damaged</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Debit</PostingType>
        <Entity>
            <Type>Customer</Type>
            <EntityRef>
                <value>1</value>
                <name>Amy's Bird Sanctuary</name>
            </EntityRef>
        </Entity>
        <AccountRef name="Job Expenses:Job Materials:Fountain and Garden Lighting">65</AccountRef>
      </JournalEntryLineDetail>
      <ProjectRef>39298034</ProjectRef>
    </Line>
    <Line>
      <Id>1</Id>
      <Description>Sprinkler Hds - Sprinkler Hds Inventory Adjustment</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Credit</PostingType>
        <Entity>
            <Type>Vendor</Type>
            <EntityRef>
                <value>2</value>
                <name>IDX Vendor</name>
            </EntityRef>
        </Entity>
        <AccountRef name="Notes Payable">44</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <TxnTaxDetail />
    <Adjustment>false</Adjustment>
  </JournalEntry>
</IntuitResponse>
```

## Full update a journalentry

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/journalentry`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing JournalEntry object. The request body must include all writable fields of the existing object, including all lines, as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `journalentryresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "1",
  "domain": "QBO",
  "TxnDate": "2015-06-29",
  "sparse": false,
  "Line": [
    {
      "JournalEntryLineDetail": {
        "PostingType": "Debit",
        "AccountRef": {
          "name": "Job Expenses:Job Materials:Fountain and Garden Lighting",
          "value": "65"
        }
      },
      "DetailType": "JournalEntryLineDetail",
      "Amount": 25.54,
      "Id": "0",
      "Description": "Updated description"
    },
    {
      "JournalEntryLineDetail": {
        "PostingType": "Credit",
        "AccountRef": {
          "name": "Notes Payable",
          "value": "44"
        }
      },
      "DetailType": "JournalEntryLineDetail",
      "Amount": 25.54,
      "Id": "1",
      "Description": "Sprinkler Hds - Sprinkler Hds Inventory Adjustment"
    }
  ],
  "Adjustment": false,
  "Id": "227",
  "TxnTaxDetail": {},
  "MetaData": {
    "CreateTime": "2015-06-29T12:33:57-07:00",
    "LastUpdatedTime": "2015-06-29T12:33:57-07:00"
  }
}
```

#### XML example

```xml
<JournalEntry xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
   <Id>227</Id>
    <SyncToken>2</SyncToken>
    <MetaData>
      <CreateTime>2015-06-29T12:33:57-07:00</CreateTime>
      <LastUpdatedTime>2015-06-29T12:33:57-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-06-29</TxnDate>
    <Line>
      <Id>0</Id>
      <Description>Updated Description</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Debit</PostingType>
        <AccountRef name="Job Expenses:Job Materials:Fountain and Garden Lighting">65</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <Line>
      <Id>1</Id>
      <Description>Sprinkler Hds - Sprinkler Hds Inventory Adjustment</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Credit</PostingType>
        <AccountRef name="Notes Payable">44</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <TxnTaxDetail />
    <Adjustment>false</Adjustment>
</JournalEntry>
```

### Returns

The journalentry response body.

#### Example

```json
{
  "time": "2015-06-29T12:57:14.02-07:00",
  "JournalEntry": {
    "SyncToken": "2",
    "domain": "QBO",
    "TxnDate": "2015-06-29",
    "sparse": false,
    "Line": [
      {
        "JournalEntryLineDetail": {
          "PostingType": "Debit",
          "AccountRef": {
            "name": "Job Expenses:Job Materials:Fountain and Garden Lighting",
            "value": "65"
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "Amount": 25.54,
        "Id": "0",
        "Description": "Updated description"
      },
      {
        "JournalEntryLineDetail": {
          "PostingType": "Credit",
          "AccountRef": {
            "name": "Notes Payable",
            "value": "44"
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "Amount": 25.54,
        "Id": "1",
        "Description": "Sprinkler Hds - Sprinkler Hds Inventory Adjustment"
      }
    ],
    "Adjustment": false,
    "Id": "227",
    "TxnTaxDetail": {},
    "MetaData": {
      "CreateTime": "2015-06-29T12:33:57-07:00",
      "LastUpdatedTime": "2015-06-29T12:57:15-07:00"
    }
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-06-29T13:09:49.199-07:00">
  <JournalEntry domain="QBO" sparse="false">
    <Id>227</Id>
    <SyncToken>3</SyncToken>
    <MetaData>
      <CreateTime>2015-06-29T12:33:57-07:00</CreateTime>
      <LastUpdatedTime>2015-06-29T13:09:50-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-06-29</TxnDate>
    <Line>
      <Id>0</Id>
      <Description>Updated Description</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Debit</PostingType>
        <AccountRef name="Job Expenses:Job Materials:Fountain and Garden Lighting">65</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <Line>
      <Id>1</Id>
      <Description>Sprinkler Hds - Sprinkler Hds Inventory Adjustment</Description>
      <Amount>25.54</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Credit</PostingType>
        <AccountRef name="Notes Payable">44</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <TxnTaxDetail />
    <Adjustment>false</Adjustment>
  </JournalEntry>
</IntuitResponse>
```

## Sparse update a journalentry

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/journalentry`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Sparse updating provides the ability to update a subset of properties for a given object; only elements specified in the request are updated. Missing elements are left untouched. The ID of the object to update is specified in the request body.​

### Request Body

Schema: `journalentryresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "1",
  "domain": "QBO",
  "TxnDate": "2015-11-30",
  "PrivateNote": "Revised private note via sparse update",
  "sparse": true,
  "Adjustment": false,
  "Id": "227"
}
```

#### XML example

```xml
<JournalEntry xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>842</Id>
    <SyncToken>1</SyncToken>
    <PrivateNote>Revised private note via sparse update</PrivateNote>
    <TxnTaxDetail />
    <Adjustment>false</Adjustment>
  </JournalEntry>
```

### Returns

The JournalEntry response body.

#### Example

```json
{
  "time": "2015-06-29T12:54:38.135-07:00",
  "JournalEntry": {
    "DocNumber": "1112",
    "SyncToken": "1",
    "domain": "QBO",
    "TxnDate": "2015-11-30",
    "PrivateNote": "Revised private note via sparse update",
    "sparse": false,
    "Line": [
      {
        "JournalEntryLineDetail": {
          "PostingType": "Debit",
          "AccountRef": {
            "name": "Job Expenses:Job Materials:Fountain and Garden Lighting",
            "value": "65"
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "Amount": 25.54,
        "Id": "0",
        "Description": "Four sprinkler heads damaged"
      },
      {
        "JournalEntryLineDetail": {
          "PostingType": "Credit",
          "AccountRef": {
            "name": "Notes Payable",
            "value": "44"
          }
        },
        "DetailType": "JournalEntryLineDetail",
        "Amount": 25.54,
        "Id": "1",
        "Description": "Sprinkler Hds - Sprinkler Hds Inventory Adjustment"
      }
    ],
    "Adjustment": false,
    "Id": "227",
    "TxnTaxDetail": {},
    "MetaData": {
      "CreateTime": "2015-06-29T12:33:57-07:00",
      "LastUpdatedTime": "2015-06-29T12:54:38-07:00"
    }
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-06-29T12:53:48.529-07:00">
  <JournalEntry domain="QBO" sparse="false">
    <Id>228</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2015-06-29T12:45:32-07:00</CreateTime>
      <LastUpdatedTime>2015-06-29T12:53:48-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-06-29</TxnDate>
    <PrivateNote>Revised private note via sparse update</PrivateNote>
    <Line>
      <Id>0</Id>
      <Description>nov portion of rider insurance</Description>
      <Amount>100.00</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Debit</PostingType>
        <AccountRef name="Truck:Depreciation">39</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <Line>
      <Id>1</Id>
      <Description>nov portion of rider insurance</Description>
      <Amount>100.00</Amount>
      <DetailType>JournalEntryLineDetail</DetailType>
      <JournalEntryLineDetail>
        <PostingType>Credit</PostingType>
        <AccountRef name="Notes Payable">44</AccountRef>
      </JournalEntryLineDetail>
    </Line>
    <TxnTaxDetail />
    <Adjustment>false</Adjustment>
  </JournalEntry>
</IntuitResponse>
```
