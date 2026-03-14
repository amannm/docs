# ReimburseCharge

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/reimbursecharge
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / ReimburseCharge
> Canonical entity: `ReimburseCharge`

A Reimburse Charge is a billable Expense. This happens when you mark your Expense/Bill lines as Billable to some customer to be invoiced later.

## The ReimburseCharge object

### reimbursechargeresponse

Model type: `object`

#### `Id`

Required: Optional
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

#### `Line [0..n]`

Required: Required
Type: `Line`

<details>
<summary>Child attributes for `Line [0..n]`</summary>

##### reimbursechargeline

Model type: `object`

###### `ReimburseLineDetail`

Required: Required
Type: `ReimburseLineDetail`

Reimburse charge details for the line.

<details>
<summary>Child attributes for `ReimburseLineDetail`</summary>

###### discountlinedetail

Model type: `object`

###### `ClassRef`

Required: Optional
Type: `ReferenceType`

Reference to the Class associated with this discount. Query the Class name list resource to determine the appropriate Class object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

<details>
<summary>Child attributes for `ClassRef`</summary>

###### referencetype

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

###### `TaxCodeRef`

Required: Optional
Type: `ReferenceType`

The `TaxCode`associated with the sales tax for the expense. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `TaxCodeRef.value` and `TaxCodeRef.name`, respectively.

<details>
<summary>Child attributes for `TaxCodeRef`</summary>

###### referencetype

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

###### `DiscountAccountRef`

Required: Optional
Type: `ReferenceType`

Income account used to track discounts. Query the Account name list resource to determine the appropriate Account object for this reference, where `Account.AccountType=Income` and `Account.AccountSubType=DiscountsRefundsGiven`. Use `Account.Id` and `Account.Name` from that object for `DiscountAccountRef.value` and `DiscountAccountRef.name`, respectively.

<details>
<summary>Child attributes for `DiscountAccountRef`</summary>

###### referencetype

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

###### `PercentBased`

Required: Optional
Type: `Boolean`

True if the discount is a percentage; null or false if discount based on amount.

###### `DiscountPercent`

Required: Optional
Type: `Decimal`

Percentage by which the amount due is reduced, from 0% to 100%. To enter a discount of 8.5% use 8.5, not 0.085.

</details>

###### `DetailType`

Required: Required
Type: `LineDetailTypeEnum`

Set this to ReimburseLineDetail.

###### `LinkedTxn [0..n]`

Required: Optional
Type: `LinkedTxn`

List of LinkedTxn objects. This will contain the Invoice linked transaction if the ReimburseCharge has been linked to an Invoice.

<details>
<summary>Child attributes for `LinkedTxn [0..n]`</summary>

###### linkedtxn

Model type: `object`

###### `TxnId`

Required: Required
Type: `String`

Transaction Id of the related transaction.

###### `TxnType`

Required: Required
Type: `String`

Transaction type of the linked object.

###### `TxnLineId`

Required: Conditionally required
Type: `String`

Required for Deposit and Bill entities. The line number of a specific line of the linked transaction. If supplied, the `TxnId` and `TxnType` attributes of the linked transaction must also be populated.

</details>

###### `LineNum`

Required: Optional
Type: `Decimal`

Specifies the position of the line in the collection of transaction lines. Positive integer.

###### `LineId`

Required: Optional
Type: `String`

The line Id for the line. This will be used to link it to the invoice.

</details>

#### `Amount`

Required: Required
Type: `Decimal`
Max length: Max 15 digits in 10.5 format

The amount of the line item.

#### `CustomerRef`

Required: Required
Type: `ReferenceType`
Traits: filterable

Reference to a customer or job. Query the Customer name list resource to determine the appropriate Customer object for this reference. Use `Customer.Id` and `Customer.DisplayName` from that object for `CustomerRef.value` and `CustomerRef.name`, respectively.

<details>
<summary>Child attributes for `CustomerRef`</summary>

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

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `CurrencyRef`

Required: Conditionally required
Type: `CurrencyRefType`

