# RecurringTransaction

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/recurringtransaction
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / RecurringTransaction
> Canonical entity: `RecurringTransaction`

A RecurringTransaction object refers to scheduling the creation of transactions, setting up reminders, and creating transaction templates for later use. This feature is available in QuickBooks Online Essentials and Plus SKUs.

## The RecurringTransaction object

### recurringtransactionresponse

Model type: `object`

#### `Id`

Required: Optional
Type: `String`
Traits: system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `RecurringInfo`

Required: Required
Type: `RecurringInfo`

Describes the recurring schedules for transactions.

<details>
<summary>Child attributes for `RecurringInfo`</summary>

##### recurringinfo

Model type: `object`

###### `Active`

Type: `Boolean`

This setting indicates whether the recurring schedule is enabled.

###### `RecurType`

Required: Optional
Type: `string`
Traits: filterable, sortable

The recur type which can be `Automated`, `Reminded` or `UnScheduled`.

###### `ScheduleInfo`

Required: Optional
Type: `RecurringScheduleInfo`

Describes the scheduling information for the transaction.

<details>
<summary>Child attributes for `ScheduleInfo`</summary>

###### recurringscheduleinfo

Model type: `object`

###### `DayOfWeek`

Required: Optional
Type: `String`

The day of the week.

###### `StartDate`

Required: Optional
Type: `DateTime`

The start date for the recurring schedule

<details>
<summary>Child attributes for `StartDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `MaxOccurrences`

Required: Optional
Type: `String`

The max number of recurring occurrences.

###### `RemindDays`

Required: Optional
Type: `String`

The days before start date for a reminded RecurType.

###### `IntervalType`

Required: Optional
Type: `String`

Specifies the interval type. Values for `IntervalType`can be one of the following:

Yearly

— The allowed properties for yearly interval type are :

- ScheduleInfo.StartDate
- ScheduleInfo.EndDate or ScheduleInfo.MaxOccurrences
- ScheduleInfo.DaysBefore (or ScheduleInfo.RemindDays for Reminded RecurType)
- ScheduleInfo.MonthOfYear
- ScheduleInfo.DayOfMonth

Monthly

— The allowed properties for monthly interval type are :

- ScheduleInfo.NumInterval
- ScheduleInfo.StartDate
- ScheduleInfo.EndDate or ScheduleInfo.MaxOccurrences
- ScheduleInfo.DaysBefore (or ScheduleInfo.RemindDays for Reminded RecurType)
- (ScheduleInfo.DayOfWeek and ScheduleInfo.WeekOfMonth) or ScheduleInfo.DayOfMonth

Weekly

— The allowed properties for weekly interval type are :

- ScheduleInfo.NumInterval
- ScheduleInfo.StartDate
- ScheduleInfo.EndDate or ScheduleInfo.MaxOccurrence
- ScheduleInfo.DaysBefore(or ScheduleInfo.RemindDays for Reminded RecurType)
- ScheduleInfo.DayOfWeek

Daily

— The allowed properties for daily interval type are :

- ScheduleInfo.NumInterval
- ScheduleInfo.StartDate
- ScheduleInfo.EndDate or ScheduleInfo.MaxOccurrences
- ScheduleInfo.DaysBefore (or ScheduleInfo.RemindDays for Reminded RecurType)

###### `WeekOfMonth`

Required: Optional
Type: `String`

The week of the month.

###### `MonthOfYear`

Required: Optional
Type: `String`

The month of the year.

###### `DaysBefore`

Required: Optional
Type: `String`

The days before the scheduled date.

###### `NextDate`

Required: Optional
Type: `DateTime`
Traits: read only

The date when the next transaction is created.

<details>
<summary>Child attributes for `NextDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `NumInterval`

Required: Optional
Type: `String`

The interval based on the interval type.

###### `EndDate`

Required: Optional
Type: `DateTime`

The end date for the recurring schedule.

<details>
<summary>Child attributes for `EndDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `PreviousDate`

Required: Optional
Type: `DateTime`
Traits: read only

The date when the last transaction is created.

<details>
<summary>Child attributes for `PreviousDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `DayOfMonth`

Required: Optional
Type: `String`

The day of the month.

</details>

###### `Name`

Required: Optional
Type: `string`
Traits: filterable, sortable

The name of the recurring schedule template.

</details>

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `Type`

Type: `String`
Traits: filterable

Specifies the list of entities that are supported for recurring transactions: `Bill`,`Purchase`,`CreditMemo`,`Deposit`,`Estimate`,`Invoice`,`JournalEntry`,`RefundReceipt`,`SalesReceipt`,`Transfer`,`VendorCredit` or `PurchaseOrder`

#### `RecurDataRef`

Required: Optional
Type: `ReferenceType`
Traits: filterable, sortable

Reference to the recur template associated with the transaction.

<details>
<summary>Child attributes for `RecurDataRef`</summary>

