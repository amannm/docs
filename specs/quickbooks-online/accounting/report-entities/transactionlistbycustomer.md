# TransactionListByCustomer

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/transactionlistbycustomer
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Report entities](index.md) / TransactionListByCustomer
> Canonical entity: `TransactionListByCustomer`

The information below provides a reference on how to access the Transaction List By Customer report from the QuickBooks Online Report Service.

## The transaction list by customer report object

The table below lists all possible attributes that can be returned in the report response. Values are not localized unless indicated. [Click here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions) to download the latest XSD.

### transactionlistreporttoplevel

Model type: `object`

#### `Header`

The report header.

<details>
<summary>Child attributes for `Header`</summary>

##### transactionlistreportheader

Model type: `object`

###### `Customer`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `ReportName`

Type: `String`

Name of the report.

###### `Vendor`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `Option`

Container for one or more name/value pairs that return additional information about the report contents.

<details>
<summary>Child attributes for `Option`</summary>

###### reportoption

Model type: `object`

###### `name`

Type: `String`

Supported Names: `AccountingStandard`—Indicates the accounting standard being used for this report. Returned with ProfitAndLoss and BalanceSheet reports, only. `NoReportData`—Used to signal whether report contains data. If `true`, report contains no data. If `false`, report contains data. Returned for every report type.

###### `value`

Type: `String`

The value of the parameter, as passed in with the report endpoint URL.

</details>

###### `Item`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `Employee`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `ReportBasis`

Type: `ReportBasisEnum`

Accounting method. Possible values include `Cash` and `Accrual`.

###### `StartPeriod`

Type: `String`

The date specified by the start_date query parameter submitted with the request. Format is `yyyy-mm-dd`.

###### `Currency`

Type: `String`

A string containing the currency code associated with the report.

###### `EndPeriod`

Type: `String`

The date specified by the end_date query parameter submitted with the request. Format is `yyyy-mm-dd`.

###### `Time`

Type: `DateTime`

Date and timestamp of the report.

###### `Department`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

###### `SummarizeColumnsBy`

Type: `SummarizeColumnsByEnum`

The method by which report columns are organized. This contains the value specified by the `summarize_column_by` query parameter submitted with the request.

</details>

#### `Rows`

Top level container holding information for report rows.

<details>
<summary>Child attributes for `Rows`</summary>

##### reportrows

Model type: `object`

###### `Row [0..n]`

Represents a row in a report. A group of rows is enclosed in a `Rows` container. Rows may be nested either as a single row or in sets, based on the accounts represented in the report and query parameters specified in the request. Parameters:

`type`—As an enclosing section of sub-rows, this is always the string, `Section`. As a leaf row, this is always the string, `Data`.

`group`—The group name, valid when `type=Section`. Possible values include: `Income`, `COGS`, `GrossProfit`, `Expenses`, `NetOperatingIncome`, `OtherIncome`, `OtherExpenses`, `NetOtherIncome`, `NetIncome`

<details>
<summary>Child attributes for `Row [0..n]`</summary>

###### reportrow

Model type: `object`

###### `ColData`

Information for each column of a leaf row `Row type=Data`. There must be a `ColData` definition for each column defined in the `Columns` section. Parameters:

`id`—The reference id of the entity as returned in the Identity field. Returned where applicable.

`value`—The value for column. The type of value is based on the column type.

`href`—The link to the quick zoom data for this cell, available when the report endpoint specifies the `qzurl` query parameter. The `qzurl` query parameter is supported on a report by report basis; check the list of query parameters for the specific report to determine support.

The value of the parameter is localized.

###### `Summary`

Summary row for a report section. It is the cumulative total amount of money in the account, including the sub accounts.

###### `Rows`

Container for one or more leaf rows.

###### `Header`

Header row for the report section.

</details>

</details>

#### `Columns`

Top level container holding information for report columns or subcolumns.

<details>
<summary>Child attributes for `Columns`</summary>

##### reportcolumns

Model type: `object`

###### `Column [0..n]`

Container for an individual report column definition.

<details>
<summary>Child attributes for `Column [0..n]`</summary>

###### reportcolumn

Model type: `object`

###### `ColType`

Type: `ColumnTypeEnum`

The type of information found in the column. Possible values include:

`Account`—This column in the row represents an account for the row item. The row further defines the specific account.

`Money`—This column in the row represents an amount for the row item.

