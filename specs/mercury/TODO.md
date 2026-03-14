# Completed
- [x] Populated this directory with Markdown representations of the Mercury API reference.
- [x] Confirmed the local path mapping, for example `https://docs.mercury.com/reference/getaccount` -> `https://docs.mercury.com/reference/getaccount.md` -> `./getaccount.md`.
- [x] Used `cdp` to inspect `https://docs.mercury.com/reference/getaccount` and verify that Mercury serves a public ReadMe-hosted reference app whose rendered DOM exposes the full current `/reference/*` navigation, while the version selector advertises additional public roots at `/v1-pre/reference` and `/v2/reference`.
- [x] Wrote [`./sync.py`](./sync.py), which discovers reference pages from the public sitemap and rendered reference links, downloads each `.md` export, and rewrites internal Mercury reference links to local relative paths where possible.

# Notes
- The current sync produced 62 generated Markdown files under `specs/mercury/`: 58 files for the default `/reference` tree plus 4 files under `./v2/`.
- Mercury's public sitemap currently covers the full default `/reference/*` corpus; the rendered DOM adds the root `/reference` link but that root does not expose its own `.md` export.
- The `v1-pre` selector entry is publicly visible, but its rendered reference root did not expose additional syncable Markdown pages during this run.
- Internal links such as `https://docs.mercury.com/reference/events` are rewritten to local links like `./events.md` or the appropriate relative path.
