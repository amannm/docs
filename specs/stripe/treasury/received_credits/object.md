# The ReceivedCredit object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount (in cents) transferred.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `failure_code` (enum, nullable)
  Reason for the failure. A ReceivedCredit might fail because the receiving FinancialAccount is closed or frozen.
Possible enum values:
  - `account_closed`
    Funds can’t be sent to a closed FinancialAccount.

  - `account_frozen`
    Funds can’t be sent to a frozen FinancialAccount.

  - `international_transaction`
    International transactions can’t be sent to FinancialAccount.

  - `other`
    Funds can’t be sent to FinancialAccount for other reasons.

- `financial_account` (string, nullable)
  The FinancialAccount that received the funds.

- `hosted_regulatory_receipt_url` (string, nullable)
  A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

- `initiating_payment_method_details` (object)
  Details about the PaymentMethod used to send a ReceivedCredit.

  - `initiating_payment_method_details.balance` (enum, nullable)
    Set when `type` is `balance`.
Possible enum values:
    - `payments`
      The Stripe payments balance.

  - `initiating_payment_method_details.billing_details` (object)
    The contact details of the person or business referenced by the received payment method details.

    - `initiating_payment_method_details.billing_details.address` (object)
      Billing address.

      - `initiating_payment_method_details.billing_details.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `initiating_payment_method_details.billing_details.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `initiating_payment_method_details.billing_details.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `initiating_payment_method_details.billing_details.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `initiating_payment_method_details.billing_details.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `initiating_payment_method_details.billing_details.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `initiating_payment_method_details.billing_details.email` (string, nullable)
      Email address.

    - `initiating_payment_method_details.billing_details.name` (string, nullable)
      Full name.

  - `initiating_payment_method_details.financial_account` (object, nullable)
    Set when `type` is `financial_account`. This is a [FinancialAccount](object.md#financial_accounts) ID.

    - `initiating_payment_method_details.financial_account.id` (string)
      The FinancialAccount ID.

    - `initiating_payment_method_details.financial_account.network` (enum)
      The rails the ReceivedCredit was sent over. A FinancialAccount can only send funds over `stripe`.

  - `initiating_payment_method_details.issuing_card` (string, nullable)
    Set when `type` is `issuing_card`. This is an [Issuing Card](object.md#issuing_cards) ID.

  - `initiating_payment_method_details.type` (enum)
    Polymorphic type matching the originating money movement’s source. This can be an external account, a Stripe balance, or a FinancialAccount.

  - `initiating_payment_method_details.us_bank_account` (object, nullable)
    Set when `type` is `us_bank_account`.

    - `initiating_payment_method_details.us_bank_account.bank_name` (string, nullable)
      Bank name.

    - `initiating_payment_method_details.us_bank_account.last4` (string, nullable)
      The last four digits of the bank account number.

    - `initiating_payment_method_details.us_bank_account.routing_number` (string, nullable)
      The routing number for the bank account.

- `linked_flows` (object)
  Other flows linked to a ReceivedCredit.

  - `linked_flows.credit_reversal` (string, nullable)
    The CreditReversal created as a result of this ReceivedCredit being reversed.

  - `linked_flows.issuing_authorization` (string, nullable)
    Set if the ReceivedCredit was created due to an [Issuing Authorization](object.md#issuing_authorizations) object.

  - `linked_flows.issuing_transaction` (string, nullable)
    Set if the ReceivedCredit is also viewable as an [Issuing transaction](object.md#issuing_transactions) object.

  - `linked_flows.source_flow` (string, nullable)
    ID of the source flow. Set if `network` is `stripe` and the source flow is visible to the user. Examples of source flows include OutboundPayments, payouts, or CreditReversals.

  - `linked_flows.source_flow_details` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
    The expandable object of the source flow.

    - `linked_flows.source_flow_details.credit_reversal` (object, nullable)
      Details about a [CreditReversal](object.md#credit_reversals).

      - `linked_flows.source_flow_details.credit_reversal.id` (string)
        Unique identifier for the object.

      - `linked_flows.source_flow_details.credit_reversal.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `linked_flows.source_flow_details.credit_reversal.amount` (integer)
        Amount (in cents) transferred.

      - `linked_flows.source_flow_details.credit_reversal.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `linked_flows.source_flow_details.credit_reversal.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `linked_flows.source_flow_details.credit_reversal.financial_account` (string)
        The FinancialAccount to reverse funds from.

      - `linked_flows.source_flow_details.credit_reversal.hosted_regulatory_receipt_url` (string, nullable)
        A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

      - `linked_flows.source_flow_details.credit_reversal.livemode` (boolean)
        If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

      - `linked_flows.source_flow_details.credit_reversal.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `linked_flows.source_flow_details.credit_reversal.network` (enum)
        The rails used to reverse the funds.

      - `linked_flows.source_flow_details.credit_reversal.received_credit` (string)
        The ReceivedCredit being reversed.

      - `linked_flows.source_flow_details.credit_reversal.status` (enum)
        Status of the CreditReversal
Possible enum values:
        - `canceled`
          The CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).

        - `posted`
          The CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)

        - `processing`
          The CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).

      - `linked_flows.source_flow_details.credit_reversal.status_transitions` (object)
        Hash containing timestamps of when the object transitioned to a particular `status`.

        - `linked_flows.source_flow_details.credit_reversal.status_transitions.posted_at` (timestamp, nullable)
          Timestamp describing when the CreditReversal changed status to `posted`

      - `linked_flows.source_flow_details.credit_reversal.transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The Transaction associated with this object.

    - `linked_flows.source_flow_details.outbound_payment` (object, nullable)
      Details about an [OutboundPayment](object.md#outbound_payments).

      - `linked_flows.source_flow_details.outbound_payment.id` (string)
        Unique identifier for the object.

      - `linked_flows.source_flow_details.outbound_payment.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `linked_flows.source_flow_details.outbound_payment.amount` (integer)
        Amount (in cents) transferred.

      - `linked_flows.source_flow_details.outbound_payment.cancelable` (boolean)
        Returns `true` if the object can be canceled, and `false` otherwise.

      - `linked_flows.source_flow_details.outbound_payment.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `linked_flows.source_flow_details.outbound_payment.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `linked_flows.source_flow_details.outbound_payment.customer` (string, nullable)
        ID of the [customer](https://docs.stripe.com/docs/api/customers.md) to whom an OutboundPayment is sent.

      - `linked_flows.source_flow_details.outbound_payment.description` (string, nullable)
        An arbitrary string attached to the object. Often useful for displaying to users.

      - `linked_flows.source_flow_details.outbound_payment.destination_payment_method` (string, nullable)
        The PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using `destination_payment_method_data`.

      - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details` (object, nullable)
        Details about the PaymentMethod for an OutboundPayment.

        - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details` (object)
          Contact details for the person or business receiving the OutboundPayment.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address` (object)
            Billing address.

            - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.city` (string, nullable)
              City, district, suburb, town, or village.

            - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.line1` (string, nullable)
              Address line 1, such as the street, PO Box, or company name.

            - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.line2` (string, nullable)
              Address line 2, such as the apartment, suite, unit, or building.

            - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.postal_code` (string, nullable)
              ZIP or postal code.

            - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.state` (string, nullable)
              State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.email` (string, nullable)
            Email address.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.name` (string, nullable)
            Full name.

        - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.financial_account` (object, nullable)
          Details about the `financial_account`.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.financial_account.id` (string)
            Token of the FinancialAccount.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.financial_account.network` (enum)
            The rails used to send funds.

        - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.type` (enum)
          The type of the payment method used in the OutboundPayment.
Possible enum values:
          - `financial_account`
          - `us_bank_account`

        - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account` (object, nullable)
          Details about the `us_bank_account`.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
            Account holder type: individual or company.
Possible enum values:
            - `company`
              Account belongs to a company

            - `individual`
              Account belongs to an individual

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.account_type` (enum, nullable)
            Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
            - `checking`
              Bank account type is checking

            - `savings`
              Bank account type is savings

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.bank_name` (string, nullable)
            Name of the bank associated with the bank account.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.fingerprint` (string, nullable)
            Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.last4` (string, nullable)
            Last four digits of the bank account number.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            ID of the mandate used to make this payment.

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.network` (enum)
            The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
            - `ach`
              ACH network

            - `us_domestic_wire`
              US domestic wire network

          - `linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.routing_number` (string, nullable)
            Routing number of the bank account.

      - `linked_flows.source_flow_details.outbound_payment.end_user_details` (object, nullable)
        Details about the end user.

        - `linked_flows.source_flow_details.outbound_payment.end_user_details.ip_address` (string, nullable)
          IP address of the user initiating the OutboundPayment. Set if `present` is set to `true`. IP address collection is required for risk and compliance reasons. This will be used to help determine if the OutboundPayment is authorized or should be blocked.

        - `linked_flows.source_flow_details.outbound_payment.end_user_details.present` (boolean)
          `true` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`.

      - `linked_flows.source_flow_details.outbound_payment.expected_arrival_date` (timestamp)
        The date when funds are expected to arrive in the destination account.

      - `linked_flows.source_flow_details.outbound_payment.financial_account` (string)
        The FinancialAccount that funds were pulled from.

      - `linked_flows.source_flow_details.outbound_payment.hosted_regulatory_receipt_url` (string, nullable)
        A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

      - `linked_flows.source_flow_details.outbound_payment.livemode` (boolean)
        If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

      - `linked_flows.source_flow_details.outbound_payment.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `linked_flows.source_flow_details.outbound_payment.returned_details` (object, nullable)
        Details about a returned OutboundPayment. Only set when the status is `returned`.

        - `linked_flows.source_flow_details.outbound_payment.returned_details.code` (enum)
          Reason for the return.
Possible enum values:
          - `account_closed`
            The destination has been closed.

          - `account_frozen`
            The destination has been frozen.

          - `bank_account_restricted`
            The destination bank account has restrictions on either the type or number of transfers allowed. This normally indicates that the bank account is a savings or other non-checking account.

          - `bank_ownership_changed`
            The destination bank account is no longer valid because its branch has changed ownership.

          - `declined`
            The destination has declined this OutboundPayment.

          - `incorrect_account_holder_name`
            The destination bank notified us that the bank account holder name on file is incorrect.

          - `invalid_account_number`
            The destination bank account details on file are probably incorrect. The routing number seems correct, but the account number is invalid.

          - `invalid_currency`
            The destination was unable to process this OutboundPayment because of its currency.

          - `no_account`
            The destination bank account details on file are probably incorrect. No bank account exists with these details.

          - `other`
            The destination could not process this OutboundPayment.

        - `linked_flows.source_flow_details.outbound_payment.returned_details.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
          The Transaction associated with this object.

      - `linked_flows.source_flow_details.outbound_payment.statement_descriptor` (string)
        The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).

      - `linked_flows.source_flow_details.outbound_payment.status` (enum)
        Current status of the OutboundPayment: `processing`, `failed`, `posted`, `returned`, `canceled`. An OutboundPayment is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundPayment has been “confirmed” and funds have left the account, or to `failed` or `canceled`. If an OutboundPayment fails to arrive at its destination, its status will change to `returned`.

      - `linked_flows.source_flow_details.outbound_payment.status_transitions` (object)
        Hash containing timestamps of when the object transitioned to a particular `status`.

        - `linked_flows.source_flow_details.outbound_payment.status_transitions.canceled_at` (timestamp, nullable)
          Timestamp describing when an OutboundPayment changed status to `canceled`.

        - `linked_flows.source_flow_details.outbound_payment.status_transitions.failed_at` (timestamp, nullable)
          Timestamp describing when an OutboundPayment changed status to `failed`.

        - `linked_flows.source_flow_details.outbound_payment.status_transitions.posted_at` (timestamp, nullable)
          Timestamp describing when an OutboundPayment changed status to `posted`.

        - `linked_flows.source_flow_details.outbound_payment.status_transitions.returned_at` (timestamp, nullable)
          Timestamp describing when an OutboundPayment changed status to `returned`.

      - `linked_flows.source_flow_details.outbound_payment.tracking_details` (object, nullable)
        Details about network-specific tracking information if available.

        - `linked_flows.source_flow_details.outbound_payment.tracking_details.ach` (object, nullable)
          ACH network tracking details.

          - `linked_flows.source_flow_details.outbound_payment.tracking_details.ach.trace_id` (string)
            ACH trace ID of the OutboundPayment for payments sent over the `ach` network.

        - `linked_flows.source_flow_details.outbound_payment.tracking_details.type` (enum)
          The US bank account network used to send funds.
Possible enum values:
          - `ach`
          - `us_domestic_wire`

        - `linked_flows.source_flow_details.outbound_payment.tracking_details.us_domestic_wire` (object, nullable)
          US domestic wire network tracking details.

          - `linked_flows.source_flow_details.outbound_payment.tracking_details.us_domestic_wire.chips` (string, nullable)
            CHIPS System Sequence Number (SSN) of the OutboundPayment for payments sent over the `us_domestic_wire` network.

          - `linked_flows.source_flow_details.outbound_payment.tracking_details.us_domestic_wire.imad` (string, nullable)
            IMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.

          - `linked_flows.source_flow_details.outbound_payment.tracking_details.us_domestic_wire.omad` (string, nullable)
            OMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.

      - `linked_flows.source_flow_details.outbound_payment.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
        The Transaction associated with this object.

    - `linked_flows.source_flow_details.outbound_transfer` (object, nullable)
      Details about an [OutboundTransfer](object.md#outbound_transfers).

      - `linked_flows.source_flow_details.outbound_transfer.id` (string)
        Unique identifier for the object.

      - `linked_flows.source_flow_details.outbound_transfer.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `linked_flows.source_flow_details.outbound_transfer.amount` (integer)
        Amount (in cents) transferred.

      - `linked_flows.source_flow_details.outbound_transfer.cancelable` (boolean)
        Returns `true` if the object can be canceled, and `false` otherwise.

      - `linked_flows.source_flow_details.outbound_transfer.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `linked_flows.source_flow_details.outbound_transfer.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `linked_flows.source_flow_details.outbound_transfer.description` (string, nullable)
        An arbitrary string attached to the object. Often useful for displaying to users.

      - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method` (string, nullable)
        The PaymentMethod used as the payment instrument for an OutboundTransfer.

      - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details` (object)
        Details about the PaymentMethod for an OutboundTransfer

        - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details` (object)
          Contact details for the person or business receiving the OutboundTransfer.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address` (object)
            Billing address.

            - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.city` (string, nullable)
              City, district, suburb, town, or village.

            - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.line1` (string, nullable)
              Address line 1, such as the street, PO Box, or company name.

            - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.line2` (string, nullable)
              Address line 2, such as the apartment, suite, unit, or building.

            - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.postal_code` (string, nullable)
              ZIP or postal code.

            - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.state` (string, nullable)
              State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.email` (string, nullable)
            Email address.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.name` (string, nullable)
            Full name.

        - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.financial_account` (object, nullable)
          Details about the `financial_account`.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.financial_account.id` (string)
            Token of the FinancialAccount.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.financial_account.network` (enum)
            The rails used to send funds.

        - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.type` (enum)
          The type of the payment method used in the OutboundTransfer.

        - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account` (object, nullable)
          Details about the `us_bank_account`.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
            Account holder type: individual or company.
Possible enum values:
            - `company`
              Account belongs to a company

            - `individual`
              Account belongs to an individual

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.account_type` (enum, nullable)
            Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
            - `checking`
              Bank account type is checking

            - `savings`
              Bank account type is savings

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.bank_name` (string, nullable)
            Name of the bank associated with the bank account.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.fingerprint` (string, nullable)
            Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.last4` (string, nullable)
            Last four digits of the bank account number.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            ID of the mandate used to make this payment.

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.network` (enum)
            The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
            - `ach`
              ACH network

            - `us_domestic_wire`
              US domestic wire network

          - `linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.routing_number` (string, nullable)
            Routing number of the bank account.

      - `linked_flows.source_flow_details.outbound_transfer.expected_arrival_date` (timestamp)
        The date when funds are expected to arrive in the destination account.

      - `linked_flows.source_flow_details.outbound_transfer.financial_account` (string)
        The FinancialAccount that funds were pulled from.

      - `linked_flows.source_flow_details.outbound_transfer.hosted_regulatory_receipt_url` (string, nullable)
        A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

      - `linked_flows.source_flow_details.outbound_transfer.livemode` (boolean)
        If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

      - `linked_flows.source_flow_details.outbound_transfer.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `linked_flows.source_flow_details.outbound_transfer.returned_details` (object, nullable)
        Details about a returned OutboundTransfer. Only set when the status is `returned`.

        - `linked_flows.source_flow_details.outbound_transfer.returned_details.code` (enum)
          Reason for the return.
Possible enum values:
          - `account_closed`
            The destination has been closed.

          - `account_frozen`
            The destination has been frozen.

          - `bank_account_restricted`
            The destination bank account has restrictions on either the type or number of transfers allowed. This normally indicates that the bank account is a savings or other non-checking account.

          - `bank_ownership_changed`
            The destination bank account is no longer valid because its branch has changed ownership.

          - `declined`
            The destination has declined this OutboundTransfer.

          - `incorrect_account_holder_name`
            The destination bank notified us that the bank account holder name on file is incorrect.

          - `invalid_account_number`
            The destination bank account details on file are probably incorrect. The routing number seems correct, but the account number is invalid.

          - `invalid_currency`
            The destination was unable to process this OutboundTransfer because of its currency.

          - `no_account`
            The destination bank account details on file are probably incorrect. No bank account exists with these details.

          - `other`
            The destination could not process this OutboundTransfer.

        - `linked_flows.source_flow_details.outbound_transfer.returned_details.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
          The Transaction associated with this object.

      - `linked_flows.source_flow_details.outbound_transfer.statement_descriptor` (string)
        Information about the OutboundTransfer to be sent to the recipient account.

      - `linked_flows.source_flow_details.outbound_transfer.status` (enum)
        Current status of the OutboundTransfer: `processing`, `failed`, `canceled`, `posted`, `returned`. An OutboundTransfer is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundTransfer has been “confirmed” and funds have left the account, or to `failed` or `canceled`. If an OutboundTransfer fails to arrive at its destination, its status will change to `returned`.

      - `linked_flows.source_flow_details.outbound_transfer.status_transitions` (object)
        Hash containing timestamps of when the object transitioned to a particular `status`.

        - `linked_flows.source_flow_details.outbound_transfer.status_transitions.canceled_at` (timestamp, nullable)
          Timestamp describing when an OutboundTransfer changed status to `canceled`

        - `linked_flows.source_flow_details.outbound_transfer.status_transitions.failed_at` (timestamp, nullable)
          Timestamp describing when an OutboundTransfer changed status to `failed`

        - `linked_flows.source_flow_details.outbound_transfer.status_transitions.posted_at` (timestamp, nullable)
          Timestamp describing when an OutboundTransfer changed status to `posted`

        - `linked_flows.source_flow_details.outbound_transfer.status_transitions.returned_at` (timestamp, nullable)
          Timestamp describing when an OutboundTransfer changed status to `returned`

      - `linked_flows.source_flow_details.outbound_transfer.tracking_details` (object, nullable)
        Details about network-specific tracking information if available.

        - `linked_flows.source_flow_details.outbound_transfer.tracking_details.ach` (object, nullable)
          ACH network tracking details.

          - `linked_flows.source_flow_details.outbound_transfer.tracking_details.ach.trace_id` (string)
            ACH trace ID of the OutboundTransfer for transfers sent over the `ach` network.

        - `linked_flows.source_flow_details.outbound_transfer.tracking_details.type` (enum)
          The US bank account network used to send funds.
Possible enum values:
          - `ach`
          - `us_domestic_wire`

        - `linked_flows.source_flow_details.outbound_transfer.tracking_details.us_domestic_wire` (object, nullable)
          US domestic wire network tracking details.

          - `linked_flows.source_flow_details.outbound_transfer.tracking_details.us_domestic_wire.chips` (string, nullable)
            CHIPS System Sequence Number (SSN) of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

          - `linked_flows.source_flow_details.outbound_transfer.tracking_details.us_domestic_wire.imad` (string, nullable)
            IMAD of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

          - `linked_flows.source_flow_details.outbound_transfer.tracking_details.us_domestic_wire.omad` (string, nullable)
            OMAD of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

      - `linked_flows.source_flow_details.outbound_transfer.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
        The Transaction associated with this object.

    - `linked_flows.source_flow_details.payout` (object, nullable)
      Details about a [Payout](object.md#payouts).

      - `linked_flows.source_flow_details.payout.id` (string)
        Unique identifier for the object.

      - `linked_flows.source_flow_details.payout.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `linked_flows.source_flow_details.payout.amount` (integer)
        The amount (in cents) that transfers to your bank account or debit card.

      - `linked_flows.source_flow_details.payout.application_fee` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The application fee (if any) for the payout. [See the Connect documentation](https://docs.stripe.com/docs/connect/instant-payouts.md#monetization-and-fees) for details.

      - `linked_flows.source_flow_details.payout.application_fee_amount` (integer, nullable)
        The amount of the application fee (if any) requested for the payout. [See the Connect documentation](https://docs.stripe.com/docs/connect/instant-payouts.md#monetization-and-fees) for details.

      - `linked_flows.source_flow_details.payout.arrival_date` (timestamp)
        Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays.

      - `linked_flows.source_flow_details.payout.automatic` (boolean)
        Returns `true` if the payout is created by an [automated payout schedule](https://docs.stripe.com/docs/payouts.md#payout-schedule) and `false` if it’s [requested manually](https://stripe.com/docs/payouts#manual-payouts).

      - `linked_flows.source_flow_details.payout.balance_transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        ID of the balance transaction that describes the impact of this payout on your account balance.

      - `linked_flows.source_flow_details.payout.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `linked_flows.source_flow_details.payout.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `linked_flows.source_flow_details.payout.description` (string, nullable)
        An arbitrary string attached to the object. Often useful for displaying to users.

      - `linked_flows.source_flow_details.payout.destination` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        ID of the bank account or card the payout is sent to.

      - `linked_flows.source_flow_details.payout.failure_balance_transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        If the payout fails or cancels, this is the ID of the balance transaction that reverses the initial balance transaction and returns the funds from the failed payout back in your balance.

      - `linked_flows.source_flow_details.payout.failure_code` (string, nullable)
        Error code that provides a reason for a payout failure, if available. View our [list of failure codes](https://docs.stripe.com/docs/api.md#payout_failures).

      - `linked_flows.source_flow_details.payout.failure_message` (string, nullable)
        Message that provides the reason for a payout failure, if available.

      - `linked_flows.source_flow_details.payout.livemode` (boolean)
        If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

      - `linked_flows.source_flow_details.payout.metadata` (object, nullable)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `linked_flows.source_flow_details.payout.method` (string)
        The method used to send this payout, which can be `standard` or `instant`. `instant` is supported for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).

      - `linked_flows.source_flow_details.payout.original_payout` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        If the payout reverses another, this is the ID of the original payout.

      - `linked_flows.source_flow_details.payout.payout_method` (string, nullable)
        ID of the v2 FinancialAccount the funds are sent to.

      - `linked_flows.source_flow_details.payout.reconciliation_status` (enum)
        If `completed`, you can use the [Balance Transactions API](https://docs.stripe.com/docs/api/balance_transactions/list.md#balance_transaction_list-payout) to list all balance transactions that are paid out in this payout.
Possible enum values:
        - `completed`
          The Balance Transactions paid out in this payout. You can query it with the [Balance Transactions API](https://docs.stripe.com/docs/api/balance_transactions/list.md#balance_transaction_list-payout).

        - `in_progress`
          You can query the Balance Transactions paid out in this payout soon.

        - `not_applicable`
          We don’t support listing Balance Transactions for this payout. We only support this for standard automatic payouts.

      - `linked_flows.source_flow_details.payout.reversed_by` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        If the payout reverses, this is the ID of the payout that reverses this payout.

      - `linked_flows.source_flow_details.payout.source_type` (string)
        The source balance this payout came from, which can be one of the following: `card`, `fpx`, or `bank_account`.

      - `linked_flows.source_flow_details.payout.statement_descriptor` (string, nullable)
        Extra information about a payout that displays on the user’s bank statement.

      - `linked_flows.source_flow_details.payout.status` (string)
        Current status of the payout: `paid`, `pending`, `in_transit`, `canceled` or `failed`. A payout is `pending` until it’s submitted to the bank, when it becomes `in_transit`. The status changes to `paid` if the transaction succeeds, or to `failed` or `canceled` (within 5 business days). Some payouts that fail might initially show as `paid`, then change to `failed`.

      - `linked_flows.source_flow_details.payout.trace_id` (object, nullable)
        A value that generates from the beneficiary’s bank that allows users to track payouts with their bank. Banks might call this a “reference number” or something similar.

        - `linked_flows.source_flow_details.payout.trace_id.status` (string)
          Possible values are `pending`, `supported`, and `unsupported`. When `payout.status` is `pending` or `in_transit`, this will be `pending`. When the payout transitions to `paid`, `failed`, or `canceled`, this status will become `supported` or `unsupported` shortly after in most cases. In some cases, this may appear as `pending` for up to 10 days after `arrival_date` until transitioning to `supported` or `unsupported`.

        - `linked_flows.source_flow_details.payout.trace_id.value` (string, nullable)
          The trace ID value if `trace_id.status` is `supported`, otherwise `nil`.

      - `linked_flows.source_flow_details.payout.type` (enum)
        Can be `bank_account` or `card`.

    - `linked_flows.source_flow_details.type` (enum)
      The type of the source flow that originated the ReceivedCredit.
Possible enum values:
      - `credit_reversal`
        ReceivedCredits that were reversed and have associated CreditReversals.

      - `other`
        ReceivedCredits created from other source flow.

      - `outbound_payment`
        ReceivedCredits created from OutboundPayments.

      - `outbound_transfer`
        ReceivedCredits created from OutboundPayments.

      - `payout`
        ReceivedCredits created from Payouts.

  - `linked_flows.source_flow_type` (string, nullable)
    The type of flow that originated the ReceivedCredit (for example, `outbound_payment`).

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `network` (enum)
  The rails used to send the funds.
Possible enum values:
  - `ach`
  - `card`
  - `stripe`
  - `us_domestic_wire`

- `reversal_details` (object, nullable)
  Details describing when a ReceivedCredit may be reversed.

  - `reversal_details.deadline` (timestamp, nullable)
    Time before which a ReceivedCredit can be reversed.

  - `reversal_details.restricted_reason` (enum, nullable)
    Set if a ReceivedCredit cannot be reversed.
Possible enum values:
    - `already_reversed`
      A ReceivedCredit that’s already reversed has this `restricted_reason`. It may have a deadline populated in some cases.

    - `deadline_passed`
      A ReceivedCredit which used to be reversible until the timestamp in `deadline`, but is no longer reversible. ACH ReceivedCredits are only reversible for some time after they’re created.

    - `network_restricted`
      Network constraints prevent Stripe from allowing reversal on some ReceivedCredits, such as a ReceivedCredit from a wire transfer.

    - `other`
      A ReceivedCredit that was reversed because of another reason.

    - `source_flow_restricted`
      Stripe restricts users from reversing a Stripe network ReceivedCredit.

- `status` (enum)
  Status of the ReceivedCredit. ReceivedCredits are created either `succeeded` (approved) or `failed` (declined). If a ReceivedCredit is declined, the failure reason can be found in the `failure_code` field.
Possible enum values:
  - `failed`
    The ReceivedCredit was declined, and no Transaction was created.

  - `succeeded`
    The ReceivedCredit was approved.

- `transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The Transaction associated with this object.

### The ReceivedCredit object

```json
{
  "id": "rc_1MtkSr2eZvKYlo2CcysvUbEw",
  "object": "treasury.received_credit",
  "amount": 1000,
  "created": 1680755425,
  "currency": "usd",
  "description": "Stripe Test",
  "failure_code": null,
  "financial_account": "fa_1MtkSr2eZvKYlo2CsJozwFWD",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/CBQaFwoVYWNjdF8xMDMyRDgyZVp2S1lsbzJDKOKVuaEGMgagXvSInCY6NpMvimqdsEKNHRrHZ3OGyVm_l5LfDMezNeY83F5Mq-rryXZ-J1z-jfFBv30wz5WxDH97VRBIzw",
  "initiating_payment_method_details": {
    "billing_details": {
      "address": {
        "city": null,
        "country": null,
        "line1": null,
        "line2": null,
        "postal_code": null,
        "state": null
      },
      "email": null,
      "name": "Jane Austen"
    },
    "type": "us_bank_account",
    "us_bank_account": {
      "bank_name": "STRIPE TEST BANK",
      "last4": "6789",
      "routing_number": "110000000"
    }
  },
  "linked_flows": {
    "credit_reversal": null,
    "issuing_authorization": null,
    "issuing_transaction": null,
    "source_flow": null,
    "source_flow_type": null
  },
  "livemode": false,
  "network": "ach",
  "reversal_details": {
    "deadline": 1681084800,
    "restricted_reason": null
  },
  "status": "succeeded",
  "transaction": "trxn_1MtkSr2eZvKYlo2CuFFh9Rh0"
}
```
