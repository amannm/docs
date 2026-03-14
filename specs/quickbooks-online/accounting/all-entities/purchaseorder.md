# PurchaseOrder

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/purchaseorder
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / PurchaseOrder
> Canonical entity: `PurchaseOrder`

The PurchaseOrder object is a non-posting transaction representing a request to purchase goods or services from a third party.

## The purchaseorder object

### purchaseorderresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `APAccountRef`

Required: Required
Type: `ReferenceType`

Specifies to which AP account the bill is credited. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `APAccountRef.value` and `APAccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Liability` and `Account.AccountSubType` set to `AccountsPayable`.
If the company has a single AP account, the account is implied. However, it is recommended that the AP Account be explicitly specified in all cases to prevent unexpected errors when relating transactions to each other.

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
Locales: GB, AU, IN, CA

Method in which tax is applied. Allowed values are: `TaxExcluded`, `TaxInclusive`, and `NotApplicable`. Not applicable to US companies; required for non-US companies.

#### `TotalAmt`

Type: `BigDecimal`
Traits: read only, system defined

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `PurchaseOrder` was created from.

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

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: current server date

The date entered by the user when this transaction occurred. For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.
Sort order is ASC by default.

#### `CustomField `

Required: Optional
Type: `CustomField`

One of, up to three custom fields for the transaction. Available for custom fields so configured for the company. Check `Preferences.SalesFormsPrefs.CustomField` and `Preferences.VendorAndPurchasesPrefs.POCustomField` for custom fields currenly configured. [Click here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/create-custom-fields) to learn about managing custom fields.

<details>
<summary>Child attributes for `CustomField `</summary>

##### customfield

Model type: `object`

###### `DefinitionId`

Required: Required
Type: `String`
Traits: read only, system defined

Unique identifier of the CustomFieldDefinition that corresponds to this CustomField.

###### `Type`

Type: `CustomFieldTypeEnum`
Traits: read only

Data type of custom field. Only one type is currently supported: `StringType`.

###### `StringValue`

Required: Optional
Type: `String`

The value for the `StringType`custom field.

###### `Name`

Required: Optional
Type: `String`
Traits: read only

Name of the custom field.

</details>

#### `POEmail`

Required: Optional
Type: `EmailAddress`
Minor version: 17

Used to specify the vendor e-mail address where the purchase req is sent.

<details>
<summary>Child attributes for `POEmail`</summary>

##### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

</details>

#### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with the transaction. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerTxn` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

#### `SalesTermRef`

Required: Optional
Type: `ReferenceType`

Reference to the sales term associated with the transaction. Query the Term name list resource to determine the appropriate Term object for this reference. Use `Term.Id` and `Term.Name` from that object for `SalesTermRef.value` and `SalesTermRef.name`, respectively.

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

Zero or more Bill objects linked to this purchase order; `LinkedTxn.TxnType` is set to `Bill`. To retrieve details of a linked Bill transaction, issue a separate request to read the Bill whose ID is `linkedTxn.TxnId`.

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

#### `Memo`

Required: Optional
Type: `String`
Max length: Max of 4000 chars

A message for the vendor. This text appears on the Purchase Order object sent to the vendor.

#### `POStatus`

Required: Optional
Type: `String`

Purchase order status. Valid values are: `Open` and `Closed`.

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
Max length: Maximum of 21 chars

Reference number for the transaction. If not explicitly provided at create time, this field is populated based on the setting of `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` as follows:

If `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` is true a custom value can be provided. If no value is supplied, the resulting DocNumber is null.

If `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` is false, resulting DocNumber is system generated by incrementing the last number by 1.

Throws an error when duplicate DocNumber is sent in the request. Recommended best practice: check the setting of `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` before setting DocNumber. If a duplicate DocNumber needs to be supplied, add the query parameter name/value pair, `include=allowduplicatedocnum` to the URI. Sort order is ASC by default.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: Max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the purchase order to the vendor. This field maps to the Memo field on the Purchase Order form.

#### `ShipMethodRef`

Required: Optional
Type: `ReferenceType`

Reference to the user-defined ShipMethod associated with the transaction. Store shipping method string in both `ShipMethodRef.value` and `ShipMethodRef.name`.

<details>
<summary>Child attributes for `ShipMethodRef`</summary>

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

#### `ShipTo`

