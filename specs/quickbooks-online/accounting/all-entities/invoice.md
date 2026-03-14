# Invoice

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Invoice
> Canonical entity: `Invoice`

An Invoice represents a sales form where the customer pays for a product or service later.

### Business Rules

- An invoice must have at least one `Line` for either a sales item or an inline subtotal.
- An invoice must have `CustomerRef` populated.
- The `DocNumber` attribute is populated automatically by the data service if not supplied.
- If `ShipAddr`, `BillAddr`, or both are not provided, the appropriate customer address from the referenced Customer object is used to fill those values.
- If you have a large number of invoice and corresponding payment records that you wish to import to the QuickBooks Online company, sort the invoice and payment records in chronological order and use the batch resource to send invoice and payments batches of 10, one after the other, to ensure any open invoices get credited with their payments.
- If an invoice is taxable, there is a limit of 750 lines per invoice.

## The invoice object

### invoiceresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items of a transaction. Valid `Line` types include `SalesItemLine`, `GroupLine`, `DescriptionOnlyLine` (also used for inline Subtotal lines), `DiscountLine` and `SubTotalLine` (used for the overall transaction). If the transaction is taxable there is a limit of 750 lines per transaction.

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

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company. Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Applicable if multicurrency is enabled for the company.

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

#### `DocNumber`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 21 chars

Reference number for the transaction. If not explicitly provided at create time, this field is populated based on the setting of `Preferences:CustomTxnNumber` as follows:

If `Preferences:CustomTxnNumber` is true a custom value can be provided. If no value is supplied, the resulting DocNumber is null.

If `Preferences:CustomTxnNumber` is false, resulting DocNumber is system generated by incrementing the last number by 1.

If `Preferences:CustomTxnNumber` is false then do not send a value as it can lead to unwanted duplicates. If a DocNumber value is sent for an Update operation, then it just updates that particular invoice and does not alter the internal system DocNumber.
*Note:* DocNumber is an optional field for all locales except France. For France locale if `Preferences:CustomTxnNumber` is enabled it will **not** be automatically generated and is a required field. If a duplicate DocNumber needs to be supplied, add the query parameter name/value pair, `include=allowduplicatedocnum` to the URI.

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

Identifies the e-mail address where the invoice is sent. If `EmailStatus=NeedToSend`, `BillEmail`is a required input.

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

#### `TotalAmt`

Type: `BigDecimal`
Traits: read only, system defined

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `InvoiceLink`

Type: `String`
Traits: read only, system defined
Minor version: 36

Sharable link for the invoice sent to external customers. The link is generated only for invoices with online payment enabled and having a valid customer email address. Include query param `include=invoiceLink` to get the link back on query response.

#### `RecurDataRef`

Type: `ReferenceType`
Traits: read only
Minor version: 52

A reference to the Recurring Transaction. It captures what recurring transaction template the `Invoice` was created from.

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

For internal use only

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

The balance reflecting any payments made against the transaction. Initially set to the value of `TotalAmt`. A Balance of 0 indicates the invoice is fully paid. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks. If you process a linked transaction against a specific transaction, the `balance` value won't change. It will remain the same.

#### `HomeTotalAmt`

Type: `Decimal`
Traits: read only, system defined

Total amount of the transaction in the home currency. Includes the total of all the charges, allowances and taxes. Calculated by QuickBooks business logic. Value is valid only when `CurrencyRef` is specified. Applicable if multicurrency is enabled for the company.

#### `FreeFormAddress`

Type: `Boolean`
Traits: system defined

Denotes how `ShipAddr` is stored: formatted or unformatted. The value of this flag is system defined based on format of shipping address at object create time.

- If set to `false`, shipping address is returned in a formatted style using City, Country, CountrySubDivisionCode, Postal code.
- If set to `true`, shipping address is returned in an unformatted style using Line1 through Line5 attributes.

#### `AllowOnlinePayment`

Type: `Boolean`
Traits: deprecated

Deprecated flag to allow online payments. In use before `AllowOnlineCreditCardPayment` and `AllowOnlineACHPayment` flags existed and provided to maintain backward compatibility.

If set to `true`, this invoice was created before `AllowOnlinePayment` was deprecated and denotes both CC and ACH payments are allowed. In addition, the `AllowOnlineCreditCardPayment` and `AllowOnlineACHPayment` flags must be set to `true`.

If set to `false`, this invoice was created after the `AllowOnlinePayment` flag was deprecated and is not used.

Do not modify.

#### `AllowIPNPayment`

Type: `Boolean`
Traits: deprecated

Flag to allow payments from legacy Intuit Payment Network (IPN). Provided to maintain backward compatibility and must always be set to `false`. Do not modify

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: current server date

The date entered by the user when this transaction occurred.

- *yyyy/MM/dd* is the valid date format.
- For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.
- Sort order is ASC by default.

#### `ShipDate`

Required: Optional
Type: `Date`

Date for delivery of goods or services.

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

#### `TxnSource`

Required: Optional
Type: `String`

Used internally to specify originating source of a credit card transaction.

#### `LinkedTxn [0..n]`

Required: Optional
Type: `LinkedTxn`

Zero or more related transactions to this Invoice object. The following linked relationships are supported:

- Links to `Estimate` and `TimeActivity` objects can be established directly to this Invoice object with UI or with the API. Create, Read, Update, and Query operations are avaialble at the API level for these types of links.
- Only one link can be made to an `Estimate`. Progress Invoicing is not supported via the API.
- Links to expenses incurred on behalf of the customer are returned in the response with `LinkedTxn.TxnType` set to `ReimburseCharge`, `ChargeCredit` or `StatementCharge` corresponding to billable customer expenses of type `Cash`, `Delayed Credit`, and `Delayed Charge`, respectively. Links to these types of transactions are established within the QuickBooks UI, only, and are available as read-only at the API level.
- Links to payments applied to an Invoice object are returned in the response with `LinkedTxn.TxnType` set to `Payment`. Links to Payment transactions are established within the QuickBooks UI, only, and are available as read-only at the API level.

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

#### `DepositToAccountRef`

Required: Optional
Type: `ReferenceType`

