# Objectives
- populate this directory with Markdown representation of the OpenAI API documentation
- for example https://developers.openai.com/api/reference/resources/responses/methods/create -> https://developers.openai.com/api/reference/resources/responses/methods/create/index.md -> `./reference/responses/methods/create.md`
- use the `cdp` utility to inspect starting at https://developers.openai.com/api/reference/overview and understand the site
- write a custom tailored script `./sync.py` that pulls the documentation in whatever form it is available and transform it into its faithful GitHub-flavored Markdown representation