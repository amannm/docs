# Item

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/most-commonly-used/item
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [Most commonly used](index.md) / Item
> Canonical entity: `Item`

An item is a thing that your company buys, sells, or re-sells, such as products and services. An item is shown as a line on an invoice or other sales form. The `Item.Type` attribute, which specifies how the item is used, has one of the following values:

**Inventory** Used in transactions to track merchandise that your business purchases, stocks, and re-sells as inventory. QuickBooks tracks the current number of inventory items in stock, cost of goods sold, and the asset value of the inventory after the purchase and sale of every item.

**Group** Used as a container for a bundle of items with a count for each item. For example, a Gift Basket with 2 apples, 5 pencils and 1 stack of paper. The bundle is the Gift Basket, the bundle items are apples, pencils and paper. Note: Creating them via the QuickBooks Online API is not supported. Bundles cannot contain other bundles. Bundles cannot contain categories. An item can be listed more than once with same or different quantities. Bundles can be added to transactions.

**Service** Used in transactions to track services that you charge on the purchase. For example, specialized labor, consulting hours, and professional fees.

**NonInventory** Used for goods you buy but don’t track, like office supplies.
Used in transactions for goods and materials for a specific job that you charge back to the customer and don't track yourself.

In addition to the above, QuickBooks companies supports item categories to define item hierarchies. Use `Item.Type` set to `Category` to create hierarchies. Of note:

- Non-category items used as parent items and used for things the company sells cannot be freely mixed.
    - An app can now clearly distinguish between things the company sells and categories used to build a hierarchy to organize them.
    - Categories do not have a price, income account, or expense accounts.

- Items—-the things the company sells—-cannot have children. That is, if your items are organized into a hierarchy, items can only be at the leaf level of the hierarchy.
- Categories are only available on companies that have enabled Categories. Test the `CompanyInfo.NameValue.Name.ItemCategoriesFeature` flag:
    - `true`— categories are enabled
    - `false`— categories are not enabled.

### Inactivate an item

Inactivating an item is achieved by setting the `Active` attribute to false in an object update request. The record is hidden for display purposes. References to inactive objects are left intact. Not valid for `Category` item types.

## The item object

### itemresponse

Model type: `object`

#### `Id`

Required: Required for update
Type: `IdType`
Traits: read only, system defined, filterable, sortable

Unique Identifier for an Intuit entity (object). Required for the update operation.

#### `ItemCategoryType`

Required: Required
Type: `String`
Minor version: 3
Locales: FR

Classification that specifies the use of this item. Applicable for France companies, only. Available when endpoint is evoked with the `minorversion=3` query parameter. Read-only after object is created. Valid values include: `Product` and `Service`.

#### `Name`

Required: Required
Type: `String`
Traits: filterable, sortable
Max length: maximum of 100 chars

Name of the item. This value is unique.

#### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the entity. Required for the update operation.

#### `InvStartDate`

Required: Conditionally required
Type: `Date`

Date of opening balance for the inventory transaction. For read operations, the date returned in this field is always the originally provided inventory start date. For update operations, the date supplied is interpreted as the inventory adjust date, is stored as such in the underlying data model, and is reflected in the QuickBooks Online UI for the object. The inventory adjust date is not exposed for read operations through the API. Required for `Inventory` type items.

<details>
<summary>Child attributes for `InvStartDate`</summary>

##### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

#### `Type`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Minor version: specified.

Classification that specifies the use of this item. See the description at the top of the Item entity page for details about supported item types. For requests with minor versions earlier than 4 specified, this field is read-only and system-defined as follows:

`Inventory`--Default setting when `TrackQtyOnHand`, `InvStartDate`, and `AssetAccountRef` are specified. Used for goods the company sells and buys that are tracked as inventory.

`Service`--Default setting when `TrackQtyOnHand`, `InvStartDate`, and `AssetAccountRef` are not specified. Used for non-tangible goods the company sells and buys that are not tracked as inventory. For example, specialized labor, consulting hours, and professional fees.

For requests with minor version=4 query parameter, this field is required to be explicitly set with one of the following:

`Inventory`--Used for goods the company sells and buys that are tracked as inventory.

`Service`--Used for non-tangible goods the company sells and buys that are not tracked as inventory. For example, specialized labor, consulting hours, and professional fees.

`NonInventory`--Use for goods the company sells and buys that are not tracked as inventory. For example, office supplies or goods bought on behalf of the customer.

When querying Item objects with minor versions earlier than 4 specified, `NonInventory` types are returned as type `Service`. For French locales, `Type` is tied with `ItemCategoryType`: if `ItemCategoryType` is set to `Service`, then `Type` is set to `Service`, if `ItemCategoryType` is `Product`, then `Type` is set to `NonInventory`. >Required when minor version 4 is specified.

#### `QtyOnHand`

Required: Conditionally required
Type: `Decimal`

Current quantity of the `Inventory` items available for sale. Not used for `Service` or `NonInventory` type items.Required for `Inventory` type items.

#### `AssetAccountRef`

Required: Conditionally required
Type: `ReferenceType`

Reference to the Inventory Asset account that tracks the current value of the inventory. If the same account is used for all inventory items, the current balance of this account will represent the current total value of the inventory. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `AssetAccountRef.value` and `AssetAccountRef.name`, respectively. Required for `Inventory` item types.

<details>
<summary>Child attributes for `AssetAccountRef`</summary>

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

#### `FullyQualifiedName`

Type: `String`
Traits: read only, system defined, filterable

Fully qualified name of the entity. The fully qualified name prepends the topmost parent, followed by each sub element separated by colons. Takes the form of `Item:SubItem`. Returned from an existing object and not input on a new object.Limited to 5 levels.

#### `ExpenseAccountRef`

Type: `ReferenceType`

Reference to the expense account used to pay the vendor for this item. Must be an account with account type of `Cost of Goods Sold`. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `ExpenseAccountRef.value` and `ExpenseAccountRef.name`, respectively. For France locales:

This is an optional field.

This is the purchase account id, If not provided it defaults to the default purchase account: 605100 and 601100 are the default expense accounts used for `Service` and `Product` type of item, respectively.

Required for `Inventory`, `NonInventory`, and `Service` item types

<details>
<summary>Child attributes for `ExpenseAccountRef`</summary>

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

#### `Level`

Type: `Integer`
Traits: read only, system defined
Default: 0

Specifies the level of the hierarchy in which the entity is located. Zero specifies the top level of the hierarchy; anything above will be the next level with respect to the parent. Limited to 5 levels.

#### `IncomeAccountRef`

Required: Conditionally Required
Type: `ReferenceType`

Reference to the posting account, that is, the account that records the proceeds from the sale of this item. Must be an account with account type of `Sales of Product Income`. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `IncomeAccountRef.value` and `IncomeAccountRef.name`, respectively.For France locales:

This is an optional field.

This is the sales account id, If not provided it defaults to the default sales account: 706100 and 707100 are the default expense accounts used for `Service` and `Product` type of item, respectively.

required for `Inventory` and `Service` item types

<details>
<summary>Child attributes for `IncomeAccountRef`</summary>

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

#### `TaxClassificationRef`