Account to which money is deposited. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType` is `Other Current Asset` or `Bank`. Use `Account.Id` and `Account.Name` from that object for `DepositToAccountRef.value` and `DepositToAccountRef.name`, respectively.
Before you can use this field ensure that the company allows deposits in their invoices first. This can be found by querying the [Preferences endpoint](preferences.md). `SalesFormsPrefs.AllowDeposit` must be equal to true. If you do not specify this account the payment is applied to the Undeposited Funds account.

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

#### `AllowOnlineACHPayment`

Required: Optional
Type: `Boolean`
Default: <span class="literal">false</span>
Locales: US

Specifies if this invoice can be paid with online bank transfers and corresponds to the **Bank transfer** check box on the QuickBooks UI. Active when the company is payments-enabled, i.e., `Preferences.SalesFormsPrefs.ETransactionPaymentEnabled` is set to `true`.

If set to `true`, allow invoice to be paid with online bank transfers. The **Bank transfer** check box is checked on the QuickBooks UI for this invoice. True by default if the company allows invoices to be paid with ACH.

If set to `false`, online bank transfers are not allowed. The **Bank transfer** check box is not checked on the QuickBooks UI for this invoice.

#### `TransactionLocationType`

Required: Optional
Type: `String`
Default: <span class="literal">WithinFrance</span>
Minor version: 4
Locales: FR, IN, UAE

The account location. For France locale valid values include:

- `WithinFrance`
- `FranceOverseas`
- `OutsideFranceWithEU`
- `OutsideEU`

For UAE, valid values include

- `ABUDHABI`
- `AJMAN`
- `SHARJAH`
- `DUBAI`
- `FUJAIRAH`
- `RAS_AL_KHAIMAH`
- `UMM_AL_QUWAIN`
- `OTHER_GCC`

For India locale, use state code values from the list below:

<details>
<summary>Show valid values</summary>

#### ATTRIBUTES

| Name | Description |
| --- | --- |
| **STATE** | **STATECODE VALUE** |
| ANDAMAN_AND_NICOBAR_ISLANDS | 35 |
| ANDHRA_PRADESH | 37 |
| ARUNACHAL_PRADESH | 12 |
| ASSAM | 18 |
| BIHAR | 10 |
| CHANDIGARH | 04 |
| CHHATTISGARH | 22 |
| DADRA_AND_NAGAR_HAVELI | 26 |
| DAMAN_AND_DIU | 25 |
| DELHI | 07 |
| GOA | 30 |
| GUJARAT | 24 |
| HARYANA | 06 |
| HIMACHAL_PRADESH | 02 |
| JAMMU_AND_KASHMIR | 01 |
| JHARKHAND | 20 |
| KARNATAKA | 29 |
| KERALA | 32 |
| LADAKH | 38 |
| LAKSHADWEEP | 31 |
| MADHYA_PRADESH | 23 |
| MAHARASHTRA | 27 |
| MANIPUR | 14 |
| MEGHALAYA | 17 |
| MIZORAM | 15 |
| NAGALAND | 13 |
| ODISHA | 21 |
| PONDICHERRY | 34 |
| PUNJAB | 03 |
| RAJASTHAN | 08 |
| SIKKIM | 11 |
| TAMIL_NADU | 33 |
| TELANGANA | 36 |
| TRIPURA | 16 |
| UTTAR_PRADESH | 09 |
| UTTARAKHAND | 05 |
| WEST_BENGAL | 19 |
| OUTSIDE_INDIA | 97 |

</details>

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

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Statement Memo field on the Invoice form in the QuickBooks Online UI.

#### `BillEmailCc`

Required: Optional
Type: `EmailAddress`
Minor version: 8

Identifies the carbon copy e-mail address where the invoice is sent. If not specified, this field is populated from that defined in `Preferences.SalesFormsPrefs.SalesEmailCc`. If this email address is invalid, carbon copy email is not sent.

<details>
<summary>Child attributes for `BillEmailCc`</summary>

##### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

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
Default: <span class="literal">NotSet</span>

Email status of the invoice. Valid values: `NotSet`, `NeedToSend`, `EmailSent`

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

#### `Deposit`

Required: Optional
Type: `Decimal`
Locales: GB, AU, IN, CA, US

The deposit made towards this invoice.

#### `TxnTaxDetail`

Required: Optional
Type: `TxnTaxDetail`

This data type provides information for taxes charged on the transaction as a whole. It captures the details sales taxes calculated for the transaction based on the tax codes referenced by the transaction. This can be calculated by QuickBooks business logic or you may supply it when adding a transaction. See [Global tax model](https://developer.intuit.com/app/developer/qbo/docs/workflows/calculate-sales-tax/automated-sales-tax-for-non-us-locales) for more information about this element.
If sales tax is disabled (`Preferences.TaxPrefs.UsingSalesTax` is set to `false`) then `TxnTaxDetail` is ignored and not stored.

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

#### `AllowOnlineCreditCardPayment`

Required: Optional
Type: `Boolean`
Default: <span class="literal">false</span>
Locales: US

Specifies if online credit card payments are allowed for this invoice and corresponds to the **Credit card** check box on the QuickBooks UI. Active when the company is payments-enabled, i.e., `Preferences.SalesFormsPrefs.ETransactionPaymentEnabled` is set to `true`.

If set to `true`, allow invoice to be paid with online credit card payments. The **Credit card** check box is checked on the QuickBooks UI for this invoice. True by default if the company allows invoices to be paid with credit cards.

If set to `false`, online credit card payments are not allowed. The **Credit card** check box is not checked on the QuickBooks UI for this invoice.

#### `CustomField`

Required: Optional
Type: `CustomField`

One of, up to three custom fields for the transaction. Available for custom fields so configured for the company. Check `Preferences.SalesFormsPrefs.CustomField` and `Preferences.VendorAndPurchasesPrefs.POCustomField` for custom fields currenly configured. [Click here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/create-custom-fields) to learn about managing custom fields.

<details>
<summary>Child attributes for `CustomField`</summary>

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

#### `BillEmailBcc`

Required: Optional
Type: `EmailAddress`
Minor version: 8

Identifies the blind carbon copy e-mail address where the invoice is sent. If not specified, this field is populated from that defined in `Preferences.SalesFormsPrefs.SalesEmailBcc`. If this email address is invalid, blind carbon copy email is not sent.

<details>
<summary>Child attributes for `BillEmailBcc`</summary>

##### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

</details>

#### `ShipMethodRef`

Required: Optional
Type: `ReferenceType`

Reference to the ShipMethod associated with the transaction. There is no shipping method list. Reference resolves to a string. Reference to the ShipMethod associated with the transaction. There is no shipping method list. Reference resolves to a string.

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

Starting `minorversion=54` if you update the `CustomerRef`, the address passed using `BillAddr` will be honored.

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

#### `ApplyTaxAfterDiscount`

Required: Optional
Type: `Boolean`
Default: false
Locales: US

If false or null, calculate the sales tax first, and then apply the discount. If true, subtract the discount first and then calculate the sales tax.

#### Example

```json
{
  "Invoice": {
    "TxnDate": "2014-09-19",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "SalesTermRef": {
      "value": "3"
    },
    "TotalAmt": 362.07,
    "Line": [
      {
        "Description": "Rock Fountain",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 1,
          "UnitPrice": 275,
          "ItemRef": {
            "name": "Rock Fountain",
            "value": "5"
          }
        },
        "LineNum": 1,
        "Amount": 275.0,
        "Id": "1"
      },
      {
        "Description": "Fountain Pump",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 1,
          "UnitPrice": 12.75,
          "ItemRef": {
            "name": "Pump",
            "value": "11"
          }
        },
        "LineNum": 2,
        "Amount": 12.75,
        "Id": "2"
      },
      {
        "Description": "Concrete for fountain installation",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 5,
          "UnitPrice": 9.5,
          "ItemRef": {
            "name": "Concrete",
            "value": "3"
          }
        },
        "LineNum": 3,
        "Amount": 47.5,
        "Id": "3"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 335.25,
        "SubTotalLineDetail": {}
      }
    ],
    "DueDate": "2014-10-19",
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1037",
    "sparse": false,
    "CustomerMemo": {
      "value": "Thank you for your business and have a great day!"
    },
    "ProjectRef": {
      "value": "39298045"
    },
    "Deposit": 0,
    "Balance": 362.07,
    "CustomerRef": {
      "name": "Sonnenschein Family Store",
      "value": "24"
    },
    "TxnTaxDetail": {
      "TxnTaxCodeRef": {
        "value": "2"
      },
      "TotalTax": 26.82,
      "TaxLine": [
        {
          "DetailType": "TaxLineDetail",
          "Amount": 26.82,
          "TaxLineDetail": {
            "NetAmountTaxable": 335.25,
            "TaxPercent": 8,
            "TaxRateRef": {
              "value": "3"
            },
            "PercentBased": true
          }
        }
      ]
    },
    "SyncToken": "0",
    "LinkedTxn": [
      {
        "TxnId": "100",
        "TxnType": "Estimate"
      }
    ],
    "BillEmail": {
      "Address": "Familiystore@intuit.com"
    },
    "ShipAddr": {
      "City": "Middlefield",
      "Line1": "5647 Cypress Hill Ave.",
      "PostalCode": "94303",
      "Lat": "37.4238562",
      "Long": "-122.1141681",
      "CountrySubDivisionCode": "CA",
      "Id": "25"
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "Line4": "Middlefield, CA  94303",
      "Line3": "5647 Cypress Hill Ave.",
      "Line2": "Sonnenschein Family Store",
      "Line1": "Russ Sonnenschein",
      "Long": "-122.1141681",
      "Lat": "37.4238562",
      "Id": "95"
    },
    "MetaData": {
      "CreateTime": "2014-09-19T13:16:17-07:00",
      "LastUpdatedTime": "2014-09-19T13:16:17-07:00"
    },
    "CustomField": [
      {
        "DefinitionId": "1",
        "StringValue": "102",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "130"
  },
  "time": "2015-07-24T10:48:27.082-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T10:44:52.998-07:00">
    <Invoice domain="QBO" sparse="false">
        <Id>130</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-19T13:16:17-07:00</CreateTime>
            <LastUpdatedTime>2014-09-19T13:16:17-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
            <StringValue>102</StringValue>
        </CustomField>
        <DocNumber>1037</DocNumber>
        <TxnDate>2014-09-19</TxnDate>
        <LinkedTxn>
            <TxnId>100</TxnId>
            <TxnType>Estimate</TxnType>
        </LinkedTxn>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Rock Fountain</Description>
            <Amount>275.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Rock Fountain">5</ItemRef>
                <UnitPrice>275</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Id>2</Id>
            <LineNum>2</LineNum>
            <Description>Fountain Pump</Description>
            <Amount>12.75</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Pump">11</ItemRef>
                <UnitPrice>12.75</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Id>3</Id>
            <LineNum>3</LineNum>
            <Description>Concrete for fountain installation</Description>
            <Amount>47.50</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Concrete">3</ItemRef>
                <UnitPrice>9.5</UnitPrice>
                <Qty>5</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>335.25</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TxnTaxCodeRef>2</TxnTaxCodeRef>
            <TotalTax>26.82</TotalTax>
            <TaxLine>
                <Amount>26.82</Amount>
                <DetailType>TaxLineDetail</DetailType>
                <TaxLineDetail>
                    <TaxRateRef>3</TaxRateRef>
                    <PercentBased>true</PercentBased>
                    <TaxPercent>8</TaxPercent>
                    <NetAmountTaxable>335.25</NetAmountTaxable>
                </TaxLineDetail>
            </TaxLine>
        </TxnTaxDetail>
        <CustomerRef name="Sonnenschein Family Store">24</CustomerRef>
        <ProjectRef>39298045</ProjectRef>
        <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
        <BillAddr>
            <Id>95</Id>
            <Line1>Russ Sonnenschein</Line1>
            <Line2>Sonnenschein Family Store</Line2>
            <Line3>5647 Cypress Hill Ave.</Line3>
            <Line4>Middlefield, CA 94303</Line4>
            <Lat>37.4238562</Lat>
            <Long>-122.1141681</Long>
        </BillAddr>
        <ShipAddr>
            <Id>25</Id>
            <Line1>5647 Cypress Hill Ave.</Line1>
            <City>Middlefield</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94303</PostalCode>
            <Lat>37.4238562</Lat>
            <Long>-122.1141681</Long>
        </ShipAddr>
        <SalesTermRef>3</SalesTermRef>
        <DueDate>2014-10-19</DueDate>
        <TotalAmt>362.07</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <BillEmail>
            <Address>Familiystore@intuit.com</Address>
        </BillEmail>
        <Balance>362.07</Balance>
        <Deposit>0</Deposit>
    </Invoice>
</IntuitResponse>
```

## Create an invoice

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/invoice`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- Have at least one `Line` a sales item or inline subtotal.
- Have a populated `CustomerRef` element.

### Request Body

The minimum elements to create an Invoice are listed here.

Schema: `invoicerequest`

<details>
<summary>Show schema for `invoicerequest`</summary>

#### invoicerequest

Model type: `object`

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

##### `Line [0..n]`

Required: Required
Type: `Invoice line object`

The minimum line item required for the request is one of the following. `SalesItemLine`, `GroupLine` and Inline subtotal using `DescriptionOnlyLine`

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

###### descriptiononlyline

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
      "DetailType": "SalesItemLineDetail",
      "Amount": 100.0,
      "SalesItemLineDetail": {
        "ItemRef": {
          "name": "Services",
          "value": "1"
        }
      }
    }
  ],
  "CustomerRef": {
    "value": "1"
  }
}
```

#### XML example

```xml
<Invoice xmlns="http://schema.intuit.com/finance/v3">
  <Line>
    <Amount>150</Amount>
    <DetailType>SalesItemLineDetail</DetailType>
    <SalesItemLineDetail>
      <ItemRef>1</ItemRef>
    </SalesItemLineDetail>
  </Line>
  <CustomerRef>1</CustomerRef>