Required: Optional
Type: `ReferenceType`

Reference to the customer to whose shipping address the order will be shipped to.

<details>
<summary>Child attributes for `ShipTo`</summary>

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

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

#### `ShipAddr`

Required: Optional
Type: `PhysicalAddress`

Address to which the vendor shipped or will ship any goods associated with the purchase.
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

#### `VendorAddr`

Required: Optional
Type: `PhysicalAddress`

Address to which the payment should be sent.
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
<summary>Child attributes for `VendorAddr`</summary>

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

#### `EmailStatus`

Required: Optional
Type: `String`
Default: <span class="literal">NotSet</span>
Minor version: 45

Email status of the purchase order. Valid values: `NotSet`, `NeedToSend`, `EmailSent`

#### Example

```json
{
  "PurchaseOrder": {
    "DocNumber": "1005",
    "SyncToken": "0",
    "POEmail": {
      "Address": "send_email@intuit.com"
    },
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "TxnDate": "2015-07-28",
    "TotalAmt": 25.0,
    "ShipAddr": {
      "Line4": "Half Moon Bay, CA  94213",
      "Line3": "65 Ocean Dr.",
      "Id": "121",
      "Line1": "Grace Pariente",
      "Line2": "Cool Cars"
    },
    "domain": "QBO",
    "Id": "257",
    "POStatus": "Open",
    "sparse": false,
    "EmailStatus": "NotSet",
    "VendorRef": {
      "name": "Hicks Hardware",
      "value": "41"
    },
    "Line": [
      {
        "DetailType": "ItemBasedExpenseLineDetail",
        "Amount": 25.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "Id": "1",
        "ItemBasedExpenseLineDetail": {
          "ItemRef": {
            "name": "Garden Supplies",
            "value": "38"
          },
          "CustomerRef": {
            "name": "Cool Cars",
            "value": "3"
          },
          "Qty": 1,
          "TaxCodeRef": {
            "value": "NON"
          },
          "BillableStatus": "NotBillable",
          "UnitPrice": 25
        }
      }
    ],
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      },
      {
        "DefinitionId": "2",
        "Type": "StringType",
        "Name": "Sales Rep"
      }
    ],
    "VendorAddr": {
      "Line4": "Middlefield, CA  94303",
      "Line3": "42 Main St.",
      "Id": "120",
      "Line1": "Geoff Hicks",
      "Line2": "Hicks Hardware"
    },
    "MetaData": {
      "CreateTime": "2015-07-28T16:01:47-07:00",
      "LastUpdatedTime": "2015-07-28T16:01:47-07:00"
    }
  },
  "time": "2015-07-28T16:04:49.874-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T16:10:33.693-07:00">
    <PurchaseOrder domain="QBO" sparse="false">
        <Id>257</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T16:01:47-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T16:01:47-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <CustomField>
            <DefinitionId>2</DefinitionId>
            <Name>Sales Rep</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1005</DocNumber>
        <TxnDate>2015-07-28</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <Line>
            <Id>1</Id>
            <Amount>25.00</Amount>
            <DetailType>ItemBasedExpenseLineDetail</DetailType>
            <ItemBasedExpenseLineDetail>
                <ItemRef name="Garden Supplies">38</ItemRef>
                <UnitPrice>25</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
                <CustomerRef name="Cool Cars">3</CustomerRef>
                <BillableStatus>NotBillable</BillableStatus>
            </ItemBasedExpenseLineDetail>
            <ProjectRef>39298034</ProjectRef>
        </Line>
        <VendorRef name="Hicks Hardware">41</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>25.00</TotalAmt>
        <VendorAddr>
            <Id>120</Id>
            <Line1>Geoff Hicks</Line1>
            <Line2>Hicks Hardware</Line2>
            <Line3>42 Main St.</Line3>
            <Line4>Middlefield, CA 94303</Line4>
        </VendorAddr>
        <ShipAddr>
            <Id>121</Id>
            <Line1>Grace Pariente</Line1>
            <Line2>Cool Cars</Line2>
            <Line3>65 Ocean Dr.</Line3>
            <Line4>Half Moon Bay, CA 94213</Line4>
        </ShipAddr>
        <POStatus>Open</POStatus>
    </PurchaseOrder>
</IntuitResponse>
```

