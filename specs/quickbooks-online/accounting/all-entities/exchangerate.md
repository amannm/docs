# Exchangerate

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/exchangerate
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Exchangerate
> Canonical entity: `Exchangerate`

Applicable only for those companies that enable multicurrency, the exchangerate resource provides the ability to query and set exchange rates available to the QuickBooks Online company. This entity works in combination with the companycurrency entity and the Currency Center in the QuickBooks Online UI to manage exchange rates for the company.

## The exchangerate object

### exchangerateresponse

Model type: `object`

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

#### `AsOfDate`

Required: Required for update
Type: `Boolean`
Traits: filterable

Date on which this exchange rate was set.

#### `SourceCurrencyCode`

Required: Required for update
Type: `String`
Traits: filterable
Max length: Exactly 3 chars

The source currency from which the exchange rate is specified, and usually. Specify as a three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on. For example, in the equation `65 INR = 1 USD`, `INR` is the source currency.

#### `Rate`

Required: Required for update
Type: `Decimal`

The exchange rate between `SourceCurrencyCode` and `TargetCurrencyCode` on the `AsOfDate` date.

#### `CustomField `

Required: Optional
Type: `CustomField`

One of, up to three custom fields for the transaction. Available for custom fields so configured for the company. Check `Preferences.SalesFormsPrefs.CustomField` and `Preferences.VendorAndPurchasesPrefs.POCustomField` for custom fields currenly configured. [Click here](https://developer.intuit.com/app/developer/qbo/docs/develop/tutorials/create-custom-fields) to learn about managing custom fields.

<details>
<summary>Child attributes for `CustomField `</summary>

##### customfield

Model type: `object`

###### `DefinitionId`

Required: Required
Type: `String`
Traits: read only, system defined

Unique identifier of the CustomFieldDefinition that corresponds to this CustomField.

###### `Type`

Type: `CustomFieldTypeEnum`
Traits: read only

Data type of custom field. Only one type is currently supported: `StringType`.

###### `StringValue`

Required: Optional
Type: `String`

The value for the `StringType`custom field.

###### `Name`

Required: Optional
Type: `String`
Traits: read only

Name of the custom field.

</details>

#### `TargetCurrencyCode`

Required: Optional
Type: `String`
Max length: Exactly 3 chars
Default: The home currency as defined in company preferences

The target currency against which the exchange rate is specified. Specify as a three letter string representing the ISO 4217 code for the currency. For example, `USD`, `AUD`, `EUR`, and so on. For example, in the equation `65 INR = 1 USD`, `USA` is the target currency.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`
Traits: filterable, sortable

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

## Get an exchangerate for an individual currency code.

### Definition

- **Operation:** `GET /v3/company/<realmID>/exchangerate?sourcecurrencycode=<currencycode>[&asofdate=<yyyy-mm-dd>]`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

-currencycode is the desired currency code. Required. -yyyy-mm-dd is the desired effective date. If not specified, today's date is used.

### Sample Query

#### Example

```text
"?sourcecurrencycode=<USA>&asofdate=<yyyy-mm-dd>\n"
```

### Returns

Returns the exchangerate object.

#### Example

```json
{
  "ExchangeRate": {
    "SyncToken": "1",
    "domain": "QBO",
    "AsOfDate": "2015-07-07",
    "SourceCurrencyCode": "EUR",
    "Rate": 2.5,
    "sparse": false,
    "TargetCurrencyCode": "USD",
    "MetaData": {
      "LastUpdatedTime": "2015-07-08T09:24:02-07:00"
    }
  },
  "time": "2015-07-08T09:40:58.146-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-08T09:32:40.203-07:00">
    <ExchangeRate domain="QBO" sparse="false">
        <SyncToken>1</SyncToken>
        <MetaData>
            <LastUpdatedTime>2015-07-08T09:24:02-07:00</LastUpdatedTime>
        </MetaData>
        <SourceCurrencyCode>EUR</SourceCurrencyCode>
        <TargetCurrencyCode>USD</TargetCurrencyCode>
        <Rate>2.5</Rate>
        <AsOfDate>2015-07-07</AsOfDate>
    </ExchangeRate>
</IntuitResponse>
```

## Query exchangerate objects.

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from exchangerate where sourcecurrencycode in ('EUR', 'INR') and asofdate='2015-07-07'"
```

#### XML example

```sql
select * from exchangerate where sourcecurrencycode in ('EUR', 'INR') and asofdate='2015-07-07'
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "ExchangeRate": [
      {
        "SyncToken": "0",
        "AsOfDate": "2015-05-15",
        "SourceCurrencyCode": "INR",
        "Rate": 5,
        "TargetCurrencyCode": "USD",
        "MetaData": {
          "LastUpdatedTime": "2015-07-07T12:38:40-07:00"
        }
      },
      {
        "SyncToken": "0",
        "AsOfDate": "2015-07-07",
        "SourceCurrencyCode": "EUR",
        "Rate": 5,
        "TargetCurrencyCode": "USD",
        "MetaData": {
          "LastUpdatedTime": "2015-07-07T12:40:08-07:00"
        }
      }
    ],
    "maxResults": 2,
    "totalCount": 2
  },
  "time": "2015-07-08T09:19:44.495-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-08T09:18:44.070-07:00">
    <QueryResponse startPosition="1" maxResults="2" totalCount="2">
        <ExchangeRate>
            <SyncToken>0</SyncToken>
            <MetaData>
                <LastUpdatedTime>2015-07-07T12:38:40-07:00</LastUpdatedTime>
            </MetaData>
            <SourceCurrencyCode>INR</SourceCurrencyCode>
            <TargetCurrencyCode>USD</TargetCurrencyCode>
            <Rate>5</Rate>
            <AsOfDate>2015-07-07</AsOfDate>
        </ExchangeRate>
        <ExchangeRate>
            <SyncToken>0</SyncToken>
            <MetaData>
                <LastUpdatedTime>2015-07-07T12:40:08-07:00</LastUpdatedTime>
            </MetaData>
            <SourceCurrencyCode>EUR</SourceCurrencyCode>
            <TargetCurrencyCode>USD</TargetCurrencyCode>
            <Rate>5</Rate>
            <AsOfDate>2015-07-07</AsOfDate>
        </ExchangeRate>
    </QueryResponse>
</IntuitResponse>
```

## Update an exchangerate

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/exchangerate`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

- `SourceCurrencyCode`, `Rate`, and `AsOfDate` are mandatory fields.
- `TargetCurrencyCode` defaults to Home Currency if not supplied.
- Setting exchange rate to anything other than 1 for a case where `SourceCurrencyCode=TargetCurrencyCode` results in the exchange rate set to 1.
- Setting an exchange rate for the home currency, that is, where `SourceCurrencyCode` is set to the home currency results in a validation error.

### Request Body

Schema: `exchangerateresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "SyncToken": "0",
  "AsOfDate": "2015-07-08",
  "SourceCurrencyCode": "INR",
  "Rate": 7,
  "TargetCurrencyCode": "USD",
  "MetaData": {
    "LastUpdatedTime": "2015-07-07T12:38:40-07:00"
  }
}
```

#### XML example

```xml
 <ExchangeRate xmlns="http://schema.intuit.com/finance/v3" sparse="false">
    <SyncToken>0</SyncToken>
    <MetaData>
        <LastUpdatedTime>2015-07-07T12:40:08-07:00</LastUpdatedTime>
    </MetaData>
    <SourceCurrencyCode>EUR</SourceCurrencyCode>
    <TargetCurrencyCode>USD</TargetCurrencyCode>
    <Rate>2.5</Rate>
    <AsOfDate>2015-07-07</AsOfDate>
</ExchangeRate>
```

### Returns

The exchangerate response body.

#### Example

```json
{
  "ExchangeRate": {
    "SyncToken": "0",
    "domain": "QBO",
    "AsOfDate": "2015-07-08",
    "SourceCurrencyCode": "INR",
    "Rate": 7,
    "sparse": false,
    "TargetCurrencyCode": "USD",
    "MetaData": {
      "LastUpdatedTime": "2015-07-08T09:21:46-07:00"
    }
  },
  "time": "2015-07-08T09:21:46.310-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-08T09:24:02.761-07:00">
    <ExchangeRate domain="QBO" sparse="false">
        <SyncToken>1</SyncToken>
        <MetaData>
            <LastUpdatedTime>2015-07-08T09:24:02-07:00</LastUpdatedTime>
        </MetaData>
        <SourceCurrencyCode>EUR</SourceCurrencyCode>
        <TargetCurrencyCode>USD</TargetCurrencyCode>
        <Rate>2.5</Rate>
        <AsOfDate>2015-07-07</AsOfDate>
    </ExchangeRate>
</IntuitResponse>
```
