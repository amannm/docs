# Purchase

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/purchase
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Purchase
> Canonical entity: `Purchase`

A Purchase object represents an expense, such as a purchase made from a vendor. Of note,

- You must specify an `AccountRef` for all purchases.
- The `TotalAmt`attribute must add up to sum of `Line.Amount` attributes.

There are three types of purchases: Cash, Check, and Credit Card.

- Cash Purchase contains information regarding a payment made in cash.
- Check Purchase contains information regarding a payment made by check.
- Credit Card Purchase contains information regarding a payment made by credit card or refunded/credited back to a credit card.

For example, to create a transaction that sends a check to a vendor, create a Purchase object with `PaymentType` set to `Check`.

## The purchase object

### purchaseresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of a transaction. Valid `Line` types include `ItemBasedExpenseLine` (Available if `Preferences.ProductAndServicesPrefs.ForPurchase` is set to `true`) and `AccountBasedExpenseLine`

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

#### `PaymentType`

Required: Required
Type: `String`

Type can be `Cash`, `Check`, or `CreditCard`.

#### `AccountRef`

Required: Required
Type: `ReferenceType`

Specifies the account reference to which this purchase is applied based on the `PaymentType`. A type of `Check` should have bank account, `CreditCard` should specify credit card account, etc. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively.

<details>
<summary>Child attributes for `AccountRef`</summary>

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

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Required if multicurrency is enabled for the company.

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

#### `TotalAmt`

Type: `BigDecimal`
Traits: read only, system defined

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `Purchase` was created from.

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

#### `PrintStatus`

Required: Optional
Type: `String`
Default: <span class="literal">NeedToPrint</span>

PrintStatus is applicable only for `Check`. Ignored for `CreditCard`charge or refund. Valid values: `NotSet`, `NeedToPrint`, `PrintComplete.`

#### `RemitToAddr`

Required: Optional
Type: `PhysicalAddress`
Traits: read only

Address to which the payment should be sent. This attribute is applicable only for `Check`. Ignored for `CreditCard` charge or refund.
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
<summary>Child attributes for `RemitToAddr`</summary>

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

#### `TxnSource`

Required: Optional
Type: `String`

Used internally to specify originating source of a credit card transaction.

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

#### `GlobalTaxCalculation`

Required: Optional
Type: `GlobalTaxCalculationEnum`
Default: <span class="literal">TaxExcluded</span>
Locales: GB, AU, IN, CA

Method in which tax is applied. Allowed values are: `TaxExcluded`, `TaxInclusive`, and `NotApplicable`.

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

If `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` is true a custom value can be provided; duplicate values are not accepted. If no value is supplied, the resulting DocNumber is null.

If `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` is false, resulting DocNumber is system generated by incrementing the last number by 1.

For Cash/CreditCard transactions, throws an error when duplicate DocNumber is sent in the request. For Check transactions, error is thrown when duplicate DocNumber is sent in the request and `Preferences:OtherPrefs:NameValue.Name = WarnDuplicateCheckNumber` is true. Recommended best practice: check the setting of `Preferences:OtherPrefs:NameValue.Name = VendorAndPurchasesPrefs.UseCustomTxnNumbers` before setting DocNumber. If a duplicate DocNumber needs to be supplied, add the query parameter name/value pair, `include=allowduplicatedocnum` to the URI. Sort order is ASC by default.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: Max of 4000 chars

User-entered, organization-private note about the transaction. This field maps to the Memo field on the Expense form in the QuickBooks UI.

#### `Credit`

Required: Optional
Type: `Boolean`
Default: False

`False`—it represents a charge. `True`—it represents a refund. Valid only for `CreditCard`payment type. Validation Rules: Valid only for `CreditCard`transactions.

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

#### `PaymentMethodRef`

Required: Optional
Type: `ReferenceType`

Reference to a PaymentMethod associated with this transaction. Query the PaymentMethod name list resource to determine the appropriate PaymentMethod object for this reference. Use `PaymentMethod.Id` and `PaymentMethod.Name` from that object for `PaymentMethodRef.value` and `PaymentMethodRef.name`, respectively.

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

#### `PurchaseEx`

Required: Optional
Type: `Internal use`

For internal use.

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company

#### `DepartmentRef`

Required: Optional
Type: `ReferenceType`

A reference to a Department object specifying the location of the transaction. Available if `Preferences.AccountingInfoPrefs.TrackDepartments` is set to `true`.
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

#### `EntityRef`

Required: Optional
Type: `ReferenceType,`

Specifies the party with whom an expense is associated. Can be `Customer`, `Vendor, or Employee.`
Query the corresponding name list resource of the associated type to determine the appropriate object for this reference. Use the `Id` and `DisplayName` values from that object for `EntityRef.value` and `EntityRef.name`, respectively. Set `EntityRef.type` to the type of object associated with this expense. For example, if this object represents a purchase from a vendor, then set `EntityRef.type` to `Vendor` and query the Vendor resource for the appropriate object to reference.