##### referencetype

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

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`
Traits: filterable

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
  "QueryResponse": {
    "startPosition": 1,
    "maxResults": 1,
    "RecurringTransaction": [
      {
        "Bill": {
          "SyncToken": "0",
          "domain": "QBO",
          "RecurringInfo": {
            "Active": true,
            "RecurType": "Automated",
            "ScheduleInfo": {
              "NumInterval": 1,
              "NextDate": "2020-08-01",
              "DayOfMonth": 1,
              "PreviousDate": "2020-07-01",
              "IntervalType": "Monthly"
            },
            "Name": "Telephone Bill"
          },
          "RecurDataRef": {
            "value": "2"
          },
          "CurrencyRef": {
            "name": "United States Dollar",
            "value": "USD"
          },
          "TotalAmt": 74.36,
          "APAccountRef": {
            "name": "Name_01ff6",
            "value": "33"
          },
          "Id": "20",
          "sparse": false,
          "VendorRef": {
            "name": "Cal Telephone",
            "value": "32"
          },
          "Line": [
            {
              "Description": "Monthly Phone Bill",
              "DetailType": "AccountBasedExpenseLineDetail",
              "LineNum": 1,
              "Amount": 74.36,
              "Id": "1",
              "AccountBasedExpenseLineDetail": {
                "TaxCodeRef": {
                  "value": "NON"
                },
                "AccountRef": {
                  "name": "Utilities:Telephone",
                  "value": "77"
                },
                "BillableStatus": "NotBillable"
              }
            }
          ],
          "Balance": 74.36,
          "SalesTermRef": {
            "value": "3"
          },
          "MetaData": {
            "CreateTime": "2019-02-17T15:27:25-08:00",
            "LastUpdatedTime": "2020-07-05T01:19:13-07:00"
          }
        }
      }
    ]
  },
  "time": "2020-07-09T10:18:02.049-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-07-09T10:17:26.684-07:00">
    <QueryResponse startPosition="1" maxResults="1">
        <RecurringTransaction>
            <Bill domain="QBO" sparse="false">
                <Id>20</Id>
                <SyncToken>0</SyncToken>
                <MetaData>
                    <CreateTime>2019-02-17T15:27:25-08:00</CreateTime>
                    <LastUpdatedTime>2020-07-05T01:19:13-07:00</LastUpdatedTime>
                </MetaData>
                <CurrencyRef name="United States Dollar">USD</CurrencyRef>
                <Line>
                    <Id>1</Id>
                    <LineNum>1</LineNum>
                    <Description>Monthly Phone Bill</Description>
                    <Amount>74.36</Amount>
                    <DetailType>AccountBasedExpenseLineDetail</DetailType>
                    <AccountBasedExpenseLineDetail>
                        <AccountRef name="Utilities:Telephone">77</AccountRef>
                        <BillableStatus>NotBillable</BillableStatus>
                        <TaxCodeRef>NON</TaxCodeRef>
                    </AccountBasedExpenseLineDetail>
                </Line>
                <RecurDataRef>2</RecurDataRef>
                <RecurringInfo>
                    <Name>Telephone Bill</Name>
                    <RecurType>Automated</RecurType>
                    <Active>true</Active>
                    <ScheduleInfo>
                        <IntervalType>Monthly</IntervalType>
                        <NumInterval>1</NumInterval>
                        <DayOfMonth>1</DayOfMonth>
                        <NextDate>2020-08-01</NextDate>
                        <PreviousDate>2020-07-01</PreviousDate>
                    </ScheduleInfo>
                </RecurringInfo>
                <VendorRef name="Cal Telephone">32</VendorRef>
                <APAccountRef name="Name_01ff6">33</APAccountRef>
                <TotalAmt>74.36</TotalAmt>
                <SalesTermRef>3</SalesTermRef>
                <Balance>74.36</Balance>
            </Bill>
        </RecurringTransaction>
    </QueryResponse>
</IntuitResponse>
```

## Create a recurring transaction

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/recurringtransaction`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- A RecurringTransaction object must have at least one line that describes an item.
- A RecurringTransaction object must have a `DepositToAccountRef`.
- If the billing address is not provided, the customer address is used to fill those values.
- `TaxCode.CustomSalesTax` cannot be used as `TxnTaxCodeRef`.
    - This taxcode is reserved to mark the transaction as created using old sales tax model with no predefined tax rates.
    - You cannot create or update a transaction that implements `TaxCode.CustomSalesTax`.

### Request Body

The minimum elements to create an RecurringTransaction are listed here. You need the minimum payload for the transaction you are creating and the below elements.

Schema: `recurringtransactionrequest`

<details>
<summary>Show schema for `recurringtransactionrequest`</summary>

#### recurringtransactionrequest

Model type: `object`

##### `RecurringInfo`

Required: Required
Type: `RecurringInfo`

Describes the recurring schedules for transactions.

<details>
<summary>Child attributes for `RecurringInfo`</summary>

###### recurringinfo

Model type: `object`

###### `Active`

Type: `Boolean`

This setting indicates whether the recurring schedule is enabled.

###### `RecurType`

Required: Optional
Type: `string`
Traits: filterable, sortable

The recur type which can be `Automated`, `Reminded` or `UnScheduled`.

###### `ScheduleInfo`

Required: Optional
Type: `RecurringScheduleInfo`

Describes the scheduling information for the transaction.

<details>
<summary>Child attributes for `ScheduleInfo`</summary>

###### recurringscheduleinfo

Model type: `object`

###### `DayOfWeek`

Required: Optional
Type: `String`

The day of the week.

###### `StartDate`

Required: Optional
Type: `DateTime`

The start date for the recurring schedule

<details>
<summary>Child attributes for `StartDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `MaxOccurrences`

Required: Optional
Type: `String`

The max number of recurring occurrences.

###### `RemindDays`

Required: Optional
Type: `String`

The days before start date for a reminded RecurType.

###### `IntervalType`

Required: Optional
Type: `String`

Specifies the interval type. Values for `IntervalType`can be one of the following:

Yearly

— The allowed properties for yearly interval type are :

