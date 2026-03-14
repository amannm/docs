# ARAgingSummary

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/aragingsummary
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Report entities](index.md) / ARAgingSummary
> Canonical entity: `ARAgingSummary`

The information below provides a reference on how to access the AR Aging Summary report from the QuickBooks Online Report Service.

## The AR Aging Summary report object

The table below lists all possible attributes that can be returned in the report response. Values are not localized unless indicated. [Click here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions) to download the latest XSD.

### agedreceivablestoplevel

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

Top level container holding information for Aged Receivables report rows.

<details>
<summary>Child attributes for `Rows`</summary>

##### agedreceivablesreportrows

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
| US | `GrandTotal` |
| CA | `GrandTotal` |
| GB | `GrandTotal` |
| IN | `GrandTotal` |
| FR | `GrandTotal` |
| AU | `GrandTotal` |

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
    "Customer": "4",
    "ReportName": "AgedReceivables",
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
    "Time": "2016-03-09T09:09:52-08:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "id": "4",
            "value": "Jane Litigious"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "37.50"
          },
          {
            "value": "37.50"
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
              "value": "0.00"
            },
            {
              "value": "0.00"
            },
            {
              "value": "0.00"
            },
            {
              "value": "0.00"
            },
            {
              "value": "37.50"
            },
            {
              "value": "37.50"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "Customer",
        "ColTitle": ""
      },
      {
        "ColType": "Money",
        "ColTitle": "Current"
      },
      {
        "ColType": "Money",
        "ColTitle": "1 - 30"
      },
      {
        "ColType": "Money",
        "ColTitle": "31 - 60"
      },
      {
        "ColType": "Money",
        "ColTitle": "61 - 90"
      },
      {
        "ColType": "Money",
        "ColTitle": "91 and over"
      },
      {
        "ColType": "Money",
        "ColTitle": "Total"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/AgedReceivables?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `agedreceivablesquery`

<details>
<summary>Show schema for `agedreceivablesquery`</summary>

#### agedreceivablesquery

Model type: `object`

##### `customer`

Required: Optional
Type: `String`
Default: to include data for all customers

Filters report contents to include information for specified customers. Supported Values: One or more comma separated customer IDs as returned in the attribute, `Customer.Id`, of the Customer object response code.

##### `qzurl`

Required: Optional
Type: `String`
Default: false

Specifies whether Quick Zoom URL information should be generated for rows in the report. Quick Zoom URL is a hyperlink to another report containing further details about the particular column of data. Supported Values: `true`, `false`

##### `date_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range. Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `aging_method`

Required: Optional
Type: `String`
Default: Report_Date

The date upon which aging is determined. Supported Values:`Report_Date`, `Current`

##### `report_date`

Required: Optional
Type: `String`
Default: today's date

Start date to use for the report, in the format `YYYY-MM-DD`.

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order. Supported Values: `ascend`, `descend`

##### `department`

Required: Optional
Type: `String`
Default: to include data for all departments

Filters report contents to include information for specified departments if so configured in the company file. Supported Values: One or more comma separated department IDs as returned in the attribute, `Department.Id` of the Department object response code.

</details>

### Sample Query

This query returns last fiscal year aged receivables for customer, Jane Litigious (`customer=4`).

#### Example

```text
"BaseURL/v3/company/1386066315/reports/AgedReceivables?customer=4&date_macro=Last Fiscal Year\n"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "Customer": "4",
    "ReportName": "AgedReceivables",
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
    "Time": "2016-03-09T09:09:52-08:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "id": "4",
            "value": "Jane Litigious"
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": "37.50"
          },
          {
            "value": "37.50"
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
              "value": "0.00"
            },
            {
              "value": "0.00"
            },
            {
              "value": "0.00"
            },
            {
              "value": "0.00"
            },
            {
              "value": "37.50"
            },
            {
              "value": "37.50"
            }
          ]
        }
      }
    ]
  },
  "Columns": {
    "Column": [
      {
        "ColType": "Customer",
        "ColTitle": ""
      },
      {
        "ColType": "Money",
        "ColTitle": "Current"
      },
      {
        "ColType": "Money",
        "ColTitle": "1 - 30"
      },
      {
        "ColType": "Money",
        "ColTitle": "31 - 60"
      },
      {
        "ColType": "Money",
        "ColTitle": "61 - 90"
      },
      {
        "ColType": "Money",
        "ColTitle": "91 and over"
      },
      {
        "ColType": "Money",
        "ColTitle": "Total"
      }
    ]
  }
}
```
