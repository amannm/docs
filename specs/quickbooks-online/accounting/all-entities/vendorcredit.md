# VendorCredit

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/vendorcredit
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / VendorCredit
> Canonical entity: `VendorCredit`

The VendorCredit object is an accounts payable transaction that represents a refund or credit of payment for goods or services. It is a credit that a vendor owes you for various reasons such as overpaid bill, returned merchandise, or other reasons.

## The vendorcredit object

### vendorcreditresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `VendorRef`

Required: Required
Type: `ReferenceType`

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

#### `GlobalTaxCalculation`

Required: Conditionally required
Type: `GlobalTaxCalculationEnum`
Default: <span class="literal">TaxExcluded</span>
Locales: GB, AU, IN, CA

Method in which tax is applied. Allowed values are: `TaxExcluded`, `TaxInclusive`, and `NotApplicable`. Not applicable to US companies; required for non-US companies.

#### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company. Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company

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

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `VendorCredit` was created from.

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
Traits: read only, system defined, filterable, sortable

Indicates the total credit amount, determined by taking the total of all all lines of the transaction. This includes all charges, allowances, discounts, and taxes. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `DocNumber`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 21 chars

Reference number for the transaction. If not explicitly provided at create time, this field is populated based on the setting of `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` as follows:

If `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` is true a custom value can be provided. If no value is supplied, the resulting DocNumber is null.

If `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` is false, resulting DocNumber is system generated by incrementing the last number by 1.

Throws an error when duplicate DocNumber is sent in the request. Recommended best practice: check the setting of `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` before setting DocNumber. If a duplicate DocNumber needs to be supplied, add the query parameter name/value pair, `include=allowduplicatedocnum` to the URI. Sort order is ASC by default.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: Max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the transaction to the vendor. This field maps to the Memo field on the transaction form.

#### `LinkedTxn [0..n]`

Required: Optional
Type: `LinkedTxn`
Minor version: 55

Zero or more transactions linked to this object. The `LinkedTxn.TxnType` can be set to `ReimburseCharge`. The `LinkedTxn.TxnId` can be set as the ID of the transaction.

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

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

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

#### `DepartmentRef`

Required: Optional
Type: `ReferenceType`

A reference to a Department object specifying the location of the transaction. Available if `Preferences.AccountingInfoPrefs.TrackDepartments` is set to `true`. Query the Department name list resource to determine the appropriate department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

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

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: current server date

The date entered by the user when this transaction occurred. For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.
Sort order is ASC by default.

#### `IncludeInAnnualTPAR`

Required: Optional
Type: `Boolean`
Default: <span class="literal">false</span>
Minor version: 40
Locales: AU

Include the supplier in the annual TPAR. TPAR stands for Taxable Payments Annual Report. The TPAR is mandated by ATO to get the details payments that businesses make to contractors for providing services. Some government entities also need to report the grants they have paid in a TPAR.

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

#### `Balance`

Required: Optional
Type: `Decimal`
Traits: read only, sortable
Minor version: 12

The current amount of the vendor credit reflecting any adjustments to the original credit amount. Initially set to the value of `TotalAmt`. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

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
  "VendorCredit": {
    "SyncToken": "0",
    "domain": "QBO",
    "VendorRef": {
      "name": "Books by Bessie",
      "value": "30"
    },
    "TxnDate": "2014-12-23",
    "TotalAmt": 90.0,
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 90.0,
        "ProjectRef": {
          "value": "39298045"
        },
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "AccountRef": {
            "name": "Bank Charges",
            "value": "8"
          },
          "BillableStatus": "Billable",
          "CustomerRef": {
            "name": "Amy's Bird Sanctuary",
            "value": "1"
          }
        }
      }
    ],
    "Id": "255",
    "MetaData": {
      "CreateTime": "2015-07-28T14:13:30-07:00",
      "LastUpdatedTime": "2015-07-28T14:13:30-07:00"
    }
  },
  "time": "2015-07-28T14:16:42.709-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T14:16:22.952-07:00">
    <VendorCredit domain="QBO" sparse="false">
        <Id>255</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T14:13:30-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T14:13:30-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-12-23</TxnDate>
        <Line>
            <Id>1</Id>
            <Amount>90.00</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
                <AccountRef name="Bank Charges">8</AccountRef>
                <BillableStatus>Billable</BillableStatus>
                <TaxCodeRef>TAX</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <VendorRef name="Books by Bessie">30</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>90.00</TotalAmt>
    </VendorCredit>
</IntuitResponse>
```

## Create a vendorcredit

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/vendorcredit`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