## Create a purchase order

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/purchaseorder`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create an purchaseorder are listed here.

Schema: `purchaseorderrequest`

<details>
<summary>Show schema for `purchaseorderrequest`</summary>

#### purchaseorderrequest

Model type: `object`

##### `APAccountRef`

Required: Required
Type: `ReferenceType`

Specifies which AP account to which the bill is credited. Many/most small businesses have a single AP account, so the account can be implied. When specified, the account must be a Liability account, and further, the sub-type must be of type Payables. We strongly recommend that the AP Account be explicitly specified in all cases as companies that have more then one AP account will encounter unexpected errors when relating transactions to each other.

<details>
<summary>Child attributes for `APAccountRef`</summary>

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

Individual line items of a transaction. Valid `Line` types include: Item line. Note: The ItemRef in the ItemBasedExpenseLine below must reference an Item in QBO that has an expense account linked to it (e.g. in the ExpenseAccountRef field of the Item). Otherwise the request fails in QBO with a 'You must select an account for this transaction.' error.

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

</details>

##### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company

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
  "TotalAmt": 25.0,
  "Line": [
    {
      "DetailType": "ItemBasedExpenseLineDetail",
      "Amount": 25.0,
      "ProjectRef": {
        "value": "39298034"
      },
      "Id": "1",
      "ItemBasedExpenseLineDetail": {
        "ItemRef": {
          "name": "Pump",
          "value": "11"
        },
        "CustomerRef": {
          "name": "Cool Cars",
          "value": "3"
        },
        "Qty": 1,
        "TaxCodeRef": {
          "value": "NON"
        },
        "BillableStatus": "NotBillable",
        "UnitPrice": 25
      }
    }
  ],
  "APAccountRef": {
    "name": "Accounts Payable (A/P)",
    "value": "33"
  },
  "VendorRef": {
    "name": "Hicks Hardware",
    "value": "41"
  },
  "ShipTo": {
    "name": "Jeff's Jalopies",
    "value": "12"
  }
}
```

#### XML example

```xml
<PurchaseOrder xmlns="http://schema.intuit.com/finance/v3">
    <Line>
        <Id>1</Id>
        <Amount>25.00</Amount>
        <DetailType>ItemBasedExpenseLineDetail</DetailType>
        <ItemBasedExpenseLineDetail>
            <ItemRef name="Garden Supplies">38</ItemRef>
            <UnitPrice>25</UnitPrice>
            <Qty>1</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
            <CustomerRef name="Cool Cars">3</CustomerRef>
            <BillableStatus>NotBillable</BillableStatus>
        </ItemBasedExpenseLineDetail>
        <ProjectRef>39298034</ProjectRef>
    </Line>
    <VendorRef name="Hicks Hardware">41</VendorRef>
    <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
    <TotalAmt>25.00</TotalAmt>
</PurchaseOrder>
```

### Returns

#### Example

```json
{
  "PurchaseOrder": {
    "DocNumber": "1007",
    "SyncToken": "0",
    "domain": "QBO",
    "VendorRef": {
      "name": "Hicks Hardware",
      "value": "41"
    },
    "TxnDate": "2015-07-28",
    "TotalAmt": 25.0,
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "EmailStatus": "NotSet",
    "sparse": false,
    "Line": [
      {
        "DetailType": "ItemBasedExpenseLineDetail",
        "Amount": 25.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "Id": "1",
        "ItemBasedExpenseLineDetail": {
          "ItemRef": {
            "name": "Pump",
            "value": "11"
          },
          "CustomerRef": {
            "name": "Cool Cars",
            "value": "3"
          },
          "Qty": 1,
          "TaxCodeRef": {
            "value": "NON"
          },
          "BillableStatus": "NotBillable",
          "UnitPrice": 25
        }
      }
    ],
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      },
      {
        "DefinitionId": "2",
        "Type": "StringType",
        "Name": "Sales Rep"
      }
    ],
    "Id": "259",
    "MetaData": {
      "CreateTime": "2015-07-28T16:06:03-07:00",
      "LastUpdatedTime": "2015-07-28T16:06:03-07:00"
    }
  },
  "time": "2015-07-28T16:06:04.864-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T16:03:19.756-07:00">
    <PurchaseOrder domain="QBO" sparse="false">
        <Id>258</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T16:03:18-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T16:03:18-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <CustomField>
            <DefinitionId>2</DefinitionId>
            <Name>Sales Rep</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1006</DocNumber>
        <TxnDate>2015-07-28</TxnDate>
        <Line>
            <Id>1</Id>
            <Amount>25.00</Amount>
            <DetailType>ItemBasedExpenseLineDetail</DetailType>
            <ItemBasedExpenseLineDetail>
                <ItemRef name="Garden Supplies">38</ItemRef>
                <UnitPrice>25</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
                <CustomerRef name="Cool Cars">3</CustomerRef>
                <BillableStatus>NotBillable</BillableStatus>
            </ItemBasedExpenseLineDetail>
            <ProjectRef>39298034</ProjectRef>
        </Line>
        <VendorRef name="Hicks Hardware">41</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>25.00</TotalAmt>
    </PurchaseOrder>
</IntuitResponse>
```

