# Update balance settings

Updates balance settings for a given connected account. Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication.md)

## Returns

Returns the updated balance settings object for the account that was authenticated in the request.

## Parameters

- `payments` (object, optional)
  Settings that apply to the [Payments Balance](../balance.md).

  - `payments.debit_negative_balances` (boolean, optional)
    A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](https://docs.stripe.com/connect/account-balances.md).

  - `payments.payouts` (object, optional)
    Settings specific to the account’s payouts.

    - `payments.payouts.minimum_balance_by_currency` (object, optional)
      The minimum balance amount to retain per currency after automatic payouts. Only funds that exceed these amounts are paid out. Learn more about the [minimum balances for automatic payouts](https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts.md).

    - `payments.payouts.schedule` (object, optional)
      Details on when funds from charges are available, and when they are paid out to an external account. For details, see our [Setting Bank and Debit Card Payouts](https://docs.stripe.com/connect/bank-transfers.md#payout-information) documentation.

      - `payments.payouts.schedule.interval` (enum, optional)
        How frequently available funds are paid out. One of: `daily`, `manual`, `weekly`, or `monthly`. Default is `daily`.
Possible enum values:
        - `daily`
          Stripe automatically sends money to your bank account daily

        - `manual`
          You manually send funds to your bank account

        - `monthly`
          Stripe automatically sends money to your bank account monthly

        - `weekly`
          Stripe automatically sends money to your bank account weekly

      - `payments.payouts.schedule.monthly_payout_days` (array of integers, optional)
        The days of the month when available funds are paid out, specified as an array of numbers between 1–31. Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month. Required and applicable only if `interval` is `monthly`.

      - `payments.payouts.schedule.weekly_payout_days` (array of enums, optional)
        The days of the week when available funds are paid out, specified as an array, e.g., [`monday`, `tuesday`]. Required and applicable only if `interval` is `weekly`.
Possible enum values:
        - `monday`
          Select Monday as one of the weekly payout days

        - `tuesday`
          Select Tuesday as one of the weekly payout days

        - `wednesday`
          Select Wednesday as one of the weekly payout days

        - `thursday`
          Select Thursday as one of the weekly payout days

        - `friday`
          Select Friday as one of the weekly payout days

    - `payments.payouts.statement_descriptor` (string, optional)
      The text that appears on the bank account statement for payouts. If not set, this defaults to the platform’s bank descriptor as set in the Dashboard.

  - `payments.settlement_timing` (object, optional)
    Settings related to the account’s balance settlement timing.

    - `payments.settlement_timing.delay_days_override` (integer, optional)
      Change `delay_days` for this account, which determines the number of days charge funds are held before becoming available. The maximum value is 31. Passing an empty string to `delay_days_override` will return `delay_days` to the default, which is the lowest available value for the account. [Learn more about controlling delay days](https://docs.stripe.com/connect/manage-payout-schedule.md).

```curl
curl https://api.stripe.com/v1/balance_settings \
  -u "<<YOUR_SECRET_KEY>>" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "payments[payouts][schedule][interval]"=monthly \
  -d "payments[payouts][schedule][monthly_payout_days][]"=5 \
  -d "payments[payouts][schedule][monthly_payout_days][]"=20
```

### Response

```json
{
  "object": "balance_settings",
  "payments": {
    "debit_negative_balances": true,
    "payouts": {
      "minimum_balance_by_currency": {
        "usd": 1500,
        "cad": 8000
      },
      "schedule": {
        "interval": "monthly",
        "monthly_payout_days": [
          5,
          20
        ]
      },
      "statement_descriptor": null,
      "status": "enabled"
    },
    "settlement_timing": {
      "delay_days_override": 3,
      "delay_days": 3
    }
  }
}
```
