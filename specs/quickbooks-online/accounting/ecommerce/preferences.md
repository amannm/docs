# Preferences

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/ecommerce/preferences
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [E Commerce](index.md) / Preferences
> Canonical entity: `Preferences`

The Preferences resource represents a set of company preferences that control application behavior in QuickBooks Online. They are mostly exposed as read-only through the Preferences endpoint with only a very small subset of them available as writable. Preferences are not necessarily honored when making requests via the QuickBooks API because a lot of them control UI behavior in the application and may not be applicable for apps.

### Business Rules

- The create operation is not supported.
- The read request retrieves all preferences. There is no notion of preference objects or object IDs.
- Update operations are supported for a limited subset of preferences, which are not marked as readonly.
- The Delete operation is not supported.
- Query is supported with sorting and filtering enabled for Metadata timestamp attributes. Pagination is not supported.
- OtherPrefs type is used as an extension mechanism to contain additional attributes as Name/Value pairs.

## The preferences object

### preferencesresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined

Unique identifier for this object. Sort order is ASC by default.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `EmailMessagesPrefs`

<details>
<summary>Child attributes for `EmailMessagesPrefs`</summary>

##### emailmessagesprefs

Model type: `object`

###### `InvoiceMessage`

Type: `EmailMessageType`

Email message details for Invoice.

<details>
<summary>Child attributes for `InvoiceMessage`</summary>

###### emailmessagetype

Model type: `object`

###### `Message`

Type: `string`

The body of the email message.

###### `Subject`

Type: `string`

The subject of the email.

</details>

###### `EstimateMessage`

Type: `EmailMessageType`

Email message details for Estimate.

<details>
<summary>Child attributes for `EstimateMessage`</summary>

###### emailmessagetype

Model type: `object`

###### `Message`

Type: `string`

The body of the email message.

###### `Subject`

Type: `string`

The subject of the email.

</details>

###### `SalesReceiptMessage`

Type: `EmailMessageType`

Email message details for SalesReceipt.

<details>
<summary>Child attributes for `SalesReceiptMessage`</summary>

###### emailmessagetype

Model type: `object`

###### `Message`

Type: `string`

The body of the email message.

###### `Subject`

Type: `string`

The subject of the email.

</details>

###### `StatementMessage`

Type: `EmailMessageType`

Email message details for Statement.

<details>
<summary>Child attributes for `StatementMessage`</summary>

###### emailmessagetype

Model type: `object`

###### `Message`

Type: `string`

The body of the email message.

###### `Subject`

Type: `string`

The subject of the email.

</details>

</details>

#### `ProductAndServicesPrefs`

<details>
<summary>Child attributes for `ProductAndServicesPrefs`</summary>

##### productandservicesprefs

Model type: `object`

###### `RevenueRecognitionEnabled`

Type: `Boolean`
Default: False
Minor version: 65

Revenue recognition enabled.(QBO Advanced only)

###### `RecognitionFrequencyType`

Type: `String`
Minor version: 65

Indicates how frequently revenue is recognised.Possible values are Daily, Weekly, Monthly.(QBO Advanced only)

###### `ForSales`

Type: `Boolean`
Default: False

Product and Services for Sales enabled.

###### `QuantityOnHand`

Type: `Boolean`
Default: False

Quantity on hand enabled.

###### `QuantityWithPriceAndRate`

Type: `Boolean`
Default: False

Quantity with price and rate enabled.

###### `ForPurchase`

Type: `Boolean`
Default: False

Product and Services for Purchase enabled.

</details>

#### `ReportPrefs`

<details>
<summary>Child attributes for `ReportPrefs`</summary>

##### reportprefs

Model type: `object`

###### `ReportBasis`

Type: `ReportBasisEnum`

Accounting method for summary. Possible values include `Cash` and `Accrual`.

###### `CalcAgingReportFromTxnDate`

Type: `Boolean`
Traits: read only

Calculation aging from transaction date

</details>

#### `AccountingInfoPrefs`

The following settings are available for QuickBooks Online Plus editions, only. To determine this edition type, query the value of the `OfferingSku` CustomerInfo.Name name/value pair for `QuickBooks Online Plus`.

<details>
<summary>Child attributes for `AccountingInfoPrefs`</summary>

##### accountinginfoprefs

Model type: `object`

###### `FirstMonthOfFiscalYear`

Type: `MonthEnum`
Traits: read only
Default: <span class="literal"> January </span>
Minor version: 21

This setting corresponds to the **First month of fiscal year** preference in the QuickBooks Online Company Settings to specify the beginning of the company's fiscal year. Specify months as fulling spelled out: `January`, `February`, and so on.

###### `UseAccountNumbers`

Type: `Boolean`
Traits: read only
Default: <span class="literal"> off </span>
Minor version: 21

This setting corresponds to **Enable account numbers** in QuickBooks Online Company Settings.

- If set to `On`, account names are displayed with their corresponding account numbers in chart of accounts.
- If set to `off`, account numbers are not displayed with account names in chart of accounts.

###### `TaxYearMonth`

Type: `String`
Traits: read only
Default: same month as <span class="literal"> FirstMonthOfFiscalYear </span>
Minor version: 21

This setting corresponds to the **First month of income tax year** preference in the QuickBooks Online Company Settings to specify the beginning of the company's fiscal year. Specify months as fulling spelled out: `January`, `February`, and so on.

###### `ClassTrackingPerTxn`

Type: `Boolean`

This setting correspond to how classes are assigned when **Track classes** in QuickBooks Online Company Settings under Categories is set to **On**. If set to `true`, assign classes at the transaction level. Only one of `ClassTrackingPerTxnLine` or `ClassTrackingPerTxn` can be set to `true` at a given time. If **Track classes** is set to **Off** in company settings, both are set to `false`.

###### `TrackDepartments`

Type: `Boolean`

This setting corresponds to the **Track locations** preference in QuickBooks Online Company Settings under Categories. If **Track locations** is set to **On**, this attribute is returned as `true` in the response. Otherwise, `false` is returned.

###### `TaxForm`

Type: `String`
Traits: read only
Minor version: 21

This setting corresponds to the **Tax form** preference in the QuickBooks Online Company Settings to specify the tax form your company files.

###### `CustomerTerminology`

Type: `String`

This setting corresponds to the **Customer label** preference in QuickBooks Online Company Settings and specifies the term used by the company for customers. This string is used in many places throughout the QuickBooks UI having to do with sales-side activities. Possible values include: `Clients`, `Customers`, `Donors`, `Guests`, `Members`, `Patients`, `Tenants`.

###### `BookCloseDate`

Type: `Date`
Traits: read only
Minor version: 21

This setting corresponds to the **Closing date** preference in the QuickBooks Online Company Settings and specifies the date the books are closed: income and expense accounts are closed and net profit or loss is rolled up into the retained earnings account. Transactions before this date are protected from changes.

###### `DepartmentTerminology`

Type: `String`

Specifies the term used by the company for department. This string is used as a label on transaction forms. Possible values include: `Business`, `Department`, `Division`, `Location`, `Property`, `Store`, `Territory`. This is returned only if the company's **Track location** preference is enabled. See TrackDepartments for more details.

###### `ClassTrackingPerTxnLine`

Type: `Boolean`

This setting correspond to how classes are assigned when **Track classes** in QuickBooks Online Company Settings under Categories is set to **On**. If set to `true`, assign classes at the line level. Only one of `ClassTrackingPerTxnLine` or `ClassTrackingPerTxn` can be set to `true` at a given time. If **Track classes** is set to **Off** in company settings, both are set to `false`.

</details>

#### `SalesFormsPrefs`

<details>
<summary>Child attributes for `SalesFormsPrefs`</summary>

##### salesformspref

Model type: `object`

###### `AllowServiceDate`

Type: `Boolean`

Enables specifying service date.

###### `EstimateMessage`

Type: `String`
Traits: read only

Message to the customers on estimates.

###### `EmailCopyToCompany`

Type: `Boolean`

If set to true, the QuickBooks company is cc'ed on all email sent to customers for sales transactions. Email used is that defined with `CompanyInfo.Email.Address`. Available with minor verion 8.

###### `DefaultCustomerMessage`

Type: `String`

Default customer message.

###### `AllowShipping`

Type: `Boolean`

Enables specifying shipping info.

###### `DefaultDiscountAccount`

Type: `Boolean`

Default discount account.

###### `IPNSupportEnabled`

Type: `Boolean`
Traits: read only

IPN support enabled. No longer used and is being deprecated.

###### `ETransactionPaymentEnabled`

Type: `Boolean`

Enables ETransaction payment.

###### `DefaultTerms`

Type: `ReferenceType`

Default sales terms.

<details>
<summary>Child attributes for `DefaultTerms`</summary>

###### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

###### `AllowDeposit`

Type: `Boolean`

Enables specifying Deposit.

###### `UsingPriceLevels`

Type: `Boolean`
Traits: read only

If set to true, price levels are enabled for sales transactions. Full price level support available via QuickBooks UI, only, in April 2017.

###### `DefaultShippingAccount`

Type: `Boolean`

Default shipping account.

###### `ETransactionAttachPDF`

Type: `Boolean`

Specifies whether sales form PDF should be attached with ETransaction mails.

###### `CustomTxnNumbers`

Type: `Boolean`

Enables the ability to specify custom transaction numbers for sales transactions.

###### `ETransactionEnabledStatus`

Type: `ETYransactionEnabledStatusEnum`
Traits: read only

Enables ETransaction status.

###### `AllowEstimates`

Type: `Boolean`

Enables specifying Estimates.

###### `AllowDiscount`

Type: `Boolean`

Enables specifying Discount.

###### `AutoApplyCredit`

Type: `Boolean`
Traits: read only
Minor version: 21

Automatically applies credits to the next invoice you create for the same customer. Most companies turn on this setting.

###### `SalesEmailBcc`

Required: Optional
Type: `EmailAddress`
Minor version: 8

Default blind carbon copy email address where invoices are sent. Override this setting with the `Invoice.BillEmailBcc` attribute. Max 200 characters. Ignored if address is invalid. Available with minor version 8.

<details>
<summary>Child attributes for `SalesEmailBcc`</summary>

###### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

</details>

###### `SalesEmailCc`

Required: Optional
Type: `EmailAddress`
Minor version: 8