The `VendorRef` attribute must be specified.At lease one Line with `Line.Amount` must be specified.

### Request Body

The minimum elements to create an VendorCredit object are listed here.

Schema: `vendorcreditrequest`

<details>
<summary>Show schema for `vendorcreditrequest`</summary>

#### vendorcreditrequest

Model type: `object`

##### `VendorRef`

Required: Required
Type: `ReferenceType`

The vendor reference for this transaction.

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

Individual line items of a transaction. Valid `Line` types include: `ItemBasedExpenseLine` and `AccountBasedExpenseLine`

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### itembasedexpenseline

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

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company. Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company

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
  "TotalAmt": 90.0,
  "TxnDate": "2014-12-23",
  "Line": [
    {
      "DetailType": "AccountBasedExpenseLineDetail",
      "Amount": 90.0,
      "ProjectRef": {
        "value": "39298045"
      },
      "Id": "1",
      "AccountBasedExpenseLineDetail": {
        "TaxCodeRef": {
          "value": "TAX"
        },
        "AccountRef": {
          "name": "Bank Charges",
          "value": "8"
        },
        "BillableStatus": "Billable",
        "CustomerRef": {
          "name": "Amy's Bird Sanctuary",
          "value": "1"
        }
      }
    }
  ],
  "APAccountRef": {
    "name": "Accounts Payable (A/P)",
    "value": "33"
  },
  "VendorRef": {
    "name": "Books by Bessie",
    "value": "30"
  }
}
```

#### XML example

```xml
<VendorCredit xmlns="http://schema.intuit.com/finance/v3">
    <TxnDate>2014-12-23</TxnDate>
    <Line>
        <Id>1</Id>
        <Amount>90.00</Amount>
        <DetailType>AccountBasedExpenseLineDetail</DetailType>
        <AccountBasedExpenseLineDetail>
            <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
            <AccountRef name="Bank Charges">8</AccountRef>
            <BillableStatus>Billable</BillableStatus>
            <TaxCodeRef>TAX</TaxCodeRef>
        </AccountBasedExpenseLineDetail>
        <ProjectRef>39298045</ProjectRef>
    </Line>
    <VendorRef name="Books by Bessie">30</VendorRef>
    <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
    <TotalAmt>90.00</TotalAmt>
</VendorCredit>
```

### Returns

The vendorcredit response body.

#### Example

```json
{
  "VendorCredit": {
    "SyncToken": "0",
    "domain": "QBO",
    "VendorRef": {
      "name": "Books by Bessie",
      "value": "30"
    },
    "TxnDate": "2014-12-23",
    "TotalAmt": 90.0,
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 90.0,
        "ProjectRef": {
          "value": "39298045"
        },
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "AccountRef": {
            "name": "Bank Charges",
            "value": "8"
          },
          "BillableStatus": "Billable",
          "CustomerRef": {
            "name": "Amy's Bird Sanctuary",
            "value": "1"
          }
        }
      }
    ],
    "Id": "157",
    "MetaData": {
      "CreateTime": "2014-12-23T11:14:15-08:00",
      "LastUpdatedTime": "2014-12-23T11:14:15-08:00"
    }
  },
  "time": "2014-12-23T11:14:15.462-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-23T11:11:55.332-08:00">
  <VendorCredit domain="QBO" sparse="false">
    <Id>155</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-12-23T11:11:55-08:00</CreateTime>
      <LastUpdatedTime>2014-12-23T11:11:55-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-12-23</TxnDate>
    <Line>
      <Id>1</Id>
      <Amount>90.00</Amount>
      <DetailType>AccountBasedExpenseLineDetail</DetailType>
      <AccountBasedExpenseLineDetail>
        <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
        <AccountRef name="Bank Charges">8</AccountRef>
        <BillableStatus>Billable</BillableStatus>
        <TaxCodeRef>TAX</TaxCodeRef>
      </AccountBasedExpenseLineDetail>
      <ProjectRef>39298045</ProjectRef>
    </Line>
    <VendorRef name="Books by Bessie">30</VendorRef>
    <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
    <TotalAmt>90.00</TotalAmt>
  </VendorCredit>
</IntuitResponse>
```

## Delete a vendorcredit

### Definition

- **Operation:** `POST /v3/company/<realmID>/vendorcredit?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the vendorcredit object specified in the request body. Include a minimum of `VendorCredit.Id` and `VendorCredit.SyncToken` in the request body.

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
  "Id": "13"
}
```

#### XML example

```xml
<VendorCredit xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>3</Id>
    <SyncToken>0</SyncToken>