<details>
<summary>Child attributes for `EntityRef`</summary>

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
  "Purchase": {
    "SyncToken": "0",
    "domain": "QBO",
    "PurchaseEx": {
      "any": [
        {
          "name": "{http://schema.intuit.com/finance/v3}NameValue",
          "nil": false,
          "value": {
            "Name": "TxnType",
            "Value": "54"
          },
          "declaredType": "com.intuit.schema.finance.v3.NameValue",
          "scope": "javax.xml.bind.JAXBElement$GlobalScope",
          "globalScope": true,
          "typeSubstituted": false
        }
      ]
    },
    "TxnDate": "2015-07-27",
    "TotalAmt": 10.0,
    "PaymentType": "Cash",
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 10.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "AccountRef": {
            "name": "Meals and Entertainment",
            "value": "13"
          },
          "BillableStatus": "NotBillable"
        }
      }
    ],
    "AccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "CustomField": [],
    "Id": "252",
    "MetaData": {
      "CreateTime": "2015-07-27T10:37:26-07:00",
      "LastUpdatedTime": "2015-07-27T10:37:26-07:00"
    }
  },
  "time": "2015-07-27T10:39:33.171-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T10:39:51.538-07:00">
    <Purchase domain="QBO" sparse="false">
        <Id>252</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-27T10:37:26-07:00</CreateTime>
            <LastUpdatedTime>2015-07-27T10:37:26-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-07-27</TxnDate>
        <Line>
            <Id>1</Id>
            <Amount>10.00</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <AccountRef name="Meals and Entertainment">13</AccountRef>
                <BillableStatus>NotBillable</BillableStatus>
                <TaxCodeRef>NON</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <AccountRef name="Checking">35</AccountRef>
        <PaymentType>Cash</PaymentType>
        <TotalAmt>10.00</TotalAmt>
        <PurchaseEx>
            <NameValue>
                <Name>TxnType</Name>
                <Value>54</Value>
            </NameValue>
        </PurchaseEx>
    </Purchase>
</IntuitResponse>
```

## Create a purchase

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/purchase`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

You must specify an `AccountRef` for all purchases.

### Request Body

The minimum elements to create a Purchase object are listed here.

Schema: `purchaserequest`

<details>
<summary>Show schema for `purchaserequest`</summary>

#### purchaserequest

Model type: `object`

##### `PaymentType`

Required: Required
Type: `String`

Payment Type can be: `Cash`, `Check`, or `CreditCard`.

##### `AccountRef`

Required: Required
Type: `ReferenceType`

Specifies the account reference. Check must specify bank account, CreditCard must specify credit card account. Validation Rules:Valid and Active Account Reference of an appropriate type.

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

##### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of a transaction. Valid `Line`type for create: `AccountBasedExpenseLine`

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
  "PaymentType": "CreditCard",
  "AccountRef": {
    "name": "Visa",
    "value": "42"
  },
  "Line": [
    {
      "DetailType": "AccountBasedExpenseLineDetail",
      "Amount": 10.0,
      "AccountBasedExpenseLineDetail": {
        "AccountRef": {
          "name": "Meals and Entertainment",
          "value": "13"
        },
        "ProjectRef": {
          "value": "42991284"
        }
      }
    }
  ]
}
```

#### XML example

```xml
<Purchase xmlns="http://schema.intuit.com/finance/v3" sparse="false">
  <Line>
    <Amount>10.00</Amount>
    <DetailType>AccountBasedExpenseLineDetail</DetailType>
    <AccountBasedExpenseLineDetail>
      <AccountRef>79</AccountRef>
    </AccountBasedExpenseLineDetail>
    <ProjectRef>39298045</ProjectRef>
  </Line>
  <AccountRef name="QuickBooks Credit Card">126</AccountRef>
  <PaymentType>CreditCard</PaymentType>