</Invoice>
```

### Returns

The invoice response body.

#### Example

```json
{
  "Invoice": {
    "TxnDate": "2015-07-24",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "TotalAmt": 100.0,
    "Line": [
      {
        "LineNum": 1,
        "Amount": 100.0,
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
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
        "Amount": 100.0,
        "SubTotalLineDetail": {}
      }
    ],
    "DueDate": "2015-08-23",
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1069",
    "sparse": false,
    "ProjectRef": {
      "value": "39298034"
    },
    "Deposit": 0,
    "Balance": 100.0,
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "0",
    "LinkedTxn": [],
    "ShipAddr": {
      "City": "Bayshore",
      "Line1": "4581 Finch St.",
      "PostalCode": "94326",
      "Lat": "INVALID",
      "Long": "INVALID",
      "CountrySubDivisionCode": "CA",
      "Id": "109"
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "City": "Bayshore",
      "Line1": "4581 Finch St.",
      "PostalCode": "94326",
      "Lat": "INVALID",
      "Long": "INVALID",
      "CountrySubDivisionCode": "CA",
      "Id": "2"
    },
    "MetaData": {
      "CreateTime": "2015-07-24T10:33:39-07:00",
      "LastUpdatedTime": "2015-07-24T10:33:39-07:00"
    },
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "238"
  },
  "time": "2015-07-24T10:33:39.11-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T10:35:08.591-07:00">
    <Invoice domain="QBO" sparse="false">
        <Id>239</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2015-07-24T10:35:08-07:00</CreateTime>
            <LastUpdatedTime>2015-07-24T10:35:08-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
        </CustomField>
        <DocNumber>1070</DocNumber>
        <TxnDate>2015-07-24</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Amount>150.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Services">1</ItemRef>
                <TaxCodeRef>NON</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>150.00</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
        <ProjectRef>39298034</ProjectRef>
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
        <DueDate>2015-08-23</DueDate>
        <TotalAmt>150.00</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <Balance>150.00</Balance>
        <Deposit>0</Deposit>
    </Invoice>
</IntuitResponse>
```

## Delete an invoice

### Definition

- **Content type:** `application/json or application/xml`
- **Operation:** `POST /v3/company/<realmID>/invoice?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the invoice object specified in the request body. Include a minimum of `Invoice.Id` and `Invoice.SyncToken` in the request body. You must unlink any linked transactions associated with the invoice object before deleting it.

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
  "SyncToken": "3",
  "Id": "33"
}
```

#### XML example

```xml
<Invoice xmlns='http://schema.intuit.com/finance/v3' domain="QBO" sparse="false">
    <Id>863</Id>
    <SyncToken>0</SyncToken>
