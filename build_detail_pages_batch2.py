#!/usr/bin/env python3
"""Generate Tier 1 Batch 2 component detail pages using real Figma token data."""
import json
import os

with open('/Users/donnysmith/Projects/cloud/AMI-Design-System/token_data.json') as f:
    token_data = json.load(f)

components = [
    {
        'name': 'Modal',
        'slug': 'modal',
        'node_id': '40006598:91459',
        'variants': '12+',
        'category': 'Feedback',
        'token_system': 'New semantic (mixed Space/ + spacing/)',
        'token_class': 'status-good',
        'description': 'Overlay dialog for focused user interactions. Composed from Modal/Header and Modal/Footer sub-components. Uses new semantic tokens with mixed Space/ and spacing/ naming for padding. Contains tinted interactive container for backdrop overlay.',
        'anatomy': ['Backdrop overlay (Tinted interactive)', 'Container (Corner/Extra small: 4px)', 'Header (title + close button)', 'Content area (scrollable)', 'Footer (action buttons)'],
        'states': ['Open', 'Closed', 'Scrollable content'],
        'figma_variants': [
            ('Size', 'Small / Medium / Large'),
            ('Has Footer', 'Yes / No'),
            ('Has Close Button', 'Yes / No'),
            ('Type', 'Standard / Alert'),
        ],
        'sizes': ['Small (480px)', 'Medium (640px)', 'Large (800px)'],
        'real_tokens': [
            ('Text (Default)', 'Text/Neutral/Default', '#090909'),
            ('Close Icon', 'Color/Icon/Neutral/Default', '#090909'),
            ('Container (Transparent)', 'Color/Container/Neutral/Transparent interactive/Enable', '#ffffff00'),
            ('Background (Clear)', 'Color/Container/Transparent/Clear', '#ffffff00'),
            ('Backdrop Overlay', 'Color/Container/Neutral/Tinted interactive/Enable', '#0909091f'),
            ('Corner Radius', 'Corner/Extra small', '4px'),
            ('Corner (Pill)', 'Corner/Circle', '999px'),
            ('Padding (Space/6)', 'Space/6', '6px'),
            ('Padding (Space/8)', 'Space/8', '8px'),
            ('Gap (spacing/08)', 'spacing/08', '8px'),
            ('Padding (spacing/16)', 'spacing/16', '16px'),
            ('Padding (spacing/24)', 'spacing/24', '24px'),
            ('Title Font', 'font family/graphik', 'Graphik'),
            ('Title Size', 'font size/07', '20px'),
            ('Title Style', 'Headline/Extra small/Primary medium', 'Graphik Medium 20/24'),
        ],
        'legacy_note': 'Modal uses BOTH Space/ and spacing/ naming for the same type of property (padding). These should be unified to one system during migration.',
    },
    {
        'name': 'Bottom Sheet',
        'slug': 'bottom-sheet',
        'node_id': '40009097:47982',
        'variants': '8+',
        'category': 'Navigation',
        'token_system': 'Mixed (new semantic + LEGACY reference)',
        'token_class': 'status-gap',
        'description': 'Mobile-first overlay sheet that slides up from the bottom of the viewport. Mostly uses new semantic tokens but contains a legacy reference token. Uses upward elevation shadow (Cast up) — the only component with this shadow direction.',
        'anatomy': ['Container (base white)', 'Handle bar (Circle radius)', 'Header (title + close)', 'Content area (scrollable)', 'Action buttons'],
        'states': ['Collapsed', 'Half-expanded', 'Full-expanded', 'Dismissing'],
        'figma_variants': [
            ('State', 'Default / Expanded / Collapsed'),
            ('Has Header', 'Yes / No'),
            ('Content Type', 'List / Form / Custom'),
        ],
        'sizes': ['Responsive (viewport width)'],
        'real_tokens': [
            ('Container', 'Color/Container/Neutral/Base', '#ffffff'),
            ('Container (Transparent)', 'Color/Container/Neutral/Transparent interactive/Enable', '#ffffff00'),
            ('Container (Mute)', 'Color/Container/Neutral/Transparent interactive/Mute enable', '#ffffff00'),
            ('Container (Action)', 'Color/Container/Neutral/Interactive/Enable', '#090909'),
            ('Border', 'Color/Border/Neutral/Subtle 2', '#dedad7'),
            ('Icon', 'Color/Icon/Neutral/Default', '#090909'),
            ('Text', 'Text/Neutral/Default', '#090909'),
            ('Text (Inverted)', 'Text/Neutral/Inverted', '#ffffff'),
            ('Shadow', 'Elevation 2/Cast up', 'upward multi-shadow'),
            ('Title Style', 'Body/Large/Medium', 'Graphik Medium 18/26'),
            ('Body Style', 'Body/Small/Regular', 'Graphik Regular 14/20'),
            ('Corner Radius', 'Corner/Extra small', '4px'),
            ('Handle (Pill)', 'Corner/Circle', '999px'),
            ('Padding (Space/6)', 'Space/6', '6px'),
            ('Spacing', 'spacing/08', '8px'),
            ('Gap', 'spacing/12', '12px'),
            ('Padding', 'spacing/16', '16px'),
            ('Padding (Large)', 'spacing/24', '24px'),
            ('Viewport', 'viewport/common', '1440px'),
            ('LEGACY Margin', 'Components (LEGACY)/Bottom Sheet (LEGACY)/24-Margin', '24px'),
        ],
        'legacy_note': 'Contains legacy reference <code>Components (LEGACY)/Bottom Sheet (LEGACY)/24-Margin</code>. This should be migrated to <code>spacing/24</code> which already exists on this component with the same value.',
    },
    {
        'name': 'Consumer NavBar',
        'slug': 'navbar',
        'node_id': '40019054:170805',
        'variants': '24+',
        'category': 'Navigation',
        'token_system': 'New semantic (lowercase)',
        'token_class': 'status-good',
        'description': 'Primary horizontal navigation bar for the consumer-facing application. Uses new semantic tokens consistently. Contains viewport breakpoint references for responsive behavior. Links to Profile Menu and NavDrawer components.',
        'anatomy': ['Container (full-width, white base)', 'Logo area', 'Nav link group', 'Search button', 'Profile avatar button', 'Brand accent border'],
        'states': ['Default', 'Link Hover', 'Link Active', 'Mobile (hamburger)'],
        'figma_variants': [
            ('Breakpoint', 'XLarge (1440) / Large (1280) / Medium (768) / Small (375)'),
            ('State', 'Default / Menu Open'),
            ('User State', 'Logged In / Logged Out'),
        ],
        'sizes': ['XLarge (1440px)', 'Large (1280px)', 'Medium (768px)', 'Small (375px)'],
        'real_tokens': [
            ('Icon', 'Color/Icon/Neutral/Default', '#090909'),
            ('Icon (Interactive)', 'Color/Icon/Neutral/Interactive/Enable', '#090909'),
            ('Link Text', 'Text/Neutral/Interactive/Enable', '#090909'),
            ('Text', 'Text/Neutral/Default', '#090909'),
            ('Text (Inverted)', 'Text/Neutral/Inverted', '#ffffff'),
            ('Container (Transparent)', 'Color/Container/Neutral/Transparent interactive/Enable', '#ffffff00'),
            ('Button Fill', 'Color/Container/Neutral/Interactive/Enable', '#090909'),
            ('Background', 'Section bg/Neutral/Base', '#ffffff'),
            ('Brand Accent', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Nav Font', 'Body/Small/Regular', 'Graphik Regular 14/20'),
            ('Viewport Min', 'viewport/min', '1280'),
            ('Viewport Max', 'viewport/max', '2560'),
            ('Viewport Common', 'viewport/common', '1440'),
            ('Device Logic', 'device logic/show desktop', 'true'),
            ('Gap', 'spacing/04', '4px'),
            ('Spacing', 'spacing/08', '8px'),
            ('Padding', 'spacing/16', '16px'),
            ('Section Gap', 'spacing/24', '24px'),
        ],
        'legacy_note': None,
    },
    {
        'name': 'NavDrawer (Side Nav)',
        'slug': 'navdrawer',
        'node_id': '40019054:169025',
        'variants': '16+',
        'category': 'Navigation',
        'token_system': 'Mixed (new semantic + LEGACY reference)',
        'token_class': 'status-gap',
        'description': 'Collapsible side navigation panel for mobile and tablet viewports. Slides in from the left. Mostly uses new semantic tokens but contains a legacy NavBar reference token that should be cleaned up.',
        'anatomy': ['Container (white base)', 'Header (logo + close)', 'Navigation links', 'Nested folders (expandable)', 'Segments dividers', 'Footer actions'],
        'states': ['Expanded', 'Collapsed', 'Link Active', 'Folder Open', 'Folder Closed'],
        'figma_variants': [
            ('State', 'Open / Closed'),
            ('Link State', 'Default / Active / Hover'),
            ('Has Folders', 'Yes / No'),
        ],
        'sizes': ['Default (280px width)'],
        'real_tokens': [
            ('Link Text', 'Text/Neutral/Interactive/Enable', '#090909'),
            ('Text', 'Text/Neutral/Default', '#090909'),
            ('Text (Inverted)', 'Text/Neutral/Inverted', '#ffffff'),
            ('Nav Link (Brand)', 'Color/Container/Brand/Navlink/Enable', '#ffffff00'),
            ('Container (Transparent)', 'Color/Container/Neutral/Transparent interactive/Enable', '#ffffff00'),
            ('Active Fill', 'Color/Container/Neutral/Interactive/Enable', '#090909'),
            ('Background', 'Section bg/Neutral/Base', '#ffffff'),
            ('Corner Radius', 'Corner/Extra small', '4px'),
            ('Spacing', 'spacing/08', '8px'),
            ('Gap', 'spacing/12', '12px'),
            ('Padding', 'spacing/16', '16px'),
            ('Font', 'font family/graphik', 'Graphik'),
            ('Font Size', 'font size/04', '14px'),
            ('LEGACY Link Height', 'Components (LEGACY)/NavBar (LEGACY)/NavBar/Consumer/Link', '20px'),
        ],
        'legacy_note': 'Contains legacy reference <code>Components (LEGACY)/NavBar (LEGACY)/NavBar/Consumer/Link: 20</code>. This hardcoded link dimension should be migrated to a semantic spacing token.',
    },
    {
        'name': 'Footer',
        'slug': 'footer',
        'node_id': '40019515:57329',
        'variants': '6+',
        'category': 'Navigation',
        'token_system': 'Legacy (minimal tokens)',
        'token_class': 'status-critical',
        'description': 'Page footer with legal links, social icons, and copyright. Two versions exist: the latest footer (40019515) has only 2 legacy tokens, while the older 4.0 footer (40017359) uses Roboto font and /Primary color tokens — a pre-rebrand artifact. Both need full migration.',
        'anatomy': ['Container (dark background)', 'Logo', 'Link columns (legal, resources)', 'Social media icons', 'Copyright text', 'ISI link'],
        'states': ['Desktop', 'Tablet', 'Mobile'],
        'figma_variants': [
            ('Breakpoint', 'XLarge / Large / Medium / Small'),
            ('Version', 'Latest / 4.0 (Legacy)'),
        ],
        'sizes': ['Full-width (responsive)'],
        'real_tokens': [
            ('Fill', 'Fill / White', '#FFFFFF'),
            ('Icon Color', 'Icon/Neutral/White', '#FFFFFF'),
        ],
        'legacy_note': '<strong>CRITICAL:</strong> Footer has only 2 token bindings — among the least tokenized components. The older 4.0 Footer uses <strong>Roboto</strong> (not Graphik) and <code>/Primary / 000000</code> legacy tokens. Footer needs comprehensive tokenization for background, text, link, and spacing properties.',
    },
    {
        'name': 'Profile Menu',
        'slug': 'profile-menu',
        'node_id': '40019054:170681',
        'variants': '4+',
        'category': 'Navigation',
        'token_system': 'New semantic (mixed Space/ + spacing/)',
        'token_class': 'status-good',
        'description': 'User profile dropdown menu accessed from the NavBar avatar. The most richly tokenized component in the system with 33 variable bindings. Uses brand mute colors, elevation shadows, section backgrounds, and multiple type styles. Contains Corner/Medium (16px) — unique to this component.',
        'anatomy': ['Avatar trigger (Circle radius)', 'Dropdown container (elevation shadow)', 'User info section (brand mute bg)', 'Menu links (with icons)', 'Divider (subtle border)', 'Sign out action'],
        'states': ['Closed', 'Open', 'Link Hover', 'Link Active'],
        'figma_variants': [
            ('State', 'Closed / Open'),
            ('User Type', 'Consumer'),
            ('Has Avatar', 'Yes / No'),
        ],
        'sizes': ['Fixed width (320px est.)'],
        'real_tokens': [
            ('Container (Transparent)', 'Color/Container/Neutral/Transparent interactive/Enable', '#ffffff00'),
            ('User Section Bg', 'Color/Container/Brand/Mute 2', '#f9f3f1'),
            ('Brand Fill', 'Color/Container/Brand/Medium 3', '#9a6b5e'),
            ('Static Black', 'Color/Container/Neutral/Static/Black', '#090909'),
            ('Border', 'Color/Border/Neutral/Subtle 2', '#dedad7'),
            ('Border (Alpha)', 'Color/Border/Neutral/Default 08', '#09090914'),
            ('Brand Border', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Text', 'Text/Neutral/Default', '#090909'),
            ('Text (Support)', 'Text/Neutral/Support', '#787676'),
            ('Text (Brand)', 'Text/Brand/Default', '#9a6b5e'),
            ('Background', 'Section bg/Neutral/Base', '#ffffff'),
            ('Section Bg (Brand)', 'Section bg/Brand/Subtle 1', '#f1e5e2'),
            ('Shadow', 'Elevation 2/Cast down', 'multi-shadow'),
            ('Avatar Radius', 'Corner/Circle', '999px'),
            ('Container Radius', 'Corner/Medium', '16px'),
            ('Spacing (Space/6)', 'Space/6', '6px'),
            ('Gap', 'spacing/04', '4px'),
            ('Spacing', 'spacing/08', '8px'),
            ('Padding', 'spacing/16', '16px'),
            ('Section Gap', 'spacing/24', '24px'),
            ('Title', 'Body/Medium/Medium', 'Graphik Medium 16/24'),
            ('Body', 'Body/Medium/Regular', 'Graphik Regular 16/24'),
            ('Small Text', 'Body/Small/Regular', 'Graphik Regular 14/20'),
            ('Footnote', 'Footnote/Regular', 'Graphik Regular 12/18'),
        ],
        'legacy_note': 'Uses BOTH <code>Space/6</code> (PascalCase) and <code>spacing/04</code> (lowercase) within the same component. These should be unified during migration.',
    },
    {
        'name': 'Search',
        'slug': 'search',
        'node_id': '72:37300',
        'variants': '8+',
        'category': 'Form Controls',
        'token_system': 'No tokens (zero bindings)',
        'token_class': 'status-critical',
        'description': 'Search input component with filter capabilities. Has ZERO token bindings — all visual properties are hardcoded. This component needs complete tokenization before engineering handoff.',
        'anatomy': ['Container', 'Search icon', 'Input field', 'Clear button', 'Filter button (optional)'],
        'states': ['Empty', 'Focused', 'With text', 'With filters active'],
        'figma_variants': [
            ('State', 'Default / Focused / Active'),
            ('Has Filter', 'Yes / No'),
        ],
        'sizes': ['Default (full-width)'],
        'real_tokens': [],
        'legacy_note': '<strong>CRITICAL:</strong> Search has ZERO token bindings. All colors, spacing, typography, and radius values are hardcoded. This component needs full tokenization mapping to existing Text Input field tokens (same form control family). Recommend using: <code>Color/Container/Neutral/Base</code>, <code>Color/Border/Neutral/Text field/*</code>, <code>Corner/Small</code>, <code>spacing/*</code>.',
    },
    {
        'name': 'ISI (Important Safety Info)',
        'slug': 'isi',
        'node_id': '40000195:43952',
        'variants': '6',
        'category': 'Layout',
        'token_system': 'Fully legacy (Text & Icons/)',
        'token_class': 'status-critical',
        'description': 'Important Safety Information component — a regulatory requirement for pharmaceutical product pages. Uses entirely legacy token naming with large spacing values (80px, 124px) not found elsewhere in the system. Contains expandable/collapsible behavior for long-form safety content.',
        'anatomy': ['Container (neutral grey bg)', 'Headline (Graphik Regular 24)', 'Safety text items (13px body)', 'Expand/collapse toggle', 'Scroll container'],
        'states': ['Collapsed (preview)', 'Expanded (full content)', 'Sticky footer mode'],
        'figma_variants': [
            ('Breakpoint', 'XL (Logged In) / L / M / S'),
            ('State', 'Collapsed / Expanded'),
            ('Context', 'Logged In / Marketing'),
        ],
        'sizes': ['XL (logged in)', 'L (1280px)', 'M (768px)', 'S (375px)'],
        'real_tokens': [
            ('Text', 'Text & Icons/Default', '#090909'),
            ('Text (Neutral)', 'Text & Icons/Neutral', '#323131'),
            ('Text (White)', 'Text & Icons/White', '#ffffff'),
            ('Text (Light)', 'Text & Icons/Light', '#e5e5e5'),
            ('Background', 'Color/White/100', '#ffffff'),
            ('Container Bg', 'Color/Neutral Grey/40', '#f7f5f1'),
            ('Headline', 'Headline/Medium', 'Graphik Regular 24/1.2'),
            ('Body', 'Body/Small', 'Graphik Regular 13/20'),
            ('Spacing (32)', 'Spacing/32', '32px'),
            ('Spacing (48)', 'Spacing/48', '48px'),
            ('Spacing (80)', 'Spacing/80', '80px'),
            ('Spacing (124)', 'Spacing/124', '124px'),
        ],
        'legacy_note': '<strong>FULLY LEGACY:</strong> Every token uses old naming (<code>Text & Icons/</code>, <code>Color/White/100</code>, <code>Spacing/</code>). Spacing values 80px and 124px are unique to ISI — may need new tokens in the semantic system. Migration map: <code>Text & Icons/Default</code> → <code>Text/Neutral/Default</code>, <code>Color/Neutral Grey/40</code> → <code>Color/Container/Neutral/Mute 1</code>.',
    },
    {
        'name': 'Brand Container',
        'slug': 'brand-container',
        'node_id': '40006816:21702',
        'variants': '6',
        'category': 'Brand / Logos',
        'token_system': 'Legacy (minimal tokens)',
        'token_class': 'status-critical',
        'description': 'Brand-specific styled containers for product pages (Botox, Juvederm, Kybella, SkinVive, Skinmedica, Juvederm Voluma XC). Only 4 legacy tokens found — most brand-specific styling appears hardcoded per product. Each brand has unique color schemes that may need dedicated brand token collections.',
        'anatomy': ['Outer container', 'Brand logo', 'Brand gradient/color (product-specific)', 'Content area', 'Border/divider'],
        'states': ['Default'],
        'figma_variants': [
            ('Brand', 'Botox / Juvederm / Kybella / SkinVive / Skinmedica / Juvederm Voluma XC'),
        ],
        'sizes': ['Responsive (container-width)'],
        'real_tokens': [
            ('Spacing', 'Spacing/16', '16px'),
            ('Gap', 'Spacing/8', '8px'),
            ('Border (Light)', 'Color/Black/20', '#e5e5e5'),
            ('Text (Dark)', 'Color/Black/50', '#323131'),
        ],
        'legacy_note': '<strong>CRITICAL:</strong> Only 4 tokens, all legacy naming (<code>Spacing/</code>, <code>Color/Black/</code>). Brand-specific colors appear hardcoded. Consider creating a brand token collection: <code>Color/Brand/Botox/*</code>, <code>Color/Brand/Juvederm/*</code>, etc. Migration: <code>Spacing/16</code> → <code>spacing/16</code>, <code>Color/Black/20</code> → <code>Color/Border/Neutral/Subtle 2</code>.',
    },
    {
        'name': 'Card (Product)',
        'slug': 'card',
        'node_id': '40006816:21739',
        'variants': '20+',
        'category': 'Data Display',
        'token_system': 'Fully legacy (Text & Icons/ + Desktop/)',
        'token_class': 'status-critical',
        'description': 'Product-specific card used throughout the application for courses, events, and content. FULLY LEGACY — uses Text & Icons/ naming, Desktop/P3 font tokens, and Color/Dusty Rose/100. High-priority migration target as cards appear on every major screen.',
        'anatomy': ['Container (with shadow/border)', 'Image area (top)', 'Content area', 'Title (Headline/Small Medium)', 'Description (Body/Small)', 'Metadata (P3 font)', 'Action button', 'Brand accent (Dusty Rose)'],
        'states': ['Default', 'Hover', 'Selected', 'Loading'],
        'figma_variants': [
            ('Size', 'XL / L / M / S'),
            ('Type', 'Standard (product specific) / List / Marketing / Article'),
            ('State', 'Default / Hover'),
            ('Has Image', 'Yes / No'),
        ],
        'sizes': ['XL (1440px)', 'L (1280px)', 'M (768px)', 'S (375px)'],
        'real_tokens': [
            ('Text', 'Text & Icons/Default', '#090909'),
            ('Text (White)', 'Text & Icons/White', '#ffffff'),
            ('Text (Neutral)', 'Text & Icons/Neutral', '#323131'),
            ('Text (Subdued)', 'Text & Icons/Subdued', '#818386'),
            ('Brand Accent', 'Color/Dusty Rose/100', '#c08676'),
            ('Background', 'Color/White/100', '#ffffff'),
            ('Border/Divider', 'Color/Neutral Grey/80', '#e9e5de'),
            ('Dark Fill', 'Color/Black/50', '#323131'),
            ('Meta Font', 'Desktop/P3', 'Graphik Regular 13/24'),
            ('Title', 'Headline/Small (Medium)', 'Graphik Medium 22/1.2'),
            ('Body', 'Body/Small', 'Graphik Regular 13/20'),
            ('Button', 'Button/Regular', 'Graphik Regular 16/1.5'),
            ('Spacing (0)', 'Spacing/0', '0px'),
            ('Spacing (8)', 'Spacing/8', '8px'),
            ('Spacing (12)', 'Spacing/12', '12px'),
            ('Spacing (16)', 'Spacing/16', '16px'),
            ('Spacing (24)', 'Spacing/24', '24px'),
        ],
        'legacy_note': '<strong>HIGH PRIORITY MIGRATION:</strong> Cards appear on every major screen (Home Dashboard, Course Catalog, Live Events). All 17 tokens use legacy naming. Migration map: <code>Text & Icons/Default</code> → <code>Text/Neutral/Default</code>, <code>Color/Dusty Rose/100</code> → <code>Color/Border/Brand/Medium 3</code> or new brand token, <code>Desktop/P3</code> → <code>Body/Small/Regular</code>, <code>Headline/Small (Medium)</code> → needs new semantic headline token.',
    },
    {
        'name': 'Progress Bar',
        'slug': 'progress-bar',
        'node_id': '40007190:39151',
        'variants': '4+',
        'category': 'Data Display',
        'token_system': 'Legacy (AMIO/Primary — oldest system)',
        'token_class': 'status-critical',
        'description': 'Linear progress indicator used in course completion tracking. Uses the OLDEST token system found in the design system: AMIO/Primary/ prefix. Also uses Color/Dusty Rose/ legacy naming. Highest migration priority among data display components.',
        'anatomy': ['Track (background bar)', 'Fill (progress indicator)', 'Percentage label', 'Optional course count text'],
        'states': ['0%', '25%', '50%', '75%', '100%', 'Indeterminate'],
        'figma_variants': [
            ('Progress', '0% / 25% / 50% / 75% / 100%'),
            ('Size', 'Default'),
            ('Has Label', 'Yes / No'),
        ],
        'sizes': ['Default (container-width)'],
        'real_tokens': [
            ('Track Color (Light)', 'Color/Dusty Rose/60', '#e7cdc0'),
            ('Fill Color', 'Color/Dusty Rose/100', '#c08676'),
            ('Text (Black)', 'AMIO/Primary/Black', '#000000'),
            ('Fill Alt', 'AMIO/Primary/Dusty Rose', '#c08676'),
            ('Label Font', 'Caption/Regular', 'Graphik Regular 13/24 (3px tracking)'),
        ],
        'legacy_note': '<strong>OLDEST TOKEN SYSTEM:</strong> Uses <code>AMIO/Primary/</code> prefix — the earliest naming convention found, pre-dating even <code>Text & Icons/</code>. Migration map: <code>AMIO/Primary/Black</code> → <code>Text/Neutral/Default</code>, <code>AMIO/Primary/Dusty Rose</code> → <code>Color/Container/Brand/Interactive/Enable</code> or brand token, <code>Color/Dusty Rose/60</code> → needs new semantic track token, <code>Caption/Regular</code> → <code>Body/Small/Regular</code>.',
    },
]

OUT_DIR = '/Users/donnysmith/Projects/cloud/AMI-Design-System/components'

def build_page(comp):
    # Token system badge
    tc = comp.get('token_class', 'status-info')
    system_badge = f'<span class="status-badge {tc}">{comp["token_system"]}</span>'

    # Figma variant properties table
    fv_rows = ''
    for prop, vals in comp.get('figma_variants', []):
        fv_rows += f'          <tr><td><strong>{prop}</strong></td><td>{vals}</td></tr>\n'

    variants_html = ''
    if fv_rows:
        variants_html = f'''
    <div class="subsection">
      <h3 class="subsection-title">Figma Variant Properties</h3>
      <table class="data-table">
        <thead><tr><th>Property</th><th>Values</th></tr></thead>
        <tbody>
{fv_rows}        </tbody>
      </table>
    </div>'''

    # Sizes
    sizes_html = ''
    if comp.get('sizes'):
        size_items = ''.join(f'<span class="status-badge" style="margin-right:8px;background:var(--bg-page);color:var(--text-default)">{s}</span>' for s in comp['sizes'])
        sizes_html = f'''
    <div class="subsection">
      <h3 class="subsection-title">Sizes</h3>
      <div style="display:flex;flex-wrap:wrap;gap:8px">{size_items}</div>
    </div>'''

    # Anatomy
    anatomy_items = ''.join(f'<li>{part}</li>' for part in comp.get('anatomy', []))
    anatomy_html = f'''
    <div class="subsection">
      <h3 class="subsection-title">Anatomy</h3>
      <div class="card" style="padding:16px 24px">
        <ol style="margin:0;padding-left:20px;line-height:2">{anatomy_items}</ol>
      </div>
    </div>'''

    # States
    states_items = ''.join(f'<span class="status-badge" style="margin-right:8px;background:var(--bg-page);color:var(--text-default)">{s}</span>' for s in comp.get('states', []))
    states_html = f'''
    <div class="subsection">
      <h3 class="subsection-title">States</h3>
      <div style="display:flex;flex-wrap:wrap;gap:8px">{states_items}</div>
    </div>'''

    # Token table (real Figma data)
    token_rows = ''
    for prop, token, value in comp.get('real_tokens', []):
        is_color = value.startswith('#') and len(value) <= 9
        swatch = f'<span style="display:inline-block;width:14px;height:14px;border-radius:3px;background:{value};border:1px solid #ddd;vertical-align:middle;margin-right:6px"></span>' if is_color else ''
        token_rows += f'          <tr><td>{prop}</td><td><span class="token-name">{token}</span></td><td>{swatch}{value}</td></tr>\n'

    tokens_html = ''
    if token_rows:
        tokens_html = f'''
    <div class="subsection">
      <h3 class="subsection-title">Token Usage <span class="status-badge status-good" style="font-size:10px">From Figma</span></h3>
      <table class="data-table">
        <thead><tr><th>Property</th><th>Token Path</th><th>Resolved Value</th></tr></thead>
        <tbody>
{token_rows}        </tbody>
      </table>
    </div>'''
    else:
        tokens_html = '''
    <div class="subsection">
      <h3 class="subsection-title">Token Usage</h3>
      <div class="issue-card gap">
        <h4>No Token Bindings Found</h4>
        <p>This component returned zero variable definitions from Figma. All visual properties appear to be hardcoded.</p>
      </div>
    </div>'''

    # Legacy note
    legacy_html = ''
    if comp.get('legacy_note'):
        legacy_html = f'''
    <div class="issue-card info" style="margin-top:16px">
      <h4>Migration Note</h4>
      <p>{comp['legacy_note']}</p>
    </div>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{comp['name']} — AMI Design System Audit</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>

<nav class="site-nav">
  <div class="nav-inner">
    <a href="../index.html" class="nav-brand">AMI Design System</a>
    <div class="nav-links">
      <a href="../index.html">Overview</a>
      <a href="../tokens.html">Tokens</a>
      <a href="../components.html" class="active">Components</a>
      <a href="../screens.html">Screens</a>
      <a href="../assets.html">Assets</a>
      <a href="../architecture.html">Architecture</a>
      <a href="../patterns.html">Patterns</a>
      <a href="../remediation.html">Remediation</a>
    </div>
  </div>
</nav>

<div class="container" style="max-width:960px">
  <div style="margin-bottom:8px">
    <a href="../components.html" style="color:var(--brand);text-decoration:none;font-size:13px">&larr; All Components</a>
  </div>

  <div class="section-header" style="flex-wrap:wrap;gap:8px">
    <h1 style="margin:0">{comp['name']}</h1>
    {system_badge}
  </div>
  <p style="color:var(--text-secondary);margin-top:4px;font-size:13px">
    Figma Node: <code>{comp['node_id']}</code> &middot; Category: {comp['category']} &middot; Variants: {comp['variants']}
  </p>

  <div class="card" style="padding:20px;margin:16px 0">
    <p style="margin:0;line-height:1.6">{comp['description']}</p>
  </div>

  <div class="section">
{anatomy_html}
{states_html}
{sizes_html}
{variants_html}
{tokens_html}
{legacy_html}

    <div class="subsection" style="margin-top:24px">
      <h3 class="subsection-title">Engineering Notes</h3>
      <div class="card" style="padding:16px 24px">
        <ul style="margin:0;padding-left:20px;line-height:2">
          <li>Component category: <strong>{comp['category']}</strong></li>
          <li>Token system: <strong>{comp['token_system']}</strong></li>
          <li>Figma node: <code>{comp['node_id']}</code></li>
          <li>Total token bindings: <strong>{len(comp.get('real_tokens', []))}</strong></li>
          <li>Font family: Graphik (verify weight availability)</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<footer class="site-footer">
  AMI Design System Audit &mdash; Generated February 27, 2026 &mdash; <a href="https://github.com/d999ss/AMI-Design-System">GitHub</a>
</footer>

</body>
</html>'''

# Generate all pages
for comp in components:
    html = build_page(comp)
    path = os.path.join(OUT_DIR, f'{comp["slug"]}.html')
    with open(path, 'w') as f:
        f.write(html)
    print(f'  {comp["slug"]}.html ({len(html):,} bytes) — {comp["token_system"]}')

print(f'\nGenerated {len(components)} Batch 2 component detail pages')
