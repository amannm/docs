# Entitlements

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/entitlements
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / Entitlements
> Canonical entity: `Entitlements`

The Entitlements resource retrieves the features available to a company, identified by the company's `realmID`. The features available are determined by the type of company established during QuickBooks Online setup. These features are a super set of those enabled for the company by preferences and those enabled for a user by permissions.

**Note**: This resource does not accept an `application/json` header. Use `application/xml` as the `accept` header.

## The entitlements object

### entitlementsresponse

Model type: `object`

#### `PlanName`

Type: `String`

Billing plan associated with this company.

#### `Entitlement [0..n]`

`Entitlement.id`--Integer. Name of the entitlement. `Entitlement.name`--String. Name of the entitlement. `Entitlement.Term`--Boolean. Availability of entitlement: `On` or `Off`.

#### `SupportedLanguages`

Type: `String`

Comma separated list of languages.

#### `Entitlement`

Type: `TelephoneNumber`
Max length: maximum of 20 chars

Primary phone number.

<details>
<summary>Child attributes for `Entitlement`</summary>

##### telephonenumber

Model type: `object`

###### `FreeFormNumber`

Required: Optional
Type: `String`
Max length: Maximum of 20 chars

Specifies the telephone number in free form.

</details>

#### `CompanyStartDate`

Type: `DateTime`

DateTime when company file was created. This field and `Metadata.CreateTime` contain the same value.

<details>
<summary>Child attributes for `CompanyStartDate`</summary>

##### datetime

Model type: `object`

###### `dateTime`

Type: `string`

Local time zone: *`YYYY-MM-DDTHH:MM:SS`* UTC:  *YYYY-MM-DD*T *HH* *:MM:* *SS*Z Specific time zone:  `*YYYY-MM-DD*T` *`HH`* *`:MM:SS`* `+/- *HH* *:MM*`

</details>

#### `EmployerId`

Type: `String`

Employer identifier (EIN).

#### `QboCompany`

Type: `Boolean`

Check if the company is a QuickBooks Online company. `false` is returned if not a QuickBooks Online company, the company exists in the Intuit ecosystem, but is not a QuickBooks Online company, or the company is a QuickBooks Online company, but the current user does not belong to the company.

#### `Email`

Type: `EmailAddress`
Max length: max 100 chars

Default email address.

<details>
<summary>Child attributes for `Email`</summary>

##### emailaddress

Model type: `object`

###### `Address`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

An email address. The address format must follow the RFC 822 standard.

</details>

#### `WebAddr`

Type: `WebSiteAddress`

Website address.

<details>
<summary>Child attributes for `WebAddr`</summary>

##### websiteaddress

Model type: `object`

###### `URI`

Required: Optional
Type: `String`
Max length: Maximum of 1000 chars

Uniform Resource Identifier for the web site.

</details>

#### `FiscalYearStartMonth`

Type: `MonthEnum`

The start month of fiscal year.

#### `Thresholds [0..n]`

Type: `Threshold`
Minor version: 43

The threshold for this company.

<details>
<summary>Child attributes for `Thresholds [0..n]`</summary>

##### threshold

Model type: `object`

###### `currentCount`

Type: `String`

Indicates current value of attribute.

###### `aboveThreshold`

Type: `String`

Indicate whether the current count of the attribute has reached its limit.

###### `enforced`

Type: `String`

Whether the threshold is enforced.

###### `limit`

Type: `String`

The upper limit for the threshold.

###### `name`

Type: `String`

The name of the threshold.

</details>

#### `DaysRemainingTrial`

Type: `Integer`

Remaining trial period days.

#### `MaxUsers`

Type: `Integer`

Maximum billable users allowed in the company.

#### `CurrentUsers`

Type: `Integer`

Billable users currently in the company.

#### Example