Default carbon copy email address where invoices are sent. Override this setting with the `Invoice.BillEmailCc` attribute. Max 200 characters. Ignored if address is invalid. Available with minor version 8.

<details>
<summary>Child attributes for `SalesEmailCc`</summary>

###### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

</details>

###### `UsingProgressInvoicing`

Required: Optional
Type: `Boolean`
Traits: read only
Default: false or null
Minor version: 32

Enables Progress Invoicing

###### `CustomField`

Required: Optional
Type: `CustomFieldDefinition`
Traits: read only

Toggles whether Sales Forms Custom Fields are enabled on the sales form. Sales forms can have up to three custom fields.

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

#### `VendorAndPurchasesPrefs`

<details>
<summary>Child attributes for `VendorAndPurchasesPrefs`</summary>

##### vendorandpurchaseprefs

Model type: `object`

###### `DefaultMarkupAccount`

Type: `ReferenceType`

Default markup account.

<details>
<summary>Child attributes for `DefaultMarkupAccount`</summary>

###### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

###### `TrackingByCustomer`

Type: `Boolean`

Enables tracking by customer.

###### `DefaultTerms`

Type: `ReferenceType`

Default terms

<details>
<summary>Child attributes for `DefaultTerms`</summary>

###### referencetype

Model type: `object`

###### `value`

Required: Required
Type: `string`

The ID for the referenced object as found in the Id field of the object payload. The context is set by the type of reference and is specific to the QuickBooks company file.

###### `name`

Required: Optional
Type: `string`

An identifying name for the object being referenced by `value` and is derived from the field that holds the common name of that object. This varies by context and specific type of object referenced. For example, references to a Customer object use `Customer.DisplayName` to populate this field. Optionally returned in responses, implementation dependent.

</details>

###### `BillableExpenseTracking`

Type: `Boolean`

Billable Expense tracking enabled.

###### `DefaultMarkup`

Type: `Decimal`

Default markup rate used to calculate the markup amount on the transactions. To enter a markup rate of 8.5%, enter 8.5, not 0.085.

###### `TPAREnabled`

Type: `Boolean`
Traits: read only
Minor version: 40
Locales: AU

Indicates if TPAR enabled by customer.

###### `POCustomField`

Required: Optional
Type: `CustomFieldDefinition`
Traits: read only

Toggles whether Purchase Order Custom Fields are enabled on the sales form. Purchase Order forms can have up to three custom fields

<details>
<summary>Child attributes for `POCustomField`</summary>

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

#### `TaxPrefs`

<details>
<summary>Child attributes for `TaxPrefs`</summary>

##### taxprefs

Model type: `object`

###### `PartnerTaxEnabled`

Type: `Boolean`
Traits: read only

Partner tax refers to the automated sales tax engine that provides sales tax compliance. All QuickBooks Online companies created after November 10, 2017 are enabled by default.

- If `true`, automated sales tax is enabled for the company and sales tax is set up (`UsingSalesTax` is set to `true`).
- If `false`, automated sales tax is enabled for the company but the company doesn't have sales tax set up (`UsingSalesTax` is set to `false`).
- If not present in response payload, the company is not enabled for automated sales tax.

###### `TaxGroupCodeRef`

Type: `String`
Traits: read only

Reference to the TaxCode.Id for tax code group to use.

###### `UsingSalesTax`

Type: `Boolean`
Traits: read only

Sales tax enabled

</details>

#### `OtherPrefs`

Specifies extension of Preference resource to allow extension of Name-Value pair based extension at the top level.

<details>
<summary>Show child attributes</summary>

#### ATTRIBUTES

| Name | Description |
| --- | --- |
| **EXTENSIONS** | **DESCRIPTION** |
| Name | Name of the element. |
| Value | Value of the element. |
| DataPartner | Data partner enabled.<br> `NameValue.Name="DataPartner"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| DateFormat | The date format.<br> `NameValue.Name="DateFormat"`<br> `NameValue.Value="String"` Where `String` is set to one of the following:<br> `Month Date Year separated by a slash`<br> `Date Month Year separated by a slash`<br> `Date Month Year separated by a dash`<br> `Year Month Date separated by a dash`<br> `Year Month Date separated by a slash`<br> `Month Date Year separated by a dash`<br> `Date Month Year separated by a dot`<br> `Month Date Year separated by a dot`<br> `Year Month Date separated by a dot` Available for non-US locales. For US locale use minor version 21. |
| DateFormatMnemonic | The date format mnemonic.<br> `NameValue.Name="DateFormatMnemonic"`<br> `NameValue.Value="String"` Where `String` is set to one of the following:<br> `MMDDYYYY_SEP_SLASH`<br> `DDMMYYYY_SEP_SLASH`<br> `DDMMYYYY_SEP_DASH`<br> `YYYYMMDD_SEP_DASH`<br> `YYYYMMDD_SEP_SLASH`<br> `MMDDYYYY_SEP_DASH`<br> `DDMMYYYY_SEP_DOT`<br> `MMDDYYYY_SEP_DOT`<br> `YYYYMMDD_SEP_DOT` Available for non-US locales. For US locale use minor version 21. |
| DefaultCustomerMessage | The default message appearing on sales transactions.<br> `NameValue.Name = "SalesFormsPrefs.DefaultCustomerMessage"`<br> `NameValue.Value = "string"` |
| DefaultItem | The default line item appearing on sales transactions.<br> `NameValue.Name = "SalesFormsPrefs.DefaultItem"`<br> `NameValue.Value = "string"`<br> where `String` is the `Item.Id` of the item. |
| DefaultTaxRateSelection | The default tax rate selection.<br> `NameValue.Name="AccountingInfoPrefs.DefaultTaxRateSelection"`<br> `NameValue.Value="string"`<br> where `String` is one of the following:`1` transactions are exclusive of tax. `2` transactions are inclusive of tax. |
| DTXCopyMemo | The DTX copy memo enabled<br> `NameValue.Name="DTXCopyMemo"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false` Disabled. |
| MTDEnabled | Make Tax Digital flag for UK locale<br> `NameValue.Name="MTDEnabled"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| FDPEnabled | FDP enabled.<br> `NameValue.Name="FDPEnabled"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| MarkupOnBillableExpenseEnabled | If enabled, the default markup amount specified by `VendorAndPurchasesPrefs.DefaultMarkUp` is automatically added to the expense.<br> `NameValue.Name="VendorAndPurchasesPrefs.MarkupOnBillableExpenseEnabled"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| NumberFormat | The number format.<br> `NameValue.Name="NumberFormat"`<br> `NameValue.Value="String"` Where `String` is set to one of the following:<br> `US Number Format`<br> `German Number Format`<br> `French Number Format`<br> `Indian Number Format` Available for non-US locales. For US locale use minor version 21. |
| NumberFormatMnemonic | The number format mnemonic.<br> `NameValue.Name="NumberFormatMnemonic"`<br> `NameValue.Value="String"` Where `String` is set to one of the following:<br> `US_NB`<br> `DE_NB`<br> `FR_NB`<br> `IN_NB` Available for non-US locales. For US locale use minor version 21. |
| ProjectsEnabled | Projects enabled.<br> `NameValue.Name="ProjectsEnabled"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| PurchseOrderEnabled | If enabled, the QuickBooks Online company allows purchase orders to be generated.<br> `NameValue.Name="VendorAndPurchasesPrefs.PurchseOrderEnabled"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| SalesFormContentEnabled | The DTX copy memo<br> `NameValue.Name="SFCEnabled"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| ShowAccountNumbers | Show account numbers.<br> `NameValue.Name="AccountingInfoPrefs.ShowAccountNumbers"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true` Display account numbers on reports and transactions, such as in sales and expense forms for your view only. `false` Do not show account numbers in reports and transactions. |
| Sign me out if inactive for specified amount of minutes | Sign me out if inactive for specified minutes.<br> `NameValue.Name="SignoutInactiveMinutes"`<br> `NameValue.Value="String"`<br> Where `String` is an interger value containing the number of seconds to keep the session alive. |
| TimeTrackingFeatureEnabled | Time tracking enabled.<br> `NameValue.Name="TimeTrackingFeatureEnabled"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| UncategorizedAssetAccountId | The default account to use for uncategorized assets.<br> `NameValue.Name="UncategorizedAssetAccountId"`<br> `NameValue.Value="string"`. where `String` is the `Account.Id` of the item. |
| UncategorizedExpenseAccountId | The default account to use for uncategorized expenses.<br> `NameValue.Name="UncategorizedExpensesAccountId"`<br> `NameValue.Value="string"`. Where `String` is the `Account.Id` of the item. |
| UncategorizedIncomeAccountId | The default account to use for uncategorized expenses.<br> `NameValue.Name="UncategorizedExpensesAccountId"`<br> `NameValue.Value="string"`. Where `String` is the `Account.Id` of the item. |
| Vendor1099Enabled | Vendor 1099 forms enabled.<br> `NameValue.Name="Vendor1099Enabled"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| Warn if duplicate check number is used | `NameValue.Name="WarnDuplicateCheckNumber"`<br> `NameValue.Value="Flag"` <br> Where `Flag` is defined as: `true` Warn if duplicate check number is used.<br> `false` Do no warn if duplicate check number is used |
| Warn if duplicate bill number is used | `NameValue.Name="WarnDuplicateBillNumber"`<br> `NameValue.Value="Flag"` <br> Where `Flag` is defined as: `true` Warn if duplicate bill number is used.<br> `false` Do no warn if duplicate bill number is used |
| Warn if duplicate journal number is used | `NameValue.Name="WarnDuplicateJournalNumber"`<br> `NameValue.Value="Flag"` <br> Where `Flag` is defined as: `true` Warn if duplicate journal number is used.<br> `false` Do no warn if duplicate journal number is used |
| UseCustomTxnNumbers | If enabled, the QuickBooks Online company allows the ability to specify custom transaction numbers for expense transactions.<br> `NameValue.Name="VendorAndPurchasesPrefs.UseCustomTxnNumbers"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| AllowGratuity | If enabled, the QuickBooks Online company allows to specify Gratuity for SalesReceipts.<br> `NameValue.Name="SalesFormsPrefs.AllowGratuity"`<br> `NameValue.Value="Flag"`<br> Where `Flag` is defined as:`true`Enabled. `false`Disabled. |
| GratuityAccount | The default account to use for gratuity.<br> `NameValue.Name="SalesFormsPrefs.GratuityAccount"`<br> `NameValue.Value="string"`. where `String` is the `Account.Id` of the account. |

