# shadowrocket-rules

Mike's personal Shadowrocket configuration.

## How it works

- `mike.conf`: final configuration used by Shadowrocket.
- `rules/custom.list`: personal rules maintained separately.
- Public upstream: `Johnshall/Shadowrocket-ADBlock-Rules-Forever`, branch `release`, file `sr_cnip.conf`.
- GitHub Actions checks upstream every day and rebuilds `mike.conf`.
- Personal rules are injected immediately after `[Rule]`, so they take priority over upstream rules and survive upstream updates.

## Security

This repository is public. Never store proxy credentials, UUIDs, passwords, tokens, private subscription URLs, or other secrets here.
