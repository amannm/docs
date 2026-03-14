# Batch

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/batch
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Batch
> Canonical entity: `Batch`

The batch operation enables an application to perform multiple operations in a single request. For example, in a single batch request an application can create a customer, update an invoice, and read an account. Compared to multiple requests, a single batch request can improve an application's performance by decreasing network roundtrips and increasing throughput. The individual operations within a batch request are called `BatchItemRequest` objects.

### Business Rules

- The maximum number of payloads in a single `BatchItemRequest` is 30.
- The maximum number requests to the batch endpoint per minute per realmID is 40.
- Execution order of `BatchItemRequest` objects should not be assumed.
- `BatchItemRequest` objects are treated independently; a given object cannot depend on another one within the same batch operation. For example, a newly created customer is not available for a subsequent invoice create operation within the same batch operation. You would need to create the customer object first, either atomonously or via a batch request, and then create the invoice object in a subsequent batch request.
- A batch request is authenticated once. This single authentication applies to all `BatchItemRequest` objects in the request.
- The maximum number of objects that can be returned in a response is 1000.

## Sample batch request

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/batch`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The request on the right includes four `BatchItemRequest` objects.

Schema: `batchrequest`

<details>
<summary>Show schema for `batchrequest`</summary>

#### batchrequest

Model type: `object`

##### `BatchItemRequest`

Required: Required
Type: `batchitemrequest`

A wrapper around all request objects for this batch operation.

<details>
<summary>Child attributes for `BatchItemRequest`</summary>

###### batchitemrequest

Model type: `object`

###### `bId`

Required: Required
Type: `String`

Unique identifier for the batch item.

###### `optionsData`

Required: Conditionally required
Type: `String`

Use for the void operation for those resources that support it. Must be supplied with `operation` set to `update`. Valid value: `void`. Required for void operations.

###### `operation`

Required: Conditionally required
Type: `String`

The operation to perform with the supplied request object payload. Do not use if this `batchitemrequest` object is for a query operation. Valid values include: `create`, `update`, `delete` Required for create, update, and delete.

###### `Query`

Required: Optional
Type: `string`

The `SELECT` statement for the query. When `Query` is defined, do not define the `operation` attribute.

###### `resourceName`

Required: Optional
Type: `Request object`

The payload for the request for create, update, and delete operations.

</details>

</details>

#### Example

```json
{
  "BatchItemRequest": [
    {
      "bId": "bid1",
      "Vendor": {
        "DisplayName": "Smith Family Store"
      },
      "operation": "create"
    },
    {
      "bId": "bid2",
      "operation": "delete",
      "Invoice": {
        "SyncToken": "0",
        "Id": "129"
      }
    },
    {
      "SalesReceipt": {
        "PrivateNote": "A private note.",
        "SyncToken": "0",
        "domain": "QBO",
        "Id": "11",
        "sparse": true
      },
      "bId": "bid3",
      "operation": "update"
    },
    {
      "Query": "select * from SalesReceipt where TotalAmt > '300.00'",
      "bId": "bid4"
    }
  ]
}
```

#### XML example

```xml
<IntuitBatchRequest xmlns="http://schema.intuit.com/finance/v3">
    <BatchItemRequest bId="bid1" operation="create">
        <Vendor>
            <DisplayName>Smith Family Grocery</DisplayName>
        </Vendor>
    </BatchItemRequest>
    <BatchItemRequest bId="bid2" operation="delete">
        <Invoice>
            <Id>119</Id>
            <SyncToken>0</SyncToken>
        </Invoice>
    </BatchItemRequest>
    <BatchItemRequest bId="bid3" operation="update">
        <SalesReceipt xmlns="http://schema.intuit.com/finance/v3" sparse="true">
            <Id>38</Id>
            <SyncToken>0</SyncToken>
            <PrivateNote>This is another private note.</PrivateNote>
        </SalesReceipt>
    </BatchItemRequest>
        <BatchItemRequest bId="bid4">
        <Query>select * from SalesReceipt where TotalAmt > '200.00'</Query>
   </BatchItemRequest>
