# shadowrocket-rules

Personal Shadowrocket configuration and rule-maintenance repository.

## Purpose

This repository provides one maintainable Shadowrocket configuration that combines:

1. Manually verified personal rules with the highest priority.
2. Optional third-party supplementary rule sets.
3. A maintained public base configuration.
4. Automatic upstream synchronization through GitHub Actions.

It is intentionally service-neutral. Personal rules can be added over time for any app, website, network service, or routing requirement.

## Structure

- `mike.conf` — generated configuration imported by Shadowrocket.
- `rules/custom.list` — manually verified personal rules; highest priority.
- `rules/external.list` — optional third-party supplementary rule sets.
- `scripts/build.py` — builds the final configuration.
- `.github/workflows/sync-upstream.yml` — checks the public base daily and rebuilds `mike.conf`.

The public base is currently `Johnshall/Shadowrocket-ADBlock-Rules-Forever`, branch `release`, file `sr_cnip.conf`.

## Rule priority

`custom.list` → `external.list` → public base rules → final fallback.

This keeps personal exceptions independent from upstream updates and makes future additions easy to maintain.

## Security

This repository is public. Never store proxy credentials, UUIDs, passwords, tokens, private subscription URLs, or other secrets here.
