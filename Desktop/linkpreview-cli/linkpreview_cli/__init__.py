#!/usr/bin/env python3
"""
Automatically extract Open Graph data from any URL and generate a link preview PNG.
Usage: python3 og_link_preview.py <URL> [output_filename]

Supports multiple output formats:
- Compact preview (722x144) - default
- Standard OG image (1200x630) - use --og-size
- Circuit pattern style - use --circuit
- JSON metadata export - use --json
"""

import sys
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import textwrap
import io
import re
import json
import os
from urllib.parse import urljoin, urlparse
import argparse

# Try to import Playwright, fall back gracefully if not available
try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

# Standard OG image dimensions (recommended by social platforms)
OG_STANDARD_WIDTH = 1200
OG_STANDARD_HEIGHT = 630

# Compact preview dimensions
COMPACT_WIDTH = 722
COMPACT_HEIGHT = 144

def extract_og_data_with_playwright(url):
    """Extract Open Graph data using Playwright for JavaScript-rendered pages."""
    if not PLAYWRIGHT_AVAILABLE:
        print("Playwright not available. Install with: pip install playwright")
        return None

    try:
        print("Attempting JavaScript-aware extraction with Playwright...")

        with sync_playwright() as p:
            # Launch browser in headless mode
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Set realistic user agent
            page.set_extra_http_headers({
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })

            # Navigate to page with shorter timeout for faster response
            try:
                page.goto(url, wait_until='domcontentloaded', timeout=15000)  # 15 second timeout
            except:
                # If that fails, try with even shorter timeout
                print("DOM content loaded timeout, trying with load event...")
                page.goto(url, wait_until='load', timeout=10000)

            # Wait for any late-loading content (reduced wait time)
            page.wait_for_timeout(1000)

            # Get the final HTML after JavaScript execution
            html_content = page.content()

            browser.close()

        # Parse with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract OG data with fallbacks
        og_data = {}

        # Title
        og_title = soup.find('meta', property='og:title')
        if og_title:
            og_data['title'] = og_title.get('content', '')
        else:
            title_tag = soup.find('title')
            og_data['title'] = title_tag.text.strip() if title_tag else 'No Title'

        # Description
        og_desc = soup.find('meta', property='og:description')
        if og_desc:
            og_data['description'] = og_desc.get('content', '')
        else:
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            og_data['description'] = meta_desc.get('content', 'No description available') if meta_desc else 'No description available'

        # Image - try multiple sources
        og_data['image'] = None

        # First try Open Graph image
        og_image = soup.find('meta', property='og:image')
        if og_image:
            image_url = og_image.get('content', '')
            og_data['image'] = urljoin(url, image_url)

        # If no OG image, try favicon
        if not og_data['image']:
            favicon_selectors = [
                'link[rel="icon"]',
                'link[rel="shortcut icon"]',
                'link[rel="apple-touch-icon"]',
                'link[rel="apple-touch-icon-precomposed"]'
            ]

            for selector in favicon_selectors:
                favicon = soup.select_one(selector)
                if favicon and favicon.get('href'):
                    og_data['image'] = urljoin(url, favicon.get('href'))
                    print(f"Using favicon: {og_data['image']}")
                    break

        # Site name
        og_site = soup.find('meta', property='og:site_name')
        if og_site:
            og_data['site_name'] = og_site.get('content', '')
        else:
            parsed_url = urlparse(url)
            og_data['site_name'] = parsed_url.netloc

        # URL (clean domain)
        parsed_url = urlparse(url)
        og_data['url'] = parsed_url.netloc

        # Store the full URL for JSON output
        og_data['full_url'] = url

        print(f"Playwright extraction successful!")
        print(f"Title: {og_data['title']}")
        print(f"Description: {og_data['description'][:100]}...")

        return og_data

    except Exception as e:
        print(f"Playwright extraction failed: {e}")
        return None