</details>

#### `TimeTrackingPrefs`

<details>
<summary>Child attributes for `TimeTrackingPrefs`</summary>

##### timetrackingprefs

Model type: `object`

###### `WorkWeekStartDate`

Type: `WeekEnum`
Traits: read only

Work week starting day.

###### `MarkTimeEntriesBillable`

Type: `Boolean`
Traits: read only

Mark time entries as billable.

###### `ShowBillRateToAll`

Type: `Boolean`

Billing rate to all employees enabled.

###### `UsingSalesTax`

Type: `Boolean`

Services for time tracking enabled.

###### `BillCustomers`

Type: `Boolean`

Enables billing customers for time.

</details>

#### `CurrencyPrefs`

<details>
<summary>Child attributes for `CurrencyPrefs`</summary>

##### currencyprefs

Model type: `object`

###### `HomeCurrency`

Type: `ReferenceType`
Traits: read only

Currency code of the country where the business is physically located.

###### `MultiCurrencyEnabled`

Type: `Boolean`
Traits: read only

Multicurrency enabled for this company. Not available with QuickBooks Simple Start.

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
  "Preferences": {
    "EmailMessagesPrefs": {
      "InvoiceMessage": {
        "Message": "Your invoice is attached.  Please remit payment at your earliest convenience.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Invoice from Craig's Design and Landscaping Services"
      },
      "EstimateMessage": {
        "Message": "Please review the estimate below.  Feel free to contact us if you have any questions.\nWe look forward to working with you.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Estimate from Craig's Design and Landscaping Services"
      },
      "SalesReceiptMessage": {
        "Message": "Your sales receipt is attached.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Sales Receipt from Craig's Design and Landscaping Services"
      },
      "StatementMessage": {
        "Message": "Your statement is attached.  Please remit payment at your earliest convenience.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Statement from Craig's Design and Landscaping Services"
      }
    },
    "ProductAndServicesPrefs": {
      "QuantityWithPriceAndRate": true,
      "ForPurchase": true,
      "QuantityOnHand": true,
      "ForSales": true
    },
    "domain": "QBO",
    "SyncToken": "6",
    "ReportPrefs": {
      "ReportBasis": "Accrual",
      "CalcAgingReportFromTxnDate": false
    },
    "AccountingInfoPrefs": {
      "FirstMonthOfFiscalYear": "January",
      "UseAccountNumbers": true,
      "TaxYearMonth": "January",
      "ClassTrackingPerTxn": false,
      "TrackDepartments": true,
      "TaxForm": "6",
      "CustomerTerminology": "Customers",
      "BookCloseDate": "2018-12-31",
      "DepartmentTerminology": "Location",
      "ClassTrackingPerTxnLine": true
    },
    "SalesFormsPrefs": {
      "ETransactionPaymentEnabled": false,
      "CustomTxnNumbers": false,
      "AllowShipping": false,
      "AllowServiceDate": false,
      "ETransactionEnabledStatus": "NotApplicable",
      "DefaultCustomerMessage": "Thank you for your business and have a great day!",
      "EmailCopyToCompany": false,
      "AllowEstimates": true,
      "DefaultTerms": {
        "value": "3"
      },
      "AllowDiscount": true,
      "DefaultDiscountAccount": "86",
      "AllowDeposit": true,
      "AutoApplyPayments": true,
      "IPNSupportEnabled": false,
      "AutoApplyCredit": true,
      "CustomField": [
        {
          "CustomField": [
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom3"
            },
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom2"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom1"
            }
          ]
        },
        {
          "CustomField": [
            {
              "StringValue": "Crew #",
              "Type": "StringType",
              "Name": "SalesFormsPrefs.SalesCustomName1"
            }
          ]
        }
      ],
      "UsingPriceLevels": false,
      "ETransactionAttachPDF": false
    },
    "VendorAndPurchasesPrefs": {
      "BillableExpenseTracking": true,
      "TrackingByCustomer": true,
      "POCustomField": [
        {
          "CustomField": [
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom3"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom2"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom1"
            }
          ]
        },
        {
          "CustomField": [
            {
              "StringValue": "Sales Rep",
              "Type": "StringType",
              "Name": "PurchasePrefs.PurchaseCustomName2"
            },
            {
              "StringValue": "Crew #",
              "Type": "StringType",
              "Name": "PurchasePrefs.PurchaseCustomName1"
            }
          ]
        }
      ]
    },
    "TaxPrefs": {
      "TaxGroupCodeRef": {
        "value": "2"
      },
      "UsingSalesTax": true
    },
    "OtherPrefs": {
      "NameValue": [
        {
          "Name": "SalesFormsPrefs.DefaultCustomerMessage",
          "Value": "Thank you for your business and have a great day!"
        },
        {
          "Name": "SalesFormsPrefs.DefaultItem",
          "Value": "1"
        },
        {
          "Name": "DTXCopyMemo",
          "Value": "false"
        },
        {
          "Name": "UncategorizedAssetAccountId",
          "Value": "32"
        },
        {
          "Name": "UncategorizedIncomeAccountId",
          "Value": "30"
        },
        {
          "Name": "UncategorizedExpenseAccountId",
          "Value": "31"
        },
        {
          "Name": "SFCEnabled",
          "Value": "true"
        },
        {
          "Name": "DataPartner",
          "Value": "false"
        },
        {
          "Name": "Vendor1099Enabled",
          "Value": "true"
        },
        {
          "Name": "TimeTrackingFeatureEnabled",
          "Value": "true"
        },
        {
          "Name": "FDPEnabled",
          "Value": "false"
        },
        {
          "Name": "ProjectsEnabled",
          "Value": "false"
        },
        {
          "Name": "DateFormat",
          "Value": "Month Date Year separated by a slash"
        },
        {
          "Name": "DateFormatMnemonic",
          "Value": "MMDDYYYY_SEP_SLASH"
        },
        {
          "Name": "NumberFormat",
          "Value": "US Number Format"
        },
        {
          "Name": "NumberFormatMnemonic",
          "Value": "US_NB"
        },
        {
          "Name": "WarnDuplicateCheckNumber",
          "Value": "true"
        },
        {
          "Name": "WarnDuplicateBillNumber",
          "Value": "false"
        },
        {
          "Name": "SignoutInactiveMinutes",
          "Value": "60"
        },
        {
          "Name": "AccountingInfoPrefs.ShowAccountNumbers",
          "Value": "false"
        }
      ]
    },
    "sparse": false,
    "TimeTrackingPrefs": {
      "WorkWeekStartDate": "Monday",
      "MarkTimeEntriesBillable": true,
      "ShowBillRateToAll": false,
      "UseServices": true,
      "BillCustomers": true
    },
    "CurrencyPrefs": {
      "HomeCurrency": {
        "value": "USD"
      },
      "MultiCurrencyEnabled": false
    },
    "Id": "1",
    "MetaData": {
      "CreateTime": "2017-10-25T01:05:43-07:00",
      "LastUpdatedTime": "2018-03-08T13:24:26-08:00"
    }
  },
  "time": "2018-03-12T08:22:43.280-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2018-03-12T08:44:41.982-07:00">
    <Preferences domain="QBO" sparse="false">
        <Id>1</Id>
        <SyncToken>6</SyncToken>
        <MetaData>
            <CreateTime>2017-10-25T01:05:43-07:00</CreateTime>
            <LastUpdatedTime>2018-03-08T13:24:26-08:00</LastUpdatedTime>
        </MetaData>
        <AccountingInfoPrefs>
            <UseAccountNumbers>true</UseAccountNumbers>
            <TrackDepartments>true</TrackDepartments>
            <DepartmentTerminology>Location</DepartmentTerminology>
            <ClassTrackingPerTxn>false</ClassTrackingPerTxn>
            <ClassTrackingPerTxnLine>true</ClassTrackingPerTxnLine>
            <FirstMonthOfFiscalYear>January</FirstMonthOfFiscalYear>
            <TaxYearMonth>January</TaxYearMonth>
            <TaxForm>6</TaxForm>
            <BookCloseDate>2018-12-31</BookCloseDate>
            <CustomerTerminology>Customers</CustomerTerminology>
        </AccountingInfoPrefs>
        <ProductAndServicesPrefs>
            <ForSales>true</ForSales>
            <ForPurchase>true</ForPurchase>
            <QuantityWithPriceAndRate>true</QuantityWithPriceAndRate>
            <QuantityOnHand>true</QuantityOnHand>
        </ProductAndServicesPrefs>
        <SalesFormsPrefs>
            <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom3</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom2</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom1</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
            </CustomField>
            <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
                <CustomField>
                    <Name>SalesFormsPrefs.SalesCustomName1</Name>
                    <Type>StringType</Type>
                    <StringValue>Crew #</StringValue>
                </CustomField>
            </CustomField>
            <CustomTxnNumbers>false</CustomTxnNumbers>
            <EmailCopyToCompany>false</EmailCopyToCompany>
            <AllowDeposit>true</AllowDeposit>
            <AllowDiscount>true</AllowDiscount>
            <DefaultDiscountAccount>86</DefaultDiscountAccount>
            <AllowEstimates>true</AllowEstimates>
            <ETransactionEnabledStatus>NotApplicable</ETransactionEnabledStatus>
            <ETransactionAttachPDF>false</ETransactionAttachPDF>
            <ETransactionPaymentEnabled>false</ETransactionPaymentEnabled>
            <IPNSupportEnabled>false</IPNSupportEnabled>
            <AllowServiceDate>false</AllowServiceDate>
            <AllowShipping>false</AllowShipping>
            <DefaultTerms>3</DefaultTerms>
            <AutoApplyCredit>true</AutoApplyCredit>
            <AutoApplyPayments>true</AutoApplyPayments>
            <UsingPriceLevels>false</UsingPriceLevels>
            <DefaultCustomerMessage>Thank you for your business and have a great day!</DefaultCustomerMessage>
        </SalesFormsPrefs>
        <EmailMessagesPrefs>
            <InvoiceMessage>
                <Subject>Invoice from Craig's Design and Landscaping Services</Subject>
                <Message>Your invoice is attached.  Please remit payment at your earliest convenience.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </InvoiceMessage>
            <EstimateMessage>
                <Subject>Estimate from Craig's Design and Landscaping Services</Subject>
                <Message>Please review the estimate below.  Feel free to contact us if you have any questions.
