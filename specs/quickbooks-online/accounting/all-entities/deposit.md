# Deposit

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/deposit
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Deposit
> Canonical entity: `Deposit`

A deposit object is a transaction that records one or more deposits of the following types:

- A customer payment, originally held in the Undeposited Funds account, into the Asset Account specified by the `Deposit.DepositToAccountRef` attribute. The `Deposit.line.LinkedTxn` element is used in this case to hold deposit information.
- A new, direct deposit specified by `Deposit.Line.DepositLineDetail` line detail.

### Business Rules

- There must be at least one line item included in a create request.
- Any transaction that funds the Undeposited Funds account can be linked to a Deposit object with a `Deposit.Line.LinkedTxn` element.

## The deposit object

### depositresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `DepositToAccountRef`

Required: Required
Type: `ReferenceType`

Identifies the account to be used for this deposit. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType` is `Other Current Asset` or `Bank`. Use `Account.Id` and `Account.Name` from that object for `DepositToAccountRef.value` and `DepostiToAccountRef.name`, respectively.

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

#### `Line [0..n]`

Required: Required
Type: `Line`

Individual line items comprising the deposit. Specify a `Line.LinkedTxn` element along with DepositLine detail type if this line is to record a deposit for an existing transaction. Select `UndepositedFunds` account on the existing transaction to make it available for the Deposit.

Possible types of transactions that can be linked to a Deposit include: `Transfer`, `Payment` (for Cash, CreditCard, and Check payment method types), `SalesReceipt`, `RefundReceipt`, `JournalEntry`.

In addition, any expense object whose line item has `AccountReceivable` can be linked to a Payment and then that Payment can be linked to a Deposit object.

Use `Line.LinkedTxn.TxnId` as the ID in a separate read request for the specific resource to retrieve details of the linked object. Valid `Line` types include: `LinkedTxn` and `DepositLine`

<details>
<summary>Child attributes for `Line [0..n]`</summary>

##### linelinkedtxn

Model type: `object`

###### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item.

###### `LinkedTxn [0..n]`

Required: Required

Transaction to which the current entity is related. For example, a billpayment line links to the originating bill object for which the billpayment is applied.

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

##### depositline

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

Set to `DepositLineDetail`for this type of line.

###### `Amount`

Required: Required
Type: `Decimal`
Max length: max 15 digits in 10.5 format

The amount of the line item.

###### `DepositLineDetail`

Required: Required
Type: `DepositLineDetail`

<details>
<summary>Child attributes for `DepositLineDetail`</summary>

###### depositlinedetail

Model type: `object`

###### `AccountRef`

Required: Required
Type: `ReferenceType`

Account where the funds are deposited. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType` equals one of the following: `Income`, `Other Income`, `Expense`, `Other Expense`, `Other Current Assets`, `Equity` or `COGS`. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively. For France locales: The account associated with the referenced Account object is looked up in the account category list.

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

###### `PaymentMethodRef`

Required: Optional
Type: `ReferenceType`

Reference to a PaymentMethod associated with this transaction. Query the PaymentMethod name list resource to determine the appropriate PaymentMethod object for this reference. Use `PaymentMethod.Id` and `PaymentMethod.Name` from that object for `PaymentMethodRef.value` and `PaymentMethodRef.name`, respectively.

<details>
<summary>Child attributes for `PaymentMethodRef`</summary>

###### referencetype

Model type: `object`

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

Reference to the Class associated with the transaction. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

###### `CheckNum`

Required: Optional
Type: `String`

Check number for the desposit.

###### `TaxCodeRef`

Required: Optional
Type: `ReferenceType`
Minor version: 4
Locales: GB, AU, IN, CA

Sales/Purchase tax code associated with the Line. For Non US Companies. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively.

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

###### `TaxApplicableOn`

Required: Optional
Type: `TaxApplicableOnEnum`
Minor version: 4
Locales: GB, AU, IN, CA

Indicates whether the tax applicable on the line is sales or purchase. For Non US Companies. Valid value: `Sales`, `Purchase` Required if TaxCodeRef is specified.