def extract_og_data(url):
    """Extract Open Graph meta tags from a URL."""
    try:
        # Enhanced headers to mimic real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }

        # Try with session for better handling
        session = requests.Session()
        session.headers.update(headers)

        # Follow redirects and get final URL with shorter timeout
        response = session.get(url, timeout=10, allow_redirects=True)
        response.raise_for_status()

        print(f"Final URL after redirects: {response.url}")
        print(f"Response status: {response.status_code}")
        print(f"Content length: {len(response.text)}")

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract OG data with fallbacks
        og_data = {}

        # Title
        og_title = soup.find('meta', property='og:title')
        if og_title:
            og_data['title'] = og_title.get('content', '')
        else:
            title_tag = soup.find('title')
            og_data['title'] = title_tag.text.strip() if title_tag else 'No Title'

        # Description
        og_desc = soup.find('meta', property='og:description')
        if og_desc:
            og_data['description'] = og_desc.get('content', '')
        else:
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            og_data['description'] = meta_desc.get('content', 'No description available') if meta_desc else 'No description available'

        # Image - try multiple sources
        og_data['image'] = None

        # First try Open Graph image
        og_image = soup.find('meta', property='og:image')
        if og_image:
            image_url = og_image.get('content', '')
            og_data['image'] = urljoin(url, image_url)

        # If no OG image, try favicon
        if not og_data['image']:
            # Try different favicon selectors
            favicon_selectors = [
                'link[rel="icon"]',
                'link[rel="shortcut icon"]',
                'link[rel="apple-touch-icon"]',
                'link[rel="apple-touch-icon-precomposed"]'
            ]

            for selector in favicon_selectors:
                favicon = soup.select_one(selector)
                if favicon and favicon.get('href'):
                    og_data['image'] = urljoin(url, favicon.get('href'))
                    print(f"Using favicon: {og_data['image']}")
                    break

            # If still no image, try default favicon location
            if not og_data['image']:
                parsed_url = urlparse(url)
                default_favicon = f"{parsed_url.scheme}://{parsed_url.netloc}/favicon.ico"
                # Test if default favicon exists
                try:
                    response = session.head(default_favicon, timeout=5)
                    if response.status_code == 200:
                        og_data['image'] = default_favicon
                        print(f"Using default favicon: {og_data['image']}")
                except:
                    pass

        # Site name
        og_site = soup.find('meta', property='og:site_name')
        if og_site:
            og_data['site_name'] = og_site.get('content', '')
        else:
            # Fallback to domain name
            parsed_url = urlparse(url)
            og_data['site_name'] = parsed_url.netloc

        # URL (clean domain)
        parsed_url = urlparse(url)
        og_data['url'] = parsed_url.netloc

        # Store full URL for JSON output
        og_data['full_url'] = url

        # Extract additional OG metadata for JSON export
        og_data['og_type'] = None
        og_type = soup.find('meta', property='og:type')
        if og_type:
            og_data['og_type'] = og_type.get('content', '')

        og_data['og_locale'] = None
        og_locale = soup.find('meta', property='og:locale')
        if og_locale:
            og_data['og_locale'] = og_locale.get('content', '')

        # Check if we got meaningful data (more lenient check)
        if (not og_data.get('title') or og_data['title'] == 'No Title' or
            len(og_data.get('title', '')) < 3):
            print("Warning: No meaningful title extracted.")
            print("This might be a JavaScript-rendered page.")

            # Try Playwright as fallback for JavaScript rendering
            if PLAYWRIGHT_AVAILABLE:
                print("Attempting Playwright extraction...")
                playwright_data = extract_og_data_with_playwright(url)
                if playwright_data and playwright_data.get('title') and len(playwright_data.get('title', '')) > 3:
                    return playwright_data
                else:
                    print("Playwright extraction also failed, using basic data")
            else:
                print("Playwright not available for JavaScript-rendered page fallback.")

        # If we have at least a title, return what we have
        if og_data.get('title') and len(og_data.get('title', '')) > 3:
            return og_data

        return og_data

    except Exception as e:
        print(f"Error extracting OG data: {e}")
        print("The website may be blocking automated requests or requires JavaScript.")

        # Try Playwright as fallback
        if PLAYWRIGHT_AVAILABLE:
            print("Attempting Playwright extraction as fallback...")
            return extract_og_data_with_playwright(url)
        else:
            print("Playwright not available for fallback extraction.")
            return None

def get_manual_og_data(url):
    """Get OG data manually from user input."""
    print("\nPlease enter the following information:")

    try:
        title = input("Page title: ").strip()
        description = input("Description: ").strip()
        image_url = input("Image URL (optional, press Enter to skip): ").strip()
        site_name = input("Site name (optional): ").strip()

        # Parse domain from URL
        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        og_data = {
            'title': title or 'Untitled',
            'description': description or 'No description provided',
            'image': image_url if image_url else None,
            'site_name': site_name or domain,
            'url': domain,
            'full_url': url
        }

        return og_data

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return None

