# ProfitAndLossDetail

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/profitandlossdetail
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / ProfitAndLossDetail
> Canonical entity: `ProfitAndLossDetail`

The information below provides a reference on how to access the Profit and Loss Detail report from the QuickBooks Online Report Service.

## The profit and loss detail report object

The table below lists all possible attributes that can be returned in the report response. Values are not localized unless indicated. [Click here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions) to download the latest XSD.

### profitandlossdetailquery

Model type: `object`

#### `customer`

Required: Optional
Type: `String`
Default: Include data for all customers

Filters report contents to include information for specified customers.
Supported Values: One or more comma separated customer IDs as returned in the attribute, `Customer.Id`, of the Customer object response code.

#### `account`

Required: Optional
Type: `String`
Default: Data for all account types

(source_account_type) Filters report contents to include information for specified accounts.
Supported Values: One or more comma separated account IDs as returned in the attribute, `Account.Id`, of the Account object response code.

#### `accounting_method`

Required: Optional
Type: `String`
Default: Method defined in prefrences by the <span class="literal">Preferences.ReportPrefs.ReportBasis</span> attribute

The accounting method used in the report. Supported Values:`Cash`, `Accrual`

#### `end_date`

Required: Optional
Type: `String`

The end date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

#### `date_macro`

Required: Optional
Type: `String`
Default: This Fiscal Year-to-date

Predefined date range. Use if you want the report to cover a standard report date range; otherwise, use the `start_date` and `end_date` to cover an explicit report date range.
Supported Values: Today, Yesterday, This Week, Last Week, This Week-to-date, Last Week-to-date, Next Week, Next 4 Weeks, This Month, Last Month, This Month-to-date, Last Month-to-date, Next Month, This Fiscal Quarter, Last Fiscal Quarter, This Fiscal Quarter-to-date, Last Fiscal Quarter-to-date, Next Fiscal Quarter, This Fiscal Year, Last Fiscal Year, This Fiscal Year-to-date, Last Fiscal Year-to-date, Next Fiscal Year

#### `adjusted_gain_loss`

Required: Optional
Type: `String`
Default: <span class="literal">false</span>
Locales: CA

Specifies whether unrealized gain and losses are included in the report.
Supported Values: `true`, `false`

#### `class`

Required: Optional
Type: `String`
Default: Include data for all classes

Filters report contents to include information for specified classes if so configured in the company file.
Supported Values: One or more comma separated class IDs as returned in the attribute, `Class.Id`, of the Class entity response code.

#### `sort_by`

Required: Optional
Type: `String`
Default: <span class="literal">txn_type</span>

The column type used in sorting report rows. Specify a column type as defined with the columns query parameter.

#### `payment_method`

Required: Optional
Type: `String`
Default: Default includes information for all payment methods

Filters report contents based on payment method.
Supported Values: `Cash`, `Check`, `Dinners Club`, `American Express`, `Discover`, `MasterCard`, `Visa`

#### `sort_order`

Required: Optional
Type: `String`
Default: <span class="literal">ascend</span>

The sort order.
Supported Values: `ascend`, `descend`

#### `employee`

Required: Optional
Type: `String`
Default: Include data for all employees

Filters report contents to include information for specified employees.
Supported Values: One or more comma separated account IDs as returned in the attribute, `Employee.Id`, of the Employee entity response code.

#### `department`

Required: Optional
Type: `String`
Default: Include data for all departments

Filters report contents to include information for specified departments if so configured in the company file.
Supported Values: One or more comma separated department IDs as returned in the attribute, `Department.Id` of the Department object response code.

#### `vendor`

Required: Optional
Type: `String`
Default: Return data for all vendors

Filters report contents to include information for specified vendors.
Supported Values: One or more comma separated vendor IDs as returned in the attribute, `Vendor.Id`, of the Vendor object response code.

#### `account_type`

Required: Optional
Type: `String`
Default: All account types

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

#### `start_date`

Required: Optional
Type: `String`

The start date of the report, in the format `YYYY-MM-DD`. `start_date` must be less than `end_date`. Use if you want the report to cover an explicit date range; otherwise, use `date_macro` to cover a standard report date range. If not specified value of `date_macro` is used

#### `columns`

Required: Optional
Type: `String`
Default: columns denoted with *