- ScheduleInfo.StartDate
- ScheduleInfo.EndDate or ScheduleInfo.MaxOccurrences
- ScheduleInfo.DaysBefore (or ScheduleInfo.RemindDays for Reminded RecurType)
- ScheduleInfo.MonthOfYear
- ScheduleInfo.DayOfMonth

Monthly

— The allowed properties for monthly interval type are :

- ScheduleInfo.NumInterval
- ScheduleInfo.StartDate
- ScheduleInfo.EndDate or ScheduleInfo.MaxOccurrences
- ScheduleInfo.DaysBefore (or ScheduleInfo.RemindDays for Reminded RecurType)
- (ScheduleInfo.DayOfWeek and ScheduleInfo.WeekOfMonth) or ScheduleInfo.DayOfMonth

Weekly

— The allowed properties for weekly interval type are :

- ScheduleInfo.NumInterval
- ScheduleInfo.StartDate
- ScheduleInfo.EndDate or ScheduleInfo.MaxOccurrence
- ScheduleInfo.DaysBefore(or ScheduleInfo.RemindDays for Reminded RecurType)
- ScheduleInfo.DayOfWeek

Daily

— The allowed properties for daily interval type are :

- ScheduleInfo.NumInterval
- ScheduleInfo.StartDate
- ScheduleInfo.EndDate or ScheduleInfo.MaxOccurrences
- ScheduleInfo.DaysBefore (or ScheduleInfo.RemindDays for Reminded RecurType)

###### `WeekOfMonth`

Required: Optional
Type: `String`

The week of the month.

###### `MonthOfYear`

Required: Optional
Type: `String`

The month of the year.

###### `DaysBefore`

Required: Optional
Type: `String`

The days before the scheduled date.

###### `NextDate`

Required: Optional
Type: `DateTime`
Traits: read only

The date when the next transaction is created.

<details>
<summary>Child attributes for `NextDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `NumInterval`

Required: Optional
Type: `String`

The interval based on the interval type.

###### `EndDate`

Required: Optional
Type: `DateTime`

The end date for the recurring schedule.

<details>
<summary>Child attributes for `EndDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `PreviousDate`

Required: Optional
Type: `DateTime`
Traits: read only

The date when the last transaction is created.

<details>
<summary>Child attributes for `PreviousDate`</summary>

###### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

###### `DayOfMonth`

Required: Optional
Type: `String`

The day of the month.

</details>

###### `Name`

Required: Optional
Type: `string`
Traits: filterable, sortable

The name of the recurring schedule template.

</details>

</details>

#### Example

```json
{
  "Invoice": {
    "AllowOnlineACHPayment": false,
    "ShipFromAddr": {
      "Id": "713",
      "Line1": "123 Sierra Way, San Pablo, CA, 87999, USA"
    },
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "HomeBalance": 55,
    "PrintStatus": "NeedToPrint",
    "BillEmail": {
      "Address": "Travis@Waldron.com"
    },
    "DeliveryInfo": {
      "DeliveryType": "Email"
    },
    "TotalAmt": 55,
    "Line": [
      {
        "LineNum": 1,
        "Amount": 55,
        "SalesItemLineDetail": {
          "ItemRef": {
            "name": "Hours",
            "value": "2"
          },
          "Qty": 1,
          "TaxCodeRef": {
            "value": "NON"
          },
          "ItemAccountRef": {
            "name": "Services",
            "value": "1"
          },
          "UnitPrice": 55,
          "TaxClassificationRef": {
            "value": "EUC-99990201-V1-00020000"
          }
        },
        "Id": "1",
        "DetailType": "SalesItemLineDetail"
      },
      {
        "DetailType": "SubTotalLineDetail",
        "Amount": 55,
        "SubTotalLineDetail": {}
      }
    ],
    "ApplyTaxAfterDiscount": false,
    "RecurDataRef": {
      "value": "4"
    },
    "TaxExemptionRef": {},
    "Balance": 55,
    "CustomerRef": {
      "name": "Travis Waldron",
      "value": "26"
    },
    "TxnTaxDetail": {
      "TotalTax": 0
    },
    "AllowOnlineCreditCardPayment": false,
    "LinkedTxn": [],
    "RecurringInfo": {
      "Active": true,
      "RecurType": "Automated",
      "ScheduleInfo": {
        "StartDate": "2020-09-01",
        "MaxOccurrences": 10,
        "IntervalType": "Monthly",
        "DaysBefore": 2,
        "NextDate": "2020-09-01",
        "NumInterval": 1,
        "DayOfMonth": 1
      },
      "Name": "RecurTemplate2"
    },
    "ExchangeRate": 1,
    "ShipAddr": {
      "City": "Monlo Park",
      "Line1": "78 First St.",
      "PostalCode": "94304",
      "Lat": "37.4585825",
      "Long": "-122.1352789",
      "CountrySubDivisionCode": "CA",
      "Id": "27"
    },
    "DepartmentRef": {
      "name": "DeptName100768f890d64",
      "value": "1"
    },
    "EmailStatus": "NeedToSend",
    "BillAddr": {
      "City": "Monlo Park",
      "Line1": "78 First St.",
      "PostalCode": "94304",
      "Lat": "37.4585825",
      "Long": "-122.1352789",
      "CountrySubDivisionCode": "CA",
      "Id": "27"
    },
    "FreeFormAddress": true,
    "CustomField": [
      {
        "DefinitionId": "1",
        "Type": "StringType",
        "Name": "Crew #"
      }
    ],
    "HomeTotalAmt": 55,
    "AllowOnlinePayment": false,
    "AllowIPNPayment": false
  }
}
```

#### XML example