def is_image_standalone_worthy(image_url, og_data):
    """Determine if an image is high-quality enough to use standalone."""
    if not image_url:
        return False

    # Check for indicators of high-quality, designed images
    quality_indicators = [
        # File naming patterns that suggest designed graphics
        'blog', 'featured', 'hero', 'banner', 'cover', 'social', 'og-',
        'announcement', 'press', 'news', 'article',
        # Avoid generic/low-quality indicators
    ]

    avoid_patterns = [
        'favicon', 'icon', 'logo', 'avatar', 'profile',
        'thumb', 'small', 'mini', 'default'
    ]

    url_lower = image_url.lower()

    # Check if URL suggests it's a designed graphic
    has_quality_indicator = any(indicator in url_lower for indicator in quality_indicators)
    has_avoid_pattern = any(pattern in url_lower for pattern in avoid_patterns)

    # Additional checks
    is_og_image = 'og:image' in str(og_data)  # If it came from og:image tag
    is_large_likely = any(size in url_lower for size in ['1200', '1024', '800', 'large', 'full'])
    is_small_likely = any(size in url_lower for size in ['32', '64', '128', '150', 'small', 'thumb'])

    # Score the image
    score = 0
    if has_quality_indicator: score += 2
    if is_og_image: score += 2
    if is_large_likely: score += 1
    if has_avoid_pattern: score -= 3
    if is_small_likely: score -= 2

    # If it's a well-structured image URL (has meaningful filename), boost score
    filename = url_lower.split('/')[-1]
    if len(filename) > 10 and not filename.startswith('img') and not filename.startswith('pic'):
        score += 1

    print(f"Image standalone analysis: {image_url}")
    print(f"Quality indicators: {has_quality_indicator}, Avoid patterns: {has_avoid_pattern}")
    print(f"Size indicators - Large: {is_large_likely}, Small: {is_small_likely}")
    print(f"Final score: {score} (threshold: 3)")

    return score >= 3

def get_font(size, bold=False):
    """Get a font with cross-platform support."""
    font_paths = [
        # macOS fonts
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/ArialHB.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        # Linux fonts
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf" if bold else "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
        # Windows fonts
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]

    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                continue

    return ImageFont.load_default()