Column types to be shown in the report.
Supported Values: create_by, create_date, doc_num*, last_mod_by, last_mod_date, memo*, name*, pmt_mthd, split_acc*, tx_date*, txn_type*
 Additional columns with tax enabled: tax_code
 Additional columns with class tracking enabled: klass_name*
 Additional columns with location tracking enabled: dept_name*
 Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies).
NonTracking status is enabled for the company if `CompanyInfo.NameValue.Name.NonTracking` is set to `true`. Currently enabled for Canadian company, other locales can be added in the future.

<details>
<summary>Show additonal values supported based on multicurrency settings for the company.</summary>

#### MULTICURRENCY SETTINGS

| Name | Description |
| --- | --- |
|  | MULTICURRENCY DISABLED |
| debit(not supported for P&L Detail Report) | debt_amt |
| credit(not supported for P&L Detail Report) | credit_amt |
| currency | N/A |
| exchange rate | N/A |
| open balance(not supported for P&L Detail Report) | nat_open_bal |
| amount<br>*use for NonTracking disabled comapanies* | subt_nat_amount* |
| amount<br>*use for NonTracking enabled comapanies* | subt_nat_amount_nt* |
| balance<br>*use for NonTracking disabled comapanies* | rbal_nat_amount* |
| balance<br>*use for NonTracking enabled comapanies* | rbal_nat_amount_nt* |
| tax amount(not supported for P&L Detail Report) | tax_amount |
| taxable amount(not supported for P&L Detail Report) | net_amount |

</details>

#### Example

```json
{
  "Header": {
    "Customer": "3",
    "ReportName": "ProfitAndLossDetail",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "ReportBasis": "Accrual",
    "StartPeriod": "2015-06-01",
    "Currency": "USD",
    "EndPeriod": "2015-06-30",
    "Time": "2016-03-11T14:53:39-08:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "value": "Ordinary Income/Expenses"
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
              "Header": {
                "ColData": [
                  {
                    "value": "Income"
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
                    "Header": {
                      "ColData": [
                        {
                          "id": "49",
                          "value": "Landscaping Services"
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
                          "Header": {
                            "ColData": [
                              {
                                "value": "Job Materials"
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
                                "Header": {
                                  "ColData": [
                                    {
                                      "value": "Plants and Soil"
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
                                          "value": "2015-06-27"
                                        },
                                        {
                                          "id": "3",
                                          "value": "Cool Cars"
                                        },
                                        {
                                          "value": "1750.0"
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
                                      "value": "Total for Plants and Soil"
                                    },
                                    {
                                      "value": ""
                                    },
                                    {
                                      "value": "1750.0"
                                    }
                                  ]
                                }
                              }
                            ]
                          },
                          "type": "Section",
                          "Summary": {
                            "ColData": [
                              {
                                "value": "Total for Job Materials"
                              },
                              {
                                "value": ""
                              },
                              {
                                "value": "1750.0"
                              }
                            ]
                          }
                        }
                      ]
                    },
                    "type": "Section",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total for Landscaping Services"
                        },
                        {
                          "value": ""
                        },
                        {
                          "value": "1750.0"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "id": "79",
                          "value": "Sales of Product Income"
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
                              "value": "2015-06-27"
                            },
                            {
                              "id": "3",
                              "value": "Cool Cars"
                            },
                            {
                              "value": "20.0"
                            }
                          ],
                          "type": "Data"
                        },
                        {
                          "ColData": [
                            {
                              "value": "2015-06-27"
                            },
                            {
                              "id": "3",
                              "value": "Cool Cars"
                            },
                            {
                              "value": "24.0"
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
                          "value": "Total for Sales of Product Income"
                        },
                        {
                          "value": ""
                        },
                        {
                          "value": "44.0"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "id": "1",
                          "value": "Services"
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
                              "value": "2015-06-27"
                            },
                            {
                              "id": "3",
                              "value": "Cool Cars"
                            },
                            {
                              "value": "400.0"
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
                          "value": "Total for Services"
                        },
                        {
                          "value": ""
                        },
                        {
                          "value": "400.0"
                        }
                      ]
                    }
                  }
                ]
              },
              "type": "Section",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total for Income"
                  },
                  {
                    "value": ""
                  },
                  {
                    "value": "2194.0"
                  }
                ]
              }
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Net Income"
            },
            {
              "value": ""
            },
            {
              "value": "2194.0"
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
        "ColType": "name",
        "ColTitle": "Name"
      },
      {
        "ColType": "subt_nat_amount",
        "ColTitle": "Amount"
      }
    ]
  }
}
```