Reference to the currency in which all amounts on the associated transaction are expressed. This must be defined if multicurrency is enabled for the company. Multicurrency is enabled for the company if `Preferences.MultiCurrencyEnabled` is set to `true`. Read more about multicurrency support [here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/manage-multiple-currencies). Applicable if multicurrency is enabled for the company.

<details>
<summary>Child attributes for `CurrencyRef`</summary>

##### currencyref

Model type: `object`

###### `value`

Required: Required
Type: `String`

A three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on.

###### `name`

Required: Optional
Type: `String`

The full name of the currency.

</details>

#### `HasBeenInvoiced`

Type: `Boolean`
Traits: filterable
Default: false

Boolean indicating whether the reimbursable charge has been linked to an Invoice.

#### `HomeTotalAmt`

Type: `Decimal`
Traits: read only, system defined

Total amount of the transaction in the home currency. Includes the total of all the charges, allowances and taxes. Calculated by QuickBooks business logic. Value is valid only when `CurrencyRef` is specified. Applicable if multicurrency is enabled for the company.

#### `PrivateNote`

Required: Optional
Type: `String`
Max length: max of 4000 chars

User entered, organization-private note about the transaction. This note does not appear on the invoice to the customer. This field maps to the Statement Memo field on the Invoice form in the QuickBooks Online UI.

#### `LinkedTxn [0..n]`

Required: Optional
Type: `LinkedTxn`

The LinkedTxn will contain the Invoice Id if the ReimburseCharge has been linked with an Invoice.

<details>
<summary>Child attributes for `LinkedTxn [0..n]`</summary>

##### linkedtxn

Model type: `object`

###### `TxnId`

Required: Required
Type: `String`

Transaction Id of the related transaction.

###### `TxnType`

Required: Required
Type: `String`

Transaction type of the linked object.

###### `TxnLineId`

Required: Conditionally required
Type: `String`

Required for Deposit and Bill entities. The line number of a specific line of the linked transaction. If supplied, the `TxnId` and `TxnType` attributes of the linked transaction must also be populated.

</details>

#### `ExchangeRate`

Required: Optional
Type: `Decimal`
Default: 1

