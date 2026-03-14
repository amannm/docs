# CustomerBalanceDetail

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customerbalancedetail
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / CustomerBalanceDetail
> Canonical entity: `CustomerBalanceDetail`

The information below provides a reference on how to access the Customer Balance Detail report from the QuickBooks Online Report Service.

## The customer balance detail report object

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
    "Customer": "1",
    "ReportName": "CustomerBalanceDetail",
    "Option": [
      {
        "Name": "report_date",
        "Value": "2016-03-10"
      },
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "all",
    "Currency": "USD",
    "Time": "2016-03-10T13:43:05-08:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "id": "1",
              "value": "Amy's Bird Sanctuary"
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
                  "value": "2015-08-04"
                },
                {
                  "value": "100.0"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.1"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.1"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.2"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.2"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.1"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "100.0"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.1"
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
              "value": "Total for Amy's Bird Sanctuary"
            },
            {
              "value": "854.8"
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
              "value": "854.8"
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
        "ColType": "subt_amount",
        "ColTitle": "Amount"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/CustomerBalanceDetail?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `customerbalancedetailquery`

<details>
<summary>Show schema for `customerbalancedetailquery`</summary>

#### customerbalancedetailquery

Model type: `object`

##### `customer`

Required: Optional
Type: `String`
Default: Include data for all customers

Filters report contents to include information for specified customers.
Supported Values: One or more comma separated customer IDs as returned in the attribute, `Customer.Id`, of the Customer object response code.

##### `shipvia`

Required: Optional
Type: `String`
Default: Include data for all shipping methods

Filter by the shipping method as stored in `Invoice.ShipMethodRef.Name`.
Supported Values: Any shipping method as sent in the `Invoice.ShipMethodRef.Name` attribute at Invoice create- or update-time.

##### `term`

Required: Optional
Type: `String`
Default: Return data for all terms

Filters report contents based on term or terms supplied.
Supported Values: One or more comma separated term IDs as returned in the attribute, `Term.Id` of the Term object response code.

##### `end_duedate`

Required: Optional
Type: `String`
Default: To return all receivables due data

The range of dates over which receivables are due, in the format `YYYY-MM-DD`. `start_duedate` must be less than `end_duedate`. If not specified, all data is returned.

##### `start_duedate`

Required: Optional
Type: `String`
Default: To return all receivables due data

The range of dates over which receivables are due, in the format `YYYY-MM-DD`. `start_duedate` must be less than `end_duedate`. If not specified, all data is returned.

##### `custom1`

Required: Optional
Type: `String`
Default: Include data for all fields

Filter by the specified custom field as defined by the `CustomField` attribute in transaction entities where supported.
Supported Values: Name of custom field.

##### `sort_by`

Required: Optional
Type: `String`
Default: <span class="literal">txn_type</span>

The column type used in sorting report rows. Specify a column type as defined with the columns query parameter.

##### `arpaid`

Required: Optional
Type: `String`
Default: <span class="literal">Unpaid</span>Unpaid

Supported Values:`All`, `Paid`, `Unpaid`

##### `report_date`

Required: Optional
Type: `String`
Default: today's date

Start date to use for the report, in the format `YYYY-MM-DD`.

##### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>Unpaid

The sort order.
Supported Values: `ascend`, `descend`

##### `aging_method`

Required: Optional
Type: `String`
Default: <span class="literal">Report_Date</span>Unpaid

The date upon which aging is determined.
Supported Values:`Report_Date`, `Current`

##### `department`

Required: Optional
Type: `String`
Default: Include data for all departments

Filters report contents to include information for specified departments if so configured in the company file.
Supported Values: One or more comma separated department IDs as returned in the attribute, `Department.Id` of the Department object response code.

##### `columns`

Required: Optional
Type: `String`
Default: columns denoted with *

Column types to be shown in the report.
Supported Values: bill_addr, create_by, create_date, cust_bill_email, cust_comp_name, cust_msg, cust_phone_other, cust_tel, cust_name, deliv_addr, doc_num*, due_date*, last_mod_by, last_mod_date, memo*, sale_sent_state, ship_addr, ship_date, ship_via, term_name, tracking_num, tx_date*, txn_type*
 Additional columns with custom fields enabled: sales_cust1, sales_cust2, sales_cust3
 Additional columns with location tracking enabled: dept_name*

<details>
<summary>Show additonal values supported based on multicurrency settings for the company.</summary>

#### MULTICURRENCY DISABLED

| Name | Description |
| --- | --- |
| currency | N/A |
| exchange rate | N/A |
| open balance | subt_open_bal* |
| amount | subt_amount* |

#### MULTICURRENCY ENABLED

| Name | Description |
| --- | --- |
| currency | currency |
| exchange rate | exch_rate |
| open balance | foreign_open_bal |
| amount | foreign_amount |

</details>

</details>

### Sample Query

This query returns the customer balance detail report for Amy's Bird Sanctuary, (`customer=1`).

#### Example

```text
"BaseURL/v3/company/1386066315/reports/CustomerBalancedDetail?customer=1&start_duedate=2015-08-01&end_duedate=2015-09-30&columns=subt_amount,tx_date"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "Customer": "1",
    "ReportName": "CustomerBalanceDetail",
    "Option": [
      {
        "Name": "report_date",
        "Value": "2016-03-10"
      },
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "DateMacro": "all",
    "Currency": "USD",
    "Time": "2016-03-10T13:43:05-08:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "id": "1",
              "value": "Amy's Bird Sanctuary"
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
                  "value": "2015-08-04"
                },
                {
                  "value": "100.0"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.1"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.1"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.2"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.2"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.1"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "100.0"
                }
              ],
              "type": "Data"
            },
            {
              "ColData": [
                {
                  "value": "2015-08-04"
                },
                {
                  "value": "109.1"
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
              "value": "Total for Amy's Bird Sanctuary"
            },
            {
              "value": "854.8"
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
              "value": "854.8"
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
        "ColType": "subt_amount",
        "ColTitle": "Amount"
      }
    ]
  }
}
```