## Query a report

### Definition

- **Accept type:** `application/json`
- **Operation:** `GET /v3/company/<realmID>/reports/ProfitAndLossDetail?<name>=<value>[&...]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Query Parameters

Customize the information returned in the report by specifying query parameters with the query. Listed below are query parameters available for this report.

Schema: `profitandlossdetailquery`

_Matches the top-level sample object schema._

### Sample Query

This query returns detailed profit and loss information for June 2015 for Cool Cars (`customer=3`).

#### Example

```text
"BaseURL/v3/company/1386066315/reports/ProfitAndLossDetail?start_date=2015-06-01&end_date=2015-06-30&customer=3&columns=tx_date%2Cname%2Csubt_nat_amount"
```

### Returns

Returns the report object.

#### Example

```json
{
  "Header": {
    "Customer": "3",
    "ReportName": "ProfitAndLossDetail",
    "Option": [
      {
        "Name": "NoReportData",
        "Value": "false"
      }
    ],
    "ReportBasis": "Accrual",
    "StartPeriod": "2015-06-01",
    "Currency": "USD",
    "EndPeriod": "2015-06-30",
    "Time": "2016-03-11T14:53:39-08:00"
  },
  "Rows": {
    "Row": [
      {
        "Header": {
          "ColData": [
            {
              "value": "Ordinary Income/Expenses"
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
              "Header": {
                "ColData": [
                  {
                    "value": "Income"
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
                    "Header": {
                      "ColData": [
                        {
                          "id": "49",
                          "value": "Landscaping Services"
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
                          "Header": {
                            "ColData": [
                              {
                                "value": "Job Materials"
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
                                "Header": {
                                  "ColData": [
                                    {
                                      "value": "Plants and Soil"
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
                                          "value": "2015-06-27"
                                        },
                                        {
                                          "id": "3",
                                          "value": "Cool Cars"
                                        },
                                        {
                                          "value": "1750.0"
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
                                      "value": "Total for Plants and Soil"
                                    },
                                    {
                                      "value": ""
                                    },
                                    {
                                      "value": "1750.0"
                                    }
                                  ]
                                }
                              }
                            ]
                          },
                          "type": "Section",
                          "Summary": {
                            "ColData": [
                              {
                                "value": "Total for Job Materials"
                              },
                              {
                                "value": ""
                              },
                              {
                                "value": "1750.0"
                              }
                            ]
                          }
                        }
                      ]
                    },
                    "type": "Section",
                    "Summary": {
                      "ColData": [
                        {
                          "value": "Total for Landscaping Services"
                        },
                        {
                          "value": ""
                        },
                        {
                          "value": "1750.0"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "id": "79",
                          "value": "Sales of Product Income"
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
                              "value": "2015-06-27"
                            },
                            {
                              "id": "3",
                              "value": "Cool Cars"
                            },
                            {
                              "value": "20.0"
                            }
                          ],
                          "type": "Data"
                        },
                        {
                          "ColData": [
                            {
                              "value": "2015-06-27"
                            },
                            {
                              "id": "3",
                              "value": "Cool Cars"
                            },
                            {
                              "value": "24.0"
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
                          "value": "Total for Sales of Product Income"
                        },
                        {
                          "value": ""
                        },
                        {
                          "value": "44.0"
                        }
                      ]
                    }
                  },
                  {
                    "Header": {
                      "ColData": [
                        {
                          "id": "1",
                          "value": "Services"
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
                              "value": "2015-06-27"
                            },
                            {
                              "id": "3",
                              "value": "Cool Cars"
                            },
                            {
                              "value": "400.0"
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
                          "value": "Total for Services"
                        },
                        {
                          "value": ""
                        },
                        {
                          "value": "400.0"
                        }
                      ]
                    }
                  }
                ]
              },
              "type": "Section",
              "Summary": {
                "ColData": [
                  {
                    "value": "Total for Income"
                  },
                  {
                    "value": ""
                  },
                  {
                    "value": "2194.0"
                  }
                ]
              }
            }
          ]
        },
        "type": "Section",
        "Summary": {
          "ColData": [
            {
              "value": "Net Income"
            },
            {
              "value": ""
            },
            {
              "value": "2194.0"
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
        "ColType": "name",
        "ColTitle": "Name"
      },
      {
        "ColType": "subt_nat_amount",
        "ColTitle": "Amount"
      }
    ]
  }
}
```