## Delete a purchase order

### Definition

- **Operation:** `POST /v3/company/<realmID>/purchaseorder?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the purchaseorder object specified in the request body. Include a minimum of `PurchaseOrder.Id` and `PurchaseOrder.SyncToken` in the request body. You must unlink any linked transactions associated with the purchaseorder object before deleting it.

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
  "Id": "125"
}
```

#### XML example

```xml
<PurchaseOrder xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>114</Id>
    <SyncToken>0</SyncToken>
</PurchaseOrder>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "PurchaseOrder": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "125"
  },
  "time": "2015-05-26T14:08:39.858-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-05-26T14:10:17.544-07:00">
    <PurchaseOrder domain="QBO" status="Deleted">
        <Id>114</Id>
    </PurchaseOrder>
</IntuitResponse>
```

## Get a purchase order as PDF

### Definition

- **Content type:** `application/pdf`
- **Operation:** `GET /v3/company/<realmID>/purchaseorder/<purchaseorderId>/pdf`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Returns

This resource returns the specified object in the response body as an Adobe Portable Document Format (PDF) file. The resulting PDF file is formatted according to custom form styles in the company settings.

## Query a purchase order

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from PurchaseOrder where Id = '259'"
```

#### XML example

```sql
select * from PurchaseOrder where Id = '259'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 1,
    "PurchaseOrder": [
      {
        "DocNumber": "1007",
        "SyncToken": "0",
        "domain": "QBO",
        "VendorRef": {
          "name": "Hicks Hardware",
          "value": "41"
        },
        "TxnDate": "2015-07-28",
        "TotalAmt": 25.0,
        "APAccountRef": {
          "name": "Accounts Payable (A/P)",
          "value": "33"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "ItemBasedExpenseLineDetail",
            "Amount": 25.0,
            "ProjectRef": {
              "value": "39298034"
            },
            "Id": "1",
            "ItemBasedExpenseLineDetail": {
              "ItemRef": {
                "name": "Garden Supplies",
                "value": "38"
              },
              "CustomerRef": {
                "name": "Cool Cars",
                "value": "3"
              },
              "Qty": 1,
              "TaxCodeRef": {
                "value": "NON"
              },
              "BillableStatus": "NotBillable",
              "UnitPrice": 25
            }
          }
        ],
        "CustomField": [
          {
            "DefinitionId": "1",
            "Type": "StringType",
            "Name": "Crew #"
          },
          {
            "DefinitionId": "2",
            "Type": "StringType",
            "Name": "Sales Rep"
          }
        ],
        "Id": "259",
        "MetaData": {
          "CreateTime": "2015-07-28T16:06:03-07:00",
          "LastUpdatedTime": "2015-07-28T16:06:03-07:00"
        }
      }
    ],
    "maxResults": 1
  },
  "time": "2015-07-28T16:09:26.277-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T16:08:50.873-07:00">
    <QueryResponse startPosition="1" maxResults="1" totalCount="1">
        <PurchaseOrder domain="QBO" sparse="false">
            <Id>259</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-07-28T16:06:03-07:00</CreateTime>
                <LastUpdatedTime>2015-07-28T16:06:03-07:00</LastUpdatedTime>
            </MetaData>
            <CustomField>
                <DefinitionId>1</DefinitionId>
                <Name>Crew #</Name>
                <Type>StringType</Type>
            </CustomField>
            <CustomField>
                <DefinitionId>2</DefinitionId>
                <Name>Sales Rep</Name>
                <Type>StringType</Type>
            </CustomField>
            <DocNumber>1007</DocNumber>
            <TxnDate>2015-07-28</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>25.00</Amount>
                <DetailType>ItemBasedExpenseLineDetail</DetailType>
                <ItemBasedExpenseLineDetail>
                    <ItemRef name="Garden Supplies">38</ItemRef>
                    <UnitPrice>25</UnitPrice>
                    <Qty>1</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                    <CustomerRef name="Cool Cars">3</CustomerRef>
                    <BillableStatus>NotBillable</BillableStatus>
                </ItemBasedExpenseLineDetail>
                <ProjectRef>39298034</ProjectRef>
            </Line>
            <VendorRef name="Hicks Hardware">41</VendorRef>
            <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
            <TotalAmt>25.00</TotalAmt>
        </PurchaseOrder>
    </QueryResponse>