</Invoice>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "Invoice": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "33"
  },
  "time": "2013-03-15T00:18:15.322-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T08:30:33.626-07:00">
  <Invoice domain="QBO" status="Deleted">
    <Id>41</Id>
  </Invoice>
</IntuitResponse>
```

## Void an invoice

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/invoice?operation=void`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to void an existing invoice object; include a minimum of `Invoice.Id` and the current `Invoice.SyncToken`. The transaction remains active but all amounts and quantities are zeroed and the string, `Voided`, is injected into `Invoice.PrivateNote`, prepended to existing text if present.

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
  "Id": "129"
}
```

#### XML example

```xml
<Invoice xmlns='http://schema.intuit.com/finance/v3' domain="QBO" sparse="false">
    <Id>863</Id>
    <SyncToken>0</SyncToken>
</Invoice>
```

### Returns

The Invoice response body.

#### Example

```json
{
  "Invoice": {
    "AllowOnlineACHPayment": false,
    "domain": "QBO",
    "TxnDate": "2014-11-09",
    "PrintStatus": "NEED_TO_PRINT",
    "SalesTermRef": {
      "value": "3"
    },
    "TotalAmt": 0,
    "Line": [
      {
        "Description": "Sod",
        "DetailType": "SALES_ITEM_LINE_DETAIL",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 0,
          "ItemRef": {
            "name": "Sod",
            "value": "14"
          }
        },
        "LineNum": 1,
        "Amount": 0,
        "Id": "1"
      },
      {
        "Description": "2 cubic ft. bag",
        "DetailType": "SALES_ITEM_LINE_DETAIL",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 0,
          "ItemRef": {
            "name": "Soil",
            "value": "15"
          }
        },
        "LineNum": 2,
        "Amount": 0,
        "Id": "2"
      },
      {
        "Description": "Weekly Gardening Service",
        "DetailType": "SALES_ITEM_LINE_DETAIL",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "Qty": 0,
          "ItemRef": {
            "name": "Gardening",
            "value": "6"
          }
        },
        "LineNum": 3,
        "Amount": 0,
        "Id": "3"
      },
      {
        "Description": "Rock Fountain",
        "DetailType": "SALES_ITEM_LINE_DETAIL",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 0,
          "ItemRef": {
            "name": "Rock Fountain",
            "value": "5"
          }
        },
        "LineNum": 4,
        "Amount": 0,
        "Id": "4"
      },
      {
        "Description": "Fountain Pump",
        "DetailType": "SALES_ITEM_LINE_DETAIL",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 0,
          "ItemRef": {
            "name": "Pump",
            "value": "11"
          }
        },
        "LineNum": 5,
        "Amount": 0,
        "Id": "5"
      },
      {
        "DetailType": "SUB_TOTAL_LINE_DETAIL",
        "Amount": 0,
        "SubTotalLineDetail": {}
      }
    ],
    "DueDate": "2014-12-09",
    "MetaData": {
      "CreateTime": "2014-11-09T13:15:36-08:00",
      "LastUpdatedTime": "2016-03-16T12:27:10-07:00"
    },
    "DocNumber": "1036",
    "PrivateNote": "Voided",
    "sparse": false,
    "CustomerMemo": {
      "value": "Thank you for your business and have a great day!"
    },
    "ProjectRef": {
      "value": "39298045"
    },
    "Deposit": 0,
    "Balance": 0,
    "CustomerRef": {
      "name": "0969 Ocean View Road",
      "value": "8"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "AllowOnlineCreditCardPayment": false,
    "SyncToken": "1",
    "LinkedTxn": [],
    "BillEmail": {
      "Address": "Sporting_goods@intuit.com"
    },
    "ShipAddr": {
      "City": "Middlefield",
      "Line1": "370 Easy St.",
      "PostalCode": "94482",
      "Lat": "37.4031672",
      "Long": "-122.0642815",
      "CountrySubDivisionCode": "CA",
      "Id": "8"
    },
    "EmailStatus": "NOT_SET",
    "BillAddr": {
      "Line4": "Middlefield, CA  94482",
      "Line3": "370 Easy St.",
      "Line2": "Freeman Sporting Goods",
      "Line1": "Sasha Tillou",
      "Long": "INVALID",
      "Lat": "INVALID",
      "Id": "94"
    },
    "ApplyTaxAfterDiscount": false,
    "CustomField": [
      {
        "DefinitionId": "1",
        "StringValue": "105",
        "Type": "STRING_TYPE",
        "Name": "Crew #"
      }
    ],
    "Id": "129",
    "AllowOnlinePayment": false,
    "AllowIPNPayment": false
  },
  "time": "2016-03-16T12:27:10.711-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T08:30:33.626-07:00">
  <Invoice domain="QBO" status="Deleted">
    <Id>41</Id>
  </Invoice>
</IntuitResponse>
```

## Get an invoice as PDF

### Definition

- **Content type:** `application/pdf`
- **Operation:** `GET /v3/company/<realmID>/invoice/<invoiceId>/pdf`
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

## Query an invoice

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Invoice where id = '239'"
```

#### XML example

