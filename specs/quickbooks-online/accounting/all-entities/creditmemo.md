# CreditMemo

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/creditmemo
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / CreditMemo
> Canonical entity: `CreditMemo`

The CreditMemo object is a financial transaction representing a refund or credit of payment or part of a payment for goods or services that have been sold.

## The creditmemo object

### creditmemoresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of a transaction. Valid `Line` types include:`SalesItemLine`, `GroupLine`, `DescriptionOnlyLine`, `DiscountLine` and `SubTotalLine`

<details>
<summary>Child attributes for `Line [0..n]`</summary>

##### salesitemline

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

Set to `SalesItemLineDetail`for this type of line.

###### `SalesItemLineDetail`

Required: Required
Type: `SalesItemLineDetail`

<details>
<summary>Child attributes for `SalesItemLineDetail`</summary>

###### salesitemlinedetail

Model type: `object`

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`
Minor version: 1
Locales: GB, AU, CA, IN

The total amount of the line item including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `DiscountAmt`

Required: Optional
Type: `Decimal`
Minor version: 4
Locales: FR

The discount amount applied to this line. If both `DiscountAmt` and `DiscountRate` are supplied, `DiscountRate` takes precedence and `DiscountAmt` is recalculated by QuickBooks services based on amount of `DiscountRate`.

###### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to an Item object.

Query the Item name list resource to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively.

Set ItemRef.value to `SHIPPING_ITEM_ID` when Line.amount represents transaction-wide shipping charges. Valid when `Preferences.SalesFormsPrefs.AllowShipping` is set to `true`.

Set ItemRef.value to `GRATUITY_ITEM_ID` when Line.amount represents transaction-wide gratuity amount. Valid when `Preferences.OtherPrefs.Name.SalesFormsPrefs.AllowGratuity` is set to `true`.

When a line lacks an ItemRef it is treated as documentation and the `Line.Amount`attribute is ignored.

Applicable to invoice objects, only, and when `linktxn` specifies a `ReimburseCharge`. When `Item.Id` is set to 1, `ItemAccountRef` refers to reimburse expense account Id.

For France locales: The account associated with the referenced Item object is looked up in the account category list.

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

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class for the line item. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

Used to define markup when this line represents a billable expense on the invoice. Markup information for the billable expense line.

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

###### `ItemAccountRef`

Required: Optional
Type: `ReferenceType`

Available with invoice objects, only, and when there is a `linkedtxn` of type `ReimburseCharge` for this object. When `ItemRef.Id` is set to 1, `ItemAccountRef` maps to the reimbursable charge account.

<details>
<summary>Child attributes for `ItemAccountRef`</summary>

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

###### `DiscountRate`

Required: Optional
Type: `Decimal`
Minor version: 4
Locales: FR

The discount rate applied to this line. If both `DiscountAmt` and `DiscountRate` are supplied, `DiscountRate` takes precedence and `DiscountAmt` is recalculated by QuickBooks services based on amount of `DiscountRate`.

###### `Qty`

Required: Optional
Type: `Decimal`

Number of items for the line.

###### `UnitPrice`

Required: Optional
Type: `Decimal`

Unit price of the subject item as referenced by `ItemRef`. Corresponds to the Rate column on the QuickBooks Online UI to specify either unit price, a discount, or a tax rate for item. If used for unit price, the monetary value of the service or product, as expressed in the home currency. You can override the unit price of the subject item by supplying a new value with create or update operations. If used for a discount or tax rate, express the percentage as a fraction. For example, specify `0.4` for 40% tax.

###### `TaxClassificationRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, system defined
Minor version: 21