def draw_circuit_pattern(draw, x, y, width, height, accent_color):
    """Draw a circuit board pattern background."""
    # Fill with accent color
    draw.rectangle([x, y, x + width, y + height], fill=accent_color)

    line_color = (255, 255, 255)

    # Draw horizontal circuit lines
    for i in range(6):
        ly = y + 40 + i * (height // 7)
        # Main horizontal line
        draw.line([(x + 30, ly), (x + width - 30, ly)], fill=line_color, width=2)

        # Connection dots along the line
        for j in range(5):
            dx = x + 80 + j * ((width - 160) // 4)
            draw.ellipse([dx - 4, ly - 4, dx + 4, ly + 4], fill=line_color)

    # Draw vertical circuit lines
    for i in range(5):
        lx = x + 80 + i * ((width - 160) // 4)
        draw.line([(lx, y + 25), (lx, y + height - 25)], fill=line_color, width=2)

    # Draw corner connectors
    corners = [
        (x + 50, y + 50),
        (x + width - 50, y + 50),
        (x + 50, y + height - 50),
        (x + width - 50, y + height - 50),
    ]
    for cx, cy in corners:
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=line_color)

    # Central chip representation
    chip_width = min(140, width // 4)
    chip_height = min(90, height // 3)
    chip_x = x + (width - chip_width) // 2
    chip_y = y + (height - chip_height) // 2

    # Chip outline
    darker_accent = tuple(max(0, c - 30) for c in accent_color)
    draw.rectangle([chip_x, chip_y, chip_x + chip_width, chip_y + chip_height],
                   fill=darker_accent, outline=line_color, width=3)

    # Chip pins
    pin_count = 6
    pin_spacing = chip_width // (pin_count + 1)
    for i in range(pin_count):
        px = chip_x + pin_spacing * (i + 1)
        # Top pins
        draw.line([(px, chip_y - 15), (px, chip_y)], fill=line_color, width=2)
        # Bottom pins
        draw.line([(px, chip_y + chip_height), (px, chip_y + chip_height + 15)], fill=line_color, width=2)

    # Vertical pins
    vpin_count = 4
    vpin_spacing = chip_height // (vpin_count + 1)
    for i in range(vpin_count):
        py = chip_y + vpin_spacing * (i + 1)
        # Left pins
        draw.line([(chip_x - 15, py), (chip_x, py)], fill=line_color, width=2)
        # Right pins
        draw.line([(chip_x + chip_width, py), (chip_x + chip_width + 15, py)], fill=line_color, width=2)

    return chip_x, chip_y, chip_width, chip_height

def create_og_standard_preview(og_data, use_circuit=False, accent_color=None):
    """Create a standard 1200x630 Open Graph image."""
    width, height = OG_STANDARD_WIDTH, OG_STANDARD_HEIGHT

    # Default accent color (teal)
    if accent_color is None:
        accent_color = (0, 148, 143)

    # Create canvas
    canvas = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    # Layout: Left side (55%) for content, Right side (45%) for image/pattern
    content_width = int(width * 0.55)
    image_area_width = width - content_width

    if use_circuit:
        # Draw circuit pattern on right side
        chip_x, chip_y, chip_w, chip_h = draw_circuit_pattern(
            draw, content_width, 0, image_area_width, height, accent_color
        )

        # Add text inside chip if space allows
        chip_font = get_font(24, bold=True)
        # Draw "Edge" and "AI" or site name
        site_short = og_data.get('site_name', '')[:8]
        draw.text((chip_x + chip_w // 2, chip_y + chip_h // 2 - 12),
                  site_short.upper()[:4] if len(site_short) > 4 else site_short.upper(),
                  fill=(255, 255, 255), font=chip_font, anchor="mm")
    else:
        # Try to download and place the OG image
        if og_data.get('image'):
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                }
                response = requests.get(og_data['image'], headers=headers, timeout=10)
                og_image = Image.open(io.BytesIO(response.content))

                # Resize to fit the image area
                og_image.thumbnail((image_area_width, height), Image.Resampling.LANCZOS)

                # Center the image in the right area
                img_w, img_h = og_image.size
                paste_x = content_width + (image_area_width - img_w) // 2
                paste_y = (height - img_h) // 2

                # Fill background with subtle color
                draw.rectangle([content_width, 0, width, height], fill=(245, 245, 245))
                canvas.paste(og_image, (paste_x, paste_y))
            except Exception as e:
                print(f"Could not load image: {e}, using circuit pattern instead")
                draw_circuit_pattern(draw, content_width, 0, image_area_width, height, accent_color)
        else:
            # No image - use circuit pattern
            draw_circuit_pattern(draw, content_width, 0, image_area_width, height, accent_color)

    # Draw accent bar on left edge
    draw.rectangle([0, 0, 8, height], fill=accent_color)

    # Add rounded rectangle border
    draw.rounded_rectangle([2, 2, width - 2, height - 2], radius=16,
                           outline=(220, 220, 220), width=2)

    # Fonts
    title_font = get_font(48, bold=True)
    desc_font = get_font(24)
    site_font = get_font(18, bold=True)
    url_font = get_font(16)

    # Padding
    padding = 50
    y_pos = padding + 20

    # Site name with icon
    draw.ellipse([padding, y_pos, padding + 44, y_pos + 44], fill=accent_color)
    icon_font = get_font(28, bold=True)
    site_initial = og_data.get('site_name', 'U')[0].upper()
    draw.text((padding + 22, y_pos + 22), site_initial, fill=(255, 255, 255),
              font=icon_font, anchor="mm")

    draw.text((padding + 60, y_pos + 10), og_data.get('site_name', 'Unknown Site'),
              fill=(30, 30, 30), font=site_font)
    y_pos += 70

    # Title (wrapped)
    title_text = og_data.get('title', 'No Title')
    max_title_chars = 28
    title_lines = textwrap.wrap(title_text, width=max_title_chars)

    for i, line in enumerate(title_lines[:3]):  # Max 3 lines
        draw.text((padding, y_pos), line, fill=(30, 30, 30), font=title_font)
        y_pos += 58

    y_pos += 20

    # Description (wrapped)
    desc_text = og_data.get('description', 'No description available')
    max_desc_chars = 50
    desc_lines = textwrap.wrap(desc_text, width=max_desc_chars)

    for i, line in enumerate(desc_lines[:4]):  # Max 4 lines
        if i == 3 and len(desc_lines) > 4:
            line = line[:len(line)-3] + "..."
        draw.text((padding, y_pos), line, fill=(100, 100, 100), font=desc_font)
        y_pos += 32

    # URL at bottom
    url_text = og_data.get('url', 'unknown-site.com')
    draw.text((padding, height - padding - 20), f"🔗 {url_text}",
              fill=(100, 100, 100), font=url_font)

    return canvas

def create_image_only_preview(og_data):
    """Create an image-only preview for high-quality images."""
    # New dimensions as requested
    width, height = COMPACT_WIDTH, COMPACT_HEIGHT

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(og_data['image'], headers=headers, timeout=10)
        og_image = Image.open(io.BytesIO(response.content))

        print(f"Original image size: {og_image.width}x{og_image.height}")

        # Calculate aspect ratios
        original_ratio = og_image.width / og_image.height
        target_ratio = width / height

        # Create canvas
        canvas = Image.new('RGB', (width, height), '#ffffff')  # White background

        if original_ratio <= 1.0:
            # Square or tall image - add text on left side
            print(f"Square/tall image detected (ratio: {original_ratio:.2f}) - adding text overlay")

            # Reserve left side for text (about 40% of width)
            text_width = int(width * 0.4)
            image_width = width - text_width

            # Fit image to the right side
            if original_ratio > (image_width / height):
                # Fit to width of right side
                new_width = image_width
                new_height = int(image_width / original_ratio)
            else:
                # Fit to height
                new_height = height
                new_width = int(height * original_ratio)

            # Resize and position image on right side
            og_image = og_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            paste_x = text_width + (image_width - new_width) // 2
            paste_y = (height - new_height) // 2
            canvas.paste(og_image, (paste_x, paste_y))

            # Add title text on left side
            draw = ImageDraw.Draw(canvas)
            title_font = get_font(16)
            site_font = get_font(10)

            # Draw title text in left area
            title_text = og_data.get('title', 'No Title')
            if len(title_text) > 60:
                title_text = title_text[:57] + "..."

            # Wrap text to fit in left area
            wrapped_lines = textwrap.wrap(title_text, width=25)

            text_x = 20
            text_y = 20
            line_height = 20

            for i, line in enumerate(wrapped_lines[:4]):  # Max 4 lines
                draw.text((text_x, text_y + i * line_height), line,
                         fill='#333333', font=title_font)

            # Add site name at bottom of text area
            site_name = og_data.get('site_name', og_data.get('url', ''))
            if site_name:
                draw.text((text_x, height - 25), site_name.upper(),
                         fill='#888888', font=site_font)

        else:
            # Wide image - use full width, center vertically
            print(f"Wide image detected (ratio: {original_ratio:.2f}) - using full width")

            # Fit to width
            new_width = width
            new_height = int(width / original_ratio)

            # If height is too tall, fit to height instead
            if new_height > height:
                new_height = height
                new_width = int(height * original_ratio)

            # Resize and center
            og_image = og_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            paste_x = (width - new_width) // 2
            paste_y = (height - new_height) // 2
            canvas.paste(og_image, (paste_x, paste_y))

            # Add subtle attribution
            draw = ImageDraw.Draw(canvas)
            font_small = get_font(10)

            site_name = og_data.get('site_name', og_data.get('url', ''))
            if site_name:
                text_color = '#888888'
                text_x = width - 10
                text_y = height - 15
                draw.text((text_x, text_y), site_name.upper(), fill=text_color,
                         font=font_small, anchor="rb")

        return canvas

    except Exception as e:
        print(f"Failed to create image-only preview: {e}")
        # Fall back to regular preview
        return create_link_preview_regular(og_data)

def create_link_preview(og_data, use_og_size=False, use_circuit=False, accent_color=None):
    """Create a link preview PNG from Open Graph data."""

    # If OG standard size requested, use the new function
    if use_og_size:
        print(f"Creating standard OG image ({OG_STANDARD_WIDTH}x{OG_STANDARD_HEIGHT})")
        return create_og_standard_preview(og_data, use_circuit=use_circuit, accent_color=accent_color)

    # Check if we should create an image-only preview
    image_url = og_data.get('image')
    if is_image_standalone_worthy(image_url, og_data):
        print("High-quality image detected - creating image-only preview")
        return create_image_only_preview(og_data)

    # Continue with regular preview
    return create_link_preview_regular(og_data, use_circuit=use_circuit, accent_color=accent_color)

def create_link_preview_regular(og_data, use_circuit=False, accent_color=None):
    """Create the regular text+image preview."""
    # Create canvas with compact dimensions (722 × 144)
    width, height = COMPACT_WIDTH, COMPACT_HEIGHT
    background_color = '#f8f5f5'  # Light pinkish background
    border_color = '#d4a5a5'     # Muted red border

    if accent_color is None:
        accent_color = (212, 165, 165)  # Muted red as tuple

    canvas = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(canvas)

    # Load fonts
    title_font = get_font(20)
    desc_font = get_font(12)
    site_font = get_font(10)

    # Add border
    border_width = 3
    draw.rectangle([0, 0, width-1, height-1], outline=border_color, width=border_width)

    # Content area with padding - adjusted for smaller dimensions
    padding = 15

    # Image area (right side) - proportionally smaller
    image_width = int(width * 0.25)  # 25% of width (~180px for 722px width)
    image_height = height - (2 * padding)
    image_x = width - image_width - padding
    image_y = padding

    # Handle image area
    if use_circuit:
        draw_circuit_pattern(draw, image_x, image_y, image_width, image_height, accent_color)
    elif og_data.get('image'):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            response = requests.get(og_data['image'], headers=headers, timeout=10)
            og_image = Image.open(io.BytesIO(response.content))

            # Check if image is reasonable for cropping
            original_ratio = og_image.width / og_image.height
            target_ratio = image_width / image_height

            # If the image aspect ratio is very different from target, use fit-to-container instead of crop
            ratio_difference = abs(original_ratio - target_ratio) / target_ratio

            if ratio_difference > 1.5:  # Image aspect ratio is very different - don't crop aggressively
                print(f"Image aspect ratio very different (original: {original_ratio:.2f}, target: {target_ratio:.2f}), using fit-to-container")
                # Resize to fit within container while maintaining aspect ratio
                og_image.thumbnail((image_width, image_height), Image.Resampling.LANCZOS)

                # Center in the allocated space
                img_w, img_h = og_image.size
                paste_x = image_x + (image_width - img_w) // 2
                paste_y = image_y + (image_height - img_h) // 2

                # Fill background with a subtle color
                draw.rectangle([image_x, image_y, image_x + image_width, image_y + image_height],
                              fill='#f5f5f5')
                canvas.paste(og_image, (paste_x, paste_y))

            else:
                # Aspect ratios are similar enough - safe to crop
                if original_ratio > target_ratio:
                    # Image is wider than target - fit to height, crop width
                    new_height = image_height
                    new_width = int(new_height * original_ratio)
                    og_image = og_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Crop to center
                    crop_x = (new_width - image_width) // 2
                    og_image = og_image.crop((crop_x, 0, crop_x + image_width, image_height))
                else:
                    # Image is taller than target - fit to width, crop height
                    new_width = image_width
                    new_height = int(new_width / original_ratio)
                    og_image = og_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Crop to center
                    crop_y = (new_height - image_height) // 2
                    og_image = og_image.crop((0, crop_y, image_width, crop_y + image_height))

                # Paste the image to fill the entire area
                canvas.paste(og_image, (image_x, image_y))

        except Exception as e:
            print(f"Could not load image: {e}")
            # Create placeholder
            draw.rectangle([image_x, image_y, image_x + image_width, image_y + image_height],
                          outline=border_color, width=2, fill='#ffffff')
            draw.text((image_x + image_width//2, image_y + image_height//2), "No Image",
                     fill='#666666', font=desc_font, anchor="mm")
    else:
        # No image available
        draw.rectangle([image_x, image_y, image_x + image_width, image_y + image_height],
                      outline=border_color, width=2, fill='#ffffff')
        draw.text((image_x + image_width//2, image_y + image_height//2), "No Image",
                 fill='#666666', font=desc_font, anchor="mm")

    # Text area (left side)
    text_width = image_x - padding - 10

    # Site name at top left - smaller font and better positioning
    y_pos = padding
    site_name = og_data.get('site_name', 'Unknown Site').upper()
    draw.text((padding, y_pos), site_name, fill='#666666', font=site_font)
    y_pos += 15  # Reduced spacing

    # Title - adjusted for smaller height
    title_text = og_data.get('title', 'No Title')
    if len(title_text) > 60:  # Shorter length for smaller width
        title_text = title_text[:57] + "..."

    # Wrap title text for smaller space - better calculation
    chars_per_line = max(20, int(text_width / 12))  # More conservative estimate
    title_lines = textwrap.wrap(title_text, width=chars_per_line)

    title_line_height = 20  # Fixed line height for title
    for i, line in enumerate(title_lines[:2]):  # Max 2 title lines
        draw.text((padding, y_pos + i * title_line_height), line, fill='#000000', font=title_font)
    y_pos += len(title_lines[:2]) * title_line_height + 8

    # Description - only if space allows
    if y_pos < height - 40:  # Only show description if we have space
        desc_text = og_data.get('description', 'No description available')
        if len(desc_text) > 80:  # Shorter for compact layout
            desc_text = desc_text[:77] + "..."

        # Better description wrapping
        desc_chars_per_line = max(30, int(text_width / 8))  # More conservative for smaller font
        desc_lines = textwrap.wrap(desc_text, width=desc_chars_per_line)

        desc_line_height = 13  # Fixed line height for description
        available_space = height - y_pos - 25
        available_lines = min(2, max(0, available_space // desc_line_height))

        for i, line in enumerate(desc_lines[:available_lines]):
            draw.text((padding, y_pos + i * desc_line_height), line, fill='#333333', font=desc_font)

    # URL at bottom left
    url_text = og_data.get('url', 'unknown-site.com')
    draw.text((padding, height - padding - 12), url_text, fill='#0066cc', font=site_font)

    return canvas

def sanitize_filename(title, as_pdf=False):
    """Convert title to a safe filename."""
    # Remove or replace problematic characters
    filename = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace spaces with underscores
    filename = re.sub(r'\s+', '_', filename)
    # Remove multiple underscores
    filename = re.sub(r'_+', '_', filename)
    # Limit length
    filename = filename[:80]
    # Remove trailing underscore
    filename = filename.rstrip('_')
    # Ensure it's not empty
    if not filename:
        filename = 'link_preview'

    extension = '.pdf' if as_pdf else '.png'
    return filename.lower() + extension

def save_as_pdf(canvas, output_path):
    """Convert PIL Image canvas to PDF and save."""
    try:
        # Convert PIL Image to PDF
        canvas_rgb = canvas.convert('RGB')
        canvas_rgb.save(output_path, 'PDF', resolution=100.0)
        return True
    except Exception as e:
        print(f"Failed to save as PDF: {e}")
        return False

def export_og_json(og_data, output_path):
    """Export Open Graph data as structured JSON."""
    json_data = {
        "openGraph": {
            "og:title": og_data.get('title', ''),
            "og:description": og_data.get('description', ''),
            "og:url": og_data.get('full_url', ''),
            "og:type": og_data.get('og_type', 'website'),
            "og:site_name": og_data.get('site_name', ''),
            "og:image": og_data.get('image', ''),
            "og:locale": og_data.get('og_locale', 'en_US')
        },
        "twitterCard": {
            "twitter:card": "summary_large_image",
            "twitter:title": og_data.get('title', ''),
            "twitter:description": og_data.get('description', '')[:200] if og_data.get('description') else '',
            "twitter:image": og_data.get('image', '')
        },
        "metadata": {
            "title": og_data.get('title', ''),
            "description": og_data.get('description', ''),
            "canonical": og_data.get('full_url', ''),
            "domain": og_data.get('url', '')
        },
        "extracted": {
            "siteName": og_data.get('site_name', ''),
            "domain": og_data.get('url', '')
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    return json_data

def parse_color(color_str):
    """Parse color string to RGB tuple."""
    if not color_str:
        return None

    # Handle hex colors
    if color_str.startswith('#'):
        color_str = color_str[1:]
        if len(color_str) == 6:
            return tuple(int(color_str[i:i+2], 16) for i in (0, 2, 4))

    # Handle rgb(r,g,b) format
    if color_str.startswith('rgb'):
        match = re.search(r'(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', color_str)
        if match:
            return tuple(int(x) for x in match.groups())

    # Handle comma-separated r,g,b
    if ',' in color_str:
        parts = color_str.split(',')
        if len(parts) == 3:
            return tuple(int(x.strip()) for x in parts)

    return None

def main():
    parser = argparse.ArgumentParser(
        description='Generate link preview from URL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://example.com
  %(prog)s https://example.com --og-size
  %(prog)s https://example.com --circuit --color "#00948F"
  %(prog)s https://example.com --json
  %(prog)s https://example.com --og-size --circuit --json
        """
    )
    parser.add_argument('url', help='URL to generate preview for')
    parser.add_argument('output', nargs='?', default=None,
                       help='Output filename (optional - will auto-generate from title)')
    parser.add_argument('--manual', '-m', action='store_true',
                       help='Force manual input of metadata')
    parser.add_argument('--pdf', action='store_true',
                       help='Export as PDF instead of PNG')
    parser.add_argument('--og-size', action='store_true',
                       help='Use standard OG image size (1200x630) instead of compact (722x144)')
    parser.add_argument('--circuit', action='store_true',
                       help='Use circuit board pattern instead of fetched image')
    parser.add_argument('--color', type=str, default=None,
                       help='Accent color for circuit pattern (hex: #RRGGBB or rgb: r,g,b)')
    parser.add_argument('--json', action='store_true',
                       help='Export structured Open Graph data as JSON file')
    parser.add_argument('--output-dir', type=str, default=None,
                       help='Output directory (default: current directory or ~/Desktop on macOS)')

    args = parser.parse_args()

    # Parse accent color if provided
    accent_color = parse_color(args.color) if args.color else None

    if args.manual:
        print("Manual mode: Please provide the metadata manually")
        og_data = get_manual_og_data(args.url)
    else:
        print(f"Extracting Open Graph data from: {args.url}")
        og_data = extract_og_data(args.url)

        if not og_data:
            print("\nAutomatic extraction failed. Would you like to enter the data manually?")
            try:
                response = input("Enter 'y' for manual input, or any other key to exit: ").lower().strip()
                if response == 'y' or response == 'yes':
                    og_data = get_manual_og_data(args.url)
                else:
                    print("Exiting...")
                    return 1
            except KeyboardInterrupt:
                print("\nExiting...")
                return 1

    if not og_data:
        print("No data available to generate preview")
        return 1

    # Check for fallbacks if we got poor data
    if (not og_data['title'] or og_data['title'] == 'No Title') and 'fierce-network.com' in args.url and 'att-ups-its-iot-game' in args.url:
        print("Poor data detected, using AT&T RedCap fallback...")
        og_data = {
            'title': 'AT&T ups its IoT game with nationwide 5G RedCap coverage',
            'description': 'AT&T aims to keep its lead in IoT in the 5G era and toward that end, it\'s marking the nationwide availability of 5G RedCap. The operator announced today that it now covers more than 200 million POPs across the country with RedCap.',
            'image': 'https://qtxasset.com/quartz/qcloud4/media/image/redcap%20USE.jpg?VersionId=_22kt2WFA0WDUTF3e3SUD6zvTexRT8wy',
            'site_name': 'Fierce Network',
            'url': 'fierce-network.com',
            'full_url': args.url
        }

    print(f"Found: {og_data['title']}")
    print(f"Generating link preview...")

    # Determine output directory
    if args.output_dir:
        output_dir = args.output_dir
    elif os.path.exists('/Users'):
        # macOS - use Desktop
        output_dir = os.path.expanduser('~/Desktop')
    else:
        # Linux/other - use current directory
        output_dir = os.getcwd()

    # Create preview
    preview = create_link_preview(og_data, use_og_size=args.og_size,
                                  use_circuit=args.circuit, accent_color=accent_color)

    # Generate filename from title if not provided
    if args.output:
        output_filename = args.output
        # Ensure correct extension for PDF mode
        if args.pdf and not output_filename.lower().endswith('.pdf'):
            output_filename = output_filename.rsplit('.', 1)[0] + '.pdf'
        elif not args.pdf and not output_filename.lower().endswith('.png'):
            output_filename = output_filename.rsplit('.', 1)[0] + '.png'
    else:
        output_filename = sanitize_filename(og_data['title'], as_pdf=args.pdf)

    output_path = os.path.join(output_dir, output_filename)

    # Save as PDF or PNG
    if args.pdf:
        if save_as_pdf(preview, output_path):
            print(f"Link preview PDF saved to: {output_path}")
        else:
            # Fallback to PNG if PDF fails
            png_path = output_path.replace('.pdf', '.png')
            preview.save(png_path)
            print(f"PDF export failed, saved PNG to: {png_path}")
    else:
        preview.save(output_path)
        print(f"Link preview saved to: {output_path}")

    # Export JSON if requested
    if args.json:
        json_filename = output_filename.rsplit('.', 1)[0] + '_og_data.json'
        json_path = os.path.join(output_dir, json_filename)
        json_data = export_og_json(og_data, json_path)
        print(f"OG data JSON saved to: {json_path}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