###### `TxnType`

Required: Optional
Type: `TxnTypeEnum`

Type of the payment transaction. For information purposes only.

<details>
<summary>Show more details</summary>

`APCreditCard`, `ARRefundCreditCard`, `Bill`, `BillPaymentCheck`, `BuildAssembly`, `CarryOver`, `CashPurchase`, `Charge`, `Check`, `CreditMemo`, `Deposit`, `EFPLiabilityCheck`, `EFTBillPayment`, `EFTRefund`, `Estimate`, `InventoryAdjustment`, `InventoryTransfer`, `Invoice`, `ItemReceipt`, `JournalEntry`, `LiabilityAdjustment`, `Paycheck`, `PayrollLiabilityCheck`, `Purchase`, `PurchaseOrder`, `PriorPayment`, `ReceivePayment`, `RefundCheck`, `RefundReceipt`, `SalesOrder`, `SalesReceipt`, `SalesTaxPaymentCheck`, `Transfer`, `TimeActivity`, `VendorCredit`, `YTDAdjustment`

</details>

###### `Entity`

Required: Optional
Type: `ReferenceType`

Reference to a customer from which deposit was received. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `Entity.value` and `Entity.name`, respectively.

<details>
<summary>Child attributes for `Entity`</summary>

###### referencetype

Model type: `object`

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
Max length: max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer

###### `CustomField`

Required: Optional
Type: `CustomField`

One of, up to three custom fields for the transaction. Available for custom fields so configured for the company. Check `Preferences.SalesFormsPrefs.CustomField` and `Preferences.VendorAndPurchasesPrefs.POCustomField` for custom fields currenly configured. [Click here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/create-custom-fields) to learn about managing custom fields.

<details>
<summary>Child attributes for `CustomField`</summary>

###### customfield

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
Minor version: 3
Locales: GB, AU, IN, CA

Method in which tax is applied. Allowed values are: `TaxExcluded`, `TaxInclusive`, and `NotApplicable`. Not applicable to US companies; required for non-US companies.

#### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). The CurrencyRef can be overwritten by the `Line.DepositLineDetail` Entity. If the customer that you are referring to has a default currency of USD then the currency for this Deposit will always be set as USD.

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

A reference to the Recurring Transaction. It captures what recurring transaction template the `Deposit` was created from.

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

Indicates the total amount of the transaction. This includes the total of all the charges, allowances, and taxes. Calculated by QuickBooks business logic; any value you supply is over-written by QuickBooks.

#### `HomeTotalAmt`

Type: `Decimal`
Traits: read only, system defined

Total amount of the transaction in the home currency. Includes the total of all the charges, allowances and taxes. Calculated by QuickBooks business logic. Value is valid only when `CurrencyRef` is specified. Applicable if multicurrency is enabled for the company.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Memo field on the Invoice form.

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

#### `DepartmentRef`

Required: Optional
Type: `ReferenceType`

A reference to a Department object specifying the location of the transaction, as defined using location tracking in QuickBooks Online. Available if `Preferences.AccountingInfoPrefs.TrackDepartments` is set to `true`. Query the Department name list resource to determine the appropriate Department object for this reference. Use `Department.Id` and `Department.Name` from that object for `DepartmentRef.value` and `DepartmentRef.name`, respectively.

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

#### `TxnSource`

Required: Optional
Type: `String`

Used internally to specify originating source of a credit card transaction.

#### `TxnDate`

Required: Optional
Type: `Date`
Traits: filterable, sortable
Default: current server date

The date entered by the user when this transaction occurred. For posting transactions, this is the posting date that affects the financial statements. If the date is not supplied, the current date on the server is used.
Sort order is ASC by default.

#### `CashBack`

Required: Optional
Type: `CashBackInfo`

<details>
<summary>Child attributes for `CashBack`</summary>

##### cashbackinfo

Model type: `object`

###### `AccountRef`

Required: Required
Type: `ReferenceType`