```text
"<EntitlementsResponse>\n  <QboCompany>true</QboCompany>\n  <PlanName>QBWEBPLUSPAYROLLMONTHLY</PlanName>\n  <MaxUsers>10</MaxUsers>\n  <CurrentUsers>4</CurrentUsers>\n  <DaysRemainingTrial>0</DaysRemainingTrial>\n  <Entitlement id=\"7\">\n    <name>PayPal</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"8\">\n    <name>Merchant Service</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"1\">\n    <name>Class Tracking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"3\">\n    <name>Expense Tracking by Customer</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"4\">\n    <name>Time Tracking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"5\">\n    <name>Budgets</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"6\">\n    <name>Custom Invoice Styles</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"9\">\n    <name>1099 Forms for Vendors</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"10\">\n    <name>Managing Bills to Pay Later</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"11\">\n    <name>Complete Set of Reports</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"12\">\n    <name>Enhanced Reporting</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"13\">\n    <name>Exporting to Excel</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"15\">\n    <name>Delayed Charges</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"16\">\n    <name>Custom Sales Fields</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"17\">\n    <name>More Users -- up to 20</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"19\">\n    <name>Recurring Transactions</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"20\">\n    <name>Closing the Books</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"21\">\n    <name>Location Tracking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"22\">\n    <name>More Names</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"25\">\n    <name>Custom Home Page</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"26\">\n    <name>Do-it-yourself Payroll</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"28\">\n    <name>Online Banking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"29\">\n    <name>Basic Sales</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"30\">\n    <name>Basic Banking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"31\">\n    <name>Accounting</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"33\">\n    <name>Reports Only User</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"35\">\n    <name>Estimates</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"41\">\n    <name>Company Snapshot</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"42\">\n    <name>Purchase Order</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"43\">\n    <name>Inventory</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"44\">\n    <name>Do-it-yourself Payroll (Paycycle)</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"45\">\n    <name>Multi-Currency</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"46\">\n    <name>Trends</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"47\">\n    <name>Hide Employee List</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"48\">\n    <name>Simple Report List</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"49\">\n    <name>Global Tax Model</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"52\">\n    <name>Accountant Menu</name>\n    <term>On</term>\n  </Entitlement>\n  <Thresholds>\n    <threshold>\n      <name>CLASSES_AND_DEPARTMENTS</name>\n      <limit>40</limit>\n      <enforced>true</enforced>\n      <currentCount>19</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>ACCOUNTS</name>\n      <limit>250</limit>\n      <enforced>true</enforced>\n      <currentCount>7</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>USERS</name>\n      <limit>5</limit>\n      <enforced>true</enforced>\n      <currentCount>1</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>ACCOUTANTS</name>\n      <limit>2</limit>\n      <enforced>false</enforced>\n      <currentCount>-2</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>CUSTOMFIELD_ALL</name>\n      <limit>6</limit>\n      <enforced>false</enforced>\n      <currentCount>0</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>CUSTOMFIELD_PO</name>\n      <limit>3</limit>\n      <enforced>false</enforced>\n      <currentCount>0</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>CUSTOMFIELD_SALES</name>\n      <limit>3</limit>\n      <enforced>false</enforced>\n      <currentCount>0</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n   </Thresholds>\n</EntitlementsResponse>\n"
```

#### XML example

```xml
<EntitlementsResponse>
  <QboCompany>true</QboCompany>
  <PlanName>QBWEBPLUSPAYROLLMONTHLY</PlanName>
  <MaxUsers>10</MaxUsers>
  <CurrentUsers>4</CurrentUsers>
  <DaysRemainingTrial>0</DaysRemainingTrial>
  <Entitlement id="7">
    <name>PayPal</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="8">
    <name>Merchant Service</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="1">
    <name>Class Tracking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="3">
    <name>Expense Tracking by Customer</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="4">
    <name>Time Tracking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="5">
    <name>Budgets</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="6">
    <name>Custom Invoice Styles</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="9">
    <name>1099 Forms for Vendors</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="10">
    <name>Managing Bills to Pay Later</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="11">
    <name>Complete Set of Reports</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="12">
    <name>Enhanced Reporting</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="13">
    <name>Exporting to Excel</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="15">
    <name>Delayed Charges</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="16">
    <name>Custom Sales Fields</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="17">
    <name>More Users -- up to 20</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="19">
    <name>Recurring Transactions</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="20">
    <name>Closing the Books</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="21">
    <name>Location Tracking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="22">
    <name>More Names</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="25">
    <name>Custom Home Page</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="26">
    <name>Do-it-yourself Payroll</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="28">
    <name>Online Banking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="29">
    <name>Basic Sales</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="30">
    <name>Basic Banking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="31">
    <name>Accounting</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="33">
    <name>Reports Only User</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="35">
    <name>Estimates</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="41">
    <name>Company Snapshot</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="42">
    <name>Purchase Order</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="43">
    <name>Inventory</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="44">
    <name>Do-it-yourself Payroll (Paycycle)</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="45">
    <name>Multi-Currency</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="46">
    <name>Trends</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="47">
    <name>Hide Employee List</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="48">
    <name>Simple Report List</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="49">
    <name>Global Tax Model</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="52">
    <name>Accountant Menu</name>
    <term>On</term>
  </Entitlement>
  <Thresholds>
    <threshold>
      <name>CLASSES_AND_DEPARTMENTS</name>
      <limit>40</limit>
      <enforced>true</enforced>
      <currentCount>19</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>ACCOUNTS</name>
      <limit>250</limit>
      <enforced>true</enforced>
      <currentCount>7</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>USERS</name>
      <limit>5</limit>
      <enforced>true</enforced>
      <currentCount>1</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>ACCOUTANTS</name>
      <limit>2</limit>
      <enforced>false</enforced>
      <currentCount>-2</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>CUSTOMFIELD_ALL</name>
      <limit>6</limit>
      <enforced>false</enforced>
      <currentCount>0</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>CUSTOMFIELD_PO</name>
      <limit>3</limit>
      <enforced>false</enforced>
      <currentCount>0</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>CUSTOMFIELD_SALES</name>
      <limit>3</limit>
      <enforced>false</enforced>
      <currentCount>0</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
   </Thresholds>
  </EntitlementsResponse>
```

