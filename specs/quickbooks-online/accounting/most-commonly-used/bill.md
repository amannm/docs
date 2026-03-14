# Bill

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/bill
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Most commonly used](index.md) / Bill
> Canonical entity: `Bill`

A Bill object is an AP transaction representing a request-for-payment from a third party for goods/services rendered, received, or both.

## The bill object

### billresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `VendorRef`

Required: Required
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the vendor for this transaction. Query the Vendor name list resource to determine the appropriate Vendor object for this reference. Use `Vendor.Id` and `Vendor.Name` from that object for `VendorRef.value` and `VendorRef.name`, respectively.

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

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of a transaction. Valid `Line` types include: `ItemBasedExpenseLine` and `AccountBasedExpenseLine`

<details>
<summary>Child attributes for `Line [0..n]`</summary>

##### itembasedexpenseline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. Its use in requests is as folllows:

If `Id`is greater than zero and exists for the company, the request is considered an update operation for a line item.

If no `Id`is provided, the `Id`provided is less than or equal to zero, or the `Id`provided is greater than zero and does not exist for the company then the request is considered a create operation for a line item.

Available in all objects that use lines and support the update operation.

###### `ItemBasedExpenseLineDetail`

Required: Required
Type: `ItemBasedExpenseLineDetail`

<details>
<summary>Child attributes for `ItemBasedExpenseLineDetail`</summary>

###### itembasedexpenselinedetail

Model type: `object`

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`

The total amount of the line item including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to the Item. Query the Item name list resource to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively. When a line lacks an ItemRef it is treated as documentation and the `Line.Amount` attribute is ignored. For France locales: The account associated with the referenced Item object is looked up in the account category list.

If this account has same location as specified in the transaction by the `TransactionLocationType` attribute and the same VAT as in the line item `TaxCodeRef` attribute, then the item account is used.

If there is a mismatch, then the account from the account category list that matches the transaction location and VAT is used.

If this account is not present in the account category list, then a new account is created with the new location, new VAT code, and all other attributes as in the default account.

<details>
<summary>Child attributes for `ItemRef`</summary>

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

###### `PriceLevelRef`

Required: Optional
Type: `ReferenceType`

Reference to the PriceLevel of the service or item for the line. Support for this element will be available in the coming months.

<details>
<summary>Child attributes for `PriceLevelRef`</summary>

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

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with the expense. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

###### `MarkupInfo`

Required: Optional
Type: `MarkupInfo`

Markup information for the expense.

<details>
<summary>Child attributes for `MarkupInfo`</summary>

###### markupinfo

Model type: `object`

###### `PriceLevelRef`

Required: Optional
Type: `ReferenceType`

Reference to a PriceLevel for the markup. Support for this element will be available in the coming months.

<details>
<summary>Child attributes for `PriceLevelRef`</summary>

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

###### `Percent`

Required: Optional
Type: `Decimal`

Markup amount expressed as a percent of charges already entered in the current transaction. To enter a rate of 10% use 10.0, not 0.01.

###### `MarkUpIncomeAccountRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, system defined

The account associated with the markup. Available with invoice objects, only, and when linktxn specified a `ReimburseCharge`.

<details>
<summary>Child attributes for `MarkUpIncomeAccountRef`</summary>

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

###### `BillableStatus`

Required: Optional
Type: `BillableStatusEnum`
Traits: read only

The billable status of the expense. This field is not updatable through an API request. The value automatically changes when an invoice is created. Valid values: `Billable`, `NotBillable`, `HasBeenBilled`

###### `Qty`

Required: Optional
Type: `Decimal`

Number of items for the line.

###### `UnitPrice`

Required: Optional
Type: `Decimal`

Unit price of the subject item as referenced by `ItemRef`. Corresponds to the Rate column on the QuickBooks Online UI to specify either unit price, a discount, or a tax rate for item. If used for unit price, the monetary value of the service or product, as expressed in the home currency. If used for a discount or tax rate, express the percentage as a fraction. For example, specify `0.4` for 40% tax.

</details>

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item.

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `ItemBasedExpenseLineDetail` for this type of line.

###### `LinkedTxn [0..n]`

Required: Optional
Type: `LinkedTxn`
Minor version: 55