We look forward to working with you.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </EstimateMessage>
            <SalesReceiptMessage>
                <Subject>Sales Receipt from Craig's Design and Landscaping Services</Subject>
                <Message>Your sales receipt is attached.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </SalesReceiptMessage>
            <StatementMessage>
                <Subject>Statement from Craig's Design and Landscaping Services</Subject>
                <Message>Your statement is attached.  Please remit payment at your earliest convenience.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </StatementMessage>
        </EmailMessagesPrefs>
        <VendorAndPurchasesPrefs>
            <TrackingByCustomer>true</TrackingByCustomer>
            <BillableExpenseTracking>true</BillableExpenseTracking>
            <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom3</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom2</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom1</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
            </POCustomField>
            <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
                <CustomField>
                    <Name>PurchasePrefs.PurchaseCustomName2</Name>
                    <Type>StringType</Type>
                    <StringValue>Sales Rep</StringValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.PurchaseCustomName1</Name>
                    <Type>StringType</Type>
                    <StringValue>Crew #</StringValue>
                </CustomField>
            </POCustomField>
        </VendorAndPurchasesPrefs>
        <TimeTrackingPrefs>
            <UseServices>true</UseServices>
            <BillCustomers>true</BillCustomers>
            <ShowBillRateToAll>false</ShowBillRateToAll>
            <WorkWeekStartDate>Monday</WorkWeekStartDate>
            <MarkTimeEntriesBillable>true</MarkTimeEntriesBillable>
        </TimeTrackingPrefs>
        <TaxPrefs>
            <UsingSalesTax>true</UsingSalesTax>
            <TaxGroupCodeRef>2</TaxGroupCodeRef>
        </TaxPrefs>
        <CurrencyPrefs>
            <MultiCurrencyEnabled>false</MultiCurrencyEnabled>
            <HomeCurrency>USD</HomeCurrency>
        </CurrencyPrefs>
        <ReportPrefs>
            <ReportBasis>Accrual</ReportBasis>
            <CalcAgingReportFromTxnDate>false</CalcAgingReportFromTxnDate>
        </ReportPrefs>
        <OtherPrefs>
            <NameValue>
                <Name>SalesFormsPrefs.DefaultCustomerMessage</Name>
                <Value>Thank you for your business and have a great day!</Value>
            </NameValue>
            <NameValue>
                <Name>SalesFormsPrefs.DefaultItem</Name>
                <Value>1</Value>
            </NameValue>
            <NameValue>
                <Name>DTXCopyMemo</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedAssetAccountId</Name>
                <Value>32</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedIncomeAccountId</Name>
                <Value>30</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedExpenseAccountId</Name>
                <Value>31</Value>
            </NameValue>
            <NameValue>
                <Name>SFCEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>DataPartner</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>Vendor1099Enabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>TimeTrackingFeatureEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>FDPEnabled</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>ProjectsEnabled</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>DateFormat</Name>
                <Value>Month Date Year separated by a slash</Value>
            </NameValue>
            <NameValue>
                <Name>DateFormatMnemonic</Name>
                <Value>MMDDYYYY_SEP_SLASH</Value>
            </NameValue>
            <NameValue>
                <Name>NumberFormat</Name>
                <Value>US Number Format</Value>
            </NameValue>
            <NameValue>
                <Name>NumberFormatMnemonic</Name>
                <Value>US_NB</Value>
            </NameValue>
            <NameValue>
                <Name>WarnDuplicateCheckNumber</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>WarnDuplicateBillNumber</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>SignoutInactiveMinutes</Name>
                <Value>60</Value>
            </NameValue>
            <NameValue>
                <Name>AccountingInfoPrefs.ShowAccountNumbers</Name>
                <Value>false</Value>
            </NameValue>
        </OtherPrefs>
    </Preferences>
</IntuitResponse>
```

## Query preferences

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Preferences\n"
```

#### XML example

