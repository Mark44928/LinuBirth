# LinuBirth

The pretty useless countdown to Linus Torvalds' birthday (December 28).

Cool human-looking visuals, a portrait of Linus, and a confetti party when the big day arrives.

## Running locally

```
make start        # python3 -m http.server on :8080
make check        # sanity check
```

Then open `http://localhost:8080`.

## GitHub Pages

1. Create this repo on GitHub (empty, no README), push this branch.
2. Settings → Pages → Build and deployment → Branch: `main`, folder: `/ (root)`.
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