Zero or more transactions linked to this object. The `LinkedTxn.TxnType` can be set to `ReimburseCharge`. The `LinkedTxn.TxnId` can be set as the ID of the transaction.

<details>
<summary>Child attributes for `LinkedTxn [0..n]`</summary>

###### linkedtxn

Model type: `object`

###### `TxnId`

Required: Required
Type: `String`

Transaction Id of the related transaction.

###### `TxnType`

Required: Required
Type: `String`

Transaction type of the linked object.

###### `TxnLineId`

Required: Conditionally required
Type: `String`

Required for Deposit and Bill entities. The line number of a specific line of the linked transaction. If supplied, the `TxnId` and `TxnType` attributes of the linked transaction must also be populated.

</details>

###### `Description`

Required: Optional
Type: `String`
Max length: Max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer.

##### accountbasedexpenseline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. Its use in requests is as folllows:

If `Id`is greater than zero and exists for the company, the request is considered an update operation for a line item.

If no `Id`is provided, the `Id`provided is less than or equal to zero, or the `Id`provided is greater than zero and does not exist for the company then the request is considered a create operation for a line item.

Available in all objects that use lines and support the update operation.

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `AccountBasedExpenseLineDetail`for this type of line.

###### `Amount`

Required: Required
Type: `Decimal`
Max length: max 15 digits in 10.5 format

The amount of the line item.

###### `AccountBasedExpenseLineDetail`

Required: Required
Type: `AccountBasedExpense`

**LineDetail**

<details>
<summary>Child attributes for `AccountBasedExpenseLineDetail`</summary>

###### accountbasedexpenselinedetail

Model type: `object`

###### `AccountRef`

Required: Required
Type: `ReferenceType`

Reference to the Expense account associated with this item. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType=Expense`. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively. For France locales: The account associated with the referenced Account object is looked up in the account category list.

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

###### `TaxAmount`

Required: Optional
Type: `Decimal`

Sales tax paid as part of the expense.

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`
Minor version: 1

The total amount of the line item including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with the expense. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

###### `TaxCodeRef`

Required: Optional
Type: `ReferenceType`

The `TaxCode`associated with the sales tax for the expense. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively.

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

###### `MarkupInfo`

Required: Optional
Type: `MarkupInfo`

Markup information for the expense.

<details>
<summary>Child attributes for `MarkupInfo`</summary>

###### markupinfo

Model type: `object`

###### `PriceLevelRef`

Required: Optional
Type: `ReferenceType`

Reference to a PriceLevel for the markup. Support for this element will be available in the coming months.

<details>
<summary>Child attributes for `PriceLevelRef`</summary>

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

###### `Percent`

Required: Optional
Type: `Decimal`

Markup amount expressed as a percent of charges already entered in the current transaction. To enter a rate of 10% use 10.0, not 0.01.

###### `MarkUpIncomeAccountRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, system defined

The account associated with the markup. Available with invoice objects, only, and when linktxn specified a `ReimburseCharge`.

<details>
<summary>Child attributes for `MarkUpIncomeAccountRef`</summary>

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

###### `BillableStatus`

Required: Optional
Type: `BillableStatusEnum`
Traits: read only

The billable status of the expense. This field is not updatable through an API request. The value automatically changes when an invoice is created. Valid values: `Billable`, `NotBillable`, `HasBeenBilled`

###### `CustomerRef`

Required: Optional
Type: `ReferenceType`

Reference to the Customer associated with the expense. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

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

###### `Description`

Required: Optional
Type: `String`
Max length: max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive Integer.

</details>

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company. Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company.

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
Locales: GB, AU, IN, CA

Method in which tax is applied. Allowed values are: `TaxExcluded`, `TaxInclusive`, and `NotApplicable`. Not applicable to US companies; required for non-US companies.

#### `HomeBalance`

Type: `Decimal`
Traits: read only
Minor version: 3

Convenience field containing the amount in `Balance` expressed in terms of the home currency. Calculated by QuickBooks business logic. Value is valid only when `CurrencyRef` is specified and available when endpoint is evoked with the `minorversion=3` query parameter. Applicable if multicurrency is enabled for the company.

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `Bill` was created from.

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

#### `Balance`

Type: `Decimal`
Traits: read only, filterable