```sql
select * from Preferences
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "Preferences": {
    "EmailMessagesPrefs": {
      "InvoiceMessage": {
        "Message": "Your invoice is attached.  Please remit payment at your earliest convenience.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Invoice from Craig's Design and Landscaping Services"
      },
      "EstimateMessage": {
        "Message": "Please review the estimate below.  Feel free to contact us if you have any questions.\nWe look forward to working with you.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Estimate from Craig's Design and Landscaping Services"
      },
      "SalesReceiptMessage": {
        "Message": "Your sales receipt is attached.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Sales Receipt from Craig's Design and Landscaping Services"
      },
      "StatementMessage": {
        "Message": "Your statement is attached.  Please remit payment at your earliest convenience.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Statement from Craig's Design and Landscaping Services"
      }
    },
    "ProductAndServicesPrefs": {
      "QuantityWithPriceAndRate": true,
      "ForPurchase": true,
      "QuantityOnHand": true,
      "ForSales": true
    },
    "domain": "QBO",
    "SyncToken": "6",
    "ReportPrefs": {
      "ReportBasis": "Accrual",
      "CalcAgingReportFromTxnDate": false
    },
    "AccountingInfoPrefs": {
      "FirstMonthOfFiscalYear": "January",
      "UseAccountNumbers": true,
      "TaxYearMonth": "January",
      "ClassTrackingPerTxn": false,
      "TrackDepartments": true,
      "TaxForm": "6",
      "CustomerTerminology": "Customers",
      "BookCloseDate": "2018-12-31",
      "DepartmentTerminology": "Location",
      "ClassTrackingPerTxnLine": true
    },
    "SalesFormsPrefs": {
      "ETransactionPaymentEnabled": false,
      "CustomTxnNumbers": false,
      "AllowShipping": false,
      "AllowServiceDate": false,
      "ETransactionEnabledStatus": "NotApplicable",
      "DefaultCustomerMessage": "Thank you for your business and have a great day!",
      "EmailCopyToCompany": false,
      "AllowEstimates": true,
      "DefaultTerms": {
        "value": "3"
      },
      "AllowDiscount": true,
      "DefaultDiscountAccount": "86",
      "AllowDeposit": true,
      "AutoApplyPayments": true,
      "IPNSupportEnabled": false,
      "AutoApplyCredit": true,
      "CustomField": [
        {
          "CustomField": [
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom3"
            },
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom2"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom1"
            }
          ]
        },
        {
          "CustomField": [
            {
              "StringValue": "Crew #",
              "Type": "StringType",
              "Name": "SalesFormsPrefs.SalesCustomName1"
            }
          ]
        }
      ],
      "UsingPriceLevels": false,
      "ETransactionAttachPDF": false
    },
    "VendorAndPurchasesPrefs": {
      "BillableExpenseTracking": true,
      "TrackingByCustomer": true,
      "POCustomField": [
        {
          "CustomField": [
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom3"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom2"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom1"
            }
          ]
        },
        {
          "CustomField": [
            {
              "StringValue": "Sales Rep",
              "Type": "StringType",
              "Name": "PurchasePrefs.PurchaseCustomName2"
            },
            {
              "StringValue": "Crew #",
              "Type": "StringType",
              "Name": "PurchasePrefs.PurchaseCustomName1"
            }
          ]
        }
      ]
    },
    "TaxPrefs": {
      "TaxGroupCodeRef": {
        "value": "2"
      },
      "UsingSalesTax": true
    },
    "OtherPrefs": {
      "NameValue": [
        {
          "Name": "SalesFormsPrefs.DefaultCustomerMessage",
          "Value": "Thank you for your business and have a great day!"
        },
        {
          "Name": "SalesFormsPrefs.DefaultItem",
          "Value": "1"
        },
        {
          "Name": "DTXCopyMemo",
          "Value": "false"
        },
        {
          "Name": "UncategorizedAssetAccountId",
          "Value": "32"
        },
        {
          "Name": "UncategorizedIncomeAccountId",
          "Value": "30"
        },
        {
          "Name": "UncategorizedExpenseAccountId",
          "Value": "31"
        },
        {
          "Name": "SFCEnabled",
          "Value": "true"
        },
        {
          "Name": "DataPartner",
          "Value": "false"
        },
        {
          "Name": "Vendor1099Enabled",
          "Value": "true"
        },
        {
          "Name": "TimeTrackingFeatureEnabled",
          "Value": "true"
        },
        {
          "Name": "FDPEnabled",
          "Value": "false"
        },
        {
          "Name": "ProjectsEnabled",
          "Value": "false"
        },
        {
          "Name": "DateFormat",
          "Value": "Month Date Year separated by a slash"
        },
        {
          "Name": "DateFormatMnemonic",
          "Value": "MMDDYYYY_SEP_SLASH"
        },
        {
          "Name": "NumberFormat",
          "Value": "US Number Format"
        },
        {
          "Name": "NumberFormatMnemonic",
          "Value": "US_NB"
        },
        {
          "Name": "WarnDuplicateCheckNumber",
          "Value": "true"
        },
        {
          "Name": "WarnDuplicateBillNumber",
          "Value": "false"
        },
        {
          "Name": "SignoutInactiveMinutes",
          "Value": "60"
        },
        {
          "Name": "AccountingInfoPrefs.ShowAccountNumbers",
          "Value": "false"
        }
      ]
    },
    "sparse": false,
    "TimeTrackingPrefs": {
      "WorkWeekStartDate": "Monday",
      "MarkTimeEntriesBillable": true,
      "ShowBillRateToAll": false,
      "UseServices": true,
      "BillCustomers": true
    },
    "CurrencyPrefs": {
      "HomeCurrency": {
        "value": "USD"
      },
      "MultiCurrencyEnabled": false
    },
    "Id": "1",
    "MetaData": {
      "CreateTime": "2017-10-25T01:05:43-07:00",
      "LastUpdatedTime": "2018-03-08T13:24:26-08:00"
    }
  },
  "time": "2018-03-12T08:45:52.965-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2018-03-12T08:44:41.982-07:00">
    <Preferences domain="QBO" sparse="false">
        <Id>1</Id>
        <SyncToken>6</SyncToken>
        <MetaData>
            <CreateTime>2017-10-25T01:05:43-07:00</CreateTime>
            <LastUpdatedTime>2018-03-08T13:24:26-08:00</LastUpdatedTime>
        </MetaData>
        <AccountingInfoPrefs>
            <UseAccountNumbers>true</UseAccountNumbers>
            <TrackDepartments>true</TrackDepartments>
            <DepartmentTerminology>Location</DepartmentTerminology>
            <ClassTrackingPerTxn>false</ClassTrackingPerTxn>
            <ClassTrackingPerTxnLine>true</ClassTrackingPerTxnLine>
            <FirstMonthOfFiscalYear>January</FirstMonthOfFiscalYear>
            <TaxYearMonth>January</TaxYearMonth>
            <TaxForm>6</TaxForm>
            <BookCloseDate>2018-12-31</BookCloseDate>
            <CustomerTerminology>Customers</CustomerTerminology>
        </AccountingInfoPrefs>
        <ProductAndServicesPrefs>
            <ForSales>true</ForSales>
            <ForPurchase>true</ForPurchase>
            <QuantityWithPriceAndRate>true</QuantityWithPriceAndRate>
            <QuantityOnHand>true</QuantityOnHand>
        </ProductAndServicesPrefs>
        <SalesFormsPrefs>
            <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom3</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom2</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom1</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
            </CustomField>
            <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
                <CustomField>
                    <Name>SalesFormsPrefs.SalesCustomName1</Name>
                    <Type>StringType</Type>
                    <StringValue>Crew #</StringValue>
                </CustomField>
            </CustomField>
            <CustomTxnNumbers>false</CustomTxnNumbers>
            <EmailCopyToCompany>false</EmailCopyToCompany>
            <AllowDeposit>true</AllowDeposit>
            <AllowDiscount>true</AllowDiscount>
            <DefaultDiscountAccount>86</DefaultDiscountAccount>
            <AllowEstimates>true</AllowEstimates>
            <ETransactionEnabledStatus>NotApplicable</ETransactionEnabledStatus>
            <ETransactionAttachPDF>false</ETransactionAttachPDF>
            <ETransactionPaymentEnabled>false</ETransactionPaymentEnabled>
            <IPNSupportEnabled>false</IPNSupportEnabled>
            <AllowServiceDate>false</AllowServiceDate>
            <AllowShipping>false</AllowShipping>
            <DefaultTerms>3</DefaultTerms>
            <AutoApplyCredit>true</AutoApplyCredit>
            <AutoApplyPayments>true</AutoApplyPayments>
            <UsingPriceLevels>false</UsingPriceLevels>
            <DefaultCustomerMessage>Thank you for your business and have a great day!</DefaultCustomerMessage>
        </SalesFormsPrefs>
        <EmailMessagesPrefs>
            <InvoiceMessage>
                <Subject>Invoice from Craig's Design and Landscaping Services</Subject>
                <Message>Your invoice is attached.  Please remit payment at your earliest convenience.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </InvoiceMessage>
            <EstimateMessage>
                <Subject>Estimate from Craig's Design and Landscaping Services</Subject>
                <Message>Please review the estimate below.  Feel free to contact us if you have any questions.
We look forward to working with you.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </EstimateMessage>
            <SalesReceiptMessage>
                <Subject>Sales Receipt from Craig's Design and Landscaping Services</Subject>
                <Message>Your sales receipt is attached.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </SalesReceiptMessage>
            <StatementMessage>
                <Subject>Statement from Craig's Design and Landscaping Services</Subject>
                <Message>Your statement is attached.  Please remit payment at your earliest convenience.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </StatementMessage>
        </EmailMessagesPrefs>
        <VendorAndPurchasesPrefs>
            <TrackingByCustomer>true</TrackingByCustomer>
            <BillableExpenseTracking>true</BillableExpenseTracking>
            <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom3</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom2</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom1</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
            </POCustomField>
            <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
                <CustomField>
                    <Name>PurchasePrefs.PurchaseCustomName2</Name>
                    <Type>StringType</Type>
                    <StringValue>Sales Rep</StringValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.PurchaseCustomName1</Name>
                    <Type>StringType</Type>
                    <StringValue>Crew #</StringValue>
                </CustomField>
            </POCustomField>
        </VendorAndPurchasesPrefs>
        <TimeTrackingPrefs>
            <UseServices>true</UseServices>
            <BillCustomers>true</BillCustomers>
            <ShowBillRateToAll>false</ShowBillRateToAll>
            <WorkWeekStartDate>Monday</WorkWeekStartDate>
            <MarkTimeEntriesBillable>true</MarkTimeEntriesBillable>
        </TimeTrackingPrefs>
        <TaxPrefs>
            <UsingSalesTax>true</UsingSalesTax>
            <TaxGroupCodeRef>2</TaxGroupCodeRef>
        </TaxPrefs>
        <CurrencyPrefs>
            <MultiCurrencyEnabled>false</MultiCurrencyEnabled>
            <HomeCurrency>USD</HomeCurrency>
        </CurrencyPrefs>
        <ReportPrefs>
            <ReportBasis>Accrual</ReportBasis>
            <CalcAgingReportFromTxnDate>false</CalcAgingReportFromTxnDate>
        </ReportPrefs>
        <OtherPrefs>
            <NameValue>
                <Name>SalesFormsPrefs.DefaultCustomerMessage</Name>
                <Value>Thank you for your business and have a great day!</Value>
            </NameValue>
            <NameValue>
                <Name>SalesFormsPrefs.DefaultItem</Name>
                <Value>1</Value>
            </NameValue>
            <NameValue>
                <Name>DTXCopyMemo</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedAssetAccountId</Name>
                <Value>32</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedIncomeAccountId</Name>
                <Value>30</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedExpenseAccountId</Name>
                <Value>31</Value>
            </NameValue>
            <NameValue>
                <Name>SFCEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>DataPartner</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>Vendor1099Enabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>TimeTrackingFeatureEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>FDPEnabled</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>ProjectsEnabled</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>DateFormat</Name>
                <Value>Month Date Year separated by a slash</Value>
            </NameValue>
            <NameValue>
                <Name>DateFormatMnemonic</Name>
                <Value>MMDDYYYY_SEP_SLASH</Value>
            </NameValue>
            <NameValue>
                <Name>NumberFormat</Name>
                <Value>US Number Format</Value>
            </NameValue>
            <NameValue>
                <Name>NumberFormatMnemonic</Name>
                <Value>US_NB</Value>
            </NameValue>
            <NameValue>
                <Name>WarnDuplicateCheckNumber</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>WarnDuplicateBillNumber</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>SignoutInactiveMinutes</Name>
                <Value>60</Value>
            </NameValue>
            <NameValue>
                <Name>AccountingInfoPrefs.ShowAccountNumbers</Name>
                <Value>false</Value>
            </NameValue>
        </OtherPrefs>
    </Preferences>
</IntuitResponse>
```

## Read preferences

### Definition

- **Operation:** `GET /v3/company/<realmID>/preferences`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the Preferences details for the specified company.

### Returns

Returns the Preferences object.

#### Example

