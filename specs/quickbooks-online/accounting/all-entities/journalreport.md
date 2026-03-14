# JournalReport

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/journalreport
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / JournalReport
> Canonical entity: `JournalReport`

The information below provides a reference on how to access the journal report from the QuickBooks Online Report Service. For FR locales use [JournalReportFR](journalreportfr.md) instead.
This report presents a summary of the journal code ledgers for non-FR companies.

## The journal report object

The table below lists all possible attributes that can be returned in the report response. [Click here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions) to download the latest XSD.

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
    "ReportName": "JournalReport",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "this month-to-date",
    "StartPeriod": "2019-05-01",
    "Currency": "USD",
    "EndPeriod": "2019-05-22",
    "Time": "2019-05-22T17:16:03-07:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "63",
            "value": "Expense"
          },
          {
            "value": ""
          },
          {
            "id": "8",
            "value": "InactiveCo (deleted)"
          },
          {
            "value": ""
          },
          {
            "id": "35",
            "value": "Checking"
          },
          {
            "value": ""
          },
          {
            "value": "30.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "63",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": "30.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "30.00"
            },
            {
              "value": "30.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "64",
            "value": "Expense"
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "35",
            "value": "Checking"
          },
          {
            "value": ""
          },
          {
            "value": "11.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "64",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": "11.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "11.00"
            },
            {
              "value": "11.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "65",
            "value": "Invoice"
          },
          {
            "value": "1035"
          },
          {
            "id": "1",
            "value": "Bill Braski"
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "15.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "65",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "1",
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "15.00"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "15.00"
            },
            {
              "value": "15.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "73",
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
            "value": "time activity - Opening inventory and value"
          },
          {
            "id": "34",
            "value": "Opening Balance Equity"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "73",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "time activity - Opening inventory and value"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": ".00"
            },
            {
              "value": ""
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "76",
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
            "value": "inv item - Opening inventory and value"
          },
          {
            "id": "34",
            "value": "Opening Balance Equity"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "76",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "inv item - Opening inventory and value"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": ".00"
            },
            {
              "value": ""
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "79",
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
            "value": "inv item2 - Opening inventory and value"
          },
          {
            "id": "34",
            "value": "Opening Balance Equity"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "79",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "inv item2 - Opening inventory and value"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": ".00"
            },
            {
              "value": ""
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-10"
          },
          {
            "id": "68",
            "value": "Inventory Qty Adjust"
          },
          {
            "value": "4"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "68",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": "1595.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "68",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ""
          },
          {
            "value": "1595.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "68",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "1595.00"
            },
            {
              "value": "1595.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-11"
          },
          {
            "id": "67",
            "value": "Inventory Qty Adjust"
          },
          {
            "value": "3"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Motors - Quantity adjustment"
          },
          {
            "id": "44",
            "value": "Inventory Shrinkage"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "67",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Motors - Quantity adjustment"
          },
          {
            "id": "44",
            "value": "Inventory Shrinkage"
          },
          {
            "value": ""
          },
          {
            "value": "495.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "67",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Motors - Quantity adjustment"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": "495.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "67",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Motors - Quantity adjustment"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "495.00"
            },
            {
              "value": "495.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-15"
          },
          {
            "id": "72",
            "value": "Invoice"
          },
          {
            "value": "1036"
          },
          {
            "id": "4",
            "value": "Gary Witiker"
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "58.25"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "29",
            "value": "Sales of Product Income"
          },
          {
            "value": ""
          },
          {
            "value": "10.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "29",
            "value": "Sales of Product Income"
          },
          {
            "value": ""
          },
          {
            "value": "15.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "41",
            "value": "Service Fee Income Account"
          },
          {
            "value": ""
          },
          {
            "value": "31.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": "1.56"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".25"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".44"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "58.25"
            },
            {
              "value": "58.25"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-20"
          },
          {
            "id": "75",
            "value": "Invoice"
          },
          {
            "value": "1037"
          },
          {
            "id": "4",
            "value": "Gary Witiker"
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "43.60"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "29",
            "value": "Sales of Product Income"
          },
          {
            "value": ""
          },
          {
            "value": "40.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": "2.50"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".40"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".70"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "43.60"
            },
            {
              "value": "43.60"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-20"
          },
          {
            "id": "78",
            "value": "Invoice"
          },
          {
            "value": "1038"
          },
          {
            "id": "4",
            "value": "Gary Witiker"
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "21.80"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "29",
            "value": "Sales of Product Income"
          },
          {
            "value": ""
          },
          {
            "value": "20.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": "1.25"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".20"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".35"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "21.80"
            },
            {
              "value": "21.80"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-22"
          },
          {
            "id": "81",
            "value": "Invoice"
          },
          {
            "value": "1039"
          },
          {
            "id": "5",
            "value": "Open Balance (deleted)"
          },
          {
            "value": "Created by QB Online to adjust balance for deletion"
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "41.90"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "81",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Created by QB Online to adjust balance for deletion"
          },
          {
            "id": "1",
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "41.90"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "41.90"
            },
            {
              "value": "41.90"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-22"
          },
          {
            "id": "82",
            "value": "Payment"
          },
          {
            "value": ""
          },
          {
            "id": "5",
            "value": "Open Balance (deleted)"
          },
          {
            "value": "Created by QB Online to link credits to charges."
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "82",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL"
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
              "value": "2311.55"
            },
            {
              "value": "2311.55"
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
        "ColType": "memo",
        "ColTitle": "Memo/Description"
      },
      {
        "ColType": "account_name",
        "ColTitle": "Account"
      },
      {
        "ColType": "debt_amt",
        "ColTitle": "Debit"
      },
      {
        "ColType": "credit_amt",
        "ColTitle": "Credit"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/JournalReport?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `journalreportqueryUS`

<details>
<summary>Show schema for `journalreportqueryUS`</summary>

#### journalreportqueryUS

Model type: `object`

##### `end_date`

Required: Optional
Type: `String`

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `date_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range. Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

##### `sort_by`

Required: Optional
Type: `String`
Default: <span class="literal">txn_type</span>

The column type used in sorting report rows. Specify a column type as defined with the columns query parameter.

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order. Supported Values: `ascend`, `descend`

##### `start_date`

Required: Optional
Type: `String`

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

##### `columns`

Required: Optional
Type: `String`
Default: columns denoted with *

Default columns included in the report are denoted with *. Column types to be shown in the report. Supported Values: acct_num_with_extn*, account_name*, credit_amt*, create_by, create_date, debt_amt*, doc_num*, due_date*, is_ar_paid*, is_ap_paid*, item_name, journal_code_name*, last_mod_by, last_mod_date, memo*, name, neg_open_bal, paid_date*, pmt_mthd*, quantity, rate, tx_date*, txn_num*, txn_type*
 **To retrieve the account number (acct_num_with_extn) it's also needed to request the account name (account_name) in the same request.**
 The account number will only be returned if the company has enabled the 'enable account numbers' option in its Chart of Accounts preferences.

</details>

### Sample Query

This query returns a list of all journal codes.

#### Example

```text
"BaseURL/v3/company/1386066315/reports/JournalReport"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "ReportName": "JournalReport",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "this month-to-date",
    "StartPeriod": "2019-05-01",
    "Currency": "USD",
    "EndPeriod": "2019-05-22",
    "Time": "2019-05-22T17:16:03-07:00"
  },
  "Rows": {
    "Row": [
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "63",
            "value": "Expense"
          },
          {
            "value": ""
          },
          {
            "id": "8",
            "value": "InactiveCo (deleted)"
          },
          {
            "value": ""
          },
          {
            "id": "35",
            "value": "Checking"
          },
          {
            "value": ""
          },
          {
            "value": "30.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "63",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": "30.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "30.00"
            },
            {
              "value": "30.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "64",
            "value": "Expense"
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "35",
            "value": "Checking"
          },
          {
            "value": ""
          },
          {
            "value": "11.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "64",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": "11.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "11.00"
            },
            {
              "value": "11.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "65",
            "value": "Invoice"
          },
          {
            "value": "1035"
          },
          {
            "id": "1",
            "value": "Bill Braski"
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "15.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "65",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "1",
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "15.00"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "15.00"
            },
            {
              "value": "15.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "73",
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
            "value": "time activity - Opening inventory and value"
          },
          {
            "id": "34",
            "value": "Opening Balance Equity"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "73",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "time activity - Opening inventory and value"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": ".00"
            },
            {
              "value": ""
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "76",
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
            "value": "inv item - Opening inventory and value"
          },
          {
            "id": "34",
            "value": "Opening Balance Equity"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "76",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "inv item - Opening inventory and value"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": ".00"
            },
            {
              "value": ""
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-07"
          },
          {
            "id": "79",
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
            "value": "inv item2 - Opening inventory and value"
          },
          {
            "id": "34",
            "value": "Opening Balance Equity"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "79",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "inv item2 - Opening inventory and value"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": ".00"
            },
            {
              "value": ""
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-10"
          },
          {
            "id": "68",
            "value": "Inventory Qty Adjust"
          },
          {
            "value": "4"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "68",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": "1595.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "68",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ""
          },
          {
            "value": "1595.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "68",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "1595.00"
            },
            {
              "value": "1595.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-11"
          },
          {
            "id": "67",
            "value": "Inventory Qty Adjust"
          },
          {
            "value": "3"
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Motors - Quantity adjustment"
          },
          {
            "id": "44",
            "value": "Inventory Shrinkage"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "67",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Motors - Quantity adjustment"
          },
          {
            "id": "44",
            "value": "Inventory Shrinkage"
          },
          {
            "value": ""
          },
          {
            "value": "495.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "67",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Motors - Quantity adjustment"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": "495.00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "67",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Motors - Quantity adjustment"
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "495.00"
            },
            {
              "value": "495.00"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-15"
          },
          {
            "id": "72",
            "value": "Invoice"
          },
          {
            "value": "1036"
          },
          {
            "id": "4",
            "value": "Gary Witiker"
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "58.25"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "29",
            "value": "Sales of Product Income"
          },
          {
            "value": ""
          },
          {
            "value": "10.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "29",
            "value": "Sales of Product Income"
          },
          {
            "value": ""
          },
          {
            "value": "15.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "41",
            "value": "Service Fee Income Account"
          },
          {
            "value": ""
          },
          {
            "value": "31.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": "1.56"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".25"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "72",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".44"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "58.25"
            },
            {
              "value": "58.25"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-20"
          },
          {
            "id": "75",
            "value": "Invoice"
          },
          {
            "value": "1037"
          },
          {
            "id": "4",
            "value": "Gary Witiker"
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "43.60"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "29",
            "value": "Sales of Product Income"
          },
          {
            "value": ""
          },
          {
            "value": "40.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": "2.50"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".40"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "75",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".70"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "43.60"
            },
            {
              "value": "43.60"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-20"
          },
          {
            "id": "78",
            "value": "Invoice"
          },
          {
            "value": "1038"
          },
          {
            "id": "4",
            "value": "Gary Witiker"
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "21.80"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "29",
            "value": "Sales of Product Income"
          },
          {
            "value": ""
          },
          {
            "value": "20.00"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "31",
            "value": "Inventory Asset"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "30",
            "value": "Cost of Goods Sold"
          },
          {
            "value": ".00"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": "1.25"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".20"
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "78",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "38",
            "value": "California Department of Tax and Fee Administration Payable"
          },
          {
            "value": ""
          },
          {
            "value": ".35"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "21.80"
            },
            {
              "value": "21.80"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-22"
          },
          {
            "id": "81",
            "value": "Invoice"
          },
          {
            "value": "1039"
          },
          {
            "id": "5",
            "value": "Open Balance (deleted)"
          },
          {
            "value": "Created by QB Online to adjust balance for deletion"
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": "41.90"
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "81",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": "Created by QB Online to adjust balance for deletion"
          },
          {
            "id": "1",
            "value": "Sales"
          },
          {
            "value": ""
          },
          {
            "value": "41.90"
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
              "value": "41.90"
            },
            {
              "value": "41.90"
            }
          ]
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "2019-05-22"
          },
          {
            "id": "82",
            "value": "Payment"
          },
          {
            "value": ""
          },
          {
            "id": "5",
            "value": "Open Balance (deleted)"
          },
          {
            "value": "Created by QB Online to link credits to charges."
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "ColData": [
          {
            "value": "0-00-00"
          },
          {
            "id": "82",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "",
            "value": ""
          },
          {
            "value": ""
          },
          {
            "id": "36",
            "value": "Accounts Receivable (A/R)"
          },
          {
            "value": ""
          },
          {
            "value": ""
          }
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
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
        }
      },
      {
        "ColData": [
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
        ],
        "type": "Data"
      },
      {
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "TOTAL"
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
              "value": "2311.55"
            },
            {
              "value": "2311.55"
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
        "ColType": "memo",
        "ColTitle": "Memo/Description"
      },
      {
        "ColType": "account_name",
        "ColTitle": "Account"
      },
      {
        "ColType": "debt_amt",
        "ColTitle": "Debit"
      },
      {
        "ColType": "credit_amt",
        "ColTitle": "Credit"
      }
    ]
  }
}
```
