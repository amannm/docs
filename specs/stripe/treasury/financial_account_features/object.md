# The FinancialAccount Feature object

## Attributes

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `card_issuing` (object, nullable)
  Contains a Feature encoding the FinancialAccount’s ability to be used with the Issuing product, including attaching cards to and drawing funds from.

  - `card_issuing.requested` (boolean)
    Whether the FinancialAccount should have the Feature.

  - `card_issuing.status` (enum)
    Whether the Feature is operational.
Possible enum values:
    - `active`
      Indicates that the Feature might be used.

    - `pending`
      Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

    - `restricted`
      Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

  - `card_issuing.status_details` (array of objects)
    Additional details; includes at least one entry when the status is not `active`.

    - `card_issuing.status_details.code` (enum)
      Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
      - `activating`
        This Feature has met all other requirements and Stripe is in the process of making it active.

      - `capability_not_requested`
        The user hasn’t requested required capabilities to activate this Feature.

      - `financial_account_closed`
        The FinancialAccount that this Feature is attached to is closed.

      - `rejected_other`
        The FinancialAccount is never allowed to use this Feature.

      - `rejected_unsupported_business`
        The user’s business isn’t supported by this Feature.

      - `requirements_past_due`
        Onboarding requirements needed to activate this Feature.

      - `requirements_pending_verification`
        Stripe is in the process of verifying the user.

      - `restricted_by_platform`
        Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

      - `restricted_other`
        The FinancialAccount isn’t currently allowed to use this Feature.

    - `card_issuing.status_details.resolution` (enum, nullable)
      Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
      - `contact_stripe`
        The user should contact Stripe via support.stripe.com.

      - `provide_information`
        The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

      - `remove_restriction`
        The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

    - `card_issuing.status_details.restriction` (enum, nullable)
      The `platform_restrictions` that are restricting this Feature.
Possible enum values:
      - `inbound_flows`
        Restricts all inbound money movement.

      - `outbound_flows`
        Restricts all outbound money movement.

- `deposit_insurance` (object, nullable)
  Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.

  - `deposit_insurance.requested` (boolean)
    Whether the FinancialAccount should have the Feature.

  - `deposit_insurance.status` (enum)
    Whether the Feature is operational.
Possible enum values:
    - `active`
      Indicates that the Feature might be used.

    - `pending`
      Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

    - `restricted`
      Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

  - `deposit_insurance.status_details` (array of objects)
    Additional details; includes at least one entry when the status is not `active`.

    - `deposit_insurance.status_details.code` (enum)
      Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
      - `activating`
        This Feature has met all other requirements and Stripe is in the process of making it active.

      - `capability_not_requested`
        The user hasn’t requested required capabilities to activate this Feature.

      - `financial_account_closed`
        The FinancialAccount that this Feature is attached to is closed.

      - `rejected_other`
        The FinancialAccount is never allowed to use this Feature.

      - `rejected_unsupported_business`
        The user’s business isn’t supported by this Feature.

      - `requirements_past_due`
        Onboarding requirements needed to activate this Feature.

      - `requirements_pending_verification`
        Stripe is in the process of verifying the user.

      - `restricted_by_platform`
        Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

      - `restricted_other`
        The FinancialAccount isn’t currently allowed to use this Feature.

    - `deposit_insurance.status_details.resolution` (enum, nullable)
      Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
      - `contact_stripe`
        The user should contact Stripe via support.stripe.com.

      - `provide_information`
        The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

      - `remove_restriction`
        The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

    - `deposit_insurance.status_details.restriction` (enum, nullable)
      The `platform_restrictions` that are restricting this Feature.
Possible enum values:
      - `inbound_flows`
        Restricts all inbound money movement.

      - `outbound_flows`
        Restricts all outbound money movement.

