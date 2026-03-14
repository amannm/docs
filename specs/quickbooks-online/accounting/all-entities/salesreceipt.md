# SalesReceipt

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/salesreceipt
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / SalesReceipt
> Canonical entity: `SalesReceipt`

A SalesReceipt object represents the sales receipt that is given to a customer. A sales receipt is similar to an invoice. However, for a sales receipt, payment is received as part of the sale of goods and services. The sales receipt specifies a deposit account where the customer's payment is deposited. If the deposit account is not specified, the Undeposited Account is used.

## The salesreceipt object

### salesreceiptresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of a transaction. Valid `Line` types include: `SalesItemLine`, `GroupLine`, `DescriptionOnlyLine`, `DiscountLine` and `SubTotalLine` (read-only). If the transaction is taxable there is a limit of 750 lines per transaction.

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

#### `ShipFromAddr`

Required: Conditionally required
Type: `PhysicalAddress`
Minor version: 35

Identifies the address where the goods are shipped from. For transactions without shipping, it represents the address where the sale took place.
If automated sales tax is enabled (`Preferences.TaxPrefs.PartnerTaxEnabled` is set to `true`) and automated tax calculations are being used, this field is required for an accurate sales tax calculation.
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
<summary>Child attributes for `ShipFromAddr`</summary>

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

Identifies the e-mail address where the invoice is sent. Required if `EmailStatus=NeedToSend`

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

Convenience field containing the amount in `Balance` expressed in terms of the home currency. Calculated by QuickBooks business logic. Value is valid only when `CurrencyRef` is specified and available when endpoint is evoked with the `minorversion=3` query parameter. Applicable if multicurrency is enabled for the company

#### `DeliveryInfo`

Type: `DeliveryInfo`
Traits: read only

Email delivery information. Returned when a request has been made to deliver email with the send operation.

<details>
<summary>Child attributes for `DeliveryInfo`</summary>

##### deliveryinfo

Model type: `object`

###### `DeliveryType`

Type: `DeliveryTypeEnum`
Traits: read only

Type of the delivery. Used to confirm that email has been sent via the send operation. Valid values currently include: `Email`.

###### `DeliveryTime`

Type: `DateTime`
Traits: read only

Delivery date and time.

<details>
<summary>Child attributes for `DeliveryTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

</details>

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `SalesReceipt` was created from.

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
Traits: read only, system defined, filterable

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks. If you process a linked refund transaction against a specific transaction, the `totalAmt` value won't change. It will remain the same. However, voiding the linked refund will change the `totalAmt` value to O.

#### `Balance`

Type: `Decimal`
Traits: read only, filterable, sortable

The balance reflecting any payments made against the transaction. Initially set to the value of `TotalAmt`. A Balance of 0 indicates the invoice is fully paid. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `HomeTotalAmt`

Type: `Decimal`
Traits: read only, system defined

Total amount of the transaction in the home currency. Includes the total of all the charges, allowances and taxes. Calculated by QuickBooks business logic. Value is valid only when `CurrencyRef` is specified. Applicable if multicurrency is enabled for the company

#### `FreeFormAddress`

Type: `Boolean`
Traits: system defined

Denotes how `ShipAddr` is stored: formatted or unformatted. The value of this flag is system defined based on format of shipping address at object create time.

- If set to `false`, shipping address is returned in a formatted style using City, Country, CountrySubDivisionCode, Postal code.
- If set to `true`, shipping address is returned in an unformatted style using Line1 through Line5 attributes.

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

#### `ShipDate`

Required: Optional
Type: `Date`

Location of the transaction, as defined using location tracking in QuickBooks Online.

<details>
<summary>Child attributes for `ShipDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `TrackingNum`

Required: Optional
Type: `String`

Shipping provider's tracking number for the delivery of the goods associated with the transaction.

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

#### `PrintStatus`

Required: Optional
Type: `String`
Default: <span class="literal">NotSet</span>

Printing status of the invoice. Valid values: `NotSet`, `NeedToPrint`, `PrintComplete`.

#### `PaymentRefNum`

Required: Optional
Type: `String`
Max length: Max 21 characters

The reference number for the payment received. For example, Â Check # for a check, envelope # for a cash donation.

#### `TxnSource`

Required: Optional
Type: `String`

Used internally to specify originating source of a credit card transaction.

#### `LinkedTxn [0..n]`

Required: Optional
Type: `LinkedTxn`

Zero or more related transactions to this sales receipt object. The following linked relationships are supported:

- Links to `Estimate` and `TimeActivity` objects can be established directly to this sales receipt object with UI or with the API. Create, Read, Update, and Query operations are avaialble at the API level for these types of links.
- Only one link can be made to an `Estimate`.
- Links to expenses incurred on behalf of the customer are returned in the response with `LinkedTxn.TxnType` set to `ReimburseCharge`, `ChargeCredit` or `StatementCharge` corresponding to billable customer expenses of type `Cash`, `Delayed Credit`, and `Delayed Charge`, respectively. Links to these types of transactions are established within the QuickBooks UI, only, and are available as read-only at the API level.
- Links to payments applied to an sales receipt object are returned in the response with `LinkedTxn.TxnType` set to `Payment`. Links to Payment transactions are established within the QuickBooks UI, only, and are available as read-only at the API level.
- Links the sales receipt to refundReceipt objects that are applied to the sales receipt. Returned in the response if `linkedTxnTxnType` is a refundReceipt. Note that linking sales receipts to refund receipts can only be done via the customer-facing QuickBooks UI. This is only available as read-only via our API

Use `LinkedTxn.TxnId` as the ID in a separate read request for the specific resource to retrieve details of the linked object.

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

#### `ApplyTaxAfterDiscount`

Required: Optional
Type: `Boolean`
Locales: US

If false or null, calculate the sales tax first, and then apply the discount. If true, subtract the discount first and then calculate the sales tax. Default Value: false Constraints: US versions of QuickBooks only.

#### `DocNumber`

Required: Optional
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 21 chars

Reference number for the transaction. If not explicitly provided at create time, this field is populated based on the setting of `Preferences:CustomTxnNumber` as follows:

If `Preferences:CustomTxnNumber` is true a custom value can be provided. If no value is supplied, the resulting DocNumber is null.

