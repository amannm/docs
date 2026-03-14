# The FinancialAccount object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `active_features` (array of enums)
  The array of paths to active Features in the Features hash.

- `balance` (object)
  The single multi-currency balance of the FinancialAccount. Positive values represent money that belongs to the user while negative values represent funds the user owes. Currently, FinancialAccounts can only carry balances in USD.

  - `balance.cash` (object)
    Funds the user can spend right now.

  - `balance.inbound_pending` (object)
    Funds not spendable yet, but will become available at a later time.

  - `balance.outbound_pending` (object)
    Funds in the account, but not spendable because they are being held for pending outbound flows.

- `country` (string)
  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `features` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The features and their statuses for this FinancialAccount.

  - `features.object` (string)
    String representing the object’s type. Objects of the same type share the same value.

  - `features.card_issuing` (object, nullable)
    Contains a Feature encoding the FinancialAccount’s ability to be used with the Issuing product, including attaching cards to and drawing funds from.

    - `features.card_issuing.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `features.card_issuing.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `features.card_issuing.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `features.card_issuing.status_details.code` (enum)
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

      - `features.card_issuing.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `features.card_issuing.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

  - `features.deposit_insurance` (object, nullable)
    Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.

    - `features.deposit_insurance.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `features.deposit_insurance.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `features.deposit_insurance.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `features.deposit_insurance.status_details.code` (enum)
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

      - `features.deposit_insurance.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `features.deposit_insurance.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

  - `features.financial_addresses` (object, nullable)
    Contains Features that add FinancialAddresses to the FinancialAccount.

    - `features.financial_addresses.aba` (object, nullable)
      Adds an ABA FinancialAddress to the FinancialAccount.

      - `features.financial_addresses.aba.requested` (boolean)
        Whether the FinancialAccount should have the Feature.

      - `features.financial_addresses.aba.status` (enum)
        Whether the Feature is operational.
Possible enum values:
        - `active`
          Indicates that the Feature might be used.

        - `pending`
          Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

        - `restricted`
          Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

      - `features.financial_addresses.aba.status_details` (array of objects)
        Additional details; includes at least one entry when the status is not `active`.

        - `features.financial_addresses.aba.status_details.code` (enum)
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

        - `features.financial_addresses.aba.status_details.resolution` (enum, nullable)
          Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
          - `contact_stripe`
            The user should contact Stripe via support.stripe.com.

          - `provide_information`
            The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

          - `remove_restriction`
            The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

        - `features.financial_addresses.aba.status_details.restriction` (enum, nullable)
          The `platform_restrictions` that are restricting this Feature.
Possible enum values:
          - `inbound_flows`
            Restricts all inbound money movement.

          - `outbound_flows`
            Restricts all outbound money movement.

  - `features.inbound_transfers` (object, nullable)
    Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.

    - `features.inbound_transfers.ach` (object, nullable)
      Enables ACH Debits via the InboundTransfers API.

      - `features.inbound_transfers.ach.requested` (boolean)
        Whether the FinancialAccount should have the Feature.

      - `features.inbound_transfers.ach.status` (enum)
        Whether the Feature is operational.
Possible enum values:
        - `active`
          Indicates that the Feature might be used.

        - `pending`
          Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

        - `restricted`
          Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

      - `features.inbound_transfers.ach.status_details` (array of objects)
        Additional details; includes at least one entry when the status is not `active`.

        - `features.inbound_transfers.ach.status_details.code` (enum)
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

        - `features.inbound_transfers.ach.status_details.resolution` (enum, nullable)
          Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
          - `contact_stripe`
            The user should contact Stripe via support.stripe.com.

          - `provide_information`
            The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

          - `remove_restriction`
            The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

        - `features.inbound_transfers.ach.status_details.restriction` (enum, nullable)
          The `platform_restrictions` that are restricting this Feature.
Possible enum values:
          - `inbound_flows`
            Restricts all inbound money movement.

          - `outbound_flows`
            Restricts all outbound money movement.

  - `features.intra_stripe_flows` (object, nullable)
    Represents the ability for this FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).

    - `features.intra_stripe_flows.requested` (boolean)
      Whether the FinancialAccount should have the Feature.

    - `features.intra_stripe_flows.status` (enum)
      Whether the Feature is operational.
Possible enum values:
      - `active`
        Indicates that the Feature might be used.

      - `pending`
        Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

      - `restricted`
        Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

    - `features.intra_stripe_flows.status_details` (array of objects)
      Additional details; includes at least one entry when the status is not `active`.

      - `features.intra_stripe_flows.status_details.code` (enum)
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

      - `features.intra_stripe_flows.status_details.resolution` (enum, nullable)
        Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
        - `contact_stripe`
          The user should contact Stripe via support.stripe.com.

        - `provide_information`
          The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

        - `remove_restriction`
          The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

      - `features.intra_stripe_flows.status_details.restriction` (enum, nullable)
        The `platform_restrictions` that are restricting this Feature.