- `financial_addresses` (object, nullable)
  Contains Features that add FinancialAddresses to the FinancialAccount.

  - `financial_addresses.aba` (object, nullable)
    Adds an ABA FinancialAddress to the FinancialAccount.

    - `financial_addresses.aba.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `financial_addresses.aba.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `financial_addresses.aba.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `financial_addresses.aba.status_details.code` (enum)
        Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
        - `activating`
          This Feature has met all other requirements and Stripe is in the process of making it active.

        - `capability_not_requested`
          The user hasn’t requested required capabilities to activate this Feature.

        - `financial_account_closed`
          The FinancialAccount that this Feature is attached to is closed.

        - `rejected_other`
          The FinancialAccount is never allowed to use this Feature.

        - `rejected_unsupported_business`
          The user’s business isn’t supported by this Feature.

        - `requirements_past_due`
          Onboarding requirements needed to activate this Feature.

        - `requirements_pending_verification`
          Stripe is in the process of verifying the user.

        - `restricted_by_platform`
          Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

        - `restricted_other`
          The FinancialAccount isn’t currently allowed to use this Feature.

      - `financial_addresses.aba.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `financial_addresses.aba.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

- `inbound_transfers` (object, nullable)
  Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.

  - `inbound_transfers.ach` (object, nullable)
    Enables ACH Debits via the InboundTransfers API.

    - `inbound_transfers.ach.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `inbound_transfers.ach.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `inbound_transfers.ach.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `inbound_transfers.ach.status_details.code` (enum)
        Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
        - `activating`
          This Feature has met all other requirements and Stripe is in the process of making it active.

        - `capability_not_requested`
          The user hasn’t requested required capabilities to activate this Feature.

        - `financial_account_closed`
          The FinancialAccount that this Feature is attached to is closed.

        - `rejected_other`
          The FinancialAccount is never allowed to use this Feature.

        - `rejected_unsupported_business`
          The user’s business isn’t supported by this Feature.

        - `requirements_past_due`
          Onboarding requirements needed to activate this Feature.

        - `requirements_pending_verification`
          Stripe is in the process of verifying the user.

        - `restricted_by_platform`
          Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

        - `restricted_other`
          The FinancialAccount isn’t currently allowed to use this Feature.

      - `inbound_transfers.ach.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `inbound_transfers.ach.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

- `intra_stripe_flows` (object, nullable)
  Represents the ability for this FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).

  - `intra_stripe_flows.requested` (boolean)
    Whether the FinancialAccount should have the Feature.

  - `intra_stripe_flows.status` (enum)
    Whether the Feature is operational.
Possible enum values:
    - `active`
      Indicates that the Feature might be used.

    - `pending`
      Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

    - `restricted`
      Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

  - `intra_stripe_flows.status_details` (array of objects)
    Additional details; includes at least one entry when the status is not `active`.

    - `intra_stripe_flows.status_details.code` (enum)
      Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
      - `activating`
        This Feature has met all other requirements and Stripe is in the process of making it active.

      - `capability_not_requested`
        The user hasn’t requested required capabilities to activate this Feature.

      - `financial_account_closed`
        The FinancialAccount that this Feature is attached to is closed.

      - `rejected_other`
        The FinancialAccount is never allowed to use this Feature.

      - `rejected_unsupported_business`
        The user’s business isn’t supported by this Feature.

      - `requirements_past_due`
        Onboarding requirements needed to activate this Feature.

      - `requirements_pending_verification`
        Stripe is in the process of verifying the user.

      - `restricted_by_platform`
        Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

      - `restricted_other`
        The FinancialAccount isn’t currently allowed to use this Feature.

    - `intra_stripe_flows.status_details.resolution` (enum, nullable)
      Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
      - `contact_stripe`
        The user should contact Stripe via support.stripe.com.

      - `provide_information`
        The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

      - `remove_restriction`
        The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

    - `intra_stripe_flows.status_details.restriction` (enum, nullable)
      The `platform_restrictions` that are restricting this Feature.
Possible enum values:
      - `inbound_flows`
        Restricts all inbound money movement.

      - `outbound_flows`
        Restricts all outbound money movement.

- `outbound_payments` (object, nullable)
  Contains Features related to initiating money movement out of the FinancialAccount to someone else’s bucket of money.

  - `outbound_payments.ach` (object, nullable)
    Enables ACH transfers via the OutboundPayments API.

    - `outbound_payments.ach.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `outbound_payments.ach.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `outbound_payments.ach.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `outbound_payments.ach.status_details.code` (enum)
        Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
        - `activating`
          This Feature has met all other requirements and Stripe is in the process of making it active.

        - `capability_not_requested`
          The user hasn’t requested required capabilities to activate this Feature.

        - `financial_account_closed`
          The FinancialAccount that this Feature is attached to is closed.

        - `rejected_other`
          The FinancialAccount is never allowed to use this Feature.

        - `rejected_unsupported_business`
          The user’s business isn’t supported by this Feature.

        - `requirements_past_due`
          Onboarding requirements needed to activate this Feature.

        - `requirements_pending_verification`
          Stripe is in the process of verifying the user.

        - `restricted_by_platform`
          Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

        - `restricted_other`
          The FinancialAccount isn’t currently allowed to use this Feature.

      - `outbound_payments.ach.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `outbound_payments.ach.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

  - `outbound_payments.us_domestic_wire` (object, nullable)
    Enables US domestic wire transfers via the OutboundPayments API.

    - `outbound_payments.us_domestic_wire.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `outbound_payments.us_domestic_wire.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `outbound_payments.us_domestic_wire.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `outbound_payments.us_domestic_wire.status_details.code` (enum)
        Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
        - `activating`
          This Feature has met all other requirements and Stripe is in the process of making it active.

        - `capability_not_requested`
          The user hasn’t requested required capabilities to activate this Feature.

        - `financial_account_closed`
          The FinancialAccount that this Feature is attached to is closed.

        - `rejected_other`
          The FinancialAccount is never allowed to use this Feature.

        - `rejected_unsupported_business`
          The user’s business isn’t supported by this Feature.

        - `requirements_past_due`
          Onboarding requirements needed to activate this Feature.

        - `requirements_pending_verification`
          Stripe is in the process of verifying the user.

        - `restricted_by_platform`
          Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

        - `restricted_other`
          The FinancialAccount isn’t currently allowed to use this Feature.

      - `outbound_payments.us_domestic_wire.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `outbound_payments.us_domestic_wire.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