</Purchase>
```

### Returns

The purchase response body.

#### Example

```json
{
  "Purchase": {
    "SyncToken": "0",
    "domain": "QBO",
    "PurchaseEx": {
      "any": [
        {
          "name": "{http://schema.intuit.com/finance/v3}NameValue",
          "nil": false,
          "value": {
            "Name": "TxnType",
            "Value": "54"
          },
          "declaredType": "com.intuit.schema.finance.v3.NameValue",
          "scope": "javax.xml.bind.JAXBElement$GlobalScope",
          "globalScope": true,
          "typeSubstituted": false
        }
      ]
    },
    "Credit": false,
    "TotalAmt": 10.0,
    "PaymentType": "CreditCard",
    "TxnDate": "2015-07-27",
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 10.0,
        "ProjectRef": {
          "value": "42991284"
        },
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "AccountRef": {
            "name": "Meals and Entertainment",
            "value": "13"
          },
          "BillableStatus": "NotBillable"
        }
      }
    ],
    "AccountRef": {
      "name": "Visa",
      "value": "42"
    },
    "CustomField": [],
    "Id": "247",
    "MetaData": {
      "CreateTime": "2015-07-27T10:27:01-07:00",
      "LastUpdatedTime": "2015-07-27T10:27:01-07:00"
    }
  },
  "time": "2015-07-27T10:27:01.593-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T10:32:49.668-07:00">
  <Purchase domain="QBO" sparse="false">
    <Id>248</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-07-27T10:32:49-07:00</CreateTime>
      <LastUpdatedTime>2015-07-27T10:32:49-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2015-07-27</TxnDate>
    <Line>
      <Id>1</Id>
      <Amount>10.00</Amount>
      <DetailType>AccountBasedExpenseLineDetail</DetailType>
      <AccountBasedExpenseLineDetail>
        <AccountRef name="Meals and Entertainment">13</AccountRef>
        <BillableStatus>NotBillable</BillableStatus>
        <TaxCodeRef>NON</TaxCodeRef>
      </AccountBasedExpenseLineDetail>
      <ProjectRef>39298045</ProjectRef>
    </Line>
    <AccountRef name="Visa">42</AccountRef>
    <PaymentType>CreditCard</PaymentType>
    <Credit>false</Credit>
    <TotalAmt>10.00</TotalAmt>
    <PurchaseEx>
      <NameValue>
        <Name>TxnType</Name>
        <Value>54</Value>
      </NameValue>
    </PurchaseEx>
  </Purchase>
</IntuitResponse>
```

## Delete a purchase

### Definition

- **Content type:** `application/json or application/xml`
- **Operation:** `POST /v3/company/<realmID>/purchase?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the Purchase object specified in the request body. Include a minimum of `Purchase.Id` and `Purchase.SyncToken` in the request body.

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
  "SyncToken": "2",
  "Id": "595"
}
```

#### XML example

```xml
<Purchase xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
  <Id>603</Id>
  <SyncToken>1</SyncToken>
</Purchase>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "Purchase": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "595"
  },
  "time": "2014-04-22T12:00:52.298-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-04-22T09:13:16.868-07:00">
  <Purchase domain="QBO" status="Deleted">
    <Id>603</Id>
  </Purchase>
</IntuitResponse>
```

## Query a purchase

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Purchase where TotalAmt < '100.00'"
```

#### XML example

