# The InboundTransfer object

## Attributes

- `id` (string)
  Unique identifier for the object.

- `object` (string)
  String representing the object’s type. Objects of the same type share the same value.

- `amount` (integer)
  Amount (in cents) transferred.

- `cancelable` (boolean)
  Returns `true` if the InboundTransfer is able to be canceled.

- `created` (timestamp)
  Time at which the object was created. Measured in seconds since the Unix epoch.

- `currency` (enum)
  Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

- `description` (string, nullable)
  An arbitrary string attached to the object. Often useful for displaying to users.

- `failure_details` (object, nullable)
  Details about this InboundTransfer’s failure. Only set when status is `failed`.

  - `failure_details.code` (enum)
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

- `financial_account` (string)
  The FinancialAccount that received the funds.

- `hosted_regulatory_receipt_url` (string, nullable)
  A [hosted transaction receipt](https://docs.stripe.com/docs/treasury/moving-money/regulatory-receipts.md) URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

- `linked_flows` (object)
  Other flows linked to a InboundTransfer.

  - `linked_flows.received_debit` (string, nullable)
    If funds for this flow were returned after the flow went to the `succeeded` state, this field contains a reference to the ReceivedDebit return.

- `livemode` (boolean)
  If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.

- `metadata` (object)
  Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata.md) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

- `origin_payment_method` (string, nullable)
  The origin payment method to be debited for an InboundTransfer.

- `origin_payment_method_details` (object, nullable)
  Details about the PaymentMethod for an InboundTransfer.

  - `origin_payment_method_details.billing_details` (object)
    Contact details for the person or business referenced by the PaymentMethod.

    - `origin_payment_method_details.billing_details.address` (object)
      Billing address.

      - `origin_payment_method_details.billing_details.address.city` (string, nullable)
        City, district, suburb, town, or village.

      - `origin_payment_method_details.billing_details.address.country` (string, nullable)
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

      - `origin_payment_method_details.billing_details.address.line1` (string, nullable)
        Address line 1, such as the street, PO Box, or company name.

      - `origin_payment_method_details.billing_details.address.line2` (string, nullable)
        Address line 2, such as the apartment, suite, unit, or building.

      - `origin_payment_method_details.billing_details.address.postal_code` (string, nullable)
        ZIP or postal code.

      - `origin_payment_method_details.billing_details.address.state` (string, nullable)
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).

    - `origin_payment_method_details.billing_details.email` (string, nullable)
      Email address.

    - `origin_payment_method_details.billing_details.name` (string, nullable)
      Full name.

  - `origin_payment_method_details.type` (enum)
    The type of the payment method used in the InboundTransfer.
Possible enum values:
    - `us_bank_account`
      US Bank Account

  - `origin_payment_method_details.us_bank_account` (object, nullable)
    Optional fields for `us_bank_account`.

    - `origin_payment_method_details.us_bank_account.account_holder_type` (enum, nullable)
      Account holder type: individual or company.
Possible enum values:
      - `company`
        Account belongs to a company

      - `individual`
        Account belongs to an individual

    - `origin_payment_method_details.us_bank_account.account_type` (enum, nullable)
      Account type: checkings or savings. Defaults to checking if omitted.
Possible enum values:
      - `checking`
        Bank account type is checking

      - `savings`
        Bank account type is savings

    - `origin_payment_method_details.us_bank_account.bank_name` (string, nullable)
      Name of the bank associated with the bank account.

    - `origin_payment_method_details.us_bank_account.fingerprint` (string, nullable)
      Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

    - `origin_payment_method_details.us_bank_account.last4` (string, nullable)
      Last four digits of the bank account number.

    - `origin_payment_method_details.us_bank_account.mandate` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
      ID of the mandate used to make this payment.

    - `origin_payment_method_details.us_bank_account.network` (enum)
      The network rails used. See the [docs](https://docs.stripe.com/docs/treasury/money-movement/timelines.md) to learn more about money movement timelines for each network type.

    - `origin_payment_method_details.us_bank_account.routing_number` (string, nullable)
      Routing number of the bank account.

- `returned` (boolean, nullable)
  Returns `true` if the funds for an InboundTransfer were returned after the InboundTransfer went to the `succeeded` state.

- `statement_descriptor` (string)
  Statement descriptor shown when funds are debited from the source. Not all payment networks support `statement_descriptor`.

- `status` (enum)
  Status of the InboundTransfer: `processing`, `succeeded`, `failed`, and `canceled`. An InboundTransfer is `processing` if it is created and pending. The status changes to `succeeded` once the funds have been “confirmed” and a `transaction` is created and posted. The status changes to `failed` if the transfer fails.

- `status_transitions` (object)
  Hash containing timestamps of when the object transitioned to a particular `status`.

  - `status_transitions.failed_at` (timestamp, nullable)
    Timestamp describing when an InboundTransfer changed status to `failed`.

  - `status_transitions.succeeded_at` (timestamp, nullable)
    Timestamp describing when an InboundTransfer changed status to `succeeded`.

- `transaction` (string, nullable, expandable (can be expanded into an object with the `expand` request parameter))
  The Transaction associated with this object.