```sql
select * from Invoice where id = '239'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 1,
    "maxResults": 1,
    "Invoice": [
      {
        "TxnDate": "2015-07-24",
        "domain": "QBO",
        "PrintStatus": "NeedToPrint",
        "TotalAmt": 150.0,
        "Line": [
          {
            "LineNum": 1,
            "Amount": 150.0,
            "SalesItemLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
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
            "Amount": 150.0,
            "SubTotalLineDetail": {}
          }
        ],
        "DueDate": "2015-08-23",
        "ApplyTaxAfterDiscount": false,
        "DocNumber": "1070",
        "sparse": false,
        "ProjectRef": {
          "value": "39298034"
        },
        "Deposit": 0,
        "Balance": 150.0,
        "CustomerRef": {
          "name": "Amy's Bird Sanctuary",
          "value": "1"
        },
        "TxnTaxDetail": {
          "TotalTax": 0
        },
        "SyncToken": "0",
        "LinkedTxn": [],
        "ShipAddr": {
          "City": "Bayshore",
          "Line1": "4581 Finch St.",
          "PostalCode": "94326",
          "Lat": "INVALID",
          "Long": "INVALID",
          "CountrySubDivisionCode": "CA",
          "Id": "109"
        },
        "EmailStatus": "NotSet",
        "BillAddr": {
          "City": "Bayshore",
          "Line1": "4581 Finch St.",
          "PostalCode": "94326",
          "Lat": "INVALID",
          "Long": "INVALID",
          "CountrySubDivisionCode": "CA",
          "Id": "2"
        },
        "MetaData": {
          "CreateTime": "2015-07-24T10:35:08-07:00",
          "LastUpdatedTime": "2015-07-24T10:35:08-07:00"
        },
        "CustomField": [
          {
            "DefinitionId": "1",
            "Type": "StringType",
            "Name": "Crew #"
          }
        ],
        "Id": "239"
      }
    ]
  },
  "time": "2015-07-24T10:38:50.01-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T10:37:57.940-07:00">
    <QueryResponse startPosition="1" maxResults="1" totalCount="1">
        <Invoice domain="QBO" sparse="false">
            <Id>239</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2015-07-24T10:35:08-07:00</CreateTime>
                <LastUpdatedTime>2015-07-24T10:35:08-07:00</LastUpdatedTime>
            </MetaData>
            <CustomField>
                <DefinitionId>1</DefinitionId>
                <Name>Crew #</Name>
                <Type>StringType</Type>
            </CustomField>
            <DocNumber>1070</DocNumber>
            <TxnDate>2015-07-24</TxnDate>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Amount>150.00</Amount>
                <DetailType>SalesItemLineDetail</DetailType>
                <SalesItemLineDetail>
                    <ItemRef name="Services">1</ItemRef>
                    <TaxCodeRef>NON</TaxCodeRef>
                </SalesItemLineDetail>
            </Line>
            <Line>
                <Amount>150.00</Amount>
                <DetailType>SubTotalLineDetail</DetailType>
                <SubTotalLineDetail />
            </Line>
            <TxnTaxDetail>
                <TotalTax>0</TotalTax>
            </TxnTaxDetail>
            <CustomerRef name="Amy's Bird Sanctuary">1</CustomerRef>
            <ProjectRef>39298034</ProjectRef>
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
            <DueDate>2015-08-23</DueDate>
            <TotalAmt>150.00</TotalAmt>
            <Deposit>0</Deposit>
        </Invoice>
    </QueryResponse>
</IntuitResponse>
```

## Read an invoice

### Definition