- `outbound_transfers` (object, nullable)
  Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.

  - `outbound_transfers.ach` (object, nullable)
    Enables ACH transfers via the OutboundTransfers API.

    - `outbound_transfers.ach.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `outbound_transfers.ach.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `outbound_transfers.ach.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `outbound_transfers.ach.status_details.code` (enum)
        Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
        - `activating`
          This Feature has met all other requirements and Stripe is in the process of making it active.

        - `capability_not_requested`
          The user hasn’t requested required capabilities to activate this Feature.

        - `financial_account_closed`
          The FinancialAccount that this Feature is attached to is closed.

        - `rejected_other`
          The FinancialAccount is never allowed to use this Feature.

        - `rejected_unsupported_business`
          The user’s business isn’t supported by this Feature.

        - `requirements_past_due`
          Onboarding requirements needed to activate this Feature.

        - `requirements_pending_verification`
          Stripe is in the process of verifying the user.

        - `restricted_by_platform`
          Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

        - `restricted_other`
          The FinancialAccount isn’t currently allowed to use this Feature.

      - `outbound_transfers.ach.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `outbound_transfers.ach.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

  - `outbound_transfers.us_domestic_wire` (object, nullable)
    Enables US domestic wire transfers via the OutboundTransfers API.

    - `outbound_transfers.us_domestic_wire.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `outbound_transfers.us_domestic_wire.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `outbound_transfers.us_domestic_wire.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `outbound_transfers.us_domestic_wire.status_details.code` (enum)
        Represents the reason why the status is `pending` or `restricted`.
Possible enum values:
        - `activating`
          This Feature has met all other requirements and Stripe is in the process of making it active.

        - `capability_not_requested`
          The user hasn’t requested required capabilities to activate this Feature.

        - `financial_account_closed`
          The FinancialAccount that this Feature is attached to is closed.

        - `rejected_other`
          The FinancialAccount is never allowed to use this Feature.

        - `rejected_unsupported_business`
          The user’s business isn’t supported by this Feature.

        - `requirements_past_due`
          Onboarding requirements needed to activate this Feature.

        - `requirements_pending_verification`
          Stripe is in the process of verifying the user.

        - `restricted_by_platform`
          Some or all functionality of this Feature has been restricted by the platform via FinancialAccount `platform_restritions`.

        - `restricted_other`
          The FinancialAccount isn’t currently allowed to use this Feature.

      - `outbound_transfers.us_domestic_wire.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `outbound_transfers.us_domestic_wire.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

### The FinancialAccount Feature object

```json
{
  "object": "treasury.financial_account_features",
  "card_issuing": {
    "requested": true,
    "status": "active",
    "status_details": []
  },
  "deposit_insurance": {
    "requested": true,
    "status": "active",
    "status_details": []
  },
  "financial_addresses": {
    "aba": {
      "requested": true,
      "status": "active",
      "status_details": []
    }
  },
  "inbound_transfers": {
    "ach": {
      "requested": true,
      "status": "active",
      "status_details": []
    }
  },
  "intra_stripe_flows": {
    "requested": true,
    "status": "active",
    "status_details": []
  },
  "outbound_payments": {
    "ach": {
      "requested": true,
      "status": "active",
      "status_details": []
    },
    "us_domestic_wire": {
      "requested": true,
      "status": "active",
      "status_details": []
    }
  },
  "outbound_transfers": {
    "ach": {
      "requested": true,
      "status": "active",
      "status_details": []
    },
    "us_domestic_wire": {
      "requested": true,
      "status": "active",
      "status_details": []
    }
  }
}
```
