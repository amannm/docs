# Objectives
- populate this directory with Markdown representation of the QuickBooks Online API documentation
- for example https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account -> `./accounting/all-entities/account.md`
- use the `cdp` utility to inspect starting at https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account and understand the site
- write a custom tailored script `./sync.py` that pulls the documentation in whatever form it is available and transform it into its faithful GitHub-flavored Markdown representation