</VendorCredit>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "VendorCredit": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "13"
  },
  "time": "2015-05-27T10:42:58.468-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-05-27T10:42:58.468-07:00">
    <VendorCredit domain="QBO" status="Deleted">
        <Id>3</Id>
    </VendorCredit>
</IntuitResponse>
```

## Query a vendorcredit

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from vendorcredit"
```

#### XML example

```sql
select * from VendorCredit
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 2,
    "VendorCredit": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Books by Bessie",
          "value": "30"
        },
        "TxnDate": "2014-12-23",
        "TotalAmt": 90.0,
        "APAccountRef": {
          "name": "Accounts Payable (A/P)",
          "value": "33"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 90.0,
            "ProjectRef": {
              "value": "39298045"
            },
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "TAX"
              },
              "AccountRef": {
                "name": "Bank Charges",
                "value": "8"
              },
              "BillableStatus": "Billable",
              "CustomerRef": {
                "name": "Amy's Bird Sanctuary",
                "value": "1"
              }
            }
          }
        ],
        "Id": "255",
        "MetaData": {
          "CreateTime": "2015-07-28T14:13:30-07:00",
          "LastUpdatedTime": "2015-07-28T14:13:30-07:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Books by Bessie",
          "value": "30"
        },
        "TxnDate": "2014-12-23",
        "TotalAmt": 90.0,
        "APAccountRef": {
          "name": "Accounts Payable (A/P)",
          "value": "33"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 90.0,
            "ProjectRef": {
              "value": "39298045"
            },
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "TAX"
              },
              "AccountRef": {
                "name": "Bank Charges",
                "value": "8"
              },
              "BillableStatus": "Billable",
              "CustomerRef": {
                "name": "Amy's Bird Sanctuary",
                "value": "1"
              }
            }
          }
        ],
        "Id": "253",
        "MetaData": {
          "CreateTime": "2015-07-28T14:13:08-07:00",
          "LastUpdatedTime": "2015-07-28T14:13:08-07:00"
        }
      }
    ],
    "maxResults": 2
  },
  "time": "2015-07-28T14:14:36.327-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T14:14:00.506-07:00">
    <QueryResponse startPosition="1" maxResults="2" totalCount="2">
        <VendorCredit domain="QBO" sparse="false">
            <Id>255</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-07-28T14:13:30-07:00</CreateTime>
                <LastUpdatedTime>2015-07-28T14:13:30-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-12-23</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>90.00</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
                    <AccountRef name="Bank Charges">8</AccountRef>
                    <BillableStatus>Billable</BillableStatus>
                    <TaxCodeRef>TAX</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
                <ProjectRef>39298045</ProjectRef>
            </Line>
            <VendorRef name="Books by Bessie">30</VendorRef>
            <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
            <TotalAmt>90.00</TotalAmt>
        </VendorCredit>
        <VendorCredit domain="QBO" sparse="false">
            <Id>253</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-07-28T14:13:08-07:00</CreateTime>
                <LastUpdatedTime>2015-07-28T14:13:08-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-12-23</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>90.00</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
                    <AccountRef name="Bank Charges">8</AccountRef>
                    <BillableStatus>Billable</BillableStatus>
                    <TaxCodeRef>TAX</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
                <ProjectRef>39298045</ProjectRef>
            </Line>
            <VendorRef name="Books by Bessie">30</VendorRef>
            <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
            <TotalAmt>90.00</TotalAmt>
        </VendorCredit>
    </QueryResponse>
</IntuitResponse>
```

## Read a vendorcredit

### Definition

- **Operation:** `GET /v3/company/<realmID>/vendorcredit/<vendorcreditId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a VendorcCredit object that has been previously created.

### Returns

The vendorcredit response body.

#### Example

```json
{
  "VendorCredit": {
    "SyncToken": "0",
    "domain": "QBO",
    "VendorRef": {
      "name": "Books by Bessie",
      "value": "30"
    },
    "TxnDate": "2014-12-23",
    "TotalAmt": 90.0,
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 90.0,
        "ProjectRef": {
          "value": "39298045"
        },
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "AccountRef": {
            "name": "Bank Charges",
            "value": "8"
          },
          "BillableStatus": "Billable",
          "CustomerRef": {
            "name": "Amy's Bird Sanctuary",
            "value": "1"
          }
        }
      }
    ],
    "Id": "255",
    "MetaData": {
      "CreateTime": "2015-07-28T14:13:30-07:00",
      "LastUpdatedTime": "2015-07-28T14:13:30-07:00"
    }
  },
  "time": "2015-07-28T14:16:42.709-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T14:16:22.952-07:00">
    <VendorCredit domain="QBO" sparse="false">
        <Id>255</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T14:13:30-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T14:13:30-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-12-23</TxnDate>
        <Line>
            <Id>1</Id>
            <Amount>90.00</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
                <AccountRef name="Bank Charges">8</AccountRef>
                <BillableStatus>Billable</BillableStatus>
                <TaxCodeRef>TAX</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <VendorRef name="Books by Bessie">30</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>90.00</TotalAmt>
    </VendorCredit>