Possible enum values:
        - `inbound_flows`
          Restricts all inbound money movement.

        - `outbound_flows`
          Restricts all outbound money movement.

  - `features.outbound_payments` (object, nullable)
    Contains Features related to initiating money movement out of the FinancialAccount to someone else’s bucket of money.

    - `features.outbound_payments.ach` (object, nullable)
      Enables ACH transfers via the OutboundPayments API.

      - `features.outbound_payments.ach.requested` (boolean)
        Whether the FinancialAccount should have the Feature.

      - `features.outbound_payments.ach.status` (enum)
        Whether the Feature is operational.
Possible enum values:
        - `active`
          Indicates that the Feature might be used.

        - `pending`
          Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

        - `restricted`
          Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

      - `features.outbound_payments.ach.status_details` (array of objects)
        Additional details; includes at least one entry when the status is not `active`.

        - `features.outbound_payments.ach.status_details.code` (enum)
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

        - `features.outbound_payments.ach.status_details.resolution` (enum, nullable)
          Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
          - `contact_stripe`
            The user should contact Stripe via support.stripe.com.

          - `provide_information`
            The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

          - `remove_restriction`
            The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

        - `features.outbound_payments.ach.status_details.restriction` (enum, nullable)
          The `platform_restrictions` that are restricting this Feature.
Possible enum values:
          - `inbound_flows`
            Restricts all inbound money movement.

          - `outbound_flows`
            Restricts all outbound money movement.

    - `features.outbound_payments.us_domestic_wire` (object, nullable)
      Enables US domestic wire transfers via the OutboundPayments API.

      - `features.outbound_payments.us_domestic_wire.requested` (boolean)
        Whether the FinancialAccount should have the Feature.

      - `features.outbound_payments.us_domestic_wire.status` (enum)
        Whether the Feature is operational.
Possible enum values:
        - `active`
          Indicates that the Feature might be used.

        - `pending`
          Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

        - `restricted`
          Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

      - `features.outbound_payments.us_domestic_wire.status_details` (array of objects)
        Additional details; includes at least one entry when the status is not `active`.

        - `features.outbound_payments.us_domestic_wire.status_details.code` (enum)
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

        - `features.outbound_payments.us_domestic_wire.status_details.resolution` (enum, nullable)
          Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
          - `contact_stripe`
            The user should contact Stripe via support.stripe.com.

          - `provide_information`
            The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

          - `remove_restriction`
            The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

        - `features.outbound_payments.us_domestic_wire.status_details.restriction` (enum, nullable)
          The `platform_restrictions` that are restricting this Feature.
Possible enum values:
          - `inbound_flows`
            Restricts all inbound money movement.

          - `outbound_flows`
            Restricts all outbound money movement.

  - `features.outbound_transfers` (object, nullable)
    Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.

    - `features.outbound_transfers.ach` (object, nullable)
      Enables ACH transfers via the OutboundTransfers API.

      - `features.outbound_transfers.ach.requested` (boolean)
        Whether the FinancialAccount should have the Feature.

      - `features.outbound_transfers.ach.status` (enum)
        Whether the Feature is operational.
Possible enum values:
        - `active`
          Indicates that the Feature might be used.

        - `pending`
          Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

        - `restricted`
          Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

      - `features.outbound_transfers.ach.status_details` (array of objects)
        Additional details; includes at least one entry when the status is not `active`.

        - `features.outbound_transfers.ach.status_details.code` (enum)
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

        - `features.outbound_transfers.ach.status_details.resolution` (enum, nullable)
          Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
          - `contact_stripe`
            The user should contact Stripe via support.stripe.com.

          - `provide_information`
            The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

          - `remove_restriction`
            The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

        - `features.outbound_transfers.ach.status_details.restriction` (enum, nullable)
          The `platform_restrictions` that are restricting this Feature.
Possible enum values:
          - `inbound_flows`
            Restricts all inbound money movement.

          - `outbound_flows`
            Restricts all outbound money movement.

    - `features.outbound_transfers.us_domestic_wire` (object, nullable)
      Enables US domestic wire transfers via the OutboundTransfers API.

      - `features.outbound_transfers.us_domestic_wire.requested` (boolean)
        Whether the FinancialAccount should have the Feature.

      - `features.outbound_transfers.us_domestic_wire.status` (enum)
        Whether the Feature is operational.