The balance reflecting any payments made against the transaction. Initially set to the value of `TotalAmt`. A Balance of 0 indicates the bill is fully paid. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: current server date

The date entered by the user when this transaction occurred. For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.
Sort order is ASC by default.

#### `APAccountRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable, sortable

Specifies to which AP account the bill is credited. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `APAccountRef.value` and `APAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Liability` and `Account.AccountSubType` set to `AccountsPayable`. If the company has a single AP account, the account is implied. However, it is recommended that the AP Account be explicitly specified in all cases to prevent unexpected errors when relating transactions to each other.

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

#### `SalesTermRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the Term associated with the transaction. Query the Term name list resource to determine the appropriate Term object for this reference. Use `Term.Id` and `Term.Name` from that object for `SalesTermRef.value` and `SalesTermRef.name`, respectively.

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

#### `LinkedTxn [0..n]`

Required: Optional
Type: `LinkedTxn`

Zero or more transactions linked to this Bill object. The `LinkedTxn.TxnType` can be set to `PurchaseOrder`, `BillPaymentCheck` or if using Minor Version 55 and above `ReimburseCharge`. Use `LinkedTxn.TxnId` as the ID of the transaction.

<details>
<summary>Child attributes for `LinkedTxn [0..n]`</summary>

##### linkedtxn

Model type: `object`

###### `TxnId`

Required: Required
Type: `String`

Transaction Id of the related transaction.

###### `TxnType`

Required: Required
Type: `String`

Transaction type of the linked object.

###### `TxnLineId`

Required: Conditionally required
Type: `String`

Required for Deposit and Bill entities. The line number of a specific line of the linked transaction. If supplied, the `TxnId` and `TxnType` attributes of the linked transaction must also be populated.

</details>

#### `TotalAmt`

Required: Optional
Type: `BigDecimal`
Traits: read only, filterable, sortable

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

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

#### `DueDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable

Date when the payment of the transaction is due. If date is not provided, the number of days specified in `SalesTermRef` added the transaction date will be used.

<details>
<summary>Child attributes for `DueDate`</summary>

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

#### `DocNumber`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 21 chars

Reference number for the transaction. If not explicitly provided at create time, a custom value can be provided. If no value is supplied, the resulting DocNumber is null. Throws an error when duplicate DocNumber is sent in the request. Recommended best practice: check the setting of `Preferences:OtherPrefs` before setting DocNumber. If a duplicate DocNumber needs to be supplied, add the query parameter name/value pair, `include=allowduplicatedocnum` to the URI. Sort order is ASC by default.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Memo field on the Invoice form.

#### `TxnTaxDetail`

Required: Optional
Type: `TxnTaxDetail`
Locales: GB, AU, IN, CA

This data type provides information for taxes charged on the transaction as a whole. It captures the details of all taxes calculated for the transaction based on the tax codes referenced by the transaction. This can be calculated by QuickBooks business logic or you may supply it when adding a transaction. If sales tax is disabled (`Preferences.TaxPrefs.UsingSalesTax` is set to `false`) then `TxnTaxDetail` is ignored and not stored.

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

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

#### `DepartmentRef`

Required: Optional
Type: `ReferenceType`

A reference to a Department object specifying the location of the transaction, as defined using location tracking in QuickBooks Online. Query the Department name list resource to determine the appropriate department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

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

#### `IncludeInAnnualTPAR`

Required: Optional
Type: `Boolean`
Default: <span class="literal">false</span>
Minor version: 40
Locales: AU

Include the supplier in the annual TPAR. TPAR stands for Taxable Payments Annual Report. The TPAR is mandated by ATO to get the details payments that businesses make to contractors for providing services. Some government entities also need to report the grants they have paid in a TPAR.

#### Example

