# Setup

This repo *is* the special `<username>/<username>` GitHub profile repo. GitHub
renders `README.md` on your profile page automatically once this repo exists
under your account with that exact name.

## 1. Create the special repo

If you haven't already:

1. On GitHub, create a new repository named **exactly** your username
   (e.g. if your username is `ayan-humayoun56`, the repo must be named
   `ayan-humayoun56`).
2. Make it **public**.
3. Push the contents of this folder to it as the `main` branch.

```bash
git init
git remote add origin https://github.com/ayan-humayoun56/ayan-humayoun56.git
git add .
git commit -m "init: research profile"
git branch -M main
git push -u origin main
```

## 2. Find-and-replace the placeholders

Every dynamic badge/stat URL in `README.md` uses the literal placeholder
`ayan-humayoun56`. Replace it everywhere with your actual GitHub
username:

```bash
# macOS/BSD sed
sed -i '' 's/ayan-humayoun56/ayan-humayoun56/g' README.md

# GNU sed (Linux)
sed -i 's/ayan-humayoun56/ayan-humayoun56/g' README.md
```

Also replace `ayanhumayoun1@gmail.com` and `https://www.linkedin.com/in/ayan-humayun-02940b3a3/` in the **Connect**
section.

## 3. Enable the GitHub Actions workflows

Two workflows live in `.github/workflows/`:

- **`ascii-portrait.yml`** — downloads your GitHub avatar, converts it to
  ASCII art with `jp2a`, and re-renders `assets/svg/ascii-portrait.svg`.
  Runs weekly and on manual dispatch. To run it immediately: go to
  **Actions → Generate ASCII Portrait → Run workflow**.

- **`snake.yml`** — generates the animated contribution snake using
  [`Platane/snk`](https://github.com/Platane/snk) and publishes it to an
  `output` branch, which `README.md` references directly via
  `raw.githubusercontent.com`. Runs daily and on manual dispatch.

Both need **Settings → Actions → General → Workflow permissions** set to
**"Read and write permissions"** so they can commit/push their output.

If you'd rather use your own photo instead of your GitHub avatar for the
ASCII portrait, drop it at `assets/portrait/profile.png` before running the
workflow — see `assets/portrait/README.md`.

## 4. Regenerating the hand-designed SVG cards

The research-interest cards, tech-stack grid, skills dashboard, and roadmap
are generated (not hand-edited) from `scripts/render_svgs.py`. To change
their content — add a project, bump a skill bar, tick off a roadmap item —
edit the data at the top of that script and re-run:

```bash
python3 scripts/render_svgs.py
```

The ASCII wordmark at the top of the README was generated with `figlet` and
wrapped with `scripts/txt_to_svg.py`:

```bash
figlet -f slant "AYAN" > /tmp/wordmark.txt
python3 scripts/txt_to_svg.py /tmp/wordmark.txt assets/svg/ascii-wordmark.svg \
  --title "ayan@research:~$ figlet -f slant AYAN" --color blue
```

## 5. Everything else

- Update the **Featured Projects** table with real repo links as you publish
  them.
- Update **Certifications & Learning** and **Research Roadmap** as you
  complete new milestones — these are the sections worth revisiting most
  often.
- The color palette is GitHub Dark (`#0D1117` / `#161B22` / `#30363D` /
  `#F0F6FC` / `#8B949E` / `#58A6FF` / `#7EE787` / `#BC8CFF`) throughout. Keep
  new elements inside that palette to stay consistent.
