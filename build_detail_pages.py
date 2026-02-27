#!/usr/bin/env python3
"""Generate individual component detail pages for Tier 1 components."""
import json
import os

# Component definitions with all known data
# Format: (name, node_id, variants, category, token_system, description, anatomy_parts, states, props)
components = [
    {
        'name': 'Button',
        'slug': 'button',
        'node_id': '40006598:72259',
        'variants': '308+',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Primary interactive element for triggering actions. The most variant-rich component in the system with 308+ configurations spanning sizes, styles, states, and icon positions.',
        'anatomy': ['Container', 'Label text', 'Leading icon (optional)', 'Trailing icon (optional)'],
        'states': ['Default', 'Hover', 'Active/Pressed', 'Focused', 'Disabled'],
        'variants_list': [
            ('Primary', 'Filled background, high emphasis'),
            ('Secondary', 'Outlined, medium emphasis'),
            ('Tertiary', 'Text-only, low emphasis'),
            ('Destructive', 'Red variant for dangerous actions'),
        ],
        'sizes': ['Small (32px)', 'Medium (40px)', 'Large (48px)'],
        'tokens': [
            ('Background (Primary)', 'Color/Button/Primary/Background/Default', '#9A6B5E'),
            ('Background (Hover)', 'Color/Button/Primary/Background/Hover', '#876054'),
            ('Text (Primary)', 'Color/Button/Primary/Text/Default', '#FFFFFF'),
            ('Border (Secondary)', 'Color/Button/Secondary/Border/Default', '#9A6B5E'),
            ('Background (Disabled)', 'Color/Button/Primary/Background/Disabled', '#ECE9E5'),
            ('Border Radius', 'Radius/Button', '4px'),
            ('Padding Horizontal', 'Spacing/Button/Horizontal', '16px'),
            ('Padding Vertical', 'Spacing/Button/Vertical', '8px'),
            ('Font Family', 'Font/Button', 'Inter'),
            ('Font Weight', 'Font/Button/Weight', '600 (Semi Bold)'),
        ],
    },
    {
        'name': 'Text Input',
        'slug': 'text-input',
        'node_id': '40006598:70760',
        'variants': '36',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Standard text field for user input. Includes label, placeholder, helper text, and error state configurations with consistent spacing and typography.',
        'anatomy': ['Container', 'Label', 'Input field', 'Placeholder text', 'Helper text', 'Error message', 'Leading icon (optional)', 'Trailing icon (optional)'],
        'states': ['Default', 'Hover', 'Focused', 'Filled', 'Error', 'Disabled'],
        'variants_list': [
            ('Default', 'Standard text input with label'),
            ('With Helper', 'Includes helper text below input'),
            ('With Error', 'Error state with red border and message'),
            ('With Icons', 'Leading and/or trailing icon support'),
        ],
        'sizes': ['Medium (40px)', 'Large (48px)'],
        'tokens': [
            ('Border (Default)', 'Color/Input/Border/Default', '#B3B0AE'),
            ('Border (Focus)', 'Color/Input/Border/Focus', '#9A6B5E'),
            ('Border (Error)', 'Color/Input/Border/Error', '#D32F2F'),
            ('Background', 'Color/Input/Background/Default', '#FFFFFF'),
            ('Label Text', 'Color/Input/Label/Default', '#090909'),
            ('Placeholder', 'Color/Input/Placeholder/Default', '#787676'),
            ('Helper Text', 'Color/Input/Helper/Default', '#787676'),
            ('Error Text', 'Color/Input/Error/Default', '#D32F2F'),
            ('Border Radius', 'Radius/Input', '4px'),
            ('Font Family', 'Font/Input', 'Inter'),
        ],
    },
    {
        'name': 'Select',
        'slug': 'select',
        'node_id': '40006598:84030',
        'variants': '72',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Dropdown selection component for choosing from a list of options. Supports single and multi-select modes with search functionality.',
        'anatomy': ['Container', 'Label', 'Selected value', 'Dropdown indicator', 'Option list', 'Option item', 'Checkmark (multi)', 'Search field (optional)'],
        'states': ['Default', 'Hover', 'Open', 'Selected', 'Multi-selected', 'Error', 'Disabled'],
        'variants_list': [
            ('Single Select', 'Choose one option from dropdown'),
            ('Multi Select', 'Choose multiple options with checkmarks'),
            ('Searchable', 'Type-ahead filtering of options'),
            ('With Error', 'Error state with validation message'),
        ],
        'sizes': ['Medium (40px)', 'Large (48px)'],
        'tokens': [
            ('Border (Default)', 'Color/Select/Border/Default', '#B3B0AE'),
            ('Border (Open)', 'Color/Select/Border/Focus', '#9A6B5E'),
            ('Background', 'Color/Select/Background/Default', '#FFFFFF'),
            ('Dropdown Background', 'Color/Select/Dropdown/Background', '#FFFFFF'),
            ('Option Hover', 'Color/Select/Option/Hover', '#F7F6F5'),
            ('Selected Option', 'Color/Select/Option/Selected', '#F1E5E2'),
            ('Border Radius', 'Radius/Select', '4px'),
        ],
    },
    {
        'name': 'Accordion',
        'slug': 'accordion',
        'node_id': '40006598:90126',
        'variants': '15',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Expandable/collapsible content sections. Used for FAQs, settings panels, and progressive disclosure patterns.',
        'anatomy': ['Container', 'Header', 'Title text', 'Expand/collapse icon', 'Content area', 'Divider'],
        'states': ['Collapsed', 'Expanded', 'Hover', 'Focused', 'Disabled'],
        'variants_list': [
            ('Default', 'Standard accordion with dividers'),
            ('Bordered', 'Outlined container style'),
            ('Flush', 'No borders, minimal styling'),
        ],
        'sizes': [],
        'tokens': [
            ('Background', 'Color/Accordion/Background/Default', '#FFFFFF'),
            ('Border', 'Color/Accordion/Border/Default', '#ECE9E5'),
            ('Title Text', 'Color/Accordion/Title/Default', '#090909'),
            ('Icon', 'Color/Accordion/Icon/Default', '#787676'),
            ('Content Text', 'Color/Accordion/Content/Default', '#3D3D3C'),
        ],
    },
    {
        'name': 'Chip',
        'slug': 'chip',
        'node_id': '40006598:71720',
        'variants': '10',
        'category': 'Form Controls',
        'token_system': 'Mixed',
        'token_class': 'status-gap',
        'description': 'Compact interactive element for filtering, tagging, and selection. Used extensively in course catalog filters and tag displays.',
        'anatomy': ['Container', 'Label text', 'Leading icon (optional)', 'Close/remove icon (optional)'],
        'states': ['Default', 'Selected', 'Hover', 'Disabled'],
        'variants_list': [
            ('Filter', 'Toggleable chip for filtering content'),
            ('Input', 'Removable chip showing selected values'),
            ('Suggestion', 'Clickable suggestion chip'),
        ],
        'sizes': ['Small (24px)', 'Medium (32px)'],
        'tokens': [
            ('Background (Default)', 'Mixed system', '#F7F6F5'),
            ('Background (Selected)', 'Mixed system', '#F1E5E2'),
            ('Border (Default)', 'Mixed system', '#B3B0AE'),
            ('Text', 'Mixed system', '#3D3D3C'),
            ('Border Radius', 'Mixed system', '16px (pill)'),
        ],
    },
    {
        'name': 'Badge',
        'slug': 'badge',
        'node_id': '40003841:33610',
        'variants': '30',
        'category': 'Data Display',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Status indicator used to highlight states, counts, or categories. Appears on cards, navigation items, and profile elements.',
        'anatomy': ['Container', 'Label text', 'Leading dot/icon (optional)'],
        'states': ['Default'],
        'variants_list': [
            ('Neutral', 'Gray badge for general labels'),
            ('Success', 'Green for positive status'),
            ('Warning', 'Yellow/amber for caution'),
            ('Error', 'Red for errors or alerts'),
            ('Info', 'Blue for informational'),
            ('Brand', 'Brand color for special status'),
        ],
        'sizes': ['Small', 'Medium'],
        'tokens': [
            ('Background (Neutral)', 'Color/Badge/Neutral/Background', '#F7F6F5'),
            ('Background (Success)', 'Color/Badge/Success/Background', '#E8F5E9'),
            ('Background (Warning)', 'Color/Badge/Warning/Background', '#FFF8E1'),
            ('Background (Error)', 'Color/Badge/Error/Background', '#FFEBEE'),
            ('Background (Info)', 'Color/Badge/Info/Background', '#E3F2FD'),
            ('Text (Neutral)', 'Color/Badge/Neutral/Text', '#787676'),
            ('Border Radius', 'Radius/Badge', '4px'),
        ],
    },
    {
        'name': 'Link - Standalone',
        'slug': 'link',
        'node_id': '40008110:15068',
        'variants': '96',
        'category': 'Navigation',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Standalone navigation link with consistent hover/focus styling. Used throughout the application for page navigation and external references.',
        'anatomy': ['Link text', 'Underline', 'Leading icon (optional)', 'Trailing icon (optional)'],
        'states': ['Default', 'Hover', 'Active', 'Visited', 'Focused', 'Disabled'],
        'variants_list': [
            ('Default', 'Standard text link'),
            ('With Icon', 'Link with leading or trailing icon'),
            ('External', 'Opens in new tab, with external indicator'),
            ('Inline', 'Used within body text'),
        ],
        'sizes': ['Small (12px)', 'Medium (14px)', 'Large (16px)'],
        'tokens': [
            ('Text (Default)', 'Color/Link/Text/Default', '#9A6B5E'),
            ('Text (Hover)', 'Color/Link/Text/Hover', '#876054'),
            ('Text (Visited)', 'Color/Link/Text/Visited', '#6D4C41'),
            ('Underline', 'Color/Link/Underline/Default', '#9A6B5E'),
            ('Font Weight', 'Font/Link/Weight', '500 (Medium)'),
        ],
    },
    {
        'name': 'Checkbox',
        'slug': 'checkbox',
        'node_id': '40006598:81360',
        'variants': '12',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Binary selection control for forms. Supports individual checkboxes and checkbox lists with labels and descriptions.',
        'anatomy': ['Checkbox box', 'Checkmark icon', 'Label text', 'Description (optional)'],
        'states': ['Unchecked', 'Checked', 'Indeterminate', 'Hover', 'Focused', 'Disabled'],
        'variants_list': [
            ('Default', 'Standard checkbox with label'),
            ('With Description', 'Checkbox with helper description text'),
            ('Indeterminate', 'Partial selection state for parent checkboxes'),
        ],
        'sizes': ['Medium (20px)', 'Large (24px)'],
        'tokens': [
            ('Border (Unchecked)', 'Color/Checkbox/Border/Default', '#B3B0AE'),
            ('Background (Checked)', 'Color/Checkbox/Background/Checked', '#9A6B5E'),
            ('Checkmark', 'Color/Checkbox/Icon/Checked', '#FFFFFF'),
            ('Label', 'Color/Checkbox/Label/Default', '#090909'),
            ('Border Radius', 'Radius/Checkbox', '4px'),
        ],
    },
    {
        'name': 'Tabs',
        'slug': 'tabs',
        'node_id': '40008120:29000',
        'variants': '32',
        'category': 'Navigation',
        'token_system': 'Mixed',
        'token_class': 'status-gap',
        'description': 'Horizontal tab navigation for switching between content views. Used in course catalog, live events, and profile sections.',
        'anatomy': ['Tab bar container', 'Tab item', 'Tab label', 'Active indicator (underline)', 'Badge (optional)', 'Icon (optional)'],
        'states': ['Default', 'Active', 'Hover', 'Focused', 'Disabled'],
        'variants_list': [
            ('Default', 'Standard text tabs'),
            ('With Icons', 'Tabs with leading icons'),
            ('With Badge', 'Tabs with count badges'),
            ('Scrollable', 'Horizontally scrollable tab set'),
        ],
        'sizes': [],
        'tokens': [
            ('Text (Default)', 'Mixed system', '#787676'),
            ('Text (Active)', 'Mixed system', '#9A6B5E'),
            ('Indicator', 'Mixed system', '#9A6B5E'),
            ('Background', 'Mixed system', 'transparent'),
            ('Border Bottom', 'Mixed system', '#ECE9E5'),
        ],
    },
    {
        'name': 'Tooltip',
        'slug': 'tooltip',
        'node_id': '40003841:33483',
        'variants': '4',
        'category': 'Feedback',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Contextual popup displaying supplementary information on hover or focus. Used for icon explanations and truncated text.',
        'anatomy': ['Container', 'Content text', 'Arrow/pointer', 'Trigger element'],
        'states': ['Hidden', 'Visible'],
        'variants_list': [
            ('Top', 'Arrow pointing down, tooltip above trigger'),
            ('Bottom', 'Arrow pointing up, tooltip below trigger'),
            ('Left', 'Arrow pointing right, tooltip left of trigger'),
            ('Right', 'Arrow pointing left, tooltip right of trigger'),
        ],
        'sizes': [],
        'tokens': [
            ('Background', 'Color/Tooltip/Background', '#090909'),
            ('Text', 'Color/Tooltip/Text', '#FFFFFF'),
            ('Border Radius', 'Radius/Tooltip', '4px'),
            ('Padding', 'Spacing/Tooltip', '8px 12px'),
        ],
    },
]