</IntuitBatchRequest>
```

### Returns

Some content has been omitted in order to showcase the overall `BatchItemRequest` object structure.

Schema: `batchresponse`

<details>
<summary>Show schema for `batchresponse`</summary>

#### batchresponse

Model type: `object`

##### `BatchItemResponse`

Required: Required
Type: `batchitemresponse`

A wrapper around all response objects for this batch operation.

<details>
<summary>Child attributes for `BatchItemResponse`</summary>

###### batchitemresponse

Model type: `object`

###### `bId`

Required: Required
Type: `String`

Unique identifier for the batch item. This corresponds to the id supplied in the corresponding batch item request.

###### `ResourceName`

Type: `Response object`

The payload for the response. If the operation results in an error, a `Fault` object is returned.

###### `QueryResponse`

Type: `array of response objects`

The payload for the query response. Returned only if a query operation is specified in the batch request. If the operation results in an error, a `Fault` object is returned.

</details>

</details>

#### Example

```json
{
  "BatchItemResponse": [
    {
      "Fault": {
        "type": "ValidationFault",
        "Error": [
          {
            "Message": "Duplicate Name Exists Error",
            "code": "6240",
            "Detail": "The name supplied already exists. : Another customer, vendor or employee is already using this \nname. Please use a different name.",
            "element": ""
          }
        ]
      },
      "bId": "bid1"
    },
    {
      "Fault": {
        "type": "ValidationFault",
        "Error": [
          {
            "Message": "Object Not Found",
            "code": "610",
            "Detail": "Object Not Found : Something you're trying to use has been made inactive. Check the fields with accounts, customers, items, vendors or employees.",
            "element": ""
          }
        ]
      },
      "bId": "bid2"
    },
    {
      "Fault": {
        "type": "ValidationFault",
        "Error": [
          {
            "Message": "Stale Object Error",
            "code": "5010",
            "Detail": "Stale Object Error : You and root were working on this at the same time. root finished before you did, so your work was not saved.",
            "element": ""
          }
        ]
      },
      "bId": "bid3"
    },
    {
      "bId": "bid4",
      "QueryResponse": {
        "SalesReceipt": [
          {
            "TxnDate": "2015-08-25",
            "domain": "QBO",
            "CurrencyRef": {
              "name": "United States Dollar",
              "value": "USD"
            },
            "PrintStatus": "NotSet",
            "PaymentRefNum": "10264",
            "TotalAmt": 337.5,
            "Line": [
              {
                "Description": "Custom Design",
                "DetailType": "SalesItemLineDetail",
                "SalesItemLineDetail": {
                  "TaxCodeRef": {
                    "value": "NON"
                  },
                  "Qty": 4.5,
                  "UnitPrice": 75,
                  "ItemRef": {
                    "name": "Design",
                    "value": "4"
                  }
                },
                "LineNum": 1,
                "Amount": 337.5,
                "Id": "1"
              },
              {
                "DetailType": "SubTotalLineDetail",
                "Amount": 337.5,
                "SubTotalLineDetail": {}
              }
            ],
            "ApplyTaxAfterDiscount": false,
            "DocNumber": "1003",
            "PrivateNote": "A private note.",
            "sparse": false,
            "DepositToAccountRef": {
              "name": "Checking",
              "value": "35"
            },
            "CustomerMemo": {
              "value": "Thank you for your business and have a great day!"
            },
            "Balance": 0,
            "CustomerRef": {
              "name": "Dylan Sollfrank",
              "value": "6"
            },
            "TxnTaxDetail": {
              "TotalTax": 0
            },
            "SyncToken": "1",
            "PaymentMethodRef": {
              "name": "Check",
              "value": "2"
            },
            "EmailStatus": "NotSet",
            "BillAddr": {
              "Lat": "INVALID",
              "Long": "INVALID",
              "Id": "49",
              "Line1": "Dylan Sollfrank"
            },
            "MetaData": {
              "CreateTime": "2015-08-27T14:59:48-07:00",
              "LastUpdatedTime": "2016-04-15T09:01:10-07:00"
            },
            "CustomField": [
              {
                "DefinitionId": "1",
                "Type": "StringType",
                "Name": "Crew #"
              }
            ],
            "Id": "11"
          }
        ],
        "startPosition": 1,
        "maxResults": 1
      }
    }
  ],
  "time": "2016-04-15T09:01:18.141-07:00"
}
```

#### XML example

```xml
<<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2016-04-18T13:09:30.392-07:00">
  <BatchItemResponse bId="bid1">
    <Vendor domain="QBO" sparse="false">
      <Id>58</Id>
      <SyncToken>0</SyncToken>
      <MetaData>
        <CreateTime>2016-04-18T13:09:30-07:00</CreateTime>
        <LastUpdatedTime>2016-04-18T13:09:30-07:00</LastUpdatedTime>
      </MetaData>
      <DisplayName>Smith Family Grocery</DisplayName>
      <PrintOnCheckName>Smith Family Grocery</PrintOnCheckName>
      <Active>true</Active>
      <Balance>0</Balance>
      <Vendor1099>false</Vendor1099>
      <CurrencyRef name="United States Dollar">USD</CurrencyRef>
    </Vendor>
  </BatchItemResponse>
  <BatchItemResponse bId="bid2">
    <Invoice domain="QBO" status="Deleted">
      <Id>119</Id>
    </Invoice>
  </BatchItemResponse>
  <BatchItemResponse bId="bid3">
    <SalesReceipt domain="QBO" sparse="false">
      <Id>38</Id>
      <SyncToken>1</SyncToken>
      <MetaData>
        <CreateTime>2016-03-21T11:15:46-07:00</CreateTime>
        <LastUpdatedTime>2016-04-18T13:09:30-07:00</LastUpdatedTime>
      </MetaData>
      <CustomField>
        <DefinitionId>1</DefinitionId>
        <Name>Crew #</Name>
        <Type>StringType</Type>
      </CustomField>
      <DocNumber>1011</DocNumber>
      <TxnDate>2016-03-21</TxnDate>
      <CurrencyRef name="United States Dollar">USD</CurrencyRef>
      <PrivateNote>This is another private note.</PrivateNote>
      <Line>
        <Id>1</Id>
        <LineNum>1</LineNum>
        <Description>Pest Control Services</Description>
        <Amount>87.50</Amount>
        <DetailType>SalesItemLineDetail</DetailType>
        <SalesItemLineDetail>
          <ItemRef name="Pest Control">10</ItemRef>
          <UnitPrice>35</UnitPrice>
          <Qty>2.5</Qty>
          <TaxCodeRef>NON</TaxCodeRef>
        </SalesItemLineDetail>
      </Line>
      <Line>
        <Amount>87.50</Amount>
        <DetailType>SubTotalLineDetail</DetailType>
        <SubTotalLineDetail />
      </Line>
      <Line>
        <Amount>8.75</Amount>
        <DetailType>DiscountLineDetail</DetailType>
        <DiscountLineDetail>
          <PercentBased>true</PercentBased>
          <DiscountPercent>10</DiscountPercent>
          <DiscountAccountRef name="Discounts given">86</DiscountAccountRef>
        </DiscountLineDetail>
      </Line>
      <TxnTaxDetail>
        <TotalTax>0</TotalTax>
      </TxnTaxDetail>
      <CustomerRef name="Pye's Cakes">15</CustomerRef>
      <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
      <BillAddr>
        <Id>57</Id>
        <Line1>Karen Pye</Line1>
        <Line2>Pye's Cakes</Line2>
        <Line3>350 Mountain View Dr.</Line3>
        <Line4>South Orange, NJ  07079</Line4>
        <Lat>40.7489277</Lat>
        <Long>-74.2609903</Long>
      </BillAddr>
      <ShipAddr>
        <Id>15</Id>
        <Line1>350 Mountain View Dr.</Line1>
        <City>South Orange</City>
        <CountrySubDivisionCode>NJ</CountrySubDivisionCode>
        <PostalCode>07079</PostalCode>
        <Lat>40.7633073</Lat>
        <Long>-74.2426072</Long>
      </ShipAddr>
      <TotalAmt>78.75</TotalAmt>
      <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
      <PrintStatus>NotSet</PrintStatus>
      <EmailStatus>NotSet</EmailStatus>
      <BillEmail>
        <Address>karen@pye.com</Address>
      </BillEmail>
      <Balance>0</Balance>
      <PaymentMethodRef name="Cash">1</PaymentMethodRef>
      <DepositToAccountRef name="Undeposited Funds">4</DepositToAccountRef>
    </SalesReceipt>
  </BatchItemResponse>
  <BatchItemResponse bId="bid4">
    <QueryResponse startPosition="1" maxResults="2">
      <SalesReceipt domain="QBO" sparse="false">
        <Id>17</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
          <CreateTime>2016-03-20T15:12:39-07:00</CreateTime>
          <LastUpdatedTime>2016-03-20T15:12:39-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
          <DefinitionId>1</DefinitionId>
          <Name>Crew #</Name>
          <Type>StringType</Type>
        </CustomField>
        <DocNumber>1008</DocNumber>
        <TxnDate>2016-02-27</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <Line>
          <Id>1</Id>
          <LineNum>1</LineNum>
          <Description>Custom Design</Description>
          <Amount>225.00</Amount>
          <DetailType>SalesItemLineDetail</DetailType>
          <SalesItemLineDetail>
            <ItemRef name="Design">4</ItemRef>
            <UnitPrice>75</UnitPrice>
            <Qty>3</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
          </SalesItemLineDetail>
        </Line>
        <Line>
          <Amount>225.00</Amount>
          <DetailType>SubTotalLineDetail</DetailType>
          <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
          <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Kate Whelan">14</CustomerRef>
        <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
        <BillAddr>
          <Id>54</Id>
          <Line1>Kate Whelan</Line1>
          <Line2>45 First St.</Line2>
          <Line3>Menlo Park, CA  94304 USA</Line3>
          <Lat>37.3813444</Lat>
          <Long>-122.1802812</Long>
        </BillAddr>
        <ShipAddr>
          <Id>14</Id>
          <Line1>45 First St.</Line1>
          <City>Menlo Park</City>
          <Country>USA</Country>
          <CountrySubDivisionCode>CA</CountrySubDivisionCode>
          <PostalCode>94304</PostalCode>
          <Lat>37.4585825</Lat>
          <Long>-122.1352789</Long>
        </ShipAddr>
        <TotalAmt>225.00</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NeedToPrint</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <BillEmail>
          <Address>Kate@Whelan.com</Address>
        </BillEmail>
        <Balance>0</Balance>
        <DepositToAccountRef name="Checking">35</DepositToAccountRef>
      </SalesReceipt>
      <SalesReceipt domain="QBO" sparse="false">
        <Id>11</Id>
        <SyncToken>0</SyncToken>
        <MetaData>
          <CreateTime>2016-03-20T14:59:48-07:00</CreateTime>
          <LastUpdatedTime>2016-03-20T14:59:48-07:00</LastUpdatedTime>
        </MetaData>
        <CustomField>
          <DefinitionId>1</DefinitionId>
          <Name>Crew #</Name>
          <Type>StringType</Type>
        </CustomField>
        <DocNumber>1003</DocNumber>
        <TxnDate>2016-03-18</TxnDate>
        <CurrencyRef name="United States Dollar">USD</CurrencyRef>
        <Line>
          <Id>1</Id>
          <LineNum>1</LineNum>
          <Description>Custom Design</Description>
          <Amount>337.50</Amount>
          <DetailType>SalesItemLineDetail</DetailType>
          <SalesItemLineDetail>
            <ItemRef name="Design">4</ItemRef>
            <UnitPrice>75</UnitPrice>
            <Qty>4.5</Qty>
            <TaxCodeRef>NON</TaxCodeRef>
          </SalesItemLineDetail>
        </Line>
        <Line>
          <Amount>337.50</Amount>
          <DetailType>SubTotalLineDetail</DetailType>
          <SubTotalLineDetail />
        </Line>
        <TxnTaxDetail>
          <TotalTax>0</TotalTax>
        </TxnTaxDetail>
        <CustomerRef name="Dylan Sollfrank">6</CustomerRef>
        <CustomerMemo>Thank you for your business and have a great day!</CustomerMemo>
        <BillAddr>
          <Id>49</Id>
          <Line1>Dylan Sollfrank</Line1>
          <Lat>INVALID</Lat>
          <Long>INVALID</Long>
        </BillAddr>
        <TotalAmt>337.50</TotalAmt>
        <ApplyTaxAfterDiscount>false</ApplyTaxAfterDiscount>
        <PrintStatus>NotSet</PrintStatus>
        <EmailStatus>NotSet</EmailStatus>
        <Balance>0</Balance>
        <PaymentMethodRef name="Check">2</PaymentMethodRef>
        <PaymentRefNum>10264</PaymentRefNum>
        <DepositToAccountRef name="Checking">35</DepositToAccountRef>
      </SalesReceipt>
    </QueryResponse>
  </BatchItemResponse>
</IntuitResponse>
```