```xml
<RecurringTransaction xmlns="http://schema.intuit.com/finance/v3">>
        <Invoice>

            <CustomField>
                <DefinitionId>1</DefinitionId>
                <Name>Crew #</Name>
                <Type>StringType</Type>
            </CustomField>
            <DepartmentRef name="DeptName100768f890d64">1</DepartmentRef>
            <CurrencyRef name="United States Dollar">USD</CurrencyRef>
            <ExchangeRate>1</ExchangeRate>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Amount>55.00</Amount>
                <DetailType>SalesItemLineDetail</DetailType>
                <SalesItemLineDetail>
                    <ItemRef name="Hours">2</ItemRef>
                    <UnitPrice>55</UnitPrice>
                    <Qty>1</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                </SalesItemLineDetail>
            </Line>
            <Line>
                <Amount>55.00</Amount>
                <DetailType>SubTotalLineDetail</DetailType>
                <SubTotalLineDetail/>
            </Line>
            <TxnTaxDetail>
                <TotalTax>0</TotalTax>
            </TxnTaxDetail>
            <RecurDataRef>5</RecurDataRef>
            <RecurringInfo>
                <Name>RecurTemplate3</Name>
                <RecurType>Automated</RecurType>
                <Active>true</Active>
                <ScheduleInfo>
                    <IntervalType>Monthly</IntervalType>
                    <NumInterval>1</NumInterval>
                    <DayOfMonth>1</DayOfMonth>
                    <DaysBefore>2</DaysBefore>
                    <MaxOccurrences>10</MaxOccurrences>
                    <StartDate>2020-09-01</StartDate>
                    <NextDate>2020-09-01</NextDate>
                </ScheduleInfo>
            </RecurringInfo>
            <CustomerRef name="Travis Waldron">26</CustomerRef>
            <BillAddr>
                <Id>714</Id>
                <Line1>78 First St.</Line1>
                <City>Monlo Park</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94304</PostalCode>
            </BillAddr>
            <ShipAddr>
                <Id>715</Id>
                <Line1>78 First St.</Line1>
                <City>Monlo Park</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94304</PostalCode>
            </ShipAddr>
            <DueDate>2020-08-13</DueDate>
            <TotalAmt>55.00</TotalAmt>
            <HomeTotalAmt>55.00</HomeTotalAmt>
            <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
            <PrintStatus>NeedToPrint</PrintStatus>
            <EmailStatus>NeedToSend</EmailStatus>
            <BillEmail>
                <Address>Travis@Waldron.com</Address>
            </BillEmail>
            <Balance>55.00</Balance>
            <DeliveryInfo>
                <DeliveryType>Email</DeliveryType>
            </DeliveryInfo>
            <AllowIPNPayment>false</AllowIPNPayment>
            <AllowOnlinePayment>false</AllowOnlinePayment>
            <AllowOnlineCreditCardPayment>false</AllowOnlineCreditCardPayment>
            <AllowOnlineACHPayment>false</AllowOnlineACHPayment>
        </Invoice>
    </RecurringTransaction>
```

### Returns

The RecurringTransaction response body.

#### Example

