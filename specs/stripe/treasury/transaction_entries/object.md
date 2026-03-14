# The TransactionEntry object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `balance_impact` (object)
  The current impact of the TransactionEntry on the FinancialAccount’s balance.

  - `balance_impact.cash` (integer)
    The change made to funds the user can spend right now.

  - `balance_impact.inbound_pending` (integer)
    The change made to funds that are not spendable yet, but will become available at a later time.

  - `balance_impact.outbound_pending` (integer)
    The change made to funds in the account, but not spendable because they are being held for pending outbound flows.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `effective_at` (timestamp)
  When the TransactionEntry will impact the FinancialAccount’s balance.

- `financial_account` (string)
  The FinancialAccount associated with this object.

- `flow` (string, nullable)
  Token of the flow associated with the TransactionEntry.

- `flow_details` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  Details of the flow associated with the TransactionEntry.

  - `flow_details.credit_reversal` (object, nullable)
    The CreditReversal object associated with the Transaction. Set if `type=credit_reversal`.

    - `flow_details.credit_reversal.id` (string)
      Unique identifier for the object.

    - `flow_details.credit_reversal.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `flow_details.credit_reversal.amount` (integer)
      Amount (in cents) transferred.

    - `flow_details.credit_reversal.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `flow_details.credit_reversal.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.credit_reversal.financial_account` (string)
      The FinancialAccount to reverse funds from.

    - `flow_details.credit_reversal.hosted_regulatory_receipt_url` (string, nullable)
      A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

    - `flow_details.credit_reversal.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `flow_details.credit_reversal.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `flow_details.credit_reversal.network` (enum)
      The rails used to reverse the funds.

    - `flow_details.credit_reversal.received_credit` (string)
      The ReceivedCredit being reversed.

    - `flow_details.credit_reversal.status` (enum)
      Status of the CreditReversal
Possible enum values:
      - `canceled`
        The CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).

      - `posted`
        The CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)

      - `processing`
        The CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).

    - `flow_details.credit_reversal.status_transitions` (object)
      Hash containing timestamps of when the object transitioned to a particular `status`.

      - `flow_details.credit_reversal.status_transitions.posted_at` (timestamp, nullable)
        Timestamp describing when the CreditReversal changed status to `posted`

    - `flow_details.credit_reversal.transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      The Transaction associated with this object.

  - `flow_details.debit_reversal` (object, nullable)
    The DebitReversal object associated with the Transaction. Set if `type=debit_reversal`.

    - `flow_details.debit_reversal.id` (string)
      Unique identifier for the object.

    - `flow_details.debit_reversal.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `flow_details.debit_reversal.amount` (integer)
      Amount (in cents) transferred.

    - `flow_details.debit_reversal.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `flow_details.debit_reversal.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.debit_reversal.financial_account` (string, nullable)
      The FinancialAccount to reverse funds from.

    - `flow_details.debit_reversal.hosted_regulatory_receipt_url` (string, nullable)
      A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

    - `flow_details.debit_reversal.linked_flows` (object, nullable)
      Other flows linked to a DebitReversal.

      - `flow_details.debit_reversal.linked_flows.issuing_dispute` (string, nullable)
        Set if there is an Issuing dispute associated with the DebitReversal.

    - `flow_details.debit_reversal.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `flow_details.debit_reversal.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `flow_details.debit_reversal.network` (enum)
      The rails used to reverse the funds.

    - `flow_details.debit_reversal.received_debit` (string)
      The ReceivedDebit being reversed.

    - `flow_details.debit_reversal.status` (enum)
      Status of the DebitReversal
Possible enum values:
      - `failed`
        The network has resolved the DebitReversal against the user.

      - `processing`
        The DebitReversal starting state.

      - `succeeded`
        The network has resolved the DebitReversal in the users favour. A crediting Transaction is created.

    - `flow_details.debit_reversal.status_transitions` (object)
      Hash containing timestamps of when the object transitioned to a particular `status`.

      - `flow_details.debit_reversal.status_transitions.completed_at` (timestamp, nullable)
        Timestamp describing when the DebitReversal changed status to `completed`.

    - `flow_details.debit_reversal.transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      The Transaction associated with this object.

  - `flow_details.inbound_transfer` (object, nullable)
    The InboundTransfer object associated with the Transaction. Set if `type=inbound_transfer`.

    - `flow_details.inbound_transfer.id` (string)
      Unique identifier for the object.

    - `flow_details.inbound_transfer.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `flow_details.inbound_transfer.amount` (integer)
      Amount (in cents) transferred.

    - `flow_details.inbound_transfer.cancelable` (boolean)
      Returns `true` if the InboundTransfer is able to be canceled.

    - `flow_details.inbound_transfer.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `flow_details.inbound_transfer.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.inbound_transfer.description` (string, nullable)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `flow_details.inbound_transfer.failure_details` (object, nullable)
      Details about this InboundTransfer’s failure. Only set when status is `failed`.

      - `flow_details.inbound_transfer.failure_details.code` (enum)
        Reason for the failure.
Possible enum values:
        - `account_closed`
          The bank account has been closed.

        - `account_frozen`
          The bank account has been frozen.

        - `bank_account_restricted`
          The bank account has restrictions on either the type or number of transfers allowed. This normally indicates that the bank account is a savings or other non-checking account.

        - `bank_ownership_changed`
          The bank account is no longer valid because its branch has changed ownership.

        - `debit_not_authorized`
          Debit transactions are not approved on the bank account.

        - `incorrect_account_holder_address`
          The bank notified us that the bank account holder address on file is incorrect.

        - `incorrect_account_holder_name`
          The bank notified us that the bank account holder name on file is incorrect.

        - `incorrect_account_holder_tax_id`
          The bank notified us that the bank account holder tax ID on file is incorrect.

        - `insufficient_funds`
          The bank account has insufficient funds to cover the debit transaction.

        - `invalid_account_number`
          The bank account details on file are probably incorrect. The routing number seems correct, but the account number is invalid.

        - `invalid_currency`
          The bank was unable to process this transfer because of its currency. This is probably because the bank account can’t accept payments in that currency.

        - `no_account`
          The bank account details on file are probably incorrect. No bank account exists with these details.

        - `other`
          The bank could not process this transfer.

    - `flow_details.inbound_transfer.financial_account` (string)
      The FinancialAccount that received the funds.

    - `flow_details.inbound_transfer.hosted_regulatory_receipt_url` (string, nullable)
      A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

    - `flow_details.inbound_transfer.linked_flows` (object)
      Other flows linked to a InboundTransfer.

      - `flow_details.inbound_transfer.linked_flows.received_debit` (string, nullable)
        If funds for this flow were returned after the flow went to the `succeeded` state, this field contains a reference to the ReceivedDebit return.

    - `flow_details.inbound_transfer.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `flow_details.inbound_transfer.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `flow_details.inbound_transfer.origin_payment_method` (string, nullable)
      The origin payment method to be debited for an InboundTransfer.

    - `flow_details.inbound_transfer.origin_payment_method_details` (object, nullable)
      Details about the PaymentMethod for an InboundTransfer.

      - `flow_details.inbound_transfer.origin_payment_method_details.billing_details` (object)
        Contact details for the person or business referenced by the PaymentMethod.

        - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.address` (object)
          Billing address.

          - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.address.postal_code` (string, nullable)
            ZIP or postal code.

          - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.email` (string, nullable)
          Email address.

        - `flow_details.inbound_transfer.origin_payment_method_details.billing_details.name` (string, nullable)
          Full name.

      - `flow_details.inbound_transfer.origin_payment_method_details.type` (enum)
        The type of the payment method used in the InboundTransfer.
Possible enum values:
        - `us_bank_account`
          US Bank Account

      - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account` (object, nullable)
        Optional fields for `us_bank_account`.

        - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
          Account holder type: individual or company.
Possible enum values:
          - `company`
            Account belongs to a company

          - `individual`
            Account belongs to an individual

        - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account.account_type` (enum, nullable)
          Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
          - `checking`
            Bank account type is checking

          - `savings`
            Bank account type is savings

        - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account.bank_name` (string, nullable)
          Name of the bank associated with the bank account.

        - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account.fingerprint` (string, nullable)
          Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

        - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account.last4` (string, nullable)
          Last four digits of the bank account number.

        - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
          ID of the mandate used to make this payment.

        - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account.network` (enum)
          The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.

        - `flow_details.inbound_transfer.origin_payment_method_details.us_bank_account.routing_number` (string, nullable)
          Routing number of the bank account.

    - `flow_details.inbound_transfer.returned` (boolean, nullable)
      Returns `true` if the funds for an InboundTransfer were returned after the InboundTransfer went to the `succeeded` state.

    - `flow_details.inbound_transfer.statement_descriptor` (string)
      Statement descriptor shown when funds are debited from the source. Not all payment networks support `statement_descriptor`.

    - `flow_details.inbound_transfer.status` (enum)
      Status of the InboundTransfer: `processing`, `succeeded`, `failed`, and `canceled`. An InboundTransfer is `processing` if it is created and pending. The status changes to `succeeded` once the funds have been “confirmed” and a `transaction` is created and posted. The status changes to `failed` if the transfer fails.

    - `flow_details.inbound_transfer.status_transitions` (object)
      Hash containing timestamps of when the object transitioned to a particular `status`.

      - `flow_details.inbound_transfer.status_transitions.failed_at` (timestamp, nullable)
        Timestamp describing when an InboundTransfer changed status to `failed`.

      - `flow_details.inbound_transfer.status_transitions.succeeded_at` (timestamp, nullable)
        Timestamp describing when an InboundTransfer changed status to `succeeded`.

    - `flow_details.inbound_transfer.transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      The Transaction associated with this object.

  - `flow_details.issuing_authorization` (object, nullable)
    The Issuing authorization object associated with the Transaction. Set if `type=issuing_authorization`.

    - `flow_details.issuing_authorization.id` (string)
      Unique identifier for the object.

    - `flow_details.issuing_authorization.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `flow_details.issuing_authorization.amount` (integer)
      The total amount that was authorized or rejected. This amount is in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `amount` should be the same as `merchant_amount`, unless `currency` and `merchant_currency` are different.

    - `flow_details.issuing_authorization.amount_details` (object, nullable)
      Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

      - `flow_details.issuing_authorization.amount_details.atm_fee` (integer, nullable)
        The fee charged by the ATM for the cash withdrawal.

      - `flow_details.issuing_authorization.amount_details.cashback_amount` (integer, nullable)
        The amount of cash requested by the cardholder.

    - `flow_details.issuing_authorization.approved` (boolean)
      Whether the authorization has been approved.

    - `flow_details.issuing_authorization.authorization_method` (enum)
      How the card details were provided.
Possible enum values:
      - `chip`
        The card was physically present and inserted into a chip-enabled terminal. The transaction is cryptographically secured.

      - `contactless`
        The card was tapped on a contactless-enabled terminal. If a digital wallet copy of the card was used, the `wallet` field will be present.

      - `keyed_in`
        The card number was manually entered into a terminal.

      - `online`
        The card was used in a card-not-present scenario, such as a transaction initiated at an online e-commerce checkout.

      - `swipe`
        The card was physically swiped in a terminal.

    - `flow_details.issuing_authorization.balance_transactions` (array of objects)
      List of balance transactions associated with this authorization.

      - `flow_details.issuing_authorization.balance_transactions.id` (string)
        Unique identifier for the object.

      - `flow_details.issuing_authorization.balance_transactions.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `flow_details.issuing_authorization.balance_transactions.amount` (integer)
        Gross amount of this transaction (in cents). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.

      - `flow_details.issuing_authorization.balance_transactions.available_on` (timestamp)
        The date that the transaction’s net funds become available in the Stripe balance.

      - `flow_details.issuing_authorization.balance_transactions.balance_type` (enum)
        The balance that this transaction impacts.
