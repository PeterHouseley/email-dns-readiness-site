# Email DNS Readiness Snapshot

Static marketing site for Email DNS Readiness Snapshot.

## Run locally

```bash
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173`.

## Rebuild generated assets

The infrastructure map is generated from source so the visual system stays editable:

```bash
python3 scripts/build-design-assets.py
```

This writes `assets/generated/dns-routing-map.svg`.