```sql
select * from Purchase where TotalAmt < '100.00'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Purchase": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "PurchaseEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "TxnType",
                "Value": "11"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "Credit": true,
        "TotalAmt": 900.0,
        "PrivateNote": "Monthly Payment",
        "PaymentType": "CreditCard",
        "TxnDate": "2014-10-03",
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 900.0,
            "ProjectRef": {
              "value": "39298034"
            },
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "AccountRef": {
                "name": "Checking",
                "value": "35"
              },
              "BillableStatus": "NotBillable"
            }
          }
        ],
        "AccountRef": {
          "name": "Mastercard",
          "value": "41"
        },
        "Id": "139",
        "MetaData": {
          "CreateTime": "2014-10-03T14:35:37-07:00",
          "LastUpdatedTime": "2014-10-03T14:35:37-07:00"
        }
      },
      {
        "DocNumber": "70",
        "SyncToken": "0",
        "domain": "QBO",
        "PurchaseEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "TxnType",
                "Value": "3"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "TxnDate": "2014-09-11",
        "TotalAmt": 185.0,
        "PrintStatus": "NotSet",
        "PaymentType": "Check",
        "EntityRef": {
          "type": "Vendor",
          "name": "Chin's Gas and Oil",
          "value": "33"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 185.0,
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "AccountRef": {
                "name": "Maintenance and Repair",
                "value": "72"
              },
              "BillableStatus": "NotBillable"
            }
          }
        ],
        "AccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "Id": "133",
        "MetaData": {
          "CreateTime": "2014-10-03T14:17:55-07:00",
          "LastUpdatedTime": "2014-10-03T14:17:55-07:00"
        }
      },
      {
        "DocNumber": "75",
        "SyncToken": "0",
        "domain": "QBO",
        "PurchaseEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "TxnType",
                "Value": "3"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "TxnDate": "2014-09-19",
        "TotalAmt": 228.75,
        "Id": "115",
        "PrintStatus": "NotSet",
        "PaymentType": "Check",
        "EntityRef": {
          "type": "Vendor",
          "name": "Hicks Hardware",
          "value": "41"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "ItemBasedExpenseLineDetail",
            "Amount": 125.0,
            "Id": "1",
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
          },
          {
            "DetailType": "ItemBasedExpenseLineDetail",
            "Amount": 11.25,
            "Id": "2",
            "ItemBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "Qty": 15,
              "BillableStatus": "NotBillable",
              "UnitPrice": 0.75,
              "ItemRef": {
                "name": "Sprinkler Heads",
                "value": "16"
              }
            },
            "Description": "Sprinkler Heads"
          },
          {
            "DetailType": "ItemBasedExpenseLineDetail",
            "Amount": 62.5,
            "Id": "3",
            "ItemBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "Qty": 25,
              "BillableStatus": "NotBillable",
              "UnitPrice": 2.5,
              "ItemRef": {
                "name": "Sprinkler Pipes",
                "value": "17"
              }
            },
            "Description": "Sprinkler Pipes"
          },
          {
            "DetailType": "ItemBasedExpenseLineDetail",
            "Amount": 30.0,
            "Id": "4",
            "ItemBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "Qty": 3,
              "BillableStatus": "NotBillable",
              "UnitPrice": 10,
              "ItemRef": {
                "name": "Pump",
                "value": "11"
              }
            },
            "Description": "Fountain Pump"
          }
        ],
        "AccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "RemitToAddr": {
          "City": "Middlefield",
          "Line1": "42 Main St.",
          "PostalCode": "94303",
          "Lat": "37.445013",
          "Long": "-122.1391443",
          "CountrySubDivisionCode": "CA",
          "Id": "37"
        },
        "MetaData": {
          "CreateTime": "2014-09-19T12:51:46-07:00",
          "LastUpdatedTime": "2014-09-19T12:51:46-07:00"
        }
      },
      {
        "DocNumber": "12",
        "SyncToken": "0",
        "domain": "QBO",
        "PurchaseEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "TxnType",
                "Value": "54"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "TxnDate": "2014-07-09",
        "TotalAmt": 250.0,
        "PaymentType": "Cash",
        "EntityRef": {
          "type": "Vendor",
          "name": "Robertson & Associates",
          "value": "49"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 250.0,
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "AccountRef": {
                "name": "Legal & Professional Fees:Accounting",
                "value": "69"
              },
              "BillableStatus": "NotBillable"
            }
          }
        ],
        "AccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "Id": "107",
        "MetaData": {
          "CreateTime": "2014-09-19T12:36:23-07:00",
          "LastUpdatedTime": "2014-09-19T12:36:23-07:00"
        }
      },
      {
        "DocNumber": "15",
        "SyncToken": "1",
        "domain": "QBO",
        "PurchaseEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "TxnType",
                "Value": "54"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "TxnDate": "2014-08-16",
        "TotalAmt": 108.09,
        "PaymentType": "Cash",
        "EntityRef": {
          "type": "Vendor",
          "name": "Tania's Nursery",
          "value": "50"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 108.09,
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "AccountRef": {
                "name": "Job Expenses",
                "value": "58"
              },
              "BillableStatus": "NotBillable"
            }
          }
        ],
        "AccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "Id": "87",
        "MetaData": {
          "CreateTime": "2014-09-18T13:14:42-07:00",
          "LastUpdatedTime": "2014-09-18T13:17:06-07:00"
        }
      },
      {
        "DocNumber": "3",
        "SyncToken": "0",
        "domain": "QBO",
        "PurchaseEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "TxnType",
                "Value": "54"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "Credit": false,
        "TotalAmt": 158.08,
        "PaymentType": "CreditCard",
        "TxnDate": "2014-07-16",
        "EntityRef": {
          "type": "Vendor",
          "name": "Tania's Nursery",
          "value": "50"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 158.08,
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "AccountRef": {
                "name": "Job Expenses:Job Materials:Plants and Soil",
                "value": "66"
              },
              "BillableStatus": "NotBillable"
            }
          }
        ],
        "AccountRef": {
          "name": "Mastercard",
          "value": "41"
        },
        "Id": "85",
        "MetaData": {
          "CreateTime": "2014-09-18T13:12:01-07:00",
          "LastUpdatedTime": "2014-09-18T13:12:01-07:00"
        }
      },
      {
        "DocNumber": "13",
        "SyncToken": "0",
        "domain": "QBO",
        "PurchaseEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "TxnType",
                "Value": "54"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "TxnDate": "2014-09-13",
        "TotalAmt": 215.66,
        "PaymentType": "Cash",
        "EntityRef": {
          "type": "Vendor",
          "name": "Hicks Hardware",
          "value": "41"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 215.66,
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "AccountRef": {
                "name": "Job Expenses:Job Materials:Sprinklers and Drip Systems",
                "value": "67"
              },
              "BillableStatus": "NotBillable"
            }
          }
        ],
        "AccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "Id": "83",
        "MetaData": {
          "CreateTime": "2014-09-18T13:08:20-07:00",
          "LastUpdatedTime": "2014-09-18T13:08:20-07:00"
        }
      },
      {
        "DocNumber": "1",
        "SyncToken": "0",
        "domain": "QBO",
        "PurchaseEx": {
          "any": [
            {
              "name": "{http://schema.intuit.com/finance/v3}NameValue",
              "nil": false,
              "value": {
                "Name": "TxnType",
                "Value": "54"
              },
              "declaredType": "com.intuit.schema.finance.v3.NameValue",
              "scope": "javax.xml.bind.JAXBElement$GlobalScope",
              "globalScope": true,
              "typeSubstituted": false
            }
          ]
        },
        "Credit": false,
        "TotalAmt": 112.0,
        "PaymentType": "CreditCard",
        "TxnDate": "2014-09-17",
        "EntityRef": {
          "type": "Vendor",
          "name": "Ellis Equipment Rental",
          "value": "38"
        },
        "sparse": false,
        "Line": [
          {
            "DetailType": "AccountBasedExpenseLineDetail",
            "Amount": 112.0,
            "Id": "1",
            "AccountBasedExpenseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "AccountRef": {
                "name": "Equipment Rental",
                "value": "29"
              },
              "BillableStatus": "NotBillable"
            },
            "Description": "Equipment rental for 5 days"
          }
        ],
        "AccountRef": {
          "name": "Mastercard",
          "value": "41"
        },
        "Id": "51",
        "MetaData": {
          "CreateTime": "2014-09-17T11:45:45-07:00",
          "LastUpdatedTime": "2014-09-17T11:45:45-07:00"
        }
      }
    ],
    "maxResults": 8
  },
  "time": "2015-07-27T09:09:11.269-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T09:07:48.039-07:00">
    <QueryResponse startPosition="1" maxResults="8">
        <Purchase domain="QBO" sparse="false">
            <Id>139</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-10-03T14:35:37-07:00</CreateTime>
                <LastUpdatedTime>2014-10-03T14:35:37-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-10-03</TxnDate>
            <PrivateNote>Monthly Payment</PrivateNote>
            <Line>
                <Id>1</Id>
                <Amount>900.00</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <AccountRef name="Checking">35</AccountRef>
                    <BillableStatus>NotBillable</BillableStatus>
                    <TaxCodeRef>NON</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
                <ProjectRef>39298045</ProjectRef>
            </Line>
            <AccountRef name="Mastercard">41</AccountRef>
            <PaymentType>CreditCard</PaymentType>
            <Credit>true</Credit>
            <TotalAmt>900.00</TotalAmt>
            <PurchaseEx>
                <NameValue>
                    <Name>TxnType</Name>
                    <Value>11</Value>
                </NameValue>
            </PurchaseEx>
        </Purchase>
        <Purchase domain="QBO" sparse="false">
            <Id>133</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-10-03T14:17:55-07:00</CreateTime>
                <LastUpdatedTime>2014-10-03T14:17:55-07:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>70</DocNumber>
            <TxnDate>2014-09-11</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>185.00</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <AccountRef name="Maintenance and Repair">72</AccountRef>
                    <BillableStatus>NotBillable</BillableStatus>
                    <TaxCodeRef>NON</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
            </Line>
            <AccountRef name="Checking">35</AccountRef>
            <PaymentType>Check</PaymentType>
            <EntityRef name="Chin's Gas and Oil" type="Vendor">33</EntityRef>
            <TotalAmt>185.00</TotalAmt>
            <PrintStatus>NotSet</PrintStatus>
            <PurchaseEx>
                <NameValue>
                    <Name>TxnType</Name>
                    <Value>3</Value>
                </NameValue>
            </PurchaseEx>
        </Purchase>
        <Purchase domain="QBO" sparse="false">
            <Id>115</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-19T12:51:46-07:00</CreateTime>
                <LastUpdatedTime>2014-09-19T12:51:46-07:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>75</DocNumber>
            <TxnDate>2014-09-19</TxnDate>
            <Line>
                <Id>1</Id>
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
            <Line>
                <Id>2</Id>
                <Description>Sprinkler Heads</Description>
                <Amount>11.25</Amount>
                <DetailType>ItemBasedExpenseLineDetail</DetailType>
                <ItemBasedExpenseLineDetail>
                    <ItemRef name="Sprinkler Heads">16</ItemRef>
                    <UnitPrice>0.75</UnitPrice>
                    <Qty>15</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                    <BillableStatus>NotBillable</BillableStatus>
                </ItemBasedExpenseLineDetail>
            </Line>
            <Line>
                <Id>3</Id>
                <Description>Sprinkler Pipes</Description>
                <Amount>62.50</Amount>
                <DetailType>ItemBasedExpenseLineDetail</DetailType>
                <ItemBasedExpenseLineDetail>
                    <ItemRef name="Sprinkler Pipes">17</ItemRef>
                    <UnitPrice>2.5</UnitPrice>
                    <Qty>25</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                    <BillableStatus>NotBillable</BillableStatus>
                </ItemBasedExpenseLineDetail>
            </Line>
            <Line>
                <Id>4</Id>
                <Description>Fountain Pump</Description>
                <Amount>30.00</Amount>
                <DetailType>ItemBasedExpenseLineDetail</DetailType>
                <ItemBasedExpenseLineDetail>
                    <ItemRef name="Pump">11</ItemRef>
                    <UnitPrice>10</UnitPrice>
                    <Qty>3</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                    <BillableStatus>NotBillable</BillableStatus>
                </ItemBasedExpenseLineDetail>
            </Line>
            <AccountRef name="Checking">35</AccountRef>
            <PaymentType>Check</PaymentType>
            <EntityRef name="Hicks Hardware" type="Vendor">41</EntityRef>
            <RemitToAddr>
                <Id>37</Id>
                <Line1>42 Main St.</Line1>
                <City>Middlefield</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94303</PostalCode>
                <Lat>37.445013</Lat>
                <Long>-122.1391443</Long>
            </RemitToAddr>
            <TotalAmt>228.75</TotalAmt>
            <PrintStatus>NotSet</PrintStatus>
            <PurchaseEx>
                <NameValue>
                    <Name>TxnType</Name>
                    <Value>3</Value>
                </NameValue>
            </PurchaseEx>
        </Purchase>
        <Purchase domain="QBO" sparse="false">
            <Id>107</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-19T12:36:23-07:00</CreateTime>
                <LastUpdatedTime>2014-09-19T12:36:23-07:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>12</DocNumber>
            <TxnDate>2014-07-09</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>250.00</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <AccountRef name="Legal &amp; Professional Fees:Accounting">69</AccountRef>
                    <BillableStatus>NotBillable</BillableStatus>
                    <TaxCodeRef>NON</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
            </Line>
            <AccountRef name="Checking">35</AccountRef>
            <PaymentType>Cash</PaymentType>
            <EntityRef name="Robertson &amp; Associates" type="Vendor">49</EntityRef>
            <TotalAmt>250.00</TotalAmt>
            <PurchaseEx>
                <NameValue>
                    <Name>TxnType</Name>
                    <Value>54</Value>
                </NameValue>
            </PurchaseEx>
        </Purchase>
        <Purchase domain="QBO" sparse="false">
            <Id>87</Id>
            <SyncToken>1</SyncToken>
            <MetaData>
                <CreateTime>2014-09-18T13:14:42-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T13:17:06-07:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>15</DocNumber>
            <TxnDate>2014-08-16</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>108.09</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <AccountRef name="Job Expenses">58</AccountRef>
                    <BillableStatus>NotBillable</BillableStatus>
                    <TaxCodeRef>NON</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
            </Line>
            <AccountRef name="Checking">35</AccountRef>
            <PaymentType>Cash</PaymentType>
            <EntityRef name="Tania's Nursery" type="Vendor">50</EntityRef>
            <TotalAmt>108.09</TotalAmt>
            <PurchaseEx>
                <NameValue>
                    <Name>TxnType</Name>
                    <Value>54</Value>
                </NameValue>
            </PurchaseEx>
        </Purchase>
        <Purchase domain="QBO" sparse="false">
            <Id>85</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-18T13:12:01-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T13:12:01-07:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>3</DocNumber>
            <TxnDate>2014-07-16</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>158.08</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <AccountRef name="Job Expenses:Job Materials:Plants and Soil">66</AccountRef>
                    <BillableStatus>NotBillable</BillableStatus>
                    <TaxCodeRef>NON</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
            </Line>
            <AccountRef name="Mastercard">41</AccountRef>
            <PaymentType>CreditCard</PaymentType>
            <EntityRef name="Tania's Nursery" type="Vendor">50</EntityRef>
            <Credit>false</Credit>
            <TotalAmt>158.08</TotalAmt>
            <PurchaseEx>
                <NameValue>
                    <Name>TxnType</Name>
                    <Value>54</Value>
                </NameValue>
            </PurchaseEx>
        </Purchase>
        <Purchase domain="QBO" sparse="false">
            <Id>83</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-18T13:08:20-07:00</CreateTime>
                <LastUpdatedTime>2014-09-18T13:08:20-07:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>13</DocNumber>
            <TxnDate>2014-09-13</TxnDate>
            <Line>
                <Id>1</Id>
                <Amount>215.66</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <AccountRef name="Job Expenses:Job Materials:Sprinklers and Drip Systems">67</AccountRef>
                    <BillableStatus>NotBillable</BillableStatus>
                    <TaxCodeRef>NON</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
            </Line>
            <AccountRef name="Checking">35</AccountRef>
            <PaymentType>Cash</PaymentType>
            <EntityRef name="Hicks Hardware" type="Vendor">41</EntityRef>
            <TotalAmt>215.66</TotalAmt>
            <PurchaseEx>
                <NameValue>
                    <Name>TxnType</Name>
                    <Value>54</Value>
                </NameValue>
            </PurchaseEx>
        </Purchase>
        <Purchase domain="QBO" sparse="false">
            <Id>51</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-09-17T11:45:45-07:00</CreateTime>
                <LastUpdatedTime>2014-09-17T11:45:45-07:00</LastUpdatedTime>
            </MetaData>
            <DocNumber>1</DocNumber>
            <TxnDate>2014-09-17</TxnDate>
            <Line>
                <Id>1</Id>
                <Description>Equipment rental for 5 days</Description>
                <Amount>112.00</Amount>
                <DetailType>AccountBasedExpenseLineDetail</DetailType>
                <AccountBasedExpenseLineDetail>
                    <AccountRef name="Equipment Rental">29</AccountRef>
                    <BillableStatus>NotBillable</BillableStatus>
                    <TaxCodeRef>NON</TaxCodeRef>
                </AccountBasedExpenseLineDetail>
            </Line>
            <AccountRef name="Mastercard">41</AccountRef>
            <PaymentType>CreditCard</PaymentType>
            <EntityRef name="Ellis Equipment Rental" type="Vendor">38</EntityRef>
            <Credit>false</Credit>
            <TotalAmt>112.00</TotalAmt>
            <PurchaseEx>
                <NameValue>
                    <Name>TxnType</Name>
                    <Value>54</Value>
                </NameValue>
            </PurchaseEx>
        </Purchase>
    </QueryResponse>
</IntuitResponse>
```