Type: `ReferenceType`
Minor version: 34

Tax classification segregates different items into different classifications and the tax classification is one of the key parameters to determine appropriate tax on transactions involving items. Tax classifications are sourced by either tax governing authorities as in India/Malaysia or externally like Exactor. 'Fuel', 'Garments' and 'Soft drinks' are a few examples of tax classification in layman terms. User can choose a specific tax classification for an item while creating it. A level 1 tax classification cannot be associated to an Item.

<details>
<summary>Child attributes for `TaxClassificationRef`</summary>

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

#### `Sku`

Required: Optional
Type: `String`
Traits: filterable
Max length: maximum of 100 chars
Minor version: 4

The stock keeping unit (SKU) for this Item. This is a company-defined identifier for an item or product used in tracking inventory.

#### `SalesTaxIncluded`

Required: Optional
Type: `Boolean`
Default: false

True if the sales tax is included in the item amount, and therefore is not calculated for the transaction.

#### `TrackQtyOnHand`

Required: Optional
Type: `Boolean`
Default: false

True if there is quantity on hand to be tracked. Once this value is true, it cannot be updated to false. Applicable for items of type `Inventory`. Not applicable for `Service` or `NonInventory` item types.

#### `SalesTaxCodeRef`

Required: Optional
Type: `ReferenceType`

Reference to the sales tax code for the Sales item. Applicable to Service and Sales item types only. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `SalesTaxCodeRef.value` and `SalesTaxCodeRef.name`, respectively.

<details>
<summary>Child attributes for `SalesTaxCodeRef`</summary>

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

#### `ClassRef`

Required: Optional
Type: `ReferenceType`
Minor version: 41

Reference to the Class for the item. Query the Class name list resource to determine the appropriate object for this reference. Use `Class.Id` and `Class.Name` from that object for `ClassRef.value` and `ClassRef.name`, respectively.

<details>
<summary>Child attributes for `ClassRef`</summary>

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

#### `Source`

Required: Optional
Type: `String`
Minor version: 59

The Source type of the transactions created by QuickBooks Commerce. Valid values include: `QBCommerce`

#### `PurchaseTaxIncluded`

Required: Optional
Type: `Boolean`
Default: False

True if the purchase tax is included in the item amount, and therefore is not calculated for the transaction.

#### `Description`

Required: Optional
Type: `String`
Max length: maximum of 4000 chars

Description of the item.

#### `AbatementRate`

Required: Optional
Type: `Decimal`
Minor version: 3
Locales: IN

Sales tax abatement rate for India locales.

#### `SubItem`

Required: Optional
Type: `Boolean`

If true, this is a sub item. If false or null, this is a top-level item. Creating inventory hierarchies with traditional inventory items is being phased out in lieu of using categories and sub categories.

#### `Taxable`

Required: Optional
Type: `Boolean`
Locales: US

If true, transactions for this item are taxable. Applicable to US companies, only.

#### `UQCDisplayText`

Required: Optional
Type: `String`
Max length: maximum of 25 chars
Minor version: 33
Locales: IN

Text to be displayed on customer's invoice to denote the Unit of Measure (instead of the standard code).

#### `ReorderPoint`

Required: Optional
Type: `Decimal`

The minimum quantity of a particular inventory item that you need to restock at any given time. The ReorderPoint value cannot be set to null for sparse updates(sparse=true). It can be set to null only for full updates.

#### `PurchaseDesc`

Required: Optional
Type: `String`
Max length: Max 1000 chars

Purchase description for the item.

#### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the entity. The MetaData values are set by Data Services and are read only for all applications.

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

#### `PrefVendorRef`

Required: Optional
Type: `ReferenceType`
Minor version: 31

Reference to the preferred vendor of this item. Query the Vendor name list resource to determine the appropriate object for this reference. Use `Vendor.Id` and `Vendor.Name` from that object for `ParentRef.value` and `ParentRef.name`, respectively.

<details>
<summary>Child attributes for `PrefVendorRef`</summary>

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

#### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable
Default: true

If true, the object is currently enabled for use by QuickBooks.

#### `UQCId`

Required: Optional
Type: `String`
Minor version: 33
Locales: IN

Id of Standard Unit of Measure (UQC:Unique Quantity Code) of the item according to GST rule. UQCId should be one of the following ids:

<details>
<summary>Show valid values</summary>

#### ATTRIBUTES

| Name | Description |
| --- | --- |
| **ID** | **VALUE** |
| 1 | BAG |
| 2 | BAL |
| 3 | BDL |
| 4 | BKL |
| 5 | BOU |
| 6 | BOX |
| 7 | BTL |
| 8 | BUN |
| 9 | CAN |
| 10 | CBM |
| 11 | CCM |
| 12 | CMS |
| 13 | CTN |
| 14 | DOZ |
| 15 | DRM |
| 16 | GGR |
| 17 | GMS |
| 18 | GRS |
| 19 | GYD |
| 20 | KGS |
| 21 | KLR |
| 22 | KME |
| 23 | MLT |
| 24 | MTR |
| 25 | NOS |
| 26 | PAC |
| 27 | PCS |
| 28 | PRS |
| 29 | QTL |
| 30 | ROL |
| 31 | SET |
| 32 | SQF |
| 33 | SQM |
| 34 | SQY |
| 35 | TBS |
| 36 | TGM |
| 37 | THD |
| 38 | TON |
| 39 | TUB |
| 40 | UGS |
| 41 | UNT |
| 42 | YDS |
| 43 | OTH |

</details>

#### `ReverseChargeRate`

Required: Optional
Type: `Decimal`
Minor version: 3
Locales: IN

Sales tax reverse charge rate for India locales.

#### `PurchaseTaxCodeRef`

Required: Optional
Type: `ReferenceType`

Reference to the purchase tax code for the item. Applicable to Service, Other Charge, and Product (Non-Inventory) item types. Query the TaxCode name list resource to determine the appropriate TaxCode object for this reference. Use `TaxCode.Id` and `TaxCode.Name` from that object for `PurchaseTaxCodeRef.value` and `PurchaseTaxCodeRef.name`, respectively.

<details>
<summary>Child attributes for `PurchaseTaxCodeRef`</summary>

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

#### `ServiceType`

Required: Optional
Type: `String`
Minor version: 3
Locales: IN

Sales tax service type for India locales.

<details>
<summary>Show valid values</summary>