Reference to the `TaxClassification`for this item. Available for companies that have [automated sales tax](https://developer.intuit.com/hub/blog/2017/12/11/using-quickbooks-online-api-automated-sales-tax) enabled.

`TaxClassificationRef.Name`: Currently not populated.

`TaxClassificationRef.value`: The system-defined Tax Classification code that is applied to this line item.

For internal use only.

<details>
<summary>Child attributes for `TaxClassificationRef`</summary>

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

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item. For Invoice objects in global locales: when updating `Amount`, remove the `TxnTaxDetail` element in the object before submitting it in the update request payload.

###### `Description`

Required: Optional
Type: `String`
Max length: Max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer

##### groupline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. Its use in requests is as folllows:

If `Id`is greater than zero and exists for the company, the request is considered an update operation for a line item.

If no `Id`is provided, the `Id`provided is less than or equal to zero, or the `Id`provided is greater than zero and does not exist for the company then the request is considered a create operation for a line item.

Available in all objects that use lines and support the update operation.

###### `GroupLineDetail`

Required: Required
Type: `GroupLineDetail`

<details>
<summary>Child attributes for `GroupLineDetail`</summary>

###### grouplinedetail

Model type: `object`

###### `Quantity`

Required: Optional
Type: `Decimal`
Default: 1

Quantity of the group item.

###### `Line [0..n]`

Required: Optional
Type: `Line`

Individual ItemLine elements that comprise a bundle. Returned in responses.

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### salesitemline

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

Set to `SalesItemLineDetail`for this type of line.

###### `SalesItemLineDetail`

Required: Required
Type: `SalesItemLineDetail`

<details>
<summary>Child attributes for `SalesItemLineDetail`</summary>

###### salesitemlinedetail

Model type: `object`

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`
Minor version: 1
Locales: GB, AU, CA, IN

The total amount of the line item including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `DiscountAmt`

Required: Optional
Type: `Decimal`
Minor version: 4
Locales: FR

The discount amount applied to this line. If both `DiscountAmt` and `DiscountRate` are supplied, `DiscountRate` takes precedence and `DiscountAmt` is recalculated by QuickBooks services based on amount of `DiscountRate`.

###### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to an Item object.

Query the Item name list resource to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively.

Set ItemRef.value to `SHIPPING_ITEM_ID` when Line.amount represents transaction-wide shipping charges. Valid when `Preferences.SalesFormsPrefs.AllowShipping` is set to `true`.

Set ItemRef.value to `GRATUITY_ITEM_ID` when Line.amount represents transaction-wide gratuity amount. Valid when `Preferences.OtherPrefs.Name.SalesFormsPrefs.AllowGratuity` is set to `true`.

When a line lacks an ItemRef it is treated as documentation and the `Line.Amount`attribute is ignored.

Applicable to invoice objects, only, and when `linktxn` specifies a `ReimburseCharge`. When `Item.Id` is set to 1, `ItemAccountRef` refers to reimburse expense account Id.

For France locales: The account associated with the referenced Item object is looked up in the account category list.

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

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class for the line item. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

Used to define markup when this line represents a billable expense on the invoice. Markup information for the billable expense line.

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

###### `ItemAccountRef`

Required: Optional
Type: `ReferenceType`

Available with invoice objects, only, and when there is a `linkedtxn` of type `ReimburseCharge` for this object. When `ItemRef.Id` is set to 1, `ItemAccountRef` maps to the reimbursable charge account.

<details>
<summary>Child attributes for `ItemAccountRef`</summary>

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

###### `DiscountRate`

Required: Optional
Type: `Decimal`
Minor version: 4
Locales: FR

The discount rate applied to this line. If both `DiscountAmt` and `DiscountRate` are supplied, `DiscountRate` takes precedence and `DiscountAmt` is recalculated by QuickBooks services based on amount of `DiscountRate`.

###### `Qty`

Required: Optional
Type: `Decimal`

Number of items for the line.

###### `UnitPrice`

Required: Optional
Type: `Decimal`

Unit price of the subject item as referenced by `ItemRef`. Corresponds to the Rate column on the QuickBooks Online UI to specify either unit price, a discount, or a tax rate for item. If used for unit price, the monetary value of the service or product, as expressed in the home currency. You can override the unit price of the subject item by supplying a new value with create or update operations. If used for a discount or tax rate, express the percentage as a fraction. For example, specify `0.4` for 40% tax.

###### `TaxClassificationRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, system defined
Minor version: 21

Reference to the `TaxClassification`for this item. Available for companies that have [automated sales tax](https://developer.intuit.com/hub/blog/2017/12/11/using-quickbooks-online-api-automated-sales-tax) enabled.

`TaxClassificationRef.Name`: Currently not populated.

`TaxClassificationRef.value`: The system-defined Tax Classification code that is applied to this line item.

For internal use only.

<details>
<summary>Child attributes for `TaxClassificationRef`</summary>

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

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item. For Invoice objects in global locales: when updating `Amount`, remove the `TxnTaxDetail` element in the object before submitting it in the update request payload.

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

###### `GroupItemRef`

Required: Optional
Type: `ReferenceType`

Reference to a group item for all the lines that belong to the bundle. Query the Item name list resource to determine the appropriate Item group object (`Item.Type=Group`) for this reference. Use `Item.Id` and `Item.Name` from that object for `GroupItemRef.value` and `GroupItemRef.name`, respectively.

<details>
<summary>Child attributes for `GroupItemRef`</summary>

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

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `GroupLineDetail`for this type of line.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer

###### `Description`

Required: Optional
Type: `String`
Max length: Max 4000 chars

Free form text description of the line item that appears in the printed record.

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

##### discountline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. Its use in requests is as folllows:

If `Id`is greater than zero and exists for the company, the request is considered an update operation for a line item.

If no `Id`is provided, the `Id`provided is less than or equal to zero, or the `Id`provided is greater than zero and does not exist for the company then the request is considered a create operation for a line item.

Available in all objects that use lines and support the update operation. Not supported for BillPayment, Estimate, Invoice, or Payment objects.

###### `DiscountLineDetail`

Required: Required
Type: `DiscountLineDetail`

Discount detail type for the entire transaction. This is in contrast to a discount applied to a specific line. The company preference **Sales Form Entry | Discounts** must be enabled for this type of line to be available. Must be enabled for this type of line to be available.

<details>
<summary>Child attributes for `DiscountLineDetail`</summary>

###### discountlinedetail

Model type: `object`

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with this discount. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

###### `DiscountAccountRef`

Required: Optional
Type: `ReferenceType`

Income account used to track discounts. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType=Income` and `Account.AccountSubType=DiscountsRefundsGiven`. Use `Account.Id` and `Account.Name` from that object for `DiscountAccountRef.value` and `DiscountAccountRef.name`, respectively.

<details>
<summary>Child attributes for `DiscountAccountRef`</summary>

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

###### `PercentBased`

Required: Optional
Type: `Boolean`

True if the discount is a percentage; null or false if discount based on amount.

###### `DiscountPercent`

Required: Optional
Type: `Decimal`

Percentage by which the amount due is reduced, from 0% to 100%. To enter a discount of 8.5% use 8.5, not 0.085.

</details>

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `DiscountLineDetail`for this type of line.

###### `Amount`

Required: Required
Type: `Decimal`
Max length: max 15 digits in 10.5 format

The amount of the line item.

###### `Description`

Required: Optional
Type: `String`
Max length: max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer.

##### subtotalline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. Its use in requests is as folllows:

If `Id`is greater than zero and exists for the company, the request is considered an update operation for a line item.

If no `Id`is provided, the `Id`provided is less than or equal to zero, or the `Id`provided is greater than zero and does not exist for the company then the request is considered a create operation for a line item.

Available in all objects that use lines and support the update operation.

###### `SubTotalLineDetail`

Required: Required
Type: `LineDetail`

Subtotal **LineDetail**

<details>
<summary>Child attributes for `SubTotalLineDetail`</summary>

###### subtotallinedetail

Model type: `object`

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

</details>

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `SubTotalLineDetail`for this type of line.

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item.

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

#### `CustomerRef`

Required: Required
Type: `ReferenceType`
Traits: filterable

Reference to a customer or job. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

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

#### `BillEmail`

Required: Conditionally required
Type: `EmailAddress`

Identifies the e-mail address where the credit-memo is sent. If `EmailStatus=NeedToSend`, `BillEmail`is a required input.

<details>
<summary>Child attributes for `BillEmail`</summary>

##### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

</details>

#### `HomeBalance`

Type: `Decimal`
Traits: read only
Minor version: 3

Convenience field containing the amount in `Balance` expressed in terms of the home currency. Calculated by QuickBooks business logic. Value is valid only when `CurrencyRef` is specified and available when endpoint is evoked with the `minorversion=3` query parameter. Applicable if multicurrency is enabled for the company.

#### `RemainingCredit`

Type: `Decimal`
Traits: read only

Indicates the total credit amount still available to apply towards the payment.

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `CreditMemo` was created from.

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

#### `TaxExemptionRef`

Type: `ReferenceType`
Traits: read only, system defined
Minor version: 21

Reference to the `TaxExepmtion` ID associated with this object. Available for companies that have [automated sales tax](https://developer.intuit.com/hub/blog/2017/12/11/using-quickbooks-online-api-automated-sales-tax) enabled.

`TaxExemptionRef.Name`: The Tax Exemption Id for the customer to which this object is associated. This Id is typically issued by the state.

`TaxExemptionRef.value`: The system-generated Id of the exemption type.

For internal use only.

<details>
<summary>Child attributes for `TaxExemptionRef`</summary>

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
Traits: read only, filterable, sortable

The balance reflecting any payments made against the transaction. Initially set to the value of `TotalAmt`. A Balance of 0 indicates the invoice is fully paid. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `HomeTotalAmt`

Type: `Decimal`
Traits: read only, system defined

Total amount of the transaction in the home currency. Includes the total of all the charges, allowances and taxes. Calculated by QuickBooks business logic. Value is valid only when `CurrencyRef` is specified. Applicable if multicurrency is enabled for the company.

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

#### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with the transaction. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

#### `PrintStatus`

Required: Optional
Type: `String`
Default: <span class="literal">NotSet</span>

Printing status of the credit-memo. Valid values: `NotSet`, `NeedToPrint`, `PrintComplete`.

#### `SalesTermRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable

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

#### `TotalAmt`

Required: Optional
Type: `BigDecimal`

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `InvoiceRef`

Required: Optional
Type: `ReferenceType`
Default: WithinIndia
Minor version: 37
Locales: IN

Reference to the Invoice for which Credit memo is issued. Needed for GST compliance. Use `Invoice.Id` and `Invoice.Name` from that object for `InvoiceRef.value` and `InvoiceRef.name`, respectively.

<details>
<summary>Child attributes for `InvoiceRef`</summary>

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
Default: WithinFrance
Minor version: 4
Locales: FR

The account location. Valid values include:

`WithinFrance`

`FranceOverseas`

`OutsideFranceWithEU`

`OutsideEU`

For France locales, only.

#### `ApplyTaxAfterDiscount`

Required: Optional
Type: `Boolean`
Default: <span class="literal">false</span>
Locales: US

If false or null, calculate the sales tax first, and then apply the discount. If true, subtract the discount first and then calculate the sales tax. US versions of QuickBooks only.

#### `DocNumber`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: maximum of 21 chars

Reference number for the transaction. If not explicitly provided at create time, this field is populated based on the setting of `Preferences:CustomTxnNumber` as follows:

If `Preferences:CustomTxnNumber` is true a custom value can be provided. If no value is supplied, the resulting DocNumber is null.

If `Preferences:CustomTxnNumber` is false, resulting DocNumber is system generated by incrementing the last number by 1.

If `Preferences:CustomTxnNumber` is false then do not send a value as it can lead to unwanted duplicates. If a DocNumber value is sent for an Update operation, then it just updates that particular invoice and does not alter the internal system DocNumber.
*Note:* DocNumber is an optional field for all locales except France. For France locale if `Preferences:CustomTxnNumber` is enabled it will **not** be automatically generated and is a required field.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the deposit form.

#### `CustomerMemo`

Required: Optional
Type: `MemoRef`

User-entered message to the customer; this message is visible to end user on their transactions.

<details>
<summary>Child attributes for `CustomerMemo`</summary>

##### memoref

Model type: `object`

###### `value`

Required: Required
Type: `String`
Max length: Maximum 1000 chars

User-entered message to the customer; this message is visible to the end user on their transactions.

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

#### `PaymentMethodRef`

Required: Optional
Type: `ReferenceType`
Traits: read only

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

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

#### `ShipAddr`

Required: Optional
Type: `PhysicalAddress`

Identifies the address where the goods must be shipped. If `ShipAddr`is not specified, and a default `Customer:ShippingAddr` is specified in QuickBooks for this customer, the default ship-to address will be used by QuickBooks.
For international addresses - countries should be passed as 3 ISO alpha-3 characters or the full name of the country.
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

#### `EmailStatus`

Required: Optional
Type: `String`
Default: <span class="literal">NotSet</span>

Email status of the credit-memo. Valid values: `NotSet`, `NeedToSend`, `EmailSent`

#### `BillAddr`

Required: Optional
Type: `PhysicalAddress`

Bill-to address of the credit memo. If `BillAddr`is not specified, and a default `Customer:BillingAddr` is specified in QuickBooks for this customer, the default bill-to address is used by QuickBooks.
For international addresses - countries should be passed as 3 ISO alpha-3 characters or the full name of the country.
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
  "CreditMemo": {
    "TxnDate": "2014-09-02",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "TotalAmt": 100.0,
    "RemainingCredit": 0,
    "Line": [
      {
        "Description": "Pest Control Services",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 1,
          "UnitPrice": 100,
          "ItemRef": {
            "name": "Pest Control",
            "value": "10"
          }
        },
        "LineNum": 1,
        "Amount": 100.0,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 100.0,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1026",
    "sparse": false,
    "CustomerMemo": {
      "value": "Updated customer memo."
    },
    "ProjectRef": {
      "value": "39298034"
    },
    "Balance": 0,
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "3",
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "ShipAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Bayshore",
      "PostalCode": "94326",
      "Id": "108",
      "Line1": "4581 Finch St."
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "Line4": "Bayshore, CA  94326",
      "Line3": "4581 Finch St.",
      "Id": "79",
      "Line1": "Amy Lauterbach",
      "Line2": "Amy's Bird Sanctuary"
    },
    "MetaData": {
      "CreateTime": "2014-09-18T12:51:27-07:00",
      "LastUpdatedTime": "2015-07-01T09:16:28-07:00"
    },
    "BillEmail": {
      "Address": "Birds@Intuit.com"
    },
    "Id": "73"
  },
  "time": "2015-07-23T09:10:45.624-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T09:10:07.878-07:00">
    <CreditMemo domain="QBO" sparse="false">
        <Id>73</Id>
        <SyncToken>3</SyncToken>
        <MetaData>
            <CreateTime>2014-09-18T12:51:27-07:00</CreateTime>
            <LastUpdatedTime>2015-07-01T09:16:28-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1026</DocNumber>
        <TxnDate>2014-09-02</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Pest Control Services</Description>
            <Amount>100.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Pest Control">10</ItemRef>
                <UnitPrice>100</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>100.00</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
        <ProjectRef>39298034</ProjectRef>
        <CustomerMemo>Updated customer memo.</CustomerMemo>
        <BillAddr>
            <Id>79</Id>
            <Line1>Amy Lauterbach</Line1>
            <Line2>Amy's Bird Sanctuary</Line2>
            <Line3>4581 Finch St.</Line3>
            <Line4>Bayshore, CA 94326</Line4>
        </BillAddr>
        <ShipAddr>
            <Id>108</Id>
            <Line1>4581 Finch St.</Line1>
            <City>Bayshore</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94326</PostalCode>
        </ShipAddr>
        <TotalAmt>100.00</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <BillEmail>
            <Address>Birds@Intuit.com</Address>
        </BillEmail>
        <Balance>0</Balance>
        <RemainingCredit>0</RemainingCredit>
    </CreditMemo>
</IntuitResponse>
```

## Create a credit memo

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/creditmemo`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The minimum elements to create an creditmemo are listed here.

Schema: `creditmemorequest`

<details>
<summary>Show schema for `creditmemorequest`</summary>

#### creditmemorequest

Model type: `object`

##### `Line`

Required: Required

The minimum line item required for the request is one of the following. Sales item line type Group item line type

<details>
<summary>Child attributes for `Line`</summary>

###### salesitemline

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

Set to `SalesItemLineDetail`for this type of line.

###### `SalesItemLineDetail`

Required: Required
Type: `SalesItemLineDetail`

<details>
<summary>Child attributes for `SalesItemLineDetail`</summary>

###### salesitemlinedetail

Model type: `object`

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`
Minor version: 1
Locales: GB, AU, CA, IN

The total amount of the line item including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `DiscountAmt`

Required: Optional
Type: `Decimal`
Minor version: 4
Locales: FR

The discount amount applied to this line. If both `DiscountAmt` and `DiscountRate` are supplied, `DiscountRate` takes precedence and `DiscountAmt` is recalculated by QuickBooks services based on amount of `DiscountRate`.

###### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to an Item object.

Query the Item name list resource to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively.

Set ItemRef.value to `SHIPPING_ITEM_ID` when Line.amount represents transaction-wide shipping charges. Valid when `Preferences.SalesFormsPrefs.AllowShipping` is set to `true`.

Set ItemRef.value to `GRATUITY_ITEM_ID` when Line.amount represents transaction-wide gratuity amount. Valid when `Preferences.OtherPrefs.Name.SalesFormsPrefs.AllowGratuity` is set to `true`.

When a line lacks an ItemRef it is treated as documentation and the `Line.Amount`attribute is ignored.

Applicable to invoice objects, only, and when `linktxn` specifies a `ReimburseCharge`. When `Item.Id` is set to 1, `ItemAccountRef` refers to reimburse expense account Id.

For France locales: The account associated with the referenced Item object is looked up in the account category list.

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

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class for the line item. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

Used to define markup when this line represents a billable expense on the invoice. Markup information for the billable expense line.

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

###### `ItemAccountRef`

Required: Optional
Type: `ReferenceType`

Available with invoice objects, only, and when there is a `linkedtxn` of type `ReimburseCharge` for this object. When `ItemRef.Id` is set to 1, `ItemAccountRef` maps to the reimbursable charge account.

<details>
<summary>Child attributes for `ItemAccountRef`</summary>

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

###### `DiscountRate`

Required: Optional
Type: `Decimal`
Minor version: 4
Locales: FR

The discount rate applied to this line. If both `DiscountAmt` and `DiscountRate` are supplied, `DiscountRate` takes precedence and `DiscountAmt` is recalculated by QuickBooks services based on amount of `DiscountRate`.

###### `Qty`

Required: Optional
Type: `Decimal`

Number of items for the line.

###### `UnitPrice`

Required: Optional
Type: `Decimal`

Unit price of the subject item as referenced by `ItemRef`. Corresponds to the Rate column on the QuickBooks Online UI to specify either unit price, a discount, or a tax rate for item. If used for unit price, the monetary value of the service or product, as expressed in the home currency. You can override the unit price of the subject item by supplying a new value with create or update operations. If used for a discount or tax rate, express the percentage as a fraction. For example, specify `0.4` for 40% tax.

###### `TaxClassificationRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, system defined
Minor version: 21

Reference to the `TaxClassification`for this item. Available for companies that have [automated sales tax](https://developer.intuit.com/hub/blog/2017/12/11/using-quickbooks-online-api-automated-sales-tax) enabled.

`TaxClassificationRef.Name`: Currently not populated.

`TaxClassificationRef.value`: The system-defined Tax Classification code that is applied to this line item.

For internal use only.

<details>
<summary>Child attributes for `TaxClassificationRef`</summary>

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

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item. For Invoice objects in global locales: when updating `Amount`, remove the `TxnTaxDetail` element in the object before submitting it in the update request payload.

###### `Description`

Required: Optional
Type: `String`
Max length: Max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer

###### groupline

Model type: `object`

###### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

The Id of the line item. Its use in requests is as folllows:

If `Id`is greater than zero and exists for the company, the request is considered an update operation for a line item.

If no `Id`is provided, the `Id`provided is less than or equal to zero, or the `Id`provided is greater than zero and does not exist for the company then the request is considered a create operation for a line item.

Available in all objects that use lines and support the update operation.

###### `GroupLineDetail`

Required: Required
Type: `GroupLineDetail`

<details>
<summary>Child attributes for `GroupLineDetail`</summary>

###### grouplinedetail

Model type: `object`

###### `Quantity`

Required: Optional
Type: `Decimal`
Default: 1

Quantity of the group item.

###### `Line [0..n]`

Required: Optional
Type: `Line`

Individual ItemLine elements that comprise a bundle. Returned in responses.

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### salesitemline

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

Set to `SalesItemLineDetail`for this type of line.

###### `SalesItemLineDetail`

Required: Required
Type: `SalesItemLineDetail`

<details>
<summary>Child attributes for `SalesItemLineDetail`</summary>

###### salesitemlinedetail

Model type: `object`

###### `TaxInclusiveAmt`

Required: Optional
Type: `Decimal`
Minor version: 1
Locales: GB, AU, CA, IN

The total amount of the line item including tax. Constraints: Available when endpoint is evoked with the `minorversion=1`query parameter.

###### `DiscountAmt`

Required: Optional
Type: `Decimal`
Minor version: 4
Locales: FR

The discount amount applied to this line. If both `DiscountAmt` and `DiscountRate` are supplied, `DiscountRate` takes precedence and `DiscountAmt` is recalculated by QuickBooks services based on amount of `DiscountRate`.

###### `ItemRef`

Required: Optional
Type: `ReferenceType`

Reference to an Item object.

Query the Item name list resource to determine the appropriate Item object for this reference. Use `Item.Id` and `Item.Name` from that object for `ItemRef.value` and `ItemRef.name`, respectively.

Set ItemRef.value to `SHIPPING_ITEM_ID` when Line.amount represents transaction-wide shipping charges. Valid when `Preferences.SalesFormsPrefs.AllowShipping` is set to `true`.

Set ItemRef.value to `GRATUITY_ITEM_ID` when Line.amount represents transaction-wide gratuity amount. Valid when `Preferences.OtherPrefs.Name.SalesFormsPrefs.AllowGratuity` is set to `true`.

When a line lacks an ItemRef it is treated as documentation and the `Line.Amount`attribute is ignored.

Applicable to invoice objects, only, and when `linktxn` specifies a `ReimburseCharge`. When `Item.Id` is set to 1, `ItemAccountRef` refers to reimburse expense account Id.

For France locales: The account associated with the referenced Item object is looked up in the account category list.

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

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class for the line item. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

Used to define markup when this line represents a billable expense on the invoice. Markup information for the billable expense line.

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

###### `ItemAccountRef`

Required: Optional
Type: `ReferenceType`

Available with invoice objects, only, and when there is a `linkedtxn` of type `ReimburseCharge` for this object. When `ItemRef.Id` is set to 1, `ItemAccountRef` maps to the reimbursable charge account.

<details>
<summary>Child attributes for `ItemAccountRef`</summary>

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

###### `DiscountRate`

Required: Optional
Type: `Decimal`
Minor version: 4
Locales: FR

The discount rate applied to this line. If both `DiscountAmt` and `DiscountRate` are supplied, `DiscountRate` takes precedence and `DiscountAmt` is recalculated by QuickBooks services based on amount of `DiscountRate`.

###### `Qty`

Required: Optional
Type: `Decimal`

Number of items for the line.

###### `UnitPrice`

Required: Optional
Type: `Decimal`

Unit price of the subject item as referenced by `ItemRef`. Corresponds to the Rate column on the QuickBooks Online UI to specify either unit price, a discount, or a tax rate for item. If used for unit price, the monetary value of the service or product, as expressed in the home currency. You can override the unit price of the subject item by supplying a new value with create or update operations. If used for a discount or tax rate, express the percentage as a fraction. For example, specify `0.4` for 40% tax.

###### `TaxClassificationRef`

Required: Optional
Type: `ReferenceType`
Traits: read only, system defined
Minor version: 21

Reference to the `TaxClassification`for this item. Available for companies that have [automated sales tax](https://developer.intuit.com/hub/blog/2017/12/11/using-quickbooks-online-api-automated-sales-tax) enabled.

`TaxClassificationRef.Name`: Currently not populated.

`TaxClassificationRef.value`: The system-defined Tax Classification code that is applied to this line item.

For internal use only.

<details>
<summary>Child attributes for `TaxClassificationRef`</summary>

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

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item. For Invoice objects in global locales: when updating `Amount`, remove the `TxnTaxDetail` element in the object before submitting it in the update request payload.

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

###### `GroupItemRef`

Required: Optional
Type: `ReferenceType`

Reference to a group item for all the lines that belong to the bundle. Query the Item name list resource to determine the appropriate Item group object (`Item.Type=Group`) for this reference. Use `Item.Id` and `Item.Name` from that object for `GroupItemRef.value` and `GroupItemRef.name`, respectively.

<details>
<summary>Child attributes for `GroupItemRef`</summary>

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

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set to `GroupLineDetail`for this type of line.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer

###### `Description`

Required: Optional
Type: `String`
Max length: Max 4000 chars

Free form text description of the line item that appears in the printed record.

</details>

##### `CustomerRef`

Required: Required
Type: `ReferenceType`
Traits: filterable

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

##### `ProjectRef`

Required: Conditionally required
Type: `ReferenceType`
Traits: filterable
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
      "DetailType": "SalesItemLineDetail",
      "Amount": 50,
      "SalesItemLineDetail": {
        "ItemRef": {
          "name": "Concrete",
          "value": "3"
        }
      }
    }
  ],
  "CustomerRef": {
    "name": "CoolCars",
    "value": "3"
  }
}
```

#### XML example

```xml
<CreditMemo xmlns="http://schema.intuit.com/finance/v3">
    <Line>
        <Amount>50</Amount>
        <DetailType>SalesItemLineDetail</DetailType>
        <SalesItemLineDetail>
            <ItemRef name="Concrete">3</ItemRef>
            <TaxCodeRef>TAX</TaxCodeRef>
        </SalesItemLineDetail>
    </Line>
    <CustomerRef name="Cool Cars">3</CustomerRef>
</CreditMemo>
```

### Returns

The creditmemo response body.

#### Example

```json
{
  "CreditMemo": {
    "DocNumber": "1039",
    "SyncToken": "0",
    "domain": "QBO",
    "Balance": 50.0,
    "BillAddr": {
      "City": "Half Moon Bay",
      "Line1": "65 Ocean Dr.",
      "PostalCode": "94213",
      "Lat": "37.4300318",
      "Long": "-122.4336537",
      "CountrySubDivisionCode": "CA",
      "Id": "4"
    },
    "TxnDate": "2014-12-31",
    "TotalAmt": 50.0,
    "CustomerRef": {
      "name": "Cool Cars",
      "value": "3"
    },
    "ShipAddr": {
      "City": "Half Moon Bay",
      "Line1": "65 Ocean Dr.",
      "PostalCode": "94213",
      "Lat": "37.4300318",
      "Long": "-122.4336537",
      "CountrySubDivisionCode": "CA",
      "Id": "4"
    },
    "RemainingCredit": 50.0,
    "PrintStatus": "NeedToPrint",
    "ProjectRef": {
      "value": "39298034"
    },
    "EmailStatus": "NotSet",
    "sparse": false,
    "Line": [
      {
        "LineNum": 1,
        "Amount": 50.0,
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "ItemRef": {
            "name": "Concrete",
            "value": "3"
          }
        },
        "Id": "1",
        "DetailType": "SalesItemLineDetail"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 50.0,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "150",
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "MetaData": {
      "CreateTime": "2014-12-31T09:44:40-08:00",
      "LastUpdatedTime": "2014-12-31T09:44:40-08:00"
    }
  },
  "time": "2014-12-31T09:44:40.726-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-31T09:39:59.991-08:00">
    <CreditMemo domain="QBO" sparse="false">
        <Id>149</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-12-31T09:40:00-08:00</CreateTime>
            <LastUpdatedTime>2014-12-31T09:40:00-08:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1038</DocNumber>
        <TxnDate>2014-12-31</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Amount>50.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Concrete">3</ItemRef>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>50.00</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Cool Cars">3</CustomerRef>
        <ProjectRef>39298034</ProjectRef>
        <BillAddr>
            <Id>4</Id>
            <Line1>65 Ocean Dr.</Line1>
            <City>Half Moon Bay</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94213</PostalCode>
            <Lat>37.4300318</Lat>
            <Long>-122.4336537</Long>
        </BillAddr>
        <ShipAddr>
            <Id>4</Id>
            <Line1>65 Ocean Dr.</Line1>
            <City>Half Moon Bay</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94213</PostalCode>
            <Lat>37.4300318</Lat>
            <Long>-122.4336537</Long>
        </ShipAddr>
        <TotalAmt>50.00</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <Balance>50.00</Balance>
        <RemainingCredit>50.00</RemainingCredit>
    </CreditMemo>
</IntuitResponse>
```

## Delete a credit memo

### Definition

- **Operation:** `POST /v3/company/<realmID>/creditmemo?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the creditmemo object specified in the request body. Include a minimum of `CreditMemo.Id` and `CreditMemo.SyncToken` in the request body.

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
  "Id": "73"
}
```

#### XML example

```xml
<CreditMemo xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>73</Id>
    <SyncToken>0</SyncToken>
</CreditMemo>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "CreditMemo": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "73"
  },
  "time": "2015-05-26T13:53:33.118-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-05-26T13:12:16.102-07:00">
    <CreditMemo domain="QBO" status="Deleted">
        <Id>73</Id>
    </CreditMemo>
</IntuitResponse>
```

## Get a credit memo as PDF

### Definition

- **Content type:** `application/pdf`
- **Operation:** `GET /v3/company/<realmID>/creditmemo/<creditmemoId>/pdf`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Returns

This resource returns the specified object in the response body as an Adobe Portable Document Format (PDF) file. The resulting PDF file is formatted according to custom form styles in the company settings.

## Query a credit memo

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"Select * from CreditMemo where TxnDate > '2014-04-15'"
```

#### XML example

```sql
Select * from CreditMemo where TxnDate > '2014-04-15'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "CreditMemo": [
      {
        "TxnDate": "2014-09-02",
        "domain": "QBO",
        "PrintStatus": "NeedToPrint",
        "TotalAmt": 100.0,
        "RemainingCredit": 0,
        "Line": [
          {
            "Description": "Pest Control Services",
            "DetailType": "SalesItemLineDetail",
            "SalesItemLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "Qty": 1,
              "UnitPrice": 100,
              "ItemRef": {
                "name": "Pest Control",
                "value": "10"
              }
            },
            "LineNum": 1,
            "Amount": 100.0,
            "Id": "1"
          },
          {
            "DetailType": "SubTotalLineDetail",
            "Amount": 100.0,
            "SubTotalLineDetail": {}
          }
        ],
        "ApplyTaxAfterDiscount": false,
        "DocNumber": "1026",
        "sparse": false,
        "CustomerMemo": {
          "value": "Updated customer memo."
        },
        "ProjectRef": {
          "value": "39298034"
        },
        "Balance": 0,
        "CustomerRef": {
          "name": "Amy's Bird Sanctuary",
          "value": "1"
        },
        "TxnTaxDetail": {
          "TotalTax": 0
        },
        "SyncToken": "3",
        "CustomField": [
          {
            "DefinitionId": "1",
            "Type": "StringType",
            "Name": "Crew #"
          }
        ],
        "ShipAddr": {
          "CountrySubDivisionCode": "CA",
          "City": "Bayshore",
          "PostalCode": "94326",
          "Id": "108",
          "Line1": "4581 Finch St."
        },
        "EmailStatus": "NotSet",
        "BillAddr": {
          "Line4": "Bayshore, CA  94326",
          "Line3": "4581 Finch St.",
          "Id": "79",
          "Line1": "Amy Lauterbach",
          "Line2": "Amy's Bird Sanctuary"
        },
        "MetaData": {
          "CreateTime": "2014-09-18T12:51:27-07:00",
          "LastUpdatedTime": "2015-07-01T09:16:28-07:00"
        },
        "BillEmail": {
          "Address": "Birds@Intuit.com"
        },
        "Id": "73"
      },
      {
        "DocNumber": "1039",
        "SyncToken": "0",
        "domain": "QBO",
        "Balance": 50.0,
        "BillAddr": {
          "City": "Half Moon Bay",
          "Line1": "65 Ocean Dr.",
          "PostalCode": "94213",
          "Lat": "37.4300318",
          "Long": "-122.4336537",
          "CountrySubDivisionCode": "CA",
          "Id": "4"
        },
        "TxnDate": "2015-01-13",
        "TotalAmt": 50.0,
        "CustomerRef": {
          "name": "Cool Cars",
          "value": "3"
        },
        "RemainingCredit": 50.0,
        "PrintStatus": "NeedToPrint",
        "ProjectRef": {
          "value": "36387497"
        },
        "EmailStatus": "NotSet",
        "sparse": false,
        "Line": [
          {
            "LineNum": 1,
            "Amount": 50.0,
            "SalesItemLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "ItemRef": {
                "name": "Concrete",
                "value": "3"
              }
            },
            "Id": "1",
            "DetailType": "SalesItemLineDetail"
          },
          {
            "DetailType": "SubTotalLineDetail",
            "Amount": 50.0,
            "SubTotalLineDetail": {}
          }
        ],
        "ApplyTaxAfterDiscount": false,
        "CustomField": [
          {
            "DefinitionId": "1",
            "Type": "StringType",
            "Name": "Crew #"
          }
        ],
        "Id": "158",
        "TxnTaxDetail": {
          "TotalTax": 0
        },
        "MetaData": {
          "CreateTime": "2015-01-13T10:32:35-08:00",
          "LastUpdatedTime": "2015-01-13T10:32:35-08:00"
        }
      }
    ],
    "maxResults": 2
  },
  "time": "2015-07-23T09:13:36.246-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T09:14:22.897-07:00">
    <QueryResponse startPosition="1" maxResults="2">
        <CreditMemo domain="QBO" sparse="false">
            <Id>73</Id>
            <SyncToken>3</SyncToken>
            <MetaData>
                <CreateTime>2014-09-18T12:51:27-07:00</CreateTime>
                <LastUpdatedTime>2015-07-01T09:16:28-07:00</LastUpdatedTime>
            </MetaData>
            <CustomField>
                <DefinitionId>1</DefinitionId>
                <Name>Crew #</Name>
                <Type>StringType</Type>
            </CustomField>
            <DocNumber>1026</DocNumber>
            <TxnDate>2014-09-02</TxnDate>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Description>Pest Control Services</Description>
                <Amount>100.00</Amount>
                <DetailType>SalesItemLineDetail</DetailType>
                <SalesItemLineDetail>
                    <ItemRef name="Pest Control">10</ItemRef>
                    <UnitPrice>100</UnitPrice>
                    <Qty>1</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                </SalesItemLineDetail>
            </Line>
            <Line>
                <Amount>100.00</Amount>
                <DetailType>SubTotalLineDetail</DetailType>
                <SubTotalLineDetail />
            </Line>
            <TxnTaxDetail>
                <TotalTax>0</TotalTax>
            </TxnTaxDetail>
            <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
            <ProjectRef>39298034</ProjectRef>
            <CustomerMemo>Updated customer memo.</CustomerMemo>
            <BillAddr>
                <Id>79</Id>
                <Line1>Amy Lauterbach</Line1>
                <Line2>Amy's Bird Sanctuary</Line2>
                <Line3>4581 Finch St.</Line3>
                <Line4>Bayshore, CA 94326</Line4>
            </BillAddr>
            <ShipAddr>
                <Id>108</Id>
                <Line1>4581 Finch St.</Line1>
                <City>Bayshore</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94326</PostalCode>
            </ShipAddr>
            <TotalAmt>100.00</TotalAmt>
            <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
            <PrintStatus>NeedToPrint</PrintStatus>
            <EmailStatus>NotSet</EmailStatus>
            <BillEmail>
                <Address>Birds@Intuit.com</Address>
            </BillEmail>
            <Balance>0</Balance>
            <RemainingCredit>0</RemainingCredit>
        </CreditMemo>
        <CreditMemo domain="QBO" sparse="false">
            <Id>158</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-01-13T10:32:35-08:00</CreateTime>
                <LastUpdatedTime>2015-01-13T10:32:35-08:00</LastUpdatedTime>
            </MetaData>
            <CustomField>
                <DefinitionId>1</DefinitionId>
                <Name>Crew #</Name>
                <Type>StringType</Type>
            </CustomField>
            <DocNumber>1039</DocNumber>
            <TxnDate>2015-01-13</TxnDate>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Amount>50.00</Amount>
                <DetailType>SalesItemLineDetail</DetailType>
                <SalesItemLineDetail>
                    <ItemRef name="Concrete">3</ItemRef>
                    <TaxCodeRef>NON</TaxCodeRef>
                </SalesItemLineDetail>
            </Line>
            <Line>
                <Amount>50.00</Amount>
                <DetailType>SubTotalLineDetail</DetailType>
                <SubTotalLineDetail />
            </Line>
            <TxnTaxDetail>
                <TotalTax>0</TotalTax>
            </TxnTaxDetail>
            <CustomerRef name="Cool Cars">3</CustomerRef>
            <ProjectRef>36387497</ProjectRef>
            <BillAddr>
                <Id>4</Id>
                <Line1>65 Ocean Dr.</Line1>
                <City>Half Moon Bay</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94213</PostalCode>
                <Lat>37.4300318</Lat>
                <Long>-122.4336537</Long>
            </BillAddr>
            <TotalAmt>50.00</TotalAmt>
            <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
            <PrintStatus>NeedToPrint</PrintStatus>
            <EmailStatus>NotSet</EmailStatus>
            <Balance>50.00</Balance>
            <RemainingCredit>50.00</RemainingCredit>
        </CreditMemo>
    </QueryResponse>
</IntuitResponse>
```

## Read a credit memo

### Definition

- **Content type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/creditmemo/<creditmemoId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a creditmemo that has been previously created.

### Returns

The creditmemo response body.

#### Example

```json
{
  "CreditMemo": {
    "TxnDate": "2014-09-02",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "TotalAmt": 100.0,
    "RemainingCredit": 0,
    "Line": [
      {
        "Description": "Pest Control Services",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 1,
          "UnitPrice": 100,
          "ItemRef": {
            "name": "Pest Control",
            "value": "10"
          }
        },
        "LineNum": 1,
        "Amount": 100.0,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 100.0,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1026",
    "sparse": false,
    "CustomerMemo": {
      "value": "Updated customer memo."
    },
    "ProjectRef": {
      "value": "39298034"
    },
    "Balance": 0,
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "3",
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "ShipAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Bayshore",
      "PostalCode": "94326",
      "Id": "108",
      "Line1": "4581 Finch St."
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "Line4": "Bayshore, CA  94326",
      "Line3": "4581 Finch St.",
      "Id": "79",
      "Line1": "Amy Lauterbach",
      "Line2": "Amy's Bird Sanctuary"
    },
    "MetaData": {
      "CreateTime": "2014-09-18T12:51:27-07:00",
      "LastUpdatedTime": "2015-07-01T09:16:28-07:00"
    },
    "BillEmail": {
      "Address": "Birds@Intuit.com"
    },
    "Id": "73"
  },
  "time": "2015-07-23T09:10:45.624-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T09:10:07.878-07:00">
    <CreditMemo domain="QBO" sparse="false">
        <Id>73</Id>
        <SyncToken>3</SyncToken>
        <MetaData>
            <CreateTime>2014-09-18T12:51:27-07:00</CreateTime>
            <LastUpdatedTime>2015-07-01T09:16:28-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1026</DocNumber>
        <TxnDate>2014-09-02</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Pest Control Services</Description>
            <Amount>100.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Pest Control">10</ItemRef>
                <UnitPrice>100</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>100.00</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
        <ProjectRef>39298034</ProjectRef>
        <CustomerMemo>Updated customer memo.</CustomerMemo>
        <BillAddr>
            <Id>79</Id>
            <Line1>Amy Lauterbach</Line1>
            <Line2>Amy's Bird Sanctuary</Line2>
            <Line3>4581 Finch St.</Line3>
            <Line4>Bayshore, CA 94326</Line4>
        </BillAddr>
        <ShipAddr>
            <Id>108</Id>
            <Line1>4581 Finch St.</Line1>
            <City>Bayshore</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94326</PostalCode>
        </ShipAddr>
        <TotalAmt>100.00</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <BillEmail>
            <Address>Birds@Intuit.com</Address>
        </BillEmail>
        <Balance>0</Balance>
        <RemainingCredit>0</RemainingCredit>
    </CreditMemo>
</IntuitResponse>
```

## Send a credit memo

### Definition

- **Content type:** `application/octet-stream`
- **Operation:** `POST (Using email address supplied in CreditMemo.BillEmail.EmailAddress) /v3/company/<realmID>/creditmemo/<creditmemoId>/send
POST(Specifying an explicit email address) /v3/company/<realmID>/creditmemo/<creditmemoId>/send?sendTo=<emailAddress>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- The `CreditMemo.EmailStatus` parameter is set to `EmailSent`.
- The `CreditMemo.DeliveryInfo` element is populated with sending information
- The `CreditMemo.BillEmail.Address` parameter is updated to the address specified with the value of the `sendTo` query parameter, if specified.

### Returns

The CreditMemo response body.

#### Example

```json
{
  "CreditMemo": {
    "TxnDate": "2014-09-02",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "DeliveryInfo": {
      "DeliveryType": "Email",
      "DeliveryTime": "2019-09-19T10:43:46-07:00"
    },
    "TotalAmt": 100.0,
    "RemainingCredit": 0,
    "Line": [
      {
        "Description": "Pest Control Services",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 1,
          "UnitPrice": 100,
          "ItemRef": {
            "name": "Pest Control",
            "value": "10"
          }
        },
        "LineNum": 1,
        "Amount": 100.0,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 100.0,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1026",
    "sparse": false,
    "CustomerMemo": {
      "value": "Updated customer memo."
    },
    "ProjectRef": {
      "value": "39298034"
    },
    "Balance": 0,
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "3",
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "ShipAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Bayshore",
      "PostalCode": "94326",
      "Id": "108",
      "Line1": "4581 Finch St."
    },
    "EmailStatus": "EmailSent",
    "BillAddr": {
      "Line4": "Bayshore, CA  94326",
      "Line3": "4581 Finch St.",
      "Id": "79",
      "Line1": "Amy Lauterbach",
      "Line2": "Amy's Bird Sanctuary"
    },
    "MetaData": {
      "CreateTime": "2014-09-18T12:51:27-07:00",
      "LastUpdatedTime": "2019-09-19T10:43:46-07:00"
    },
    "BillEmail": {
      "Address": "Birds@Intuit.com"
    },
    "Id": "73"
  },
  "time": "2019-09-19T10:43:46-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T09:10:07.878-07:00">
    <CreditMemo domain="QBO" sparse="false">
        <Id>73</Id>
        <SyncToken>3</SyncToken>
        <MetaData>
            <CreateTime>2014-09-18T12:51:27-07:00</CreateTime>
            <LastUpdatedTime>2019-09-19T10:43:46-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1026</DocNumber>
        <TxnDate>2014-09-02</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Pest Control Services</Description>
            <Amount>100.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Pest Control">10</ItemRef>
                <UnitPrice>100</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>100.00</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
        <ProjectRef>39298034</ProjectRef>
        <CustomerMemo>Updated customer memo.</CustomerMemo>
        <BillAddr>
            <Id>79</Id>
            <Line1>Amy Lauterbach</Line1>
            <Line2>Amy's Bird Sanctuary</Line2>
            <Line3>4581 Finch St.</Line3>
            <Line4>Bayshore, CA 94326</Line4>
        </BillAddr>
        <ShipAddr>
            <Id>108</Id>
            <Line1>4581 Finch St.</Line1>
            <City>Bayshore</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94326</PostalCode>
        </ShipAddr>
        <TotalAmt>100.00</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>EmailSent</EmailStatus>
        <BillEmail>
            <Address>Birds@Intuit.com</Address>
        </BillEmail>
         <DeliveryInfo>
            <DeliveryType>Email</DeliveryType>
            <DeliveryTime>2019-09-19T10:43:46-07:00</DeliveryTime>
        </DeliveryInfo>
        <Balance>0</Balance>
        <RemainingCredit>0</RemainingCredit>
    </CreditMemo>
</IntuitResponse>
```

## Full update a credit memo

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/creditmemo`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing creditmemo object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `creditmemoresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "TxnDate": "2014-09-02",
  "domain": "QBO",
  "PrintStatus": "NeedToPrint",
  "TotalAmt": 100.0,
  "RemainingCredit": 0,
  "Line": [
    {
      "Description": "Pest Control Services",
      "DetailType": "SalesItemLineDetail",
      "SalesItemLineDetail": {
        "TaxCodeRef": {
          "value": "NON"
        },
        "Qty": 1,
        "UnitPrice": 100,
        "ItemRef": {
          "name": "Pest Control",
          "value": "10"
        }
      },
      "LineNum": 1,
      "Amount": 100.0,
      "Id": "1"
    },
    {
      "DetailType": "SubTotalLineDetail",
      "Amount": 100.0,
      "SubTotalLineDetail": {}
    }
  ],
  "ApplyTaxAfterDiscount": false,
  "DocNumber": "1026",
  "sparse": false,
  "CustomerMemo": {
    "value": "Another memo update."
  },
  "ProjectRef": {
    "value": "39298045"
  },
  "Balance": 0,
  "CustomerRef": {
    "name": "Amy's Bird Sanctuary",
    "value": "1"
  },
  "TxnTaxDetail": {
    "TotalTax": 0
  },
  "SyncToken": "4",
  "CustomField": [
    {
      "DefinitionId": "1",
      "Type": "StringType",
      "Name": "Crew #"
    }
  ],
  "ShipAddr": {
    "CountrySubDivisionCode": "CA",
    "City": "Bayshore",
    "PostalCode": "94326",
    "Id": "108",
    "Line1": "4581 Finch St."
  },
  "EmailStatus": "NotSet",
  "BillAddr": {
    "Line4": "Bayshore, CA  94326",
    "Line3": "4581 Finch St.",
    "Id": "79",
    "Line1": "Amy Lauterbach",
    "Line2": "Amy's Bird Sanctuary"
  },
  "MetaData": {
    "CreateTime": "2014-09-18T12:51:27-07:00",
    "LastUpdatedTime": "2015-07-01T09:16:28-07:00"
  },
  "BillEmail": {
    "Address": "Birds@Intuit.com"
  },
  "Id": "73"
}
```

#### XML example

```xml
<CreditMemo xmlns="http://schema.intuit.com/finance/v3" sparse="false">
    <Id>73</Id>
    <SyncToken>3</SyncToken>
    <MetaData>
        <CreateTime>2014-09-18T12:51:27-07:00</CreateTime>
        <LastUpdatedTime>2015-07-01T09:16:28-07:00</LastUpdatedTime>
    </MetaData>
    <CustomField>
        <DefinitionId>1</DefinitionId>
        <Name>Crew #</Name>
        <Type>StringType</Type>
    </CustomField>
    <DocNumber>1026</DocNumber>
    <TxnDate>2014-09-02</TxnDate>
    <Line>
        <Id>1</Id>
        <LineNum>1</LineNum>
        <Description>Pest Control Services</Description>
        <Amount>100.00</Amount>
        <DetailType>SalesItemLineDetail</DetailType>
        <SalesItemLineDetail>
            <ItemRef name="Pest Control">10</ItemRef>
            <UnitPrice>100</UnitPrice>
            <Qty>1</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
        </SalesItemLineDetail>
    </Line>
    <Line>
        <Amount>100.00</Amount>
        <DetailType>SubTotalLineDetail</DetailType>
        <SubTotalLineDetail />
    </Line>
    <TxnTaxDetail>
        <TotalTax>0</TotalTax>
    </TxnTaxDetail>
    <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
    <ProjectRef>39298045</ProjectRef>
    <CustomerMemo>Memo change via update operation.</CustomerMemo>
    <BillAddr>
        <Id>79</Id>
        <Line1>Amy Lauterbach</Line1>
        <Line2>Amy's Bird Sanctuary</Line2>
        <Line3>4581 Finch St.</Line3>
        <Line4>Bayshore, CA 94326</Line4>
    </BillAddr>
    <ShipAddr>
        <Id>108</Id>
        <Line1>4581 Finch St.</Line1>
        <City>Bayshore</City>
        <CountrySubDivisionCode>CA</CountrySubDivisionCode>
        <PostalCode>94326</PostalCode>
    </ShipAddr>
    <TotalAmt>100.00</TotalAmt>
    <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
    <PrintStatus>NeedToPrint</PrintStatus>
    <EmailStatus>NotSet</EmailStatus>
    <BillEmail>
        <Address>Birds@Intuit.com</Address>
    </BillEmail>
    <Balance>0</Balance>
    <RemainingCredit>0</RemainingCredit>
</CreditMemo>
```

### Returns

The creditmemo response body.

#### Example

```json
{
  "CreditMemo": {
    "TxnDate": "2014-09-02",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "TotalAmt": 100.0,
    "RemainingCredit": 0,
    "Line": [
      {
        "Description": "Pest Control Services",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 1,
          "UnitPrice": 100,
          "ItemRef": {
            "name": "Pest Control",
            "value": "10"
          }
        },
        "LineNum": 1,
        "Amount": 100.0,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 100.0,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1026",
    "sparse": false,
    "CustomerMemo": {
      "value": "Another memo update."
    },
    "ProjectRef": {
      "value": "39298045"
    },
    "Balance": 0,
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "5",
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "ShipAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Bayshore",
      "PostalCode": "94326",
      "Id": "108",
      "Line1": "4581 Finch St."
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "Line4": "Bayshore, CA  94326",
      "Line3": "4581 Finch St.",
      "Id": "79",
      "Line1": "Amy Lauterbach",
      "Line2": "Amy's Bird Sanctuary"
    },
    "MetaData": {
      "CreateTime": "2014-09-18T12:51:27-07:00",
      "LastUpdatedTime": "2015-07-23T09:23:52-07:00"
    },
    "BillEmail": {
      "Address": "Birds@Intuit.com"
    },
    "Id": "73"
  },
  "time": "2015-07-23T09:23:52.115-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-23T09:19:58.180-07:00">
    <CreditMemo domain="QBO" sparse="false">
        <Id>73</Id>
        <SyncToken>4</SyncToken>
        <MetaData>
            <CreateTime>2014-09-18T12:51:27-07:00</CreateTime>
            <LastUpdatedTime>2015-07-23T09:19:58-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1026</DocNumber>
        <TxnDate>2014-09-02</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Pest Control Services</Description>
            <Amount>100.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Pest Control">10</ItemRef>
                <UnitPrice>100</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>100.00</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
        <ProjectRef>39298045</ProjectRef>
        <CustomerMemo>Memo change via update operation.</CustomerMemo>
        <BillAddr>
            <Id>79</Id>
            <Line1>Amy Lauterbach</Line1>
            <Line2>Amy's Bird Sanctuary</Line2>
            <Line3>4581 Finch St.</Line3>
            <Line4>Bayshore, CA 94326</Line4>
        </BillAddr>
        <ShipAddr>
            <Id>108</Id>
            <Line1>4581 Finch St.</Line1>
            <City>Bayshore</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94326</PostalCode>
        </ShipAddr>
        <TotalAmt>100.00</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <BillEmail>
            <Address>Birds@Intuit.com</Address>
        </BillEmail>
        <Balance>0</Balance>
        <RemainingCredit>0</RemainingCredit>
    </CreditMemo>
</IntuitResponse>
```