```json
{
  "Bill": {
    "SyncToken": "2",
    "domain": "QBO",
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "VendorRef": {
      "name": "Norton Lumber and Building Materials",
      "value": "46"
    },
    "TxnDate": "2014-11-06",
    "TotalAmt": 103.55,
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "LinkedTxn": [
      {
        "TxnId": "118",
        "TxnType": "BillPaymentCheck"
      }
    ],
    "SalesTermRef": {
      "value": "3"
    },
    "DueDate": "2014-12-06",
    "sparse": false,
    "Line": [
      {
        "Description": "Lumber",
        "DetailType": "AccountBasedExpenseLineDetail",
        "ProjectRef": {
          "value": "39298034"
        },
        "Amount": 103.55,
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "AccountRef": {
            "name": "Job Expenses:Job Materials:Decks and Patios",
            "value": "64"
          },
          "BillableStatus": "Billable",
          "CustomerRef": {
            "name": "Travis Waldron",
            "value": "26"
          }
        }
      }
    ],
    "Balance": 0,
    "Id": "25",
    "MetaData": {
      "CreateTime": "2014-11-06T15:37:25-08:00",
      "LastUpdatedTime": "2015-02-09T10:11:11-08:00"
    }
  },
  "time": "2015-02-09T10:17:20.251-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-09T10:11:31.515-08:00">
    <Bill domain="QBO" sparse="false">
        <Id>25</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2014-11-06T15:37:25-08:00</CreateTime>
            <LastUpdatedTime>2015-02-09T10:11:11-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-11-06</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <LinkedTxn>
            <TxnId>118</TxnId>
            <TxnType>BillPaymentCheck</TxnType>
        </LinkedTxn>
        <Line>
            <Id>1</Id>
            <Description>Lumber</Description>
            <Amount>103.55</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <CustomerRef name="Travis Waldron">26</CustomerRef>
                <AccountRef name="Job Expenses:Job Materials:Decks and Patios">64</AccountRef>
                <BillableStatus>Billable</BillableStatus>
                <TaxCodeRef>TAX</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <VendorRef name="Norton Lumber and Building Materials">46</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>103.55</TotalAmt>
        <SalesTermRef>3</SalesTermRef>
        <DueDate>2014-12-06</DueDate>
        <Balance>0</Balance>
    </Bill>
</IntuitResponse>
```

## Create a bill

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/bill`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create an bill are listed here.

Schema: `billrequest`

<details>
<summary>Show schema for `billrequest`</summary>

#### billrequest

Model type: `object`

##### `VendorRef`

Required: Required
Type: `ReferenceType`
Traits: filterable

Reference to the vendor for this transaction. Query the Vendor name list resource to determine the appropriate Vendor object for this reference. Use `Vendor.Id` and `Vendor.Name` from that object for `VendorRef.value` and `VendorRef.name`, respectively.

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

##### `Line [0..n]`

Required: Required
Type: `Line`

The minimum line item required for the request.

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### accountbasedexpenseline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. Its use in requests is as folllows:

If `Id`is greater than zero and exists for the company, the request is considered an update operation for a line item.

If no `Id`is provided, the `Id`provided is less than or equal to zero, or the `Id`provided is greater than zero and does not exist for the company then the request is considered a create operation for a line item.

Available in all objects that use lines and support the update operation.

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `AccountBasedExpenseLineDetail`for this type of line.

###### `Amount`

Required: Required
Type: `Decimal`
Max length: max 15 digits in 10.5 format

The amount of the line item.

###### `AccountBasedExpenseLineDetail`

Required: Required
Type: `AccountBasedExpense`

**LineDetail**

<details>
<summary>Child attributes for `AccountBasedExpenseLineDetail`</summary>

###### accountbasedexpenselinedetail

Model type: `object`

###### `AccountRef`

Required: Required
Type: `ReferenceType`

Reference to the Expense account associated with this item. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType=Expense`. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively. For France locales: The account associated with the referenced Account object is looked up in the account category list.

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

###### `TaxAmount`

Required: Optional
Type: `Decimal`

Sales tax paid as part of the expense.

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`
Minor version: 1

The total amount of the line item including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with the expense. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

###### `TaxCodeRef`

Required: Optional
Type: `ReferenceType`

The `TaxCode`associated with the sales tax for the expense. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively.

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

###### `MarkupInfo`

Required: Optional
Type: `MarkupInfo`

Markup information for the expense.

<details>
<summary>Child attributes for `MarkupInfo`</summary>

###### markupinfo

Model type: `object`

###### `PriceLevelRef`

Required: Optional
Type: `ReferenceType`

Reference to a PriceLevel for the markup. Support for this element will be available in the coming months.

<details>
<summary>Child attributes for `PriceLevelRef`</summary>

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

###### `Percent`

Required: Optional
Type: `Decimal`

Markup amount expressed as a percent of charges already entered in the current transaction. To enter a rate of 10% use 10.0, not 0.01.

###### `MarkUpIncomeAccountRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, system defined