`ADVT`, `AIRPORTSERVICES`, `AIRTRANSPORT`, `AIRTRVLAGNT`, `ARCHITECT`,`ASSTMGMT`, `ATMMAINTENANCE`, `AUCTIONSERV`, `AUTHSERST`, `BANKANDFIN`, `BEAUTYPARLOR`, `BROADCAST`, `BUSINESSAUX`, `BUSINESSEXHIBITION`, `BUSINESSSUPPORTSERV`, `CA`, `CABLEOPTR`, `CARGOHAND`, `CLEANINGSERV`, `CLEARANDFORW`, `CLUBSANDASSSERVICE`, `COMMCOACHORTRAINING`, `CONSENG`, `CONSTRCOMMERCIALCOMPLEX`, `CONTAINERRAILTRANS`, `CONVSERV`, `COSTACC`, `COURIER`, `CREDITCARD`, `CREDITRATAGNCY`, `CRUISESHIPTOUR`, `CS`, `CUSHOUSEAG`, `DESIGNSERV`, `DEVELOPSUPPLYCONTENT`, `DREDGING`, `DRYCLEANING`, `ERECTIONCOMMORINSTALL`, `EVENTMGMT`, `FASHIONDES`, `FOREXBROKING`, `FORWARDCONTRACT`, `FRANCHISESERV`, `GENERALINSURANCE"/>`, `GOODSTRANSPORT`, `HEALTHCLUBANDFITNESS`, `INFORMATIONSERV`, `INSURAUX`, `INTDEC`, `INTELLECTUALPROPERTY`, `INTERNATIONALAIRTRAVEL`, `INTERNETCAFE`, `INTERNETTELEPHONY`, `LIFEINS`, `MAILLISTCOMPILE`, `MANDAPKEEPER`, `MANPWRRECRUIT`, `MGMTCONSUL`, `MGMTMAINTREPAIR`, `MININGOIL`, `MKTRESAGNCY`, `ONLINEINFORMRETRIEVAL`, `OPINIONPOLL`, `OUTDOORCATERING`, `PACKAGINGSERV`, `PANDALSHAMIANA`, `PHOTOGRAPHY`, `PORT`, `PORTSER`, `PROCESSCLEARHOUSE`, `PUBLICRELATIONMGMT`, `RAILTRAVELAGNT`, `REALESTAGT`, `RECOVERYAGENTS`, `REGISTRARSERV`, `RENTACAB`, `RENTINGIMMOVABLEPROP`, `RESIDENTIALCOMPLEXCONST`, `SALEOFSPACEFORADVT`, `SCANDTECHCONSUL`, `SECAG`, `SERVICESPROVIDEDFORTRANSACTION`, `SHARETRANSFERSERV`, `SHIPMGMT`, `SITEPREP`, `SOUNDRECORD`, `SPONSORSHIP`, `STAG`, `STOCKBROKING"/>`, `STOCKEXCHGSERV`, `STORANDWAREHOUSING`, `SUPPLYTANGIBLEGOODS`, `SURVEYANDMAPMAKING`, `SURVEYMINERALS`, `TECHINSPECTION`, `TECHTESTING`, `TELECOMMUNICATIONSERV`, `TELEVISIONANDRADIO`, `TOUROP`, `TRANSPORTPIPELINE`, `TRAVELAGENT`, `ULIPMANAGEMENT`, `UNDERWRITER`, `VIDEOTAPEPROD`, `WORKSCONTRACT`

</details>

#### `PurchaseCost`

Required: Optional
Type: `Decimal`
Max length: Maximum of 99999999999

Amount paid when buying or ordering the item, as expressed in the home currency.

#### `ParentRef`

Required: Optional
Type: `ReferenceType`

The immediate parent of the sub item in the hierarchical Item:SubItem list. If SubItem is true, then ParenRef is required. If SubItem is true, then ParenRef is required. Query the Item name list resource to determine the appropriate object for this reference. Use `Item.Id` and `Item.Name` from that object for `ParentRef.value` and `ParentRef.name`, respectively.

<details>
<summary>Child attributes for `ParentRef`</summary>

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

#### `UnitPrice`

Required: Optional
Type: `Decimal`
Traits: sortable
Max length: maximum of 99999999999
Default: 0

Corresponds to the Price/Rate column on the QuickBooks Online UI to specify either unit price, a discount, or a tax rate for item. If used for unit price, the monetary value of the service or product, as expressed in the home currency. If used for a discount or tax rate, express the percentage as a fraction. For example, specify `0.4` for 40% tax.

#### Example

```json
{
  "Item": {
    "FullyQualifiedName": "Trees",
    "domain": "QBO",
    "Name": "Trees",
    "SyncToken": "0",
    "sparse": false,
    "Active": true,
    "Type": "Category",
    "Id": "29",
    "MetaData": {
      "CreateTime": "2015-10-06T08:50:34-07:00",
      "LastUpdatedTime": "2015-10-06T08:50:34-07:00"
    }
  },
  "time": "2015-10-06T08:50:34.863-07:00"
}
```

#### XML example

```text
To be supplied.
```