# Batch 2 components (will be added later)
batch2 = [
    {
        'name': 'Action Menu',
        'slug': 'action-menu',
        'node_id': '40006598:82298',
        'variants': '6',
        'category': 'Navigation',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Contextual menu triggered by a button or icon. Displays a list of actions available for an item.',
        'anatomy': ['Trigger button', 'Menu container', 'Menu item', 'Divider', 'Icon (optional)'],
        'states': ['Closed', 'Open', 'Item Hover', 'Item Active'],
        'variants_list': [
            ('Default', 'Standard action menu'),
            ('With Icons', 'Menu items with leading icons'),
            ('With Dividers', 'Grouped items separated by dividers'),
        ],
        'sizes': [],
        'tokens': [
            ('Background', 'Color/ActionMenu/Background', '#FFFFFF'),
            ('Item Hover', 'Color/ActionMenu/Item/Hover', '#F7F6F5'),
            ('Text', 'Color/ActionMenu/Text', '#090909'),
            ('Shadow', 'Elevation/ActionMenu', '0 4px 16px rgba(0,0,0,0.12)'),
        ],
    },
    {
        'name': 'Counter Badge',
        'slug': 'counter-badge',
        'node_id': '40006598:71412',
        'variants': '2',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Numeric indicator showing count values. Used on notification icons and navigation elements.',
        'anatomy': ['Container (circle)', 'Count text'],
        'states': ['Default', 'Overflow (99+)'],
        'variants_list': [
            ('Default', 'Shows numeric count'),
            ('Dot', 'Simple dot indicator without number'),
        ],
        'sizes': ['Small (16px)', 'Medium (20px)'],
        'tokens': [
            ('Background', 'Color/CounterBadge/Background', '#D32F2F'),
            ('Text', 'Color/CounterBadge/Text', '#FFFFFF'),
            ('Border Radius', 'Radius/CounterBadge', '999px'),
        ],
    },
    {
        'name': 'Button Group',
        'slug': 'button-group',
        'node_id': '40006598:81018',
        'variants': '36',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Set of related buttons displayed as a single visual unit. Used for toggle options and segmented controls.',
        'anatomy': ['Container', 'Button items', 'Active indicator', 'Dividers'],
        'states': ['Default', 'One Active', 'Multi Active', 'Disabled'],
        'variants_list': [
            ('Outlined', 'Bordered button group'),
            ('Filled', 'Active button has filled background'),
        ],
        'sizes': ['Small', 'Medium', 'Large'],
        'tokens': [
            ('Border', 'Color/ButtonGroup/Border', '#B3B0AE'),
            ('Background (Active)', 'Color/ButtonGroup/Active/Background', '#9A6B5E'),
            ('Text (Active)', 'Color/ButtonGroup/Active/Text', '#FFFFFF'),
            ('Border Radius', 'Radius/ButtonGroup', '4px'),
        ],
    },
    {
        'name': 'Toggle',
        'slug': 'toggle',
        'node_id': '40015525:22363',
        'variants': '2',
        'category': 'Form Controls',
        'token_system': 'Mixed',
        'token_class': 'status-gap',
        'description': 'Binary on/off switch control for settings and preferences.',
        'anatomy': ['Track', 'Thumb', 'Label (optional)'],
        'states': ['Off', 'On', 'Hover', 'Focused', 'Disabled'],
        'variants_list': [
            ('Default', 'Standard toggle switch'),
            ('With Label', 'Toggle with adjacent label text'),
        ],
        'sizes': ['Medium'],
        'tokens': [
            ('Track (Off)', 'Mixed system', '#B3B0AE'),
            ('Track (On)', 'Mixed system', '#9A6B5E'),
            ('Thumb', 'Mixed system', '#FFFFFF'),
        ],
    },
    {
        'name': 'Snackbar',
        'slug': 'snackbar',
        'node_id': '40017359:55323',
        'variants': '3',
        'category': 'Feedback',
        'token_system': 'Mixed',
        'token_class': 'status-gap',
        'description': 'Temporary notification bar appearing at the bottom of the screen for action confirmations and brief messages.',
        'anatomy': ['Container', 'Message text', 'Action button (optional)', 'Close icon (optional)'],
        'states': ['Visible', 'Dismissing'],
        'variants_list': [
            ('Default', 'Standard snackbar message'),
            ('With Action', 'Includes action button'),
            ('Error', 'Red variant for error messages'),
        ],
        'sizes': [],
        'tokens': [
            ('Background', 'Mixed system', '#3D3D3C'),
            ('Text', 'Mixed system', '#FFFFFF'),
            ('Action Text', 'Mixed system', '#F1E5E2'),
        ],
    },
    {
        'name': 'Progress Circle',
        'slug': 'progress-circle',
        'node_id': '40000054:23550',
        'variants': '2',
        'category': 'Data Display',
        'token_system': 'Mixed',
        'token_class': 'status-gap',
        'description': 'Circular progress indicator showing completion percentage. Used for course progress and achievement tracking.',
        'anatomy': ['Track circle', 'Progress arc', 'Center text (percentage)', 'Label (optional)'],
        'states': ['Empty (0%)', 'In Progress', 'Complete (100%)'],
        'variants_list': [
            ('Default', 'Standard circular progress'),
            ('With Label', 'Progress circle with text label below'),
        ],
        'sizes': ['Small (40px)', 'Medium (64px)', 'Large (96px)'],
        'tokens': [
            ('Track', 'Mixed system', '#ECE9E5'),
            ('Progress', 'Mixed system', '#9A6B5E'),
            ('Text', 'Mixed system', '#090909'),
        ],
    },
    {
        'name': 'Avatar',
        'slug': 'avatar',
        'node_id': '40019054:169935',
        'variants': '3',
        'category': 'Data Display',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'User profile image or initials display. Used in navigation, profile sections, and user references.',
        'anatomy': ['Container (circle)', 'Image/initials', 'Status indicator (optional)'],
        'states': ['With Image', 'With Initials', 'Fallback'],
        'variants_list': [
            ('Image', 'Displays user photo'),
            ('Initials', 'Shows user initials on colored background'),
            ('Icon', 'Generic user icon as fallback'),
        ],
        'sizes': ['Small (24px)', 'Medium (32px)', 'Large (40px)', 'XLarge (64px)'],
        'tokens': [
            ('Background', 'Color/Avatar/Background', '#F1E5E2'),
            ('Text', 'Color/Avatar/Text', '#9A6B5E'),
            ('Border', 'Color/Avatar/Border', '#FFFFFF'),
        ],
    },
    {
        'name': 'Alert - Inpage',
        'slug': 'alert-inpage',
        'node_id': '40007190:39217',
        'variants': '3',
        'category': 'Feedback',
        'token_system': 'Mixed',
        'token_class': 'status-gap',
        'description': 'Inline alert banner for contextual messages within page content. Supports info, warning, error, and success variants.',
        'anatomy': ['Container', 'Icon', 'Title (optional)', 'Message text', 'Close button (optional)', 'Action link (optional)'],
        'states': ['Default', 'Dismissible'],
        'variants_list': [
            ('Info', 'Blue informational alert'),
            ('Warning', 'Amber warning alert'),
            ('Error', 'Red error alert'),
            ('Success', 'Green success alert'),
        ],
        'sizes': [],
        'tokens': [
            ('Background (Info)', 'Mixed system', '#E3F2FD'),
            ('Background (Warning)', 'Mixed system', '#FFF8E1'),
            ('Background (Error)', 'Mixed system', '#FFEBEE'),
            ('Background (Success)', 'Mixed system', '#E8F5E9'),
            ('Border Radius', 'Mixed system', '4px'),
        ],
    },
]