The account associated with the markup. Available with invoice objects, only, and when linktxn specified a `ReimburseCharge`.

<details>
<summary>Child attributes for `MarkUpIncomeAccountRef`</summary>

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

###### `BillableStatus`

Required: Optional
Type: `BillableStatusEnum`
Traits: read only

The billable status of the expense. This field is not updatable through an API request. The value automatically changes when an invoice is created. Valid values: `Billable`, `NotBillable`, `HasBeenBilled`

###### `CustomerRef`

Required: Optional
Type: `ReferenceType`

Reference to the Customer associated with the expense. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

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

###### `Description`

Required: Optional
Type: `String`
Max length: max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive Integer.

</details>

##### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company.

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
      "DetailType": "AccountBasedExpenseLineDetail",
      "Amount": 200.0,
      "Id": "1",
      "AccountBasedExpenseLineDetail": {
        "AccountRef": {
          "value": "7"
        }
      }
    }
  ],
  "VendorRef": {
    "value": "56"
  }
}
```

#### XML example

```xml
<Bill xmlns="http://schema.intuit.com/finance/v3">
    <Line>
        <Id>1</Id>
        <Amount>500.00</Amount>
        <DetailType>AccountBasedExpenseLineDetail</DetailType>
        <AccountBasedExpenseLineDetail>
            <AccountRef>7</AccountRef>
        </AccountBasedExpenseLineDetail>
    </Line>
    <VendorRef>56</VendorRef>
</Bill>
```

### Returns

The bill response body.

#### Example

```json
{
  "Bill": {
    "SyncToken": "0",
    "domain": "QBO",
    "VendorRef": {
      "name": "Bob's Burger Joint",
      "value": "56"
    },
    "TxnDate": "2014-12-31",
    "TotalAmt": 200.0,
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "Id": "151",
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 200.0,
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "AccountRef": {
            "name": "Advertising",
            "value": "7"
          },
          "BillableStatus": "NotBillable"
        }
      }
    ],
    "Balance": 200.0,
    "DueDate": "2014-12-31",
    "MetaData": {
      "CreateTime": "2014-12-31T09:59:18-08:00",
      "LastUpdatedTime": "2014-12-31T09:59:18-08:00"
    }
  },
  "time": "2014-12-31T09:59:17.449-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-31T09:15:04.907-08:00">
    <Bill domain="QBO" sparse="false">
        <Id>148</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-12-31T09:15:05-08:00</CreateTime>
            <LastUpdatedTime>2014-12-31T09:15:05-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-12-31</TxnDate>
        <Line>
            <Id>1</Id>
            <Amount>500.00</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <AccountRef name="Advertising">7</AccountRef>
                <BillableStatus>NotBillable</BillableStatus>
                <TaxCodeRef>NON</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
        </Line>
        <VendorRef name="Bob's Burger Joint">56</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>500.00</TotalAmt>
        <DueDate>2014-12-31</DueDate>
        <Balance>500.00</Balance>
    </Bill>
</IntuitResponse>
```

## Delete a bill

### Definition

- **Operation:** `POST /v3/company/<realmID>/bill?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the bill object specified in the request body. Include a minimum of `Bill.Id` and `Bill.SyncToken` in the request body. You must unlink any linked transactions associated with the bill object before deleting it.

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
  "Id": "108"
}
```

#### XML example

```xml
<Bill xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>126</Id>
    <SyncToken>0</SyncToken>
</Bill>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "Bill": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "108"
  },
  "time": "2015-05-26T13:14:34.775-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-05-26T13:12:16.102-07:00">
    <Bill domain="QBO" status="Deleted">
        <Id>126</Id>
    </Bill>
</IntuitResponse>
```

## Query a bill

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from bill maxresults 2"
```

#### XML example