If `Preferences:CustomTxnNumber` is false, resulting DocNumber is system generated by incrementing the last number by 1.

If `Preferences:CustomTxnNumber` is false then do not send a value as it can lead to unwanted duplicates. If a DocNumber value is sent for an Update operation, then it just updates that particular invoice and does not alter the internal system DocNumber.
*Note:* DocNumber is an optional field for all locales except France. For France locale if `Preferences:CustomTxnNumber` is enabled it will **not** be automatically generated and is a required field.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: Max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the transaction form to the customer. This field maps to the Memo field on the Sales Receipt form.

#### `DepositToAccountRef`

Required: Optional
Type: `ReferenceType`

Account to which payment money is deposited. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType` is `Other Current Asset` or `Bank`. Use `Account.Id` and `Account.Name` from that object for `DepositToAccountRef.value` and `DepositToAccountRef.name`, respectively.
If you do not specify this account, payment is applied to the Undeposited Funds account.

<details>
<summary>Child attributes for `DepositToAccountRef`</summary>

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

#### `EmailStatus`

Required: Optional
Type: `String`

Email status of the receipt. Valid values: `NotSet`, `NeedToSend`, `EmailSent`.

#### `CreditCardPayment`

Required: Optional
Type: `CreditCardPayment`

Information about a credit card payment for the transaction. Used when PaymentType is `CreditCard`. Inject with data only if the payment was transacted through Intuit Payments API.

<details>
<summary>Child attributes for `CreditCardPayment`</summary>

##### creditcardpayment

Model type: `object`

###### `CreditChargeResponse`

Required: Optional
Type: `CreditChargeResponse`

Holds credit-card transaction response information from a merchant account service.

<details>
<summary>Child attributes for `CreditChargeResponse`</summary>

###### creditchargeresponse

Model type: `object`

###### `Status`

Required: Optional
Type: `CCPaymentStatusEnum`

Indicates the status of the payment transaction. Possible values include `Completed`, `Unknown`.

###### `AuthCode`

Required: Optional
Type: `String`
Max length: maximum 100 characters

Code returned from the credit card processor to indicate that the charge will be paid by the card issuer.

###### `TxnAuthorizationTime`

Required: Optional
Type: `DateTime`

Timestamp indicating the time in which the card processor authorized the transaction.

<details>
<summary>Child attributes for `TxnAuthorizationTime`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `CCTransId`

Required: Optional
Type: `String`
Max length: maximum 100 characters

Unique identifier of the payment transaction. It can be used to track the status of transactions, or to search transactions.

</details>

###### `CreditChargeInfo`

Required: Optional
Type: `CreditChargeInfo`

Holds creditcard information to request a credit card payment from a merchant account service.

<details>
<summary>Child attributes for `CreditChargeInfo`</summary>

###### creditchargeinfo

Model type: `object`

###### `CcExpiryMonth`

Required: Optional
Type: `Integer`

Expiration Month on card, expressed as a number: `1`=January, `2`=February, etc.

###### `ProcessPayment`

Required: Optional
Type: `Boolean`

-`false` or no value-Store credit card information only. Do not store QuickBooks Payment transaction information in CreditChargeResponse. -`true`-Store credit card payment transaction information in CreditChargeResponse below. Use this setting when QuickBooks Payments is configured to process credit card charges.

###### `PostalCode`

Required: Optional
Type: `String`
Max length: maximum 30 characters

Credit card holder billing postal code. Five digits in the USA.

###### `Amount`

Required: Optional
Type: `Decimal`

The amount processed using the credit card.

###### `NameOnAcct`

Required: Optional
Type: `String`

Account holder name, as printed on the card.

###### `CcExpiryYear`

Required: Optional
Type: `Integer`
Default: current year

Expiration Year on card, expressed as a 4 digit number `1999`, `2003`, etc.

###### `Type`

Required: Optional
Type: `String`

Type of credit card. For example, MasterCard, Visa, Discover, American Express, and so on.

###### `BillAddrStreet`

Required: Optional
Type: `String`
Max length: maximum 255 characters

Credit card holder billing address of record: the street address to which credit card statements are sent.

</details>

</details>

#### `TxnTaxDetail`

Required: Optional
Type: `TxnTaxDetail`

This element provides information for taxes charged on the transaction as a whole. It captures the details sales taxes calculated for the transaction based on the tax codes referenced by the transaction. This can be calculated by QuickBooks business logic or you may supply it when adding a transaction. See [Global tax model](https://developer.intuit.com/app/developer/qbo/docs/workflows/calculate-sales-tax/automated-sales-tax-for-non-us-locales) for more information about this element. If sales tax is disabled (`Preferences.TaxPrefs.UsingSalesTax` is set to `false`) then `TxnTaxDetail` is ignored and not stored.

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

#### `ShipMethodRef`

Required: Optional
Type: `ReferenceType`

Reference to the ShipMethod associated with the transaction. There is no shipping method list. Reference resolves to a string.

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

#### `BillAddr`

Required: Optional
Type: `PhysicalAddress`

Bill-to address of the Invoice. If `BillAddr`is not specified, and a default `Customer:BillingAddr` is specified in QuickBooks for this customer, the default bill-to address is used by QuickBooks.
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
  "SalesReceipt": {
    "TxnDate": "2014-09-14",
    "domain": "QBO",
    "PrintStatus": "NotSet",
    "PaymentRefNum": "10264",
    "TotalAmt": 337.5,
    "Line": [
      {
        "Description": "Custom Design",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 4.5,
          "UnitPrice": 75,
          "ItemRef": {
            "name": "Design",
            "value": "4"
          }
        },
        "LineNum": 1,
        "Amount": 337.5,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 337.5,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1003",
    "sparse": false,
    "DepositToAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "CustomerMemo": {
      "value": "Thank you for your business and have a great day!"
    },
    "ProjectRef": {
      "value": "39298243"
    },
    "Balance": 0,
    "CustomerRef": {
      "name": "Dylan Sollfrank",
      "value": "6"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "0",
    "PaymentMethodRef": {
      "name": "Check",
      "value": "2"
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "Lat": "INVALID",
      "Long": "INVALID",
      "Id": "49",
      "Line1": "Dylan Sollfrank"
    },
    "MetaData": {
      "CreateTime": "2014-09-16T14:59:48-07:00",
      "LastUpdatedTime": "2014-09-16T14:59:48-07:00"
    },
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "11"
  },
  "time": "2015-07-29T09:29:56.229-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-29T09:29:33.366-07:00">
    <SalesReceipt domain="QBO" sparse="false">
        <Id>11</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-16T14:59:48-07:00</CreateTime>
            <LastUpdatedTime>2014-09-16T14:59:48-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1003</DocNumber>
        <TxnDate>2014-09-14</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Custom Design</Description>
            <Amount>337.50</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Design">4</ItemRef>
                <UnitPrice>75</UnitPrice>
                <Qty>4.5</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>337.50</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Dylan Sollfrank">6</CustomerRef>
        <ProjectRef>39298234</ProjectRef>
        <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
        <BillAddr>
            <Id>49</Id>
            <Line1>Dylan Sollfrank</Line1>
            <Lat>INVALID</Lat>
            <Long>INVALID</Long>
        </BillAddr>
        <TotalAmt>337.50</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NotSet</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <Balance>0</Balance>
        <PaymentMethodRef name="Check">2</PaymentMethodRef>
        <PaymentRefNum>10264</PaymentRefNum>
        <DepositToAccountRef name="Checking">35</DepositToAccountRef>
    </SalesReceipt>
</IntuitResponse>
```

