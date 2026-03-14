# TrialBalance

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/trialbalance
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Report entities](index.md) / TrialBalance
> Canonical entity: `TrialBalance`

The information below provides a reference on how to access the Trial Balance report from the QuickBooks Online Report Service. For France-based companies, use TrialBalanceFR as the endpoint.

## The trial balance report object

The table below lists all possible attributes that can be returned in the report response. Values are not localized unless indicated. [Click here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions) to download the latest XSD.

### trialbalancereporttoplevel

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

Top level container holding information for profit and loss report rows.

<details>
<summary>Child attributes for `Rows`</summary>

##### profitandlossreportrows

Model type: `object`

###### `Row [0..n]`

Represents a row in a report. A group of rows is enclosed in a `Rows` container. Rows may be nested either as a single row or in sets, based on the accounts represented in the report and query parameters specified in the request. Parameters:

`type`—As an enclosing section of sub-rows, this is always the string, `Section`. As a leaf row, this is always the string, `Data`.

`group`—The group name, valid when `type=Section`.

<details>
<summary>Show possible values for group</summary>

#### Values based on locales

| Name | Description |
| --- | --- |
| US | `Income` `COGS` `GrossProfit` `Expenses` `NetOperatingIncome` `OtherExpenses` `NetOtherIncome` `NetIncome` |
| CA | `Income` `COGS` `Expenses` `OtherIncome` `OtherExpenses` `NetIncome` |
| GB | `Income` `COGS` `GrossProfit` `Expenses` `NetOperatingIncome` `OtherIncome` `OtherExpenses` `NetOtherIncome` `NetIncome` |
| IN | `Income` `COGS` `GrossProfit` `OtherIncome` `Expenses` `OtherExpenses` `NetIncome` |
| FR | `DepreciationAndProvisions` `OperatingExpenses` `QuotasResultInJointOperations` `FinancialCharges` `ExceptionalCharges` `EmployeeParticipationResults` `IncomeTaxExpenses` `TotalExpenses` `ProfitOrLoss` `Including` `Revenue` `Export` `JointOperations` `FinancialProducts` `ExceptionalItems` `TotalIncome` |
| AU | `Income` `COGS` `GrossProfit` `OtherIncome` `Expenses` `OtherExpenses` `NetIncome` |

</details>

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
    "ReportName": "TrialBalance",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "this month-to-date",
    "ReportBasis": "Accrual",
    "StartPeriod": "2016-03-01",
    "Currency": "USD",
    "EndPeriod": "2016-03-14",
    "Time": "2016-03-14T10:11:07-07:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "id": "35",
            "value": "Checking"
          },
          {
            "value": "4151.74"
          },
          {
            "value": ""
          }
        ]
      },
      {
        "ColData": [
          {
            "id": "13",
            "value": "Meals and Entertainment"
          },
          {
            "value": ""
          },
          {
            "value": "46.00"
          }
        ]
      },
      {
        "ColData": [
          {
            "id": "93",
            "value": "QuickBooks Payments Fees"
          },
          {
            "value": "0.44"
          },
          {
            "value": ""
          }
        ]
      },
      {
        "group": "GrandTotal",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL"
            },
            {
              "value": "36587.47"
            },
            {
              "value": "36587.47"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "Account",
        "ColTitle": ""
      },
      {
        "ColType": "Money",
        "ColTitle": "Debit"
      },
      {
        "ColType": "Money",
        "ColTitle": "Credit"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `FR locale - GET /v3/company/<realmID>/reports/TrialBalanceFR?minorversion=4&<name>=<value>[&...]

non-FR locales - GET /v3/company/<realmID>/reports/TrialBalance?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `trialbalancequery`

<details>
<summary>Show schema for `trialbalancequery`</summary>

#### trialbalancequery

Model type: `object`

##### `accounting_method`

Required: Optional
Type: `String`
Default: Method defined in preferences by the <span class="literal">Preferences.ReportPrefs.ReportBasis</span> attribute.

The accounting method used in the report. Supported Values:`Cash`, `Accrual`

##### `end_date`

Required: Optional
Type: `String`
Default: <span class="literal">date_macro</span>

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `date_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range. Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order. Supported Values: `ascend`, `descend`

##### `summarize_column_by`

Required: Optional
Type: `String`
Default: Total*

The criteria by which to group the report results. Supported Values: Total, Month, Week, Days, Quarter, Year, Customers, Vendors, Classes, Departments, Employees, ProductsAndServices

##### `start_date`

Required: Optional
Type: `String`
Default: <span class="literal">date_macro</span>

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

</details>

### Sample Query

This query returns a trial balance report.

#### Example

```text
"For non-FR locales:\r\nBaseURL/v3/company/1386066315/reports/TrialBalance\r\nFor FR locale:\r\nBaseURL/v3/company/1386066315/reports/TrialBalanceFR?minorversion=4"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "TrialBalance",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "this month-to-date",
    "ReportBasis": "Accrual",
    "StartPeriod": "2016-03-01",
    "Currency": "USD",
    "EndPeriod": "2016-03-14",
    "Time": "2016-03-14T10:11:07-07:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "id": "35",
            "value": "Checking"
          },
          {
            "value": "4151.74"
          },
          {
            "value": ""
          }
        ]
      },
      {
        "ColData": [
          {
            "id": "13",
            "value": "Meals and Entertainment"
          },
          {
            "value": ""
          },
          {
            "value": "46.00"
          }
        ]
      },
      {
        "ColData": [
          {
            "id": "93",
            "value": "QuickBooks Payments Fees"
          },
          {
            "value": "0.44"
          },
          {
            "value": ""
          }
        ]
      },
      {
        "group": "GrandTotal",
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL"
            },
            {
              "value": "36587.47"
            },
            {
              "value": "36587.47"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "Account",
        "ColTitle": ""
      },
      {
        "ColType": "Money",
        "ColTitle": "Debit"
      },
      {
        "ColType": "Money",
        "ColTitle": "Credit"
      }
    ]
  }
}
```