```json
{
  "Preferences": {
    "EmailMessagesPrefs": {
      "InvoiceMessage": {
        "Message": "Your invoice is attached.  Please remit payment at your earliest convenience.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Invoice from Craig's Design and Landscaping Services"
      },
      "EstimateMessage": {
        "Message": "Please review the estimate below.  Feel free to contact us if you have any questions.\nWe look forward to working with you.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Estimate from Craig's Design and Landscaping Services"
      },
      "SalesReceiptMessage": {
        "Message": "Your sales receipt is attached.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Sales Receipt from Craig's Design and Landscaping Services"
      },
      "StatementMessage": {
        "Message": "Your statement is attached.  Please remit payment at your earliest convenience.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Statement from Craig's Design and Landscaping Services"
      }
    },
    "ProductAndServicesPrefs": {
      "QuantityWithPriceAndRate": true,
      "ForPurchase": true,
      "QuantityOnHand": true,
      "ForSales": true
    },
    "domain": "QBO",
    "SyncToken": "6",
    "ReportPrefs": {
      "ReportBasis": "Accrual",
      "CalcAgingReportFromTxnDate": false
    },
    "AccountingInfoPrefs": {
      "FirstMonthOfFiscalYear": "January",
      "UseAccountNumbers": true,
      "TaxYearMonth": "January",
      "ClassTrackingPerTxn": false,
      "TrackDepartments": true,
      "TaxForm": "6",
      "CustomerTerminology": "Customers",
      "BookCloseDate": "2018-12-31",
      "DepartmentTerminology": "Location",
      "ClassTrackingPerTxnLine": true
    },
    "SalesFormsPrefs": {
      "ETransactionPaymentEnabled": false,
      "CustomTxnNumbers": false,
      "AllowShipping": false,
      "AllowServiceDate": false,
      "ETransactionEnabledStatus": "NotApplicable",
      "DefaultCustomerMessage": "Thank you for your business and have a great day!",
      "EmailCopyToCompany": false,
      "AllowEstimates": true,
      "DefaultTerms": {
        "value": "3"
      },
      "AllowDiscount": true,
      "DefaultDiscountAccount": "86",
      "AllowDeposit": true,
      "AutoApplyPayments": true,
      "IPNSupportEnabled": false,
      "AutoApplyCredit": true,
      "CustomField": [
        {
          "CustomField": [
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom3"
            },
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom2"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom1"
            }
          ]
        },
        {
          "CustomField": [
            {
              "StringValue": "Crew #",
              "Type": "StringType",
              "Name": "SalesFormsPrefs.SalesCustomName1"
            }
          ]
        }
      ],
      "UsingPriceLevels": false,
      "ETransactionAttachPDF": false
    },
    "VendorAndPurchasesPrefs": {
      "BillableExpenseTracking": true,
      "TrackingByCustomer": true,
      "POCustomField": [
        {
          "CustomField": [
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom3"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom2"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom1"
            }
          ]
        },
        {
          "CustomField": [
            {
              "StringValue": "Sales Rep",
              "Type": "StringType",
              "Name": "PurchasePrefs.PurchaseCustomName2"
            },
            {
              "StringValue": "Crew #",
              "Type": "StringType",
              "Name": "PurchasePrefs.PurchaseCustomName1"
            }
          ]
        }
      ]
    },
    "TaxPrefs": {
      "TaxGroupCodeRef": {
        "value": "2"
      },
      "UsingSalesTax": true
    },
    "OtherPrefs": {
      "NameValue": [
        {
          "Name": "SalesFormsPrefs.DefaultCustomerMessage",
          "Value": "Thank you for your business and have a great day!"
        },
        {
          "Name": "SalesFormsPrefs.DefaultItem",
          "Value": "1"
        },
        {
          "Name": "DTXCopyMemo",
          "Value": "false"
        },
        {
          "Name": "UncategorizedAssetAccountId",
          "Value": "32"
        },
        {
          "Name": "UncategorizedIncomeAccountId",
          "Value": "30"
        },
        {
          "Name": "UncategorizedExpenseAccountId",
          "Value": "31"
        },
        {
          "Name": "SFCEnabled",
          "Value": "true"
        },
        {
          "Name": "DataPartner",
          "Value": "false"
        },
        {
          "Name": "Vendor1099Enabled",
          "Value": "true"
        },
        {
          "Name": "TimeTrackingFeatureEnabled",
          "Value": "true"
        },
        {
          "Name": "FDPEnabled",
          "Value": "false"
        },
        {
          "Name": "ProjectsEnabled",
          "Value": "false"
        },
        {
          "Name": "DateFormat",
          "Value": "Month Date Year separated by a slash"
        },
        {
          "Name": "DateFormatMnemonic",
          "Value": "MMDDYYYY_SEP_SLASH"
        },
        {
          "Name": "NumberFormat",
          "Value": "US Number Format"
        },
        {
          "Name": "NumberFormatMnemonic",
          "Value": "US_NB"
        },
        {
          "Name": "WarnDuplicateCheckNumber",
          "Value": "true"
        },
        {
          "Name": "WarnDuplicateBillNumber",
          "Value": "false"
        },
        {
          "Name": "SignoutInactiveMinutes",
          "Value": "60"
        },
        {
          "Name": "AccountingInfoPrefs.ShowAccountNumbers",
          "Value": "false"
        }
      ]
    },
    "sparse": false,
    "TimeTrackingPrefs": {
      "WorkWeekStartDate": "Monday",
      "MarkTimeEntriesBillable": true,
      "ShowBillRateToAll": false,
      "UseServices": true,
      "BillCustomers": true
    },
    "CurrencyPrefs": {
      "HomeCurrency": {
        "value": "USD"
      },
      "MultiCurrencyEnabled": false
    },
    "Id": "1",
    "MetaData": {
      "CreateTime": "2017-10-25T01:05:43-07:00",
      "LastUpdatedTime": "2018-03-08T13:24:26-08:00"
    }
  },
  "time": "2018-03-12T08:22:43.280-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2018-03-12T08:44:41.982-07:00">
    <Preferences domain="QBO" sparse="false">
        <Id>1</Id>
        <SyncToken>6</SyncToken>
        <MetaData>
            <CreateTime>2017-10-25T01:05:43-07:00</CreateTime>
            <LastUpdatedTime>2018-03-08T13:24:26-08:00</LastUpdatedTime>
        </MetaData>
        <AccountingInfoPrefs>
            <UseAccountNumbers>true</UseAccountNumbers>
            <TrackDepartments>true</TrackDepartments>
            <DepartmentTerminology>Location</DepartmentTerminology>
            <ClassTrackingPerTxn>false</ClassTrackingPerTxn>
            <ClassTrackingPerTxnLine>true</ClassTrackingPerTxnLine>
            <FirstMonthOfFiscalYear>January</FirstMonthOfFiscalYear>
            <TaxYearMonth>January</TaxYearMonth>
            <TaxForm>6</TaxForm>
            <BookCloseDate>2018-12-31</BookCloseDate>
            <CustomerTerminology>Customers</CustomerTerminology>
        </AccountingInfoPrefs>
        <ProductAndServicesPrefs>
            <ForSales>true</ForSales>
            <ForPurchase>true</ForPurchase>
            <QuantityWithPriceAndRate>true</QuantityWithPriceAndRate>
            <QuantityOnHand>true</QuantityOnHand>
        </ProductAndServicesPrefs>
        <SalesFormsPrefs>
            <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom3</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom2</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom1</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
            </CustomField>
            <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
                <CustomField>
                    <Name>SalesFormsPrefs.SalesCustomName1</Name>
                    <Type>StringType</Type>
                    <StringValue>Crew #</StringValue>
                </CustomField>
            </CustomField>
            <CustomTxnNumbers>false</CustomTxnNumbers>
            <EmailCopyToCompany>false</EmailCopyToCompany>
            <AllowDeposit>true</AllowDeposit>
            <AllowDiscount>true</AllowDiscount>
            <DefaultDiscountAccount>86</DefaultDiscountAccount>
            <AllowEstimates>true</AllowEstimates>
            <ETransactionEnabledStatus>NotApplicable</ETransactionEnabledStatus>
            <ETransactionAttachPDF>false</ETransactionAttachPDF>
            <ETransactionPaymentEnabled>false</ETransactionPaymentEnabled>
            <IPNSupportEnabled>false</IPNSupportEnabled>
            <AllowServiceDate>false</AllowServiceDate>
            <AllowShipping>false</AllowShipping>
            <DefaultTerms>3</DefaultTerms>
            <AutoApplyCredit>true</AutoApplyCredit>
            <AutoApplyPayments>true</AutoApplyPayments>
            <UsingPriceLevels>false</UsingPriceLevels>
            <DefaultCustomerMessage>Thank you for your business and have a great day!</DefaultCustomerMessage>
        </SalesFormsPrefs>
        <EmailMessagesPrefs>
            <InvoiceMessage>
                <Subject>Invoice from Craig's Design and Landscaping Services</Subject>
                <Message>Your invoice is attached.  Please remit payment at your earliest convenience.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </InvoiceMessage>
            <EstimateMessage>
                <Subject>Estimate from Craig's Design and Landscaping Services</Subject>
                <Message>Please review the estimate below.  Feel free to contact us if you have any questions.
We look forward to working with you.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </EstimateMessage>
            <SalesReceiptMessage>
                <Subject>Sales Receipt from Craig's Design and Landscaping Services</Subject>
                <Message>Your sales receipt is attached.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </SalesReceiptMessage>
            <StatementMessage>
                <Subject>Statement from Craig's Design and Landscaping Services</Subject>
                <Message>Your statement is attached.  Please remit payment at your earliest convenience.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </StatementMessage>
        </EmailMessagesPrefs>
        <VendorAndPurchasesPrefs>
            <TrackingByCustomer>true</TrackingByCustomer>
            <BillableExpenseTracking>true</BillableExpenseTracking>
            <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom3</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom2</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom1</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
            </POCustomField>
            <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
                <CustomField>
                    <Name>PurchasePrefs.PurchaseCustomName2</Name>
                    <Type>StringType</Type>
                    <StringValue>Sales Rep</StringValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.PurchaseCustomName1</Name>
                    <Type>StringType</Type>
                    <StringValue>Crew #</StringValue>
                </CustomField>
            </POCustomField>
        </VendorAndPurchasesPrefs>
        <TimeTrackingPrefs>
            <UseServices>true</UseServices>
            <BillCustomers>true</BillCustomers>
            <ShowBillRateToAll>false</ShowBillRateToAll>
            <WorkWeekStartDate>Monday</WorkWeekStartDate>
            <MarkTimeEntriesBillable>true</MarkTimeEntriesBillable>
        </TimeTrackingPrefs>
        <TaxPrefs>
            <UsingSalesTax>true</UsingSalesTax>
            <TaxGroupCodeRef>2</TaxGroupCodeRef>
        </TaxPrefs>
        <CurrencyPrefs>
            <MultiCurrencyEnabled>false</MultiCurrencyEnabled>
            <HomeCurrency>USD</HomeCurrency>
        </CurrencyPrefs>
        <ReportPrefs>
            <ReportBasis>Accrual</ReportBasis>
            <CalcAgingReportFromTxnDate>false</CalcAgingReportFromTxnDate>
        </ReportPrefs>
        <OtherPrefs>
            <NameValue>
                <Name>SalesFormsPrefs.DefaultCustomerMessage</Name>
                <Value>Thank you for your business and have a great day!</Value>
            </NameValue>
            <NameValue>
                <Name>SalesFormsPrefs.DefaultItem</Name>
                <Value>1</Value>
            </NameValue>
            <NameValue>
                <Name>DTXCopyMemo</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedAssetAccountId</Name>
                <Value>32</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedIncomeAccountId</Name>
                <Value>30</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedExpenseAccountId</Name>
                <Value>31</Value>
            </NameValue>
            <NameValue>
                <Name>SFCEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>DataPartner</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>Vendor1099Enabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>TimeTrackingFeatureEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>FDPEnabled</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>ProjectsEnabled</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>DateFormat</Name>
                <Value>Month Date Year separated by a slash</Value>
            </NameValue>
            <NameValue>
                <Name>DateFormatMnemonic</Name>
                <Value>MMDDYYYY_SEP_SLASH</Value>
            </NameValue>
            <NameValue>
                <Name>NumberFormat</Name>
                <Value>US Number Format</Value>
            </NameValue>
            <NameValue>
                <Name>NumberFormatMnemonic</Name>
                <Value>US_NB</Value>
            </NameValue>
            <NameValue>
                <Name>WarnDuplicateCheckNumber</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>WarnDuplicateBillNumber</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>SignoutInactiveMinutes</Name>
                <Value>60</Value>
            </NameValue>
            <NameValue>
                <Name>AccountingInfoPrefs.ShowAccountNumbers</Name>
                <Value>false</Value>
            </NameValue>
        </OtherPrefs>
    </Preferences>
</IntuitResponse>
```