## Create an item

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/item`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The elements to create an item are listed here.

Schema: `itemrequest`

<details>
<summary>Show schema for `itemrequest`</summary>

#### itemrequest

Model type: `object`

##### `Name`

Required: Required
Type: `String`
Traits: filterable, sortable
Max length: Maximum of 100 chars

Name of the item. This value must be unique, at least one character in length, and cannot include tabs, new lines, or colons. Required for create.

##### `QtyOnHand`

Required: Conditionally required
Type: `Decimal`

Current quantity of the `Inventory` items available for sale. Not used for `Service` or `NonInventory` type items.Required for `Inventory` type items.

##### `IncomeAccountRef`

Required: Conditionally required
Type: `ReferenceType`

Reference to the posting account, that is, the account that records the proceeds from the sale of this item. Must be an account with account type of `Sales of Product Income`. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `IncomeAccountRef.value` and `IncomeAccountRef.name`, respectively. For France locales:

This is an optional field.

This is the sales account id, If not provided it defaults to the default sales account: 706100 and 707100 are the default expense accounts used for `Service` and `Product` type of item, respectively.

Required for `Inventory` and `Service` item types.

<details>
<summary>Child attributes for `IncomeAccountRef`</summary>

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

##### `Type`

Required: Conditionally required
Type: `String`
Traits: filterable, sortable
Minor version: specified.

Classification that specifies the use of this item. See the description at the top of the Item entity page for details about supported item types. For requests with minor versions earlier than 4 specified, this field is read-only and system-defined as follows:

`Inventory`--Default setting when `TrackQtyOnHand`, `InvStartDate`, and `AssetAccountRef` are specified. Used for goods the company sells and buys that are tracked as inventory.

`Service`--Default setting when `TrackQtyOnHand`, `InvStartDate`, and `AssetAccountRef` are not specified. Used for non-tangible goods the company sells and buys that are not tracked as inventory. For example, specialized labor, consulting hours, and professional fees.

For requests with minor version=4 query parameter, this field is required to be explicitly set with one of the following:

`Inventory`--Used for goods the company sells and buys that are tracked as inventory.

`Service`--Used for non-tangible goods the company sells and buys that are not tracked as inventory. For example, specialized labor, consulting hours, and professional fees.

`NonInventory`--Use for goods the company sells and buys that are not tracked as inventory. For example, office supplies or goods bought on behalf of the customer.

When querying Item objects with minor versions earlier than 4 specified, `NonInventory` types are returned as type `Service`. For French locales, `Type` is tied with `ItemCategoryType`: if `ItemCategoryType` is set to `Service`, then `Type` is set to `Service`, if `ItemCategoryType` is `Product`, then `Type` is set to `NonInventory`. >Required when minor version 4 is specified.

##### `AssetAccountRef`

Required: Condtionally required
Type: `ReferenceType`

Reference to the Inventory Asset account that tracks the current value of the inventory. If the same account is used for all inventory items, the current balance of this account will represent the current total value of the inventory. Must be an account with account type of `Other Current Asset`. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `AssetAccountRef.value` and `AssetAccountRef.name`, respectively. Required for `Inventory` item types.

<details>
<summary>Child attributes for `AssetAccountRef`</summary>

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

##### `InvStartDate`

Required: Condtionally required
Type: `Date`

Date of opening balance for the inventory transaction. Required when creating an `Item.Type=Inventory`. Required for `Inventory` item types.

<details>
<summary>Child attributes for `InvStartDate`</summary>

###### date

Model type: `object`

###### `date`

Type: `String`

Local timezone: *`YYYY-MM-DD`*UTC: `*YYYY-MM-DD*Z` Specific time zone: *`YYYY-MM-DD+/-HH:MM`*
 The date format follows the [XML Schema standard.](https://www.w3.org/TR/xmlschema-2/)

</details>

##### `ExpenseAccountRef`

Required: Condtionally required
Type: `ReferenceType`

Reference to the expense account used to pay the vendor for this item. Must be an account with account type of `Cost of Goods Sold`. Query the Account name list resource to determine the appropriate Account object for this reference. Use `Account.Id` and `Account.Name` from that object for `ExpenseAccountRef.value` and `ExpenseAccountRef.name`, respectively. For France locales:

This is an optional field.

This is the purchase account id, If not provided it defaults to the default purchase account: 605100 and 601100 are the default expense accounts used for `Service` and `Product` type of item, respectively.

Required for `Inventory`, `NonInventory`, and `Service` item types.

<details>
<summary>Child attributes for `ExpenseAccountRef`</summary>

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

</details>

#### Example

```json
{
  "TrackQtyOnHand": true,
  "Name": "Garden Supplies",
  "QtyOnHand": 10,
  "IncomeAccountRef": {
    "name": "Sales of Product Income",
    "value": "79"
  },
  "AssetAccountRef": {
    "name": "Inventory Asset",
    "value": "81"
  },
  "InvStartDate": "2015-01-01",
  "Type": "Inventory",
  "ExpenseAccountRef": {
    "name": "Cost of Goods Sold",
    "value": "80"
  }
}
```

#### XML example

```xml
<Item xmlns="http://schema.intuit.com/finance/v3" sparse="false">
    <Name>Kitchen Supplies</Name>
    <IncomeAccountRef name="Sales of Product Income">79</IncomeAccountRef>
    <PurchaseDesc>This is the purchasing description.</PurchaseDesc>
    <PurchaseCost>35</PurchaseCost>
    <ExpenseAccountRef name="Cost of Goods Sold">80</ExpenseAccountRef>
    <AssetAccountRef name="Inventory Asset-1">81</AssetAccountRef>
    <Type>Inventory</Type>
    <TrackQtyOnHand>true</TrackQtyOnHand>,
    <QtyOnHand>10</QtyOnHand>,
    <InvStartDate>2015-01-01</InvStartDate>