## Read entitlements

### Definition

- **Operation:** `GET /entitlements/v3/<realmID>`
- **Production Base URL (OAUTH1):** `https://qbo.sbfinance.intuit.com/manage`
- **Production Base URL (OAUTH2):** `https://quickbooks.api.intuit.com/manage`
- **Sandbox Base URL (OAUTH1):** `https://qbo.sbfinance.intuit.com/manage`
- **Sandbox Base URL (OAUTH2):** `https://sandbox-quickbooks.api.intuit.com/manage`

Retrieves the entitlements details.

### Returns

#### Example

```text
"<EntitlementsResponse>\n  <QboCompany>true</QboCompany>\n  <PlanName>QBWEBPLUSPAYROLLMONTHLY</PlanName>\n  <MaxUsers>10</MaxUsers>\n  <CurrentUsers>4</CurrentUsers>\n  <DaysRemainingTrial>0</DaysRemainingTrial>\n  <Entitlement id=\"7\">\n    <name>PayPal</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"8\">\n    <name>Merchant Service</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"1\">\n    <name>Class Tracking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"3\">\n    <name>Expense Tracking by Customer</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"4\">\n    <name>Time Tracking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"5\">\n    <name>Budgets</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"6\">\n    <name>Custom Invoice Styles</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"9\">\n    <name>1099 Forms for Vendors</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"10\">\n    <name>Managing Bills to Pay Later</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"11\">\n    <name>Complete Set of Reports</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"12\">\n    <name>Enhanced Reporting</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"13\">\n    <name>Exporting to Excel</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"15\">\n    <name>Delayed Charges</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"16\">\n    <name>Custom Sales Fields</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"17\">\n    <name>More Users -- up to 20</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"19\">\n    <name>Recurring Transactions</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"20\">\n    <name>Closing the Books</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"21\">\n    <name>Location Tracking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"22\">\n    <name>More Names</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"25\">\n    <name>Custom Home Page</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"26\">\n    <name>Do-it-yourself Payroll</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"28\">\n    <name>Online Banking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"29\">\n    <name>Basic Sales</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"30\">\n    <name>Basic Banking</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"31\">\n    <name>Accounting</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"33\">\n    <name>Reports Only User</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"35\">\n    <name>Estimates</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"41\">\n    <name>Company Snapshot</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"42\">\n    <name>Purchase Order</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"43\">\n    <name>Inventory</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"44\">\n    <name>Do-it-yourself Payroll (Paycycle)</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"45\">\n    <name>Multi-Currency</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"46\">\n    <name>Trends</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"47\">\n    <name>Hide Employee List</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"48\">\n    <name>Simple Report List</name>\n    <term>Off</term>\n  </Entitlement>\n  <Entitlement id=\"49\">\n    <name>Global Tax Model</name>\n    <term>On</term>\n  </Entitlement>\n  <Entitlement id=\"52\">\n    <name>Accountant Menu</name>\n    <term>On</term>\n  </Entitlement>\n  <Thresholds>\n    <threshold>\n      <name>CLASSES_AND_DEPARTMENTS</name>\n      <limit>40</limit>\n      <enforced>true</enforced>\n      <currentCount>19</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>ACCOUNTS</name>\n      <limit>250</limit>\n      <enforced>true</enforced>\n      <currentCount>7</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>USERS</name>\n      <limit>5</limit>\n      <enforced>true</enforced>\n      <currentCount>1</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>ACCOUTANTS</name>\n      <limit>2</limit>\n      <enforced>false</enforced>\n      <currentCount>-2</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>CUSTOMFIELD_ALL</name>\n      <limit>6</limit>\n      <enforced>false</enforced>\n      <currentCount>0</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>CUSTOMFIELD_PO</name>\n      <limit>3</limit>\n      <enforced>false</enforced>\n      <currentCount>0</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n    <threshold>\n      <name>CUSTOMFIELD_SALES</name>\n      <limit>3</limit>\n      <enforced>false</enforced>\n      <currentCount>0</currentCount>\n      <aboveThreshold>false</aboveThreshold>\n    </threshold>\n   </Thresholds>\n</EntitlementsResponse>\n"
```

