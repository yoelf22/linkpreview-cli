# linkpreview-cli

Generate link preview images from any URL. Extracts Open Graph metadata and produces PNG or PDF cards — useful for social sharing, documentation, or archiving.

## Features

- Extracts Open Graph (and Twitter Card) metadata from any URL
- Two output sizes: compact (722x144) and standard OG (1200x630)
- Circuit-board pattern style with customizable accent color
- PDF export
- JSON metadata export
- Playwright fallback for JavaScript-rendered pages
- Manual metadata entry when auto-extraction fails

## Installation

```bash
pip install -e .
```

For JavaScript-rendered pages, also install Playwright browsers:

```bash
pip install playwright
playwright install chromium
```

## Usage

```bash
# Basic — generates a compact preview PNG
linkpreview https://example.com

# Standard OG size (1200x630)
linkpreview https://example.com --og-size

# Circuit pattern with custom color
linkpreview https://example.com --circuit --color "#00948F"

# Export as PDF
linkpreview https://example.com --pdf

# Export OG metadata as JSON
linkpreview https://example.com --json

# Specify output file and directory
linkpreview https://example.com preview.png --output-dir ./out

# Combine options
linkpreview https://example.com --og-size --circuit --json --pdf
```

## Options

| Flag | Description |
|------|-------------|
| `url` | URL to generate preview for |
| `output` | Output filename (optional — auto-generated from page title) |
| `--og-size` | Use 1200x630 instead of compact 722x144 |
| `--circuit` | Circuit board pattern instead of fetched image |
| `--color` | Accent color for circuit pattern (`#RRGGBB` or `r,g,b`) |
| `--pdf` | Export as PDF instead of PNG |
| `--json` | Also export OG metadata as JSON |
| `--output-dir` | Output directory (defaults to `~/Desktop` on macOS) |
| `--manual`, `-m` | Enter metadata manually |

## Dependencies

- requests
- beautifulsoup4
- Pillow
- playwright (optional, for JS-rendered pages)
- lxml

## License

MIT