Possible enum values:
        - `active`
          Indicates that the Feature might be used.

        - `pending`
          Indicates that the Feature can’t be used but that the `status` eventually changes to either `restricted` or `active` without user intervention.

        - `restricted`
          Indicates that the Feature can’t be used and either requires some action by the user or is permanently disabled.

      - `features.outbound_transfers.us_domestic_wire.status_details` (array of objects)
        Additional details; includes at least one entry when the status is not `active`.

        - `features.outbound_transfers.us_domestic_wire.status_details.code` (enum)
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

        - `features.outbound_transfers.us_domestic_wire.status_details.resolution` (enum, nullable)
          Represents what the user should do, if anything, to activate the Feature.
Possible enum values:
          - `contact_stripe`
            The user should contact Stripe via support.stripe.com.

          - `provide_information`
            The user should provide necessary onboarding requirements through `/v1/accounts` or the Stripe Dashboard.

          - `remove_restriction`
            The user should remove the restriction on the Feature by unrestricting the FinancialAccount `platform_restritions` indicated by the `status_details.restriction` field.

        - `features.outbound_transfers.us_domestic_wire.status_details.restriction` (enum, nullable)
          The `platform_restrictions` that are restricting this Feature.
Possible enum values:
          - `inbound_flows`
            Restricts all inbound money movement.

          - `outbound_flows`
            Restricts all outbound money movement.

- `financial_addresses` (array of objects)
  The set of credentials that resolve to a FinancialAccount.

  - `financial_addresses.aba` (object, nullable)
    Identifying information for the ABA address

    - `financial_addresses.aba.account_holder_name` (string)
      The name of the person or business that owns the bank account.

    - `financial_addresses.aba.account_number` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      The account number.

    - `financial_addresses.aba.account_number_last4` (string)
      The last four characters of the account number.

    - `financial_addresses.aba.bank_name` (string)
      Name of the bank.

    - `financial_addresses.aba.routing_number` (string)
      Routing number for the account.

  - `financial_addresses.supported_networks` (array of enums, nullable)
    The list of networks that the address supports

  - `financial_addresses.type` (enum)
    The type of financial address

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (object, nullable)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `nickname` (string, nullable)
  The nickname for the FinancialAccount.

- `pending_features` (array of enums)
  The array of paths to pending Features in the Features hash.

- `platform_restrictions` (object, nullable)
  The set of functionalities that the platform can restrict on the FinancialAccount.

  - `platform_restrictions.inbound_flows` (enum, nullable)
    Restricts all inbound money movement.
Possible enum values:
    - `restricted`
      The functionality is restricted.

    - `unrestricted`
      The functionality is not restricted.

  - `platform_restrictions.outbound_flows` (enum, nullable)
    Restricts all outbound money movement.
Possible enum values:
    - `restricted`
      The functionality is restricted.

    - `unrestricted`
      The functionality is not restricted.

- `restricted_features` (array of enums)
  The array of paths to restricted Features in the Features hash.

- `status` (enum)
  Status of this FinancialAccount.
Possible enum values:
  - `closed`
    The FinancialAccount is closed.

  - `open`
    The FinancialAccount is open.

- `status_details` (object)
  Details related to the status of this FinancialAccount.

  - `status_details.closed` (object, nullable)
    Details related to the closure of this FinancialAccount

    - `status_details.closed.reasons` (array of enums)
      The array that contains reasons for a FinancialAccount closure.
Possible enum values:
      - `account_rejected`
        The underlying account is permanently [rejected](https://docs.stripe.com/docs/api/account/reject.md).

      - `closed_by_platform`
        The FinancialAccount has been closed through the API.

      - `other`
        The FinancialAccount has been closed by Stripe.

- `supported_currencies` (array of enums)
  The currencies the FinancialAccount can hold a balance in. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

### The FinancialAccount object

```json
{
  "id": "fa_1MtZmL2eZvKYlo2Cer6cdwEC",
  "object": "treasury.financial_account",
  "active_features": [
    "financial_addresses.aba",
    "outbound_payments.ach",
    "outbound_payments.us_domestic_wire"
  ],
  "balance": {
    "cash": {
      "usd": 0
    },
    "inbound_pending": {
      "usd": 0
    },
    "outbound_pending": {
      "usd": 0
    }
  },
  "country": "US",
  "created": 1680714349,
  "financial_addresses": [
    {
      "aba": {
        "account_holder_name": "Jenny Rosen",
        "account_number_last4": "7890",
        "bank_name": "STRIPE TEST BANK",
        "routing_number": "0000000001"
      },
      "supported_networks": [
        "ach",
        "us_domestic_wire"
      ],
      "type": "aba"
    }
  ],
  "livemode": true,
  "metadata": null,
  "pending_features": [],
  "restricted_features": [],
  "status": "open",
  "status_details": {
    "closed": null
  },
  "supported_currencies": [
    "usd"
  ],
  "features": {}
}
```