</Item>
```

### Returns

Returns the newly created item object.

#### Example

```json
{
  "Item": {
    "FullyQualifiedName": "Garden Supplies",
    "domain": "QBO",
    "Id": "19",
    "Name": "Garden Supplies",
    "TrackQtyOnHand": true,
    "UnitPrice": 0,
    "PurchaseCost": 0,
    "QtyOnHand": 10,
    "IncomeAccountRef": {
      "name": "Sales of Product Income",
      "value": "79"
    },
    "AssetAccountRef": {
      "name": "Inventory Asset",
      "value": "81"
    },
    "Taxable": false,
    "sparse": false,
    "Active": true,
    "SyncToken": "0",
    "InvStartDate": "2015-01-01",
    "Type": "Inventory",
    "ExpenseAccountRef": {
      "name": "Cost of Goods Sold",
      "value": "80"
    },
    "MetaData": {
      "CreateTime": "2015-12-09T11:12:39-08:00",
      "LastUpdatedTime": "2015-12-09T11:12:41-08:00"
    }
  },
  "time": "2015-12-09T11:12:39.748-08:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-12-09T11:19:56.688-08:00">
  <Item domain="QBO" sparse="false">
    <Id>19</Id>
    <SyncToken>0</SyncToken>
    <MetaData>
      <CreateTime>2015-12-09T11:19:56-08:00</CreateTime>
      <LastUpdatedTime>2015-12-09T11:19:57-08:00</LastUpdatedTime>
    </MetaData>
    <Name>Kitchen Supplies</Name>
    <Active>true</Active>
    <FullyQualifiedName>Kitchen Supplies</FullyQualifiedName>
    <Taxable>false</Taxable>
    <UnitPrice>0</UnitPrice>
    <Type>Inventory</Type>
    <IncomeAccountRef name="Sales of Product Income">79</IncomeAccountRef>
    <PurchaseDesc>This is the purchasing description.</PurchaseDesc>
    <PurchaseCost>35</PurchaseCost>
    <ExpenseAccountRef name="Cost of Goods Sold">80</ExpenseAccountRef>
    <AssetAccountRef name="Inventory Asset">81</AssetAccountRef>
    <TrackQtyOnHand>true</TrackQtyOnHand>
    <QtyOnHand>10</QtyOnHand>
    <InvStartDate>2015-01-01</InvStartDate>
  </Item>
</IntuitResponse>
```

## Create a category

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/item?minorversion=4`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Request Body

The elements to create a category are listed here.

Schema: `categoryrequest`

<details>
<summary>Show schema for `categoryrequest`</summary>

#### categoryrequest

Model type: `object`

##### `Type`

Required: Required
Type: `String`

Must be set to the literal string, `Category` Available when endpoint is envoked with the `minorversion=4` query paramter. Without `minorversion=4`, the type is set to `Service`.

##### `Name`

Required: Required
Type: `String`
Max length: maximum of 100 chars

Name of the category.

##### `SubItem`

Required: Conditionally required
Type: `Boolean`
Default: <span class="literal">false</span>

`true`--The object is a sub-category. `false`--The object is a top-level category (default). Sub-categories can be nested to a maximum depth of three levels below a top-level category. Required for sub-category.

##### `ParentRef`

Required: Conditionally required
Type: `ReferenceType`

The immediate parent of the sub item in the hierarchical Category:Sub-category list. If SubItem is true, then ParenRef is required. Query the Item name list resource to determine the appropriate object for this reference. Use `Item.Id` and `Item.Name` from that object for `ParentRef.value` and `ParentRef.name`, respectively.

<details>
<summary>Child attributes for `ParentRef`</summary>

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

</details>

#### Example

```json
{
  "SubItem": true,
  "Type": "Category",
  "Name": "Cedar",
  "ParentRef": {
    "name": "Trees",
    "value": "29"
  }
}
```

#### XML example

```text
To be supplied.
```

### Returns

Returns the newly created item object. Categories are only available on companies that have enabled Categories. Test the `CompanyInfo.NameValue.Name.ItemCategoriesFeature` flag:

- `true`— categories are enabled
- `false`— categories are not enabled.

Schema: `categoryresponse`

<details>
<summary>Show schema for `categoryresponse`</summary>

#### categoryresponse

Model type: `object`

##### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

##### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

##### `Level`

Type: `Integer`
Traits: read only, system defined

Specifies the level of the hierarchy in which the object is located. First sub-category level below the top-most category is 1. Returned in the response body only when SubItem is set to `true`. Sub-categories can be nested to a maximum depth of three levels below a top-level category.

##### `FullyQualifiedName`

Type: `String`
Traits: read only, system defined, filterable

Colon-separated list of the top-level category, followed by each sub-category in the hierarchy. Takes the form of `Category:SubCategory1:SubCategory2:...`. Limited to 5 levels: 4 category levels with an inventory, non-inventory, or service item as the 5th.

##### `Name`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

Name of the category.

##### `SubItem`

Required: Optional
Type: `Boolean`

Denotes this object is a sub-category. Returned in the response body if this object is a sub-category. `true`--This is a sub-category. `false`--This is a top-level category (default).

##### `ParentRef`

Required: Optional
Type: `ReferenceType`

Reference to the parent of this sub-category. Returned in the response body only when SubItem is set to `true`. Query the Item name list resource to determine the appropriate object for this reference. Use `Item.Id` and `Item.DisplayName` from that object for `ParentRef.value` and `ParentRef.name`, respectively.

<details>
<summary>Child attributes for `ParentRef`</summary>

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

##### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable

For categories, this is always set to `true`.

##### `Type`

Required: Optional
Type: `String`
Traits: filterable, sortable

Set to the literal string, `Category`. When querying Item objects with minor versions earlier than 4 specified, `Category` types are returned as type `Service`.

##### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the object. The MetaData values are set by Data Services and are read only for all applications.

<details>
<summary>Child attributes for `MetaData`</summary>

###### modificationmetadata

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

</details>

#### Example

```json
{
  "Item": {
    "FullyQualifiedName": "Trees:Cedar",
    "domain": "QBO",
    "Name": "Cedar",
    "Level": 1,
    "sparse": false,
    "SubItem": true,
    "ParentRef": {
      "name": "Trees",
      "value": "29"
    },
    "Active": true,
    "SyncToken": "0",
    "Type": "Category",
    "Id": "30",
    "MetaData": {
      "CreateTime": "2015-10-06T10:50:42-07:00",
      "LastUpdatedTime": "2015-10-06T10:50:42-07:00"
    }
  },
  "time": "2015-10-06T10:50:42.707-07:00"
}
```

#### XML example

```text
To be supplied.
```

## Query a bundle

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>&minorversion=4`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Item where Type='Group'"
```

#### XML example

```text
To be supplied.
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Item": [
      {
        "Sku": "234",
        "FullyQualifiedName": "Deluxe Fountain",
        "domain": "QBO",
        "Name": "Deluxe Fountain",
        "TrackQtyOnHand": false,
        "Type": "Group",
        "PurchaseCost": 0,
        "Taxable": false,
        "ItemGroupDetail": {
          "ItemGroupLine": [
            {
              "Qty": 1,
              "ItemRef": {
                "type": "Inventory",
                "name": "Pump",
                "value": "11"
              }
            },
            {
              "Qty": 1,
              "ItemRef": {
                "type": "Inventory",
                "name": "Rock Fountain",
                "value": "5"
              }
            },
            {
              "Qty": 2,
              "ItemRef": {
                "type": "Service",
                "name": "Lighting",
                "value": "8"
              }
            },
            {
              "Qty": 4,
              "ItemRef": {
                "type": "Service",
                "name": "Installation",
                "value": "7"
              }
            }
          ]
        },
        "sparse": false,
        "Active": true,
        "PrintGroupedItems": true,
        "SyncToken": "1",
        "UnitPrice": 0,
        "Id": "49",
        "MetaData": {
          "CreateTime": "2016-06-23T10:51:32-07:00",
          "LastUpdatedTime": "2016-06-23T10:52:20-07:00"
        }
      }
    ],
    "maxResults": 1
  },
  "time": "2016-06-08T13:59:00.697-07:00"
}
```

#### XML example

```text
To be supplied.
```

## Query a category

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>&minorversion=4`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Item where Type='Category'"
```

#### XML example

```text
To be supplied.
```

### Returns

Returns the results of the query. Categories are only available on companies that have enabled Categories. Test the `CompanyInfo.NameValue.Name.ItemCategoriesFeature` flag:

- `true`— categories are enabled
- `false`— categories are not enabled.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Item": [
      {
        "FullyQualifiedName": "Flowers",
        "domain": "QBO",
        "Name": "Flowers",
        "SyncToken": "1",
        "sparse": false,
        "Active": true,
        "Type": "Category",
        "Id": "20",
        "MetaData": {
          "CreateTime": "2015-09-16T13:03:07-07:00",
          "LastUpdatedTime": "2015-09-16T13:40:51-07:00"
        }
      },
      {
        "FullyQualifiedName": "Flowers:Daises",
        "domain": "QBO",
        "Name": "Daises",
        "Level": 1,
        "sparse": false,
        "SubItem": true,
        "ParentRef": {
          "name": "Flowers",
          "value": "20"
        },
        "Active": true,
        "SyncToken": "0",
        "Type": "Category",
        "Id": "22",
        "MetaData": {
          "CreateTime": "2015-09-16T13:16:41-07:00",
          "LastUpdatedTime": "2015-09-16T13:31:46-07:00"
        }
      },
      {
        "FullyQualifiedName": "Flowers:Roses",
        "domain": "QBO",
        "Name": "Roses",
        "Level": 1,
        "sparse": false,
        "SubItem": true,
        "ParentRef": {
          "name": "Flowers",
          "value": "20"
        },
        "Active": true,
        "SyncToken": "0",
        "Type": "Category",
        "Id": "21",
        "MetaData": {
          "CreateTime": "2015-09-16T13:14:11-07:00",
          "LastUpdatedTime": "2015-09-16T13:14:11-07:00"
        }
      },
      {
        "FullyQualifiedName": "Garden Supplies",
        "domain": "QBO",
        "Name": "Garden Supplies",
        "SyncToken": "0",
        "sparse": false,
        "Active": true,
        "Type": "Category",
        "Id": "19",
        "MetaData": {
          "CreateTime": "2015-09-16T13:02:07-07:00",
          "LastUpdatedTime": "2015-09-16T13:02:07-07:00"
        }
      },
      {
        "FullyQualifiedName": "Organic Fir",
        "domain": "QBO",
        "Name": "Organic Fir",
        "SyncToken": "2",
        "sparse": false,
        "Active": true,
        "Type": "Category",
        "Id": "34",
        "MetaData": {
          "CreateTime": "2015-10-07T12:43:54-07:00",
          "LastUpdatedTime": "2015-10-07T12:48:23-07:00"
        }
      },
      {
        "FullyQualifiedName": "Organic Trees",
        "domain": "QBO",
        "Name": "Organic Trees",
        "SyncToken": "2",
        "sparse": false,
        "Active": true,
        "Type": "Category",
        "Id": "29",
        "MetaData": {
          "CreateTime": "2015-10-06T08:50:34-07:00",
          "LastUpdatedTime": "2015-10-07T12:48:23-07:00"
        }
      },
      {
        "FullyQualifiedName": "Organic Trees:Cedar",
        "domain": "QBO",
        "Name": "Cedar",
        "Level": 1,
        "sparse": false,
        "SubItem": true,
        "ParentRef": {
          "name": "Organic Trees",
          "value": "29"
        },
        "Active": true,
        "SyncToken": "0",
        "Type": "Category",
        "Id": "30",
        "MetaData": {
          "CreateTime": "2015-10-06T10:50:42-07:00",
          "LastUpdatedTime": "2015-10-07T12:38:03-07:00"
        }
      },
      {
        "FullyQualifiedName": "Organic Trees:Fig",
        "domain": "QBO",
        "Name": "Fig",
        "Level": 1,
        "sparse": false,
        "SubItem": true,
        "ParentRef": {
          "name": "Organic Trees",
          "value": "29"
        },
        "Active": true,
        "SyncToken": "0",
        "Type": "Category",
        "Id": "31",
        "MetaData": {
          "CreateTime": "2015-10-06T11:07:23-07:00",
          "LastUpdatedTime": "2015-10-07T12:38:03-07:00"
        }
      }
    ],
    "maxResults": 8
  },
  "time": "2015-10-08T13:59:00.697-07:00"
}
```

#### XML example

```text
To be supplied.
```

## Query an item

### Definition

- **Content type:** `text/plain`
- **Operation:** `GET /v3/company/<realmID>/query?query=<selectStatement>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

