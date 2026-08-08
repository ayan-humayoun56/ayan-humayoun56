# assets/portrait

This folder holds the source image and generated ASCII text for the profile
portrait shown in `README.md`.

- `profile.png` — the source image. If absent, the `ascii-portrait.yml`
  workflow downloads your current GitHub avatar automatically. Drop your own
  square-ish photo here (roughly 400–600px) if you'd rather use that instead.
- `ascii-portrait.txt` — the raw ASCII text produced by `jp2a`. Regenerated
  automatically; you don't need to edit it by hand.

The rendered, themed version that actually appears in the README lives at
`../svg/ascii-portrait.svg`, produced from `ascii-portrait.txt` by
`scripts/txt_to_svg.py`.

To regenerate locally instead of waiting for the scheduled workflow:

```bash
# from the repo root, with jp2a installed (apt-get install jp2a)
jp2a --width=68 --chars=" .:-=+*#%@" assets/portrait/profile.png \
  > assets/portrait/ascii-portrait.txt

python3 scripts/txt_to_svg.py assets/portrait/ascii-portrait.txt \
  assets/svg/ascii-portrait.svg --title "ayan@github:~/portrait" --color green
```