The bank acount into which the cashback amount is transferred. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `\AccountRef.name`, respectively. The specified account must have `Account.Classification` set to `Asset`.

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

###### `Amount`

Required: Required
Type: `String`

Amount of the cash back transaction.

###### `Memo`

Required: Optional
Type: `String`

Memo associated with this cash back transaction.

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
Minor version: 4
Locales: GB, AU, IN, CA

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
  "Deposit": {
    "SyncToken": "0",
    "domain": "QBO",
    "DepositToAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "TxnDate": "2014-12-22",
    "TotalAmt": 1675.52,
    "sparse": false,
    "Line": [
      {
        "Amount": 1675,
        "LinkedTxn": [
          {
            "TxnLineId": "0",
            "TxnId": "120",
            "TxnType": "Payment"
          }
        ]
      }
    ],
    "Id": "148",
    "MetaData": {
      "CreateTime": "2014-12-22T12:46:52-08:00",
      "LastUpdatedTime": "2014-12-22T12:46:52-08:00"
    }
  },
  "time": "2014-12-22T13:39:35.449-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-22T12:48:50.866-08:00">
  <Deposit domain="QBO" sparse="false">
    <Id>148</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-12-22T12:46:52-08:00</CreateTime>
      <LastUpdatedTime>2014-12-22T12:46:52-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-12-22</TxnDate>
    <Line>
      <Amount>1675</Amount>
      <LinkedTxn>
        <TxnId>120</TxnId>
        <TxnType>Payment</TxnType>
        <TxnLineId>0</TxnLineId>
      </LinkedTxn>
    </Line>
    <DepositToAccountRef name="Checking">35</DepositToAccountRef>
    <TotalAmt>1675.52</TotalAmt>
  </Deposit>
</IntuitResponse>
```

## Create a deposit

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/deposit`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

A create request includes at least one line representing a deposit--either a direct deposit or linked deposit. More than one deposit can be included in the request; types can be mixed.

 A direct deposit must have at least:
-One line that specifies `Deposit.Line.DepositLineDetail.AccountRef`.
-The `Deposit.DepositToAccountRef` attribute specified.

A deposit via linked transaction must have at least:
-One line that specifies `Deposit.Line.LinkedTxn`.
-The `Deposit.DepositToAccountRef` attribute specified.

### Request Body

The minimum elements to create a Deposit object are listed here.

Schema: `depositrequest`

<details>
<summary>Show schema for `depositrequest`</summary>

#### depositrequest

Model type: `object`

##### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company.
Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). The CurrencyRef can be overwritten by the `Line.DepositLineDetail` Entity. If the customer that you are referring to has a default currency of USD then the currency for this Deposit will always be set as USD.

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

##### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

##### `DepositToAccountRef`

Required: Optional
Type: `ReferenceType`

Identifies the account to be used for this deposit. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType` is `Other Current Asset` or `Bank`. Use `Account.Id` and `Account.Name` from that object for `DepositToAccountRef.value` and `DepostiToAccountRef.name`, respectively.

<details>
<summary>Child attributes for `DepositToAccountRef`</summary>

###### referencetype

Model type: `object`

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

Required: Optional
Type: `Line`

Individual line items of a transaction. Valid `Line` types include:
 DepositLine

<details>
<summary>Child attributes for `Line [0..n]`</summary>

###### depositline

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

Set to `DepositLineDetail`for this type of line.

###### `Amount`

Required: Required
Type: `Decimal`
Max length: max 15 digits in 10.5 format

The amount of the line item.

###### `DepositLineDetail`

Required: Required
Type: `DepositLineDetail`

<details>
<summary>Child attributes for `DepositLineDetail`</summary>

###### depositlinedetail

Model type: `object`

###### `AccountRef`

Required: Required
Type: `ReferenceType`

Account where the funds are deposited. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType` equals one of the following: `Income`, `Other Income`, `Expense`, `Other Expense`, `Other Current Assets`, `Equity` or `COGS`. Use `Account.Id` and `Account.Name` from that object for `AccountRef.value` and `AccountRef.name`, respectively. For France locales: The account associated with the referenced Account object is looked up in the account category list.

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