### Sample Query

#### Example

```sql
"select * from Item maxresults 2"
```

#### XML example

```sql
select * from Item maxresults 2
```

### Returns

Returns the results of the query.

#### Example

```json
{
  "QueryResponse": {
    "startPosition": 1,
    "Item": [
      {
        "FullyQualifiedName": "Concrete",
        "domain": "QBO",
        "Name": "Concrete",
        "TrackQtyOnHand": false,
        "Type": "Service",
        "PurchaseCost": 0,
        "IncomeAccountRef": {
          "name": "Landscaping Services:Job Materials:Fountains and Garden Lighting",
          "value": "48"
        },
        "Taxable": true,
        "MetaData": {
          "CreateTime": "2014-09-16T10:36:03-07:00",
          "LastUpdatedTime": "2014-09-19T12:47:47-07:00"
        },
        "sparse": false,
        "Active": true,
        "SyncToken": "1",
        "UnitPrice": 0,
        "Id": "3",
        "Description": "Concrete for fountain installation"
      },
      {
        "FullyQualifiedName": "Design",
        "domain": "QBO",
        "Name": "Design",
        "TrackQtyOnHand": false,
        "Type": "Service",
        "PurchaseCost": 0,
        "IncomeAccountRef": {
          "name": "Design income",
          "value": "82"
        },
        "Taxable": false,
        "MetaData": {
          "CreateTime": "2014-09-16T10:41:38-07:00",
          "LastUpdatedTime": "2015-04-17T14:31:10-07:00"
        },
        "sparse": false,
        "Active": true,
        "SyncToken": "1",
        "UnitPrice": 75,
        "Id": "4",
        "Description": "Custom Design"
      }
    ],
    "maxResults": 2
  },
  "time": "2015-04-22T11:04:34.194-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T14:52:37.614-07:00">
    <QueryResponse startPosition="1" maxResults="2">
        <Item domain="QBO" sparse="false">
            <Id>3</Id>
            <SyncToken>1</SyncToken>
            <MetaData>
                <CreateTime>2014-09-16T10:36:03-07:00</CreateTime>
                <LastUpdatedTime>2014-09-19T12:47:47-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Concrete</Name>
            <Description>Concrete for fountain installation</Description>
            <Active>true</Active>
            <FullyQualifiedName>Concrete</FullyQualifiedName>
            <Taxable>true</Taxable>
            <UnitPrice>0</UnitPrice>
            <Type>Service</Type>
            <IncomeAccountRef name="Landscaping Services:Job Materials:Fountains and Garden Lighting">48</IncomeAccountRef>
            <PurchaseCost>0</PurchaseCost>
            <TrackQtyOnHand>false</TrackQtyOnHand>
        </Item>
        <Item domain="QBO" sparse="false">
            <Id>4</Id>
            <SyncToken>1</SyncToken>
            <MetaData>
                <CreateTime>2014-09-16T10:41:38-07:00</CreateTime>
                <LastUpdatedTime>2015-04-17T14:31:10-07:00</LastUpdatedTime>
            </MetaData>
            <Name>Design</Name>
            <Description>Custom Design</Description>
            <Active>true</Active>
            <FullyQualifiedName>Design</FullyQualifiedName>
            <Taxable>false</Taxable>
            <UnitPrice>75</UnitPrice>
            <Type>Service</Type>
            <IncomeAccountRef name="Design income">82</IncomeAccountRef>
            <PurchaseCost>0</PurchaseCost>
            <TrackQtyOnHand>false</TrackQtyOnHand>
        </Item>
    </QueryResponse>
</IntuitResponse>
```

## Read a bundle

### Definition

- **Operation:** `GET /v3/company/<realmID>/item/<itemId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a item bundle object that has been previously created.

### Returns

Returns the bundle object.

#### Example

```json
{
  "Item": {
    "Sku": "234",
    "FullyQualifiedName": "Deluxe Fountain",
    "domain": "QBO",
    "Name": "Deluxe Fountain",
    "TrackQtyOnHand": false,
    "Type": "Group",
    "PurchaseCost": 0,
    "Taxable": false,
    "ItemGroupDetail": {
      "ItemGroupLine": [
        {
          "Qty": 1,
          "ItemRef": {
            "type": "Inventory",
            "name": "Pump",
            "value": "11"
          }
        },
        {
          "Qty": 1,
          "ItemRef": {
            "type": "Inventory",
            "name": "Rock Fountain",
            "value": "5"
          }
        },
        {
          "Qty": 2,
          "ItemRef": {
            "type": "Service",
            "name": "Lighting",
            "value": "8"
          }
        },
        {
          "Qty": 4,
          "ItemRef": {
            "type": "Service",
            "name": "Installation",
            "value": "7"
          }
        }
      ]
    },
    "sparse": false,
    "Active": true,
    "PrintGroupedItems": true,
    "SyncToken": "1",
    "UnitPrice": 0,
    "Id": "49",
    "MetaData": {
      "CreateTime": "2016-06-23T10:51:32-07:00",
      "LastUpdatedTime": "2016-06-23T10:52:20-07:00"
    }
  },
  "time": "2016-06-23T15:14:21.695-07:00"
}
```

#### XML example

```text
To be supplied.
```

## Read a category

### Definition

- **Operation:** `GET /v3/company/<realmID>/item/<itemId>?minorversion=4`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a item object that has been previously created.

### Returns

Returns the category object.Categories are only available on companies that have enabled Categories. Test the `CompanyInfo.NameValue.Name.ItemCategoriesFeature` flag:

- `true`— categories are enabled
- `false`— categories are not enabled.

#### Example

```json
{
  "Item": {
    "FullyQualifiedName": "Trees",
    "domain": "QBO",
    "Name": "Trees",
    "SyncToken": "0",
    "sparse": false,
    "Active": true,
    "Type": "Category",
    "Id": "29",
    "MetaData": {
      "CreateTime": "2015-10-06T08:50:34-07:00",
      "LastUpdatedTime": "2015-10-06T08:50:34-07:00"
    }
  },
  "time": "2015-10-06T08:50:34.863-07:00"
}
```

#### XML example

```text
To be supplied.
```

## Read an item

### Definition

- **Operation:** `GET /v3/company/<realmID>/item/<itemId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a item object that has been previously created.