## Read a purchase

### Definition

- **Operation:** `GET /v3/company/<realmID>/purchase/<purchaseId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Purchase object that has been previously created.

### Returns

The purchase response body.

#### Example

```json
{
  "Purchase": {
    "SyncToken": "0",
    "domain": "QBO",
    "PurchaseEx": {
      "any": [
        {
          "name": "{http://schema.intuit.com/finance/v3}NameValue",
          "nil": false,
          "value": {
            "Name": "TxnType",
            "Value": "54"
          },
          "declaredType": "com.intuit.schema.finance.v3.NameValue",
          "scope": "javax.xml.bind.JAXBElement$GlobalScope",
          "globalScope": true,
          "typeSubstituted": false
        }
      ]
    },
    "TxnDate": "2015-07-27",
    "TotalAmt": 10.0,
    "PaymentType": "Cash",
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 10.0,
        "ProjectRef": {
          "value": "39298034"
        },
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "AccountRef": {
            "name": "Meals and Entertainment",
            "value": "13"
          },
          "BillableStatus": "NotBillable"
        }
      }
    ],
    "AccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "CustomField": [],
    "Id": "252",
    "MetaData": {
      "CreateTime": "2015-07-27T10:37:26-07:00",
      "LastUpdatedTime": "2015-07-27T10:37:26-07:00"
    }
  },
  "time": "2015-07-27T10:39:33.171-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T10:39:51.538-07:00">
    <Purchase domain="QBO" sparse="false">
        <Id>252</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-27T10:37:26-07:00</CreateTime>
            <LastUpdatedTime>2015-07-27T10:37:26-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-07-27</TxnDate>
        <Line>
            <Id>1</Id>
            <Amount>10.00</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <AccountRef name="Meals and Entertainment">13</AccountRef>
                <BillableStatus>NotBillable</BillableStatus>
                <TaxCodeRef>NON</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <AccountRef name="Checking">35</AccountRef>
        <PaymentType>Cash</PaymentType>
        <TotalAmt>10.00</TotalAmt>
        <PurchaseEx>
            <NameValue>
                <Name>TxnType</Name>
                <Value>54</Value>
            </NameValue>
        </PurchaseEx>
    </Purchase>
