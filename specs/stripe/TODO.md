# Completed
- [x] Populated this directory with Stripe API Markdown docs from `https://docs.stripe.com/api`.
- [x] Confirmed the local path mapping, for example `https://docs.stripe.com/api/v2/core/events/list.md` -> `./v2/core/events/list.md`.
- [x] Used `cdp` to inspect `https://docs.stripe.com/api` and verify the app exposes its API navigation via `window.__INITIAL_STATE__.navigation.products`.
- [x] Wrote [`./sync.py`](./sync.py), which discovers API pages from the public Stripe docs HTML, syncs the corresponding `.md` endpoints, follows additional internal `/api...md` links, and rewrites local links where possible.

# Notes
- The current sync produced 943 local Markdown files under `specs/stripe/`.
- Stripe currently links to `https://docs.stripe.com/api/v2/core/accounts/createperson.md`, but that upstream Markdown URL returns HTTP 404. `./sync.py` reports and skips unavailable pages instead of failing the full sync.