###### `ColTitle`

Type: `String`

The column label. This string appears at the top of the column. If not defined, the column does not have a label. The value of this attribute is localized.

</details>

</details>

#### Example

```json
{
  "Header": {
    "ReportName": "TransactionListByCustomer",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "true"
      }
    ],
    "StartPeriod": "2016-06-01",
    "Currency": "USD",
    "EndPeriod": "2016-07-31",
    "Time": "2020-09-29T14:20:06-07:00"
  },
  "Rows": {},
  "Columns": {
    "Column": [
      {
        "ColTitle": "Date",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "tx_date"
          }
        ]
      },
      {
        "ColTitle": "Transaction Type",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "txn_type"
          }
        ]
      },
      {
        "ColTitle": "Num",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "doc_num"
          }
        ]
      },
      {
        "ColTitle": "Posting",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "is_no_post"
          }
        ]
      },
      {
        "ColTitle": "Memo/Description",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "memo"
          }
        ]
      },
      {
        "ColTitle": "Account",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "account_name"
          }
        ]
      },
      {
        "ColTitle": "Amount ",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "amount"
          }
        ]
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/TransactionListByCustomer?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `transactionlistbycustomerquery`

<details>
<summary>Show schema for `transactionlistbycustomerquery`</summary>

#### transactionlistbycustomerquery

Model type: `object`

##### `date_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year, This Calendar Quarter, This Calendar Quarter-to-date, Last Calendar Quarter, Last Calendar Quarter-to-date, Next Calendar Quarter, This Calendar Year, This Calendar Year-to-date, Last Calendar Year, Last Calendar Year-to-date, Next Calendar Year

##### `payment_method`

Required: Optional
Type: `String`
Default: Include all payment methods

Filters report contents based on payment method.
Supported Values: `Cash`, `Check`, `Dinners Club`, `American Express`, `Discover`, `MasterCard`, `Visa`, `Credit Card`

##### `duedate_macro`

Required: Optional
Type: `String`
Default: All dates

Predefined date range of due dates for balances to include in the report; otherwise, use the start_duedate and end_duedate to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `arpaid`

Required: Optional
Type: `String`
Default: <span class="literal">All</span>

Supported Values:`All`, `Paid`, `Unpaid`

##### `bothamount`

Required: Optional
Type: `String`
Default: Include data for all amounts

Filters report contents to include information for specified transaction amount. For example, `bothamount=1233.45` limits report contents to transactions of amount 1233.45.

##### `transaction_type`

Required: Optional
Type: `String`
Default: Return data for all transactions

Filters report contents based transaction type. Supported values include:
CreditCardCharge, Check, Invoice, ReceivePayment, JournalEntry, Bill, CreditCardCredit, VendorCredit, Credit, BillPaymentCheck, BillPaymentCreditCard, Charge, Transfer, Deposit, Statement, BillableCharge, TimeActivity, CashPurchase, SalesReceipt, CreditMemo, CreditRefund, Estimate, InventoryQuantityAdjustment, PurchaseOrder, GlobalTaxPayment, GlobalTaxAdjustment, Service Tax Refund, Service Tax Gross Adjustment, Service Tax Reversal, Service Tax Defer, Service Tax Partial Utilisation

##### `docnum`

Required: Optional
Type: `String`
Default: Include data for all docnums.

Filters report contents to include information for specified transaction number, as found in the `docnum` parameter of the transaction object.

##### `start_moddate`

Required: Optional
Type: `String`
Default: <span class="literal">moddate_macro</span>

(Account List Detail) Specify an explicit account modification report date range, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use the `moddate_macro` to cover a standard report date range.

##### `source_account_type`

Required: Optional
Type: `String`
Default: <span class="literal">All account types</span>

Account type from which transactions are included in the report.
Supported Values: AccountsPayable, AccountsReceivable, Bank, CostOfGoodsSold, CreditCard, Equity, Expense, FixedAsset, Income, LongTermLiability, NonPosting, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome

<details>
<summary>Show supported account types and values</summary>

#### ATTRIBUTES

