# VendorBalanceDetail

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/vendorbalancedetail
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Report entities](index.md) / VendorBalanceDetail
> Canonical entity: `VendorBalanceDetail`

The information below provides a reference on how to access the Vendor Balance Detail report from the QuickBooks Online Report Service.

## The vendor balance detail report object

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
    "ReportName": "VendorBalanceDetail",
    "Vendor": "31",
    "Option": [
      {
        "Name": "report_date",
        "Value": "2015-12-31"
      },
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "last calendar year",
    "StartPeriod": "2015-01-01",
    "Currency": "USD",
    "EndPeriod": "2015-12-31",
    "Time": "2016-03-14T11:18:40-07:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "id": "31",
              "value": "Brosnahan Insurance Agency"
            },
            {
              "value": ""
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "ColData": [
                {
                  "value": "2015-07-02"
                },
                {
                  "value": "241.23"
                },
                {
                  "value": "241.23"
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Total for Brosnahan Insurance Agency"
            },
            {
              "value": "241.23"
            },
            {
              "value": "241.23"
            }
          ]
        }
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL"
            },
            {
              "value": "241.23"
            },
            {
              "value": "241.23"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "tx_date",
        "ColTitle": "Date"
      },
      {
        "ColType": "subt_neg_amount",
        "ColTitle": "Amount"
      },
      {
        "ColType": "subt_neg_open_bal",
        "ColTitle": "Open Balance"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/VendorBalanceDetail?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `vendorbalancedetailquery`

<details>
<summary>Show schema for `vendorbalancedetailquery`</summary>

#### vendorbalancedetailquery

Model type: `object`

##### `term`

Required: Optional
Type: `String`
Default: Return data for all terms

Filters report contents based on term or terms supplied. Supported Values: One or more comma separated term IDs as returned in the attribute, `Term.Id` of the Term object response code.

##### `end_duedate`

Required: Optional
Type: `String`
Default: To return all receivables due data

The range of dates over which receivables are due, in the format `YYYY-MM-DD`. `start_duedate` must be less than `end_duedate`. If not specified, all data is returned.

##### `accounting_method`

Required: Optional
Type: `String`
Default: Method defined in preferences by the <span class="literal">Preferences.ReportPrefs.ReportBasis</span> attribute.

The accounting method used in the report. Supported Values:`Cash`, `Accrual`

##### `date_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range. Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `start_duedate`

Required: Optional
Type: `String`
Default: To return all receivables due data

The range of dates over which receivables are due, in the format `YYYY-MM-DD`. `start_duedate` must be less than `end_duedate`. If not specified, all data is returned.

##### `duedate_macro`

Required: Optional
Type: `String`
Default: <span class="literal">This Fiscal Year-to-date</span>

Predefined date range of due dates for balances to include in the report; otherwise, use the start_duedate and end_duedate to cover an explicit report date range. Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `sort_by`

Required: Optional
Type: `String`
Default: <span class="literal">txn_type</span>

The column type used in sorting report rows. Specify a column type as defined with the columns query parameter.

##### `report_date`

Required: Optional
Type: `String`
Default: Today's date

Start date to use for the report, in the format `YYYY-MM-DD`.

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order. Supported Values: `ascend`, `descend`

##### `appaid`

Required: Optional
Type: `String`
Default: <span class="literal">Unpaid</span>

Status of the balance. Supported Values: `Paid`, `Unpaid`, `All`

##### `department`

Required: Optional
Type: `String`
Default: Include data for all departments

Filters report contents to include information for specified departments if so configured in the company file. Supported Values: One or more comma separated department IDs as returned in the attribute, `Department.Id` of the Department object response code.

##### `vendor`

Required: Optional
Type: `String`
Default: Return data for all vendors

Filters report contents to include information for specified vendors. Supported Values: One or more comma separated vendor IDs as returned in the attribute, `Vendor.Id`, of the Vendor object response code.

##### `columns`

Required: Optional
Type: `String`
Default: columns denoted with *

Column types to be shown in the report. Supported Values: create_by, create_date, doc_num*, due_date*, last_mod_by, last_mod_date, memo*, term_name, tx_date*, txn_type*, vend_bill_addr, vend_comp_name, vend_name*, vend_pri_cont, vend_pri_email, vend_pri_tel
 Additional columns with location tracking enabled: dept_name*

<details>
<summary>Show additional values supported based on multicurrency settings for the company.</summary>

#### MULTICURRENCY DISABLED

| Name | Description |
| --- | --- |
| currency | N/A |
| exchange rate | N/A |
| open balance | subt_neg_open_bal* |
| amount | subt_neg_amount* |

#### MULTICURRENCY ENABLED

| Name | Description |
| --- | --- |
| currency | currency |
| exchange rate | exch_rate |
| open balance | neg_foreign_open_bal <br> subt_neg_home_open_bal* |
| amount | neg_foreign_amount <br> subt_neg_home_amount* |

</details>

</details>

### Sample Query

This query returns the last fiscal year's vendor balance detail report for Brosnahan Insurance Agency (vendor=31).

#### Example

```text
"BaseURL/v3/company/1386066315/reports/VendorBalanceDetail?vendor=31&columns=tx_date,subt_neg_amount,subt_neg_open_bal&date_macro=Last Fiscal Year"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "VendorBalanceDetail",
    "Vendor": "31",
    "Option": [
      {
        "Name": "report_date",
        "Value": "2015-12-31"
      },
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "last calendar year",
    "StartPeriod": "2015-01-01",
    "Currency": "USD",
    "EndPeriod": "2015-12-31",
    "Time": "2016-03-14T11:18:40-07:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "id": "31",
              "value": "Brosnahan Insurance Agency"
            },
            {
              "value": ""
            },
            {
              "value": ""
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "ColData": [
                {
                  "value": "2015-07-02"
                },
                {
                  "value": "241.23"
                },
                {
                  "value": "241.23"
                }
              ],
              "type": "Data"
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Total for Brosnahan Insurance Agency"
            },
            {
              "value": "241.23"
            },
            {
              "value": "241.23"
            }
          ]
        }
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL"
            },
            {
              "value": "241.23"
            },
            {
              "value": "241.23"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "tx_date",
        "ColTitle": "Date"
      },
      {
        "ColType": "subt_neg_amount",
        "ColTitle": "Amount"
      },
      {
        "ColType": "subt_neg_open_bal",
        "ColTitle": "Open Balance"
      }
    ]
  }
}
```