## Create a salesreceipt

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/salesreceipt`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- A SalesReceipt object must have at least one line that describes an item and an amount.

### Request Body

The minimum elements to create a salesreceipt are listed here.

Schema: `salesreceiptrequest`

<details>
<summary>Show schema for `salesreceiptrequest`</summary>

#### salesreceiptrequest

Model type: `object`

##### `Line [0..n]`

Required: Required

The minimum line item required for the request is one of the following: `SalesItemLine` and `GroupLine`

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

</details>

#### Example

```json
{
  "Line": [
    {
      "Description": "Pest Control Services",
      "DetailType": "SalesItemLineDetail",
      "SalesItemLineDetail": {
        "TaxCodeRef": {
          "value": "NON"
        },
        "Qty": 1,
        "UnitPrice": 35,
        "ItemRef": {
          "name": "Pest Control",
          "value": "10"
        }
      },
      "LineNum": 1,
      "Amount": 35.0,
      "Id": "1"
    }
  ]
}
```

#### XML example

```xml
<SalesReceipt xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Line>
        <Id>1</Id>
        <LineNum>1</LineNum>
        <Description>Pest Control Services</Description>
        <Amount>35.00</Amount>
        <DetailType>SalesItemLineDetail</DetailType>
        <SalesItemLineDetail>
            <ItemRef name="Pest Control">10</ItemRef>
            <UnitPrice>35</UnitPrice>
            <Qty>1</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
        </SalesItemLineDetail>
    </Line>
</SalesReceipt>
```

### Returns

The salesreceipt response body.

#### Example

```json
{
  "SalesReceipt": {
    "DocNumber": "1074",
    "SyncToken": "0",
    "domain": "QBO",
    "Balance": 0,
    "DepositToAccountRef": {
      "name": "Undeposited Funds",
      "value": "4"
    },
    "TxnDate": "2015-07-29",
    "TotalAmt": 35.0,
    "PrintStatus": "NeedToPrint",
    "EmailStatus": "NotSet",
    "sparse": false,
    "Line": [
      {
        "Description": "Pest Control Services",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 1,
          "UnitPrice": 35,
          "ItemRef": {
            "name": "Pest Control",
            "value": "10"
          }
        },
        "LineNum": 1,
        "Amount": 35.0,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 35.0,
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
    "Id": "263",
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "MetaData": {
      "CreateTime": "2015-07-29T09:25:02-07:00",
      "LastUpdatedTime": "2015-07-29T09:25:02-07:00"
    }
  },
  "time": "2015-07-29T09:25:04.214-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-29T09:26:40.184-07:00">
    <SalesReceipt domain="QBO" sparse="false">
        <Id>264</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-29T09:26:38-07:00</CreateTime>
            <LastUpdatedTime>2015-07-29T09:26:38-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1075</DocNumber>
        <TxnDate>2015-07-29</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Pest Control Services</Description>
            <Amount>35.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Pest Control">10</ItemRef>
                <UnitPrice>35</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>35.00</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <TotalAmt>35.00</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <Balance>0</Balance>
        <DepositToAccountRef name="Undeposited Funds">4</DepositToAccountRef>
    </SalesReceipt>
</IntuitResponse>
```

## Delete a salesreceipt

### Definition

- **Content type:** `application/json or application/xml`
- **Operation:** `POST /v3/company/<realmID>/salesreceipt?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the SalesReceipt object specified in the request body. Include a minimum of `SalesReceipt.Id` and `SalesReceipt.SyncToken` in the request body.

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
  "SyncToken": "1",
  "Id": "98"
}
```

#### XML example

```xml
<SalesReceipt xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
  <Id>3084</Id>
  <SyncToken>2</SyncToken>
</SalesReceipt>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "SalesReceipt": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "98"
  },
  "time": "2013-03-13T13:39:58.505-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T08:54:09.001-07:00">
  <SalesReceipt domain="QBO" status="Deleted">
    <Id>3084</Id>
  </SalesReceipt>
</IntuitResponse>
```

## Void a salesreceipt

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/salesreceipt?operation=update&include=void`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use a sparse update operation with `include=void` to void an existing SalesReceipt object; include a minimum of `SalesReceipt.Id` and `SalesReceipt.SyncToken`. The transaction remains active but all amounts and quantities are zeroed and the string, `Voided`, is injected into `SalesReceipt.PrivateNote`, prepended to existing text if present. If a sales receipt is paid and funds have been deposited, you must delete the associated deposit object before voiding the salesreceipt object.

### Request Body

Schema: `voidrequest`

<details>
<summary>Show schema for `voidrequest`</summary>

#### voidrequest

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

##### `sparse`

Required: Required
Type: `String`

Include and set to true to void an object.

</details>

#### Example

```json
{
  "SyncToken": "0",
  "Id": "161",
  "sparse": true
}
```

#### XML example

```xml
<SalesReceipt xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>38</Id>
    <SyncToken>0</SyncToken>
</SalesReceipt>
```

### Returns

The SalesReceipt response body.