###### `PaymentMethodRef`

Required: Optional
Type: `ReferenceType`

Reference to a PaymentMethod associated with this transaction. Query the PaymentMethod name list resource to determine the appropriate PaymentMethod object for this reference. Use `PaymentMethod.Id` and `PaymentMethod.Name` from that object for `PaymentMethodRef.value` and `PaymentMethodRef.name`, respectively.

<details>
<summary>Child attributes for `PaymentMethodRef`</summary>

###### referencetype

Model type: `object`

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

Reference to the Class associated with the transaction. Available if `Preferences.AccountingInfoPrefs.ClassTrackingPerLine` is set to `true`. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

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

###### `CheckNum`

Required: Optional
Type: `String`

Check number for the desposit.

###### `TaxCodeRef`

Required: Optional
Type: `ReferenceType`
Minor version: 4
Locales: GB, AU, IN, CA

Sales/Purchase tax code associated with the Line. For Non US Companies. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively.

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

###### `TaxApplicableOn`

Required: Optional
Type: `TaxApplicableOnEnum`
Minor version: 4
Locales: GB, AU, IN, CA

Indicates whether the tax applicable on the line is sales or purchase. For Non US Companies. Valid value: `Sales`, `Purchase` Required if TaxCodeRef is specified.

###### `TxnType`

Required: Optional
Type: `TxnTypeEnum`

Type of the payment transaction. For information purposes only.

<details>
<summary>Show more details</summary>

`APCreditCard`, `ARRefundCreditCard`, `Bill`, `BillPaymentCheck`, `BuildAssembly`, `CarryOver`, `CashPurchase`, `Charge`, `Check`, `CreditMemo`, `Deposit`, `EFPLiabilityCheck`, `EFTBillPayment`, `EFTRefund`, `Estimate`, `InventoryAdjustment`, `InventoryTransfer`, `Invoice`, `ItemReceipt`, `JournalEntry`, `LiabilityAdjustment`, `Paycheck`, `PayrollLiabilityCheck`, `Purchase`, `PurchaseOrder`, `PriorPayment`, `ReceivePayment`, `RefundCheck`, `RefundReceipt`, `SalesOrder`, `SalesReceipt`, `SalesTaxPaymentCheck`, `Transfer`, `TimeActivity`, `VendorCredit`, `YTDAdjustment`

</details>

###### `Entity`

Required: Optional
Type: `ReferenceType`

Reference to a customer from which deposit was received. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `Entity.value` and `Entity.name`, respectively.

<details>
<summary>Child attributes for `Entity`</summary>

###### referencetype

Model type: `object`

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
Max length: max 4000 chars

Free form text description of the line item that appears in the printed record.

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer

###### `CustomField`

Required: Optional
Type: `CustomField`

One of, up to three custom fields for the transaction. Available for custom fields so configured for the company. Check `Preferences.SalesFormsPrefs.CustomField` and `Preferences.VendorAndPurchasesPrefs.POCustomField` for custom fields currenly configured. [Click here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/create-custom-fields) to learn about managing custom fields.

<details>
<summary>Child attributes for `CustomField`</summary>

###### customfield

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

</details>

</details>

#### Example

```json
{
  "Line": [
    {
      "DetailType": "DepositLineDetail",
      "Amount": 20.0,
      "ProjectRef": {
        "value": "42991284"
      },
      "DepositLineDetail": {
        "AccountRef": {
          "name": "Unapplied Cash Payment Income",
          "value": "87"
        }
      }
    }
  ],
  "DepositToAccountRef": {
    "name": "Checking",
    "value": "35"
  }
}
```

#### XML example

```xml
<Deposit xmlns="http://schema.intuit.com/finance/v3" domain="QBO">
    <Line>
        <Amount>20.00</Amount>
        <DetailType>DepositLineDetail</DetailType>
        <DepositLineDetail>
            <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
        </DepositLineDetail>
        <ProjectRef>39298045</ProjectRef>
    </Line>
    <DepositToAccountRef name="Checking">35</DepositToAccountRef>
</Deposit>
```

