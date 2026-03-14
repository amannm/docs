# InventoryValuationDetail

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/inventoryvaluationdetail
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / InventoryValuationDetail
> Canonical entity: `InventoryValuationDetail`

The information below provides a reference on how to access the Inventory Valuation Detail report from the QuickBooks Online Report Service.

## The inventory valuation detail report object

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
    "ReportName": "InventoryValuationDetail",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "this month",
    "StartPeriod": "2024-06-01",
    "Currency": "USD",
    "EndPeriod": "2024-06-30",
    "Time": "2024-06-27T08:27:23-07:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "id": "1010000081",
              "value": "Item One"
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
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "ColData": [
                {
                  "value": "2024-06-27"
                },
                {
                  "id": "1455000001",
                  "value": "Inventory Starting Value"
                },
                {
                  "value": "START"
                },
                {
                  "id": "",
                  "value": ""
                },
                {
                  "value": "10.00"
                },
                {
                  "value": "20.00"
                },
                {
                  "value": "200.00"
                },
                {
                  "value": "10.00"
                },
                {
                  "value": "200.00"
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
              "value": "Total for Item One"
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
              "value": "10.00"
            },
            {
              "value": ""
            },
            {
              "value": "200.00"
            },
            {
              "value": "10.00"
            },
            {
              "value": "200.00"
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
        "ColType": "txn_type",
        "ColTitle": "Transaction Type"
      },
      {
        "ColType": "doc_num",
        "ColTitle": "Num"
      },
      {
        "ColType": "name",
        "ColTitle": "Name"
      },
      {
        "ColType": "quantity",
        "ColTitle": "Qty"
      },
      {
        "ColType": "rate",
        "ColTitle": "Rate"
      },
      {
        "ColType": "home_amount",
        "ColTitle": "FIFO Cost"
      },
      {
        "ColType": "qty_on_hand",
        "ColTitle": "Qty On Hand"
      },
      {
        "ColType": "home_asset_value",
        "ColTitle": "Asset Value"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/InventoryValuationDetail?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `inventoryvaluationdetailquery`

<details>
<summary>Show schema for `inventoryvaluationdetailquery`</summary>

#### inventoryvaluationdetailquery

Model type: `object`

##### `end_date`

Required: Optional
Type: `String`
Default: today's date

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used.

##### `end_svcdate`

Required: Optional
Type: `String`
Default: today's date

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used.

##### `date_macro`

Required: Optional
Type: `String`
Default: this month to date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `svcdate_macro`

Required: Optional
Type: `String`
Default: Total*

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `start_svcdate`

Required: Optional
Type: `String`
Default: today's date

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used.

##### `group_by`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The field in the transaction by which to group results.
Supported Values: Name, Account, Transaction Type, Customer, Vendor, Employee, Location, Payment Method, Day, Week, Month, Quarter, Year, None

##### `start_date`

Required: Optional
Type: `String`
Default: first date of the month

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used.

##### `columns`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

Column types to show in the report.
Supported Values: tx_date, txn_id, txn_type, doc_num, name, quantity, rate, home_amount, qty_on_hand, asset_value, create_date, create_by, last_mod_date, last_mod_by, item_sku, memo, exch_rate, account_name, service_date, rate_inventory, qty_on_hand, asset_value_nt, tracking_num

</details>

### Sample Query

This query returns get the inventory valuation detail report for this fiscal year-to-date.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/InventoryValuationDetail?date_macro=This Month"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "InventoryValuationDetail",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "this month",
    "StartPeriod": "2024-06-01",
    "Currency": "USD",
    "EndPeriod": "2024-06-30",
    "Time": "2024-06-27T08:27:23-07:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "id": "1010000081",
              "value": "Item One"
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
            }
          ]
        },
        "Rows": {
          "Row": [
            {
              "ColData": [
                {
                  "value": "2024-06-27"
                },
                {
                  "id": "1455000001",
                  "value": "Inventory Starting Value"
                },
                {
                  "value": "START"
                },
                {
                  "id": "",
                  "value": ""
                },
                {
                  "value": "10.00"
                },
                {
                  "value": "20.00"
                },
                {
                  "value": "200.00"
                },
                {
                  "value": "10.00"
                },
                {
                  "value": "200.00"
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
              "value": "Total for Item One"
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
              "value": "10.00"
            },
            {
              "value": ""
            },
            {
              "value": "200.00"
            },
            {
              "value": "10.00"
            },
            {
              "value": "200.00"
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
        "ColType": "txn_type",
        "ColTitle": "Transaction Type"
      },
      {
        "ColType": "doc_num",
        "ColTitle": "Num"
      },
      {
        "ColType": "name",
        "ColTitle": "Name"
      },
      {
        "ColType": "quantity",
        "ColTitle": "Qty"
      },
      {
        "ColType": "rate",
        "ColTitle": "Rate"
      },
      {
        "ColType": "home_amount",
        "ColTitle": "FIFO Cost"
      },
      {
        "ColType": "qty_on_hand",
        "ColTitle": "Qty On Hand"
      },
      {
        "ColType": "home_asset_value",
        "ColTitle": "Asset Value"
      }
    ]
  }
}
```