#### Example

```json
{
  "SalesReceipt": {
    "TxnDate": "2014-12-31",
    "domain": "QBO",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "PrintStatus": "NeedToPrint",
    "TotalAmt": 0,
    "Line": [
      {
        "LineNum": 1,
        "Amount": 0,
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 0,
          "ItemRef": {
            "name": "Services",
            "value": "1"
          }
        },
        "Id": "1",
        "DetailType": "SalesItemLineDetail"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 0,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1038",
    "PrivateNote": "Voided",
    "sparse": false,
    "DepositToAccountRef": {
      "name": "Undeposited Funds",
      "value": "4"
    },
    "CustomerMemo": {
      "value": "Thank you for your business and have a great day!"
    },
    "ProjectRef": {
      "value": "39298243"
    },
    "Balance": 0,
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "1",
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
      "Id": "98",
      "Line1": "4581 Finch St."
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Bayshore",
      "PostalCode": "94326",
      "Id": "97",
      "Line1": "4581 Finch St."
    },
    "MetaData": {
      "CreateTime": "2014-12-31T16:17:23-08:00",
      "LastUpdatedTime": "2015-02-09T12:29:53-08:00"
    },
    "BillEmail": {
      "Address": "virti_vora@Intuit.com"
    },
    "Id": "161"
  },
  "time": "2015-02-09T12:29:52.970-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-02-09T12:25:12.488-08:00">
  <SalesReceipt domain="QBO" sparse="false">
    <Id>38</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2014-11-07T11:15:46-08:00</CreateTime>
      <LastUpdatedTime>2015-02-09T12:25:12-08:00</LastUpdatedTime>
    </MetaData>
    <CustomField>
      <DefinitionId>1</DefinitionId>
      <Name>Crew #</Name>
      <Type>StringType</Type>
    </CustomField>
    <DocNumber>1011</DocNumber>
    <TxnDate>2014-11-07</TxnDate>
    <PrivateNote>Voided</PrivateNote>
    <Line>
      <Id>1</Id>
      <LineNum>1</LineNum>
      <Description>Pest Control Services</Description>
      <Amount>0</Amount>
      <DetailType>SalesItemLineDetail</DetailType>
      <SalesItemLineDetail>
        <ItemRef name="Pest Control">10</ItemRef>
        <Qty>0</Qty>
        <TaxCodeRef>NON</TaxCodeRef>
      </SalesItemLineDetail>
    </Line>
    <Line>
      <Amount>0</Amount>
      <DetailType>SubTotalLineDetail</DetailType>
      <SubTotalLineDetail/>
    </Line>
    <TxnTaxDetail>
      <TotalTax>0</TotalTax>
    </TxnTaxDetail>
    <CustomerRef name="Pye's Cakes">15</CustomerRef>
    <ProjectRef>39298546</ProjectRef>
    <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
    <BillAddr>
      <Id>57</Id>
      <Line1>Karen Pye Pye's Cakes 350 Mountain View Dr. South Orange, NJ 07079</Line1>
    </BillAddr>
    <ShipAddr>
      <Id>96</Id>
      <Line1>350 Mountain View Dr.</Line1>
      <City>South Orange</City>
      <CountrySubDivisionCode>NJ</CountrySubDivisionCode>
      <PostalCode>07079</PostalCode>
    </ShipAddr>
    <TotalAmt>0</TotalAmt>
    <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
    <PrintStatus>NotSet</PrintStatus>
    <EmailStatus>NotSet</EmailStatus>
    <BillEmail>
      <Address>karen@pye.com</Address>
    </BillEmail>
    <Balance>0</Balance>
    <PaymentMethodRef name="Cash">1</PaymentMethodRef>
    <DepositToAccountRef name="Undeposited Funds">4</DepositToAccountRef>
  </SalesReceipt>
</IntuitResponse>
```

## Get a salesreceipt as PDF

### Definition

- **Content type:** `application/pdf`
- **Operation:** `GET /v3/company/<realmID>/salesreceipt/<salesreceiptId>/pdf`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Returns

This resource returns the specified object in the response body as an Adobe Portable Document Format (PDF) file. The resulting PDF file is formatted according to custom form styles in the company settings.

#### Example

```text
"%PDF-1.4\r\n...\r\n%%EOF"
```

#### XML example

_Binary response body omitted in the source payload._

