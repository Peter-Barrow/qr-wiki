# QR Wiki

A wiki system with automated QR code generation for physical documentation. Perfect for lab equipment, tools, or any physical items that need quick-access documentation.

## Features

- 📝 Write documentation in Markdown
- 🔲 Automatically generates QR codes for each page
- 🚀 GitHub Actions deployment
- 🎨 Beautiful Material Design theme
- 🔍 Full-text search
- 📱 Mobile-friendly
- 🖨️ Printable QR code sheets

## Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer

### Installation

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone <your-repo-url>
cd qr-wiki

# Install dependencies
uv sync
```

### Local Development

```bash
# Generate QR codes for localhost
SITE_URL=http://localhost:8000 uv run python scripts/generate_qr_codes.py

# Start the development server
uv run mkdocs serve

# Visit http://localhost:8000 in your browser
```

### Adding Content

1. Create a new Markdown file in the `docs/` directory
2. Add it to the navigation in `mkdocs.yml`
3. Run the QR code generator (or let GitHub Actions do it)
4. Commit and push

Example:
```bash
# Create a new page
echo "# 3D Printer Guide" > docs/equipment/3d-printer.md

# Edit mkdocs.yml to add it to navigation
# ...

# Generate QR codes
SITE_URL=http://localhost:8000 uv run python scripts/generate_qr_codes.py

# Preview
uv run mkdocs serve
```

## Deployment

### GitHub Pages

1. Go to your repository settings
2. Navigate to Pages
3. Set source to "GitHub Actions"
4. Push to main branch - the site will deploy automatically

The workflow will automatically set the correct `SITE_URL` based on your repository name.

### Custom Domain

1. Update `site_url` in `mkdocs.yml`
2. Update `SITE_URL` environment variable in `.github/workflows/deploy.yml`
3. Configure your custom domain in GitHub Pages settings

## Project Structure

```
qr-wiki/
├── docs/                    # Markdown documentation files
│   ├── equipment/          # Equipment guides
│   ├── safety/             # Safety documentation
│   └── index.md            # Home page
├── qr-codes/               # Generated QR codes (git-ignored)
├── scripts/
│   └── generate_qr_codes.py  # QR code generation script
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions workflow
├── mkdocs.yml              # MkDocs configuration
├── pyproject.toml          # Python project configuration
└── README.md
```

## QR Code Generation

The QR code generator:
- Scans all Markdown files in `docs/`
- Generates a QR code pointing to each page's URL
- Saves QR codes to `qr-codes/` directory
- Creates a printable overview page at `/qr-codes`

### Manual Generation

```bash
# For production URL
SITE_URL=https://yourusername.github.io/qr-wiki uv run python scripts/generate_qr_codes.py

# For local testing
SITE_URL=http://localhost:8000 uv run python scripts/generate_qr_codes.py
```

## Printing QR Codes

1. Visit the `/qr-codes` page on your deployed site
2. Download individual QR codes or print the entire page
3. Use label paper or sticker sheets for easy application
4. Recommended: Laminate QR codes for durability

## Customization

### Theme Colors

Edit `mkdocs.yml`:
```yaml
theme:
  palette:
    primary: indigo  # Change to your preferred color
    accent: indigo
```

### Navigation

Edit `mkdocs.yml` under the `nav:` section to organize your pages.

### Logo and Favicon

Add your logo and favicon to the `docs/` directory and reference them in `mkdocs.yml`:
```yaml
theme:
  logo: assets/logo.png
  favicon: assets/favicon.png
```

## Tips

- **QR Code Size**: The QR codes are generated at 300x300px by default, perfect for 2"x2" stickers
- **Error Correction**: QR codes use high error correction, so they work even if partially obscured
- **Mobile Access**: All pages are mobile-optimized for easy viewing after scanning
- **Version Control**: Keep QR codes out of git (already in `.gitignore`) to avoid bloat

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your documentation
4. Submit a pull request

## License

[Your chosen license]

## Support

For issues or questions:
- Open an issue on GitHub
- Check the [MkDocs documentation](https://www.mkdocs.org/)
- Check the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