Possible enum values:
        - `issuing`
          Balance Transactions that affect your Issuing balance

        - `payments`
          Balance Transactions that affect your Payments balance

        - `refund_and_dispute_prefunding`
          Balance Transactions that affect your Refund and Dispute Prefunding balance

        - `risk_reserved`
          Balance Transactions that affect your Risk Reserved balance

      - `flow_details.issuing_authorization.balance_transactions.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `flow_details.issuing_authorization.balance_transactions.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `flow_details.issuing_authorization.balance_transactions.description` (string, nullable)
        An arbitrary string attached to the object. Often useful for displaying to users.

      - `flow_details.issuing_authorization.balance_transactions.exchange_rate` (float, nullable)
        If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent’s `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction’s `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`.

      - `flow_details.issuing_authorization.balance_transactions.fee` (integer)
        Fees (in cents) paid for this transaction. Represented as a positive integer when assessed.

      - `flow_details.issuing_authorization.balance_transactions.fee_details` (array of objects)
        Detailed breakdown of fees (in cents) paid for this transaction.

        - `flow_details.issuing_authorization.balance_transactions.fee_details.amount` (integer)
          Amount of the fee, in cents.

        - `flow_details.issuing_authorization.balance_transactions.fee_details.application` (string, nullable)
          ID of the Connect application that earned the fee.

        - `flow_details.issuing_authorization.balance_transactions.fee_details.currency` (enum)
          Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

        - `flow_details.issuing_authorization.balance_transactions.fee_details.description` (string, nullable)
          An arbitrary string attached to the object. Often useful for displaying to users.

        - `flow_details.issuing_authorization.balance_transactions.fee_details.type` (string)
          Type of the fee, one of: `application_fee`, `payment_method_passthrough_fee`, `stripe_fee` or `tax`.

      - `flow_details.issuing_authorization.balance_transactions.net` (integer)
        Net impact to a Stripe balance (in cents). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee`

      - `flow_details.issuing_authorization.balance_transactions.reporting_category` (string)
        Learn more about how [reporting categories](https://stripe.com/docs/reports/reporting-categories) can help you understand balance transactions from an accounting perspective.

      - `flow_details.issuing_authorization.balance_transactions.source` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        This transaction relates to the Stripe object.

      - `flow_details.issuing_authorization.balance_transactions.status` (string)
        The transaction’s net funds status in the Stripe balance, which are either `available` or `pending`.

      - `flow_details.issuing_authorization.balance_transactions.type` (enum)
        Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `reserve_hold`, `reserve_release`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider `reporting_category` instead.
Possible enum values:
        - `adjustment`
        - `advance`
        - `advance_funding`
        - `anticipation_repayment`
        - `application_fee`
        - `application_fee_refund`
        - `charge`
        - `climate_order_purchase`
        - `climate_order_refund`
        - `connect_collection_transfer`
        - `contribution`
        - `issuing_authorization_hold`
        - `issuing_authorization_release`
        - `issuing_dispute`
        - `issuing_transaction`
        - `obligation_outbound`
        - `obligation_reversal_inbound`
        - `payment`
        - `payment_failure_refund`
        - `payment_network_reserve_hold`
        - `payment_network_reserve_release`
        - `payment_refund`
        - `payment_reversal`
        - `payment_unreconciled`
        - `payout`
        - `payout_cancel`
        - `payout_failure`
        - `payout_minimum_balance_hold`
        - `payout_minimum_balance_release`
        - `refund`
        - `refund_failure`
        - `reserve_hold`
        - `reserve_release`
        - `reserve_transaction`
        - `reserved_funds`
        - `stripe_balance_payment_debit`
        - `stripe_balance_payment_debit_reversal`
        - `stripe_fee`
        - `stripe_fx_fee`
        - `tax_fee`
        - `topup`
        - `topup_reversal`
        - `transfer`
        - `transfer_cancel`
        - `transfer_failure`
        - `transfer_refund`

    - `flow_details.issuing_authorization.card` (object)
      Card associated with this authorization.

      - `flow_details.issuing_authorization.card.id` (string)
        Unique identifier for the object.

      - `flow_details.issuing_authorization.card.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `flow_details.issuing_authorization.card.brand` (string)
        The brand of the card.

      - `flow_details.issuing_authorization.card.cancellation_reason` (enum, nullable)
        The reason why the card was canceled.
Possible enum values:
        - `design_rejected`
          The design of this card was rejected by Stripe for violating our [partner guidelines](https://docs.stripe.com/docs/issuing/cards/physical.md#design-review).

        - `lost`
          The card was lost.

        - `stolen`
          The card was stolen.

      - `flow_details.issuing_authorization.card.cardholder` (object)
        The [Cardholder](https://docs.stripe.com/docs/api.md#issuing_cardholder_object) object to which the card belongs.

        - `flow_details.issuing_authorization.card.cardholder.id` (string)
          Unique identifier for the object.

        - `flow_details.issuing_authorization.card.cardholder.object` (string)
          String representing the object’s type. Objects of the same type share the same value.

        - `flow_details.issuing_authorization.card.cardholder.billing` (object)
          The cardholder’s billing information.

          - `flow_details.issuing_authorization.card.cardholder.billing.address` (object)
            The cardholder’s billing address.

            - `flow_details.issuing_authorization.card.cardholder.billing.address.city` (string, nullable)
              City, district, suburb, town, or village.

            - `flow_details.issuing_authorization.card.cardholder.billing.address.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `flow_details.issuing_authorization.card.cardholder.billing.address.line1` (string, nullable)
              Address line 1, such as the street, PO Box, or company name.

            - `flow_details.issuing_authorization.card.cardholder.billing.address.line2` (string, nullable)
              Address line 2, such as the apartment, suite, unit, or building.

            - `flow_details.issuing_authorization.card.cardholder.billing.address.postal_code` (string, nullable)
              ZIP or postal code.

            - `flow_details.issuing_authorization.card.cardholder.billing.address.state` (string, nullable)
              State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `flow_details.issuing_authorization.card.cardholder.company` (object, nullable)
          Additional information about a `company` cardholder.

          - `flow_details.issuing_authorization.card.cardholder.company.tax_id_provided` (boolean)
            Whether the company’s business ID number was provided.

        - `flow_details.issuing_authorization.card.cardholder.created` (timestamp)
          Time at which the object was created. Measured in seconds since the Unix epoch.

        - `flow_details.issuing_authorization.card.cardholder.email` (string, nullable)
          The cardholder’s email address.

        - `flow_details.issuing_authorization.card.cardholder.individual` (object, nullable)
          Additional information about an `individual` cardholder.

          - `flow_details.issuing_authorization.card.cardholder.individual.card_issuing` (object, nullable)
            Information related to the card_issuing program for this cardholder.

            - `flow_details.issuing_authorization.card.cardholder.individual.card_issuing.user_terms_acceptance` (object, nullable)
              Information about cardholder acceptance of Celtic [Authorized User Terms](https://stripe.com/docs/issuing/cards#accept-authorized-user-terms). Required for cards backed by a Celtic program.

              - `flow_details.issuing_authorization.card.cardholder.individual.card_issuing.user_terms_acceptance.date` (timestamp, nullable)
                The Unix timestamp marking when the cardholder accepted the Authorized User Terms.

              - `flow_details.issuing_authorization.card.cardholder.individual.card_issuing.user_terms_acceptance.ip` (string, nullable)
                The IP address from which the cardholder accepted the Authorized User Terms.

              - `flow_details.issuing_authorization.card.cardholder.individual.card_issuing.user_terms_acceptance.user_agent` (string, nullable)
                The user agent of the browser from which the cardholder accepted the Authorized User Terms.

          - `flow_details.issuing_authorization.card.cardholder.individual.dob` (object, nullable)
            The date of birth of this cardholder.

            - `flow_details.issuing_authorization.card.cardholder.individual.dob.day` (integer, nullable)
              The day of birth, between 1 and 31.

            - `flow_details.issuing_authorization.card.cardholder.individual.dob.month` (integer, nullable)
              The month of birth, between 1 and 12.

            - `flow_details.issuing_authorization.card.cardholder.individual.dob.year` (integer, nullable)
              The four-digit year of birth.

          - `flow_details.issuing_authorization.card.cardholder.individual.first_name` (string, nullable)
            The first name of this cardholder. Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.

          - `flow_details.issuing_authorization.card.cardholder.individual.last_name` (string, nullable)
            The last name of this cardholder.  Required before activating Cards. This field cannot contain any numbers, special characters (except periods, commas, hyphens, spaces and apostrophes) or non-latin letters.

          - `flow_details.issuing_authorization.card.cardholder.individual.verification` (object, nullable)
            Government-issued ID document for this cardholder.

            - `flow_details.issuing_authorization.card.cardholder.individual.verification.document` (object, nullable)
              An identifying document, either a passport or local ID card.

              - `flow_details.issuing_authorization.card.cardholder.individual.verification.document.back` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
                The back of a document returned by a [file upload](object.md#create_file) with a `purpose` value of `identity_document`.

              - `flow_details.issuing_authorization.card.cardholder.individual.verification.document.front` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
                The front of a document returned by a [file upload](object.md#create_file) with a `purpose` value of `identity_document`.

        - `flow_details.issuing_authorization.card.cardholder.livemode` (boolean)
          If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

        - `flow_details.issuing_authorization.card.cardholder.metadata` (object)
          Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

        - `flow_details.issuing_authorization.card.cardholder.name` (string)
          The cardholder’s name. This will be printed on cards issued to them.

        - `flow_details.issuing_authorization.card.cardholder.phone_number` (string, nullable)
          The cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://docs.stripe.com/docs/issuing/3d-secure.md#when-is-3d-secure-applied) for more details.

        - `flow_details.issuing_authorization.card.cardholder.preferred_locales` (array of enums, nullable)
          The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`. This changes the language of the [3D Secure flow](https://docs.stripe.com/docs/issuing/3d-secure.md) and one-time password messages sent to the cardholder.

        - `flow_details.issuing_authorization.card.cardholder.requirements` (object)
          Information about verification requirements for the cardholder.

          - `flow_details.issuing_authorization.card.cardholder.requirements.disabled_reason` (enum, nullable)
            If `disabled_reason` is present, all cards will decline authorizations with `cardholder_verification_required` reason.
Possible enum values:
            - `listed`
              Account might be on a prohibited persons or companies list. The `past_due` field contains information that you need to provide before the cardholder can approve authorizations.

            - `rejected.listed`
              Cardholder is rejected because they are on a third-party prohibited persons or companies list (such as financial services provider or government). Their status will be `blocked`.

            - `requirements.past_due`
              Cardholder has outstanding requirements. The `past_due` field contains information that you need to provide before the cardholder can activate cards.

            - `under_review`
              This cardholder has raised additional review. Stripe will make a decision and update the `disabled_reason` field.

          - `flow_details.issuing_authorization.card.cardholder.requirements.past_due` (array of enums, nullable)
            Array of fields that need to be collected in order to verify and re-enable the cardholder.
Possible enum values:
            - `company.tax_id`
              The cardholder’s business number (Tax ID).

            - `individual.card_issuing.user_terms_acceptance.date`
              The Unix timestamp marking when the Cardholder accepted their Authorized User Terms. Required for Celtic Spend Card users.

            - `individual.card_issuing.user_terms_acceptance.ip`
              The IP address from which the Cardholder accepted their Authorized User Terms. Required for Celtic Spend Card users.

            - `individual.dob.day`
              The cardholder’s date of birth’s day.

            - `individual.dob.month`
              The cardholder’s date of birth’s month.

            - `individual.dob.year`
              The cardholder’s date of birth’s year.

            - `individual.first_name`
              The cardholder’s legal first name.

            - `individual.last_name`
              The cardholder’s legal last name.

            - `individual.verification.document`
              The front and back of a government-issued form of identification.

        - `flow_details.issuing_authorization.card.cardholder.spending_controls` (object, nullable)
          Rules that control spending across this cardholder’s cards. Refer to our [documentation](https://docs.stripe.com/docs/issuing/controls/spending-controls.md) for more details.

          - `flow_details.issuing_authorization.card.cardholder.spending_controls.allowed_categories` (array of enums, nullable)
            Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to allow. All other categories will be blocked. Cannot be set with `blocked_categories`.
Possible enum values:
            - `ac_refrigeration_repair`
            - `accounting_bookkeeping_services`
            - `advertising_services`
            - `agricultural_cooperative`
            - `airlines_air_carriers`
            - `airports_flying_fields`
            - `ambulance_services`
            - `amusement_parks_carnivals`
            - `antique_reproductions`
            - `antique_shops`
            - `aquariums`
            - `architectural_surveying_services`
            - `art_dealers_and_galleries`
            - `artists_supply_and_craft_shops`
            - `auto_and_home_supply_stores`
            - `auto_body_repair_shops`
            - `auto_paint_shops`
            - `auto_service_shops`
            - `automated_cash_disburse`
            - `automated_fuel_dispensers`
            - `automobile_associations`
            - `automotive_parts_and_accessories_stores`
            - `automotive_tire_stores`
            - `bail_and_bond_payments`
            - `bakeries`
            - `bands_orchestras`
            - `barber_and_beauty_shops`
            - `betting_casino_gambling`
            - `bicycle_shops`
            - `billiard_pool_establishments`
            - `boat_dealers`
            - `boat_rentals_and_leases`
            - `book_stores`
            - `books_periodicals_and_newspapers`
            - `bowling_alleys`
            - `bus_lines`
            - `business_secretarial_schools`
            - `buying_shopping_services`
            - `cable_satellite_and_other_pay_television_and_radio`
            - `camera_and_photographic_supply_stores`
            - `candy_nut_and_confectionery_stores`
            - `car_and_truck_dealers_new_used`
            - `car_and_truck_dealers_used_only`
            - `car_rental_agencies`
            - `car_washes`
            - `carpentry_services`
            - `carpet_upholstery_cleaning`
            - `caterers`
            - `charitable_and_social_service_organizations_fundraising`
            - `chemicals_and_allied_products`
            - `child_care_services`
            - `childrens_and_infants_wear_stores`
            - `chiropodists_podiatrists`
            - `chiropractors`
            - `cigar_stores_and_stands`
            - `civic_social_fraternal_associations`
            - `cleaning_and_maintenance`
            - `clothing_rental`
            - `colleges_universities`
            - `commercial_equipment`
            - `commercial_footwear`
            - `commercial_photography_art_and_graphics`
            - `commuter_transport_and_ferries`
            - `computer_network_services`
            - `computer_programming`
            - `computer_repair`
            - `computer_software_stores`
            - `computers_peripherals_and_software`
            - `concrete_work_services`
            - `construction_materials`
            - `consulting_public_relations`
            - `correspondence_schools`
            - `cosmetic_stores`
            - `counseling_services`
            - `country_clubs`
            - `courier_services`
            - `court_costs`
            - `credit_reporting_agencies`
            - `cruise_lines`
            - `dairy_products_stores`
            - `dance_hall_studios_schools`
            - `dating_escort_services`
            - `dentists_orthodontists`
            - `department_stores`
            - `detective_agencies`
            - `digital_goods_applications`
            - `digital_goods_games`
            - `digital_goods_large_volume`
            - `digital_goods_media`
            - `direct_marketing_catalog_merchant`
            - `direct_marketing_combination_catalog_and_retail_merchant`
            - `direct_marketing_inbound_telemarketing`
            - `direct_marketing_insurance_services`
            - `direct_marketing_other`
            - `direct_marketing_outbound_telemarketing`
            - `direct_marketing_subscription`
            - `direct_marketing_travel`
            - `discount_stores`
            - `doctors`
            - `door_to_door_sales`
            - `drapery_window_covering_and_upholstery_stores`
            - `drinking_places`
            - `drug_stores_and_pharmacies`
            - `drugs_drug_proprietaries_and_druggist_sundries`
            - `dry_cleaners`
            - `durable_goods`
            - `duty_free_stores`
            - `eating_places_restaurants`
            - `educational_services`
            - `electric_razor_stores`
            - `electric_vehicle_charging`
            - `electrical_parts_and_equipment`
            - `electrical_services`
            - `electronics_repair_shops`
            - `electronics_stores`
            - `elementary_secondary_schools`
            - `emergency_services_gcas_visa_use_only`
            - `employment_temp_agencies`
            - `equipment_rental`
            - `exterminating_services`
            - `family_clothing_stores`
            - `fast_food_restaurants`
            - `financial_institutions`
            - `fines_government_administrative_entities`
            - `fireplace_fireplace_screens_and_accessories_stores`
            - `floor_covering_stores`
            - `florists`
            - `florists_supplies_nursery_stock_and_flowers`
            - `freezer_and_locker_meat_provisioners`
            - `fuel_dealers_non_automotive`
            - `funeral_services_crematories`
            - `furniture_home_furnishings_and_equipment_stores_except_appliances`
            - `furniture_repair_refinishing`
            - `furriers_and_fur_shops`
            - `general_services`
            - `gift_card_novelty_and_souvenir_shops`
            - `glass_paint_and_wallpaper_stores`
            - `glassware_crystal_stores`
            - `golf_courses_public`
            - `government_licensed_horse_dog_racing_us_region_only`
            - `government_licensed_online_casions_online_gambling_us_region_only`
            - `government_owned_lotteries_non_us_region`
            - `government_owned_lotteries_us_region_only`
            - `government_services`
            - `grocery_stores_supermarkets`
            - `hardware_equipment_and_supplies`
            - `hardware_stores`
            - `health_and_beauty_spas`
            - `hearing_aids_sales_and_supplies`
            - `heating_plumbing_a_c`
            - `hobby_toy_and_game_shops`
            - `home_supply_warehouse_stores`
            - `hospitals`
            - `hotels_motels_and_resorts`
            - `household_appliance_stores`
            - `industrial_supplies`
            - `information_retrieval_services`
            - `insurance_default`
            - `insurance_underwriting_premiums`
            - `intra_company_purchases`
            - `jewelry_stores_watches_clocks_and_silverware_stores`
            - `landscaping_services`
            - `laundries`
            - `laundry_cleaning_services`
            - `legal_services_attorneys`
            - `luggage_and_leather_goods_stores`
            - `lumber_building_materials_stores`
            - `manual_cash_disburse`
            - `marinas_service_and_supplies`
            - `marketplaces`
            - `masonry_stonework_and_plaster`
            - `massage_parlors`
            - `medical_and_dental_labs`
            - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
            - `medical_services`
            - `membership_organizations`
            - `mens_and_boys_clothing_and_accessories_stores`
            - `mens_womens_clothing_stores`
            - `metal_service_centers`
            - `miscellaneous`
            - `miscellaneous_apparel_and_accessory_shops`
            - `miscellaneous_auto_dealers`
            - `miscellaneous_business_services`
            - `miscellaneous_food_stores`
            - `miscellaneous_general_merchandise`
            - `miscellaneous_general_services`
            - `miscellaneous_home_furnishing_specialty_stores`
            - `miscellaneous_publishing_and_printing`
            - `miscellaneous_recreation_services`
            - `miscellaneous_repair_shops`
            - `miscellaneous_specialty_retail`
            - `mobile_home_dealers`
            - `motion_picture_theaters`
            - `motor_freight_carriers_and_trucking`
            - `motor_homes_dealers`
            - `motor_vehicle_supplies_and_new_parts`
            - `motorcycle_shops_and_dealers`
            - `motorcycle_shops_dealers`
            - `music_stores_musical_instruments_pianos_and_sheet_music`
            - `news_dealers_and_newsstands`
            - `non_fi_money_orders`
            - `non_fi_stored_value_card_purchase_load`
            - `nondurable_goods`
            - `nurseries_lawn_and_garden_supply_stores`
            - `nursing_personal_care`
            - `office_and_commercial_furniture`
            - `opticians_eyeglasses`
            - `optometrists_ophthalmologist`
            - `orthopedic_goods_prosthetic_devices`
            - `osteopaths`
            - `package_stores_beer_wine_and_liquor`
            - `paints_varnishes_and_supplies`
            - `parking_lots_garages`
            - `passenger_railways`
            - `pawn_shops`
            - `pet_shops_pet_food_and_supplies`
            - `petroleum_and_petroleum_products`
            - `photo_developing`
            - `photographic_photocopy_microfilm_equipment_and_supplies`
            - `photographic_studios`
            - `picture_video_production`
            - `piece_goods_notions_and_other_dry_goods`
            - `plumbing_heating_equipment_and_supplies`
            - `political_organizations`
            - `postal_services_government_only`
            - `precious_stones_and_metals_watches_and_jewelry`
            - `professional_services`
            - `public_warehousing_and_storage`
            - `quick_copy_repro_and_blueprint`
            - `railroads`
            - `real_estate_agents_and_managers_rentals`
            - `record_stores`
            - `recreational_vehicle_rentals`
            - `religious_goods_stores`
            - `religious_organizations`
            - `roofing_siding_sheet_metal`
            - `secretarial_support_services`
            - `security_brokers_dealers`
            - `service_stations`
            - `sewing_needlework_fabric_and_piece_goods_stores`
            - `shoe_repair_hat_cleaning`
            - `shoe_stores`
            - `small_appliance_repair`
            - `snowmobile_dealers`
            - `special_trade_services`
            - `specialty_cleaning`
            - `sporting_goods_stores`
            - `sporting_recreation_camps`
            - `sports_and_riding_apparel_stores`
            - `sports_clubs_fields`
            - `stamp_and_coin_stores`
            - `stationary_office_supplies_printing_and_writing_paper`
            - `stationery_stores_office_and_school_supply_stores`
            - `swimming_pools_sales`
            - `t_ui_travel_germany`
            - `tailors_alterations`
            - `tax_payments_government_agencies`
            - `tax_preparation_services`
            - `taxicabs_limousines`
            - `telecommunication_equipment_and_telephone_sales`
            - `telecommunication_services`
            - `telegraph_services`
            - `tent_and_awning_shops`
            - `testing_laboratories`
            - `theatrical_ticket_agencies`
            - `timeshares`
            - `tire_retreading_and_repair`
            - `tolls_bridge_fees`
            - `tourist_attractions_and_exhibits`
            - `towing_services`
            - `trailer_parks_campgrounds`
            - `transportation_services`
            - `travel_agencies_tour_operators`
            - `truck_stop_iteration`
            - `truck_utility_trailer_rentals`
            - `typesetting_plate_making_and_related_services`
            - `typewriter_stores`
            - `u_s_federal_government_agencies_or_departments`
            - `uniforms_commercial_clothing`
            - `used_merchandise_and_secondhand_stores`
            - `utilities`
            - `variety_stores`
            - `veterinary_services`
            - `video_amusement_game_supplies`
            - `video_game_arcades`
            - `video_tape_rental_stores`
            - `vocational_trade_schools`
            - `watch_jewelry_repair`
            - `welding_repair`
            - `wholesale_clubs`
            - `wig_and_toupee_stores`
            - `wires_money_orders`
            - `womens_accessory_and_specialty_shops`
            - `womens_ready_to_wear_stores`
            - `wrecking_and_salvage_yards`

          - `flow_details.issuing_authorization.card.cardholder.spending_controls.allowed_merchant_countries` (array of strings, nullable)
            Array of strings containing representing countries from which authorizations will be allowed. Authorizations from merchants in all other countries will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset this control.

          - `flow_details.issuing_authorization.card.cardholder.spending_controls.blocked_categories` (array of enums, nullable)
            Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to decline. All other categories will be allowed. Cannot be set with `allowed_categories`.
Possible enum values:
            - `ac_refrigeration_repair`
            - `accounting_bookkeeping_services`
            - `advertising_services`
            - `agricultural_cooperative`
            - `airlines_air_carriers`
            - `airports_flying_fields`
            - `ambulance_services`
            - `amusement_parks_carnivals`
            - `antique_reproductions`
            - `antique_shops`
            - `aquariums`
            - `architectural_surveying_services`
            - `art_dealers_and_galleries`
            - `artists_supply_and_craft_shops`
            - `auto_and_home_supply_stores`
            - `auto_body_repair_shops`
            - `auto_paint_shops`
            - `auto_service_shops`
            - `automated_cash_disburse`
            - `automated_fuel_dispensers`
            - `automobile_associations`
            - `automotive_parts_and_accessories_stores`
            - `automotive_tire_stores`
            - `bail_and_bond_payments`
            - `bakeries`
            - `bands_orchestras`
            - `barber_and_beauty_shops`
            - `betting_casino_gambling`
            - `bicycle_shops`
            - `billiard_pool_establishments`
            - `boat_dealers`
            - `boat_rentals_and_leases`
            - `book_stores`
            - `books_periodicals_and_newspapers`
            - `bowling_alleys`
            - `bus_lines`
            - `business_secretarial_schools`
            - `buying_shopping_services`
            - `cable_satellite_and_other_pay_television_and_radio`
            - `camera_and_photographic_supply_stores`
            - `candy_nut_and_confectionery_stores`
            - `car_and_truck_dealers_new_used`
            - `car_and_truck_dealers_used_only`
            - `car_rental_agencies`
            - `car_washes`
            - `carpentry_services`
            - `carpet_upholstery_cleaning`
            - `caterers`
            - `charitable_and_social_service_organizations_fundraising`
            - `chemicals_and_allied_products`
            - `child_care_services`
            - `childrens_and_infants_wear_stores`
            - `chiropodists_podiatrists`
            - `chiropractors`
            - `cigar_stores_and_stands`
            - `civic_social_fraternal_associations`
            - `cleaning_and_maintenance`
            - `clothing_rental`
            - `colleges_universities`
            - `commercial_equipment`
            - `commercial_footwear`
            - `commercial_photography_art_and_graphics`
            - `commuter_transport_and_ferries`
            - `computer_network_services`
            - `computer_programming`
            - `computer_repair`
            - `computer_software_stores`
            - `computers_peripherals_and_software`
            - `concrete_work_services`
            - `construction_materials`
            - `consulting_public_relations`
            - `correspondence_schools`
            - `cosmetic_stores`
            - `counseling_services`
            - `country_clubs`
            - `courier_services`
            - `court_costs`
            - `credit_reporting_agencies`
            - `cruise_lines`
            - `dairy_products_stores`
            - `dance_hall_studios_schools`
            - `dating_escort_services`
            - `dentists_orthodontists`
            - `department_stores`
            - `detective_agencies`
            - `digital_goods_applications`
            - `digital_goods_games`
            - `digital_goods_large_volume`
            - `digital_goods_media`
            - `direct_marketing_catalog_merchant`
            - `direct_marketing_combination_catalog_and_retail_merchant`
            - `direct_marketing_inbound_telemarketing`
            - `direct_marketing_insurance_services`
            - `direct_marketing_other`
            - `direct_marketing_outbound_telemarketing`
            - `direct_marketing_subscription`
            - `direct_marketing_travel`
            - `discount_stores`
            - `doctors`
            - `door_to_door_sales`
            - `drapery_window_covering_and_upholstery_stores`
            - `drinking_places`
            - `drug_stores_and_pharmacies`
            - `drugs_drug_proprietaries_and_druggist_sundries`
            - `dry_cleaners`
            - `durable_goods`
            - `duty_free_stores`
            - `eating_places_restaurants`
            - `educational_services`
            - `electric_razor_stores`
            - `electric_vehicle_charging`
            - `electrical_parts_and_equipment`
            - `electrical_services`
            - `electronics_repair_shops`
            - `electronics_stores`
            - `elementary_secondary_schools`
            - `emergency_services_gcas_visa_use_only`
            - `employment_temp_agencies`
            - `equipment_rental`
            - `exterminating_services`
            - `family_clothing_stores`
            - `fast_food_restaurants`
            - `financial_institutions`
            - `fines_government_administrative_entities`
            - `fireplace_fireplace_screens_and_accessories_stores`
            - `floor_covering_stores`
            - `florists`
            - `florists_supplies_nursery_stock_and_flowers`
            - `freezer_and_locker_meat_provisioners`
            - `fuel_dealers_non_automotive`
            - `funeral_services_crematories`
            - `furniture_home_furnishings_and_equipment_stores_except_appliances`
            - `furniture_repair_refinishing`
            - `furriers_and_fur_shops`
            - `general_services`
            - `gift_card_novelty_and_souvenir_shops`
            - `glass_paint_and_wallpaper_stores`
            - `glassware_crystal_stores`
            - `golf_courses_public`
            - `government_licensed_horse_dog_racing_us_region_only`
            - `government_licensed_online_casions_online_gambling_us_region_only`
            - `government_owned_lotteries_non_us_region`
            - `government_owned_lotteries_us_region_only`
            - `government_services`
            - `grocery_stores_supermarkets`
            - `hardware_equipment_and_supplies`
            - `hardware_stores`
            - `health_and_beauty_spas`
            - `hearing_aids_sales_and_supplies`
            - `heating_plumbing_a_c`
            - `hobby_toy_and_game_shops`
            - `home_supply_warehouse_stores`
            - `hospitals`
            - `hotels_motels_and_resorts`
            - `household_appliance_stores`
            - `industrial_supplies`
            - `information_retrieval_services`
            - `insurance_default`
            - `insurance_underwriting_premiums`
            - `intra_company_purchases`
            - `jewelry_stores_watches_clocks_and_silverware_stores`
            - `landscaping_services`
            - `laundries`
            - `laundry_cleaning_services`
            - `legal_services_attorneys`
            - `luggage_and_leather_goods_stores`
            - `lumber_building_materials_stores`
            - `manual_cash_disburse`
            - `marinas_service_and_supplies`
            - `marketplaces`
            - `masonry_stonework_and_plaster`
            - `massage_parlors`
            - `medical_and_dental_labs`
            - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
            - `medical_services`
            - `membership_organizations`
            - `mens_and_boys_clothing_and_accessories_stores`
            - `mens_womens_clothing_stores`
            - `metal_service_centers`
            - `miscellaneous`
            - `miscellaneous_apparel_and_accessory_shops`
            - `miscellaneous_auto_dealers`
            - `miscellaneous_business_services`
            - `miscellaneous_food_stores`
            - `miscellaneous_general_merchandise`
            - `miscellaneous_general_services`
            - `miscellaneous_home_furnishing_specialty_stores`
            - `miscellaneous_publishing_and_printing`
            - `miscellaneous_recreation_services`
            - `miscellaneous_repair_shops`
            - `miscellaneous_specialty_retail`
            - `mobile_home_dealers`
            - `motion_picture_theaters`
            - `motor_freight_carriers_and_trucking`
            - `motor_homes_dealers`
            - `motor_vehicle_supplies_and_new_parts`
            - `motorcycle_shops_and_dealers`
            - `motorcycle_shops_dealers`
            - `music_stores_musical_instruments_pianos_and_sheet_music`
            - `news_dealers_and_newsstands`
            - `non_fi_money_orders`
            - `non_fi_stored_value_card_purchase_load`
            - `nondurable_goods`
            - `nurseries_lawn_and_garden_supply_stores`
            - `nursing_personal_care`
            - `office_and_commercial_furniture`
            - `opticians_eyeglasses`
            - `optometrists_ophthalmologist`
            - `orthopedic_goods_prosthetic_devices`
            - `osteopaths`
            - `package_stores_beer_wine_and_liquor`
            - `paints_varnishes_and_supplies`
            - `parking_lots_garages`
            - `passenger_railways`
            - `pawn_shops`
            - `pet_shops_pet_food_and_supplies`
            - `petroleum_and_petroleum_products`
            - `photo_developing`
            - `photographic_photocopy_microfilm_equipment_and_supplies`
            - `photographic_studios`
            - `picture_video_production`
            - `piece_goods_notions_and_other_dry_goods`
            - `plumbing_heating_equipment_and_supplies`
            - `political_organizations`
            - `postal_services_government_only`
            - `precious_stones_and_metals_watches_and_jewelry`
            - `professional_services`
            - `public_warehousing_and_storage`
            - `quick_copy_repro_and_blueprint`
            - `railroads`
            - `real_estate_agents_and_managers_rentals`
            - `record_stores`
            - `recreational_vehicle_rentals`
            - `religious_goods_stores`
            - `religious_organizations`
            - `roofing_siding_sheet_metal`
            - `secretarial_support_services`
            - `security_brokers_dealers`
            - `service_stations`
            - `sewing_needlework_fabric_and_piece_goods_stores`
            - `shoe_repair_hat_cleaning`
            - `shoe_stores`
            - `small_appliance_repair`
            - `snowmobile_dealers`
            - `special_trade_services`
            - `specialty_cleaning`
            - `sporting_goods_stores`
            - `sporting_recreation_camps`
            - `sports_and_riding_apparel_stores`
            - `sports_clubs_fields`
            - `stamp_and_coin_stores`
            - `stationary_office_supplies_printing_and_writing_paper`
            - `stationery_stores_office_and_school_supply_stores`
            - `swimming_pools_sales`
            - `t_ui_travel_germany`
            - `tailors_alterations`
            - `tax_payments_government_agencies`
            - `tax_preparation_services`
            - `taxicabs_limousines`
            - `telecommunication_equipment_and_telephone_sales`
            - `telecommunication_services`
            - `telegraph_services`
            - `tent_and_awning_shops`
            - `testing_laboratories`
            - `theatrical_ticket_agencies`
            - `timeshares`
            - `tire_retreading_and_repair`
            - `tolls_bridge_fees`
            - `tourist_attractions_and_exhibits`
            - `towing_services`
            - `trailer_parks_campgrounds`
            - `transportation_services`
            - `travel_agencies_tour_operators`
            - `truck_stop_iteration`
            - `truck_utility_trailer_rentals`
            - `typesetting_plate_making_and_related_services`
            - `typewriter_stores`
            - `u_s_federal_government_agencies_or_departments`
            - `uniforms_commercial_clothing`
            - `used_merchandise_and_secondhand_stores`
            - `utilities`
            - `variety_stores`
            - `veterinary_services`
            - `video_amusement_game_supplies`
            - `video_game_arcades`
            - `video_tape_rental_stores`
            - `vocational_trade_schools`
            - `watch_jewelry_repair`
            - `welding_repair`
            - `wholesale_clubs`
            - `wig_and_toupee_stores`
            - `wires_money_orders`
            - `womens_accessory_and_specialty_shops`
            - `womens_ready_to_wear_stores`
            - `wrecking_and_salvage_yards`

          - `flow_details.issuing_authorization.card.cardholder.spending_controls.blocked_merchant_countries` (array of strings, nullable)
            Array of strings containing representing countries from which authorizations will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value to unset this control.

          - `flow_details.issuing_authorization.card.cardholder.spending_controls.spending_limits` (array of objects, nullable)
            Limit spending with amount-based rules that apply across this cardholder’s cards.

            - `flow_details.issuing_authorization.card.cardholder.spending_controls.spending_limits.amount` (integer)
              Maximum amount allowed to spend per interval. This amount is in the card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

            - `flow_details.issuing_authorization.card.cardholder.spending_controls.spending_limits.categories` (array of enums, nullable)
              Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) this limit applies to. Omitting this field will apply the limit to all categories.
Possible enum values:
              - `ac_refrigeration_repair`
              - `accounting_bookkeeping_services`
              - `advertising_services`
              - `agricultural_cooperative`
              - `airlines_air_carriers`
              - `airports_flying_fields`
              - `ambulance_services`
              - `amusement_parks_carnivals`
              - `antique_reproductions`
              - `antique_shops`
              - `aquariums`
              - `architectural_surveying_services`
              - `art_dealers_and_galleries`
              - `artists_supply_and_craft_shops`
              - `auto_and_home_supply_stores`
              - `auto_body_repair_shops`
              - `auto_paint_shops`
              - `auto_service_shops`
              - `automated_cash_disburse`
              - `automated_fuel_dispensers`
              - `automobile_associations`
              - `automotive_parts_and_accessories_stores`
              - `automotive_tire_stores`
              - `bail_and_bond_payments`
              - `bakeries`
              - `bands_orchestras`
              - `barber_and_beauty_shops`
              - `betting_casino_gambling`
              - `bicycle_shops`
              - `billiard_pool_establishments`
              - `boat_dealers`
              - `boat_rentals_and_leases`
              - `book_stores`
              - `books_periodicals_and_newspapers`
              - `bowling_alleys`
              - `bus_lines`
              - `business_secretarial_schools`
              - `buying_shopping_services`
              - `cable_satellite_and_other_pay_television_and_radio`
              - `camera_and_photographic_supply_stores`
              - `candy_nut_and_confectionery_stores`
              - `car_and_truck_dealers_new_used`
              - `car_and_truck_dealers_used_only`
              - `car_rental_agencies`
              - `car_washes`
              - `carpentry_services`
              - `carpet_upholstery_cleaning`
              - `caterers`
              - `charitable_and_social_service_organizations_fundraising`
              - `chemicals_and_allied_products`
              - `child_care_services`
              - `childrens_and_infants_wear_stores`
              - `chiropodists_podiatrists`
              - `chiropractors`
              - `cigar_stores_and_stands`
              - `civic_social_fraternal_associations`
              - `cleaning_and_maintenance`
              - `clothing_rental`
              - `colleges_universities`
              - `commercial_equipment`
              - `commercial_footwear`
              - `commercial_photography_art_and_graphics`
              - `commuter_transport_and_ferries`
              - `computer_network_services`
              - `computer_programming`
              - `computer_repair`
              - `computer_software_stores`
              - `computers_peripherals_and_software`
              - `concrete_work_services`
              - `construction_materials`
              - `consulting_public_relations`
              - `correspondence_schools`
              - `cosmetic_stores`
              - `counseling_services`
              - `country_clubs`
              - `courier_services`
              - `court_costs`
              - `credit_reporting_agencies`
              - `cruise_lines`
              - `dairy_products_stores`
              - `dance_hall_studios_schools`
              - `dating_escort_services`
              - `dentists_orthodontists`
              - `department_stores`
              - `detective_agencies`
              - `digital_goods_applications`
              - `digital_goods_games`
              - `digital_goods_large_volume`
              - `digital_goods_media`
              - `direct_marketing_catalog_merchant`
              - `direct_marketing_combination_catalog_and_retail_merchant`
              - `direct_marketing_inbound_telemarketing`
              - `direct_marketing_insurance_services`
              - `direct_marketing_other`
              - `direct_marketing_outbound_telemarketing`
              - `direct_marketing_subscription`
              - `direct_marketing_travel`
              - `discount_stores`
              - `doctors`
              - `door_to_door_sales`
              - `drapery_window_covering_and_upholstery_stores`
              - `drinking_places`
              - `drug_stores_and_pharmacies`
              - `drugs_drug_proprietaries_and_druggist_sundries`
              - `dry_cleaners`
              - `durable_goods`
              - `duty_free_stores`
              - `eating_places_restaurants`
              - `educational_services`
              - `electric_razor_stores`
              - `electric_vehicle_charging`
              - `electrical_parts_and_equipment`
              - `electrical_services`
              - `electronics_repair_shops`
              - `electronics_stores`
              - `elementary_secondary_schools`
              - `emergency_services_gcas_visa_use_only`
              - `employment_temp_agencies`
              - `equipment_rental`
              - `exterminating_services`
              - `family_clothing_stores`
              - `fast_food_restaurants`
              - `financial_institutions`
              - `fines_government_administrative_entities`
              - `fireplace_fireplace_screens_and_accessories_stores`
              - `floor_covering_stores`
              - `florists`
              - `florists_supplies_nursery_stock_and_flowers`
              - `freezer_and_locker_meat_provisioners`
              - `fuel_dealers_non_automotive`
              - `funeral_services_crematories`
              - `furniture_home_furnishings_and_equipment_stores_except_appliances`
              - `furniture_repair_refinishing`
              - `furriers_and_fur_shops`
              - `general_services`
              - `gift_card_novelty_and_souvenir_shops`
              - `glass_paint_and_wallpaper_stores`
              - `glassware_crystal_stores`
              - `golf_courses_public`
              - `government_licensed_horse_dog_racing_us_region_only`
              - `government_licensed_online_casions_online_gambling_us_region_only`
              - `government_owned_lotteries_non_us_region`
              - `government_owned_lotteries_us_region_only`
              - `government_services`
              - `grocery_stores_supermarkets`
              - `hardware_equipment_and_supplies`
              - `hardware_stores`
              - `health_and_beauty_spas`
              - `hearing_aids_sales_and_supplies`
              - `heating_plumbing_a_c`
              - `hobby_toy_and_game_shops`
              - `home_supply_warehouse_stores`
              - `hospitals`
              - `hotels_motels_and_resorts`
              - `household_appliance_stores`
              - `industrial_supplies`
              - `information_retrieval_services`
              - `insurance_default`
              - `insurance_underwriting_premiums`
              - `intra_company_purchases`
              - `jewelry_stores_watches_clocks_and_silverware_stores`
              - `landscaping_services`
              - `laundries`
              - `laundry_cleaning_services`
              - `legal_services_attorneys`
              - `luggage_and_leather_goods_stores`
              - `lumber_building_materials_stores`
              - `manual_cash_disburse`
              - `marinas_service_and_supplies`
              - `marketplaces`
              - `masonry_stonework_and_plaster`
              - `massage_parlors`
              - `medical_and_dental_labs`
              - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
              - `medical_services`
              - `membership_organizations`
              - `mens_and_boys_clothing_and_accessories_stores`
              - `mens_womens_clothing_stores`
              - `metal_service_centers`
              - `miscellaneous`
              - `miscellaneous_apparel_and_accessory_shops`
              - `miscellaneous_auto_dealers`
              - `miscellaneous_business_services`
              - `miscellaneous_food_stores`
              - `miscellaneous_general_merchandise`
              - `miscellaneous_general_services`
              - `miscellaneous_home_furnishing_specialty_stores`
              - `miscellaneous_publishing_and_printing`
              - `miscellaneous_recreation_services`
              - `miscellaneous_repair_shops`
              - `miscellaneous_specialty_retail`
              - `mobile_home_dealers`
              - `motion_picture_theaters`
              - `motor_freight_carriers_and_trucking`
              - `motor_homes_dealers`
              - `motor_vehicle_supplies_and_new_parts`
              - `motorcycle_shops_and_dealers`
              - `motorcycle_shops_dealers`
              - `music_stores_musical_instruments_pianos_and_sheet_music`
              - `news_dealers_and_newsstands`
              - `non_fi_money_orders`
              - `non_fi_stored_value_card_purchase_load`
              - `nondurable_goods`
              - `nurseries_lawn_and_garden_supply_stores`
              - `nursing_personal_care`
              - `office_and_commercial_furniture`
              - `opticians_eyeglasses`
              - `optometrists_ophthalmologist`
              - `orthopedic_goods_prosthetic_devices`
              - `osteopaths`
              - `package_stores_beer_wine_and_liquor`
              - `paints_varnishes_and_supplies`
              - `parking_lots_garages`
              - `passenger_railways`
              - `pawn_shops`
              - `pet_shops_pet_food_and_supplies`
              - `petroleum_and_petroleum_products`
              - `photo_developing`
              - `photographic_photocopy_microfilm_equipment_and_supplies`
              - `photographic_studios`
              - `picture_video_production`
              - `piece_goods_notions_and_other_dry_goods`
              - `plumbing_heating_equipment_and_supplies`
              - `political_organizations`
              - `postal_services_government_only`
              - `precious_stones_and_metals_watches_and_jewelry`
              - `professional_services`
              - `public_warehousing_and_storage`
              - `quick_copy_repro_and_blueprint`
              - `railroads`
              - `real_estate_agents_and_managers_rentals`
              - `record_stores`
              - `recreational_vehicle_rentals`
              - `religious_goods_stores`
              - `religious_organizations`
              - `roofing_siding_sheet_metal`
              - `secretarial_support_services`
              - `security_brokers_dealers`
              - `service_stations`
              - `sewing_needlework_fabric_and_piece_goods_stores`
              - `shoe_repair_hat_cleaning`
              - `shoe_stores`
              - `small_appliance_repair`
              - `snowmobile_dealers`
              - `special_trade_services`
              - `specialty_cleaning`
              - `sporting_goods_stores`
              - `sporting_recreation_camps`
              - `sports_and_riding_apparel_stores`
              - `sports_clubs_fields`
              - `stamp_and_coin_stores`
              - `stationary_office_supplies_printing_and_writing_paper`
              - `stationery_stores_office_and_school_supply_stores`
              - `swimming_pools_sales`
              - `t_ui_travel_germany`
              - `tailors_alterations`
              - `tax_payments_government_agencies`
              - `tax_preparation_services`
              - `taxicabs_limousines`
              - `telecommunication_equipment_and_telephone_sales`
              - `telecommunication_services`
              - `telegraph_services`
              - `tent_and_awning_shops`
              - `testing_laboratories`
              - `theatrical_ticket_agencies`
              - `timeshares`
              - `tire_retreading_and_repair`
              - `tolls_bridge_fees`
              - `tourist_attractions_and_exhibits`
              - `towing_services`
              - `trailer_parks_campgrounds`
              - `transportation_services`
              - `travel_agencies_tour_operators`
              - `truck_stop_iteration`
              - `truck_utility_trailer_rentals`
              - `typesetting_plate_making_and_related_services`
              - `typewriter_stores`
              - `u_s_federal_government_agencies_or_departments`
              - `uniforms_commercial_clothing`
              - `used_merchandise_and_secondhand_stores`
              - `utilities`
              - `variety_stores`
              - `veterinary_services`
              - `video_amusement_game_supplies`
              - `video_game_arcades`
              - `video_tape_rental_stores`
              - `vocational_trade_schools`
              - `watch_jewelry_repair`
              - `welding_repair`
              - `wholesale_clubs`
              - `wig_and_toupee_stores`
              - `wires_money_orders`
              - `womens_accessory_and_specialty_shops`
              - `womens_ready_to_wear_stores`
              - `wrecking_and_salvage_yards`

            - `flow_details.issuing_authorization.card.cardholder.spending_controls.spending_limits.interval` (enum)
              Interval (or event) to which the amount applies.
Possible enum values:
              - `all_time`
                Limit applies to all transactions.

              - `daily`
                Limit applies to a day, starting at midnight UTC.

              - `monthly`
                Limit applies to a month, starting on the 1st at midnight UTC.

              - `per_authorization`
                Limit applies to each authorization.

              - `weekly`
                Limit applies to a week, starting on Sunday at midnight UTC.

              - `yearly`
                Limit applies to a year, starting on January 1st at midnight UTC.

          - `flow_details.issuing_authorization.card.cardholder.spending_controls.spending_limits_currency` (enum, nullable)
            Currency of the amounts within `spending_limits`.

        - `flow_details.issuing_authorization.card.cardholder.status` (enum)
          Specifies whether to permit authorizations on this cardholder’s cards.
Possible enum values:
          - `active`
            A platform has enabled the cardholder to approve authorizations made with their attached cards. However, if Stripe hasn’t yet verified the cardholder’s identity information, authorizations might still be blocked.

          - `blocked`
            Cards attached to this cardholder will decline all authorizations with the `cardholder_blocked` reason. This status is non-reversible.

          - `inactive`
            Cards attached to this cardholder will decline all authorizations with the `cardholder_inactive` reason.

        - `flow_details.issuing_authorization.card.cardholder.type` (enum)
          One of `individual` or `company`. See [Choose a cardholder type](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md) for more details.
Possible enum values:
          - `company`
            The cardholder is a company or business entity, and additional information includes their tax ID. This option may not be available if your [use case](https://docs.stripe.com/docs/issuing/other/choose-cardholder.md#find-your-use-case) only supports individual cardholders.

          - `individual`
            The cardholder is a person, and additional information includes first and last name, date of birth, etc. If you’re issuing Celtic Spend Cards, then Individual cardholders must accept Authorized User Terms prior to activating their card.

      - `flow_details.issuing_authorization.card.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `flow_details.issuing_authorization.card.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Supported currencies are `usd` in the US, `eur` in the EU, and `gbp` in the UK.

      - `flow_details.issuing_authorization.card.cvc` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The card’s CVC. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://docs.stripe.com/docs/api/expanding_objects.md). Additionally, it’s only available via the [“Retrieve a card” endpoint](https://docs.stripe.com/docs/api/issuing/cards/retrieve.md), not via “List all cards” or any other endpoint.

      - `flow_details.issuing_authorization.card.exp_month` (integer)
        The expiration month of the card.

      - `flow_details.issuing_authorization.card.exp_year` (integer)
        The expiration year of the card.

      - `flow_details.issuing_authorization.card.last4` (string)
        The last 4 digits of the card number.

      - `flow_details.issuing_authorization.card.latest_fraud_warning` (object, nullable)
        Stripe’s assessment of whether this card’s details have been compromised. If this property isn’t null, cancel and reissue the card to prevent fraudulent activity risk.

        - `flow_details.issuing_authorization.card.latest_fraud_warning.started_at` (timestamp, nullable)
          Timestamp of the most recent fraud warning.

        - `flow_details.issuing_authorization.card.latest_fraud_warning.type` (enum, nullable)
          The type of fraud warning that most recently took place on this card. This field updates with every new fraud warning, so the value changes over time. If populated, cancel and reissue the card.
Possible enum values:
          - `card_testing_exposure`
            The card’s credentials were used successfully in a card testing attempt. Requires [Advanced Fraud Tools](https://docs.stripe.com/docs/issuing/controls/advanced-fraud-tools.md).

          - `fraud_dispute_filed`
            The cardholder filed a fraud dispute for a transaction

          - `third_party_reported`
            The card was reported compromised by a third party

          - `user_indicated_fraud`
            The cardholder indicated that a fraudulent transaction occurred. Requires [Advanced Fraud Tools](https://docs.stripe.com/docs/issuing/controls/advanced-fraud-tools.md).

      - `flow_details.issuing_authorization.card.livemode` (boolean)
        If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

      - `flow_details.issuing_authorization.card.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `flow_details.issuing_authorization.card.number` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The full unredacted card number. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://docs.stripe.com/docs/api/expanding_objects.md). Additionally, it’s only available via the [“Retrieve a card” endpoint](https://docs.stripe.com/docs/api/issuing/cards/retrieve.md), not via “List all cards” or any other endpoint.

      - `flow_details.issuing_authorization.card.personalization_design` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The personalization design object belonging to this card.

      - `flow_details.issuing_authorization.card.replaced_by` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The latest card that replaces this card, if any.

      - `flow_details.issuing_authorization.card.replacement_for` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The card this card replaces, if any.

      - `flow_details.issuing_authorization.card.replacement_reason` (enum, nullable)
        The reason why the previous card needed to be replaced.
Possible enum values:
        - `damaged`
          The physical card has been damaged and cannot be used at terminals. This reason is only valid for cards of type `physical`.

        - `expired`
          The expiration date has passed or is imminent.

        - `lost`
          The card was lost. This status is only valid if the card it replaces is marked as lost.

        - `stolen`
          The card was stolen. This status is only valid if the card it replaces is marked as stolen.

      - `flow_details.issuing_authorization.card.second_line` (string, nullable)
        Text separate from cardholder name, printed on the card.

      - `flow_details.issuing_authorization.card.shipping` (object, nullable)
        Where and how the card will be shipped.

        - `flow_details.issuing_authorization.card.shipping.address` (object)
          Shipping address.

          - `flow_details.issuing_authorization.card.shipping.address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `flow_details.issuing_authorization.card.shipping.address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `flow_details.issuing_authorization.card.shipping.address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `flow_details.issuing_authorization.card.shipping.address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `flow_details.issuing_authorization.card.shipping.address.postal_code` (string, nullable)
            ZIP or postal code.

          - `flow_details.issuing_authorization.card.shipping.address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `flow_details.issuing_authorization.card.shipping.address_validation` (object, nullable)
          Address validation details for the shipment.

          - `flow_details.issuing_authorization.card.shipping.address_validation.mode` (enum)
            The address validation capabilities to use.
Possible enum values:
            - `disabled`
              The card will be shipped without validating or normalizing the shipping address.

            - `normalization_only`
              The card will be shipped with the normalized address without validation. Undeliverable addresses won’t be blocked.

            - `validation_and_normalization`
              The card will be shipped with the normalized, validated address. Undeliverable addresses will be blocked.

          - `flow_details.issuing_authorization.card.shipping.address_validation.normalized_address` (object, nullable)
            The normalized shipping address.

            - `flow_details.issuing_authorization.card.shipping.address_validation.normalized_address.city` (string, nullable)
              City, district, suburb, town, or village.

            - `flow_details.issuing_authorization.card.shipping.address_validation.normalized_address.country` (string, nullable)
              Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

            - `flow_details.issuing_authorization.card.shipping.address_validation.normalized_address.line1` (string, nullable)
              Address line 1, such as the street, PO Box, or company name.

            - `flow_details.issuing_authorization.card.shipping.address_validation.normalized_address.line2` (string, nullable)
              Address line 2, such as the apartment, suite, unit, or building.

            - `flow_details.issuing_authorization.card.shipping.address_validation.normalized_address.postal_code` (string, nullable)
              ZIP or postal code.

            - `flow_details.issuing_authorization.card.shipping.address_validation.normalized_address.state` (string, nullable)
              State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

          - `flow_details.issuing_authorization.card.shipping.address_validation.result` (enum, nullable)
            The validation result for the shipping address.
Possible enum values:
            - `indeterminate`
              The deliverability of the card’s shipping address could not be determined.

            - `likely_deliverable`
              The card’s shipping address is likely deliverable.

            - `likely_undeliverable`
              The card’s shipping address is likely undeliverable as submitted.

        - `flow_details.issuing_authorization.card.shipping.carrier` (enum, nullable)
          The delivery company that shipped a card.
Possible enum values:
          - `dhl`
            DHL

          - `fedex`
            FedEx

          - `royal_mail`
            Royal Mail

          - `usps`
            USPS

        - `flow_details.issuing_authorization.card.shipping.customs` (object, nullable)
          Additional information that may be required for clearing customs.

          - `flow_details.issuing_authorization.card.shipping.customs.eori_number` (string, nullable)
            A registration number used for customs in Europe. See <https://www.gov.uk/eori> for the UK and <https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en> for the EU.

        - `flow_details.issuing_authorization.card.shipping.eta` (timestamp, nullable)
          A unix timestamp representing a best estimate of when the card will be delivered.

        - `flow_details.issuing_authorization.card.shipping.name` (string)
          Recipient name.

        - `flow_details.issuing_authorization.card.shipping.phone_number` (string, nullable)
          The phone number of the receiver of the shipment. Our courier partners will use this number to contact you in the event of card delivery issues. For individual shipments to the EU/UK, if this field is empty, we will provide them with the phone number provided when the cardholder was initially created.

        - `flow_details.issuing_authorization.card.shipping.require_signature` (boolean, nullable)
          Whether a signature is required for card delivery. This feature is only supported for US users. Standard shipping service does not support signature on delivery. The default value for standard shipping service is false and for express and priority services is true.

        - `flow_details.issuing_authorization.card.shipping.service` (enum)
          Shipment service, such as `standard` or `express`.
Possible enum values:
          - `express`
            Cards arrive in 4 business days.

          - `priority`
            Cards arrive in 2-3 business days.

          - `standard`
            Cards arrive in 5-8 business days.

        - `flow_details.issuing_authorization.card.shipping.status` (enum, nullable)
          The delivery status of the card.
Possible enum values:
          - `canceled`
            The card was canceled before being shipped.

          - `delivered`
            The card has been delivered to its destination.

          - `failure`
            The card failed to be delivered but was not returned.

          - `pending`
            The card is being prepared and has not yet shipped.

          - `returned`
            The card failed to be delivered and was returned to the sender.

          - `shipped`
            The card has been shipped. If the card’s [shipping carrier](https://docs.stripe.com/docs/issuing/cards/physical.md#shipping-your-cards) does not support tracking, this will be the card’s final status.

          - `submitted`
            The card has been submitted to the printer for shipment.

        - `flow_details.issuing_authorization.card.shipping.tracking_number` (string, nullable)
          A tracking number for a card shipment.

        - `flow_details.issuing_authorization.card.shipping.tracking_url` (string, nullable)
          A link to the shipping carrier’s site where you can view detailed information about a card shipment.

        - `flow_details.issuing_authorization.card.shipping.type` (enum)
          Packaging options.
Possible enum values:
          - `bulk`
            Cards are grouped and mailed together.

          - `individual`
            Cards are sent individually in an envelope.

      - `flow_details.issuing_authorization.card.spending_controls` (object)
        Rules that control spending for this card. Refer to our [documentation](https://docs.stripe.com/docs/issuing/controls/spending-controls.md) for more details.

        - `flow_details.issuing_authorization.card.spending_controls.allowed_categories` (array of enums, nullable)
          Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to allow. All other categories will be blocked. Cannot be set with `blocked_categories`.
Possible enum values:
          - `ac_refrigeration_repair`
          - `accounting_bookkeeping_services`
          - `advertising_services`
          - `agricultural_cooperative`
          - `airlines_air_carriers`
          - `airports_flying_fields`
          - `ambulance_services`
          - `amusement_parks_carnivals`
          - `antique_reproductions`
          - `antique_shops`
          - `aquariums`
          - `architectural_surveying_services`
          - `art_dealers_and_galleries`
          - `artists_supply_and_craft_shops`
          - `auto_and_home_supply_stores`
          - `auto_body_repair_shops`
          - `auto_paint_shops`
          - `auto_service_shops`
          - `automated_cash_disburse`
          - `automated_fuel_dispensers`
          - `automobile_associations`
          - `automotive_parts_and_accessories_stores`
          - `automotive_tire_stores`
          - `bail_and_bond_payments`
          - `bakeries`
          - `bands_orchestras`
          - `barber_and_beauty_shops`
          - `betting_casino_gambling`
          - `bicycle_shops`
          - `billiard_pool_establishments`
          - `boat_dealers`
          - `boat_rentals_and_leases`
          - `book_stores`
          - `books_periodicals_and_newspapers`
          - `bowling_alleys`
          - `bus_lines`
          - `business_secretarial_schools`
          - `buying_shopping_services`
          - `cable_satellite_and_other_pay_television_and_radio`
          - `camera_and_photographic_supply_stores`
          - `candy_nut_and_confectionery_stores`
          - `car_and_truck_dealers_new_used`
          - `car_and_truck_dealers_used_only`
          - `car_rental_agencies`
          - `car_washes`
          - `carpentry_services`
          - `carpet_upholstery_cleaning`
          - `caterers`
          - `charitable_and_social_service_organizations_fundraising`
          - `chemicals_and_allied_products`
          - `child_care_services`
          - `childrens_and_infants_wear_stores`
          - `chiropodists_podiatrists`
          - `chiropractors`
          - `cigar_stores_and_stands`
          - `civic_social_fraternal_associations`
          - `cleaning_and_maintenance`
          - `clothing_rental`
          - `colleges_universities`
          - `commercial_equipment`
          - `commercial_footwear`
          - `commercial_photography_art_and_graphics`
          - `commuter_transport_and_ferries`
          - `computer_network_services`
          - `computer_programming`
          - `computer_repair`
          - `computer_software_stores`
          - `computers_peripherals_and_software`
          - `concrete_work_services`
          - `construction_materials`
          - `consulting_public_relations`
          - `correspondence_schools`
          - `cosmetic_stores`
          - `counseling_services`
          - `country_clubs`
          - `courier_services`
          - `court_costs`
          - `credit_reporting_agencies`
          - `cruise_lines`
          - `dairy_products_stores`
          - `dance_hall_studios_schools`
          - `dating_escort_services`
          - `dentists_orthodontists`
          - `department_stores`
          - `detective_agencies`
          - `digital_goods_applications`
          - `digital_goods_games`
          - `digital_goods_large_volume`
          - `digital_goods_media`
          - `direct_marketing_catalog_merchant`
          - `direct_marketing_combination_catalog_and_retail_merchant`
          - `direct_marketing_inbound_telemarketing`
          - `direct_marketing_insurance_services`
          - `direct_marketing_other`
          - `direct_marketing_outbound_telemarketing`
          - `direct_marketing_subscription`
          - `direct_marketing_travel`
          - `discount_stores`
          - `doctors`
          - `door_to_door_sales`
          - `drapery_window_covering_and_upholstery_stores`
          - `drinking_places`
          - `drug_stores_and_pharmacies`
          - `drugs_drug_proprietaries_and_druggist_sundries`
          - `dry_cleaners`
          - `durable_goods`
          - `duty_free_stores`
          - `eating_places_restaurants`
          - `educational_services`
          - `electric_razor_stores`
          - `electric_vehicle_charging`
          - `electrical_parts_and_equipment`
          - `electrical_services`
          - `electronics_repair_shops`
          - `electronics_stores`
          - `elementary_secondary_schools`
          - `emergency_services_gcas_visa_use_only`
          - `employment_temp_agencies`
          - `equipment_rental`
          - `exterminating_services`
          - `family_clothing_stores`
          - `fast_food_restaurants`
          - `financial_institutions`
          - `fines_government_administrative_entities`
          - `fireplace_fireplace_screens_and_accessories_stores`
          - `floor_covering_stores`
          - `florists`
          - `florists_supplies_nursery_stock_and_flowers`
          - `freezer_and_locker_meat_provisioners`
          - `fuel_dealers_non_automotive`
          - `funeral_services_crematories`
          - `furniture_home_furnishings_and_equipment_stores_except_appliances`
          - `furniture_repair_refinishing`
          - `furriers_and_fur_shops`
          - `general_services`
          - `gift_card_novelty_and_souvenir_shops`
          - `glass_paint_and_wallpaper_stores`
          - `glassware_crystal_stores`
          - `golf_courses_public`
          - `government_licensed_horse_dog_racing_us_region_only`
          - `government_licensed_online_casions_online_gambling_us_region_only`
          - `government_owned_lotteries_non_us_region`
          - `government_owned_lotteries_us_region_only`
          - `government_services`
          - `grocery_stores_supermarkets`
          - `hardware_equipment_and_supplies`
          - `hardware_stores`
          - `health_and_beauty_spas`
          - `hearing_aids_sales_and_supplies`
          - `heating_plumbing_a_c`
          - `hobby_toy_and_game_shops`
          - `home_supply_warehouse_stores`
          - `hospitals`
          - `hotels_motels_and_resorts`
          - `household_appliance_stores`
          - `industrial_supplies`
          - `information_retrieval_services`
          - `insurance_default`
          - `insurance_underwriting_premiums`
          - `intra_company_purchases`
          - `jewelry_stores_watches_clocks_and_silverware_stores`
          - `landscaping_services`
          - `laundries`
          - `laundry_cleaning_services`
          - `legal_services_attorneys`
          - `luggage_and_leather_goods_stores`
          - `lumber_building_materials_stores`
          - `manual_cash_disburse`
          - `marinas_service_and_supplies`
          - `marketplaces`
          - `masonry_stonework_and_plaster`
          - `massage_parlors`
          - `medical_and_dental_labs`
          - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
          - `medical_services`
          - `membership_organizations`
          - `mens_and_boys_clothing_and_accessories_stores`
          - `mens_womens_clothing_stores`
          - `metal_service_centers`
          - `miscellaneous`
          - `miscellaneous_apparel_and_accessory_shops`
          - `miscellaneous_auto_dealers`
          - `miscellaneous_business_services`
          - `miscellaneous_food_stores`
          - `miscellaneous_general_merchandise`
          - `miscellaneous_general_services`
          - `miscellaneous_home_furnishing_specialty_stores`
          - `miscellaneous_publishing_and_printing`
          - `miscellaneous_recreation_services`
          - `miscellaneous_repair_shops`
          - `miscellaneous_specialty_retail`
          - `mobile_home_dealers`
          - `motion_picture_theaters`
          - `motor_freight_carriers_and_trucking`
          - `motor_homes_dealers`
          - `motor_vehicle_supplies_and_new_parts`
          - `motorcycle_shops_and_dealers`
          - `motorcycle_shops_dealers`
          - `music_stores_musical_instruments_pianos_and_sheet_music`
          - `news_dealers_and_newsstands`
          - `non_fi_money_orders`
          - `non_fi_stored_value_card_purchase_load`
          - `nondurable_goods`
          - `nurseries_lawn_and_garden_supply_stores`
          - `nursing_personal_care`
          - `office_and_commercial_furniture`
          - `opticians_eyeglasses`
          - `optometrists_ophthalmologist`
          - `orthopedic_goods_prosthetic_devices`
          - `osteopaths`
          - `package_stores_beer_wine_and_liquor`
          - `paints_varnishes_and_supplies`
          - `parking_lots_garages`
          - `passenger_railways`
          - `pawn_shops`
          - `pet_shops_pet_food_and_supplies`
          - `petroleum_and_petroleum_products`
          - `photo_developing`
          - `photographic_photocopy_microfilm_equipment_and_supplies`
          - `photographic_studios`
          - `picture_video_production`
          - `piece_goods_notions_and_other_dry_goods`
          - `plumbing_heating_equipment_and_supplies`
          - `political_organizations`
          - `postal_services_government_only`
          - `precious_stones_and_metals_watches_and_jewelry`
          - `professional_services`
          - `public_warehousing_and_storage`
          - `quick_copy_repro_and_blueprint`
          - `railroads`
          - `real_estate_agents_and_managers_rentals`
          - `record_stores`
          - `recreational_vehicle_rentals`
          - `religious_goods_stores`
          - `religious_organizations`
          - `roofing_siding_sheet_metal`
          - `secretarial_support_services`
          - `security_brokers_dealers`
          - `service_stations`
          - `sewing_needlework_fabric_and_piece_goods_stores`
          - `shoe_repair_hat_cleaning`
          - `shoe_stores`
          - `small_appliance_repair`
          - `snowmobile_dealers`
          - `special_trade_services`
          - `specialty_cleaning`
          - `sporting_goods_stores`
          - `sporting_recreation_camps`
          - `sports_and_riding_apparel_stores`
          - `sports_clubs_fields`
          - `stamp_and_coin_stores`
          - `stationary_office_supplies_printing_and_writing_paper`
          - `stationery_stores_office_and_school_supply_stores`
          - `swimming_pools_sales`
          - `t_ui_travel_germany`
          - `tailors_alterations`
          - `tax_payments_government_agencies`
          - `tax_preparation_services`
          - `taxicabs_limousines`
          - `telecommunication_equipment_and_telephone_sales`
          - `telecommunication_services`
          - `telegraph_services`
          - `tent_and_awning_shops`
          - `testing_laboratories`
          - `theatrical_ticket_agencies`
          - `timeshares`
          - `tire_retreading_and_repair`
          - `tolls_bridge_fees`
          - `tourist_attractions_and_exhibits`
          - `towing_services`
          - `trailer_parks_campgrounds`
          - `transportation_services`
          - `travel_agencies_tour_operators`
          - `truck_stop_iteration`
          - `truck_utility_trailer_rentals`
          - `typesetting_plate_making_and_related_services`
          - `typewriter_stores`
          - `u_s_federal_government_agencies_or_departments`
          - `uniforms_commercial_clothing`
          - `used_merchandise_and_secondhand_stores`
          - `utilities`
          - `variety_stores`
          - `veterinary_services`
          - `video_amusement_game_supplies`
          - `video_game_arcades`
          - `video_tape_rental_stores`
          - `vocational_trade_schools`
          - `watch_jewelry_repair`
          - `welding_repair`
          - `wholesale_clubs`
          - `wig_and_toupee_stores`
          - `wires_money_orders`
          - `womens_accessory_and_specialty_shops`
          - `womens_ready_to_wear_stores`
          - `wrecking_and_salvage_yards`

        - `flow_details.issuing_authorization.card.spending_controls.allowed_merchant_countries` (array of strings, nullable)
          Array of strings containing representing countries from which authorizations will be allowed. Authorizations from merchants in all other countries will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset this control.

        - `flow_details.issuing_authorization.card.spending_controls.blocked_categories` (array of enums, nullable)
          Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) of authorizations to decline. All other categories will be allowed. Cannot be set with `allowed_categories`.
Possible enum values:
          - `ac_refrigeration_repair`
          - `accounting_bookkeeping_services`
          - `advertising_services`
          - `agricultural_cooperative`
          - `airlines_air_carriers`
          - `airports_flying_fields`
          - `ambulance_services`
          - `amusement_parks_carnivals`
          - `antique_reproductions`
          - `antique_shops`
          - `aquariums`
          - `architectural_surveying_services`
          - `art_dealers_and_galleries`
          - `artists_supply_and_craft_shops`
          - `auto_and_home_supply_stores`
          - `auto_body_repair_shops`
          - `auto_paint_shops`
          - `auto_service_shops`
          - `automated_cash_disburse`
          - `automated_fuel_dispensers`
          - `automobile_associations`
          - `automotive_parts_and_accessories_stores`
          - `automotive_tire_stores`
          - `bail_and_bond_payments`
          - `bakeries`
          - `bands_orchestras`
          - `barber_and_beauty_shops`
          - `betting_casino_gambling`
          - `bicycle_shops`
          - `billiard_pool_establishments`
          - `boat_dealers`
          - `boat_rentals_and_leases`
          - `book_stores`
          - `books_periodicals_and_newspapers`
          - `bowling_alleys`
          - `bus_lines`
          - `business_secretarial_schools`
          - `buying_shopping_services`
          - `cable_satellite_and_other_pay_television_and_radio`
          - `camera_and_photographic_supply_stores`
          - `candy_nut_and_confectionery_stores`
          - `car_and_truck_dealers_new_used`
          - `car_and_truck_dealers_used_only`
          - `car_rental_agencies`
          - `car_washes`
          - `carpentry_services`
          - `carpet_upholstery_cleaning`
          - `caterers`
          - `charitable_and_social_service_organizations_fundraising`
          - `chemicals_and_allied_products`
          - `child_care_services`
          - `childrens_and_infants_wear_stores`
          - `chiropodists_podiatrists`
          - `chiropractors`
          - `cigar_stores_and_stands`
          - `civic_social_fraternal_associations`
          - `cleaning_and_maintenance`
          - `clothing_rental`
          - `colleges_universities`
          - `commercial_equipment`
          - `commercial_footwear`
          - `commercial_photography_art_and_graphics`
          - `commuter_transport_and_ferries`
          - `computer_network_services`
          - `computer_programming`
          - `computer_repair`
          - `computer_software_stores`
          - `computers_peripherals_and_software`
          - `concrete_work_services`
          - `construction_materials`
          - `consulting_public_relations`
          - `correspondence_schools`
          - `cosmetic_stores`
          - `counseling_services`
          - `country_clubs`
          - `courier_services`
          - `court_costs`
          - `credit_reporting_agencies`
          - `cruise_lines`
          - `dairy_products_stores`
          - `dance_hall_studios_schools`
          - `dating_escort_services`
          - `dentists_orthodontists`
          - `department_stores`
          - `detective_agencies`
          - `digital_goods_applications`
          - `digital_goods_games`
          - `digital_goods_large_volume`
          - `digital_goods_media`
          - `direct_marketing_catalog_merchant`
          - `direct_marketing_combination_catalog_and_retail_merchant`
          - `direct_marketing_inbound_telemarketing`
          - `direct_marketing_insurance_services`
          - `direct_marketing_other`
          - `direct_marketing_outbound_telemarketing`
          - `direct_marketing_subscription`
          - `direct_marketing_travel`
          - `discount_stores`
          - `doctors`
          - `door_to_door_sales`
          - `drapery_window_covering_and_upholstery_stores`
          - `drinking_places`
          - `drug_stores_and_pharmacies`
          - `drugs_drug_proprietaries_and_druggist_sundries`
          - `dry_cleaners`
          - `durable_goods`
          - `duty_free_stores`
          - `eating_places_restaurants`
          - `educational_services`
          - `electric_razor_stores`
          - `electric_vehicle_charging`
          - `electrical_parts_and_equipment`
          - `electrical_services`
          - `electronics_repair_shops`
          - `electronics_stores`
          - `elementary_secondary_schools`
          - `emergency_services_gcas_visa_use_only`
          - `employment_temp_agencies`
          - `equipment_rental`
          - `exterminating_services`
          - `family_clothing_stores`
          - `fast_food_restaurants`
          - `financial_institutions`
          - `fines_government_administrative_entities`
          - `fireplace_fireplace_screens_and_accessories_stores`
          - `floor_covering_stores`
          - `florists`
          - `florists_supplies_nursery_stock_and_flowers`
          - `freezer_and_locker_meat_provisioners`
          - `fuel_dealers_non_automotive`
          - `funeral_services_crematories`
          - `furniture_home_furnishings_and_equipment_stores_except_appliances`
          - `furniture_repair_refinishing`
          - `furriers_and_fur_shops`
          - `general_services`
          - `gift_card_novelty_and_souvenir_shops`
          - `glass_paint_and_wallpaper_stores`
          - `glassware_crystal_stores`
          - `golf_courses_public`
          - `government_licensed_horse_dog_racing_us_region_only`
          - `government_licensed_online_casions_online_gambling_us_region_only`
          - `government_owned_lotteries_non_us_region`
          - `government_owned_lotteries_us_region_only`
          - `government_services`
          - `grocery_stores_supermarkets`
          - `hardware_equipment_and_supplies`
          - `hardware_stores`
          - `health_and_beauty_spas`
          - `hearing_aids_sales_and_supplies`
          - `heating_plumbing_a_c`
          - `hobby_toy_and_game_shops`
          - `home_supply_warehouse_stores`
          - `hospitals`
          - `hotels_motels_and_resorts`
          - `household_appliance_stores`
          - `industrial_supplies`
          - `information_retrieval_services`
          - `insurance_default`
          - `insurance_underwriting_premiums`
          - `intra_company_purchases`
          - `jewelry_stores_watches_clocks_and_silverware_stores`
          - `landscaping_services`
          - `laundries`
          - `laundry_cleaning_services`
          - `legal_services_attorneys`
          - `luggage_and_leather_goods_stores`
          - `lumber_building_materials_stores`
          - `manual_cash_disburse`
          - `marinas_service_and_supplies`
          - `marketplaces`
          - `masonry_stonework_and_plaster`
          - `massage_parlors`
          - `medical_and_dental_labs`
          - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
          - `medical_services`
          - `membership_organizations`
          - `mens_and_boys_clothing_and_accessories_stores`
          - `mens_womens_clothing_stores`
          - `metal_service_centers`
          - `miscellaneous`
          - `miscellaneous_apparel_and_accessory_shops`
          - `miscellaneous_auto_dealers`
          - `miscellaneous_business_services`
          - `miscellaneous_food_stores`
          - `miscellaneous_general_merchandise`
          - `miscellaneous_general_services`
          - `miscellaneous_home_furnishing_specialty_stores`
          - `miscellaneous_publishing_and_printing`
          - `miscellaneous_recreation_services`
          - `miscellaneous_repair_shops`
          - `miscellaneous_specialty_retail`
          - `mobile_home_dealers`
          - `motion_picture_theaters`
          - `motor_freight_carriers_and_trucking`
          - `motor_homes_dealers`
          - `motor_vehicle_supplies_and_new_parts`
          - `motorcycle_shops_and_dealers`
          - `motorcycle_shops_dealers`
          - `music_stores_musical_instruments_pianos_and_sheet_music`
          - `news_dealers_and_newsstands`
          - `non_fi_money_orders`
          - `non_fi_stored_value_card_purchase_load`
          - `nondurable_goods`
          - `nurseries_lawn_and_garden_supply_stores`
          - `nursing_personal_care`
          - `office_and_commercial_furniture`
          - `opticians_eyeglasses`
          - `optometrists_ophthalmologist`
          - `orthopedic_goods_prosthetic_devices`
          - `osteopaths`
          - `package_stores_beer_wine_and_liquor`
          - `paints_varnishes_and_supplies`
          - `parking_lots_garages`
          - `passenger_railways`
          - `pawn_shops`
          - `pet_shops_pet_food_and_supplies`
          - `petroleum_and_petroleum_products`
          - `photo_developing`
          - `photographic_photocopy_microfilm_equipment_and_supplies`
          - `photographic_studios`
          - `picture_video_production`
          - `piece_goods_notions_and_other_dry_goods`
          - `plumbing_heating_equipment_and_supplies`
          - `political_organizations`
          - `postal_services_government_only`
          - `precious_stones_and_metals_watches_and_jewelry`
          - `professional_services`
          - `public_warehousing_and_storage`
          - `quick_copy_repro_and_blueprint`
          - `railroads`
          - `real_estate_agents_and_managers_rentals`
          - `record_stores`
          - `recreational_vehicle_rentals`
          - `religious_goods_stores`
          - `religious_organizations`
          - `roofing_siding_sheet_metal`
          - `secretarial_support_services`
          - `security_brokers_dealers`
          - `service_stations`
          - `sewing_needlework_fabric_and_piece_goods_stores`
          - `shoe_repair_hat_cleaning`
          - `shoe_stores`
          - `small_appliance_repair`
          - `snowmobile_dealers`
          - `special_trade_services`
          - `specialty_cleaning`
          - `sporting_goods_stores`
          - `sporting_recreation_camps`
          - `sports_and_riding_apparel_stores`
          - `sports_clubs_fields`
          - `stamp_and_coin_stores`
          - `stationary_office_supplies_printing_and_writing_paper`
          - `stationery_stores_office_and_school_supply_stores`
          - `swimming_pools_sales`
          - `t_ui_travel_germany`
          - `tailors_alterations`
          - `tax_payments_government_agencies`
          - `tax_preparation_services`
          - `taxicabs_limousines`
          - `telecommunication_equipment_and_telephone_sales`
          - `telecommunication_services`
          - `telegraph_services`
          - `tent_and_awning_shops`
          - `testing_laboratories`
          - `theatrical_ticket_agencies`
          - `timeshares`
          - `tire_retreading_and_repair`
          - `tolls_bridge_fees`
          - `tourist_attractions_and_exhibits`
          - `towing_services`
          - `trailer_parks_campgrounds`
          - `transportation_services`
          - `travel_agencies_tour_operators`
          - `truck_stop_iteration`
          - `truck_utility_trailer_rentals`
          - `typesetting_plate_making_and_related_services`
          - `typewriter_stores`
          - `u_s_federal_government_agencies_or_departments`
          - `uniforms_commercial_clothing`
          - `used_merchandise_and_secondhand_stores`
          - `utilities`
          - `variety_stores`
          - `veterinary_services`
          - `video_amusement_game_supplies`
          - `video_game_arcades`
          - `video_tape_rental_stores`
          - `vocational_trade_schools`
          - `watch_jewelry_repair`
          - `welding_repair`
          - `wholesale_clubs`
          - `wig_and_toupee_stores`
          - `wires_money_orders`
          - `womens_accessory_and_specialty_shops`
          - `womens_ready_to_wear_stores`
          - `wrecking_and_salvage_yards`

        - `flow_details.issuing_authorization.card.spending_controls.blocked_merchant_countries` (array of strings, nullable)
          Array of strings containing representing countries from which authorizations will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value to unset this control.

        - `flow_details.issuing_authorization.card.spending_controls.spending_limits` (array of objects, nullable)
          Limit spending with amount-based rules that apply across any cards this card replaced (i.e., its `replacement_for` card and *that* card’s `replacement_for` card, up the chain).

          - `flow_details.issuing_authorization.card.spending_controls.spending_limits.amount` (integer)
            Maximum amount allowed to spend per interval. This amount is in the card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

          - `flow_details.issuing_authorization.card.spending_controls.spending_limits.categories` (array of enums, nullable)
            Array of strings containing [categories](https://docs.stripe.com/docs/api.md#issuing_authorization_object-merchant_data-category) this limit applies to. Omitting this field will apply the limit to all categories.
Possible enum values:
            - `ac_refrigeration_repair`
            - `accounting_bookkeeping_services`
            - `advertising_services`
            - `agricultural_cooperative`
            - `airlines_air_carriers`
            - `airports_flying_fields`
            - `ambulance_services`
            - `amusement_parks_carnivals`
            - `antique_reproductions`
            - `antique_shops`
            - `aquariums`
            - `architectural_surveying_services`
            - `art_dealers_and_galleries`
            - `artists_supply_and_craft_shops`
            - `auto_and_home_supply_stores`
            - `auto_body_repair_shops`
            - `auto_paint_shops`
            - `auto_service_shops`
            - `automated_cash_disburse`
            - `automated_fuel_dispensers`
            - `automobile_associations`
            - `automotive_parts_and_accessories_stores`
            - `automotive_tire_stores`
            - `bail_and_bond_payments`
            - `bakeries`
            - `bands_orchestras`
            - `barber_and_beauty_shops`
            - `betting_casino_gambling`
            - `bicycle_shops`
            - `billiard_pool_establishments`
            - `boat_dealers`
            - `boat_rentals_and_leases`
            - `book_stores`
            - `books_periodicals_and_newspapers`
            - `bowling_alleys`
            - `bus_lines`
            - `business_secretarial_schools`
            - `buying_shopping_services`
            - `cable_satellite_and_other_pay_television_and_radio`
            - `camera_and_photographic_supply_stores`
            - `candy_nut_and_confectionery_stores`
            - `car_and_truck_dealers_new_used`
            - `car_and_truck_dealers_used_only`
            - `car_rental_agencies`
            - `car_washes`
            - `carpentry_services`
            - `carpet_upholstery_cleaning`
            - `caterers`
            - `charitable_and_social_service_organizations_fundraising`
            - `chemicals_and_allied_products`
            - `child_care_services`
            - `childrens_and_infants_wear_stores`
            - `chiropodists_podiatrists`
            - `chiropractors`
            - `cigar_stores_and_stands`
            - `civic_social_fraternal_associations`
            - `cleaning_and_maintenance`
            - `clothing_rental`
            - `colleges_universities`
            - `commercial_equipment`
            - `commercial_footwear`
            - `commercial_photography_art_and_graphics`
            - `commuter_transport_and_ferries`
            - `computer_network_services`
            - `computer_programming`
            - `computer_repair`
            - `computer_software_stores`
            - `computers_peripherals_and_software`
            - `concrete_work_services`
            - `construction_materials`
            - `consulting_public_relations`
            - `correspondence_schools`
            - `cosmetic_stores`
            - `counseling_services`
            - `country_clubs`
            - `courier_services`
            - `court_costs`
            - `credit_reporting_agencies`
            - `cruise_lines`
            - `dairy_products_stores`
            - `dance_hall_studios_schools`
            - `dating_escort_services`
            - `dentists_orthodontists`
            - `department_stores`
            - `detective_agencies`
            - `digital_goods_applications`
            - `digital_goods_games`
            - `digital_goods_large_volume`
            - `digital_goods_media`
            - `direct_marketing_catalog_merchant`
            - `direct_marketing_combination_catalog_and_retail_merchant`
            - `direct_marketing_inbound_telemarketing`
            - `direct_marketing_insurance_services`
            - `direct_marketing_other`
            - `direct_marketing_outbound_telemarketing`
            - `direct_marketing_subscription`
            - `direct_marketing_travel`
            - `discount_stores`
            - `doctors`
            - `door_to_door_sales`
            - `drapery_window_covering_and_upholstery_stores`
            - `drinking_places`
            - `drug_stores_and_pharmacies`
            - `drugs_drug_proprietaries_and_druggist_sundries`
            - `dry_cleaners`
            - `durable_goods`
            - `duty_free_stores`
            - `eating_places_restaurants`
            - `educational_services`
            - `electric_razor_stores`
            - `electric_vehicle_charging`
            - `electrical_parts_and_equipment`
            - `electrical_services`
            - `electronics_repair_shops`
            - `electronics_stores`
            - `elementary_secondary_schools`
            - `emergency_services_gcas_visa_use_only`
            - `employment_temp_agencies`
            - `equipment_rental`
            - `exterminating_services`
            - `family_clothing_stores`
            - `fast_food_restaurants`
            - `financial_institutions`
            - `fines_government_administrative_entities`
            - `fireplace_fireplace_screens_and_accessories_stores`
            - `floor_covering_stores`
            - `florists`
            - `florists_supplies_nursery_stock_and_flowers`
            - `freezer_and_locker_meat_provisioners`
            - `fuel_dealers_non_automotive`
            - `funeral_services_crematories`
            - `furniture_home_furnishings_and_equipment_stores_except_appliances`
            - `furniture_repair_refinishing`
            - `furriers_and_fur_shops`
            - `general_services`
            - `gift_card_novelty_and_souvenir_shops`
            - `glass_paint_and_wallpaper_stores`
            - `glassware_crystal_stores`
            - `golf_courses_public`
            - `government_licensed_horse_dog_racing_us_region_only`
            - `government_licensed_online_casions_online_gambling_us_region_only`
            - `government_owned_lotteries_non_us_region`
            - `government_owned_lotteries_us_region_only`
            - `government_services`
            - `grocery_stores_supermarkets`
            - `hardware_equipment_and_supplies`
            - `hardware_stores`
            - `health_and_beauty_spas`
            - `hearing_aids_sales_and_supplies`
            - `heating_plumbing_a_c`
            - `hobby_toy_and_game_shops`
            - `home_supply_warehouse_stores`
            - `hospitals`
            - `hotels_motels_and_resorts`
            - `household_appliance_stores`
            - `industrial_supplies`
            - `information_retrieval_services`
            - `insurance_default`
            - `insurance_underwriting_premiums`
            - `intra_company_purchases`
            - `jewelry_stores_watches_clocks_and_silverware_stores`
            - `landscaping_services`
            - `laundries`
            - `laundry_cleaning_services`
            - `legal_services_attorneys`
            - `luggage_and_leather_goods_stores`
            - `lumber_building_materials_stores`
            - `manual_cash_disburse`
            - `marinas_service_and_supplies`
            - `marketplaces`
            - `masonry_stonework_and_plaster`
            - `massage_parlors`
            - `medical_and_dental_labs`
            - `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`
            - `medical_services`
            - `membership_organizations`
            - `mens_and_boys_clothing_and_accessories_stores`
            - `mens_womens_clothing_stores`
            - `metal_service_centers`
            - `miscellaneous`
            - `miscellaneous_apparel_and_accessory_shops`
            - `miscellaneous_auto_dealers`
            - `miscellaneous_business_services`
            - `miscellaneous_food_stores`
            - `miscellaneous_general_merchandise`
            - `miscellaneous_general_services`
            - `miscellaneous_home_furnishing_specialty_stores`
            - `miscellaneous_publishing_and_printing`
            - `miscellaneous_recreation_services`
            - `miscellaneous_repair_shops`
            - `miscellaneous_specialty_retail`
            - `mobile_home_dealers`
            - `motion_picture_theaters`
            - `motor_freight_carriers_and_trucking`
            - `motor_homes_dealers`
            - `motor_vehicle_supplies_and_new_parts`
            - `motorcycle_shops_and_dealers`
            - `motorcycle_shops_dealers`
            - `music_stores_musical_instruments_pianos_and_sheet_music`
            - `news_dealers_and_newsstands`
            - `non_fi_money_orders`
            - `non_fi_stored_value_card_purchase_load`
            - `nondurable_goods`
            - `nurseries_lawn_and_garden_supply_stores`
            - `nursing_personal_care`
            - `office_and_commercial_furniture`
            - `opticians_eyeglasses`
            - `optometrists_ophthalmologist`
            - `orthopedic_goods_prosthetic_devices`
            - `osteopaths`
            - `package_stores_beer_wine_and_liquor`
            - `paints_varnishes_and_supplies`
            - `parking_lots_garages`
            - `passenger_railways`
            - `pawn_shops`
            - `pet_shops_pet_food_and_supplies`
            - `petroleum_and_petroleum_products`
            - `photo_developing`
            - `photographic_photocopy_microfilm_equipment_and_supplies`
            - `photographic_studios`
            - `picture_video_production`
            - `piece_goods_notions_and_other_dry_goods`
            - `plumbing_heating_equipment_and_supplies`
            - `political_organizations`
            - `postal_services_government_only`
            - `precious_stones_and_metals_watches_and_jewelry`
            - `professional_services`
            - `public_warehousing_and_storage`
            - `quick_copy_repro_and_blueprint`
            - `railroads`
            - `real_estate_agents_and_managers_rentals`
            - `record_stores`
            - `recreational_vehicle_rentals`
            - `religious_goods_stores`
            - `religious_organizations`
            - `roofing_siding_sheet_metal`
            - `secretarial_support_services`
            - `security_brokers_dealers`
            - `service_stations`
            - `sewing_needlework_fabric_and_piece_goods_stores`
            - `shoe_repair_hat_cleaning`
            - `shoe_stores`
            - `small_appliance_repair`
            - `snowmobile_dealers`
            - `special_trade_services`
            - `specialty_cleaning`
            - `sporting_goods_stores`
            - `sporting_recreation_camps`
            - `sports_and_riding_apparel_stores`
            - `sports_clubs_fields`
            - `stamp_and_coin_stores`
            - `stationary_office_supplies_printing_and_writing_paper`
            - `stationery_stores_office_and_school_supply_stores`
            - `swimming_pools_sales`
            - `t_ui_travel_germany`
            - `tailors_alterations`
            - `tax_payments_government_agencies`
            - `tax_preparation_services`
            - `taxicabs_limousines`
            - `telecommunication_equipment_and_telephone_sales`
            - `telecommunication_services`
            - `telegraph_services`
            - `tent_and_awning_shops`
            - `testing_laboratories`
            - `theatrical_ticket_agencies`
            - `timeshares`
            - `tire_retreading_and_repair`
            - `tolls_bridge_fees`
            - `tourist_attractions_and_exhibits`
            - `towing_services`
            - `trailer_parks_campgrounds`
            - `transportation_services`
            - `travel_agencies_tour_operators`
            - `truck_stop_iteration`
            - `truck_utility_trailer_rentals`
            - `typesetting_plate_making_and_related_services`
            - `typewriter_stores`
            - `u_s_federal_government_agencies_or_departments`
            - `uniforms_commercial_clothing`
            - `used_merchandise_and_secondhand_stores`
            - `utilities`
            - `variety_stores`
            - `veterinary_services`
            - `video_amusement_game_supplies`
            - `video_game_arcades`
            - `video_tape_rental_stores`
            - `vocational_trade_schools`
            - `watch_jewelry_repair`
            - `welding_repair`
            - `wholesale_clubs`
            - `wig_and_toupee_stores`
            - `wires_money_orders`
            - `womens_accessory_and_specialty_shops`
            - `womens_ready_to_wear_stores`
            - `wrecking_and_salvage_yards`

          - `flow_details.issuing_authorization.card.spending_controls.spending_limits.interval` (enum)
            Interval (or event) to which the amount applies.
Possible enum values:
            - `all_time`
              Limit applies to all transactions.

            - `daily`
              Limit applies to a day, starting at midnight UTC.

            - `monthly`
              Limit applies to a month, starting on the 1st at midnight UTC.

            - `per_authorization`
              Limit applies to each authorization.

            - `weekly`
              Limit applies to a week, starting on Sunday at midnight UTC.

            - `yearly`
              Limit applies to a year, starting on January 1st at midnight UTC.

        - `flow_details.issuing_authorization.card.spending_controls.spending_limits_currency` (enum, nullable)
          Currency of the amounts within `spending_limits`. Always the same as the currency of the card.

      - `flow_details.issuing_authorization.card.status` (enum)
        Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`.
Possible enum values:
        - `active`
          The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

        - `canceled`
          The card will decline authorizations with the `card_canceled` reason. This status is permanent.

        - `inactive`
          The card will decline authorizations with the `card_inactive` reason.

      - `flow_details.issuing_authorization.card.type` (enum)
        The type of the card.
Possible enum values:
        - `physical`
          A physical card will be printed and shipped. It can be used at physical terminals.

        - `virtual`
          No physical card will be printed. The card can be used online and can be [added to digital wallets](https://stripe.com/docs/issuing/cards/digital-wallets).

      - `flow_details.issuing_authorization.card.wallets` (object, nullable)
        Information relating to digital wallets (like Apple Pay and Google Pay).

        - `flow_details.issuing_authorization.card.wallets.apple_pay` (object)
          Apple Pay Details

          - `flow_details.issuing_authorization.card.wallets.apple_pay.eligible` (boolean)
            Apple Pay Eligibility

          - `flow_details.issuing_authorization.card.wallets.apple_pay.ineligible_reason` (enum, nullable)
            Reason the card is ineligible for Apple Pay
Possible enum values:
            - `missing_agreement`
              Apple Pay is not enabled for your account.

            - `missing_cardholder_contact`
              Cardholder phone number or email required.

            - `unsupported_region`
              Apple Pay is not supported in the cardholder’s country.

        - `flow_details.issuing_authorization.card.wallets.google_pay` (object)
          Google Pay Details

          - `flow_details.issuing_authorization.card.wallets.google_pay.eligible` (boolean)
            Google Pay Eligibility

          - `flow_details.issuing_authorization.card.wallets.google_pay.ineligible_reason` (enum, nullable)
            Reason the card is ineligible for Google Pay
Possible enum values:
            - `missing_agreement`
              Google Pay is not enabled for your account.

            - `missing_cardholder_contact`
              Cardholder phone number or email required.

            - `unsupported_region`
              Google Pay is not supported in the cardholder’s country.

        - `flow_details.issuing_authorization.card.wallets.primary_account_identifier` (string, nullable)
          Unique identifier for a card used with digital wallets

    - `flow_details.issuing_authorization.cardholder` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      The cardholder to whom this authorization belongs.

    - `flow_details.issuing_authorization.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `flow_details.issuing_authorization.currency` (enum)
      The currency of the cardholder. This currency can be different from the currency presented at authorization and the `merchant_currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.issuing_authorization.fleet` (object, nullable)
      Fleet-specific information for authorizations using Fleet cards.

      - `flow_details.issuing_authorization.fleet.cardholder_prompt_data` (object, nullable)
        Answers to prompts presented to the cardholder at the point of sale. Prompted fields vary depending on the configuration of your physical fleet cards. Typical points of sale support only numeric entry.

        - `flow_details.issuing_authorization.fleet.cardholder_prompt_data.alphanumeric_id` (string, nullable)
          [Deprecated] An alphanumeric ID, though typical point of sales only support numeric entry. The card program can be configured to prompt for a vehicle ID, driver ID, or generic ID.

        - `flow_details.issuing_authorization.fleet.cardholder_prompt_data.driver_id` (string, nullable)
          Driver ID.

        - `flow_details.issuing_authorization.fleet.cardholder_prompt_data.odometer` (integer, nullable)
          Odometer reading.

        - `flow_details.issuing_authorization.fleet.cardholder_prompt_data.unspecified_id` (string, nullable)
          An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.

        - `flow_details.issuing_authorization.fleet.cardholder_prompt_data.user_id` (string, nullable)
          User ID.

        - `flow_details.issuing_authorization.fleet.cardholder_prompt_data.vehicle_number` (string, nullable)
          Vehicle number.

      - `flow_details.issuing_authorization.fleet.purchase_type` (enum, nullable)
        The type of purchase.
Possible enum values:
        - `fuel_and_non_fuel_purchase`
          Fuel and non-fuel purchase.

        - `fuel_purchase`
          Fuel-only purchase.

        - `non_fuel_purchase`
          Non-fuel purchase.

      - `flow_details.issuing_authorization.fleet.reported_breakdown` (object, nullable)
        More information about the total amount. Typically this information is received from the merchant after the authorization has been approved and the fuel dispensed. This information is not guaranteed to be accurate as some merchants may provide unreliable data.

        - `flow_details.issuing_authorization.fleet.reported_breakdown.fuel` (object, nullable)
          Breakdown of fuel portion of the purchase.

          - `flow_details.issuing_authorization.fleet.reported_breakdown.fuel.gross_amount_decimal` (decimal string, nullable)
            Gross fuel amount that should equal Fuel Quantity multiplied by Fuel Unit Cost, inclusive of taxes.

        - `flow_details.issuing_authorization.fleet.reported_breakdown.non_fuel` (object, nullable)
          Breakdown of non-fuel portion of the purchase.

          - `flow_details.issuing_authorization.fleet.reported_breakdown.non_fuel.gross_amount_decimal` (decimal string, nullable)
            Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.

        - `flow_details.issuing_authorization.fleet.reported_breakdown.tax` (object, nullable)
          Information about tax included in this transaction.

          - `flow_details.issuing_authorization.fleet.reported_breakdown.tax.local_amount_decimal` (decimal string, nullable)
            Amount of state or provincial Sales Tax included in the transaction amount. `null` if not reported by merchant or not subject to tax.

          - `flow_details.issuing_authorization.fleet.reported_breakdown.tax.national_amount_decimal` (decimal string, nullable)
            Amount of national Sales Tax or VAT included in the transaction amount. `null` if not reported by merchant or not subject to tax.

      - `flow_details.issuing_authorization.fleet.service_type` (enum, nullable)
        The type of fuel service.
Possible enum values:
        - `full_service`
          Full-service fuel station purchase.

        - `non_fuel_transaction`
          Non-fuel transaction.

        - `self_service`
          Self-service fuel station purchase.

    - `flow_details.issuing_authorization.fraud_challenges` (array of objects, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      Fraud challenges sent to the cardholder, if this authorization was declined for fraud risk reasons.

      - `flow_details.issuing_authorization.fraud_challenges.channel` (enum)
        The method by which the fraud challenge was delivered to the cardholder.
Possible enum values:
        - `sms`
          SMS sent to the cardholder’s phone number.

      - `flow_details.issuing_authorization.fraud_challenges.status` (enum)
        The status of the fraud challenge.
Possible enum values:
        - `expired`
          The cardholder did not respond to the challenge within 12 hours of it being sent, and it has expired. Any further response to the challenge will be ignored.

        - `pending`
          The challenge has been sent to the cardholder or is about to be sent.

        - `rejected`
          The cardholder responded to the challenge indicating that the authorization was fraudulent, and that similar authorizations should continue to be declined.

        - `undeliverable`
          A challenge has been requested to be sent, but the cardholder is unable to receive it.

        - `verified`
          The cardholder responded to the challenge indicating that the authorization was not fraudulent, and that similar authorizations should be approved.

      - `flow_details.issuing_authorization.fraud_challenges.undeliverable_reason` (enum, nullable)
        If the challenge is not deliverable, the reason why.
Possible enum values:
        - `no_phone_number`
          SMS fraud challenges cannot be delivered to this cardholder because they have no `phone_number`.

        - `unsupported_phone_number`
          SMS fraud challenges cannot be delivered to this cardholder because their `phone_number` is not supported

    - `flow_details.issuing_authorization.fuel` (object, nullable)
      Information about fuel that was purchased with this transaction. Typically this information is received from the merchant after the authorization has been approved and the fuel dispensed.

      - `flow_details.issuing_authorization.fuel.industry_product_code` (string, nullable)
        [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.

      - `flow_details.issuing_authorization.fuel.quantity_decimal` (decimal string, nullable)
        The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.

      - `flow_details.issuing_authorization.fuel.type` (enum, nullable)
        The type of fuel that was purchased.
Possible enum values:
        - `diesel`
          Diesel.

        - `other`
          Other.

        - `unleaded_plus`
          Unleaded plus.

        - `unleaded_regular`
          Unleaded regular.

        - `unleaded_super`
          Unleaded super.

      - `flow_details.issuing_authorization.fuel.unit` (enum, nullable)
        The units for `quantity_decimal`.
Possible enum values:
        - `charging_minute`
          Charging minute.

        - `imperial_gallon`
          Imperial gallon.

        - `kilogram`
          Kilogram.

        - `kilowatt_hour`
          Kilowatt-hour.

        - `liter`
          Liter.

        - `other`
          Other.

        - `pound`
          Pound.

        - `us_gallon`
          US gallon.

      - `flow_details.issuing_authorization.fuel.unit_cost_decimal` (decimal string, nullable)
        The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.

    - `flow_details.issuing_authorization.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `flow_details.issuing_authorization.merchant_amount` (integer)
      The total amount that was authorized or rejected. This amount is in the `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `merchant_amount` should be the same as `amount`, unless `merchant_currency` and `currency` are different.

    - `flow_details.issuing_authorization.merchant_currency` (enum)
      The local currency that was presented to the cardholder for the authorization. This currency can be different from the cardholder currency and the `currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.issuing_authorization.merchant_data` (object)
      Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.

      - `flow_details.issuing_authorization.merchant_data.category` (string)
        A categorization of the seller’s type of business. See our [merchant categories guide](https://docs.stripe.com/docs/issuing/merchant-categories.md) for a list of possible values.

      - `flow_details.issuing_authorization.merchant_data.category_code` (string)
        The merchant category code for the seller’s business

      - `flow_details.issuing_authorization.merchant_data.city` (string, nullable)
        City where the seller is located

      - `flow_details.issuing_authorization.merchant_data.country` (string, nullable)
        Country where the seller is located

      - `flow_details.issuing_authorization.merchant_data.name` (string, nullable)
        Name of the seller

      - `flow_details.issuing_authorization.merchant_data.network_id` (string)
        Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.

      - `flow_details.issuing_authorization.merchant_data.postal_code` (string, nullable)
        Postal code where the seller is located

      - `flow_details.issuing_authorization.merchant_data.state` (string, nullable)
        State where the seller is located

      - `flow_details.issuing_authorization.merchant_data.tax_id` (string, nullable)
        The seller’s tax identification number. Currently populated for French merchants only.

      - `flow_details.issuing_authorization.merchant_data.terminal_id` (string, nullable)
        An ID assigned by the seller to the location of the sale.

      - `flow_details.issuing_authorization.merchant_data.url` (string, nullable)
        URL provided by the merchant on a 3DS request

    - `flow_details.issuing_authorization.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `flow_details.issuing_authorization.network_data` (object, nullable)
      Details about the authorization, such as identifiers, set by the card network.

      - `flow_details.issuing_authorization.network_data.acquiring_institution_id` (string, nullable)
        Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be `null`.

      - `flow_details.issuing_authorization.network_data.system_trace_audit_number` (string, nullable)
        The System Trace Audit Number (STAN) is a 6-digit identifier assigned by the acquirer. Prefer `network_data.transaction_id` if present, unless you have special requirements.

      - `flow_details.issuing_authorization.network_data.transaction_id` (string, nullable)
        Unique identifier for the authorization assigned by the card network used to match subsequent messages, disputes, and transactions.

    - `flow_details.issuing_authorization.pending_request` (object, nullable)
      The pending authorization request. This field will only be non-null during an `issuing_authorization.request` webhook.

      - `flow_details.issuing_authorization.pending_request.amount` (integer)
        The additional amount Stripe will hold if the authorization is approved, in the card’s [currency](https://docs.stripe.com/docs/api.md#issuing_authorization_object-pending-request-currency) and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

      - `flow_details.issuing_authorization.pending_request.amount_details` (object, nullable)
        Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

        - `flow_details.issuing_authorization.pending_request.amount_details.atm_fee` (integer, nullable)
          The fee charged by the ATM for the cash withdrawal.

        - `flow_details.issuing_authorization.pending_request.amount_details.cashback_amount` (integer, nullable)
          The amount of cash requested by the cardholder.

      - `flow_details.issuing_authorization.pending_request.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `flow_details.issuing_authorization.pending_request.is_amount_controllable` (boolean)
        If set `true`, you may provide [amount](https://docs.stripe.com/docs/api/issuing/authorizations/approve.md#approve_issuing_authorization-amount) to control how much to hold for the authorization.

      - `flow_details.issuing_authorization.pending_request.merchant_amount` (integer)
        The amount the merchant is requesting to be authorized in the `merchant_currency`. The amount is in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

      - `flow_details.issuing_authorization.pending_request.merchant_currency` (enum)
        The local currency the merchant is requesting to authorize.

      - `flow_details.issuing_authorization.pending_request.network_risk_score` (integer, nullable)
        The card network’s estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99.

    - `flow_details.issuing_authorization.request_history` (array of objects)
      History of every time a `pending_request` authorization was approved/declined, either by you directly or by Stripe (e.g. based on your spending_controls). If the merchant changes the authorization by performing an incremental authorization, you can look at this field to see the previous requests for the authorization. This field can be helpful in determining why a given authorization was approved/declined.

      - `flow_details.issuing_authorization.request_history.amount` (integer)
        The `pending_request.amount` at the time of the request, presented in your card’s currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). Stripe held this amount from your account to fund the authorization if the request was approved.

      - `flow_details.issuing_authorization.request_history.amount_details` (object, nullable)
        Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

        - `flow_details.issuing_authorization.request_history.amount_details.atm_fee` (integer, nullable)
          The fee charged by the ATM for the cash withdrawal.

        - `flow_details.issuing_authorization.request_history.amount_details.cashback_amount` (integer, nullable)
          The amount of cash requested by the cardholder.

      - `flow_details.issuing_authorization.request_history.approved` (boolean)
        Whether this request was approved.

      - `flow_details.issuing_authorization.request_history.authorization_code` (string, nullable)
        A code created by Stripe which is shared with the merchant to validate the authorization. This field will be populated if the authorization message was approved. The code typically starts with the letter “S”, followed by a six-digit number. For example, “S498162”. Please note that the code is not guaranteed to be unique across authorizations.

      - `flow_details.issuing_authorization.request_history.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `flow_details.issuing_authorization.request_history.currency` (string)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `flow_details.issuing_authorization.request_history.merchant_amount` (integer)
        The `pending_request.merchant_amount` at the time of the request, presented in the `merchant_currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

      - `flow_details.issuing_authorization.request_history.merchant_currency` (string)
        The currency that was collected by the merchant and presented to the cardholder for the authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `flow_details.issuing_authorization.request_history.network_risk_score` (integer, nullable)
        The card network’s estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99.

      - `flow_details.issuing_authorization.request_history.reason` (enum)
        When an authorization is approved or declined by you or by Stripe, this field provides additional detail on the reason for the outcome.
Possible enum values:
        - `account_disabled`
          The authorization request was declined because your account is disabled. For more information, please contact us at support-issuing@stripe.com. Replaces the deprecated account_inactive and account_compliance_disabled enums.

        - `card_active`
          The authorization was approved according to your Issuing default settings. Authorization outcome was not driven by real-time auth webhook or spending controls as neither were configured.

        - `card_canceled`
          The authorization request was declined because the card was canceled.

        - `card_expired`
          The authorization request was declined because the card has expired. Documentation for replacing an expired card can be found [here](https://docs.stripe.com/docs/issuing/cards/replacements.md).

        - `card_inactive`
          The authorization request was declined because the card was inactive. To activate the card, refer to our documentation.

        - `cardholder_blocked`
          The authorization request was declined because the cardholder is blocked.

        - `cardholder_inactive`
          The authorization request was declined because the cardholder was inactive. You can activate the cardholder in the dashboard or via the API update endpoint.

        - `cardholder_verification_required`
          The authorization was not approved because the cardholder still required verification. More details can be found by querying the API and obtaining the requirements field of the Cardholder object.

        - `insecure_authorization_method`
          The authorization request was declined because an insecure authorization method was used. The authorization may be retried by inserting the chip into the terminal and/or entering the PIN at the point of sale.

        - `insufficient_funds`
          The authorization request was declined because your account had insufficient funds. Documentation for topping up your Issuing Balance can be found [here](https://docs.stripe.com/docs/issuing/funding/balance.md#top-up-your-issuing-balance).

        - `network_fallback`
          [Stripe Autopilot] Stripe timed out or encountered an error when responding to the card network. If you have a dedicated BIN and have configured Autopilot, the card network approved or declined the authorization based on your STIP configuration.

        - `not_allowed`
          The charge is not allowed on the Stripe network, possibly because it is an ATM withdrawal or cash advance.

        - `pin_blocked`
          The authorization request was declined because the card’s PIN is blocked. Documentation on managing PINs can be found [here](https://docs.stripe.com/docs/issuing/cards/pin-management.md).

        - `spending_controls`
          The authorization was declined because of your spending controls. Documentation for updating your spending controls can be found [here](https://docs.stripe.com/docs/issuing/controls/spending-controls.md). Replaces the deprecated authorization_controls enum.

        - `suspected_fraud`
          The authorization was suspected to be fraud based on Stripe’s risk controls.

        - `verification_failed`
          The authorization failed required verification checks. See [authorization.verification_data](https://stripe.com/docs/api/issuing/authorizations/object#issuing_authorization_object-verification_data) for more information. Replaces the deprecated authentication_failed, incorrect_cvc, and incorrect_expiry enums.

        - `webhook_approved`
          The authorization was approved via the real-time auth webhook. More details on this can be found [here](https://stripe.com/docs/issuing/controls/real-time-authorizations).

        - `webhook_declined`
          The authorization was declined via the real-time auth webhook. More details on this can be found [here](https://stripe.com/docs/issuing/controls/real-time-authorizations).

        - `webhook_error`
          [Autopilot] The response sent through the [real-time auth webhook](https://stripe.com/docs/issuing/controls/real-time-authorizations) is invalid.

        - `webhook_timeout`
          [Autopilot] If you are using the [real-time auth webhook](https://stripe.com/docs/issuing/controls/real-time-authorizations), the webhook timed out before we received your authorization decision. Stripe approved or declined the authorization based on what you’ve configured in your Issuing default or [Autopilot](https://stripe.com/docs/issuing/controls/real-time-authorizations#autopilot) settings.

      - `flow_details.issuing_authorization.request_history.reason_message` (string, nullable)
        If the `request_history.reason` is `webhook_error` because the direct webhook response is invalid (for example, parsing errors or missing parameters), we surface a more detailed error message via this field.

      - `flow_details.issuing_authorization.request_history.requested_at` (timestamp, nullable)
        Time when the card network received an authorization request from the acquirer in UTC. Referred to by networks as transmission time.

    - `flow_details.issuing_authorization.status` (enum)
      The current status of the authorization in its lifecycle.
Possible enum values:
      - `closed`
        The authorization was declined or [captured](https://docs.stripe.com/docs/issuing/purchases/transactions.md) through one or more [transactions](https://docs.stripe.com/docs/api/issuing/authorizations/object.md#issuing_authorization_object-transactions).

      - `expired`
        The authorization was expired without capture.

      - `pending`
        The authorization was created and is awaiting approval or was approved and is awaiting [capture](https://docs.stripe.com/docs/issuing/purchases/transactions.md).

      - `reversed`
        The authorization was reversed by the merchant.

    - `flow_details.issuing_authorization.token` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      [Token](https://docs.stripe.com/docs/api/issuing/tokens/object.md) object used for this authorization. If a network token was not used for this authorization, this field will be null.

    - `flow_details.issuing_authorization.transactions` (array of objects)
      List of [transactions](https://docs.stripe.com/docs/api/issuing/transactions.md) associated with this authorization.

      - `flow_details.issuing_authorization.transactions.id` (string)
        Unique identifier for the object.

      - `flow_details.issuing_authorization.transactions.object` (string)
        String representing the object’s type. Objects of the same type share the same value.

      - `flow_details.issuing_authorization.transactions.amount` (integer)
        The transaction amount, which will be reflected in your balance. This amount is in your currency and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

      - `flow_details.issuing_authorization.transactions.amount_details` (object, nullable)
        Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal).

        - `flow_details.issuing_authorization.transactions.amount_details.atm_fee` (integer, nullable)
          The fee charged by the ATM for the cash withdrawal.

        - `flow_details.issuing_authorization.transactions.amount_details.cashback_amount` (integer, nullable)
          The amount of cash requested by the cardholder.

      - `flow_details.issuing_authorization.transactions.authorization` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The `Authorization` object that led to this transaction.

      - `flow_details.issuing_authorization.transactions.balance_transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        ID of the [balance transaction](https://docs.stripe.com/docs/api/balance_transactions.md) associated with this transaction.

      - `flow_details.issuing_authorization.transactions.card` (string, expandable (can be expanded into an object with the `expand` request parameter))
        The card used to make this transaction.

      - `flow_details.issuing_authorization.transactions.cardholder` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The cardholder to whom this transaction belongs.

      - `flow_details.issuing_authorization.transactions.created` (timestamp)
        Time at which the object was created. Measured in seconds since the Unix epoch.

      - `flow_details.issuing_authorization.transactions.currency` (enum)
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

      - `flow_details.issuing_authorization.transactions.dispute` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        If you’ve disputed the transaction, the ID of the dispute.

      - `flow_details.issuing_authorization.transactions.livemode` (boolean)
        If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

      - `flow_details.issuing_authorization.transactions.merchant_amount` (integer)
        The amount that the merchant will receive, denominated in `merchant_currency` and in the [smallest currency unit](https://docs.stripe.com/docs/currencies.md#zero-decimal). It will be different from `amount` if the merchant is taking payment in a different currency.

      - `flow_details.issuing_authorization.transactions.merchant_currency` (enum)
        The currency with which the merchant is taking payment.

      - `flow_details.issuing_authorization.transactions.merchant_data` (object)
        Details about the seller (grocery store, e-commerce website, etc.) involved in this transaction.

        - `flow_details.issuing_authorization.transactions.merchant_data.category` (string)
          A categorization of the seller’s type of business. See our [merchant categories guide](https://docs.stripe.com/docs/issuing/merchant-categories.md) for a list of possible values.

        - `flow_details.issuing_authorization.transactions.merchant_data.category_code` (string)
          The merchant category code for the seller’s business

        - `flow_details.issuing_authorization.transactions.merchant_data.city` (string, nullable)
          City where the seller is located

        - `flow_details.issuing_authorization.transactions.merchant_data.country` (string, nullable)
          Country where the seller is located

        - `flow_details.issuing_authorization.transactions.merchant_data.name` (string, nullable)
          Name of the seller

        - `flow_details.issuing_authorization.transactions.merchant_data.network_id` (string)
          Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.

        - `flow_details.issuing_authorization.transactions.merchant_data.postal_code` (string, nullable)
          Postal code where the seller is located

        - `flow_details.issuing_authorization.transactions.merchant_data.state` (string, nullable)
          State where the seller is located

        - `flow_details.issuing_authorization.transactions.merchant_data.tax_id` (string, nullable)
          The seller’s tax identification number. Currently populated for French merchants only.

        - `flow_details.issuing_authorization.transactions.merchant_data.terminal_id` (string, nullable)
          An ID assigned by the seller to the location of the sale.

        - `flow_details.issuing_authorization.transactions.merchant_data.url` (string, nullable)
          URL provided by the merchant on a 3DS request

      - `flow_details.issuing_authorization.transactions.metadata` (object)
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

      - `flow_details.issuing_authorization.transactions.network_data` (object, nullable)
        Details about the transaction, such as processing dates, set by the card network.

        - `flow_details.issuing_authorization.transactions.network_data.authorization_code` (string, nullable)
          A code created by Stripe which is shared with the merchant to validate the authorization. This field will be populated if the authorization message was approved. The code typically starts with the letter “S”, followed by a six-digit number. For example, “S498162”. Please note that the code is not guaranteed to be unique across authorizations.

        - `flow_details.issuing_authorization.transactions.network_data.processing_date` (string, nullable)
          The date the transaction was processed by the card network. This can be different from the date the seller recorded the transaction depending on when the acquirer submits the transaction to the network.

        - `flow_details.issuing_authorization.transactions.network_data.transaction_id` (string, nullable)
          Unique identifier for the authorization assigned by the card network used to match subsequent messages, disputes, and transactions.

      - `flow_details.issuing_authorization.transactions.purchase_details` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        Additional purchase information that is optionally provided by the merchant.

        - `flow_details.issuing_authorization.transactions.purchase_details.fleet` (object, nullable)
          Fleet-specific information for transactions using Fleet cards.

          - `flow_details.issuing_authorization.transactions.purchase_details.fleet.cardholder_prompt_data` (object, nullable)
            Answers to prompts presented to cardholder at point of sale.

            - `flow_details.issuing_authorization.transactions.purchase_details.fleet.cardholder_prompt_data.driver_id` (string, nullable)
              Driver ID.

            - `flow_details.issuing_authorization.transactions.purchase_details.fleet.cardholder_prompt_data.odometer` (integer, nullable)
              Odometer reading.

            - `flow_details.issuing_authorization.transactions.purchase_details.fleet.cardholder_prompt_data.unspecified_id` (string, nullable)
              An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.

            - `flow_details.issuing_authorization.transactions.purchase_details.fleet.cardholder_prompt_data.user_id` (string, nullable)
              User ID.

            - `flow_details.issuing_authorization.transactions.purchase_details.fleet.cardholder_prompt_data.vehicle_number` (string, nullable)
              Vehicle number.

          - `flow_details.issuing_authorization.transactions.purchase_details.fleet.purchase_type` (string, nullable)
            The type of purchase. One of `fuel_purchase`, `non_fuel_purchase`, or `fuel_and_non_fuel_purchase`.

          - `flow_details.issuing_authorization.transactions.purchase_details.fleet.reported_breakdown` (object, nullable)
            More information about the total amount. This information is not guaranteed to be accurate as some merchants may provide unreliable data.

            - `flow_details.issuing_authorization.transactions.purchase_details.fleet.reported_breakdown.fuel` (object, nullable)
              Breakdown of fuel portion of the purchase.

              - `flow_details.issuing_authorization.transactions.purchase_details.fleet.reported_breakdown.fuel.gross_amount_decimal` (decimal string, nullable)
                Gross fuel amount that should equal Fuel Volume multipled by Fuel Unit Cost, inclusive of taxes.

            - `flow_details.issuing_authorization.transactions.purchase_details.fleet.reported_breakdown.non_fuel` (object, nullable)
              Breakdown of non-fuel portion of the purchase.

              - `flow_details.issuing_authorization.transactions.purchase_details.fleet.reported_breakdown.non_fuel.gross_amount_decimal` (decimal string, nullable)
                Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.

            - `flow_details.issuing_authorization.transactions.purchase_details.fleet.reported_breakdown.tax` (object, nullable)
              Information about tax included in this transaction.

              - `flow_details.issuing_authorization.transactions.purchase_details.fleet.reported_breakdown.tax.local_amount_decimal` (decimal string, nullable)
                Amount of state or provincial Sales Tax included in the transaction amount. Null if not reported by merchant or not subject to tax.

              - `flow_details.issuing_authorization.transactions.purchase_details.fleet.reported_breakdown.tax.national_amount_decimal` (decimal string, nullable)
                Amount of national Sales Tax or VAT included in the transaction amount. Null if not reported by merchant or not subject to tax.

          - `flow_details.issuing_authorization.transactions.purchase_details.fleet.service_type` (string, nullable)
            The type of fuel service. One of `non_fuel_transaction`, `full_service`, or `self_service`.

        - `flow_details.issuing_authorization.transactions.purchase_details.flight` (object, nullable)
          Information about the flight that was purchased with this transaction.

          - `flow_details.issuing_authorization.transactions.purchase_details.flight.departure_at` (integer, nullable)
            The time that the flight departed.

          - `flow_details.issuing_authorization.transactions.purchase_details.flight.passenger_name` (string, nullable)
            The name of the passenger.

          - `flow_details.issuing_authorization.transactions.purchase_details.flight.refundable` (boolean, nullable)
            Whether the ticket is refundable.

          - `flow_details.issuing_authorization.transactions.purchase_details.flight.segments` (array of objects, nullable)
            The legs of the trip.

            - `flow_details.issuing_authorization.transactions.purchase_details.flight.segments.arrival_airport_code` (string, nullable)
              The three-letter IATA airport code of the flight’s destination.

            - `flow_details.issuing_authorization.transactions.purchase_details.flight.segments.carrier` (string, nullable)
              The airline carrier code.

            - `flow_details.issuing_authorization.transactions.purchase_details.flight.segments.departure_airport_code` (string, nullable)
              The three-letter IATA airport code that the flight departed from.

            - `flow_details.issuing_authorization.transactions.purchase_details.flight.segments.flight_number` (string, nullable)
              The flight number.

            - `flow_details.issuing_authorization.transactions.purchase_details.flight.segments.service_class` (string, nullable)
              The flight’s service class.

            - `flow_details.issuing_authorization.transactions.purchase_details.flight.segments.stopover_allowed` (boolean, nullable)
              Whether a stopover is allowed on this flight.

          - `flow_details.issuing_authorization.transactions.purchase_details.flight.travel_agency` (string, nullable)
            The travel agency that issued the ticket.

        - `flow_details.issuing_authorization.transactions.purchase_details.fuel` (object, nullable)
          Information about fuel that was purchased with this transaction.

          - `flow_details.issuing_authorization.transactions.purchase_details.fuel.industry_product_code` (string, nullable)
            [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.

          - `flow_details.issuing_authorization.transactions.purchase_details.fuel.quantity_decimal` (decimal string, nullable)
            The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.

          - `flow_details.issuing_authorization.transactions.purchase_details.fuel.type` (string)
            The type of fuel that was purchased. One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or `other`.

          - `flow_details.issuing_authorization.transactions.purchase_details.fuel.unit` (string)
            The units for `quantity_decimal`. One of `charging_minute`, `imperial_gallon`, `kilogram`, `kilowatt_hour`, `liter`, `pound`, `us_gallon`, or `other`.

          - `flow_details.issuing_authorization.transactions.purchase_details.fuel.unit_cost_decimal` (decimal string)
            The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.

        - `flow_details.issuing_authorization.transactions.purchase_details.lodging` (object, nullable)
          Information about lodging that was purchased with this transaction.

          - `flow_details.issuing_authorization.transactions.purchase_details.lodging.check_in_at` (integer, nullable)
            The time of checking into the lodging.

          - `flow_details.issuing_authorization.transactions.purchase_details.lodging.nights` (integer, nullable)
            The number of nights stayed at the lodging.

        - `flow_details.issuing_authorization.transactions.purchase_details.receipt` (array of objects, nullable)
          The line items in the purchase.

          - `flow_details.issuing_authorization.transactions.purchase_details.receipt.description` (string, nullable)
            The description of the item. The maximum length of this field is 26 characters.

          - `flow_details.issuing_authorization.transactions.purchase_details.receipt.quantity` (float, nullable)
            The quantity of the item.

          - `flow_details.issuing_authorization.transactions.purchase_details.receipt.total` (integer, nullable)
            The total for this line item in cents.

          - `flow_details.issuing_authorization.transactions.purchase_details.receipt.unit_cost` (integer, nullable)
            The unit cost of the item in cents.

        - `flow_details.issuing_authorization.transactions.purchase_details.reference` (string, nullable)
          A merchant-specific order number.

      - `flow_details.issuing_authorization.transactions.token` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        [Token](https://docs.stripe.com/docs/api/issuing/tokens/object.md) object used for this transaction. If a network token was not used for this transaction, this field will be null.

      - `flow_details.issuing_authorization.transactions.type` (enum)
        The nature of the transaction.
Possible enum values:
        - `capture`
          Funds were captured by the acquirer. `amount` will be negative because funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirers [can force capture in some cases](https://stripe.com/docs/issuing/purchases/transactions).

        - `refund`
          An acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions. `amount` will be positive for refunds and negative for refund reversals. Refund reversals occur when a previous refund needs to be reversed, typically due to duplicate refunds. Learn more about [refund reversals](https://stripe.com/docs/issuing/purchases/transactions#refund-reversals).

      - `flow_details.issuing_authorization.transactions.wallet` (enum, nullable)
        The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`.

    - `flow_details.issuing_authorization.verification_data` (object)
      Verifications that Stripe performed on information that the cardholder provided to the merchant.

      - `flow_details.issuing_authorization.verification_data.address_line1_check` (enum)
        Whether the cardholder provided an address first line and if it matched the cardholder’s `billing.address.line1`.
Possible enum values:
        - `match`
          Verification succeeded, values matched.

        - `mismatch`
          Verification failed, values didn’t match.

        - `not_provided`
          Verification was not performed because no value was provided.

      - `flow_details.issuing_authorization.verification_data.address_postal_code_check` (enum)
        Whether the cardholder provided a postal code and if it matched the cardholder’s `billing.address.postal_code`.
Possible enum values:
        - `match`
          Verification succeeded, values matched.

        - `mismatch`
          Verification failed, values didn’t match.

        - `not_provided`
          Verification was not performed because no value was provided.

      - `flow_details.issuing_authorization.verification_data.authentication_exemption` (object, nullable)
        The exemption applied to this authorization.

        - `flow_details.issuing_authorization.verification_data.authentication_exemption.claimed_by` (enum)
          The entity that requested the exemption, either the acquiring merchant or the Issuing user.
Possible enum values:
          - `acquirer`
            Acquiring merchant.

          - `issuer`
            Issuing user.

        - `flow_details.issuing_authorization.verification_data.authentication_exemption.type` (enum)
          The specific exemption claimed for this authorization.
Possible enum values:
          - `low_value_transaction`
            Specifies an exemption for some low-value authorizations.

          - `transaction_risk_analysis`
            Specifies an exemption for low-risk authorizations, determined using real-time risk analysis.

          - `unknown`
            Specifies an unknown exemption type.

      - `flow_details.issuing_authorization.verification_data.cvc_check` (enum)
        Whether the cardholder provided a CVC and if it matched Stripe’s record.
Possible enum values:
        - `match`
          Verification succeeded, values matched.

        - `mismatch`
          Verification failed, values didn’t match.

        - `not_provided`
          Verification was not performed because no value was provided.

      - `flow_details.issuing_authorization.verification_data.expiry_check` (enum)
        Whether the cardholder provided an expiry date and if it matched Stripe’s record.
Possible enum values:
        - `match`
          Verification succeeded, values matched.

        - `mismatch`
          Verification failed, values didn’t match.

        - `not_provided`
          Verification was not performed because no value was provided.

      - `flow_details.issuing_authorization.verification_data.postal_code` (string, nullable)
        The postal code submitted as part of the authorization used for postal code verification.

      - `flow_details.issuing_authorization.verification_data.three_d_secure` (object, nullable)
        3D Secure details.

        - `flow_details.issuing_authorization.verification_data.three_d_secure.result` (enum)
          The outcome of the 3D Secure authentication request.
Possible enum values:
          - `attempt_acknowledged`
            The merchant attempted to authenticate the authorization, but the cardholder is not enrolled or was unable to reach Stripe.

          - `authenticated`
            Authentication successful.

          - `failed`
            Authentication failed.

          - `required`
            The authorization was declined because regulatory requirements mandated an authentication for this transaction but it wasn’t submitted correctly by the merchant, and they didn’t claim an applicable exemption. Check out our [3DS documentation](https://stripe.com/docs/issuing/3d-secure#prevent-fraud) if you want to learn more.

    - `flow_details.issuing_authorization.verified_by_fraud_challenge` (boolean, nullable)
      Whether the authorization bypassed fraud risk checks because the cardholder has previously completed a fraud challenge on a similar high-risk authorization from the same merchant.

    - `flow_details.issuing_authorization.wallet` (string, nullable)
      The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized.

  - `flow_details.outbound_payment` (object, nullable)
    The OutboundPayment object associated with the Transaction. Set if `type=outbound_payment`.

    - `flow_details.outbound_payment.id` (string)
      Unique identifier for the object.

    - `flow_details.outbound_payment.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `flow_details.outbound_payment.amount` (integer)
      Amount (in cents) transferred.

    - `flow_details.outbound_payment.cancelable` (boolean)
      Returns `true` if the object can be canceled, and `false` otherwise.

    - `flow_details.outbound_payment.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `flow_details.outbound_payment.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.outbound_payment.customer` (string, nullable)
      ID of the [customer](https://docs.stripe.com/docs/api/customers.md) to whom an OutboundPayment is sent.

    - `flow_details.outbound_payment.description` (string, nullable)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `flow_details.outbound_payment.destination_payment_method` (string, nullable)
      The PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using `destination_payment_method_data`.

    - `flow_details.outbound_payment.destination_payment_method_details` (object, nullable)
      Details about the PaymentMethod for an OutboundPayment.

      - `flow_details.outbound_payment.destination_payment_method_details.billing_details` (object)
        Contact details for the person or business receiving the OutboundPayment.

        - `flow_details.outbound_payment.destination_payment_method_details.billing_details.address` (object)
          Billing address.

          - `flow_details.outbound_payment.destination_payment_method_details.billing_details.address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `flow_details.outbound_payment.destination_payment_method_details.billing_details.address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `flow_details.outbound_payment.destination_payment_method_details.billing_details.address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `flow_details.outbound_payment.destination_payment_method_details.billing_details.address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `flow_details.outbound_payment.destination_payment_method_details.billing_details.address.postal_code` (string, nullable)
            ZIP or postal code.

          - `flow_details.outbound_payment.destination_payment_method_details.billing_details.address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `flow_details.outbound_payment.destination_payment_method_details.billing_details.email` (string, nullable)
          Email address.

        - `flow_details.outbound_payment.destination_payment_method_details.billing_details.name` (string, nullable)
          Full name.

      - `flow_details.outbound_payment.destination_payment_method_details.financial_account` (object, nullable)
        Details about the `financial_account`.

        - `flow_details.outbound_payment.destination_payment_method_details.financial_account.id` (string)
          Token of the FinancialAccount.

        - `flow_details.outbound_payment.destination_payment_method_details.financial_account.network` (enum)
          The rails used to send funds.

      - `flow_details.outbound_payment.destination_payment_method_details.type` (enum)
        The type of the payment method used in the OutboundPayment.
Possible enum values:
        - `financial_account`
        - `us_bank_account`

      - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account` (object, nullable)
        Details about the `us_bank_account`.

        - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
          Account holder type: individual or company.
Possible enum values:
          - `company`
            Account belongs to a company

          - `individual`
            Account belongs to an individual

        - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account.account_type` (enum, nullable)
          Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
          - `checking`
            Bank account type is checking

          - `savings`
            Bank account type is savings

        - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account.bank_name` (string, nullable)
          Name of the bank associated with the bank account.

        - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account.fingerprint` (string, nullable)
          Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

        - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account.last4` (string, nullable)
          Last four digits of the bank account number.

        - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
          ID of the mandate used to make this payment.

        - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account.network` (enum)
          The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
          - `ach`
            ACH network

          - `us_domestic_wire`
            US domestic wire network

        - `flow_details.outbound_payment.destination_payment_method_details.us_bank_account.routing_number` (string, nullable)
          Routing number of the bank account.

    - `flow_details.outbound_payment.end_user_details` (object, nullable)
      Details about the end user.

      - `flow_details.outbound_payment.end_user_details.ip_address` (string, nullable)
        IP address of the user initiating the OutboundPayment. Set if `present` is set to `true`. IP address collection is required for risk and compliance reasons. This will be used to help determine if the OutboundPayment is authorized or should be blocked.

      - `flow_details.outbound_payment.end_user_details.present` (boolean)
        `true` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`.

    - `flow_details.outbound_payment.expected_arrival_date` (timestamp)
      The date when funds are expected to arrive in the destination account.

    - `flow_details.outbound_payment.financial_account` (string)
      The FinancialAccount that funds were pulled from.

    - `flow_details.outbound_payment.hosted_regulatory_receipt_url` (string, nullable)
      A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

    - `flow_details.outbound_payment.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `flow_details.outbound_payment.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `flow_details.outbound_payment.returned_details` (object, nullable)
      Details about a returned OutboundPayment. Only set when the status is `returned`.

      - `flow_details.outbound_payment.returned_details.code` (enum)
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

      - `flow_details.outbound_payment.returned_details.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
        The Transaction associated with this object.

    - `flow_details.outbound_payment.statement_descriptor` (string)
      The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).

    - `flow_details.outbound_payment.status` (enum)
      Current status of the OutboundPayment: `processing`, `failed`, `posted`, `returned`, `canceled`. An OutboundPayment is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundPayment has been “confirmed” and funds have left the account, or to `failed` or `canceled`. If an OutboundPayment fails to arrive at its destination, its status will change to `returned`.

    - `flow_details.outbound_payment.status_transitions` (object)
      Hash containing timestamps of when the object transitioned to a particular `status`.

      - `flow_details.outbound_payment.status_transitions.canceled_at` (timestamp, nullable)
        Timestamp describing when an OutboundPayment changed status to `canceled`.

      - `flow_details.outbound_payment.status_transitions.failed_at` (timestamp, nullable)
        Timestamp describing when an OutboundPayment changed status to `failed`.

      - `flow_details.outbound_payment.status_transitions.posted_at` (timestamp, nullable)
        Timestamp describing when an OutboundPayment changed status to `posted`.

      - `flow_details.outbound_payment.status_transitions.returned_at` (timestamp, nullable)
        Timestamp describing when an OutboundPayment changed status to `returned`.

    - `flow_details.outbound_payment.tracking_details` (object, nullable)
      Details about network-specific tracking information if available.

      - `flow_details.outbound_payment.tracking_details.ach` (object, nullable)
        ACH network tracking details.

        - `flow_details.outbound_payment.tracking_details.ach.trace_id` (string)
          ACH trace ID of the OutboundPayment for payments sent over the `ach` network.

      - `flow_details.outbound_payment.tracking_details.type` (enum)
        The US bank account network used to send funds.
Possible enum values:
        - `ach`
        - `us_domestic_wire`

      - `flow_details.outbound_payment.tracking_details.us_domestic_wire` (object, nullable)
        US domestic wire network tracking details.

        - `flow_details.outbound_payment.tracking_details.us_domestic_wire.chips` (string, nullable)
          CHIPS System Sequence Number (SSN) of the OutboundPayment for payments sent over the `us_domestic_wire` network.

        - `flow_details.outbound_payment.tracking_details.us_domestic_wire.imad` (string, nullable)
          IMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.

        - `flow_details.outbound_payment.tracking_details.us_domestic_wire.omad` (string, nullable)
          OMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.

    - `flow_details.outbound_payment.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
      The Transaction associated with this object.

  - `flow_details.outbound_transfer` (object, nullable)
    The OutboundTransfer object associated with the Transaction. Set if `type=outbound_transfer`.

    - `flow_details.outbound_transfer.id` (string)
      Unique identifier for the object.

    - `flow_details.outbound_transfer.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `flow_details.outbound_transfer.amount` (integer)
      Amount (in cents) transferred.

    - `flow_details.outbound_transfer.cancelable` (boolean)
      Returns `true` if the object can be canceled, and `false` otherwise.

    - `flow_details.outbound_transfer.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `flow_details.outbound_transfer.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.outbound_transfer.description` (string, nullable)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `flow_details.outbound_transfer.destination_payment_method` (string, nullable)
      The PaymentMethod used as the payment instrument for an OutboundTransfer.

    - `flow_details.outbound_transfer.destination_payment_method_details` (object)
      Details about the PaymentMethod for an OutboundTransfer

      - `flow_details.outbound_transfer.destination_payment_method_details.billing_details` (object)
        Contact details for the person or business receiving the OutboundTransfer.

        - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.address` (object)
          Billing address.

          - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.postal_code` (string, nullable)
            ZIP or postal code.

          - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.email` (string, nullable)
          Email address.

        - `flow_details.outbound_transfer.destination_payment_method_details.billing_details.name` (string, nullable)
          Full name.

      - `flow_details.outbound_transfer.destination_payment_method_details.financial_account` (object, nullable)
        Details about the `financial_account`.

        - `flow_details.outbound_transfer.destination_payment_method_details.financial_account.id` (string)
          Token of the FinancialAccount.

        - `flow_details.outbound_transfer.destination_payment_method_details.financial_account.network` (enum)
          The rails used to send funds.

      - `flow_details.outbound_transfer.destination_payment_method_details.type` (enum)
        The type of the payment method used in the OutboundTransfer.

      - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account` (object, nullable)
        Details about the `us_bank_account`.

        - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
          Account holder type: individual or company.
Possible enum values:
          - `company`
            Account belongs to a company

          - `individual`
            Account belongs to an individual

        - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.account_type` (enum, nullable)
          Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
          - `checking`
            Bank account type is checking

          - `savings`
            Bank account type is savings

        - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.bank_name` (string, nullable)
          Name of the bank associated with the bank account.

        - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.fingerprint` (string, nullable)
          Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

        - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.last4` (string, nullable)
          Last four digits of the bank account number.

        - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
          ID of the mandate used to make this payment.

        - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.network` (enum)
          The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
          - `ach`
            ACH network

          - `us_domestic_wire`
            US domestic wire network

        - `flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.routing_number` (string, nullable)
          Routing number of the bank account.

    - `flow_details.outbound_transfer.expected_arrival_date` (timestamp)
      The date when funds are expected to arrive in the destination account.

    - `flow_details.outbound_transfer.financial_account` (string)
      The FinancialAccount that funds were pulled from.

    - `flow_details.outbound_transfer.hosted_regulatory_receipt_url` (string, nullable)
      A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

    - `flow_details.outbound_transfer.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `flow_details.outbound_transfer.metadata` (object)
      Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

    - `flow_details.outbound_transfer.returned_details` (object, nullable)
      Details about a returned OutboundTransfer. Only set when the status is `returned`.

      - `flow_details.outbound_transfer.returned_details.code` (enum)
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

      - `flow_details.outbound_transfer.returned_details.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
        The Transaction associated with this object.

    - `flow_details.outbound_transfer.statement_descriptor` (string)
      Information about the OutboundTransfer to be sent to the recipient account.

    - `flow_details.outbound_transfer.status` (enum)
      Current status of the OutboundTransfer: `processing`, `failed`, `canceled`, `posted`, `returned`. An OutboundTransfer is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundTransfer has been “confirmed” and funds have left the account, or to `failed` or `canceled`. If an OutboundTransfer fails to arrive at its destination, its status will change to `returned`.

    - `flow_details.outbound_transfer.status_transitions` (object)
      Hash containing timestamps of when the object transitioned to a particular `status`.

      - `flow_details.outbound_transfer.status_transitions.canceled_at` (timestamp, nullable)
        Timestamp describing when an OutboundTransfer changed status to `canceled`

      - `flow_details.outbound_transfer.status_transitions.failed_at` (timestamp, nullable)
        Timestamp describing when an OutboundTransfer changed status to `failed`

      - `flow_details.outbound_transfer.status_transitions.posted_at` (timestamp, nullable)
        Timestamp describing when an OutboundTransfer changed status to `posted`

      - `flow_details.outbound_transfer.status_transitions.returned_at` (timestamp, nullable)
        Timestamp describing when an OutboundTransfer changed status to `returned`

    - `flow_details.outbound_transfer.tracking_details` (object, nullable)
      Details about network-specific tracking information if available.

      - `flow_details.outbound_transfer.tracking_details.ach` (object, nullable)
        ACH network tracking details.

        - `flow_details.outbound_transfer.tracking_details.ach.trace_id` (string)
          ACH trace ID of the OutboundTransfer for transfers sent over the `ach` network.

      - `flow_details.outbound_transfer.tracking_details.type` (enum)
        The US bank account network used to send funds.
Possible enum values:
        - `ach`
        - `us_domestic_wire`

      - `flow_details.outbound_transfer.tracking_details.us_domestic_wire` (object, nullable)
        US domestic wire network tracking details.

        - `flow_details.outbound_transfer.tracking_details.us_domestic_wire.chips` (string, nullable)
          CHIPS System Sequence Number (SSN) of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

        - `flow_details.outbound_transfer.tracking_details.us_domestic_wire.imad` (string, nullable)
          IMAD of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

        - `flow_details.outbound_transfer.tracking_details.us_domestic_wire.omad` (string, nullable)
          OMAD of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

    - `flow_details.outbound_transfer.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
      The Transaction associated with this object.

  - `flow_details.received_credit` (object, nullable)
    The ReceivedCredit object associated with the Transaction. Set if `type=received_credit`.

    - `flow_details.received_credit.id` (string)
      Unique identifier for the object.

    - `flow_details.received_credit.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `flow_details.received_credit.amount` (integer)
      Amount (in cents) transferred.

    - `flow_details.received_credit.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `flow_details.received_credit.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.received_credit.description` (string)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `flow_details.received_credit.failure_code` (enum, nullable)
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

    - `flow_details.received_credit.financial_account` (string, nullable)
      The FinancialAccount that received the funds.

    - `flow_details.received_credit.hosted_regulatory_receipt_url` (string, nullable)
      A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

    - `flow_details.received_credit.initiating_payment_method_details` (object)
      Details about the PaymentMethod used to send a ReceivedCredit.

      - `flow_details.received_credit.initiating_payment_method_details.balance` (enum, nullable)
        Set when `type` is `balance`.
Possible enum values:
        - `payments`
          The Stripe payments balance.

      - `flow_details.received_credit.initiating_payment_method_details.billing_details` (object)
        The contact details of the person or business referenced by the received payment method details.

        - `flow_details.received_credit.initiating_payment_method_details.billing_details.address` (object)
          Billing address.

          - `flow_details.received_credit.initiating_payment_method_details.billing_details.address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `flow_details.received_credit.initiating_payment_method_details.billing_details.address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `flow_details.received_credit.initiating_payment_method_details.billing_details.address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `flow_details.received_credit.initiating_payment_method_details.billing_details.address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `flow_details.received_credit.initiating_payment_method_details.billing_details.address.postal_code` (string, nullable)
            ZIP or postal code.

          - `flow_details.received_credit.initiating_payment_method_details.billing_details.address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `flow_details.received_credit.initiating_payment_method_details.billing_details.email` (string, nullable)
          Email address.

        - `flow_details.received_credit.initiating_payment_method_details.billing_details.name` (string, nullable)
          Full name.

      - `flow_details.received_credit.initiating_payment_method_details.financial_account` (object, nullable)
        Set when `type` is `financial_account`. This is a [FinancialAccount](object.md#financial_accounts) ID.

        - `flow_details.received_credit.initiating_payment_method_details.financial_account.id` (string)
          The FinancialAccount ID.

        - `flow_details.received_credit.initiating_payment_method_details.financial_account.network` (enum)
          The rails the ReceivedCredit was sent over. A FinancialAccount can only send funds over `stripe`.

      - `flow_details.received_credit.initiating_payment_method_details.issuing_card` (string, nullable)
        Set when `type` is `issuing_card`. This is an [Issuing Card](object.md#issuing_cards) ID.

      - `flow_details.received_credit.initiating_payment_method_details.type` (enum)
        Polymorphic type matching the originating money movement’s source. This can be an external account, a Stripe balance, or a FinancialAccount.

      - `flow_details.received_credit.initiating_payment_method_details.us_bank_account` (object, nullable)
        Set when `type` is `us_bank_account`.

        - `flow_details.received_credit.initiating_payment_method_details.us_bank_account.bank_name` (string, nullable)
          Bank name.

        - `flow_details.received_credit.initiating_payment_method_details.us_bank_account.last4` (string, nullable)
          The last four digits of the bank account number.

        - `flow_details.received_credit.initiating_payment_method_details.us_bank_account.routing_number` (string, nullable)
          The routing number for the bank account.

    - `flow_details.received_credit.linked_flows` (object)
      Other flows linked to a ReceivedCredit.

      - `flow_details.received_credit.linked_flows.credit_reversal` (string, nullable)
        The CreditReversal created as a result of this ReceivedCredit being reversed.

      - `flow_details.received_credit.linked_flows.issuing_authorization` (string, nullable)
        Set if the ReceivedCredit was created due to an [Issuing Authorization](object.md#issuing_authorizations) object.

      - `flow_details.received_credit.linked_flows.issuing_transaction` (string, nullable)
        Set if the ReceivedCredit is also viewable as an [Issuing transaction](object.md#issuing_transactions) object.

      - `flow_details.received_credit.linked_flows.source_flow` (string, nullable)
        ID of the source flow. Set if `network` is `stripe` and the source flow is visible to the user. Examples of source flows include OutboundPayments, payouts, or CreditReversals.

      - `flow_details.received_credit.linked_flows.source_flow_details` (object, nullable, expandable (can be expanded into an object with the `expand` request parameter))
        The expandable object of the source flow.

        - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal` (object, nullable)
          Details about a [CreditReversal](object.md#credit_reversals).

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.id` (string)
            Unique identifier for the object.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.amount` (integer)
            Amount (in cents) transferred.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.currency` (enum)
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.financial_account` (string)
            The FinancialAccount to reverse funds from.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.hosted_regulatory_receipt_url` (string, nullable)
            A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.livemode` (boolean)
            If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.metadata` (object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.network` (enum)
            The rails used to reverse the funds.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.received_credit` (string)
            The ReceivedCredit being reversed.

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.status` (enum)
            Status of the CreditReversal
Possible enum values:
            - `canceled`
              The CreditReversal has been canceled before it has been sent to the network and no funds have left the account. (Currently not supported).

            - `posted`
              The CreditReversal has been sent to the network and funds have left the account (with the Transaction posting)

            - `processing`
              The CreditReversal starting state. Funds are “held” by a pending Transaction (but they are still part of the current balance).

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.status_transitions` (object)
            Hash containing timestamps of when the object transitioned to a particular `status`.

            - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.status_transitions.posted_at` (timestamp, nullable)
              Timestamp describing when the CreditReversal changed status to `posted`

          - `flow_details.received_credit.linked_flows.source_flow_details.credit_reversal.transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            The Transaction associated with this object.

        - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment` (object, nullable)
          Details about an [OutboundPayment](object.md#outbound_payments).

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.id` (string)
            Unique identifier for the object.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.amount` (integer)
            Amount (in cents) transferred.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.cancelable` (boolean)
            Returns `true` if the object can be canceled, and `false` otherwise.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.currency` (enum)
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.customer` (string, nullable)
            ID of the [customer](https://docs.stripe.com/docs/api/customers.md) to whom an OutboundPayment is sent.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.description` (string, nullable)
            An arbitrary string attached to the object. Often useful for displaying to users.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method` (string, nullable)
            The PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using `destination_payment_method_data`.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details` (object, nullable)
            Details about the PaymentMethod for an OutboundPayment.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details` (object)
              Contact details for the person or business receiving the OutboundPayment.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address` (object)
                Billing address.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.city` (string, nullable)
                  City, district, suburb, town, or village.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.country` (string, nullable)
                  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.line1` (string, nullable)
                  Address line 1, such as the street, PO Box, or company name.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.line2` (string, nullable)
                  Address line 2, such as the apartment, suite, unit, or building.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.postal_code` (string, nullable)
                  ZIP or postal code.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.address.state` (string, nullable)
                  State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.email` (string, nullable)
                Email address.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.billing_details.name` (string, nullable)
                Full name.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.financial_account` (object, nullable)
              Details about the `financial_account`.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.financial_account.id` (string)
                Token of the FinancialAccount.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.financial_account.network` (enum)
                The rails used to send funds.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.type` (enum)
              The type of the payment method used in the OutboundPayment.
Possible enum values:
              - `financial_account`
              - `us_bank_account`

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account` (object, nullable)
              Details about the `us_bank_account`.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
                Account holder type: individual or company.
Possible enum values:
                - `company`
                  Account belongs to a company

                - `individual`
                  Account belongs to an individual

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.account_type` (enum, nullable)
                Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
                - `checking`
                  Bank account type is checking

                - `savings`
                  Bank account type is savings

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.bank_name` (string, nullable)
                Name of the bank associated with the bank account.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.fingerprint` (string, nullable)
                Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.last4` (string, nullable)
                Last four digits of the bank account number.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
                ID of the mandate used to make this payment.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.network` (enum)
                The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
                - `ach`
                  ACH network

                - `us_domestic_wire`
                  US domestic wire network

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.destination_payment_method_details.us_bank_account.routing_number` (string, nullable)
                Routing number of the bank account.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.end_user_details` (object, nullable)
            Details about the end user.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.end_user_details.ip_address` (string, nullable)
              IP address of the user initiating the OutboundPayment. Set if `present` is set to `true`. IP address collection is required for risk and compliance reasons. This will be used to help determine if the OutboundPayment is authorized or should be blocked.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.end_user_details.present` (boolean)
              `true` if the OutboundPayment creation request is being made on behalf of an end user by a platform. Otherwise, `false`.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.expected_arrival_date` (timestamp)
            The date when funds are expected to arrive in the destination account.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.financial_account` (string)
            The FinancialAccount that funds were pulled from.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.hosted_regulatory_receipt_url` (string, nullable)
            A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.livemode` (boolean)
            If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.metadata` (object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.returned_details` (object, nullable)
            Details about a returned OutboundPayment. Only set when the status is `returned`.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.returned_details.code` (enum)
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

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.returned_details.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
              The Transaction associated with this object.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.statement_descriptor` (string)
            The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.status` (enum)
            Current status of the OutboundPayment: `processing`, `failed`, `posted`, `returned`, `canceled`. An OutboundPayment is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundPayment has been “confirmed” and funds have left the account, or to `failed` or `canceled`. If an OutboundPayment fails to arrive at its destination, its status will change to `returned`.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.status_transitions` (object)
            Hash containing timestamps of when the object transitioned to a particular `status`.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.status_transitions.canceled_at` (timestamp, nullable)
              Timestamp describing when an OutboundPayment changed status to `canceled`.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.status_transitions.failed_at` (timestamp, nullable)
              Timestamp describing when an OutboundPayment changed status to `failed`.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.status_transitions.posted_at` (timestamp, nullable)
              Timestamp describing when an OutboundPayment changed status to `posted`.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.status_transitions.returned_at` (timestamp, nullable)
              Timestamp describing when an OutboundPayment changed status to `returned`.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.tracking_details` (object, nullable)
            Details about network-specific tracking information if available.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.tracking_details.ach` (object, nullable)
              ACH network tracking details.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.tracking_details.ach.trace_id` (string)
                ACH trace ID of the OutboundPayment for payments sent over the `ach` network.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.tracking_details.type` (enum)
              The US bank account network used to send funds.
Possible enum values:
              - `ach`
              - `us_domestic_wire`

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.tracking_details.us_domestic_wire` (object, nullable)
              US domestic wire network tracking details.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.tracking_details.us_domestic_wire.chips` (string, nullable)
                CHIPS System Sequence Number (SSN) of the OutboundPayment for payments sent over the `us_domestic_wire` network.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.tracking_details.us_domestic_wire.imad` (string, nullable)
                IMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.tracking_details.us_domestic_wire.omad` (string, nullable)
                OMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_payment.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
            The Transaction associated with this object.

        - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer` (object, nullable)
          Details about an [OutboundTransfer](object.md#outbound_transfers).

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.id` (string)
            Unique identifier for the object.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.amount` (integer)
            Amount (in cents) transferred.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.cancelable` (boolean)
            Returns `true` if the object can be canceled, and `false` otherwise.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.currency` (enum)
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.description` (string, nullable)
            An arbitrary string attached to the object. Often useful for displaying to users.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method` (string, nullable)
            The PaymentMethod used as the payment instrument for an OutboundTransfer.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details` (object)
            Details about the PaymentMethod for an OutboundTransfer

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details` (object)
              Contact details for the person or business receiving the OutboundTransfer.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address` (object)
                Billing address.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.city` (string, nullable)
                  City, district, suburb, town, or village.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.country` (string, nullable)
                  Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.line1` (string, nullable)
                  Address line 1, such as the street, PO Box, or company name.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.line2` (string, nullable)
                  Address line 2, such as the apartment, suite, unit, or building.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.postal_code` (string, nullable)
                  ZIP or postal code.

                - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.address.state` (string, nullable)
                  State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.email` (string, nullable)
                Email address.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.billing_details.name` (string, nullable)
                Full name.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.financial_account` (object, nullable)
              Details about the `financial_account`.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.financial_account.id` (string)
                Token of the FinancialAccount.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.financial_account.network` (enum)
                The rails used to send funds.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.type` (enum)
              The type of the payment method used in the OutboundTransfer.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account` (object, nullable)
              Details about the `us_bank_account`.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
                Account holder type: individual or company.
Possible enum values:
                - `company`
                  Account belongs to a company

                - `individual`
                  Account belongs to an individual

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.account_type` (enum, nullable)
                Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
                - `checking`
                  Bank account type is checking

                - `savings`
                  Bank account type is savings

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.bank_name` (string, nullable)
                Name of the bank associated with the bank account.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.fingerprint` (string, nullable)
                Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.last4` (string, nullable)
                Last four digits of the bank account number.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
                ID of the mandate used to make this payment.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.network` (enum)
                The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.
Possible enum values:
                - `ach`
                  ACH network

                - `us_domestic_wire`
                  US domestic wire network

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.destination_payment_method_details.us_bank_account.routing_number` (string, nullable)
                Routing number of the bank account.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.expected_arrival_date` (timestamp)
            The date when funds are expected to arrive in the destination account.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.financial_account` (string)
            The FinancialAccount that funds were pulled from.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.hosted_regulatory_receipt_url` (string, nullable)
            A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.livemode` (boolean)
            If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.metadata` (object)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.returned_details` (object, nullable)
            Details about a returned OutboundTransfer. Only set when the status is `returned`.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.returned_details.code` (enum)
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

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.returned_details.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
              The Transaction associated with this object.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.statement_descriptor` (string)
            Information about the OutboundTransfer to be sent to the recipient account.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.status` (enum)
            Current status of the OutboundTransfer: `processing`, `failed`, `canceled`, `posted`, `returned`. An OutboundTransfer is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundTransfer has been “confirmed” and funds have left the account, or to `failed` or `canceled`. If an OutboundTransfer fails to arrive at its destination, its status will change to `returned`.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.status_transitions` (object)
            Hash containing timestamps of when the object transitioned to a particular `status`.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.status_transitions.canceled_at` (timestamp, nullable)
              Timestamp describing when an OutboundTransfer changed status to `canceled`

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.status_transitions.failed_at` (timestamp, nullable)
              Timestamp describing when an OutboundTransfer changed status to `failed`

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.status_transitions.posted_at` (timestamp, nullable)
              Timestamp describing when an OutboundTransfer changed status to `posted`

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.status_transitions.returned_at` (timestamp, nullable)
              Timestamp describing when an OutboundTransfer changed status to `returned`

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.tracking_details` (object, nullable)
            Details about network-specific tracking information if available.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.tracking_details.ach` (object, nullable)
              ACH network tracking details.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.tracking_details.ach.trace_id` (string)
                ACH trace ID of the OutboundTransfer for transfers sent over the `ach` network.

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.tracking_details.type` (enum)
              The US bank account network used to send funds.
Possible enum values:
              - `ach`
              - `us_domestic_wire`

            - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.tracking_details.us_domestic_wire` (object, nullable)
              US domestic wire network tracking details.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.tracking_details.us_domestic_wire.chips` (string, nullable)
                CHIPS System Sequence Number (SSN) of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.tracking_details.us_domestic_wire.imad` (string, nullable)
                IMAD of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

              - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.tracking_details.us_domestic_wire.omad` (string, nullable)
                OMAD of the OutboundTransfer for transfers sent over the `us_domestic_wire` network.

          - `flow_details.received_credit.linked_flows.source_flow_details.outbound_transfer.transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
            The Transaction associated with this object.

        - `flow_details.received_credit.linked_flows.source_flow_details.payout` (object, nullable)
          Details about a [Payout](object.md#payouts).

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.id` (string)
            Unique identifier for the object.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.object` (string)
            String representing the object’s type. Objects of the same type share the same value.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.amount` (integer)
            The amount (in cents) that transfers to your bank account or debit card.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.application_fee` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            The application fee (if any) for the payout. [See the Connect documentation](https://docs.stripe.com/docs/connect/instant-payouts.md#monetization-and-fees) for details.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.application_fee_amount` (integer, nullable)
            The amount of the application fee (if any) requested for the payout. [See the Connect documentation](https://docs.stripe.com/docs/connect/instant-payouts.md#monetization-and-fees) for details.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.arrival_date` (timestamp)
            Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.automatic` (boolean)
            Returns `true` if the payout is created by an [automated payout schedule](https://docs.stripe.com/docs/payouts.md#payout-schedule) and `false` if it’s [requested manually](https://stripe.com/docs/payouts#manual-payouts).

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.balance_transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            ID of the balance transaction that describes the impact of this payout on your account balance.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.created` (timestamp)
            Time at which the object was created. Measured in seconds since the Unix epoch.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.currency` (enum)
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.description` (string, nullable)
            An arbitrary string attached to the object. Often useful for displaying to users.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.destination` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            ID of the bank account or card the payout is sent to.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.failure_balance_transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            If the payout fails or cancels, this is the ID of the balance transaction that reverses the initial balance transaction and returns the funds from the failed payout back in your balance.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.failure_code` (string, nullable)
            Error code that provides a reason for a payout failure, if available. View our [list of failure codes](https://docs.stripe.com/docs/api.md#payout_failures).

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.failure_message` (string, nullable)
            Message that provides the reason for a payout failure, if available.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.livemode` (boolean)
            If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.metadata` (object, nullable)
            Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.method` (string)
            The method used to send this payout, which can be `standard` or `instant`. `instant` is supported for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.original_payout` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            If the payout reverses another, this is the ID of the original payout.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.payout_method` (string, nullable)
            ID of the v2 FinancialAccount the funds are sent to.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.reconciliation_status` (enum)
            If `completed`, you can use the [Balance Transactions API](https://docs.stripe.com/docs/api/balance_transactions/list.md#balance_transaction_list-payout) to list all balance transactions that are paid out in this payout.
Possible enum values:
            - `completed`
              The Balance Transactions paid out in this payout. You can query it with the [Balance Transactions API](https://docs.stripe.com/docs/api/balance_transactions/list.md#balance_transaction_list-payout).

            - `in_progress`
              You can query the Balance Transactions paid out in this payout soon.

            - `not_applicable`
              We don’t support listing Balance Transactions for this payout. We only support this for standard automatic payouts.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.reversed_by` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
            If the payout reverses, this is the ID of the payout that reverses this payout.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.source_type` (string)
            The source balance this payout came from, which can be one of the following: `card`, `fpx`, or `bank_account`.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.statement_descriptor` (string, nullable)
            Extra information about a payout that displays on the user’s bank statement.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.status` (string)
            Current status of the payout: `paid`, `pending`, `in_transit`, `canceled` or `failed`. A payout is `pending` until it’s submitted to the bank, when it becomes `in_transit`. The status changes to `paid` if the transaction succeeds, or to `failed` or `canceled` (within 5 business days). Some payouts that fail might initially show as `paid`, then change to `failed`.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.trace_id` (object, nullable)
            A value that generates from the beneficiary’s bank that allows users to track payouts with their bank. Banks might call this a “reference number” or something similar.

            - `flow_details.received_credit.linked_flows.source_flow_details.payout.trace_id.status` (string)
              Possible values are `pending`, `supported`, and `unsupported`. When `payout.status` is `pending` or `in_transit`, this will be `pending`. When the payout transitions to `paid`, `failed`, or `canceled`, this status will become `supported` or `unsupported` shortly after in most cases. In some cases, this may appear as `pending` for up to 10 days after `arrival_date` until transitioning to `supported` or `unsupported`.

            - `flow_details.received_credit.linked_flows.source_flow_details.payout.trace_id.value` (string, nullable)
              The trace ID value if `trace_id.status` is `supported`, otherwise `nil`.

          - `flow_details.received_credit.linked_flows.source_flow_details.payout.type` (enum)
            Can be `bank_account` or `card`.

        - `flow_details.received_credit.linked_flows.source_flow_details.type` (enum)
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

      - `flow_details.received_credit.linked_flows.source_flow_type` (string, nullable)
        The type of flow that originated the ReceivedCredit (for example, `outbound_payment`).

    - `flow_details.received_credit.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `flow_details.received_credit.network` (enum)
      The rails used to send the funds.
Possible enum values:
      - `ach`
      - `card`
      - `stripe`
      - `us_domestic_wire`

    - `flow_details.received_credit.reversal_details` (object, nullable)
      Details describing when a ReceivedCredit may be reversed.

      - `flow_details.received_credit.reversal_details.deadline` (timestamp, nullable)
        Time before which a ReceivedCredit can be reversed.

      - `flow_details.received_credit.reversal_details.restricted_reason` (enum, nullable)
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

    - `flow_details.received_credit.status` (enum)
      Status of the ReceivedCredit. ReceivedCredits are created either `succeeded` (approved) or `failed` (declined). If a ReceivedCredit is declined, the failure reason can be found in the `failure_code` field.
Possible enum values:
      - `failed`
        The ReceivedCredit was declined, and no Transaction was created.

      - `succeeded`
        The ReceivedCredit was approved.

    - `flow_details.received_credit.transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      The Transaction associated with this object.

  - `flow_details.received_debit` (object, nullable)
    The ReceivedDebit object associated with the Transaction. Set if `type=received_debit`.

    - `flow_details.received_debit.id` (string)
      Unique identifier for the object.

    - `flow_details.received_debit.object` (string)
      String representing the object’s type. Objects of the same type share the same value.

    - `flow_details.received_debit.amount` (integer)
      Amount (in cents) transferred.

    - `flow_details.received_debit.created` (timestamp)
      Time at which the object was created. Measured in seconds since the Unix epoch.

    - `flow_details.received_debit.currency` (enum)
      Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

    - `flow_details.received_debit.description` (string)
      An arbitrary string attached to the object. Often useful for displaying to users.

    - `flow_details.received_debit.failure_code` (enum, nullable)
      Reason for the failure. A ReceivedDebit might fail because the FinancialAccount doesn’t have sufficient funds, is closed, or is frozen.
Possible enum values:
      - `account_closed`
        Funds can’t be pulled from a closed FinancialAccount.

      - `account_frozen`
        Funds can’t be pulled from a frozen FinancialAccount.

      - `insufficient_funds`
        The FinancialAccount doesn’t have a sufficient balance.

      - `international_transaction`
        International transactions can’t pull funds from the FinancialAccount.

      - `other`
        Funds can’t be pulled from the FinancialAccount for other reasons.

    - `flow_details.received_debit.financial_account` (string, nullable)
      The FinancialAccount that funds were pulled from.

    - `flow_details.received_debit.hosted_regulatory_receipt_url` (string, nullable)
      A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

    - `flow_details.received_debit.initiating_payment_method_details` (object)
      Details about how a ReceivedDebit was created.

      - `flow_details.received_debit.initiating_payment_method_details.balance` (enum, nullable)
        Set when `type` is `balance`.
Possible enum values:
        - `payments`
          The Stripe payments balance.

      - `flow_details.received_debit.initiating_payment_method_details.billing_details` (object)
        The contact details of the person or business referenced by the received payment method details.

        - `flow_details.received_debit.initiating_payment_method_details.billing_details.address` (object)
          Billing address.

          - `flow_details.received_debit.initiating_payment_method_details.billing_details.address.city` (string, nullable)
            City, district, suburb, town, or village.

          - `flow_details.received_debit.initiating_payment_method_details.billing_details.address.country` (string, nullable)
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

          - `flow_details.received_debit.initiating_payment_method_details.billing_details.address.line1` (string, nullable)
            Address line 1, such as the street, PO Box, or company name.

          - `flow_details.received_debit.initiating_payment_method_details.billing_details.address.line2` (string, nullable)
            Address line 2, such as the apartment, suite, unit, or building.

          - `flow_details.received_debit.initiating_payment_method_details.billing_details.address.postal_code` (string, nullable)
            ZIP or postal code.

          - `flow_details.received_debit.initiating_payment_method_details.billing_details.address.state` (string, nullable)
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

        - `flow_details.received_debit.initiating_payment_method_details.billing_details.email` (string, nullable)
          Email address.

        - `flow_details.received_debit.initiating_payment_method_details.billing_details.name` (string, nullable)
          Full name.

      - `flow_details.received_debit.initiating_payment_method_details.financial_account` (object, nullable)
        Set when `type` is `financial_account`. This is a [FinancialAccount](object.md#financial_accounts) ID.

        - `flow_details.received_debit.initiating_payment_method_details.financial_account.id` (string)
          The FinancialAccount ID.

        - `flow_details.received_debit.initiating_payment_method_details.financial_account.network` (enum)
          The rails the ReceivedCredit was sent over. A FinancialAccount can only send funds over `stripe`.

      - `flow_details.received_debit.initiating_payment_method_details.issuing_card` (string, nullable)
        Set when `type` is `issuing_card`. This is an [Issuing Card](object.md#issuing_cards) ID.

      - `flow_details.received_debit.initiating_payment_method_details.type` (enum)
        Polymorphic type matching the originating money movement’s source. This can be an external account, a Stripe balance, or a FinancialAccount.

      - `flow_details.received_debit.initiating_payment_method_details.us_bank_account` (object, nullable)
        Set when `type` is `us_bank_account`.

        - `flow_details.received_debit.initiating_payment_method_details.us_bank_account.bank_name` (string, nullable)
          Bank name.

        - `flow_details.received_debit.initiating_payment_method_details.us_bank_account.last4` (string, nullable)
          The last four digits of the bank account number.

        - `flow_details.received_debit.initiating_payment_method_details.us_bank_account.routing_number` (string, nullable)
          The routing number for the bank account.

    - `flow_details.received_debit.linked_flows` (object)
      Other flows linked to a ReceivedDebit.

      - `flow_details.received_debit.linked_flows.debit_reversal` (string, nullable)
        The DebitReversal created as a result of this ReceivedDebit being reversed.

      - `flow_details.received_debit.linked_flows.inbound_transfer` (string, nullable)
        Set if the ReceivedDebit is associated with an InboundTransfer’s return of funds.

      - `flow_details.received_debit.linked_flows.issuing_authorization` (string, nullable)
        Set if the ReceivedDebit was created due to an [Issuing Authorization](object.md#issuing_authorizations) object.

      - `flow_details.received_debit.linked_flows.issuing_transaction` (string, nullable)
        Set if the ReceivedDebit is also viewable as an [Issuing Dispute](object.md#issuing_disputes) object.

      - `flow_details.received_debit.linked_flows.payout` (string, nullable)
        Set if the ReceivedDebit was created due to a [Payout](object.md#payouts) object.

      - `flow_details.received_debit.linked_flows.topup` (string, nullable)
        Set if the ReceivedDebit was created due to a [Topup](object.md#topups) object.

    - `flow_details.received_debit.livemode` (boolean)
      If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

    - `flow_details.received_debit.network` (enum)
      The network used for the ReceivedDebit.

    - `flow_details.received_debit.reversal_details` (object, nullable)
      Details describing when a ReceivedDebit might be reversed.

      - `flow_details.received_debit.reversal_details.deadline` (timestamp, nullable)
        Time before which a ReceivedDebit can be reversed.

      - `flow_details.received_debit.reversal_details.restricted_reason` (enum, nullable)
        Set if a ReceivedDebit can’t be reversed.
Possible enum values:
        - `already_reversed`
          A ReceivedDebit that’s already reversed has this `restricted_reason`. It may have a `deadline` populated.

        - `deadline_passed`
          A ReceivedDebit that used to be reversible until the timestamp in `deadline`, but is no longer reversible. ACH ReceivedDebits are only reversible for some time after they’re created.

        - `network_restricted`
          Network constraints prevent Stripe from allowing reversal on some ReceivedDebits.

        - `other`
          A ReceivedDebit that was reversed because of another reason.

        - `source_flow_restricted`
          A ReceivedDebit that can’t be reversed because its `source_flow` is not reversible.

    - `flow_details.received_debit.status` (enum)
      Status of the ReceivedDebit. ReceivedDebits are created with a status of either `succeeded` (approved) or `failed` (declined). The failure reason can be found under the `failure_code`.
Possible enum values:
      - `failed`
        The ReceivedDebit was declined, and no Transaction was created.

      - `succeeded`
        The ReceivedDebit was approved.

    - `flow_details.received_debit.transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      The Transaction associated with this object.

  - `flow_details.type` (enum)
    Type of the flow that created the Transaction. Set to the same value as `flow_type`.
Possible enum values:
    - `credit_reversal`
      The Transaction is associated with a CreditReversal.

    - `debit_reversal`
      The Transaction is associated with a DebitReversal.

    - `inbound_transfer`
      The Transaction is associated with an InboundTransfer.

    - `issuing_authorization`
      The Transaction is associated with an Issuing authorization.

    - `other`
      The Transaction is associated with some other money movement not listed above.

    - `outbound_payment`
      The Transaction is associated with an OutboundPayment.

    - `outbound_transfer`
      The Transaction is associated with an OutboundTransfer.

    - `received_credit`
      The Transaction is associated with a ReceivedCredit.

    - `received_debit`
      The Transaction is associated with a ReceivedDebit.

- `flow_type` (enum)
  Type of the flow associated with the TransactionEntry.
Possible enum values:
  - `credit_reversal`
    The Transaction is associated with a CreditReversal.

  - `debit_reversal`
    The Transaction is associated with a DebitReversal.

  - `inbound_transfer`
    The Transaction is associated with an InboundTransfer.

  - `issuing_authorization`
    The Transaction is associated with an Issuing authorization.

  - `other`
    The Transaction is associated with some other money movement not listed above.

  - `outbound_payment`
    The Transaction is associated with an OutboundPayment.

  - `outbound_transfer`
    The Transaction is associated with an OutboundTransfer.

  - `received_credit`
    The Transaction is associated with a ReceivedCredit.

  - `received_debit`
    The Transaction is associated with a ReceivedDebit.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `transaction` (string, expandable (can be expanded into an object with the `expand` request parameter))
  The Transaction associated with this object.

- `type` (enum)
  The specific money movement that generated the TransactionEntry.
Possible enum values:
  - `credit_reversal`
    The TransactionEntry was generated by a CreditReversal.

  - `credit_reversal_posting`
    The TransactionEntry was generated by a posted CreditReversal.

  - `debit_reversal`
    The TransactionEntry was generated by a DebitReversal.

  - `inbound_transfer`
    The TransactionEntry was generated by an InboundTransfer.

  - `inbound_transfer_return`
    The TransactionEntry was generated by an InboundTransferReturn.

  - `issuing_authorization_hold`
    The TransactionEntry was generated by an Issuing authorization hold.

  - `issuing_authorization_release`
    The TransactionEntry was generated by an Issuing authorization release.

  - `other`
    The TransactionEntry was generated by some other money movement.

  - `outbound_payment`
    The TransactionEntry was generated by an OutboundPayment.

  - `outbound_payment_cancellation`
    The TransactionEntry was generated by a cancelled OutboundPayment.

  - `outbound_payment_failure`
    The TransactionEntry was generated by a failed OutboundPayment.

  - `outbound_payment_posting`
    The TransactionEntry was generated by a posted OutboundPayment.

  - `outbound_payment_return`
    The TransactionEntry was generated by a returned OutboundPayment.

  - `outbound_transfer`
    The TransactionEntry was generated by an OutboundTransfer.

  - `outbound_transfer_cancellation`
    The TransactionEntry was generated by a canceled OutboundTransfer.

  - `outbound_transfer_failure`
    The TransactionEntry was generated by a failed OutboundTransfer.

  - `outbound_transfer_posting`
    The TransactionEntry was generated by a posted OutboundTransfer.

  - `outbound_transfer_return`
    The TransactionEntry was generated by a returned OutboundTransfer.

  - `received_credit`
    The TransactionEntry was generated by a ReceivedCredit.

  - `received_debit`
    The TransactionEntry was generated by a ReceivedDebit.

### The TransactionEntry object

```json
{
  "id": "trxne_1MtkgV2eZvKYlo2CmofEnIwJ",
  "object": "treasury.transaction_entry",
  "balance_impact": {
    "cash": 0,
    "inbound_pending": 0,
    "outbound_pending": -1000
  },
  "created": 1680756271,
  "currency": "usd",
  "effective_at": 1680756271,
  "financial_account": "fa_1MtkgV2eZvKYlo2CdxyvnHeQ",
  "flow": "obt_1MtkgV2eZvKYlo2CCxhXVFLB",
  "flow_type": "outbound_transfer",
  "livemode": false,
  "transaction": "trxn_1MtkgV2eZvKYlo2CRYxD7KLh",
  "type": "outbound_transfer"
}
```