## Full update preferences

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/preferences`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable preference fields. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL or reverted to a default value. The ID of the object to update is specified in the request body.

### Request Body

Schema: `preferencesresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "ProductAndServicesPrefs": {
    "ForPurchase": true,
    "ForSales": true
  },
  "SyncToken": "20",
  "sparse": false,
  "SalesFormsPrefs": {
    "AllowEstimates": true
  },
  "Id": "1"
}
```

#### XML example

```xml
<Preferences xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
   <Id>1</Id>
   <SyncToken>2</SyncToken>
   <MetaData>
      <CreateTime>2013-04-20T10:32:18-07:00</CreateTime>
      <LastUpdatedTime>2013-07-11T17:31:39-07:00</LastUpdatedTime>
   </MetaData>
   <AccountingInfoPrefs>
      <CustomerTerminology>customer</CustomerTerminology>
   </AccountingInfoPrefs>
   <ProductAndServicesPrefs>
      <ForSales>false</ForSales>
      <ForPurchase>false</ForPurchase>
      <QuantityWithPriceAndRate>false</QuantityWithPriceAndRate>
      <QuantityOnHand>true</QuantityOnHand>
   </ProductAndServicesPrefs>
   <SalesFormsPrefs>
      <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
         <CustomField>
            <Name>SalesFormsPrefs.UseSalesCustom3</Name>
            <Type>BooleanType</Type>
            <BooleanValue>true</BooleanValue>
         </CustomField>
         <CustomField>
            <Name>SalesFormsPrefs.UseSalesCustom2</Name>
            <Type>BooleanType</Type>
            <BooleanValue>true</BooleanValue>
         </CustomField>
         <CustomField>
            <Name>SalesFormsPrefs.UseSalesCustom1</Name>
            <Type>BooleanType</Type>
            <BooleanValue>true</BooleanValue>
         </CustomField>
      </CustomField>
      <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
         <CustomField>
            <Name>SalesFormsPrefs.PrintOrderSalesCustom3</Name>
            <Type>StringType</Type>
            <StringValue>3</StringValue>
         </CustomField>
         <CustomField>
            <Name>SalesFormsPrefs.SalesCustomName3</Name>
            <Type>StringType</Type>
            <StringValue>Custom 3</StringValue>
         </CustomField>
         <CustomField>
            <Name>SalesFormsPrefs.PrintOrderSalesCustom2</Name>
            <Type>StringType</Type>
            <StringValue>2</StringValue>
         </CustomField>
         <CustomField>
            <Name>SalesFormsPrefs.PrintOrderSalesCustom1</Name>
            <Type>StringType</Type>
            <StringValue>1</StringValue>
         </CustomField>
         <CustomField>
            <Name>SalesFormsPrefs.SalesCustomName1</Name>
            <Type>StringType</Type>
            <StringValue>Custom 1</StringValue>
         </CustomField>
         <CustomField>
            <Name>SalesFormsPrefs.SalesCustomName2</Name>
            <Type>StringType</Type>
            <StringValue>Custom 2</StringValue>
         </CustomField>
      </CustomField>
      <CustomTxnNumbers>false</CustomTxnNumbers>
      <AllowDeposit>true</AllowDeposit>
      <AllowDiscount>true</AllowDiscount>
      <AllowEstimates>false</AllowEstimates>
      <IPNSupportEnabled>false</IPNSupportEnabled>
      <AllowServiceDate>true</AllowServiceDate>
      <AllowShipping>true</AllowShipping>
      <DefaultTerms>3</DefaultTerms>
      <DefaultCustomerMessage>CustomerMessage 0mw270kOzJR0</DefaultCustomerMessage>
   </SalesFormsPrefs>
   <VendorAndPurchasesPrefs>
      <TrackingByCustomer>true</TrackingByCustomer>
      <BillableExpenseTracking>true</BillableExpenseTracking>
      <DefaultTerms name="Net 30">3</DefaultTerms>
      <DefaultMarkup>10</DefaultMarkup>
      <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
         <CustomField>
            <Name>PurchasePrefs.UsePurchaseCustom3</Name>
            <Type>BooleanType</Type>
            <BooleanValue>true</BooleanValue>
         </CustomField>
         <CustomField>
            <Name>PurchasePrefs.UsePurchaseCustom2</Name>
            <Type>BooleanType</Type>
            <BooleanValue>true</BooleanValue>
         </CustomField>
         <CustomField>
            <Name>PurchasePrefs.UsePurchaseCustom1</Name>
            <Type>BooleanType</Type>
            <BooleanValue>true</BooleanValue>
         </CustomField>
      </POCustomField>
      <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
         <CustomField>
            <Name>PurchasePrefs.PurchaseCustomName3</Name>
            <Type>StringType</Type>
            <StringValue>Custom 3</StringValue>
         </CustomField>
         <CustomField>
            <Name>PurchasePrefs.PurchaseCustomName2</Name>
            <Type>StringType</Type>
            <StringValue>Custom 2</StringValue>
         </CustomField>
         <CustomField>
            <Name>PurchasePrefs.PurchaseCustomName1</Name>
            <Type>StringType</Type>
            <StringValue>Custom 1</StringValue>
         </CustomField>
         <CustomField>
            <Name>PurchasePrefs.PrintOrderPurchaseCustom2</Name>
            <Type>StringType</Type>
            <StringValue>2</StringValue>
         </CustomField>
         <CustomField>
            <Name>PurchasePrefs.PrintOrderPurchaseCustom3</Name>
            <Type>StringType</Type>
            <StringValue>3</StringValue>
         </CustomField>
         <CustomField>
            <Name>PurchasePrefs.PrintOrderPurchaseCustom1</Name>
            <Type>StringType</Type>
            <StringValue>1</StringValue>
         </CustomField>
      </POCustomField>
   </VendorAndPurchasesPrefs>
   <TimeTrackingPrefs>
      <UseServices>true</UseServices>
      <BillCustomers>true</BillCustomers>
      <ShowBillRateToAll>true</ShowBillRateToAll>
      <WorkWeekStartDate>Sunday</WorkWeekStartDate>
      <MarkTimeEntriesBillable>true</MarkTimeEntriesBillable>
   </TimeTrackingPrefs>
   <TaxPrefs>
      <UsingSalesTax>true</UsingSalesTax>
   </TaxPrefs>
   <CurrencyPrefs>
      <MultiCurrencyEnabled>false</MultiCurrencyEnabled>
      <HomeCurrency>USD</HomeCurrency>
   </CurrencyPrefs>
   <OtherPrefs>
      <NameValue>
         <Name>SalesFormsPrefs.DefaultCustomerMessage</Name>
      </NameValue>
      <NameValue>
         <Name>SalesFormsPrefs.DefaultItem</Name>
         <Value>1</Value>
      </NameValue>
   </OtherPrefs>