```sql
select * from bill maxresults 2
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 2,
    "Bill": [
      {
        "SyncToken": "2",
        "domain": "QBO",
        "VendorRef": {
          "name": "Norton Lumber and Building Materials",
          "value": "46"
        },
        "TxnDate": "2014-10-07",
        "TotalAmt": 225.0,
        "APAccountRef": {
          "name": "Accounts Payable (A/P)",
          "value": "33"
        },
        "Id": "150",
        "sparse": false,
        "Line": [
          {
            "DetailType": "ItemBasedExpenseLineDetail",
            "Amount": 100.0,
            "Id": "1",
            "ItemBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "Qty": 8,
              "BillableStatus": "NotBillable",
              "UnitPrice": 10,
              "ItemRef": {
                "name": "Pump",
                "value": "11"
              }
            },
            "Description": "Fountain Pump"
          },
          {
            "DetailType": "ItemBasedExpenseLineDetail",
            "Amount": 125.0,
            "Id": "2",
            "ItemBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "Qty": 1,
              "BillableStatus": "NotBillable",
              "UnitPrice": 125,
              "ItemRef": {
                "name": "Rock Fountain",
                "value": "5"
              }
            },
            "Description": "Rock Fountain"
          }
        ],
        "Balance": 225.0,
        "DueDate": "2014-10-07",
        "MetaData": {
          "CreateTime": "2014-10-15T13:55:31-07:00",
          "LastUpdatedTime": "2014-10-15T14:24:54-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Bob's Burger Joint",
          "value": "56"
        },
        "TxnDate": "2014-10-15",
        "TotalAmt": 200.0,
        "APAccountRef": {
          "name": "Accounts Payable (A/P)",
          "value": "33"
        },
        "Id": "149",
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 200.0,
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "AccountRef": {
                "name": "Advertising",
                "value": "7"
              },
              "BillableStatus": "NotBillable"
            }
          }
        ],
        "Balance": 200.0,
        "DueDate": "2014-10-15",
        "MetaData": {
          "CreateTime": "2014-10-15T13:48:00-07:00",
          "LastUpdatedTime": "2014-10-15T13:48:00-07:00"
        }
      }
    ],
    "maxResults": 2
  },
  "time": "2014-10-15T14:41:39.98-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-10-15T14:39:08.540-07:00">
    <QueryResponse startPosition="1" maxResults="2" totalCount="2">
        <Bill domain="QBO" sparse="false">
            <Id>150</Id>
            <SyncToken>2</SyncToken>
            <MetaData>
                <CreateTime>2014-10-15T13:55:31-07:00</CreateTime>
                <LastUpdatedTime>2014-10-15T14:24:54-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-10-07</TxnDate>
            <Line>
                <Id>1</Id>
                <Description>Fountain Pump</Description>
                <Amount>100.00</Amount>
                <DetailType>ItemBasedExpenseLineDetail</DetailType>
                <ItemBasedExpenseLineDetail>
                    <ItemRef name="Pump">11</ItemRef>
                    <UnitPrice>10</UnitPrice>
                    <Qty>8</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                    <BillableStatus>NotBillable</BillableStatus>
                </ItemBasedExpenseLineDetail>
            </Line>
            <Line>
                <Id>2</Id>
                <Description>Rock Fountain</Description>
                <Amount>125.00</Amount>
                <DetailType>ItemBasedExpenseLineDetail</DetailType>
                <ItemBasedExpenseLineDetail>
                    <ItemRef name="Rock Fountain">5</ItemRef>
                    <UnitPrice>125</UnitPrice>
                    <Qty>1</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                    <BillableStatus>NotBillable</BillableStatus>
                </ItemBasedExpenseLineDetail>
            </Line>
            <VendorRef name="Norton Lumber and Building Materials">46</VendorRef>
            <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
            <TotalAmt>225.00</TotalAmt>
            <DueDate>2014-10-07</DueDate>
            <Balance>225.00</Balance>
        </Bill>
        <Bill domain="QBO" sparse="false">
            <Id>149</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-10-15T13:48:00-07:00</CreateTime>
                <LastUpdatedTime>2014-10-15T13:48:00-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-10-15</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>200.00</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <AccountRef name="Advertising">7</AccountRef>
                    <BillableStatus>NotBillable</BillableStatus>
                    <TaxCodeRef>NON</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
            </Line>
            <VendorRef name="Bob's Burger Joint">56</VendorRef>
            <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
            <TotalAmt>200.00</TotalAmt>
            <DueDate>2014-10-15</DueDate>
            <Balance>200.00</Balance>
        </Bill>
    </QueryResponse>
</IntuitResponse>
```