## Query a salesreceipt

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from SalesReceipt where id='11'"
```

#### XML example

```sql
select * from SalesReceipt where id = '11'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "SalesReceipt": [
      {
        "TxnDate": "2014-09-14",
        "domain": "QBO",
        "PrintStatus": "NotSet",
        "PaymentRefNum": "10264",
        "TotalAmt": 337.5,
        "Line": [
          {
            "Description": "Custom Design",
            "DetailType": "SalesItemLineDetail",
            "SalesItemLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "Qty": 4.5,
              "UnitPrice": 75,
              "ItemRef": {
                "name": "Design",
                "value": "4"
              }
            },
            "LineNum": 1,
            "Amount": 337.5,
            "Id": "1"
          },
          {
            "DetailType": "SubTotalLineDetail",
            "Amount": 337.5,
            "SubTotalLineDetail": {}
          }
        ],
        "ApplyTaxAfterDiscount": false,
        "DocNumber": "1003",
        "sparse": false,
        "DepositToAccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "CustomerMemo": {
          "value": "Updated customer memo via sparse update operation."
        },
        "ProjectRef": {
          "value": "39298243"
        },
        "Balance": 0,
        "CustomerRef": {
          "name": "Dylan Sollfrank",
          "value": "6"
        },
        "TxnTaxDetail": {
          "TotalTax": 0
        },
        "SyncToken": "3",
        "PaymentMethodRef": {
          "name": "Check",
          "value": "2"
        },
        "EmailStatus": "NotSet",
        "BillAddr": {
          "Id": "122",
          "Line1": "Dylan Sollfrank"
        },
        "MetaData": {
          "CreateTime": "2014-09-16T14:59:48-07:00",
          "LastUpdatedTime": "2015-07-29T09:48:53-07:00"
        },
        "CustomField": [
          {
            "DefinitionId": "1",
            "Type": "StringType",
            "Name": "Crew #"
          }
        ],
        "Id": "11"
      }
    ],
    "startPosition": 1,
    "maxResults": 1
  },
  "time": "2015-07-29T09:50:39.882-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-29T09:51:09.514-07:00">
    <QueryResponse startPosition="1" maxResults="1">
        <SalesReceipt domain="QBO" sparse="false">
            <Id>11</Id>
            <SyncToken>3</SyncToken>
            <MetaData>
                <CreateTime>2014-09-16T14:59:48-07:00</CreateTime>
                <LastUpdatedTime>2015-07-29T09:48:53-07:00</LastUpdatedTime>
            </MetaData>
            <CustomField>
                <DefinitionId>1</DefinitionId>
                <Name>Crew #</Name>
                <Type>StringType</Type>
            </CustomField>
            <DocNumber>1003</DocNumber>
            <TxnDate>2014-09-14</TxnDate>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Description>Custom Design</Description>
                <Amount>337.50</Amount>
                <DetailType>SalesItemLineDetail</DetailType>
                <SalesItemLineDetail>
                    <ItemRef name="Design">4</ItemRef>
                    <UnitPrice>75</UnitPrice>
                    <Qty>4.5</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                </SalesItemLineDetail>
            </Line>
            <Line>
                <Amount>337.50</Amount>
                <DetailType>SubTotalLineDetail</DetailType>
                <SubTotalLineDetail />
            </Line>
            <TxnTaxDetail>
                <TotalTax>0</TotalTax>
            </TxnTaxDetail>
            <CustomerRef name="Dylan Sollfrank">6</CustomerRef>
            <ProjectRef>39298234</ProjectRef>
            <CustomerMemo>Updated customer memo via sparse update operation.</CustomerMemo>
            <BillAddr>
                <Id>122</Id>
                <Line1>Dylan Sollfrank</Line1>
            </BillAddr>
            <TotalAmt>337.50</TotalAmt>
            <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
            <PrintStatus>NotSet</PrintStatus>
            <EmailStatus>NotSet</EmailStatus>
            <Balance>0</Balance>
            <PaymentMethodRef name="Check">2</PaymentMethodRef>
            <PaymentRefNum>10264</PaymentRefNum>
            <DepositToAccountRef name="Checking">35</DepositToAccountRef>
        </SalesReceipt>
    </QueryResponse>
</IntuitResponse>
```

## Read a salesreceipt

### Definition

- **Operation:** `GET /v3/company/<realmID>/salesreceipt/<salesreceiptId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a SalesReceipt object that has been previously created.

### Returns

The salesreceipt response body.

#### Example

```json
{
  "SalesReceipt": {
    "TxnDate": "2014-09-14",
    "domain": "QBO",
    "PrintStatus": "NotSet",
    "PaymentRefNum": "10264",
    "TotalAmt": 337.5,
    "Line": [
      {
        "Description": "Custom Design",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 4.5,
          "UnitPrice": 75,
          "ItemRef": {
            "name": "Design",
            "value": "4"
          }
        },
        "LineNum": 1,
        "Amount": 337.5,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 337.5,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1003",
    "sparse": false,
    "DepositToAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "CustomerMemo": {
      "value": "Thank you for your business and have a great day!"
    },
    "ProjectRef": {
      "value": "39298243"
    },
    "Balance": 0,
    "CustomerRef": {
      "name": "Dylan Sollfrank",
      "value": "6"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "0",
    "PaymentMethodRef": {
      "name": "Check",
      "value": "2"
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "Lat": "INVALID",
      "Long": "INVALID",
      "Id": "49",
      "Line1": "Dylan Sollfrank"
    },
    "MetaData": {
      "CreateTime": "2014-09-16T14:59:48-07:00",
      "LastUpdatedTime": "2014-09-16T14:59:48-07:00"
    },
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "11"
  },
  "time": "2015-07-29T09:29:56.229-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-29T09:29:33.366-07:00">
    <SalesReceipt domain="QBO" sparse="false">
        <Id>11</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-16T14:59:48-07:00</CreateTime>
            <LastUpdatedTime>2014-09-16T14:59:48-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1003</DocNumber>
        <TxnDate>2014-09-14</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Custom Design</Description>
            <Amount>337.50</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Design">4</ItemRef>
                <UnitPrice>75</UnitPrice>
                <Qty>4.5</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>337.50</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Dylan Sollfrank">6</CustomerRef>
        <ProjectRef>39298234</ProjectRef>
        <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
        <BillAddr>
            <Id>49</Id>
            <Line1>Dylan Sollfrank</Line1>
            <Lat>INVALID</Lat>
            <Long>INVALID</Long>
        </BillAddr>
        <TotalAmt>337.50</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NotSet</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <Balance>0</Balance>
        <PaymentMethodRef name="Check">2</PaymentMethodRef>
        <PaymentRefNum>10264</PaymentRefNum>
        <DepositToAccountRef name="Checking">35</DepositToAccountRef>
    </SalesReceipt>
</IntuitResponse>
```

## Send a salesreceipt

### Definition

