# Create an account link

Creates an AccountLink object that includes a single-use Stripe URL that the platform can redirect their user to in order to take them through the Connect Onboarding flow.

## Returns

Returns an account link object if the call succeeded.

## Parameters

- `account` (string, required)
  The identifier of the account to create an account link for.

- `type` (enum, required)
  The type of account link the user is requesting.

  You can create Account Links of type `account_update` only for connected accounts where your platform is responsible for collecting requirements, including Custom accounts. You can’t create them for accounts that have access to a Stripe-hosted Dashboard. If you use [Connect embedded components](https://docs.stripe.com/connect/get-started-connect-embedded-components.md), you can include components that allow your connected accounts to update their own information. For an account without Stripe-hosted Dashboard access where Stripe is liable for negative balances, you must use embedded components.
Possible enum values:
  - `account_onboarding`
    Provides a form for inputting outstanding requirements. Send the user to the form in this mode to just collect the new information you need.

  - `account_update`
    Displays the fields that are already populated on the account object, and allows your user to edit previously provided information. Consider framing this as “edit my profile” or “update my verification information”.

- `collect` (enum, optional)
  The collect parameter is deprecated. Use `collection_options` instead.
Possible enum values:
  - `currently_due`
  - `eventually_due`

- `collection_options` (object, optional)
  Specifies the requirements that Stripe collects from connected accounts in the Connect Onboarding flow.

  - `collection_options.fields` (enum, optional)
    Specifies whether the platform collects only currently_due requirements (`currently_due`) or both currently_due and eventually_due requirements (`eventually_due`). If you don’t specify `collection_options`, the default value is `currently_due`.
Possible enum values:
    - `currently_due`
    - `eventually_due`

  - `collection_options.future_requirements` (enum, optional)
    Specifies whether the platform collects future_requirements in addition to requirements in Connect Onboarding. The default value is `omit`.
Possible enum values:
    - `include`
    - `omit`

- `refresh_url` (string, required)
  The URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link’s URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user.

- `return_url` (string, required)
  The URL that the user will be redirected to upon leaving or completing the linked flow.

```curl
curl https://api.stripe.com/v1/account_links \
  -u "<<YOUR_SECRET_KEY>>" \
  -d account=acct_1Mt0CORHFI4mz9Rw \
  --data-urlencode refresh_url="https://example.com/reauth" \
  --data-urlencode return_url="https://example.com/return" \
  -d type=account_onboarding
```

### Response

```json
{
  "object": "account_link",
  "created": 1680577733,
  "expires_at": 1680578033,
  "url": "https://connect.stripe.com/setup/c/acct_1Mt0CORHFI4mz9Rw/TqckGNUHg2mG"
}
```