## Read a bill

### Definition

- **Content type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/bill/<billId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a bill that has been previously created.

### Returns

The bill response body.

#### Example

```json
{
  "Bill": {
    "SyncToken": "2",
    "domain": "QBO",
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "VendorRef": {
      "name": "Norton Lumber and Building Materials",
      "value": "46"
    },
    "TxnDate": "2014-11-06",
    "TotalAmt": 103.55,
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "LinkedTxn": [
      {
        "TxnId": "118",
        "TxnType": "BillPaymentCheck"
      }
    ],
    "SalesTermRef": {
      "value": "3"
    },
    "DueDate": "2014-12-06",
    "sparse": false,
    "Line": [
      {
        "Description": "Lumber",
        "DetailType": "AccountBasedExpenseLineDetail",
        "ProjectRef": {
          "value": "39298034"
        },
        "Amount": 103.55,
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "AccountRef": {
            "name": "Job Expenses:Job Materials:Decks and Patios",
            "value": "64"
          },
          "BillableStatus": "Billable",
          "CustomerRef": {
            "name": "Travis Waldron",
            "value": "26"
          }
        }
      }
    ],
    "Balance": 0,
    "Id": "25",
    "MetaData": {
      "CreateTime": "2014-11-06T15:37:25-08:00",
      "LastUpdatedTime": "2015-02-09T10:11:11-08:00"
    }
  },
  "time": "2015-02-09T10:17:20.251-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-09T10:11:31.515-08:00">
    <Bill domain="QBO" sparse="false">
        <Id>25</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2014-11-06T15:37:25-08:00</CreateTime>
            <LastUpdatedTime>2015-02-09T10:11:11-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-11-06</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <LinkedTxn>
            <TxnId>118</TxnId>
            <TxnType>BillPaymentCheck</TxnType>
        </LinkedTxn>
        <Line>
            <Id>1</Id>
            <Description>Lumber</Description>
            <Amount>103.55</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <CustomerRef name="Travis Waldron">26</CustomerRef>
                <AccountRef name="Job Expenses:Job Materials:Decks and Patios">64</AccountRef>
                <BillableStatus>Billable</BillableStatus>
                <TaxCodeRef>TAX</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <VendorRef name="Norton Lumber and Building Materials">46</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>103.55</TotalAmt>
        <SalesTermRef>3</SalesTermRef>
        <DueDate>2014-12-06</DueDate>
        <Balance>0</Balance>
    </Bill>
</IntuitResponse>
```

## Full update a bill

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/bill`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing bill object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `billresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "DocNumber": "56789",
  "SyncToken": "1",
  "domain": "QBO",
  "APAccountRef": {
    "name": "Accounts Payable",
    "value": "49"
  },
  "VendorRef": {
    "name": "Bayshore CalOil Service",
    "value": "81"
  },
  "TxnDate": "2014-04-04",
  "TotalAmt": 200.0,
  "CurrencyRef": {
    "name": "United States Dollar",
    "value": "USD"
  },
  "PrivateNote": "This is a updated memo.",
  "SalesTermRef": {
    "value": "12"
  },
  "DepartmentRef": {
    "name": "Garden Services",
    "value": "1"
  },
  "DueDate": "2013-06-09",
  "sparse": false,
  "Line": [
    {
      "Description": "Gasoline",
      "DetailType": "AccountBasedExpenseLineDetail",
      "ProjectRef": {
        "value": "39298034"
      },
      "Amount": 200.0,
      "Id": "1",
      "AccountBasedExpenseLineDetail": {
        "TaxCodeRef": {
          "value": "TAX"
        },
        "AccountRef": {
          "name": "Automobile",
          "value": "75"
        },
        "BillableStatus": "Billable",
        "CustomerRef": {
          "name": "Blackwell, Edward",
          "value": "20"
        },
        "MarkupInfo": {
          "Percent": 10
        }
      }
    }
  ],
  "Balance": 200.0,
  "Id": "890",
  "MetaData": {
    "CreateTime": "2014-04-04T12:38:01-07:00",
    "LastUpdatedTime": "2014-04-04T12:48:56-07:00"
  }
}
```

#### XML example

```xml
<Bill xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>150</Id>
    <SyncToken>1</SyncToken>
    <TxnDate>2014-10-07</TxnDate>
    <Line>
        <Id>1</Id>
        <Description>Fountain Pump</Description>
        <Amount>100.00</Amount>
        <DetailType>ItemBasedExpenseLineDetail</DetailType>
        <ItemBasedExpenseLineDetail>
            <ItemRef>11</ItemRef>
            <UnitPrice>10</UnitPrice>
            <Qty>8</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
            <BillableStatus>NotBillable</BillableStatus>
        </ItemBasedExpenseLineDetail>
        <ProjectRef>39298045</ProjectRef>
    </Line>
    <Line>
        <Id>2</Id>
        <Description>Rock Fountain</Description>
        <Amount>125.00</Amount>
        <DetailType>ItemBasedExpenseLineDetail</DetailType>
        <ItemBasedExpenseLineDetail>
            <ItemRef>5</ItemRef>
            <UnitPrice>125</UnitPrice>
            <Qty>1</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
            <BillableStatus>NotBillable</BillableStatus>
        </ItemBasedExpenseLineDetail>
        <ProjectRef>39298046</ProjectRef>
    </Line>
    <VendorRef>46</VendorRef>
    <TotalAmt>225.00</TotalAmt>
    <DueDate>2014-10-07</DueDate>