</IntuitResponse>
```

## Read a purchase order

### Definition

- **Operation:** `GET /v3/company/<realmID>/purchaseorder/<purchaseorderId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a purchase order that has been previously created.

### Returns

The purchaseorder response body.

#### Example

```json
{
  "PurchaseOrder": {
    "DocNumber": "1005",
    "SyncToken": "0",
    "POEmail": {
      "Address": "send_email@intuit.com"
    },
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "TxnDate": "2015-07-28",
    "TotalAmt": 25.0,
    "ShipAddr": {
      "Line4": "Half Moon Bay, CA  94213",
      "Line3": "65 Ocean Dr.",
      "Id": "121",
      "Line1": "Grace Pariente",
      "Line2": "Cool Cars"
    },
    "domain": "QBO",
    "Id": "257",
    "POStatus": "Open",
    "sparse": false,
    "EmailStatus": "NotSet",
    "VendorRef": {
      "name": "Hicks Hardware",
      "value": "41"
    },
    "Line": [
      {
        "DetailType": "ItemBasedExpenseLineDetail",
        "Amount": 25.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "Id": "1",
        "ItemBasedExpenseLineDetail": {
          "ItemRef": {
            "name": "Garden Supplies",
            "value": "38"
          },
          "CustomerRef": {
            "name": "Cool Cars",
            "value": "3"
          },
          "Qty": 1,
          "TaxCodeRef": {
            "value": "NON"
          },
          "BillableStatus": "NotBillable",
          "UnitPrice": 25
        }
      }
    ],
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      },
      {
        "DefinitionId": "2",
        "Type": "StringType",
        "Name": "Sales Rep"
      }
    ],
    "VendorAddr": {
      "Line4": "Middlefield, CA  94303",
      "Line3": "42 Main St.",
      "Id": "120",
      "Line1": "Geoff Hicks",
      "Line2": "Hicks Hardware"
    },
    "MetaData": {
      "CreateTime": "2015-07-28T16:01:47-07:00",
      "LastUpdatedTime": "2015-07-28T16:01:47-07:00"
    }
  },
  "time": "2015-07-28T16:04:49.874-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T16:10:33.693-07:00">
    <PurchaseOrder domain="QBO" sparse="false">
        <Id>257</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T16:01:47-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T16:01:47-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <CustomField>
            <DefinitionId>2</DefinitionId>
            <Name>Sales Rep</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1005</DocNumber>
        <TxnDate>2015-07-28</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <Line>
            <Id>1</Id>
            <Amount>25.00</Amount>
            <DetailType>ItemBasedExpenseLineDetail</DetailType>
            <ItemBasedExpenseLineDetail>
                <ItemRef name="Garden Supplies">38</ItemRef>
                <UnitPrice>25</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
                <CustomerRef name="Cool Cars">3</CustomerRef>
                <BillableStatus>NotBillable</BillableStatus>
            </ItemBasedExpenseLineDetail>
            <ProjectRef>39298034</ProjectRef>
        </Line>
        <VendorRef name="Hicks Hardware">41</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>25.00</TotalAmt>
        <VendorAddr>
            <Id>120</Id>
            <Line1>Geoff Hicks</Line1>
            <Line2>Hicks Hardware</Line2>
            <Line3>42 Main St.</Line3>
            <Line4>Middlefield, CA 94303</Line4>
        </VendorAddr>
        <ShipAddr>
            <Id>121</Id>
            <Line1>Grace Pariente</Line1>
            <Line2>Cool Cars</Line2>
            <Line3>65 Ocean Dr.</Line3>
            <Line4>Half Moon Bay, CA 94213</Line4>
        </ShipAddr>
        <POStatus>Open</POStatus>
    </PurchaseOrder>
</IntuitResponse>
```