```json
{
  "time": "2020-08-13T17:04:57.367-07:00",
  "RecurringTransaction": {
    "Invoice": {
      "AllowOnlineACHPayment": false,
      "domain": "QBO",
      "CurrencyRef": {
        "name": "United States Dollar",
        "value": "USD"
      },
      "PrintStatus": "NeedToPrint",
      "BillEmail": {
        "Address": "Travis@Waldron.com"
      },
      "DeliveryInfo": {
        "DeliveryType": "Email"
      },
      "TotalAmt": 55.0,
      "Line": [
        {
          "LineNum": 1,
          "Amount": 55.0,
          "SalesItemLineDetail": {
            "TaxCodeRef": {
              "value": "NON"
            },
            "Qty": 1,
            "UnitPrice": 55,
            "ItemRef": {
              "name": "Hours",
              "value": "2"
            }
          },
          "Id": "1",
          "DetailType": "SalesItemLineDetail"
        },
        {
          "DetailType": "SubTotalLineDetail",
          "Amount": 55.0,
          "SubTotalLineDetail": {}
        }
      ],
      "DueDate": "2020-08-13",
      "MetaData": {
        "CreateTime": "2020-08-13T17:04:57-07:00",
        "LastUpdatedTime": "2020-08-13T17:04:57-07:00"
      },
      "sparse": false,
      "RecurDataRef": {
        "value": "6"
      },
      "Balance": 55.0,
      "CustomerRef": {
        "name": "Travis Waldron",
        "value": "26"
      },
      "TxnTaxDetail": {
        "TotalTax": 0
      },
      "AllowOnlineCreditCardPayment": false,
      "SyncToken": "0",
      "LinkedTxn": [],
      "RecurringInfo": {
        "Active": true,
        "RecurType": "Automated",
        "ScheduleInfo": {
          "StartDate": "2020-09-01",
          "MaxOccurrences": 10,
          "IntervalType": "Monthly",
          "DaysBefore": 2,
          "NextDate": "2020-09-01",
          "NumInterval": 1,
          "DayOfMonth": 1
        },
        "Name": "RecurTemplate2"
      },
      "ExchangeRate": 1,
      "ShipAddr": {
        "CountrySubDivisionCode": "CA",
        "City": "Monlo Park",
        "PostalCode": "94304",
        "Id": "717",
        "Line1": "78 First St."
      },
      "HomeTotalAmt": 55.0,
      "DepartmentRef": {
        "name": "DeptName100768f890d64",
        "value": "1"
      },
      "EmailStatus": "NeedToSend",
      "BillAddr": {
        "CountrySubDivisionCode": "CA",
        "City": "Monlo Park",
        "PostalCode": "94304",
        "Id": "716",
        "Line1": "78 First St."
      },
      "ApplyTaxAfterDiscount": false,
      "CustomField": [
        {
          "DefinitionId": "1",
          "Type": "StringType",
          "Name": "Crew #"
        }
      ],
      "Id": "1483",
      "AllowOnlinePayment": false,
      "AllowIPNPayment": false
    }
  }
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-08-13T17:35:04.950-07:00">
    <RecurringTransaction>
        <Invoice domain="QBO" sparse="false">
            <Id>1484</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2020-08-13T17:35:05-07:00</CreateTime>
                <LastUpdatedTime>2020-08-13T17:35:05-07:00</LastUpdatedTime>
            </MetaData>
            <CustomField>
                <DefinitionId>1</DefinitionId>
                <Name>Crew #</Name>
                <Type>StringType</Type>
            </CustomField>
            <DepartmentRef name="DeptName100768f890d64">1</DepartmentRef>
            <CurrencyRef name="United States Dollar">USD</CurrencyRef>
            <ExchangeRate>1</ExchangeRate>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Amount>55.00</Amount>
                <DetailType>SalesItemLineDetail</DetailType>
                <SalesItemLineDetail>
                    <ItemRef name="Hours">2</ItemRef>
                    <UnitPrice>55</UnitPrice>
                    <Qty>1</Qty>
                    <TaxCodeRef>NON</TaxCodeRef>
                </SalesItemLineDetail>
            </Line>
            <Line>
                <Amount>55.00</Amount>
                <DetailType>SubTotalLineDetail</DetailType>
                <SubTotalLineDetail/>
            </Line>
            <TxnTaxDetail>
                <TotalTax>0</TotalTax>
            </TxnTaxDetail>
            <RecurDataRef>7</RecurDataRef>
            <RecurringInfo>
                <Name>RecurTemplate3</Name>
                <RecurType>Automated</RecurType>
                <Active>true</Active>
                <ScheduleInfo>
                    <IntervalType>Monthly</IntervalType>
                    <NumInterval>1</NumInterval>
                    <DayOfMonth>1</DayOfMonth>
                    <DaysBefore>2</DaysBefore>
                    <MaxOccurrences>10</MaxOccurrences>
                    <StartDate>2020-09-01</StartDate>
                    <NextDate>2020-09-01</NextDate>
                </ScheduleInfo>
            </RecurringInfo>
            <CustomerRef name="Travis Waldron">26</CustomerRef>
            <BillAddr>
                <Id>718</Id>
                <Line1>78 First St.</Line1>
                <City>Monlo Park</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94304</PostalCode>
            </BillAddr>
            <ShipAddr>
                <Id>719</Id>
                <Line1>78 First St.</Line1>
                <City>Monlo Park</City>
                <CountrySubDivisionCode>CA</CountrySubDivisionCode>
                <PostalCode>94304</PostalCode>
            </ShipAddr>
            <DueDate>2020-08-13</DueDate>
            <TotalAmt>55.00</TotalAmt>
            <HomeTotalAmt>55.00</HomeTotalAmt>
            <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
            <PrintStatus>NeedToPrint</PrintStatus>
            <EmailStatus>NeedToSend</EmailStatus>
            <BillEmail>
                <Address>Travis@Waldron.com</Address>
            </BillEmail>
            <Balance>55.00</Balance>
            <DeliveryInfo>
                <DeliveryType>Email</DeliveryType>
            </DeliveryInfo>
            <AllowIPNPayment>false</AllowIPNPayment>
            <AllowOnlinePayment>false</AllowOnlinePayment>
            <AllowOnlineCreditCardPayment>false</AllowOnlineCreditCardPayment>
            <AllowOnlineACHPayment>false</AllowOnlineACHPayment>
        </Invoice>
    </RecurringTransaction>
</IntuitResponse>
```

## Delete a recurring transaction

### Definition

- **Operation:** `POST /v3/company/<realmID>/recurringtransaction?operation=delete`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

This operation deletes the RecurringTransaction object specified in the request body. Include a minimum of `RecurringTransaction.Id` and `SyncToken` in the request body. You must unlink any linked transactions associated with the RecurringTransaction object before deleting it. The sample code uses the `Invoice` entity type.

### Request Body

Schema: `deleterequest`

<details>
<summary>Show schema for `deleterequest`</summary>

#### deleterequest

Model type: `object`

##### `SyncToken`

Required: Required
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

##### `id`

Required: Required
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object.

</details>

#### Example

```json
{
  "Invoice": {
    "SyncToken": "0",
    "Id": "1483"
  }
}
```

#### XML example

```xml
 <RecurringTransaction xmlns="http://schema.intuit.com/finance/v3" domain="QBO" sparse="false">
        <Invoice>
            <Id>1484</Id>
            <SyncToken>0</SyncToken>
        </Invoice>
 </RecurringTransaction>
```

### Returns

Returns the delete response.

#### Example

```json
{
  "time": "2020-08-13T17:40:08.008-07:00",
  "RecurringTransaction": {
    "status": "Deleted",
    "domain": "QBO",
    "Invoice": {
      "Id": "1483"
    }
  }
}
```

#### XML example

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-08-13T17:38:14.907-07:00">
    <RecurringTransaction domain="QBO" status="Deleted">
        <Invoice>
            <Id>1484</Id>
        </Invoice>
    </RecurringTransaction>