### Returns

The deposit response body.

#### Example

```json
{
  "Deposit": {
    "SyncToken": "0",
    "domain": "QBO",
    "DepositToAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "TxnDate": "2014-12-22",
    "TotalAmt": 20.0,
    "sparse": false,
    "Line": [
      {
        "DetailType": "DepositLineDetail",
        "ProjectRef": {
          "value": "42991284"
        },
        "LineNum": 1,
        "Amount": 20.0,
        "Id": "1",
        "DepositLineDetail": {
          "AccountRef": {
            "name": "Unapplied Cash Payment Income",
            "value": "87"
          }
        }
      }
    ],
    "Id": "149",
    "MetaData": {
      "CreateTime": "2014-12-22T14:46:36-08:00",
      "LastUpdatedTime": "2014-12-22T14:46:36-08:00"
    }
  },
  "time": "2014-12-22T14:46:36.084-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-22T12:34:06.405-08:00">
  <Deposit domain="QBO" sparse="false">
    <Id>147</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-12-22T12:34:06-08:00</CreateTime>
      <LastUpdatedTime>2014-12-22T12:34:06-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-12-22</TxnDate>
    <Line>
      <Id>1</Id>
      <LineNum>1</LineNum>
      <Amount>20.00</Amount>
      <DetailType>DepositLineDetail</DetailType>
      <DepositLineDetail>
        <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
      </DepositLineDetail>
      <ProjectRef>39298045</ProjectRef>
    </Line>
    <DepositToAccountRef name="Checking">35</DepositToAccountRef>
    <TotalAmt>20.00</TotalAmt>
  </Deposit>
</IntuitResponse>
```

## Delete a deposit

### Definition

- **Operation:** `POST /v3/company/<realmID>/deposit?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the Deposit object specified in the request body. Include a minimum of `Id` and `SyncToken` in the request body.

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
  "Id": "148"
}
```

#### XML example

```xml
<Deposit xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>147</Id>
    <SyncToken>3</SyncToken>
</Deposit>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "Deposit": {
    "status": "Deleted",
    "domain": "QBO",
    "Id": "148"
  },
  "time": "2014-12-22T14:07:19.053-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-22T13:06:03.199-08:00">
    <Deposit domain="QBO" status="Deleted">
        <Id>147</Id>
    </Deposit>
</IntuitResponse>
```

## Query a deposit

### Definition