## Send a purchase order

### Definition

- **Content type:** `application/octet-stream`
- **Operation:** `POST (Using email address supplied in PurchaseOrder.POEmail.Address) /v3/company/<realmID>/purchaseorder/<purchaseorderId>/send
POST(Specifying an explicit email address) /v3/company/<realmID>/purchaseorder/<purchaseorderId>/send?sendTo=<emailAddr>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- The `PurchaseOrder.EmailStatus` parameter is set to `EmailSent`
- The `PurchaseOrder.POEmail.Address` parameter is updated to the address specified with the value of the `sendTo` query parameter, if specified and if the request's minor version is 17 and above.

### Returns

The PurchaseOrder response body.

#### Example

```json
{
  "PurchaseOrder": {
    "DocNumber": "1005",
    "SyncToken": "0",
    "POEmail": {
      "Address": "send_email@intuit.com"
    },
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "TxnDate": "2015-07-28",
    "TotalAmt": 25.0,
    "ShipAddr": {
      "Line4": "Half Moon Bay, CA  94213",
      "Line3": "65 Ocean Dr.",
      "Id": "121",
      "Line1": "Grace Pariente",
      "Line2": "Cool Cars"
    },
    "domain": "QBO",
    "Id": "257",
    "POStatus": "Open",
    "sparse": false,
    "EmailStatus": "EmailSent",
    "VendorRef": {
      "name": "Hicks Hardware",
      "value": "41"
    },
    "Line": [
      {
        "DetailType": "ItemBasedExpenseLineDetail",
        "Amount": 25.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "Id": "1",
        "ItemBasedExpenseLineDetail": {
          "ItemRef": {
            "name": "Garden Supplies",
            "value": "38"
          },
          "CustomerRef": {
            "name": "Cool Cars",
            "value": "3"
          },
          "Qty": 1,
          "TaxCodeRef": {
            "value": "NON"
          },
          "BillableStatus": "NotBillable",
          "UnitPrice": 25
        }
      }
    ],
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      },
      {
        "DefinitionId": "2",
        "Type": "StringType",
        "Name": "Sales Rep"
      }
    ],
    "VendorAddr": {
      "Line4": "Middlefield, CA  94303",
      "Line3": "42 Main St.",
      "Id": "120",
      "Line1": "Geoff Hicks",
      "Line2": "Hicks Hardware"
    },
    "MetaData": {
      "CreateTime": "2015-07-28T16:01:47-07:00",
      "LastUpdatedTime": "2019-09-19T10:43:46-07:00"
    }
  },
  "time": "2019-09-19T10:43:46-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T16:10:33.693-07:00">
    <PurchaseOrder domain="QBO" sparse="false">
        <Id>257</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T16:01:47-07:00</CreateTime>
            <LastUpdatedTime>2019-09-19T10:43:46-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <CustomField>
            <DefinitionId>2</DefinitionId>
            <Name>Sales Rep</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1005</DocNumber>
        <TxnDate>2015-07-28</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <Line>
            <Id>1</Id>
            <Amount>25.00</Amount>
            <DetailType>ItemBasedExpenseLineDetail</DetailType>
            <ItemBasedExpenseLineDetail>
                <ItemRef name="Garden Supplies">38</ItemRef>
                <UnitPrice>25</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
                <CustomerRef name="Cool Cars">3</CustomerRef>
                <BillableStatus>NotBillable</BillableStatus>
            </ItemBasedExpenseLineDetail>
            <ProjectRef>39298034</ProjectRef>
        </Line>
        <VendorRef name="Hicks Hardware">41</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>25.00</TotalAmt>
        <VendorAddr>
            <Id>120</Id>
            <Line1>Geoff Hicks</Line1>
            <Line2>Hicks Hardware</Line2>
            <Line3>42 Main St.</Line3>
            <Line4>Middlefield, CA 94303</Line4>
        </VendorAddr>
        <ShipAddr>
            <Id>121</Id>
            <Line1>Grace Pariente</Line1>
            <Line2>Cool Cars</Line2>
            <Line3>65 Ocean Dr.</Line3>
            <Line4>Half Moon Bay, CA 94213</Line4>
        </ShipAddr>
        <POStatus>Open</POStatus>
        <POEmail>
            <Address>send_email@intuit.com</Address>
        </POEmail>
    </PurchaseOrder>