- **Operation:** `GET /v3/company/<realmID>/invoice/<invoiceId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of an invoice that has been previously created.

### Returns

The invoice response body.

#### Example

```json
{
  "Invoice": {
    "TxnDate": "2014-09-19",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "SalesTermRef": {
      "value": "3"
    },
    "TotalAmt": 362.07,
    "Line": [
      {
        "Description": "Rock Fountain",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 1,
          "UnitPrice": 275,
          "ItemRef": {
            "name": "Rock Fountain",
            "value": "5"
          }
        },
        "LineNum": 1,
        "Amount": 275.0,
        "Id": "1"
      },
      {
        "Description": "Fountain Pump",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 1,
          "UnitPrice": 12.75,
          "ItemRef": {
            "name": "Pump",
            "value": "11"
          }
        },
        "LineNum": 2,
        "Amount": 12.75,
        "Id": "2"
      },
      {
        "Description": "Concrete for fountain installation",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 5,
          "UnitPrice": 9.5,
          "ItemRef": {
            "name": "Concrete",
            "value": "3"
          }
        },
        "LineNum": 3,
        "Amount": 47.5,
        "Id": "3"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 335.25,
        "SubTotalLineDetail": {}
      }
    ],
    "DueDate": "2014-10-19",
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1037",
    "sparse": false,
    "CustomerMemo": {
      "value": "Thank you for your business and have a great day!"
    },
    "ProjectRef": {
      "value": "39298045"
    },
    "Deposit": 0,
    "Balance": 362.07,
    "CustomerRef": {
      "name": "Sonnenschein Family Store",
      "value": "24"
    },
    "TxnTaxDetail": {
      "TxnTaxCodeRef": {
        "value": "2"
      },
      "TotalTax": 26.82,
      "TaxLine": [
        {
          "DetailType": "TaxLineDetail",
          "Amount": 26.82,
          "TaxLineDetail": {
            "NetAmountTaxable": 335.25,
            "TaxPercent": 8,
            "TaxRateRef": {
              "value": "3"
            },
            "PercentBased": true
          }
        }
      ]
    },
    "SyncToken": "0",
    "LinkedTxn": [
      {
        "TxnId": "100",
        "TxnType": "Estimate"
      }
    ],
    "BillEmail": {
      "Address": "Familiystore@intuit.com"
    },
    "ShipAddr": {
      "City": "Middlefield",
      "Line1": "5647 Cypress Hill Ave.",
      "PostalCode": "94303",
      "Lat": "37.4238562",
      "Long": "-122.1141681",
      "CountrySubDivisionCode": "CA",
      "Id": "25"
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "Line4": "Middlefield, CA  94303",
      "Line3": "5647 Cypress Hill Ave.",
      "Line2": "Sonnenschein Family Store",
      "Line1": "Russ Sonnenschein",
      "Long": "-122.1141681",
      "Lat": "37.4238562",
      "Id": "95"
    },
    "MetaData": {
      "CreateTime": "2014-09-19T13:16:17-07:00",
      "LastUpdatedTime": "2014-09-19T13:16:17-07:00"
    },
    "CustomField": [
      {
        "DefinitionId": "1",
        "StringValue": "102",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "130"
  },
  "time": "2015-07-24T10:48:27.082-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T10:44:52.998-07:00">
    <Invoice domain="QBO" sparse="false">
        <Id>130</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2014-09-19T13:16:17-07:00</CreateTime>
            <LastUpdatedTime>2014-09-19T13:16:17-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
            <StringValue>102</StringValue>
        </CustomField>
        <DocNumber>1037</DocNumber>
        <TxnDate>2014-09-19</TxnDate>
        <LinkedTxn>
            <TxnId>100</TxnId>
            <TxnType>Estimate</TxnType>
        </LinkedTxn>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Rock Fountain</Description>
            <Amount>275.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Rock Fountain">5</ItemRef>
                <UnitPrice>275</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Id>2</Id>
            <LineNum>2</LineNum>
            <Description>Fountain Pump</Description>
            <Amount>12.75</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Pump">11</ItemRef>
                <UnitPrice>12.75</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Id>3</Id>
            <LineNum>3</LineNum>
            <Description>Concrete for fountain installation</Description>
            <Amount>47.50</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Concrete">3</ItemRef>
                <UnitPrice>9.5</UnitPrice>
                <Qty>5</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>335.25</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TxnTaxCodeRef>2</TxnTaxCodeRef>
            <TotalTax>26.82</TotalTax>
            <TaxLine>
                <Amount>26.82</Amount>
                <DetailType>TaxLineDetail</DetailType>
                <TaxLineDetail>
                    <TaxRateRef>3</TaxRateRef>
                    <PercentBased>true</PercentBased>
                    <TaxPercent>8</TaxPercent>
                    <NetAmountTaxable>335.25</NetAmountTaxable>
                </TaxLineDetail>
            </TaxLine>
        </TxnTaxDetail>
        <CustomerRef name="Sonnenschein Family Store">24</CustomerRef>
        <ProjectRef>39298045</ProjectRef>
        <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
        <BillAddr>
            <Id>95</Id>
            <Line1>Russ Sonnenschein</Line1>
            <Line2>Sonnenschein Family Store</Line2>
            <Line3>5647 Cypress Hill Ave.</Line3>
            <Line4>Middlefield, CA 94303</Line4>
            <Lat>37.4238562</Lat>
            <Long>-122.1141681</Long>
        </BillAddr>
        <ShipAddr>
            <Id>25</Id>
            <Line1>5647 Cypress Hill Ave.</Line1>
            <City>Middlefield</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94303</PostalCode>
            <Lat>37.4238562</Lat>
            <Long>-122.1141681</Long>
        </ShipAddr>
        <SalesTermRef>3</SalesTermRef>
        <DueDate>2014-10-19</DueDate>
        <TotalAmt>362.07</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <BillEmail>
            <Address>Familiystore@intuit.com</Address>
        </BillEmail>
        <Balance>362.07</Balance>
        <Deposit>0</Deposit>
    </Invoice>
</IntuitResponse>
```

## Send an invoice

### Definition

- **Content type:** `application/octet-stream`
- **Operation:** `POST (Using email address supplied in Invoice.BillEmail.EmailAddress) /v3/company/<realmID>/invoice/<invoiceId>/send
POST(Specifying an explicit email address) /v3/company/<realmID>/invoice/<invoiceId>/send?sendTo=<emailAddr>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- The `Invoice.EmailStatus` parameter is set to `EmailSent`.
- The `Invoice.DeliveryInfo` element is populated with sending information
- The `Invoice.BillEmail.Address` parameter is updated to the address specified with the value of the `sendTo` query parameter, if specified.

### Returns

The invoice response body.

#### Example

```json
{
  "Invoice": {
    "TxnDate": "2013-03-14",
    "domain": "QBO",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "ShipDate": "2013-03-01",
    "TrackingNum": "123456789",
    "ClassRef": {
      "name": "Class 1",
      "value": "200900000000000003901"
    },
    "PrintStatus": "NeedToPrint",
    "SalesTermRef": {
      "value": "4"
    },
    "DeliveryInfo": {
      "DeliveryType": "Email",
      "DeliveryTime": "2014-12-17T11:50:52-08:00"
    },
    "TotalAmt": 52.0,
    "Line": [
      {
        "Description": "Sample invoice create request",
        "DetailType": "SalesItemLineDetail",
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          },
          "Qty": 1,
          "UnitPrice": 50,
          "ServiceDate": "2013-03-04",
          "ItemRef": {
            "name": "Hours",
            "value": "2"
          }
        },
        "LineNum": 1,
        "Amount": 50.0,
        "Id": "1"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 50.0,
        "SubTotalLineDetail": {}
      },
      {
        "DetailType": "DiscountLineDetail",
        "Amount": 5.0,
        "DiscountLineDetail": {
          "DiscountAccountRef": {
            "name": "Discounts given",
            "value": "30"
          },
          "PercentBased": true,
          "DiscountPercent": 10
        }
      },
      {
        "DetailType": "SalesItemLineDetail",
        "Amount": 2.0,
        "SalesItemLineDetail": {
          "ItemRef": {
            "value": "SHIPPING_ITEM_ID"
          }
        }
      }
    ],
    "DueDate": "2013-05-13",
    "MetaData": {
      "CreateTime": "2013-03-14T01:42:16-07:00",
      "LastUpdatedTime": "2014-12-17T11:50:58-08:00"
    },
    "DocNumber": "Sample_Inv#2",
    "PrivateNote": "Summary for sample invoice",
    "sparse": false,
    "DepositToAccountRef": {
      "name": "Undeposited Funds",
      "value": "4"
    },
    "CustomerMemo": {
      "value": "This is the customer message"
    },
    "EmailStatus": "EmailSent",
    "ProjectRef": {
      "value": "39298037"
    },
    "Deposit": 12.0,
    "Balance": 40.0,
    "CustomerRef": {
      "name": "Mr V3 Service Customer Jr2",
      "value": "15"
    },
    "TxnTaxDetail": {
      "TxnTaxCodeRef": {
        "value": "5"
      },
      "TotalTax": 5.0,
      "TaxLine": [
        {
          "DetailType": "TaxLineDetail",
          "Amount": 5.0,
          "TaxLineDetail": {
            "NetAmountTaxable": 50.0,
            "TaxPercent": 10,
            "TaxRateRef": {
              "value": "2"
            },
            "PercentBased": true
          }
        }
      ]
    },
    "SyncToken": "0",
    "BillEmail": {
      "Address": "test@intuit.com"
    },
    "ShipAddr": {
      "City": "San Jose",
      "Country": "USA",
      "Line5": "Cube 999",
      "Line4": "Dept 12",
      "Line3": "123 street",
      "Line2": "Building 1",
      "Line1": "Intuit",
      "PostalCode": "95123",
      "Lat": "37.2374847",
      "Long": "-121.8277925",
      "CountrySubDivisionCode": "CA",
      "Id": "36"
    },
    "DepartmentRef": {
      "name": "Mountain View",
      "value": "1"
    },
    "ShipMethodRef": {
      "name": "UPS",
      "value": "UPS"
    },
    "BillAddr": {
      "City": "Mountain View",
      "Country": "USA",
      "Line5": "Cube 999",
      "Line4": "Dept 12",
      "Line3": "123 street",
      "Line2": "Building 1",
      "Line1": "Google",
      "PostalCode": "95123",
      "Lat": "37.2374847",
      "Long": "-121.8277925",
      "CountrySubDivisionCode": "CA",
      "Id": "35"
    },
    "ApplyTaxAfterDiscount": false,
    "CustomField": [
      {
        "StringValue": "Custom1",
        "Type": "StringType",
        "Name": "Custom 1"
      },
      {
        "StringValue": "Custom2",
        "Type": "StringType",
        "Name": "Custom 2"
      },
      {
        "StringValue": "Custom3",
        "Type": "StringType",
        "Name": "Custom 3"
      }
    ],
    "Id": "96"
  },
  "time": "2013-03-14T13:32:04.895-07:00"
}
```

#### XML example

```text
Response:<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2013-04-23T08:30:39.543-07:00">
  <Invoice domain="QBO" sparse="false">
    <Id>45</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2013-04-23T08:30:19-07:00</CreateTime>
      <LastUpdatedTime>2014-11-19T11:56:44-08:00</LastUpdatedTime>
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
    <DocNumber>1015</DocNumber>
    <TxnDate>2012-04-20</TxnDate>
    <CurrencyRef name="United States Dollar">USD</CurrencyRef>
    <Line>
      <Id>1</Id>
      <LineNum>1</LineNum>
      <Amount>15.00</Amount>
      <DetailType>SalesItemLineDetail</DetailType>
      <SalesItemLineDetail>
        <ItemRef name="Sales">1</ItemRef>
        <TaxCodeRef>NON</TaxCodeRef>
      </SalesItemLineDetail>
    </Line>
    <Line>
      <Amount>15.00</Amount>
      <DetailType>SubTotalLineDetail</DetailType>
      <SubTotalLineDetail/>
    </Line>
    <TxnTaxDetail>
      <TotalTax>0</TotalTax>
    </TxnTaxDetail>
    <CustomerRef name="QKcTQIuiGo fw8Ps8qlNZ">69</CustomerRef>
      <ProjectRef>39298037</ProjectRef>
    <BillAddr>
      <Id>61</Id>
      <Line1>3500</Line1>
      <Line2>Flower Avenue</Line2>
      <City>LosAltos</City>
      <Lat>INVALID</Lat>
      <Long>INVALID</Long>
    </BillAddr>
    <ShipAddr>
      <Id>62</Id>
      <Line1>4500</Line1>
      <Line2>Lily Place</Line2>
      <Lat>38.5399041</Lat>
      <Long>-121.5582189</Long>
    </ShipAddr>
    <DueDate>2012-05-20</DueDate>
    <TotalAmt>15.00</TotalAmt>
    <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
    <PrintStatus>NeedToPrint</PrintStatus>
    <EmailStatus>EmailSent</EmailStatus>
    <DeliveryInfo>
      <DeliveryType>Email</DeliveryType>
      <DeliveryTime>2014-11-19T11:56:28-08:00</DeliveryTime>
    </DeliveryInfo>
    <Balance>15.00</Balance>
    <Deposit>0</Deposit>
  </Invoice>
</IntuitResponse>
```

## Sparse update an invoice

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/invoice`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Sparse updating provides the ability to update a subset of properties for a given object; only elements specified in the request are updated. Missing elements are left untouched. The ID of the object to update is specified in the request body.​

### Request Body

Schema: `invoiceresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "Id": "238",
  "sparse": true,
  "DueDate": "2015-09-30"
}
```

#### XML example

```xml
<Invoice xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>130</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
        <CreateTime>2014-09-19T13:16:17-07:00</CreateTime>
        <LastUpdatedTime>2014-09-19T13:16:17-07:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-09-30</TxnDate>