The number of home currency units it takes to equal one unit of currency specified by `CurrencyRef`. Applicable if multicurrency is enabled for the company.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`

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
  "ReimburseCharge": {
    "SyncToken": "0",
    "domain": "QBO",
    "HasBeenInvoiced": true,
    "TxnDate": "2020-06-23",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "LinkedTxn": [
      {
        "TxnId": "495",
        "TxnType": "Invoice"
      }
    ],
    "Amount": 100.0,
    "sparse": false,
    "Line": [
      {
        "LinkedTxn": [
          {
            "TxnId": "495",
            "TxnType": "Invoice"
          }
        ],
        "DetailType": "ReimburseLineDetail",
        "ReimburseLineDetail": {
          "ItemRef": {
            "name": "Sales",
            "value": "3"
          },
          "Qty": 1,
          "TaxCodeRef": {
            "value": "NON"
          },
          "MarkupInfo": {
            "Percent": 900
          },
          "ItemAccountRef": {
            "name": "Billable Expense Income",
            "value": "37"
          },
          "UnitPrice": 10
        },
        "LineNum": 1,
        "Amount": 10.0,
        "Id": "1"
      },
      {
        "LinkedTxn": [
          {
            "TxnId": "495",
            "TxnType": "Invoice"
          }
        ],
        "Description": "900% markup",
        "DetailType": "ReimburseLineDetail",
        "ReimburseLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "MarkupInfo": {
            "Percent": 900
          },
          "ItemAccountRef": {
            "name": "Markup",
            "value": "49"
          }
        },
        "LineNum": 2,
        "Amount": 90.0,
        "Id": "2"
      }
    ],
    "CustomerRef": {
      "name": "Cust1",
      "value": "1"
    },
    "Id": "491",
    "MetaData": {
      "CreateTime": "2020-06-23T23:26:13-07:00",
      "LastUpdatedTime": "2020-06-23T23:28:54-07:00"
    }
  },
  "time": "2020-11-07T13:29:41.836-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-11-13T08:14:09.550-07:00">
    <ReimburseCarge domain="QBO" sparse="false">
        <CustomerRef>
            <value>1</value>
            <name>Cust1</name>
        </CustomerRef>
        <HasBeenInvoiced>true</HasBeenInvoiced>
        <Amount>100</Amount>
        <domain>QBO</domain>
        <sparse>false</sparse>
        <Id>491</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2020-06-23T23:26:13-07:00</CreateTime>
            <LastUpdatedTime>2020-06-23T23:28:54-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2020-06-23</TxnDate>
        <CurrencyRef>
            <value>USD</value>
            <name>United States Dollar</name>
        </CurrencyRef>
        <LinkedTxn>
            <TxnId>495</TxnId>
            <TxnType>Invoice</TxnType>
        </LinkedTxn>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Amount>10</Amount>
            <LinkedTxn>
                <TxnId>495</TxnId>
                <TxnType>Invoice</TxnType>
            </LinkedTxn>
            <DetailType>ReimburseLineDetail</DetailType>
            <ReimburseLineDetail>
                <ItemRef>
                    <value>3</value>
                    <name>Sales</name>
                </ItemRef>
                <UnitPrice>10</UnitPrice>
                <MarkupInfo>
                    <Percent>900</Percent>
                </MarkupInfo>
                <Qty>1</Qty>
                <ItemAccountRef>
                    <value>37</value>
                    <name>Billable Expense Income</name>
                </ItemAccountRef>
                <TaxCodeRef>
                    <value>NON</value>
                </TaxCodeRef>
            </ReimburseLineDetail>
        </Line>
        <Line>
            <Id>2</Id>
            <LineNum>2</LineNum>
            <Description>900% markup</Description>
            <Amount>90</Amount>
            <LinkedTxn>
                <TxnId>495</TxnId>
                <TxnType>Invoice</TxnType>
            </LinkedTxn>
            <DetailType>ReimburseLineDetail</DetailType>
            <ReimburseLineDetail>
                <MarkupInfo>
                    <Percent>900</Percent>
                </MarkupInfo>
                <ItemAccountRef>
                    <value>49</value>
                    <name>Markup</name>
                </ItemAccountRef>
                <TaxCodeRef>
                    <value>NON</value>
                </TaxCodeRef>
            </ReimburseLineDetail>
        </Line>
    </ReimburseCarge>
</IntuitResponse>
```