</IntuitResponse>
```

## Full update a vendorcredit

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/vendorcredit`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing vendorcredit object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `vendorcreditrequest`

<details>
<summary>Show schema for `vendorcreditrequest`</summary>

#### vendorcreditrequest

Model type: `object`

##### `VendorRef`

Required: Required
Type: `ReferenceType`

The vendor reference for this transaction.

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

Individual line items of a transaction. Valid `Line` types include: `ItemBasedExpenseLine` and `AccountBasedExpenseLine`

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### itembasedexpenseline

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

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company. Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company

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
  "SyncToken": "1",
  "domain": "QBO",
  "VendorRef": {
    "name": "Books by Bessie",
    "value": "30"
  },
  "TxnDate": "2014-12-23",
  "TotalAmt": 140.0,
  "APAccountRef": {
    "name": "Accounts Payable (A/P)",
    "value": "33"
  },
  "sparse": false,
  "Line": [
    {
      "DetailType": "AccountBasedExpenseLineDetail",
      "Amount": 140.0,
      "ProjectRef": {
        "value": "39298045"
      },
      "Id": "1",
      "AccountBasedExpenseLineDetail": {
        "TaxCodeRef": {
          "value": "TAX"
        },
        "AccountRef": {
          "name": "Bank Charges",
          "value": "8"
        },
        "BillableStatus": "Billable",
        "CustomerRef": {
          "name": "Amy's Bird Sanctuary",
          "value": "1"
        }
      }
    }
  ],
  "Id": "255",
  "MetaData": {
    "CreateTime": "2015-07-28T14:13:30-07:00",
    "LastUpdatedTime": "2015-07-28T14:22:05-07:00"
  }
}
```

#### XML example

```xml
<VendorCredit xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
        <Id>255</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T14:13:30-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T14:13:30-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-12-23</TxnDate>
        <Line>
            <Id>1</Id>
            <Amount>120.00</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
                <AccountRef name="Bank Charges">8</AccountRef>
                <BillableStatus>Billable</BillableStatus>
                <TaxCodeRef>TAX</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <VendorRef name="Books by Bessie">30</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>120.00</TotalAmt>
</VendorCredit>
```

### Returns

The vendorcredit response body.

#### Example

```json
{
  "VendorCredit": {
    "SyncToken": "2",
    "domain": "QBO",
    "VendorRef": {
      "name": "Books by Bessie",
      "value": "30"
    },
    "TxnDate": "2014-12-23",
    "TotalAmt": 140.0,
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 140.0,
        "ProjectRef": {
          "value": "39298045"
        },
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "AccountRef": {
            "name": "Bank Charges",
            "value": "8"
          },
          "BillableStatus": "Billable",
          "CustomerRef": {
            "name": "Amy's Bird Sanctuary",
            "value": "1"
          }
        }
      }
    ],
    "Id": "255",
    "MetaData": {
      "CreateTime": "2015-07-28T14:13:30-07:00",
      "LastUpdatedTime": "2015-07-28T14:23:50-07:00"
    }
  },
  "time": "2015-07-28T14:23:52.196-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T14:22:06.635-07:00">
  <VendorCredit domain="QBO" sparse="false">
    <Id>255</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2015-07-28T14:13:30-07:00</CreateTime>
      <LastUpdatedTime>2015-07-28T14:22:05-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-12-23</TxnDate>
    <Line>
      <Id>1</Id>
      <Amount>120.00</Amount>
      <DetailType>AccountBasedExpenseLineDetail</DetailType>
      <AccountBasedExpenseLineDetail>
        <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
        <AccountRef name="Bank Charges">8</AccountRef>
        <BillableStatus>Billable</BillableStatus>
        <TaxCodeRef>TAX</TaxCodeRef>
      </AccountBasedExpenseLineDetail>
      <ProjectRef>39298045</ProjectRef>
    </Line>
    <VendorRef name="Books by Bessie">30</VendorRef>
    <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
    <TotalAmt>120.00</TotalAmt>
  </VendorCredit>
</IntuitResponse>
```