all_components = components + batch2

OUT_DIR = '/Users/donnysmith/Projects/cloud/AMI-Design-System/components'

def build_page(comp):
    has_screenshot = os.path.exists(f'/Users/donnysmith/Projects/cloud/AMI-Design-System/img/components/{comp["slug"]}.png')

    screenshot_html = ''
    if has_screenshot:
        screenshot_html = f'''
      <div class="card" style="padding:24px;text-align:center;margin-bottom:24px">
        <img src="../img/components/{comp['slug']}.png" alt="{comp['name']} component variants" style="max-width:100%;border-radius:4px" loading="lazy">
      </div>'''
    else:
        screenshot_html = f'''
      <div class="card" style="padding:48px 24px;text-align:center;margin-bottom:24px;background:var(--bg-page)">
        <div style="font-size:48px;margin-bottom:12px;opacity:0.3">&#9634;</div>
        <div style="font-size:14px;font-weight:500;color:var(--text-support)">Figma screenshot pending</div>
        <div style="font-size:11px;color:var(--text-disabled);margin-top:4px">Node ID: {comp['node_id']}</div>
      </div>'''

    # Variants table
    variants_rows = ''
    for vname, vdesc in comp.get('variants_list', []):
        variants_rows += f'          <tr><td><strong>{vname}</strong></td><td>{vdesc}</td></tr>\n'

    variants_html = ''
    if variants_rows:
        variants_html = f'''
    <div class="subsection">
      <h3 class="subsection-title">Variants</h3>
      <table class="data-table">
        <thead><tr><th>Variant</th><th>Description</th></tr></thead>
        <tbody>
{variants_rows}        </tbody>
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

    # Token table
    token_rows = ''
    for prop, token, value in comp.get('tokens', []):
        is_color = value.startswith('#')
        swatch = f'<span style="display:inline-block;width:14px;height:14px;border-radius:3px;background:{value};border:1px solid #eee;vertical-align:middle;margin-right:6px"></span>' if is_color else ''
        token_rows += f'          <tr><td>{prop}</td><td><span class="token-name">{token}</span></td><td>{swatch}{value}</td></tr>\n'

    tokens_html = ''
    if token_rows:
        tokens_html = f'''
    <div class="subsection">
      <h3 class="subsection-title">Token Usage</h3>
      <table class="data-table">
        <thead><tr><th>Property</th><th>Token</th><th>Value</th></tr></thead>
        <tbody>
{token_rows}        </tbody>
      </table>
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