## Query a reimburse charge

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"Select * from ReimburseCharge Where HasBeenInvoiced = false"
```

#### XML example

```sql
Select * from ReimburseCharge Where HasBeenInvoiced = false
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "ReimburseCarge": [
      {
        "SyncToken": "0",
        "domain": "QBO",
        "HasBeenInvoiced": true,
        "TxnDate": "2020-06-23",
        "CurrencyRef": {
          "name": "United States Dollar",
          "value": "USD"
        },
        "LinkedTxn": [
          {
            "TxnId": "495",
            "TxnType": "Invoice"
          }
        ],
        "Amount": 100.0,
        "sparse": false,
        "Line": [
          {
            "LinkedTxn": [
              {
                "TxnId": "495",
                "TxnType": "Invoice"
              }
            ],
            "DetailType": "ReimburseLineDetail",
            "ReimburseLineDetail": {
              "ItemRef": {
                "name": "Sales",
                "value": "3"
              },
              "Qty": 1,
              "TaxCodeRef": {
                "value": "NON"
              },
              "MarkupInfo": {
                "Percent": 900
              },
              "ItemAccountRef": {
                "name": "Billable Expense Income",
                "value": "37"
              },
              "UnitPrice": 10
            },
            "LineNum": 1,
            "Amount": 10.0,
            "Id": "1"
          },
          {
            "LinkedTxn": [
              {
                "TxnId": "495",
                "TxnType": "Invoice"
              }
            ],
            "Description": "900% markup",
            "DetailType": "ReimburseLineDetail",
            "ReimburseLineDetail": {
              "TaxCodeRef": {
                "value": "NON"
              },
              "MarkupInfo": {
                "Percent": 900
              },
              "ItemAccountRef": {
                "name": "Markup",
                "value": "49"
              }
            },
            "LineNum": 2,
            "Amount": 90.0,
            "Id": "2"
          }
        ],
        "CustomerRef": {
          "name": "Cust1",
          "value": "1"
        },
        "Id": "491",
        "MetaData": {
          "CreateTime": "2020-06-23T23:26:13-07:00",
          "LastUpdatedTime": "2020-06-23T23:28:54-07:00"
        }
      }
    ],
    "startPosition": 1,
    "maxResults": 1,
    "totalCount": 1
  },
  "time": "2020-11-07T13:32:06.76-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-11-13T08:14:09.550-07:00">
    <QueryResponse startPosition="1" maxResults="1" totalCount="1">
        <ReimburseCarge domain="QBO" sparse="false">
            <CustomerRef>
                <value>1</value>
                <name>Cust1</name>
            </CustomerRef>
            <HasBeenInvoiced>true</HasBeenInvoiced>
            <Amount>100</Amount>
            <domain>QBO</domain>
            <sparse>false</sparse>
            <Id>491</Id>
            <SyncToken>0</SyncToken>
            <MetaData>
                <CreateTime>2020-06-23T23:26:13-07:00</CreateTime>
                <LastUpdatedTime>2020-06-23T23:28:54-07:00</LastUpdatedTime>
            </MetaData>
            <TxnDate>2020-06-23</TxnDate>
            <CurrencyRef>
                <value>USD</value>
                <name>United States Dollar</name>
            </CurrencyRef>
            <LinkedTxn>
                <TxnId>495</TxnId>
                <TxnType>Invoice</TxnType>
            </LinkedTxn>
            <Line>
                <Id>1</Id>
                <LineNum>1</LineNum>
                <Amount>10</Amount>
                <LinkedTxn>
                    <TxnId>495</TxnId>
                    <TxnType>Invoice</TxnType>
                </LinkedTxn>
                <DetailType>ReimburseLineDetail</DetailType>
                <ReimburseLineDetail>
                    <ItemRef>
                        <value>3</value>
                        <name>Sales</name>
                    </ItemRef>
                    <UnitPrice>10</UnitPrice>
                    <MarkupInfo>
                        <Percent>900</Percent>
                    </MarkupInfo>
                    <Qty>1</Qty>
                    <ItemAccountRef>
                        <value>37</value>
                        <name>Billable Expense Income</name>
                    </ItemAccountRef>
                    <TaxCodeRef>
                        <value>NON</value>
                    </TaxCodeRef>
                </ReimburseLineDetail>
            </Line>
            <Line>
                <Id>2</Id>
                <LineNum>2</LineNum>
                <Description>900% markup</Description>
                <Amount>90</Amount>
                <LinkedTxn>
                    <TxnId>495</TxnId>
                    <TxnType>Invoice</TxnType>
                </LinkedTxn>
                <DetailType>ReimburseLineDetail</DetailType>
                <ReimburseLineDetail>
                    <MarkupInfo>
                        <Percent>900</Percent>
                    </MarkupInfo>
                    <ItemAccountRef>
                        <value>49</value>
                        <name>Markup</name>
                    </ItemAccountRef>
                    <TaxCodeRef>
                        <value>NON</value>
                    </TaxCodeRef>
                </ReimburseLineDetail>
            </Line>
        </ReimburseCarge>
    </QueryResponse>
</IntuitResponse>
```

## Read a reimburse charge

### Definition

- **Operation:** `GET /v3/company/<realmID>/reimbursecharge/<taxrateId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a ReimburseCharge object.

### Returns

Returns the reimbursecharge object.

#### Example