### Returns

Returns the item object.

#### Example

```json
{
  "Item": {
    "FullyQualifiedName": "Office Supplies",
    "domain": "QBO",
    "Id": "37",
    "Name": "Office Supplies",
    "TrackQtyOnHand": true,
    "Type": "Inventory",
    "PurchaseCost": 35,
    "QtyOnHand": 10,
    "IncomeAccountRef": {
      "name": "Sales of Product Income",
      "value": "79"
    },
    "AssetAccountRef": {
      "name": "Inventory Asset",
      "value": "81"
    },
    "Taxable": true,
    "MetaData": {
      "CreateTime": "2015-04-22T11:03:23-07:00",
      "LastUpdatedTime": "2015-04-22T11:03:24-07:00"
    },
    "sparse": false,
    "Active": true,
    "SyncToken": "0",
    "InvStartDate": "2013-02-19",
    "UnitPrice": 25,
    "ExpenseAccountRef": {
      "name": "Cost of Goods Sold",
      "value": "80"
    },
    "PurchaseDesc": "This is the purchasing description.",
    "Description": "This is the sales description."
  },
  "time": "2015-04-22T11:01:37.346-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T14:53:46.341-07:00">
  <Item domain="QBO" sparse="false">
    <Id>37</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2015-04-22T11:03:23-07:00</CreateTime>
      <LastUpdatedTime>2015-04-22T11:05:08-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Office Supplies</Name>
    <Description>This is a new, updated sales description.</Description>
    <Active>true</Active>
    <FullyQualifiedName>Office Supplies</FullyQualifiedName>
    <Taxable>true</Taxable>
    <UnitPrice>25</UnitPrice>
    <Type>Inventory</Type>
    <IncomeAccountRef name="Sales of Product Income">79</IncomeAccountRef>
    <PurchaseDesc>This is the purchasing description.</PurchaseDesc>
    <PurchaseCost>35</PurchaseCost>
    <ExpenseAccountRef name="Cost of Goods Sold">80</ExpenseAccountRef>
    <AssetAccountRef name="Inventory Asset">81</AssetAccountRef>
    <TrackQtyOnHand>true</TrackQtyOnHand>
    <QtyOnHand>10</QtyOnHand>
    <InvStartDate>2013-02-19</InvStartDate>
  </Item>
</IntuitResponse>
```

## Full update an item

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/item`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing item object. The request body must include all writable fields of the existing object as returned in a read response. Writable fields omitted from the request body are set to NULL. The ID of the object to update is specified in the request body.Add the query parameter, `include=donotupdateaccountontxns&minorversion=5`, to the endpoint to supress updating the income or expense account on any existing transactions associated with this Item object. Updates on soft closed transacitons will fail.

### Request Body

Schema: `itemresponse`

_Matches the top-level sample object schema._

#### Example

```json
{
  "FullyQualifiedName": "Rock Fountain",
  "domain": "QBO",
  "Id": "5",
  "Name": "Rock Fountain",
  "TrackQtyOnHand": true,
  "Type": "Inventory",
  "PurchaseCost": 125,
  "QtyOnHand": 2,
  "IncomeAccountRef": {
    "name": "Sales of Product Income",
    "value": "79"
  },
  "AssetAccountRef": {
    "name": "Inventory Asset",
    "value": "81"
  },
  "Taxable": true,
  "MetaData": {
    "CreateTime": "2014-09-16T10:42:19-07:00",
    "LastUpdatedTime": "2014-09-19T13:16:17-07:00"
  },
  "sparse": false,
  "Active": true,
  "SyncToken": "2",
  "InvStartDate": "2014-09-19",
  "UnitPrice": 275,
  "ExpenseAccountRef": {
    "name": "Cost of Goods Sold",
    "value": "80"
  },
  "PurchaseDesc": "Rock Fountain",
  "Description": "New, updated description for Rock Fountain"
}
```

#### XML example

```xml
<Item xmlns="http://schema.intuit.com/finance/v3" sparse="false">
    <Id>37</Id>
    <SyncToken>1</SyncToken>
    <MetaData>
      <CreateTime>2015-04-22T11:03:23-07:00</CreateTime>
      <LastUpdatedTime>2015-04-22T11:05:08-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Office Supplies</Name>
    <Description>This is a second, updated sales description.</Description>
    <Active>true</Active>
    <FullyQualifiedName>Office Supplies</FullyQualifiedName>
    <Taxable>true</Taxable>
    <UnitPrice>25</UnitPrice>
    <Type>Inventory</Type>
    <IncomeAccountRef name="Sales of Product Income">79</IncomeAccountRef>
    <PurchaseDesc>This is the purchasing description.</PurchaseDesc>
    <PurchaseCost>35</PurchaseCost>
    <ExpenseAccountRef name="Cost of Goods Sold">80</ExpenseAccountRef>
    <AssetAccountRef name="Inventory Asset">81</AssetAccountRef>
    <TrackQtyOnHand>true</TrackQtyOnHand>
    <QtyOnHand>10</QtyOnHand>
    <InvStartDate>2013-02-19</InvStartDate>
</Item>
```

### Returns

The item response body.

#### Example

```json
{
  "Item": {
    "FullyQualifiedName": "Rock Fountain",
    "domain": "QBO",
    "Id": "5",
    "Name": "Rock Fountain",
    "TrackQtyOnHand": true,
    "Type": "Inventory",
    "PurchaseCost": 125,
    "QtyOnHand": 2,
    "IncomeAccountRef": {
      "name": "Sales of Product Income",
      "value": "79"
    },
    "AssetAccountRef": {
      "name": "Inventory Asset",
      "value": "81"
    },
    "Taxable": true,
    "MetaData": {
      "CreateTime": "2014-09-16T10:42:19-07:00",
      "LastUpdatedTime": "2015-04-22T11:10:18-07:00"
    },
    "sparse": false,
    "Active": true,
    "SyncToken": "3",
    "InvStartDate": "2014-09-19",
    "UnitPrice": 275,
    "ExpenseAccountRef": {
      "name": "Cost of Goods Sold",
      "value": "80"
    },
    "PurchaseDesc": "Rock Fountain",
    "Description": "New, updated description for Rock Fountain"
  },
  "time": "2015-04-22T11:08:31.596-07:00"
}
```

#### XML example

```xml
<IntuitResponse xmlns="http://schema.intuit.com/finance/v3" time="2015-07-24T14:55:06.451-07:00">
  <Item domain="QBO" sparse="false">
    <Id>37</Id>
    <SyncToken>2</SyncToken>
    <MetaData>
      <CreateTime>2015-04-22T11:03:23-07:00</CreateTime>
      <LastUpdatedTime>2015-07-24T14:55:06-07:00</LastUpdatedTime>
    </MetaData>
    <Name>Office Supplies</Name>
    <Description>This is a second, updated sales description.</Description>
    <Active>true</Active>
    <FullyQualifiedName>Office Supplies</FullyQualifiedName>
    <Taxable>true</Taxable>
    <UnitPrice>25</UnitPrice>
    <Type>Inventory</Type>
    <IncomeAccountRef name="Sales of Product Income">79</IncomeAccountRef>
    <PurchaseDesc>This is the purchasing description.</PurchaseDesc>
    <PurchaseCost>35</PurchaseCost>
    <ExpenseAccountRef name="Cost of Goods Sold">80</ExpenseAccountRef>
    <AssetAccountRef name="Inventory Asset">81</AssetAccountRef>
    <TrackQtyOnHand>true</TrackQtyOnHand>
    <QtyOnHand>10</QtyOnHand>
    <InvStartDate>2013-02-19</InvStartDate>
  </Item>