</IntuitResponse>
```

## Full update a purchase

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/purchase`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing purchase object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `purchaseresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "1",
  "domain": "QBO",
  "PurchaseEx": {
    "any": [
      {
        "name": "{http://schema.intuit.com/finance/v3}NameValue",
        "nil": false,
        "value": {
          "Name": "TxnType",
          "Value": "54"
        },
        "declaredType": "com.intuit.schema.finance.v3.NameValue",
        "scope": "javax.xml.bind.JAXBElement$GlobalScope",
        "globalScope": true,
        "typeSubstituted": false
      }
    ]
  },
  "TxnDate": "2015-07-27",
  "TotalAmt": 10.0,
  "PrivateNote": "Added an updated private note via update.",
  "PaymentType": "Cash",
  "sparse": false,
  "Line": [
    {
      "DetailType": "AccountBasedExpenseLineDetail",
      "Amount": 10.0,
      "ProjectRef": {
        "value": "42991284"
      },
      "Id": "1",
      "AccountBasedExpenseLineDetail": {
        "TaxCodeRef": {
          "value": "NON"
        },
        "AccountRef": {
          "name": "Meals and Entertainment",
          "value": "13"
        },
        "BillableStatus": "NotBillable"
      }
    }
  ],
  "AccountRef": {
    "name": "Checking",
    "value": "35"
  },
  "CustomField": [],
  "Id": "252",
  "MetaData": {
    "CreateTime": "2015-07-27T10:37:26-07:00",
    "LastUpdatedTime": "2015-07-27T10:42:11-07:00"
  }
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-27T10:42:11.700-07:00">
    <Purchase domain="QBO" sparse="false">
        <Id>252</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2015-07-27T10:37:26-07:00</CreateTime>
            <LastUpdatedTime>2015-07-27T10:42:11-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2015-07-27</TxnDate>
        <PrivateNote>Added a private note via update.</PrivateNote>
        <Line>
            <Id>1</Id>
            <Amount>10.00</Amount>
            <DetailType>AccountBasedExpenseLineDetail</DetailType>
            <AccountBasedExpenseLineDetail>
                <AccountRef name="Meals and Entertainment">13</AccountRef>
                <BillableStatus>NotBillable</BillableStatus>
                <TaxCodeRef>NON</TaxCodeRef>
            </AccountBasedExpenseLineDetail>
            <ProjectRef>39298045</ProjectRef>
        </Line>
        <AccountRef name="Checking">35</AccountRef>
        <PaymentType>Cash</PaymentType>
        <TotalAmt>10.00</TotalAmt>
        <PurchaseEx>
            <NameValue>
                <Name>TxnType</Name>
                <Value>54</Value>
            </NameValue>
        </PurchaseEx>
    </Purchase>
</IntuitResponse>
```