| Name | Description |
| --- | --- |
| **FOR ACCOUNT TYPE** | **SPECIFY THESE VALUES** |
| All Balance Sheet accounts | Bank, AccountsReceivable, OtherCurrentAsset, FixedAsset, OtherAsset, AccountsPayable, CreditCard, OtherCurrentLiability, LongTermLiability, Equity |
| All Asset Accounts | Bank, AccountsReceivable, OtherCurrentAsset, FixedAsset, OtherAsset |
| All Current Asset Accounts | Bank, AccountsReceivable, OtherCurrentAsset |
| All Bank Accounts | Bank |
| All Accounts receivable (A/R) Accounts | AccountsReceivable |
| All Other Current Assets Accounts | OtherCurrentAsset |
| All Fixed Assets Accounts | FixedAsset |
| All Other Assets Accounts | OtherAsset |
| All Liability Accounts | AccountsPayable, CreditCard, OtherCurrentLiability, LongTermLiability |
| All Current Liability Accounts | AccountsPayable, CreditCard, OtherCurrentLiability |
| All Accounts payable (A/P) Accounts | AccountsPayable |
| All Credit Card Accounts | CreditCard |
| All Other Current Liabilities Accounts | OtherCurrentLiability |
| All Long Term Liabilities Accounts | LongTermLiability |
| xls | application/vnd/ms-excel |
| All Equity Accounts | Equity |
| All Income/Expense Accounts | Income, CostOfGoodsSold, Expense, OtherIncome, OtherExpense |
| All Income Accounts | Income |
| All Cost of Goods Sold Accounts | CostOfGoodsSold |
| All Expenses Accounts | Expense |
| All Other Income Accounts | OtherIncome |

</details>

##### `group_by`

Required: Optional
Type: `String`

The field in the transaction by which to group results. Supported Values: Name, Account, Transaction Type, Customer, Vendor, Employee, Location, Payment Method, Day, Week, Month, Quarter, Year, Fiscal Year, Fiscal Quarter, None

##### `start_date`

Required: Optional
Type: `String`
Default: <span class="literal">date_macro</span>

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `department`

Required: Optional
Type: `String`
Default: Include data for all departments

Filters report contents to include information for specified departments if so configured in the company file.
Supported Values: One or more comma separated department IDs as returned in the attribute, `Department.Id` of the Department object response code.

##### `start_duedate`

Required: Optional
Type: `String`
Default: Return all receivables due data

The range of dates over which receivables are due, in the format `YYYY-MM-DD`. `start_duedate` must be less than `end_duedate`. If not specified, all data is returned.

##### `columns`

Required: Optional
Type: `String`
Default: columns denoted with *

Column types to be shown in the report.
Supported Values: account_name*, create_by, create_date, cust_msg, due_date, doc_num*, inv_date, is_ap_paid, is_cleared, is_no_post*, last_mod_by, memo*, name*, other_account*, pmt_mthd, printed, sales_cust1, sales_cust2, sales_cust3, term_name, tracking_num, tx_date*, txn_type*, term_name, last_mod_date, ship_via, olb_status, is_ar_paid, extra_doc_num, cust_name
 Additional columns when location tracking enabled: dept_name*
 Additional columns with location tracking enabled: dept_name*
 Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies).

<details>
<summary>Show additional values supported based on multicurrency settings for the company.</summary>

#### MULTICURRENCY DISABLED

| Name | Description |
| --- | --- |
| debit | debt_amt |
| credit | credit_amt |
| currency | N/A |
| exchange rate | N/A |
| open balance | nat_open_bal |
| amount | subt_nat_amount* |
| tax amount | tax_amount |
| taxable amount | net_amount |

#### MULTICURRENCY ENABLED

| Name | Description |
| --- | --- |
| debit | debt_home_amt |
| credit | credit_home_amt |
| currency | currency |
| exchange rate | exch_rate |
| open balance | nat_home_open_bal |
| amount | subt_nat_home_amount* |
| tax amount | home_tax_amount |
| taxable amount | home_net_amount |

</details>

##### `end_duedate`

Required: Optional
Type: `String`
Default: Return all receivables due data

The range of dates over which receivables are due, in the format `YYYY-MM-DD`. `start_duedate` must be less than `end_duedate`. If not specified, all data is returned.

##### `end_date`

Required: Optional
Type: `String`
Default: <span class="literal">date_macro</span>

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `memo`

Required: Optional
Type: `String`
Default: Include all memos

Filters report contents to include information for specified memo.
Supported Values: One or more comma separated memo IDs.

##### `appaid`

Required: Optional
Type: `String`
Default: <span class="literal">All</span>

Status of the balance.
Supported Values: `Paid`, `Unpaid`, `All`