- **Content type:** `application/text`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Deposit  "
```

#### XML example

```sql
select * from Deposit
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "totalCount": 8,
    "Deposit": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "TxnDate": "2014-12-22",
        "TotalAmt": 1675.52,
        "sparse": false,
        "Line": [
          {
            "Amount": 1675,
            "ProjectRef": {
              "value": "39298045"
            },
            "LinkedTxn": [
              {
                "TxnLineId": "0",
                "TxnId": "120",
                "TxnType": "Payment"
              }
            ]
          }
        ],
        "Id": "148",
        "MetaData": {
          "CreateTime": "2014-12-22T12:46:52-08:00",
          "LastUpdatedTime": "2014-12-22T12:46:52-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "name": "Checking",
          "value": "35"
        },
        "TxnDate": "2014-12-10",
        "TotalAmt": 20.0,
        "sparse": false,
        "Line": [
          {
            "Amount": 1675,
            "LinkedTxn": [
              {
                "TxnLineId": "0",
                "TxnId": "120",
                "TxnType": "Payment"
              }
            ]
          },
          {
            "LineNum": 1,
            "Amount": 20.0,
            "Id": "1",
            "DepositLineDetail": {
              "AccountRef": {
                "name": "Unapplied Cash Payment Income",
                "value": "87"
              }
            },
            "DetailType": "DepositLineDetail"
          }
        ],
        "Id": "145",
        "MetaData": {
          "CreateTime": "2014-12-10T15:21:44-08:00",
          "LastUpdatedTime": "2014-12-10T15:21:44-08:00"
        }
      },
      {
        "SyncToken": "0",
        "domain": "QBO",
        "DepositToAccountRef": {
          "name": "Savings",
          "value": "36"
        },
        "TxnDate": "2014-11-05",
        "TotalAmt": 600.0,
        "PrivateNote": "Opening Balance",
        "sparse": false,
        "Line": [
          {
            "Amount": 140,
            "LinkedTxn": [
              {
                "TxnLineId": "0",
                "TxnId": "47",
                "TxnType": "SalesReceipt"
              }
            ]
          },
          {
            "Amount": 78,
            "LinkedTxn": [
              {
                "TxnLineId": "0",
                "TxnId": "38",
                "TxnType": "SalesReceipt"
              }
            ]
          },
          {
            "LineNum": 1,
            "Amount": 600.0,
            "Id": "1",
            "DepositLineDetail": {
              "AccountRef": {
                "name": "Opening Balance Equity",
                "value": "34"
              }
            },
            "DetailType": "DepositLineDetail"
          }
        ],
        "Id": "5",
        "MetaData": {
          "CreateTime": "2014-11-05T12:09:00-08:00",
          "LastUpdatedTime": "2014-11-05T12:09:00-08:00"
        }
      }
    ],
    "maxResults": 8
  },
  "time": "2014-12-22T13:11:37.977-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-22T13:02:40.942-08:00">
    <QueryResponse startPosition="1" maxResults="9" totalCount="9">
        <Deposit domain="QBO" sparse="false">
            <Id>147</Id>
            <SyncToken>3</SyncToken>
            <MetaData>
                <CreateTime>2014-12-22T12:34:06-08:00</CreateTime>
                <LastUpdatedTime>2014-12-22T13:01:13-08:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-12-19</TxnDate>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Amount>55.00</Amount>
                <DetailType>DepositLineDetail</DetailType>
                <DepositLineDetail>
                    <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
                </DepositLineDetail>
            </Line>
            <DepositToAccountRef name="Checking">35</DepositToAccountRef>
            <TotalAmt>55.00</TotalAmt>
        </Deposit>
        <Deposit domain="QBO" sparse="false">
            <Id>148</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-12-22T12:46:52-08:00</CreateTime>
                <LastUpdatedTime>2014-12-22T12:46:52-08:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-12-22</TxnDate>
            <Line>
                <Amount>1675</Amount>
                <LinkedTxn>
                    <TxnId>120</TxnId>
                    <TxnType>Payment</TxnType>
                    <TxnLineId>0</TxnLineId>
                </LinkedTxn>
                <ProjectRef>39298045</ProjectRef>
            </Line>
            <DepositToAccountRef name="Checking">35</DepositToAccountRef>
            <TotalAmt>1675.52</TotalAmt>
        </Deposit>
        <Deposit domain="QBO" sparse="false">
            <Id>146</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-12-10T15:24:40-08:00</CreateTime>
                <LastUpdatedTime>2014-12-10T15:24:40-08:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-12-10</TxnDate>
            <Line>
                <Amount>1675</Amount>
                <LinkedTxn>
                    <TxnId>120</TxnId>
                    <TxnType>Payment</TxnType>
                    <TxnLineId>0</TxnLineId>
                </LinkedTxn>
            </Line>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Amount>20.00</Amount>
                <DetailType>DepositLineDetail</DetailType>
                <DepositLineDetail>
                    <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
                </DepositLineDetail>
            </Line>
            <DepositToAccountRef name="Checking">35</DepositToAccountRef>
            <TotalAmt>20.00</TotalAmt>
        </Deposit>
        ...
        <Deposit domain="QBO" sparse="false">
            <Id>5</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2014-11-05T12:09:00-08:00</CreateTime>
                <LastUpdatedTime>2014-11-05T12:09:00-08:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2014-11-05</TxnDate>
            <PrivateNote>Opening Balance</PrivateNote>
            <Line>
                <Amount>140</Amount>
                <LinkedTxn>
                    <TxnId>47</TxnId>
                    <TxnType>SalesReceipt</TxnType>
                    <TxnLineId>0</TxnLineId>
                </LinkedTxn>
            </Line>
            <Line>
                <Amount>78</Amount>
                <LinkedTxn>
                    <TxnId>38</TxnId>
                    <TxnType>SalesReceipt</TxnType>
                    <TxnLineId>0</TxnLineId>
                </LinkedTxn>
            </Line>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Amount>600.00</Amount>
                <DetailType>DepositLineDetail</DetailType>
                <DepositLineDetail>
                    <AccountRef name="Opening Balance Equity">34</AccountRef>
                </DepositLineDetail>
            </Line>
            <DepositToAccountRef name="Savings">36</DepositToAccountRef>
            <TotalAmt>600.00</TotalAmt>
        </Deposit>
    </QueryResponse>
