# AccountListDetail

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/accountlistdetail
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Report entities](index.md) / AccountListDetail
> Canonical entity: `AccountListDetail`

The information below provides a reference on how to access the account list detail report from the QuickBooks Online Report Service.

## The account list detail report object

The table below lists all possible attributes that can be returned in the report response. Values are not localized unless indicated. [Click here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions) to download the latest XSD.

### reporttoplevel

Model type: `object`

#### `Header`

The report header.

<details>
<summary>Child attributes for `Header`</summary>

##### reportheader

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

###### `Class`

Type: `String`

A string containing the Ids as specified with the corresponding filter query parameter. Only those filter query parameters specified in the request are returned in the header.

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
    "ReportName": "AccountList",
    "Currency": "USD",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "Time": "2016-03-08T11:56:36-08:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "value": "Billable Expense Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Design income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Discounts given"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Fees Billed"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials:Decks and Patios"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials:Fountains and Garden Lighting"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials:Plants and Soil"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials:Sprinklers and Drip Systems"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Labor"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Labor:Installation"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Labor:Maintenance and Repair"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Other Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Pest Control Services"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Refunds-Allowances"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Sales of Product Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Services"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Shipping Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Unapplied Cash Payment Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Uncategorized Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "account_name",
        "ColTitle": "Account"
      },
      {
        "ColType": "account_type",
        "ColTitle": "Type"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/AccountList?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `accountlistquery`

<details>
<summary>Show schema for `accountlistquery`</summary>

#### accountlistquery

Model type: `object`

##### `account_type`

Required: Optional
Type: `String`
Default: All account types

Account type from which transactions are included in the report.
Supported Values: AccountsPayable, AccountsReceivable, Bank, CostOfGoodsSold, CreditCard, Equity, Expense, FixedAsset, Income, LongTermLiability, NonPosting, OtherAsset, OtherCurrentAsset, OtherCurrentLiability, OtherExpense, OtherIncome

<details>
<summary>Show the supported account types and values</summary>

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

##### `end_date`

Required: Optional
Type: `String`

The start date and end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range.

##### `start_moddate`

Required: Optional
Type: `String`

If not specified value of `moddate_macro` is used. (Account List Detail) Specify an explicit account modification report date range, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use the `moddate_macro` to cover a standard report date range.

##### `sort_by`

Required: Optional
Type: `String`
Default: txn_type

The column type used in sorting report rows. Specify a column type as defined with the columns query parameter.

##### `sort_order`

Required: Optional
Type: `String`
Default: ascend

The sort order.
Supported Values: `ascend`, `descend`

##### `moddate_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined report account modification date range. Use if you want the report to cover a standard report date range when accounts were modified; otherwise, use the start_moddate and end_moddate to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `end_moddate`

Required: Optional
Type: `String`

If not specified value of `moddate_macro` is used. (Account List Detail) Specify an explicit account modification report date range, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use the `moddate_macro` to cover a standard report date range.

##### `account_status`

Required: Optional
Type: `String`
Default: Not_Deleted

The account status. Supported values include: `Deleted`, `Not_Deleted`

##### `createdate_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined report account create date range. Use if you want the report to cover a standard create report date range; otherwise, use `start_createdate` and `end_createdate` to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `start_date`

Required: Optional
Type: `String`

The start date and end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range.

##### `columns`

Required: Optional
Type: `String`

Column types to be shown in the report.
Supported Values:
`account_name*`, `account_type*`, `detail_acc_type`, `create_date`, `create_by`, `detail_acc_type*`, `last_ mod_date`, `last_ mod_by`, `account_desc*`, `account_bal*`

</details>

### Sample Query

This query returns a list of all income accounts.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/AccountList?columns=account_name,account_type&account_type=Income\n"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "AccountList",
    "Currency": "USD",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "Time": "2016-03-08T11:56:36-08:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "value": "Billable Expense Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Design income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Discounts given"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Fees Billed"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials:Decks and Patios"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials:Fountains and Garden Lighting"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials:Plants and Soil"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Job Materials:Sprinklers and Drip Systems"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Labor"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Labor:Installation"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Landscaping Services:Labor:Maintenance and Repair"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Other Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Pest Control Services"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Refunds-Allowances"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Sales of Product Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Services"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Shipping Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Unapplied Cash Payment Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "Uncategorized Income"
          },
          {
            "value": "Income"
          }
        ],
        "type": "Data"
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "account_name",
        "ColTitle": "Account"
      },
      {
        "ColType": "account_type",
        "ColTitle": "Type"
      }
    ]
  }
}
```