##### `moddate_macro`

Required: Optional
Type: `String`
Default: All dates

Predefined report account modification date range. Use if you want the report to cover a standard report date range when accounts were modified; otherwise, use the start_moddate and end_moddate to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `printed`

Required: Optional
Type: `String`
Default: <span class="literal">All</span>

Filters report contents based on whether checks are printed or not.
Supported Values: `Printed`, `To_be_printed`

##### `createdate_macro`

Required: Optional
Type: `String`
Default: All dates

Predefined report account create date range. Use if you want the report to cover a standard create report date range; otherwise, use `start_createdate` and `end_createdate` to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `cleared`

Required: Optional
Type: `String`
Default: Include data for all check statuses

Filters report contents to include information for specified check status.
Supported Values:
`Cleared`: The transaction has been processed by a bank or credit card account and is reflected in the bank balance.
`Uncleared`: A financial entry that has not been reconciled or matched with the corresponding bank statement records.
`Reconciled`: The transaction has been compared to original records and verified as correct.
`Deposited`: A deposit was made into a bank account, such as a checking account.

##### `customer`

Required: Optional
Type: `String`
Default: Include data for all customers

Filters report contents to include information for specified customers.
Supported Values: One or more comma separated customer IDs as returned in the attribute, `Customer.Id`, of the Customer object response code.

##### `qzurl`

Required: Optional
Type: `String`
Default: <span class="literal">false</span>

Specifies whether Quick Zoom URL information should be generated for rows in the report. Quick Zoom URL is a hyperlink to another report containing further details about the particular column of data.
Supported Values: `true`, `false`

##### `term`

Required: Optional
Type: `String`
Default: Return data for all terms

Filters report contents based on term or terms supplied.
Supported Values: One or more comma separated term IDs as returned in the attribute, `Term.Id` of the Term object response code.

##### `end_createdate`

Required: Optional
Type: `String`
Default: <span class="literal">createdate_macro</span>

Specify an explicit account create report date range, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `createdate_macro` to cover a standard report date range. (This field is not currently available.)

##### `name`

Required: Optional
Type: `String`
Default: Include data from all customer, vendor, and employee objects

Filters report contents based on the specified comma separated list of ids for the name list customer, vendor, or employee objects.
Query the Customer, Vendor, or Employee name list resource to determine the list of objects for this reference. Specify values found in `Customer.Id`, `Vendor.Id`, and `Employee.Id`. For example, `name=1,4,7` includes data in the report for namelist ids 1, 4, and 7. vendor and employee objects

##### `sort_by`

Required: Optional
Type: `String`
Default: <span class="literal">txn_type</span>

The column type used in sorting report rows. Specify a column type as defined with the columns query parameter.

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order.
Supported Values: `ascend`, `descend`

##### `start_createdate`

Required: Optional
Type: `String`
Default: <span class="literal">createdate_macro</span>

Specify an explicit account create report date range, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `createdate_macro` to cover a standard report date range. (This field is not currently available.)

##### `end_moddate`

Required: Optional
Type: `String`
Default: <span class="literal">moddate_macro</span>

(Account List Detail) Specify an explicit account modification report date range, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use the `moddate_macro` to cover a standard report date range.

</details>

### Sample Query

This query returns detailed transaction information for the customer.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/TransactionListByCustomer?start_date=2016-06-01&end_date=2016-07-31&group_by=Customer"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "TransactionListByCustomer",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "true"
      }
    ],
    "StartPeriod": "2016-06-01",
    "Currency": "USD",
    "EndPeriod": "2016-07-31",
    "Time": "2020-09-29T14:20:06-07:00"
  },
  "Rows": {},
  "Columns": {
    "Column": [
      {
        "ColTitle": "Date",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "tx_date"
          }
        ]
      },
      {
        "ColTitle": "Transaction Type",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "txn_type"
          }
        ]
      },
      {
        "ColTitle": "Num",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "doc_num"
          }
        ]
      },
      {
        "ColTitle": "Posting",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "is_no_post"
          }
        ]
      },
      {
        "ColTitle": "Memo/Description",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "memo"
          }
        ]
      },
      {
        "ColTitle": "Account",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "account_name"
          }
        ]
      },
      {
        "ColTitle": "Amount ",
        "MetaData": [
          {
            "Name": "ColKey",
            "Value": "amount"
          }
        ]
      }
    ]
  }
}
```