</Bill>
```

### Returns

The bill response body.

#### Example

```json
{
  "Bill": {
    "DocNumber": "56789",
    "SyncToken": "2",
    "domain": "QBO",
    "APAccountRef": {
      "name": "Accounts Payable",
      "value": "49"
    },
    "VendorRef": {
      "name": "Bayshore CalOil Service",
      "value": "81"
    },
    "TxnDate": "2014-04-04",
    "TotalAmt": 200.0,
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "PrivateNote": "This is a updated memo.",
    "SalesTermRef": {
      "value": "12"
    },
    "DepartmentRef": {
      "name": "Garden Services",
      "value": "1"
    },
    "DueDate": "2013-06-09",
    "sparse": false,
    "Line": [
      {
        "Description": "Gasoline",
        "DetailType": "AccountBasedExpenseLineDetail",
        "ProjectRef": {
          "value": "39298034"
        },
        "Amount": 200.0,
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "AccountRef": {
            "name": "Automobile",
            "value": "75"
          },
          "BillableStatus": "Billable",
          "CustomerRef": {
            "name": "Blackwell, Edward",
            "value": "20"
          },
          "MarkupInfo": {
            "Percent": 10
          }
        }
      }
    ],
    "Balance": 200.0,
    "Id": "890",
    "MetaData": {
      "CreateTime": "2014-04-04T12:38:01-07:00",
      "LastUpdatedTime": "2014-04-04T12:58:16-07:00"
    }
  },
  "time": "2014-04-04T12:58:16.491-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-10-15T14:24:54.164-07:00">
    <Bill domain="QBO" sparse="false">
        <Id>150</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2014-10-15T13:55:31-07:00</CreateTime>
            <LastUpdatedTime>2014-10-15T14:24:54-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-10-07</TxnDate>
        <Line>
            <Id>1</Id>
            <Description>Fountain Pump</Description>
            <Amount>100.00</Amount>
            <DetailType>ItemBasedExpenseLineDetail</DetailType>
            <ItemBasedExpenseLineDetail>
                <ItemRef name="Pump">11</ItemRef>
                <UnitPrice>10</UnitPrice>
                <Qty>8</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
                <BillableStatus>NotBillable</BillableStatus>
            </ItemBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <Line>
            <Id>2</Id>
            <Description>Rock Fountain</Description>
            <Amount>125.00</Amount>
            <DetailType>ItemBasedExpenseLineDetail</DetailType>
            <ItemBasedExpenseLineDetail>
                <ItemRef name="Rock Fountain">5</ItemRef>
                <UnitPrice>125</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
                <BillableStatus>NotBillable</BillableStatus>
            </ItemBasedExpenseLineDetail>
            <ProjectRef>39298046</ProjectRef>
        </Line>
        <VendorRef name="Norton Lumber and Building Materials">46</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>225.00</TotalAmt>
        <DueDate>2014-10-07</DueDate>
        <Balance>225.00</Balance>
    </Bill>
</IntuitResponse>
```