<div class="page">
  <div class="breadcrumb">
    <a href="../components.html">Components</a> &rsaquo; {comp['name']}
  </div>

  <div class="page-header">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px">
      <div>
        <h1>{comp['name']}</h1>
        <p class="subtitle">{comp['description']}</p>
      </div>
      <span class="status-badge {comp['token_class']}">{comp['token_system']}</span>
    </div>
    <div class="meta">
      <strong>Category:</strong> {comp['category']} &middot;
      <strong>Variants:</strong> {comp['variants']} &middot;
      <strong>Node ID:</strong> <span class="token-name">{comp['node_id']}</span> &middot;
      <strong>Tier:</strong> <span style="display:inline-block;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:600;background:#f1e5e2;color:#9a6b5e">T1</span>
    </div>
  </div>

  <div class="section">
    <h2 class="section-title">Visual Reference</h2>
    {screenshot_html}
  </div>

  <div class="section">
    <h2 class="section-title">Component Specification</h2>
    {anatomy_html}
    {states_html}
    {variants_html}
    {sizes_html}
  </div>

  <div class="section">
    <h2 class="section-title">Design Tokens</h2>
    <p class="section-desc">Token bindings for this component. Token system: <strong>{comp['token_system']}</strong>.</p>
    {tokens_html}
  </div>

  <div class="section">
    <h2 class="section-title">Engineering Notes</h2>
    <div class="card" style="padding:24px">
      <ul style="margin:0;padding-left:20px;line-height:2;color:var(--text-support)">
        <li>Figma component node: <span class="token-name">{comp['node_id']}</span></li>
        <li>Token system: {comp['token_system']} &mdash; {'ready for direct token-to-CSS mapping' if 'New' in comp['token_system'] else 'requires token migration before implementation'}</li>
        <li>{comp['variants']} total variant configurations in Figma</li>
        <li>Auto-layout structure to be documented after Figma MCP extraction</li>
      </ul>
    </div>
  </div>
</div>

<footer class="site-footer">
  AMI Design System Audit &mdash; Generated February 27, 2026 &mdash; <a href="https://github.com/d999ss/AMI-Design-System">GitHub</a>
</footer>

</body>
</html>
'''

# Generate all pages
for comp in all_components:
    html = build_page(comp)
    path = os.path.join(OUT_DIR, f'{comp["slug"]}.html')
    with open(path, 'w') as f:
        f.write(html)
    print(f'  Generated {comp["slug"]}.html ({len(html)} bytes)')

print(f'\nGenerated {len(all_components)} component detail pages')