</IntuitResponse>
```

## Full update a purchase order

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/purchaseorder`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing purchase order object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `purchaseorderresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "DocNumber": "1005",
  "SyncToken": "0",
  "POEmail": {
    "Address": "send_email@intuit.com"
  },
  "APAccountRef": {
    "name": "Accounts Payable (A/P)",
    "value": "33"
  },
  "CurrencyRef": {
    "name": "United States Dollar",
    "value": "USD"
  },
  "sparse": false,
  "TxnDate": "2015-07-28",
  "TotalAmt": 25.0,
  "ShipAddr": {
    "Line4": "Half Moon Bay, CA  94213",
    "Line3": "65 Ocean Dr.",
    "Id": "121",
    "Line1": "Grace Pariente",
    "Line2": "Cool Cars"
  },
  "PrivateNote": "This is a private note added during update.",
  "Id": "257",
  "POStatus": "Open",
  "domain": "QBO",
  "VendorRef": {
    "name": "Hicks Hardware",
    "value": "41"
  },
  "Line": [
    {
      "DetailType": "ItemBasedExpenseLineDetail",
      "Amount": 25.0,
      "ProjectRef": {
        "value": "39298034"
      },
      "Id": "1",
      "ItemBasedExpenseLineDetail": {
        "ItemRef": {
          "name": "Garden Supplies",
          "value": "38"
        },
        "CustomerRef": {
          "name": "Cool Cars",
          "value": "3"
        },
        "Qty": 1,
        "TaxCodeRef": {
          "value": "NON"
        },
        "BillableStatus": "NotBillable",
        "UnitPrice": 25
      }
    }
  ],
  "CustomField": [
    {
      "DefinitionId": "1",
      "Type": "StringType",
      "Name": "Crew #"
    },
    {
      "DefinitionId": "2",
      "Type": "StringType",
      "Name": "Sales Rep"
    }
  ],
  "VendorAddr": {
    "Line4": "Middlefield, CA  94303",
    "Line3": "42 Main St.",
    "Id": "120",
    "Line1": "Geoff Hicks",
    "Line2": "Hicks Hardware"
  },
  "MetaData": {
    "CreateTime": "2015-07-28T16:01:47-07:00",
    "LastUpdatedTime": "2015-07-28T16:01:47-07:00"
  }
}
```

#### XML example

```xml
<PurchaseOrder xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>257</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
        <CreateTime>2015-07-28T16:01:47-07:00</CreateTime>
        <LastUpdatedTime>2015-07-28T16:01:47-07:00</LastUpdatedTime>
    </MetaData>
    <CustomField>
        <DefinitionId>1</DefinitionId>
        <Name>Crew #</Name>
        <Type>StringType</Type>
    </CustomField>
    <CustomField>
        <DefinitionId>2</DefinitionId>
        <Name>Sales Rep</Name>
        <Type>StringType</Type>
    </CustomField>
    <DocNumber>1005</DocNumber>
    <TxnDate>2015-07-28</TxnDate>
    <CurrencyRef name="United States Dollar">USD</CurrencyRef>
    <Line>
        <Id>1</Id>
        <Amount>25.00</Amount>
        <DetailType>ItemBasedExpenseLineDetail</DetailType>
        <ItemBasedExpenseLineDetail>
            <ItemRef name="Garden Supplies">38</ItemRef>
            <UnitPrice>25</UnitPrice>
            <Qty>1</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
            <CustomerRef name="Cool Cars">3</CustomerRef>
            <BillableStatus>NotBillable</BillableStatus>
        </ItemBasedExpenseLineDetail>
        <ProjectRef>39298034</ProjectRef>
    </Line>
    <VendorRef name="Hicks Hardware">41</VendorRef>
    <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
    <TotalAmt>25.00</TotalAmt>
    <VendorAddr>
        <Id>120</Id>
        <Line1>Geoff Hicks</Line1>
        <Line2>Hicks Hardware</Line2>
        <Line3>42 Main St.</Line3>
        <Line4>Middlefield, CA 94303</Line4>
    </VendorAddr>
    <ShipAddr>
        <Id>121</Id>
        <Line1>Grace Pariente</Line1>
        <Line2>Cool Cars</Line2>
        <Line3>65 Ocean Dr.</Line3>
        <Line4>Half Moon Bay, CA 94213</Line4>
    </ShipAddr>
    <POStatus>Open</POStatus>
    <PrivateNote>This is another private note.</PrivateNote>
</PurchaseOrder>
```