</IntuitResponse>
```

## Read a deposit

### Definition

- **Operation:** `GET /v3/company/<realmID>/deposit/<depositId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a Deposit object that has been previously created.

### Returns

The deposit response body.

#### Example

```json
{
  "Deposit": {
    "SyncToken": "0",
    "domain": "QBO",
    "DepositToAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "TxnDate": "2014-12-22",
    "TotalAmt": 1675.52,
    "sparse": false,
    "Line": [
      {
        "Amount": 1675,
        "LinkedTxn": [
          {
            "TxnLineId": "0",
            "TxnId": "120",
            "TxnType": "Payment"
          }
        ]
      }
    ],
    "Id": "148",
    "MetaData": {
      "CreateTime": "2014-12-22T12:46:52-08:00",
      "LastUpdatedTime": "2014-12-22T12:46:52-08:00"
    }
  },
  "time": "2014-12-22T13:39:35.449-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-22T12:48:50.866-08:00">
  <Deposit domain="QBO" sparse="false">
    <Id>148</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2014-12-22T12:46:52-08:00</CreateTime>
      <LastUpdatedTime>2014-12-22T12:46:52-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-12-22</TxnDate>
    <Line>
      <Amount>1675</Amount>
      <LinkedTxn>
        <TxnId>120</TxnId>
        <TxnType>Payment</TxnType>
        <TxnLineId>0</TxnLineId>
      </LinkedTxn>
    </Line>
    <DepositToAccountRef name="Checking">35</DepositToAccountRef>
    <TotalAmt>1675.52</TotalAmt>
  </Deposit>
</IntuitResponse>
```

## Full update a deposit

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/deposit`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing deposit object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.

### Request Body

Schema: `depositresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "1",
  "domain": "QBO",
  "DepositToAccountRef": {
    "name": "Checking",
    "value": "35"
  },
  "TxnDate": "2014-12-15",
  "TotalAmt": 1675.52,
  "sparse": false,
  "Line": [
    {
      "Amount": 1675,
      "LinkedTxn": [
        {
          "TxnLineId": "0",
          "TxnId": "120",
          "TxnType": "Payment"
        }
      ]
    }
  ],
  "Id": "148",
  "MetaData": {
    "CreateTime": "2014-12-22T12:46:52-08:00",
    "LastUpdatedTime": "2014-12-22T12:46:52-08:00"
  }
}
```

#### XML example

```xml
 <Deposit xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
    <Id>147</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
        <CreateTime>2014-12-22T12:34:06-08:00</CreateTime>
        <LastUpdatedTime>2014-12-22T12:34:06-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-12-22</TxnDate>
    <Line>
        <Id>1</Id>
        <LineNum>1</LineNum>
        <Amount>45.00</Amount>
        <DetailType>DepositLineDetail</DetailType>
        <DepositLineDetail>
            <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
        </DepositLineDetail>
    </Line>
    <DepositToAccountRef name="Checking">35</DepositToAccountRef>
    <TotalAmt>20.00</TotalAmt>