</IntuitResponse>
```

## Update a category

### Definition

- **Content type:** `application/json`
- **Operation:** `POST /v3/company/<realmID>/item?minorversion=4`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Use this operation to update any of the writable fields of an existing category object. The ID of the object to update is specified in the request body.

### Request Body

Schema: `categoryupdaterequest`

<details>
<summary>Show schema for `categoryupdaterequest`</summary>

#### categoryupdaterequest

Model type: `object`

##### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

##### `Name`

Required: Required
Type: `String`
Max length: maximum of 100 chars

Name of the category.

##### `Type`

Required: Required
Type: `String`

Must be set to the literal string, `Category` Available when endpoint is envoked with the `minorversion=4` query paramter. Without `minorversion=4`, the type is set to `Service`.

##### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

##### `SubItem`

Required: Conditionally required
Type: `Boolean`

`true`--The object is a sub-category. `false`--The object is a top-level category (default). Sub-categories can be nested to a maximum depth of three levels below a top-level category. Required if this is a sub-category object.

##### `Level`

Type: `Integer`
Traits: read only, system defined

Specifies the level of the hierarchy in which the object is located. First sub-category level below the top-most category is 1. Returned in the response body only when SubItem is set to `true`. Sub-categories can be nested to a maximum depth of three levels below a top-level category.

##### `FullyQualifiedName`

Type: `String`
Traits: read only, system defined

Colon-separated list of the top-level category, followed by each sub-category in the hierarchy. Takes the form of `Category:SubCategory1:SubCategory2:...`. Limited to 5 levels: 4 category levels with an inventory, non-inventory, or service item as the 5th.

##### `ParentRef`

Type: `ReferenceType`

The immediate parent of the sub item in the hierarchical Category:Sub-category list. If SubItem is true, then ParenRef is required. Query the Item name list resource to determine the appropriate object for this reference. Use `Item.Id` and `Item.Name` from that object for `ParentRef.value` and `ParentRef.name`, respectively.

<details>
<summary>Child attributes for `ParentRef`</summary>

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

##### `Active`

Required: Optional
Type: `Boolean`

For categories, this is always set to `true`.

##### `MetaData`

Required: Optional
Type: `ModificationMetaData`
Traits: system defined

Descriptive information about the entity. The MetaData values are set by Data Services and are read only for all applications.

<details>
<summary>Child attributes for `MetaData`</summary>

###### modificationmetadata

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

</details>

#### Example

```json
{
  "SyncToken": "1",
  "domain": "QBO",
  "Name": "Trees",
  "sparse": false,
  "Type": "Category",
  "Id": "29"
}
```

#### XML example

```text
To be supplied.
```

### Returns

The item response body. Categories are only available on companies that have enabled Categories. Test the `CompanyInfo.NameValue.Name.ItemCategoriesFeature` flag:

- `true`— categories are enabled
- `false`— categories are not enabled.

Schema: `categoryresponse`

<details>
<summary>Show schema for `categoryresponse`</summary>

#### categoryresponse

Model type: `object`

##### `Id`

Required: Required for update
Type: `String`
Traits: read only, system defined, filterable, sortable

Unique identifier for this object. Sort order is ASC by default.

##### `SyncToken`

Required: Required for update
Type: `String`
Traits: read only, system defined

Version number of the object. It is used to lock an object for use by one app at a time. As soon as an application modifies an object, its `SyncToken` is incremented. Attempts to modify an object specifying an older `SyncToken` fails. Only the latest version of the object is maintained by QuickBooks Online.

##### `Level`

Type: `Integer`
Traits: read only, system defined

Specifies the level of the hierarchy in which the object is located. First sub-category level below the top-most category is 1. Returned in the response body only when SubItem is set to `true`. Sub-categories can be nested to a maximum depth of three levels below a top-level category.

##### `FullyQualifiedName`

Type: `String`
Traits: read only, system defined, filterable

Colon-separated list of the top-level category, followed by each sub-category in the hierarchy. Takes the form of `Category:SubCategory1:SubCategory2:...`. Limited to 5 levels: 4 category levels with an inventory, non-inventory, or service item as the 5th.

##### `Name`

Required: Optional
Type: `String`
Max length: maximum of 100 chars

Name of the category.

##### `SubItem`

Required: Optional
Type: `Boolean`

Denotes this object is a sub-category. Returned in the response body if this object is a sub-category. `true`--This is a sub-category. `false`--This is a top-level category (default).

##### `ParentRef`

Required: Optional
Type: `ReferenceType`

Reference to the parent of this sub-category. Returned in the response body only when SubItem is set to `true`. Query the Item name list resource to determine the appropriate object for this reference. Use `Item.Id` and `Item.DisplayName` from that object for `ParentRef.value` and `ParentRef.name`, respectively.

<details>
<summary>Child attributes for `ParentRef`</summary>

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

##### `Active`

Required: Optional
Type: `Boolean`
Traits: filterable

For categories, this is always set to `true`.

##### `Type`

Required: Optional
Type: `String`
Traits: filterable, sortable

Set to the literal string, `Category`. When querying Item objects with minor versions earlier than 4 specified, `Category` types are returned as type `Service`.

##### `MetaData`

Required: Optional
Type: `ModificationMetaData`

Descriptive information about the object. The MetaData values are set by Data Services and are read only for all applications.

<details>
<summary>Child attributes for `MetaData`</summary>

###### modificationmetadata

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

</details>

#### Example

```json
{
  "Item": {
    "FullyQualifiedName": "Organic Trees",
    "domain": "QBO",
    "Name": "Organic Trees",
    "SyncToken": "2",
    "sparse": false,
    "Active": true,
    "Type": "Category",
    "Id": "29",
    "MetaData": {
      "CreateTime": "2015-10-06T08:50:34-07:00",
      "LastUpdatedTime": "2015-10-07T12:38:03-07:00"
    }
  },
  "time": "2015-10-07T12:40:29.199-07:00"
}
```

#### XML example

```text
To be supplied.
```