### Returns

The purchaseorder response body.

#### Example

```json
{
  "PurchaseOrder": {
    "DocNumber": "1005",
    "SyncToken": "1",
    "domain": "QBO",
    "APAccountRef": {
      "name": "Accounts Payable (A/P)",
      "value": "33"
    },
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "TxnDate": "2015-07-28",
    "TotalAmt": 25.0,
    "ShipAddr": {
      "Line4": "Half Moon Bay, CA  94213",
      "Line3": "65 Ocean Dr.",
      "Id": "121",
      "Line1": "Grace Pariente",
      "Line2": "Cool Cars"
    },
    "PrivateNote": "This is a private note added during update.",
    "VendorAddr": {
      "Line4": "Middlefield, CA  94303",
      "Line3": "42 Main St.",
      "Id": "120",
      "Line1": "Geoff Hicks",
      "Line2": "Hicks Hardware"
    },
    "POStatus": "Open",
    "sparse": false,
    "VendorRef": {
      "name": "Hicks Hardware",
      "value": "41"
    },
    "Line": [
      {
        "DetailType": "ItemBasedExpenseLineDetail",
        "Amount": 25.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "Id": "1",
        "ItemBasedExpenseLineDetail": {
          "ItemRef": {
            "name": "Garden Supplies",
            "value": "38"
          },
          "CustomerRef": {
            "name": "Cool Cars",
            "value": "3"
          },
          "Qty": 1,
          "TaxCodeRef": {
            "value": "NON"
          },
          "BillableStatus": "NotBillable",
          "UnitPrice": 25
        }
      }
    ],
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      },
      {
        "DefinitionId": "2",
        "Type": "StringType",
        "Name": "Sales Rep"
      }
    ],
    "Id": "257",
    "MetaData": {
      "CreateTime": "2015-07-28T16:01:47-07:00",
      "LastUpdatedTime": "2015-07-28T16:17:41-07:00"
    }
  },
  "time": "2015-07-28T16:17:42.952-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-28T16:19:46.916-07:00">
    <PurchaseOrder domain="QBO" sparse="false">
        <Id>257</Id>
        <SyncToken>2</SyncToken>
        <MetaData>
            <CreateTime>2015-07-28T16:01:47-07:00</CreateTime>
            <LastUpdatedTime>2015-07-28T16:19:45-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <CustomField>
            <DefinitionId>2</DefinitionId>
            <Name>Sales Rep</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1005</DocNumber>
        <TxnDate>2015-07-28</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <PrivateNote>This is another private note.</PrivateNote>
        <Line>
            <Id>1</Id>
            <Amount>25.00</Amount>
            <DetailType>ItemBasedExpenseLineDetail</DetailType>
            <ItemBasedExpenseLineDetail>
                <ItemRef name="Garden Supplies">38</ItemRef>
                <UnitPrice>25</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
                <CustomerRef name="Cool Cars">3</CustomerRef>
                <BillableStatus>NotBillable</BillableStatus>
            </ItemBasedExpenseLineDetail>
            <ProjectRef>39298034</ProjectRef>
        </Line>
        <VendorRef name="Hicks Hardware">41</VendorRef>
        <APAccountRef name="Accounts Payable (A/P)">33</APAccountRef>
        <TotalAmt>25.00</TotalAmt>
        <VendorAddr>
            <Id>120</Id>
            <Line1>Geoff Hicks</Line1>
            <Line2>Hicks Hardware</Line2>
            <Line3>42 Main St.</Line3>
            <Line4>Middlefield, CA 94303</Line4>
        </VendorAddr>
        <ShipAddr>
            <Id>121</Id>
            <Line1>Grace Pariente</Line1>
            <Line2>Cool Cars</Line2>
            <Line3>65 Ocean Dr.</Line3>
            <Line4>Half Moon Bay, CA 94213</Line4>
        </ShipAddr>
        <POStatus>Open</POStatus>
    </PurchaseOrder>
</IntuitResponse>
```