```json
{
  "ReimburseCharge": {
    "SyncToken": "0",
    "domain": "QBO",
    "HasBeenInvoiced": true,
    "TxnDate": "2020-06-23",
    "CurrencyRef": {
      "name": "United States Dollar",
      "value": "USD"
    },
    "LinkedTxn": [
      {
        "TxnId": "495",
        "TxnType": "Invoice"
      }
    ],
    "Amount": 100.0,
    "sparse": false,
    "Line": [
      {
        "LinkedTxn": [
          {
            "TxnId": "495",
            "TxnType": "Invoice"
          }
        ],
        "DetailType": "ReimburseLineDetail",
        "ReimburseLineDetail": {
          "ItemRef": {
            "name": "Sales",
            "value": "3"
          },
          "Qty": 1,
          "TaxCodeRef": {
            "value": "NON"
          },
          "MarkupInfo": {
            "Percent": 900
          },
          "ItemAccountRef": {
            "name": "Billable Expense Income",
            "value": "37"
          },
          "UnitPrice": 10
        },
        "LineNum": 1,
        "Amount": 10.0,
        "Id": "1"
      },
      {
        "LinkedTxn": [
          {
            "TxnId": "495",
            "TxnType": "Invoice"
          }
        ],
        "Description": "900% markup",
        "DetailType": "ReimburseLineDetail",
        "ReimburseLineDetail": {
          "TaxCodeRef": {
            "value": "NON"
          },
          "MarkupInfo": {
            "Percent": 900
          },
          "ItemAccountRef": {
            "name": "Markup",
            "value": "49"
          }
        },
        "LineNum": 2,
        "Amount": 90.0,
        "Id": "2"
      }
    ],
    "CustomerRef": {
      "name": "Cust1",
      "value": "1"
    },
    "Id": "491",
    "MetaData": {
      "CreateTime": "2020-06-23T23:26:13-07:00",
      "LastUpdatedTime": "2020-06-23T23:28:54-07:00"
    }
  },
  "time": "2020-11-07T13:29:41.836-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2020-11-13T08:14:09.550-07:00">
    <ReimburseCarge domain="QBO" sparse="false">
        <CustomerRef>
            <value>1</value>
            <name>Cust1</name>
        </CustomerRef>
        <HasBeenInvoiced>true</HasBeenInvoiced>
        <Amount>100</Amount>
        <domain>QBO</domain>
        <sparse>false</sparse>
        <Id>491</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
            <CreateTime>2020-06-23T23:26:13-07:00</CreateTime>
            <LastUpdatedTime>2020-06-23T23:28:54-07:00</LastUpdatedTime>
        </MetaData>
        <TxnDate>2020-06-23</TxnDate>
        <CurrencyRef>
            <value>USD</value>
            <name>United States Dollar</name>
        </CurrencyRef>
        <LinkedTxn>
            <TxnId>495</TxnId>
            <TxnType>Invoice</TxnType>
        </LinkedTxn>
        <Line>
            <Id>1</Id>
            <LineNum>1</LineNum>
            <Amount>10</Amount>
            <LinkedTxn>
                <TxnId>495</TxnId>
                <TxnType>Invoice</TxnType>
            </LinkedTxn>
            <DetailType>ReimburseLineDetail</DetailType>
            <ReimburseLineDetail>
                <ItemRef>
                    <value>3</value>
                    <name>Sales</name>
                </ItemRef>
                <UnitPrice>10</UnitPrice>
                <MarkupInfo>
                    <Percent>900</Percent>
                </MarkupInfo>
                <Qty>1</Qty>
                <ItemAccountRef>
                    <value>37</value>
                    <name>Billable Expense Income</name>
                </ItemAccountRef>
                <TaxCodeRef>
                    <value>NON</value>
                </TaxCodeRef>
            </ReimburseLineDetail>
        </Line>
        <Line>
            <Id>2</Id>
            <LineNum>2</LineNum>
            <Description>900% markup</Description>
            <Amount>90</Amount>
            <LinkedTxn>
                <TxnId>495</TxnId>
                <TxnType>Invoice</TxnType>
            </LinkedTxn>
            <DetailType>ReimburseLineDetail</DetailType>
            <ReimburseLineDetail>
                <MarkupInfo>
                    <Percent>900</Percent>
                </MarkupInfo>
                <ItemAccountRef>
                    <value>49</value>
                    <name>Markup</name>
                </ItemAccountRef>
                <TaxCodeRef>
                    <value>NON</value>
                </TaxCodeRef>
            </ReimburseLineDetail>
        </Line>
    </ReimburseCarge>
</IntuitResponse>
```