#### XML example

```xml
<EntitlementsResponse>
  <QboCompany>true</QboCompany>
  <PlanName>QBWEBPLUSPAYROLLMONTHLY</PlanName>
  <MaxUsers>10</MaxUsers>
  <CurrentUsers>4</CurrentUsers>
  <DaysRemainingTrial>0</DaysRemainingTrial>
  <Entitlement id="7">
    <name>PayPal</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="8">
    <name>Merchant Service</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="1">
    <name>Class Tracking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="3">
    <name>Expense Tracking by Customer</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="4">
    <name>Time Tracking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="5">
    <name>Budgets</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="6">
    <name>Custom Invoice Styles</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="9">
    <name>1099 Forms for Vendors</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="10">
    <name>Managing Bills to Pay Later</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="11">
    <name>Complete Set of Reports</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="12">
    <name>Enhanced Reporting</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="13">
    <name>Exporting to Excel</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="15">
    <name>Delayed Charges</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="16">
    <name>Custom Sales Fields</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="17">
    <name>More Users -- up to 20</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="19">
    <name>Recurring Transactions</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="20">
    <name>Closing the Books</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="21">
    <name>Location Tracking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="22">
    <name>More Names</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="25">
    <name>Custom Home Page</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="26">
    <name>Do-it-yourself Payroll</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="28">
    <name>Online Banking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="29">
    <name>Basic Sales</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="30">
    <name>Basic Banking</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="31">
    <name>Accounting</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="33">
    <name>Reports Only User</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="35">
    <name>Estimates</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="41">
    <name>Company Snapshot</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="42">
    <name>Purchase Order</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="43">
    <name>Inventory</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="44">
    <name>Do-it-yourself Payroll (Paycycle)</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="45">
    <name>Multi-Currency</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="46">
    <name>Trends</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="47">
    <name>Hide Employee List</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="48">
    <name>Simple Report List</name>
    <term>Off</term>
  </Entitlement>
  <Entitlement id="49">
    <name>Global Tax Model</name>
    <term>On</term>
  </Entitlement>
  <Entitlement id="52">
    <name>Accountant Menu</name>
    <term>On</term>
  </Entitlement>
  <Thresholds>
    <threshold>
      <name>CLASSES_AND_DEPARTMENTS</name>
      <limit>40</limit>
      <enforced>true</enforced>
      <currentCount>19</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>ACCOUNTS</name>
      <limit>250</limit>
      <enforced>true</enforced>
      <currentCount>7</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>USERS</name>
      <limit>5</limit>
      <enforced>true</enforced>
      <currentCount>1</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>ACCOUTANTS</name>
      <limit>2</limit>
      <enforced>false</enforced>
      <currentCount>-2</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>CUSTOMFIELD_ALL</name>
      <limit>6</limit>
      <enforced>false</enforced>
      <currentCount>0</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>CUSTOMFIELD_PO</name>
      <limit>3</limit>
      <enforced>false</enforced>
      <currentCount>0</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
    <threshold>
      <name>CUSTOMFIELD_SALES</name>
      <limit>3</limit>
      <enforced>false</enforced>
      <currentCount>0</currentCount>
      <aboveThreshold>false</aboveThreshold>
    </threshold>
   </Thresholds>
  </EntitlementsResponse>
```
