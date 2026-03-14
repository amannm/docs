# TaxClassification

> Source: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxclassification
> Breadcrumbs: [QuickBooks Online API](../../index.md) / [Accounting](../index.md) / [All entities](index.md) / TaxClassification
> Canonical entity: `TaxClassification`

Tax classification segregates different items into different classifications and the tax classification is one of the key parameters to determine appropriate tax on transactions involving items. Tax classifications are sourced by either tax governing authorities as in India/Malaysia or externally like Exactor. 'Fuel', 'Garments' and 'Soft drinks' are a few examples of tax classification in layman terms. User can choose a specific tax classification for an item while creating it.

## The taxclassification object

### taxclassification

Model type: `object`

#### `ParentRef`

Required: Required
Type: `ReferenceType`

Reference Type for parent

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

#### `Level`

Type: `String`
Traits: read only, system defined

Tax classification level (Numeric value 1, or 2. 1 specifies parent tax classification)

#### `ApplicableTo`

Required: Optional
Type: `ItemTypeEnum`

List of item types the tax classification is applicable to. Includes Inventory, NonInventory, Bundle and Service.

#### `Code`

Required: Optional
Type: `String`

Code

#### `Name`

Required: Optional
Type: `String`

Name of the tax classification

#### `Description`

Required: Optional
Type: `String`

Description of the tax classification

#### Example

```json
{
  "TaxClassification": {
    "applicableTo": [
      "Inventory",
      "Noninventory"
    ],
    "code": "EUC-01010101",
    "description": "Custom software (developed especially for purchaser) - Licensed (not sold), and delivered on a tangible format, such as on a CD or DVD.",
    "level": "2",
    "ParentRef": {
      "name": "Professional Services",
      "value": "V1-00100000"
    },
    "id": "EUC-01010101-V1-00100000",
    "name": "Tangible, custom software"
  }
}
```

## Read a taxclassification by ID

### Definition

- **Operation:** `GET /v3/company/<realmID>/taxclassification/<taxClassificationId>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a TaxClassification object that has been previously created.

### Returns

Returns the TaxClassification object.

#### Example

```json
{
  "TaxClassification": {
    "applicableTo": [
      "Inventory",
      "Noninventory"
    ],
    "code": "EUC-01010101",
    "description": "Custom software (developed especially for purchaser) - Licensed (not sold), and delivered on a tangible format, such as on a CD or DVD.",
    "level": "2",
    "ParentRef": {
      "name": "Professional Services",
      "value": "V1-00100000"
    },
    "id": "EUC-01010101-V1-00100000",
    "name": "Tangible, custom software"
  }
}
```

## Read a taxclassification by Parent ID

### Definition

- **Operation:** `GET /v3/company/<realmID>/taxclassification/<parentid>/children`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a TaxClassification object by parent ID.

### Returns

Returns the TaxClassification object by parent ID.

#### Example

```json
{
  "QueryResponse": {
    "TaxClassification": [
      {
        "applicableTo": [
          "Inventory",
          "Noninventory"
        ],
        "code": "EUC-01010101",
        "description": "Custom software (developed especially for purchaser) - Licensed (not sold), and delivered on a tangible format, such as on a CD or DVD.",
        "level": "2",
        "ParentRef": {
          "name": "Professional Services",
          "value": "V1-00100000"
        },
        "id": "EUC-01010101-V1-00100000",
        "name": "Tangible, custom software"
      },
      {
        "applicableTo": [
          "Inventory",
          "Noninventory"
        ],
        "code": "EUC-01010201",
        "description": "Canned software (off-the-shelf) - Licensed (not sold) which is delivered in a tangible format, such as on a CD or DVD.",
        "level": "2",
        "ParentRef": {
          "name": "Professional Services",
          "value": "V1-00100000"
        },
        "id": "EUC-01010201-V1-00100000",
        "name": "Tangible, canned software"
      }
    ]
  }
}
```

## Read all taxclassifications

### Definition

- **Operation:** `GET /v3/company/<realmID>/taxclassification`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of all TaxClassification objects that have been previously created.

### Returns

Returns all TaxClassification records

#### Example

```json
{
  "QueryResponse": {
    "TaxClassification": [
      {
        "applicableTo": [
          "Inventory",
          "Noninventory"
        ],
        "code": "EUC-01010101",
        "description": "Custom software (developed especially for purchaser) - Licensed (not sold), and delivered on a tangible format, such as on a CD or DVD.",
        "level": "2",
        "ParentRef": {
          "name": "Professional Services",
          "value": "V1-00100000"
        },
        "id": "EUC-01010101-V1-00100000",
        "name": "Tangible, custom software"
      },
      {
        "applicableTo": [
          "Inventory",
          "Noninventory"
        ],
        "code": "EUC-01010201",
        "description": "Canned software (off-the-shelf) - Licensed (not sold) which is delivered in a tangible format, such as on a CD or DVD.",
        "level": "2",
        "ParentRef": {
          "name": "Professional Services",
          "value": "V1-00100000"
        },
        "id": "EUC-01010201-V1-00100000",
        "name": "Tangible, canned software"
      }
    ]
  }
}
```

## Read taxclassifications by level

### Definition

- **Operation:** `GET /v3/company/<realmID>/taxclassification?level=<level>`
- **Production Base URL:** `https://quickbooks.api.intuit.com`
- **Sandbox Base URL:** `https://sandbox-quickbooks.api.intuit.com`

Retrieves the details of a TaxClassification object that has been previously created by level.

### Returns

Returns the TaxClassification object based on level.

#### Example

```json
{
  "QueryResponse": {
    "TaxClassification": [
      {
        "applicableTo": [
          "Inventory",
          "Noninventory"
        ],
        "code": "EUC-01010101",
        "description": "Custom software (developed especially for purchaser) - Licensed (not sold), and delivered on a tangible format, such as on a CD or DVD.",
        "level": "2",
        "ParentRef": {
          "name": "Professional Services",
          "value": "V1-00100000"
        },
        "id": "EUC-01010101-V1-00100000",
        "name": "Tangible, custom software"
      },
      {
        "applicableTo": [
          "Inventory",
          "Noninventory"
        ],
        "code": "EUC-01010201",
        "description": "Canned software (off-the-shelf) - Licensed (not sold) which is delivered in a tangible format, such as on a CD or DVD.",
        "level": "2",
        "ParentRef": {
          "name": "Professional Services",
          "value": "V1-00100000"
        },
        "id": "EUC-01010201-V1-00100000",
        "name": "Tangible, canned software"
      }
    ]
  }
}
```