</Preferences>
```

### Returns

The preferences response body.

#### Example

```json
{
  "Preferences": {
    "EmailMessagesPrefs": {
      "InvoiceMessage": {
        "Message": "Your invoice is attached.  Please remit payment at your earliest convenience.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Invoice from Craig's Design and Landscaping Services"
      },
      "EstimateMessage": {
        "Message": "Please review the estimate below.  Feel free to contact us if you have any questions.\nWe look forward to working with you.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Estimate from Craig's Design and Landscaping Services"
      },
      "SalesReceiptMessage": {
        "Message": "Your sales receipt is attached.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Sales Receipt from Craig's Design and Landscaping Services"
      },
      "StatementMessage": {
        "Message": "Your statement is attached.  Please remit payment at your earliest convenience.\nThank you for your business - we appreciate it very much.\n\nSincerely,\nCraig's Design and Landscaping Services",
        "Subject": "Statement from Craig's Design and Landscaping Services"
      }
    },
    "ProductAndServicesPrefs": {
      "QuantityWithPriceAndRate": true,
      "ForPurchase": true,
      "QuantityOnHand": true,
      "ForSales": true
    },
    "domain": "QBO",
    "SyncToken": "6",
    "ReportPrefs": {
      "ReportBasis": "Accrual",
      "CalcAgingReportFromTxnDate": false
    },
    "AccountingInfoPrefs": {
      "FirstMonthOfFiscalYear": "January",
      "UseAccountNumbers": true,
      "TaxYearMonth": "January",
      "ClassTrackingPerTxn": false,
      "TrackDepartments": true,
      "TaxForm": "6",
      "CustomerTerminology": "Customers",
      "BookCloseDate": "2018-12-31",
      "DepartmentTerminology": "Location",
      "ClassTrackingPerTxnLine": true
    },
    "SalesFormsPrefs": {
      "ETransactionPaymentEnabled": false,
      "CustomTxnNumbers": false,
      "AllowShipping": false,
      "AllowServiceDate": false,
      "ETransactionEnabledStatus": "NotApplicable",
      "DefaultCustomerMessage": "Thank you for your business and have a great day!",
      "EmailCopyToCompany": false,
      "AllowEstimates": true,
      "DefaultTerms": {
        "value": "3"
      },
      "AllowDiscount": true,
      "DefaultDiscountAccount": "86",
      "AllowDeposit": true,
      "AutoApplyPayments": true,
      "IPNSupportEnabled": false,
      "AutoApplyCredit": true,
      "CustomField": [
        {
          "CustomField": [
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom3"
            },
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom2"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "SalesFormsPrefs.UseSalesCustom1"
            }
          ]
        },
        {
          "CustomField": [
            {
              "StringValue": "Crew #",
              "Type": "StringType",
              "Name": "SalesFormsPrefs.SalesCustomName1"
            }
          ]
        }
      ],
      "UsingPriceLevels": false,
      "ETransactionAttachPDF": false
    },
    "VendorAndPurchasesPrefs": {
      "BillableExpenseTracking": true,
      "TrackingByCustomer": true,
      "POCustomField": [
        {
          "CustomField": [
            {
              "BooleanValue": false,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom3"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom2"
            },
            {
              "BooleanValue": true,
              "Type": "BooleanType",
              "Name": "PurchasePrefs.UsePurchaseCustom1"
            }
          ]
        },
        {
          "CustomField": [
            {
              "StringValue": "Sales Rep",
              "Type": "StringType",
              "Name": "PurchasePrefs.PurchaseCustomName2"
            },
            {
              "StringValue": "Crew #",
              "Type": "StringType",
              "Name": "PurchasePrefs.PurchaseCustomName1"
            }
          ]
        }
      ]
    },
    "TaxPrefs": {
      "TaxGroupCodeRef": {
        "value": "2"
      },
      "UsingSalesTax": true
    },
    "OtherPrefs": {
      "NameValue": [
        {
          "Name": "SalesFormsPrefs.DefaultCustomerMessage",
          "Value": "Thank you for your business and have a great day!"
        },
        {
          "Name": "SalesFormsPrefs.DefaultItem",
          "Value": "1"
        },
        {
          "Name": "DTXCopyMemo",
          "Value": "false"
        },
        {
          "Name": "UncategorizedAssetAccountId",
          "Value": "32"
        },
        {
          "Name": "UncategorizedIncomeAccountId",
          "Value": "30"
        },
        {
          "Name": "UncategorizedExpenseAccountId",
          "Value": "31"
        },
        {
          "Name": "SFCEnabled",
          "Value": "true"
        },
        {
          "Name": "DataPartner",
          "Value": "false"
        },
        {
          "Name": "Vendor1099Enabled",
          "Value": "true"
        },
        {
          "Name": "TimeTrackingFeatureEnabled",
          "Value": "true"
        },
        {
          "Name": "FDPEnabled",
          "Value": "false"
        },
        {
          "Name": "ProjectsEnabled",
          "Value": "false"
        },
        {
          "Name": "DateFormat",
          "Value": "Month Date Year separated by a slash"
        },
        {
          "Name": "DateFormatMnemonic",
          "Value": "MMDDYYYY_SEP_SLASH"
        },
        {
          "Name": "NumberFormat",
          "Value": "US Number Format"
        },
        {
          "Name": "NumberFormatMnemonic",
          "Value": "US_NB"
        },
        {
          "Name": "WarnDuplicateCheckNumber",
          "Value": "true"
        },
        {
          "Name": "WarnDuplicateBillNumber",
          "Value": "false"
        },
        {
          "Name": "SignoutInactiveMinutes",
          "Value": "60"
        },
        {
          "Name": "AccountingInfoPrefs.ShowAccountNumbers",
          "Value": "false"
        }
      ]
    },
    "sparse": false,
    "TimeTrackingPrefs": {
      "WorkWeekStartDate": "Monday",
      "MarkTimeEntriesBillable": true,
      "ShowBillRateToAll": false,
      "UseServices": true,
      "BillCustomers": true
    },
    "CurrencyPrefs": {
      "HomeCurrency": {
        "value": "USD"
      },
      "MultiCurrencyEnabled": false
    },
    "Id": "1",
    "MetaData": {
      "CreateTime": "2017-10-25T01:05:43-07:00",
      "LastUpdatedTime": "2018-03-08T13:24:26-08:00"
    }
  },
  "time": "2018-03-12T08:45:52.965-07:00"
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2018-03-12T08:44:41.982-07:00">
    <Preferences domain="QBO" sparse="false">
        <Id>1</Id>
        <SyncToken>6</SyncToken>
        <MetaData>
            <CreateTime>2017-10-25T01:05:43-07:00</CreateTime>
            <LastUpdatedTime>2018-03-08T13:24:26-08:00</LastUpdatedTime>
        </MetaData>
        <AccountingInfoPrefs>
            <UseAccountNumbers>true</UseAccountNumbers>
            <TrackDepartments>true</TrackDepartments>
            <DepartmentTerminology>Location</DepartmentTerminology>
            <ClassTrackingPerTxn>false</ClassTrackingPerTxn>
            <ClassTrackingPerTxnLine>true</ClassTrackingPerTxnLine>
            <FirstMonthOfFiscalYear>January</FirstMonthOfFiscalYear>
            <TaxYearMonth>January</TaxYearMonth>
            <TaxForm>6</TaxForm>
            <BookCloseDate>2018-12-31</BookCloseDate>
            <CustomerTerminology>Customers</CustomerTerminology>
        </AccountingInfoPrefs>
        <ProductAndServicesPrefs>
            <ForSales>true</ForSales>
            <ForPurchase>true</ForPurchase>
            <QuantityWithPriceAndRate>true</QuantityWithPriceAndRate>
            <QuantityOnHand>true</QuantityOnHand>
        </ProductAndServicesPrefs>
        <SalesFormsPrefs>
            <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom3</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom2</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>SalesFormsPrefs.UseSalesCustom1</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
            </CustomField>
            <CustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
                <CustomField>
                    <Name>SalesFormsPrefs.SalesCustomName1</Name>
                    <Type>StringType</Type>
                    <StringValue>Crew #</StringValue>
                </CustomField>
            </CustomField>
            <CustomTxnNumbers>false</CustomTxnNumbers>
            <EmailCopyToCompany>false</EmailCopyToCompany>
            <AllowDeposit>true</AllowDeposit>
            <AllowDiscount>true</AllowDiscount>
            <DefaultDiscountAccount>86</DefaultDiscountAccount>
            <AllowEstimates>true</AllowEstimates>
            <ETransactionEnabledStatus>NotApplicable</ETransactionEnabledStatus>
            <ETransactionAttachPDF>false</ETransactionAttachPDF>
            <ETransactionPaymentEnabled>false</ETransactionPaymentEnabled>
            <IPNSupportEnabled>false</IPNSupportEnabled>
            <AllowServiceDate>false</AllowServiceDate>
            <AllowShipping>false</AllowShipping>
            <DefaultTerms>3</DefaultTerms>
            <AutoApplyCredit>true</AutoApplyCredit>
            <AutoApplyPayments>true</AutoApplyPayments>
            <UsingPriceLevels>false</UsingPriceLevels>
            <DefaultCustomerMessage>Thank you for your business and have a great day!</DefaultCustomerMessage>
        </SalesFormsPrefs>
        <EmailMessagesPrefs>
            <InvoiceMessage>
                <Subject>Invoice from Craig's Design and Landscaping Services</Subject>
                <Message>Your invoice is attached.  Please remit payment at your earliest convenience.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </InvoiceMessage>
            <EstimateMessage>
                <Subject>Estimate from Craig's Design and Landscaping Services</Subject>
                <Message>Please review the estimate below.  Feel free to contact us if you have any questions.
We look forward to working with you.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </EstimateMessage>
            <SalesReceiptMessage>
                <Subject>Sales Receipt from Craig's Design and Landscaping Services</Subject>
                <Message>Your sales receipt is attached.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </SalesReceiptMessage>
            <StatementMessage>
                <Subject>Statement from Craig's Design and Landscaping Services</Subject>
                <Message>Your statement is attached.  Please remit payment at your earliest convenience.
Thank you for your business - we appreciate it very much.

Sincerely,
Craig's Design and Landscaping Services</Message>
            </StatementMessage>
        </EmailMessagesPrefs>
        <VendorAndPurchasesPrefs>
            <TrackingByCustomer>true</TrackingByCustomer>
            <BillableExpenseTracking>true</BillableExpenseTracking>
            <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="BooleanTypeCustomFieldDefinition">
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom3</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>false</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom2</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.UsePurchaseCustom1</Name>
                    <Type>BooleanType</Type>
                    <BooleanValue>true</BooleanValue>
                </CustomField>
            </POCustomField>
            <POCustomField xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="StringTypeCustomFieldDefinition">
                <CustomField>
                    <Name>PurchasePrefs.PurchaseCustomName2</Name>
                    <Type>StringType</Type>
                    <StringValue>Sales Rep</StringValue>
                </CustomField>
                <CustomField>
                    <Name>PurchasePrefs.PurchaseCustomName1</Name>
                    <Type>StringType</Type>
                    <StringValue>Crew #</StringValue>
                </CustomField>
            </POCustomField>
        </VendorAndPurchasesPrefs>
        <TimeTrackingPrefs>
            <UseServices>true</UseServices>
            <BillCustomers>true</BillCustomers>
            <ShowBillRateToAll>false</ShowBillRateToAll>
            <WorkWeekStartDate>Monday</WorkWeekStartDate>
            <MarkTimeEntriesBillable>true</MarkTimeEntriesBillable>
        </TimeTrackingPrefs>
        <TaxPrefs>
            <UsingSalesTax>true</UsingSalesTax>
            <TaxGroupCodeRef>2</TaxGroupCodeRef>
        </TaxPrefs>
        <CurrencyPrefs>
            <MultiCurrencyEnabled>false</MultiCurrencyEnabled>
            <HomeCurrency>USD</HomeCurrency>
        </CurrencyPrefs>
        <ReportPrefs>
            <ReportBasis>Accrual</ReportBasis>
            <CalcAgingReportFromTxnDate>false</CalcAgingReportFromTxnDate>
        </ReportPrefs>
        <OtherPrefs>
            <NameValue>
                <Name>SalesFormsPrefs.DefaultCustomerMessage</Name>
                <Value>Thank you for your business and have a great day!</Value>
            </NameValue>
            <NameValue>
                <Name>SalesFormsPrefs.DefaultItem</Name>
                <Value>1</Value>
            </NameValue>
            <NameValue>
                <Name>DTXCopyMemo</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedAssetAccountId</Name>
                <Value>32</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedIncomeAccountId</Name>
                <Value>30</Value>
            </NameValue>
            <NameValue>
                <Name>UncategorizedExpenseAccountId</Name>
                <Value>31</Value>
            </NameValue>
            <NameValue>
                <Name>SFCEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>DataPartner</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>Vendor1099Enabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>TimeTrackingFeatureEnabled</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>FDPEnabled</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>ProjectsEnabled</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>DateFormat</Name>
                <Value>Month Date Year separated by a slash</Value>
            </NameValue>
            <NameValue>
                <Name>DateFormatMnemonic</Name>
                <Value>MMDDYYYY_SEP_SLASH</Value>
            </NameValue>
            <NameValue>
                <Name>NumberFormat</Name>
                <Value>US Number Format</Value>
            </NameValue>
            <NameValue>
                <Name>NumberFormatMnemonic</Name>
                <Value>US_NB</Value>
            </NameValue>
            <NameValue>
                <Name>WarnDuplicateCheckNumber</Name>
                <Value>true</Value>
            </NameValue>
            <NameValue>
                <Name>WarnDuplicateBillNumber</Name>
                <Value>false</Value>
            </NameValue>
            <NameValue>
                <Name>SignoutInactiveMinutes</Name>
                <Value>60</Value>
            </NameValue>
            <NameValue>
                <Name>AccountingInfoPrefs.ShowAccountNumbers</Name>
                <Value>false</Value>
            </NameValue>
        </OtherPrefs>
    </Preferences>
</IntuitResponse>
```