</IntuitResponse>
```

## Query a recurring transaction

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"Select * From RecurringTransaction"
```

#### XML example

```sql
select * from RecurringTransaction
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "maxResults": 3,
    "RecurringTransaction": [
      {
        "Invoice": {
          "AllowOnlineACHPayment": false,
          "domain": "QBO",
          "CurrencyRef": {
            "name": "United States Dollar",
            "value": "USD"
          },
          "PrintStatus": "NeedToPrint",
          "TotalAmt": 11111.0,
          "Line": [
            {
              "LineNum": 1,
              "Amount": 11111.0,
              "SalesItemLineDetail": {
                "TaxCodeRef": {
                  "value": "NON"
                },
                "ItemRef": {
                  "name": "Garden Supplies3223",
                  "value": "211"
                }
              },
              "Id": "1",
              "DetailType": "SalesItemLineDetail"
            },
            {
              "DetailType": "SubTotalLineDetail",
              "Amount": 11111.0,
              "SubTotalLineDetail": {}
            }
          ],
          "ApplyTaxAfterDiscount": false,
          "RecurDataRef": {
            "value": "4"
          },
          "Balance": 11111.0,
          "CustomerRef": {
            "name": "0c9ff29a3c3640cdaf7a",
            "value": "401"
          },
          "TxnTaxDetail": {
            "TotalTax": 0
          },
          "AllowOnlineCreditCardPayment": false,
          "SyncToken": "0",
          "LinkedTxn": [],
          "RecurringInfo": {
            "Active": true,
            "RecurType": "Automated",
            "ScheduleInfo": {
              "NumInterval": 1,
              "NextDate": "2020-08-01",
              "DayOfMonth": 1,
              "IntervalType": "Monthly"
            },
            "Name": "Testing"
          },
          "EmailStatus": "NotSet",
          "sparse": false,
          "MetaData": {
            "CreateTime": "2020-07-06T14:24:00-07:00",
            "LastUpdatedTime": "2020-07-06T14:24:00-07:00"
          },
          "CustomField": [
            {
              "DefinitionId": "1",
              "Type": "StringType",
              "Name": "Crew #"
            },
            {
              "DefinitionId": "2",
              "Type": "StringType",
              "Name": "PO #"
            },
            {
              "DefinitionId": "3",
              "Type": "StringType",
              "Name": "Sales #"
            }
          ],
          "Id": "1537",
          "AllowOnlinePayment": false,
          "AllowIPNPayment": false
        }
      },
      {
        "Bill": {
          "SyncToken": "0",
          "domain": "QBO",
          "RecurringInfo": {
            "Active": true,
            "RecurType": "Automated",
            "ScheduleInfo": {
              "NumInterval": 1,
              "NextDate": "2020-08-01",
              "DayOfMonth": 1,
              "PreviousDate": "2020-07-01",
              "IntervalType": "Monthly"
            },
            "Name": "Telephone Bill"
          },
          "RecurDataRef": {
            "value": "2"
          },
          "CurrencyRef": {
            "name": "United States Dollar",
            "value": "USD"
          },
          "TotalAmt": 74.36,
          "APAccountRef": {
            "name": "Name_01ff6",
            "value": "33"
          },
          "Id": "20",
          "sparse": false,
          "VendorRef": {
            "name": "Cal Telephone",
            "value": "32"
          },
          "Line": [
            {
              "Description": "Monthly Phone Bill",
              "DetailType": "AccountBasedExpenseLineDetail",
              "LineNum": 1,
              "Amount": 74.36,
              "Id": "1",
              "AccountBasedExpenseLineDetail": {
                "TaxCodeRef": {
                  "value": "NON"
                },
                "AccountRef": {
                  "name": "Utilities:Telephone",
                  "value": "77"
                },
                "BillableStatus": "NotBillable"
              }
            }
          ],
          "Balance": 74.36,
          "SalesTermRef": {
            "value": "3"
          },
          "MetaData": {
            "CreateTime": "2019-02-17T15:27:25-08:00",
            "LastUpdatedTime": "2020-07-05T01:19:13-07:00"
          }
        }
      },
      {
        "Bill": {
          "SyncToken": "0",
          "domain": "QBO",
          "RecurringInfo": {
            "Active": true,
            "RecurType": "Automated",
            "ScheduleInfo": {
              "NumInterval": 1,
              "NextDate": "2020-08-01",
              "DayOfMonth": 1,
              "PreviousDate": "2020-07-01",
              "IntervalType": "Monthly"
            },
            "Name": "Monthly Building Lease"
          },
          "RecurDataRef": {
            "value": "3"
          },
          "CurrencyRef": {
            "name": "United States Dollar",
            "value": "USD"
          },
          "TotalAmt": 900.0,
          "APAccountRef": {
            "name": "Name_01ff6",
            "value": "33"
          },
          "Id": "23",
          "sparse": false,
          "VendorRef": {
            "name": "Hall Properties",
            "value": "40"
          },
          "Line": [
            {
              "Description": "Building Lease",
              "DetailType": "AccountBasedExpenseLineDetail",
              "LineNum": 1,
              "Amount": 900.0,
              "Id": "1",
              "AccountBasedExpenseLineDetail": {
                "TaxCodeRef": {
                  "value": "NON"
                },
                "AccountRef": {
                  "name": "Rent or Lease",
                  "value": "17"
                },
                "BillableStatus": "NotBillable"
              }
            }
          ],
          "Balance": 900.0,
          "SalesTermRef": {
            "value": "3"
          },
          "MetaData": {
            "CreateTime": "2019-02-17T15:31:18-08:00",
            "LastUpdatedTime": "2020-07-05T01:19:12-07:00"
          }
        }
      }
    ]
  },
  "time": "2020-07-06T17:33:54.221-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-07-06T17:39:46.777-07:00">
    <QueryResponse startPosition="1" maxResults="3">
        <RecurringTransaction>
            <Invoice domain="QBO" sparse="false">
                <Id>1537</Id>
                <SyncToken>0</SyncToken>
                <MetaData>
                    <CreateTime>2020-07-06T14:24:00-07:00</CreateTime>
                    <LastUpdatedTime>2020-07-06T14:24:00-07:00</LastUpdatedTime>
                </MetaData>
                <CustomField>
                    <DefinitionId>1</DefinitionId>
                    <Name>Crew #</Name>
                    <Type>StringType</Type>
                </CustomField>
                <CustomField>
                    <DefinitionId>2</DefinitionId>
                    <Name>PO #</Name>
                    <Type>StringType</Type>
                </CustomField>
                <CustomField>
                    <DefinitionId>3</DefinitionId>
                    <Name>Sales #</Name>
                    <Type>StringType</Type>
                </CustomField>
                <CurrencyRef name="United States Dollar">USD</CurrencyRef>
                <Line>
                    <Id>1</Id>
                    <LineNum>1</LineNum>
                    <Amount>11111.00</Amount>
                    <DetailType>SalesItemLineDetail</DetailType>
                    <SalesItemLineDetail>
                        <ItemRef name="Garden Supplies3223">211</ItemRef>
                        <TaxCodeRef>NON</TaxCodeRef>
                    </SalesItemLineDetail>
                </Line>
                <Line>
                    <Amount>11111.00</Amount>
                    <DetailType>SubTotalLineDetail</DetailType>
                    <SubTotalLineDetail/>
                </Line>
                <TxnTaxDetail>
                    <TotalTax>0</TotalTax>
                </TxnTaxDetail>
                <RecurDataRef>4</RecurDataRef>
                <RecurringInfo>
                    <Name>Testing</Name>
                    <RecurType>Automated</RecurType>
                    <Active>true</Active>
                    <ScheduleInfo>
                        <IntervalType>Monthly</IntervalType>
                        <NumInterval>1</NumInterval>
                        <DayOfMonth>1</DayOfMonth>
                        <NextDate>2020-08-01</NextDate>
                    </ScheduleInfo>
                </RecurringInfo>
                <CustomerRef name="0c9ff29a3c3640cdaf7a">401</CustomerRef>
                <TotalAmt>11111.00</TotalAmt>
                <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
                <PrintStatus>NeedToPrint</PrintStatus>
                <EmailStatus>NotSet</EmailStatus>
                <Balance>11111.00</Balance>
                <AllowIPNPayment>false</AllowIPNPayment>
                <AllowOnlinePayment>false</AllowOnlinePayment>
                <AllowOnlineCreditCardPayment>false</AllowOnlineCreditCardPayment>
                <AllowOnlineACHPayment>false</AllowOnlineACHPayment>
            </Invoice>
        </RecurringTransaction>
        <RecurringTransaction>
            <Bill domain="QBO" sparse="false">
                <Id>20</Id>
                <SyncToken>0</SyncToken>
                <MetaData>
                    <CreateTime>2019-02-17T15:27:25-08:00</CreateTime>
                    <LastUpdatedTime>2020-07-05T01:19:13-07:00</LastUpdatedTime>
                </MetaData>
                <CurrencyRef name="United States Dollar">USD</CurrencyRef>
                <Line>
                    <Id>1</Id>
                    <LineNum>1</LineNum>
                    <Description>Monthly Phone Bill</Description>
                    <Amount>74.36</Amount>
                    <DetailType>AccountBasedExpenseLineDetail</DetailType>
                    <AccountBasedExpenseLineDetail>
                        <AccountRef name="Utilities:Telephone">77</AccountRef>
                        <BillableStatus>NotBillable</BillableStatus>
                        <TaxCodeRef>NON</TaxCodeRef>
                    </AccountBasedExpenseLineDetail>
                </Line>
                <RecurDataRef>2</RecurDataRef>
                <RecurringInfo>
                    <Name>Telephone Bill</Name>
                    <RecurType>Automated</RecurType>
                    <Active>true</Active>
                    <ScheduleInfo>
                        <IntervalType>Monthly</IntervalType>
                        <NumInterval>1</NumInterval>
                        <DayOfMonth>1</DayOfMonth>
                        <NextDate>2020-08-01</NextDate>
                        <PreviousDate>2020-07-01</PreviousDate>
                    </ScheduleInfo>
                </RecurringInfo>
                <VendorRef name="Cal Telephone">32</VendorRef>
                <APAccountRef name="Name_01ff6">33</APAccountRef>
                <TotalAmt>74.36</TotalAmt>
                <SalesTermRef>3</SalesTermRef>
                <Balance>74.36</Balance>
            </Bill>
        </RecurringTransaction>
        <RecurringTransaction>
            <Bill domain="QBO" sparse="false">
                <Id>23</Id>
                <SyncToken>0</SyncToken>
                <MetaData>
                    <CreateTime>2019-02-17T15:31:18-08:00</CreateTime>
                    <LastUpdatedTime>2020-07-05T01:19:12-07:00</LastUpdatedTime>
                </MetaData>
                <CurrencyRef name="United States Dollar">USD</CurrencyRef>
                <Line>
                    <Id>1</Id>
                    <LineNum>1</LineNum>
                    <Description>Building Lease</Description>
                    <Amount>900.00</Amount>
                    <DetailType>AccountBasedExpenseLineDetail</DetailType>
                    <AccountBasedExpenseLineDetail>
                        <AccountRef name="Rent or Lease">17</AccountRef>
                        <BillableStatus>NotBillable</BillableStatus>
                        <TaxCodeRef>NON</TaxCodeRef>
                    </AccountBasedExpenseLineDetail>
                </Line>
                <RecurDataRef>3</RecurDataRef>
                <RecurringInfo>
                    <Name>Monthly Building Lease</Name>
                    <RecurType>Automated</RecurType>
                    <Active>true</Active>
                    <ScheduleInfo>
                        <IntervalType>Monthly</IntervalType>
                        <NumInterval>1</NumInterval>
                        <DayOfMonth>1</DayOfMonth>
                        <NextDate>2020-08-01</NextDate>
                        <PreviousDate>2020-07-01</PreviousDate>
                    </ScheduleInfo>
                </RecurringInfo>
                <VendorRef name="Hall Properties">40</VendorRef>
                <APAccountRef name="Name_01ff6">33</APAccountRef>
                <TotalAmt>900.00</TotalAmt>
                <SalesTermRef>3</SalesTermRef>
                <Balance>900.00</Balance>
            </Bill>
        </RecurringTransaction>
    </QueryResponse>
</IntuitResponse>
```