</Deposit>
```

### Returns

The deposit response body.

#### Example

```json
{
  "Deposit": {
    "SyncToken": "2",
    "domain": "QBO",
    "DepositToAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "TxnDate": "2014-12-07",
    "TotalAmt": 1675.52,
    "sparse": false,
    "Line": [
      {
        "Amount": 1675,
        "LinkedTxn": [
          {
            "TxnLineId": "0",
            "TxnId": "120",
            "TxnType": "Payment"
          }
        ]
      }
    ],
    "Id": "148",
    "MetaData": {
      "CreateTime": "2014-12-22T12:46:52-08:00",
      "LastUpdatedTime": "2014-12-22T14:04:10-08:00"
    }
  },
  "time": "2014-12-22T14:04:10.815-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-22T12:54:27.439-08:00">
    <Deposit domain="QBO" sparse="false">
        <Id>147</Id>
        <SyncToken>1</SyncToken>
        <MetaData>
            <CreateTime>2014-12-22T12:34:06-08:00</CreateTime>
            <LastUpdatedTime>2014-12-22T12:54:27-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-12-22</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Amount>45.00</Amount>
            <DetailType>DepositLineDetail</DetailType>
            <DepositLineDetail>
                <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
            </DepositLineDetail>
        </Line>
        <DepositToAccountRef name="Checking">35</DepositToAccountRef>
        <TotalAmt>45.00</TotalAmt>
    </Deposit>
</IntuitResponse>
```

## Sparse update a deposit

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/deposit`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Sparse updating provides the ability to update a subset of properties for a given object; only elements specified in the request are updated. Missing elements are left untouched. The ID of the object to update is specified in the request body.​

### Request Body

Schema: `depositresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "domain": "QBO",
  "DepositToAccountRef": {
    "name": "Checking",
    "value": "35"
  },
  "TxnDate": "2014-12-02",
  "sparse": true,
  "Id": "146",
  "MetaData": {
    "CreateTime": "2014-12-22T12:46:52-08:00",
    "LastUpdatedTime": "2014-12-22T12:46:52-08:00"
  }
}
```

#### XML example

```xml
<Deposit xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="true">
    <Id>147</Id>
    <SyncToken>2</SyncToken>
    <MetaData>
        <CreateTime>2014-12-22T12:34:06-08:00</CreateTime>
        <LastUpdatedTime>2014-12-22T12:55:59-08:00</LastUpdatedTime>
    </MetaData>
    <TxnDate>2014-12-19</TxnDate>
    <DepositToAccountRef name="Checking">35</DepositToAccountRef>
</Deposit>
```

### Returns

The deposit response body.

#### Example

```json
{
  "Deposit": {
    "SyncToken": "1",
    "domain": "QBO",
    "DepositToAccountRef": {
      "name": "Checking",
      "value": "35"
    },
    "TxnDate": "2014-12-02",
    "TotalAmt": 20.0,
    "sparse": false,
    "Line": [
      {
        "LineNum": 1,
        "Amount": 20.0,
        "Id": "1",
        "DepositLineDetail": {
          "AccountRef": {
            "name": "Unapplied Cash Payment Income",
            "value": "87"
          }
        },
        "DetailType": "DepositLineDetail"
      }
    ],
    "Id": "146",
    "MetaData": {
      "CreateTime": "2014-12-10T15:24:40-08:00",
      "LastUpdatedTime": "2014-12-22T15:13:18-08:00"
    }
  },
  "time": "2014-12-22T15:13:17.913-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2014-12-22T13:01:13.349-08:00">
    <Deposit domain="QBO" sparse="false">
        <Id>147</Id>
        <SyncToken>3</SyncToken>
        <MetaData>
            <CreateTime>2014-12-22T12:34:06-08:00</CreateTime>
            <LastUpdatedTime>2014-12-22T13:01:13-08:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2014-12-19</TxnDate>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Amount>55.00</Amount>
            <DetailType>DepositLineDetail</DetailType>
            <DepositLineDetail>
                <AccountRef name="Unapplied Cash Payment Income">87</AccountRef>
            </DepositLineDetail>
        </Line>
        <DepositToAccountRef name="Checking">35</DepositToAccountRef>
        <TotalAmt>55.00</TotalAmt>
    </Deposit>
</IntuitResponse>
```