</Invoice>
```

### Returns

The invoice response body.

#### Example

```json
{
  "Invoice": {
    "TxnDate": "2015-07-24",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "TotalAmt": 100.0,
    "Line": [
      {
        "LineNum": 1,
        "Amount": 100.0,
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
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
        "Amount": 100.0,
        "SubTotalLineDetail": {}
      }
    ],
    "DueDate": "2015-09-30",
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1069",
    "sparse": false,
    "ProjectRef": {
      "value": "39298045"
    },
    "Deposit": 0,
    "Balance": 100.0,
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "1",
    "LinkedTxn": [],
    "ShipAddr": {
      "City": "Bayshore",
      "Line1": "4581 Finch St.",
      "PostalCode": "94326",
      "Lat": "INVALID",
      "Long": "INVALID",
      "CountrySubDivisionCode": "CA",
      "Id": "109"
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "City": "Bayshore",
      "Line1": "4581 Finch St.",
      "PostalCode": "94326",
      "Lat": "INVALID",
      "Long": "INVALID",
      "CountrySubDivisionCode": "CA",
      "Id": "2"
    },
    "MetaData": {
      "CreateTime": "2015-07-24T10:33:39-07:00",
      "LastUpdatedTime": "2015-07-24T11:03:26-07:00"
    },
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "238"
  },
  "time": "2015-07-24T11:03:26.674-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T11:06:15.952-07:00">
    <Invoice domain="QBO" sparse="false">
        <Id>130</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2014-09-19T13:16:17-07:00</CreateTime>
            <LastUpdatedTime>2015-07-24T11:06:16-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
            <DefinitionId>1</DefinitionId>
            <Name>Crew #</Name>
            <Type>StringType</Type>
            <StringValue>102</StringValue>
        </CustomField>
        <DocNumber>1037</DocNumber>
        <TxnDate>2014-09-30</TxnDate>
        <LinkedTxn>
            <TxnId>100</TxnId>
            <TxnType>Estimate</TxnType>
        </LinkedTxn>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Description>Rock Fountain</Description>
            <Amount>275.00</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Rock Fountain">5</ItemRef>
                <UnitPrice>275</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Id>2</Id>
            <LineNum>2</LineNum>
            <Description>Fountain Pump</Description>
            <Amount>12.75</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Pump">11</ItemRef>
                <UnitPrice>12.75</UnitPrice>
                <Qty>1</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Id>3</Id>
            <LineNum>3</LineNum>
            <Description>Concrete for fountain installation</Description>
            <Amount>47.50</Amount>
            <DetailType>SalesItemLineDetail</DetailType>
            <SalesItemLineDetail>
                <ItemRef name="Concrete">3</ItemRef>
                <UnitPrice>9.5</UnitPrice>
                <Qty>5</Qty>
                <TaxCodeRef>TAX</TaxCodeRef>
            </SalesItemLineDetail>
        </Line>
        <Line>
            <Amount>335.25</Amount>
            <DetailType>SubTotalLineDetail</DetailType>
            <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
            <TxnTaxCodeRef>2</TxnTaxCodeRef>
            <TotalTax>26.82</TotalTax>
            <TaxLine>
                <Amount>26.82</Amount>
                <DetailType>TaxLineDetail</DetailType>
                <TaxLineDetail>
                    <TaxRateRef>3</TaxRateRef>
                    <PercentBased>true</PercentBased>
                    <TaxPercent>8</TaxPercent>
                    <NetAmountTaxable>335.25</NetAmountTaxable>
                </TaxLineDetail>
            </TaxLine>
        </TxnTaxDetail>
        <CustomerRef name="Sonnenschein Family Store">24</CustomerRef>
        <ProjectRef>39298034</ProjectRef>
        <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
        <BillAddr>
            <Id>95</Id>
            <Line1>Russ Sonnenschein</Line1>
            <Line2>Sonnenschein Family Store</Line2>
            <Line3>5647 Cypress Hill Ave.</Line3>
            <Line4>Middlefield, CA 94303</Line4>
            <Lat>37.4238562</Lat>
            <Long>-122.1141681</Long>
        </BillAddr>
        <ShipAddr>
            <Id>25</Id>
            <Line1>5647 Cypress Hill Ave.</Line1>
            <City>Middlefield</City>
            <CountrySubDivisionCode>CA</CountrySubDivisionCode>
            <PostalCode>94303</PostalCode>
            <Lat>37.4238562</Lat>
            <Long>-122.1141681</Long>
        </ShipAddr>
        <SalesTermRef>3</SalesTermRef>
        <DueDate>2014-10-19</DueDate>
        <TotalAmt>362.07</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <BillEmail>
            <Address>Familiystore@intuit.com</Address>
        </BillEmail>
        <Balance>362.07</Balance>
        <Deposit>0</Deposit>
    </Invoice>
</IntuitResponse>
```

## Full update an invoice

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/invoice`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing invoice object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `invoicerequest`

<details>
<summary>Show schema for `invoicerequest`</summary>

#### invoicerequest

Model type: `object`

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

##### `Line [0..n]`

Required: Required
Type: `Invoice line object`

The minimum line item required for the request is one of the following. `SalesItemLine`, `GroupLine` and Inline subtotal using `DescriptionOnlyLine`

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

###### descriptiononlyline

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
  "TxnDate": "2015-07-24",
  "domain": "QBO",
  "PrintStatus": "NeedToPrint",
  "TotalAmt": 150.0,
  "Line": [
    {
      "LineNum": 1,
      "Amount": 150.0,
      "SalesItemLineDetail": {
        "TaxCodeRef": {
          "value": "NON"
        },
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
      "Amount": 150.0,
      "SubTotalLineDetail": {}
    }
  ],
  "DueDate": "2015-08-23",
  "ApplyTaxAfterDiscount": false,
  "DocNumber": "1070",
  "sparse": false,
  "CustomerMemo": {
    "value": "Added customer memo."
  },
  "ProjectRef": {
    "value": "39298045"
  },
  "Balance": 150.0,
  "CustomerRef": {
    "name": "Amy's Bird Sanctuary",
    "value": "1"
  },
  "TxnTaxDetail": {
    "TotalTax": 0
  },
  "SyncToken": "0",
  "LinkedTxn": [],
  "ShipAddr": {
    "City": "Bayshore",
    "Line1": "4581 Finch St.",
    "PostalCode": "94326",
    "Lat": "INVALID",
    "Long": "INVALID",
    "CountrySubDivisionCode": "CA",
    "Id": "109"
  },
  "EmailStatus": "NotSet",
  "BillAddr": {
    "City": "Bayshore",
    "Line1": "4581 Finch St.",
    "PostalCode": "94326",
    "Lat": "INVALID",
    "Long": "INVALID",
    "CountrySubDivisionCode": "CA",
    "Id": "2"
  },
  "MetaData": {
    "CreateTime": "2015-07-24T10:35:08-07:00",
    "LastUpdatedTime": "2015-07-24T10:35:08-07:00"
  },
  "CustomField": [
    {
      "DefinitionId": "1",
      "Type": "StringType",
      "Name": "Crew #"
    }
  ],
  "Id": "239"
}
```

#### XML example

```xml
<Invoice xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>147</Id>
    <SyncToken>0</SyncToken>

    <MetaData>
      <CreateTime>2014-10-15T14:13:24-07:00</CreateTime>
      <LastUpdatedTime>2014-10-15T14:13:24-07:00</LastUpdatedTime>
    </MetaData>
<PrivateNote>Invoice update</PrivateNote>
    <CustomField>
      <DefinitionId>1</DefinitionId>
      <Name>Crew #</Name>
      <Type>StringType</Type>
    </CustomField>
    <DocNumber>1040</DocNumber>
    <TxnDate>2014-10-15</TxnDate>
    <Line>
      <Id>1</Id>
      <LineNum>1</LineNum>
      <Amount>15.00</Amount>
      <DetailType>SalesItemLineDetail</DetailType>
      <SalesItemLineDetail>
        <ItemRef name="Concrete">3</ItemRef>
        <TaxCodeRef>NON</TaxCodeRef>
      </SalesItemLineDetail>
    </Line>
    <Line>
      <Amount>15.00</Amount>
      <DetailType>SubTotalLineDetail</DetailType>
      <SubTotalLineDetail />
    </Line>
    <TxnTaxDetail>
      <TotalTax>0</TotalTax>
    </TxnTaxDetail>
    <CustomerRef name="Weiskopf Consulting">29</CustomerRef>
    <ProjectRef>39298034</ProjectRef>
    <BillAddr>
      <Id>98</Id>
      <Line1>645</Line1>
      <Line2>Park Avenue</Line2>
      <City>San Jose</City>
    </BillAddr>
    <ShipAddr>
      <Id>99</Id>
      <Line1>2314</Line1>
      <Line2>Gladstone Street</Line2>
      <City>San Francisco</City>
    </ShipAddr>
    <DueDate>2014-11-14</DueDate>
    <TotalAmt>15.00</TotalAmt>
    <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
    <PrintStatus>NeedToPrint</PrintStatus>
    <EmailStatus>NotSet</EmailStatus>
    <Balance>15.00</Balance>
    <Deposit>0</Deposit>
  </Invoice>
```

### Returns

The invoice response body.

#### Example

```json
{
  "Invoice": {
    "TxnDate": "2015-07-24",
    "domain": "QBO",
    "PrintStatus": "NeedToPrint",
    "TotalAmt": 150.0,
    "Line": [
      {
        "LineNum": 1,
        "Amount": 150.0,
        "SalesItemLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
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
        "Amount": 150.0,
        "SubTotalLineDetail": {}
      }
    ],
    "DueDate": "2015-08-23",
    "ApplyTaxAfterDiscount": false,
    "DocNumber": "1070",
    "sparse": false,
    "CustomerMemo": {
      "value": "Added customer memo."
    },
    "ProjectRef": {
      "value": "39298045"
    },
    "Deposit": 0,
    "Balance": 150.0,
    "CustomerRef": {
      "name": "Amy's Bird Sanctuary",
      "value": "1"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "SyncToken": "1",
    "LinkedTxn": [],
    "ShipAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Bayshore",
      "PostalCode": "94326",
      "Id": "118",
      "Line1": "4581 Finch St."
    },
    "EmailStatus": "NotSet",
    "BillAddr": {
      "CountrySubDivisionCode": "CA",
      "City": "Bayshore",
      "PostalCode": "94326",
      "Id": "117",
      "Line1": "4581 Finch St."
    },
    "MetaData": {
      "CreateTime": "2015-07-24T10:35:08-07:00",
      "LastUpdatedTime": "2015-07-24T10:53:39-07:00"
    },
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "Id": "239"
  },
  "time": "2015-07-24T10:53:39.287-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-10-15T15:32:38.807-07:00">
  <Invoice domain="QBO" sparse="false">
    <Id>147</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2014-10-15T14:13:24-07:00</CreateTime>
      <LastUpdatedTime>2014-10-15T15:32:38-07:00</LastUpdatedTime>
    </MetaData>
    <CustomField>
      <DefinitionId>1</DefinitionId>
      <Name>Crew #</Name>
      <Type>StringType</Type>
    </CustomField>
    <DocNumber>1040</DocNumber>
    <TxnDate>2014-10-15</TxnDate>
    <PrivateNote>Invoice update</PrivateNote>
    <Line>
      <Id>1</Id>
      <LineNum>1</LineNum>
      <Amount>15.00</Amount>
      <DetailType>SalesItemLineDetail</DetailType>
      <SalesItemLineDetail>
        <ItemRef name="Concrete">3</ItemRef>
        <TaxCodeRef>NON</TaxCodeRef>
      </SalesItemLineDetail>
    </Line>
    <Line>
      <Amount>15.00</Amount>
      <DetailType>SubTotalLineDetail</DetailType>
      <SubTotalLineDetail />
    </Line>
    <TxnTaxDetail>
      <TotalTax>0</TotalTax>
    </TxnTaxDetail>
    <CustomerRef name="Weiskopf Consulting">29</CustomerRef>
    <ProjectRef>39298034</ProjectRef>
    <BillAddr>
      <Id>98</Id>
      <Line1>645</Line1>
      <Line2>Park Avenue</Line2>
      <City>San Jose</City>
    </BillAddr>
    <ShipAddr>
      <Id>99</Id>
      <Line1>2314</Line1>
      <Line2>Gladstone Street</Line2>
      <City>San Francisco</City>
    </ShipAddr>
    <DueDate>2014-11-14</DueDate>
    <TotalAmt>15.00</TotalAmt>
    <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
    <PrintStatus>NeedToPrint</PrintStatus>
    <EmailStatus>NotSet</EmailStatus>
    <Balance>15.00</Balance>
    <Deposit>0</Deposit>
  </Invoice>
</IntuitResponse>
```