## Read a recurring transaction

### Definition

- **Operation:** `GET /v3/company/<realmID>/recurringtransaction/<recurringtransactionId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a RecurringTransaction object.

### Returns

Returns the RecurringTransaction object.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "maxResults": 1,
    "RecurringTransaction": [
      {
        "Bill": {
          "SyncToken": "0",
          "domain": "QBO",
          "RecurringInfo": {
            "Active": true,
            "RecurType": "Automated",
            "ScheduleInfo": {
              "NumInterval": 1,
              "NextDate": "2020-08-01",
              "DayOfMonth": 1,
              "PreviousDate": "2020-07-01",
              "IntervalType": "Monthly"
            },
            "Name": "Telephone Bill"
          },
          "RecurDataRef": {
            "value": "2"
          },
          "CurrencyRef": {
            "name": "United States Dollar",
            "value": "USD"
          },
          "TotalAmt": 74.36,
          "APAccountRef": {
            "name": "Name_01ff6",
            "value": "33"
          },
          "Id": "20",
          "sparse": false,
          "VendorRef": {
            "name": "Cal Telephone",
            "value": "32"
          },
          "Line": [
            {
              "Description": "Monthly Phone Bill",
              "DetailType": "AccountBasedExpenseLineDetail",
              "LineNum": 1,
              "Amount": 74.36,
              "Id": "1",
              "AccountBasedExpenseLineDetail": {
                "TaxCodeRef": {
                  "value": "NON"
                },
                "AccountRef": {
                  "name": "Utilities:Telephone",
                  "value": "77"
                },
                "BillableStatus": "NotBillable"
              }
            }
          ],
          "Balance": 74.36,
          "SalesTermRef": {
            "value": "3"
          },
          "MetaData": {
            "CreateTime": "2019-02-17T15:27:25-08:00",
            "LastUpdatedTime": "2020-07-05T01:19:13-07:00"
          }
        }
      }
    ]
  },
  "time": "2020-07-09T10:18:02.049-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-07-09T10:17:26.684-07:00">
    <QueryResponse startPosition="1" maxResults="1">
        <RecurringTransaction>
            <Bill domain="QBO" sparse="false">
                <Id>20</Id>
                <SyncToken>0</SyncToken>
                <MetaData>
                    <CreateTime>2019-02-17T15:27:25-08:00</CreateTime>
                    <LastUpdatedTime>2020-07-05T01:19:13-07:00</LastUpdatedTime>
                </MetaData>
                <CurrencyRef name="United States Dollar">USD</CurrencyRef>
                <Line>
                    <Id>1</Id>
                    <LineNum>1</LineNum>
                    <Description>Monthly Phone Bill</Description>
                    <Amount>74.36</Amount>
                    <DetailType>AccountBasedExpenseLineDetail</DetailType>
                    <AccountBasedExpenseLineDetail>
                        <AccountRef name="Utilities:Telephone">77</AccountRef>
                        <BillableStatus>NotBillable</BillableStatus>
                        <TaxCodeRef>NON</TaxCodeRef>
                    </AccountBasedExpenseLineDetail>
                </Line>
                <RecurDataRef>2</RecurDataRef>
                <RecurringInfo>
                    <Name>Telephone Bill</Name>
                    <RecurType>Automated</RecurType>
                    <Active>true</Active>
                    <ScheduleInfo>
                        <IntervalType>Monthly</IntervalType>
                        <NumInterval>1</NumInterval>
                        <DayOfMonth>1</DayOfMonth>
                        <NextDate>2020-08-01</NextDate>
                        <PreviousDate>2020-07-01</PreviousDate>
                    </ScheduleInfo>
                </RecurringInfo>
                <VendorRef name="Cal Telephone">32</VendorRef>
                <APAccountRef name="Name_01ff6">33</APAccountRef>
                <TotalAmt>74.36</TotalAmt>
                <SalesTermRef>3</SalesTermRef>
                <Balance>74.36</Balance>
            </Bill>
        </RecurringTransaction>
    </QueryResponse>
</IntuitResponse>
```
