# LinuBirth

[![Pages](https://github.com/Mark44928/LinuBirth/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Mark44928/LinuBirth/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made with love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)](https://mark44928.github.io/LinuBirth/)

**→ Live site: https://mark44928.github.io/LinuBirth/**

<img src="docs/screenshot.png" width="760" alt="LinuBirth screenshot">

The pretty useless countdown to Linus Torvalds' birthday (December 28). Cool human-looking visuals, a portrait of Linus, four drifting Tuxes, and a confetti party when the big day arrives.

## CLI mode (runs in Termux / any terminal)

No browser? No problem. The same countdown runs right in your terminal — Python 3 standard library only, no dependencies:

```
python3 linubirth.py            # live countdown, updates every second
python3 linubirth.py --once     # print once and exit (scripts, pipes)
python3 linubirth.py --no-color # no ANSI colors
```

```
LinuBirth  —  countdown to Dec 28

      .--.
     |o_o |
     |:_/ |
    //   \ \
   (|     | )
  /'\_   _/`\
  \___)=(___/

 32d  14h   1m  54s
```

On December 28 it flips to a "HAPPY BIRTHDAY LINUS!" banner.

## Share it

Spread the word — the site has a built-in share button (Web Share API, with a copy-link fallback). Or share directly:

- https://mark44928.github.io/LinuBirth/

Social previews (Open Graph / Twitter cards) are configured, so links unfurl nicely with a screenshot of the site.

## Running locally

```
make start        # python3 -m http.server on :8080
make check        # sanity check
```

Then open `http://localhost:8080`.

## GitHub Pages

1. Create this repo on GitHub (empty, no README), push this branch.
2. Settings → Pages → Build and deployment → Branch: `gh-pages`, folder: `/ (root)`.
3. Site publishes at `https://<user>.github.io/LinuBirth/`.

## Image

Portrait of Linus Torvalds (December 2002) from Wikimedia Commons:
https://commons.wikimedia.org/wiki/File:Linus_Torvalds.jpeg
Licensed CC BY-SA 3.0 / GFDL.

## Fonts

Bundled in `assets/fonts/` (woff2, served locally, no CDN):
- **Comic Neue** (400, 700) — the "good Comic Sans", body text
- **Patrick Hand** (400) — hand-drawn headings

Both from Google Fonts, SIL Open Font License.

---

<div align="center">
<img width="100%" src="https://api.star-history.com/svg?repos=Mark44928/LinuBirth&amp;type=Date" alt="Star history" />
</div>

---

**More projects:** [Mark44928's hub](https://mark44928.github.io/Mark44928/) — a family of dependency-free tools for Termux, Linux, and the terminal.