- **Content type:** `application/octet-stream`
- **Operation:** `POST /v3/company/<realmID>/salesreceipt/<salesreceiptId>/send
POST /v3/company/<realmID>/salesreceipt/<salesreceiptId>/send?sendTo=<emailAddr>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- The `SalesReceipt.EmailStatus` parameter is set to `EmailSent`.
- The `SalesReceipt.DeliveryInfo` element is populated with sending information.
- The `SalesReceipt.BillEmail.Address` parameter is updated to the address specified with the value of the `sendTo` query parameter, if specified.

### Returns

The salereceipt response body.

#### Example

```json
{
  "SalesReceipt": {
    "DocNumber": "1047",
    "SyncToken": "0",
    "domain": "QBO",
    "Balance": 0,
    "DepositToAccountRef": {
      "name": "Undeposited Funds",
      "value": "4"
    },
    "TxnDate": "2013-03-13",
    "TotalAmt": 5,
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "ProjectRef": {
      "value": "39298243"
    },
    "PrivateNote": "Memo for SalesReceipt",
    "PrintStatus": "NeedToPrint",
    "DepartmentRef": {
      "name": "Department1",
      "value": "1"
    },
    "DeliveryInfo": {
      "DeliveryType": "Email",
      "DeliveryTime": "2014-12-17T11:50:52-08:00"
    },
    "EmailStatus": "EmailSent",
    "sparse": false,
    "Line": [
      {
        "Description": "123189403765",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 10,
          "UnitPrice": 0.5,
          "ItemRef": {
            "name": "Sales",
            "value": "1"
          }
        },
        "LineNum": 1,
        "Amount": 5,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 5,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "CustomField": [
      {
        "Type": "StringType",
        "Name": "Custom 1"
      },
      {
        "Type": "StringType",
        "Name": "Custom 2"
      },
      {
        "Type": "StringType",
        "Name": "Custom 3"
      }
    ],
    "Id": "97",
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "MetaData": {
      "CreateTime": "2013-03-13T13:31:43-07:00",
      "LastUpdatedTime": "2014-12-17T11:50:54-08:00"
    }
  },
  "time": "2013-03-13T13:31:42.956-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T08:54:06.917-07:00">
    <SalesReceipt domain="QBO" sparse="false">
        <Id>3084</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2013-04-23T08:53:46-07:00</CreateTime>
            <LastUpdatedTime>2014-11-19T11:56:30-08:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <Name>Custom 1</Name>
            <Type>StringType</Type>
        </CustomField>
        <CustomField>
            <Name>Custom 2</Name>
            <Type>StringType</Type>
        </CustomField>
        <CustomField>
            <Name>Custom 3</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>3026</DocNumber>
        <TxnDate>2012-12-18</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <PrivateNote>Customer Sales Receipt</PrivateNote>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Sales only</Description>
            <Amount>5.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Sales">1</ItemRef>
                <UnitPrice>0.5</UnitPrice>
                <Qty>10</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>5.00</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail/>
        </Line>
        <Line>
            <Amount>0.50</Amount>
            <DetailType>DiscountLineDetail</DetailType>
            <DiscountLineDetail>
                <PercentBased>true</PercentBased>
                <DiscountPercent>10</DiscountPercent>
                <DiscountAccountRef name="Discounts given">30</DiscountAccountRef>
            </DiscountLineDetail>
        </Line>
        <TxnTaxDetail>
            <TxnTaxCodeRef>9</TxnTaxCodeRef>
            <TotalTax>0.75</TotalTax>
            <TaxLine>
                <Amount>0.75</Amount>
                <DetailType>TaxLineDetail</DetailType>
                <TaxLineDetail>
                    <TaxRateRef>18</TaxRateRef>
                    <PercentBased>true</PercentBased>
                    <TaxPercent>15</TaxPercent>
                    <NetAmountTaxable>5.00</NetAmountTaxable>
                </TaxLineDetail>
            </TaxLine>
        </TxnTaxDetail>
        <CustomerRef name="sn71lPmH0Y zOv1blD5Vq">1105</CustomerRef>
        <ProjectRef>39298546</ProjectRef>
        <CustomerMemo>Sales Receipt with customer</CustomerMemo>
        <BillAddr>
            <Id>65</Id>
            <Line1>2500 Garcia Avenue</Line1>
            <City>Mountain View</City>
            <Country>USA</Country>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94043</PostalCode>
            <Lat>37.428314</Lat>
            <Long>-122.0961024</Long>
        </BillAddr>
        <ShipAddr>
            <Id>66</Id>
            <Line1>Ms. Anupama Madhavapeddi</Line1>
            <Line2>Intuit Systems</Line2>
            <Line3>3400 Garcia Avenue</Line3>
            <Line4>Mountain View, CA 94043 USA</Line4>
            <Lat>37.428434</Lat>
            <Long>-122.0723816</Long>
        </ShipAddr>
        <ShipDate>2012-04-18</ShipDate>
        <TrackingNum>1232</TrackingNum>
        <TotalAmt>5.25</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NotSet</PrintStatus>
        <EmailStatus>EmailSent</EmailStatus>
        <BillEmail>
            <Address>test@abc.com</Address>
        </BillEmail>
        <DeliveryInfo>
            <DeliveryType>Email</DeliveryType>
            <DeliveryTime>2014-11-19T11:56:28-08:00</DeliveryTime>
        </DeliveryInfo>
        <Balance>0</Balance>
        <DepositToAccountRef name="Undeposited Funds">4</DepositToAccountRef>
    </SalesReceipt>
</IntuitResponse>
```

## Full update a salesreceipt

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/salesreceipt`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing SalesReceipt object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `salesreceiptresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "TxnDate": "2014-09-14",
  "domain": "QBO",
  "PrintStatus": "NotSet",
  "PaymentRefNum": "10264",
  "TotalAmt": 337.5,
  "Line": [
    {
      "Description": "Custom Design",
      "DetailType": "SalesItemLineDetail",
      "SalesItemLineDetail": {
        "TaxCodeRef": {
          "value": "NON"
        },
        "Qty": 4.5,
        "UnitPrice": 75,
        "ItemRef": {
          "name": "Design",
          "value": "4"
        }
      },
      "LineNum": 1,
      "Amount": 337.5,
      "Id": "1"
    },
    {
      "DetailType": "SubTotalLineDetail",
      "Amount": 337.5,
      "SubTotalLineDetail": {}
    }
  ],
  "ApplyTaxAfterDiscount": false,
  "DocNumber": "1003",
  "sparse": false,
  "DepositToAccountRef": {
    "name": "Checking",
    "value": "35"
  },
  "CustomerMemo": {
    "value": "An updated customer memo."
  },
  "ProjectRef": {
    "value": "39298243"
  },
  "Balance": 0,
  "CustomerRef": {
    "name": "Dylan Sollfrank",
    "value": "6"
  },
  "TxnTaxDetail": {
    "TotalTax": 0
  },
  "SyncToken": "0",
  "PaymentMethodRef": {
    "name": "Check",
    "value": "2"
  },
  "EmailStatus": "NotSet",
  "BillAddr": {
    "Lat": "INVALID",
    "Long": "INVALID",
    "Id": "49",
    "Line1": "Dylan Sollfrank"
  },
  "MetaData": {
    "CreateTime": "2014-09-16T14:59:48-07:00",
    "LastUpdatedTime": "2014-09-16T14:59:48-07:00"
  },
  "CustomField": [
    {
      "DefinitionId": "1",
      "Type": "StringType",
      "Name": "Crew #"
    }
  ],
  "Id": "11"
}
```

#### XML example

```xml
<SalesReceipt xmlns="http://schema.intuit.com/finance/v3" sparse="false">
    <Id>3084</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
        <CreateTime>2013-04-23T08:53:46-07:00</CreateTime>
        <LastUpdatedTime>2013-04-23T08:53:46-07:00</LastUpdatedTime>
    </MetaData>
    <PrivateNote>Sales Receipt Update testing</PrivateNote>
    <Line>
        <Id>1</Id>
        <Description>Sales only</Description>
        <Amount>5.00</Amount>
        <DetailType>SalesItemLineDetail</DetailType>
        <SalesItemLineDetail>
            <ItemRef name="Services">1</ItemRef>
            <UnitPrice>0.5</UnitPrice>
            <Qty>10</Qty>
            <TaxCodeRef>TAX</TaxCodeRef>
        </SalesItemLineDetail>
    </Line>
    <Line>
        <Amount>5.00</Amount>
        <DetailType>SubTotalLineDetail</DetailType>
        <SubTotalLineDetail/>
    </Line>
    <Line>
        <Amount>0.50</Amount>
        <DetailType>DiscountLineDetail</DetailType>
        <DiscountLineDetail>
            <PercentBased>true</PercentBased>
            <DiscountPercent>10</DiscountPercent>
        </DiscountLineDetail>
    </Line>
    <TxnTaxDetail>
        <TxnTaxCodeRef>9</TxnTaxCodeRef>
        <TotalTax>0.75</TotalTax>
        <TaxLine>
            <Amount>0.75</Amount>
            <DetailType>TaxLineDetail</DetailType>
            <TaxLineDetail>
                <TaxRateRef>18</TaxRateRef>
                <PercentBased>true</PercentBased>
                <TaxPercent>15</TaxPercent>
                <NetAmountTaxable>5.00</NetAmountTaxable>
            </TaxLineDetail>
        </TaxLine>
    </TxnTaxDetail>
    <CustomerRef>1105</CustomerRef>
    <ProjectRef>39298546</ProjectRef>
    <CustomerMemo>Sales Receipt with customer</CustomerMemo>
    <BillAddr>
        <Line1>2700 Garcia Avenue</Line1>
        <City>Mountain View</City>
        <Country>USA</Country>
        <CountrySubDivisionCode>CA</CountrySubDivisionCode>
        <PostalCode>94043</PostalCode>
    </BillAddr>
    <ShipAddr>
        <Line1>Ms. Anupama Madhavapeddi</Line1>
        <Line2>Intuit Systems</Line2>
        <Line3>3700 Garcia Avenue</Line3>
        <Line4>Mountain View, CA 94043 USA</Line4>
    </ShipAddr>
    <ShipDate>2012-04-18</ShipDate>
    <TrackingNum>1232</TrackingNum>
    <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
    <PrintStatus>NeedToPrint</PrintStatus>
    <EmailStatus>NeedToSend</EmailStatus>
    <BillEmail>
        <Address>test@abc.com</Address>
    </BillEmail>
    <Balance>0</Balance>
</SalesReceipt>
```

### Returns

The salesreceipt response body.

#### Example

```json
{
  "SalesReceipt": {
    "TxnDate": "2014-09-14",
    "domain": "QBO",
    "PrintStatus": "NotSet",
    "PaymentRefNum": "10264",
    "TotalAmt": 337.5,
    "Line": [
      {
        "Description": "Custom Design",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 4.5,
          "UnitPrice": 75,
          "ItemRef": {
            "name": "Design",
            "value": "4"
          }
        },
        "LineNum": 1,
        "Amount": 337.5,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 337.5,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1003",
    "sparse": false,
    "DepositToAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "CustomerMemo": {
      "value": "An updated customer memo."
    },
    "ProjectRef": {
      "value": "39298243"
    },
    "Balance": 0,
    "CustomerRef": {
      "name": "Dylan Sollfrank",
      "value": "6"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "1",
    "PaymentMethodRef": {
      "name": "Check",
      "value": "2"
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "Lat": "INVALID",
      "Long": "INVALID",
      "Id": "49",
      "Line1": "Dylan Sollfrank"
    },
    "MetaData": {
      "CreateTime": "2014-09-16T14:59:48-07:00",
      "LastUpdatedTime": "2015-07-29T09:43:18-07:00"
    },
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "11"
  },
  "time": "2015-07-29T09:43:01.436-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T08:54:07.001-07:00">
  <SalesReceipt domain="QBO" sparse="false">
    <Id>3084</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2013-04-23T08:53:46-07:00</CreateTime>
      <LastUpdatedTime>2013-04-23T08:53:47-07:00</LastUpdatedTime>
    </MetaData>
    <CustomField>
      <Name>Custom 1</Name>
      <Type>StringType</Type>
    </CustomField>
    <CustomField>
      <Name>Custom 2</Name>
      <Type>StringType</Type>
    </CustomField>
    <CustomField>
      <Name>Custom 3</Name>
      <Type>StringType</Type>
    </CustomField>
    <DocNumber>3026</DocNumber>
    <TxnDate>2012-12-18</TxnDate>
    <CurrencyRef name="United States Dollar">USD</CurrencyRef>
    <PrivateNote>Sales Receipt Update testing</PrivateNote>
    <Line>
      <Id>1</Id>
      <LineNum>1</LineNum>
      <Description>Sales only</Description>
      <Amount>5.00</Amount>
      <DetailType>SalesItemLineDetail</DetailType>
      <SalesItemLineDetail>
        <ItemRef name="Sales">1</ItemRef>
        <UnitPrice>0.5</UnitPrice>
        <Qty>10</Qty>
        <TaxCodeRef>TAX</TaxCodeRef>
      </SalesItemLineDetail>
    </Line>
    <Line>
      <Amount>5.00</Amount>
      <DetailType>SubTotalLineDetail</DetailType>
      <SubTotalLineDetail/>
    </Line>
    <Line>
      <Amount>0.50</Amount>
      <DetailType>DiscountLineDetail</DetailType>
      <DiscountLineDetail>
        <PercentBased>true</PercentBased>
        <DiscountPercent>10</DiscountPercent>
        <DiscountAccountRef name="Discounts given">30</DiscountAccountRef>
      </DiscountLineDetail>
    </Line>
    <TxnTaxDetail>
      <TxnTaxCodeRef>9</TxnTaxCodeRef>
      <TotalTax>0.75</TotalTax>
      <TaxLine>
        <Amount>0.75</Amount>
        <DetailType>TaxLineDetail</DetailType>
        <TaxLineDetail>
          <TaxRateRef>18</TaxRateRef>
          <PercentBased>true</PercentBased>
          <TaxPercent>15</TaxPercent>
          <NetAmountTaxable>5.00</NetAmountTaxable>
        </TaxLineDetail>
      </TaxLine>
    </TxnTaxDetail>
    <CustomerRef name="sn71lPmH0Y zOv1blD5Vq">1105</CustomerRef>
    <ProjectRef>39298546</ProjectRef>
    <CustomerMemo>Sales Receipt with customer</CustomerMemo>
    <BillAddr>
      <Id>65</Id>
      <Line1>2700 Garcia Avenue</Line1>
      <City>Mountain View</City>
      <Country>USA</Country>
      <CountrySubDivisionCode>CA</CountrySubDivisionCode>
      <PostalCode>94043</PostalCode>
      <Lat>37.4276176</Lat>
      <Long>-122.099344</Long>
    </BillAddr>
    <ShipAddr>
      <Id>66</Id>
      <Line1>Ms. Anupama Madhavapeddi</Line1>
      <Line2>Intuit Systems</Line2>
      <Line3>3700 Garcia Avenue</Line3>
      <Line4>Mountain View, CA 94043 USA</Line4>
      <Lat>37.428434</Lat>
      <Long>-122.0723816</Long>
    </ShipAddr>
    <ShipDate>2012-04-18</ShipDate>
    <TrackingNum>1232</TrackingNum>
    <TotalAmt>5.25</TotalAmt>
    <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
    <PrintStatus>NeedToPrint</PrintStatus>
    <EmailStatus>NeedToSend</EmailStatus>
    <BillEmail>
      <Address>test@abc.com</Address>
    </BillEmail>
    <Balance>0</Balance>
    <DepositToAccountRef name="Undeposited Funds">4</DepositToAccountRef>
  </SalesReceipt>
</IntuitResponse>
```

## Sparse update a salesreceipt

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/salesreceipt`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Sparse updating provides the ability to update a subset of properties for a given object; only elements specified in the request are updated. Missing elements are left untouched. The ID of the object to update is specified in the request body.​

### Request Body

Schema: `salesreceiptresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "Line": [
    {
      "DetailType": "SalesItemLineDetail",
      "Amount": 5,
      "Description": "UpdatedDescription",
      "SalesItemLineDetail": {
        "Qty": 10,
        "UnitPrice": 0.5,
        "ItemRef": {
          "value": "1"
        }
      }
    }
  ],
  "Id": "97",
  "sparse": true,
  "MetaData": {
    "CreateTime": "2013-03-13T13:39:57-07:00",
    "LastUpdatedTime": "2013-03-13T13:39:57-07:00"
  }
}
```

#### XML example

```xml
<SalesReceipt xmlns="http://schema.intuit.com/finance/v3" sparse="true">
    <Id>11</Id>
    <SyncToken>3</SyncToken>
    <MetaData>
        <CreateTime>2014-09-16T14:59:48-07:00</CreateTime>
        <LastUpdatedTime>2014-09-16T14:59:48-07:00</LastUpdatedTime>
    </MetaData>
    <Line>
        <Id>1</Id>
        <LineNum>1</LineNum>
        <Description>Custom Design</Description>
        <Amount>337.50</Amount>
        <DetailType>SalesItemLineDetail</DetailType>
        <SalesItemLineDetail>
            <ItemRef name="Design">4</ItemRef>
            <UnitPrice>75</UnitPrice>
            <Qty>4.5</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
        </SalesItemLineDetail>
    </Line>
    <CustomerMemo>Updated customer memo via sparse update operation.</CustomerMemo>
</SalesReceipt>
```

### Returns

The salesreceipt response body.

#### Example

```json
{
  "SalesReceipt": {
    "DocNumber": "1003",
    "SyncToken": "2",
    "domain": "QBO",
    "Balance": 0,
    "DepositToAccountRef": {
      "name": "Undeposited Funds",
      "value": "4"
    },
    "TxnDate": "2015-07-29",
    "TotalAmt": 337.5,
    "CustomerMemo": {
      "value": "A sparsely updated customer memo."
    },
    "PrintStatus": "NeedToPrint",
    "EmailStatus": "NotSet",
    "sparse": false,
    "Line": [
      {
        "Description": "Custom Design",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 4.5,
          "UnitPrice": 75,
          "ItemRef": {
            "name": "Design",
            "value": "4"
          }
        },
        "LineNum": 1,
        "Amount": 337.5,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 337.5,
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
    "Id": "11",
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "MetaData": {
      "CreateTime": "2014-09-16T14:59:48-07:00",
      "LastUpdatedTime": "2015-07-29T09:45:55-07:00"
    }
  },
  "time": "2015-07-29T09:45:39.381-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-29T09:49:20.113-07:00">
    <SalesReceipt domain="QBO" sparse="false">
        <Id>11</Id>
        <SyncToken>3</SyncToken>
        <MetaData>
            <CreateTime>2014-09-16T14:59:48-07:00</CreateTime>
            <LastUpdatedTime>2015-07-29T09:48:53-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1003</DocNumber>
        <TxnDate>2014-09-14</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Custom Design</Description>
            <Amount>337.50</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Design">4</ItemRef>
                <UnitPrice>75</UnitPrice>
                <Qty>4.5</Qty>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>337.50</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Dylan Sollfrank">6</CustomerRef>
        <ProjectRef>39298546</ProjectRef>
        <CustomerMemo>Updated customer memo via sparse update operation.</CustomerMemo>
        <BillAddr>
            <Id>122</Id>
            <Line1>Dylan Sollfrank</Line1>
        </BillAddr>
        <TotalAmt>337.50</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NotSet</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <Balance>0</Balance>
        <PaymentMethodRef name="Check">2</PaymentMethodRef>
        <PaymentRefNum>10264</PaymentRefNum>
        <DepositToAccountRef name="Checking">35</DepositToAccountRef>
    </SalesReceipt>
</IntuitResponse>
```