### Returns

The invoice response body.

#### Example

```json
{
  "Purchase": {
    "SyncToken": "2",
    "domain": "QBO",
    "PurchaseEx": {
      "any": [
        {
          "name": "{http://schema.intuit.com/finance/v3}NameValue",
          "nil": false,
          "value": {
            "Name": "TxnType",
            "Value": "54"
          },
          "declaredType": "com.intuit.schema.finance.v3.NameValue",
          "scope": "javax.xml.bind.JAXBElement$GlobalScope",
          "globalScope": true,
          "typeSubstituted": false
        }
      ]
    },
    "TxnDate": "2015-07-27",
    "TotalAmt": 10.0,
    "PrivateNote": "Added an updated private note via update.",
    "PaymentType": "Cash",
    "sparse": false,
    "Line": [
      {
        "DetailType": "AccountBasedExpenseLineDetail",
        "Amount": 10.0,
        "ProjectRef": {
          "value": "42991284"
        },
        "Id": "1",
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "AccountRef": {
            "name": "Meals and Entertainment",
            "value": "13"
          },
          "BillableStatus": "NotBillable"
        }
      }
    ],
    "AccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "CustomField": [],
    "Id": "252",
    "MetaData": {
      "CreateTime": "2015-07-27T10:37:26-07:00",
      "LastUpdatedTime": "2015-07-27T10:45:20-07:00"
    }
  },
  "time": "2015-07-27T10:45:20.806-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-04-22T09:02:04.982-07:00">
  <QueryResponse startPosition="1" maxResults="1">
    <Purchase domain="QBO" sparse="false">
      <Id>603</Id>
      <SyncToken>2</SyncToken>
      <MetaData>
        <CreateTime>2018-07-18T00:00:00-07:00</CreateTime>
        <LastUpdatedTime>2014-04-22T09:00:40-07:00</LastUpdatedTime>
      </MetaData>
      <TxnDate>2018-07-18</TxnDate>
      <CurrencyRef name="United States Dollar">USD</CurrencyRef>
      <PrivateNote>Taxable expense.</PrivateNote>
      <Line>
        <Id>1</Id>
        <Amount>28.40</Amount>
        <DetailType>AccountBasedExpenseLineDetail</DetailType>
        <AccountBasedExpenseLineDetail>
          <CustomerRef name="Andres, Cristina">21</CustomerRef>
          <ClassRef name="Landscaping">100000000000368490</ClassRef>
          <AccountRef name="Automobile:Fuel">76</AccountRef>
          <BillableStatus>Billable</BillableStatus>
          <MarkupInfo>
            <Percent>10</Percent>
          </MarkupInfo>
          <TaxCodeRef>TAX</TaxCodeRef>
        </AccountBasedExpenseLineDetail>
        <ProjectRef>39298045</ProjectRef>
      </Line>
      <AccountRef name="CalOil Card">50</AccountRef>
      <PaymentType>CreditCard</PaymentType>
      <EntityRef name="Bayshore CalOil Service" type="Vendor">81</EntityRef>
      <Credit>false</Credit>
      <TotalAmt>28.40</TotalAmt>
    </Purchase>
  </QueryResponse>
</IntuitResponse>
```
