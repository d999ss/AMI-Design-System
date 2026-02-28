#!/usr/bin/env python3
"""Generate components.html from inventory JSON."""
import json

with open('/tmp/ami_inventory.json') as f:
    data = json.load(f)

# Tier 1 component IDs (canonical versions)
tier1 = {
    'Button': '40006598:72259',
    'Text Input': '40006598:70760',
    'Select': '40006598:84030',
    'Accordion': '40006598:90126',
    'Chip': '40006598:71720',
    'Badge': '40003841:33610',
    'Link - Standalone': '40008110:15068',
    'Checkbox': '40006598:81360',
    'Tabs': '40008120:29000',
    'Tooltip [v1.1]': '40003841:33483',
    'Action Menu': '40006598:82298',
    'Counter Badge': '40006598:71412',
    'Button Group': '40006598:81018',
    'Snackbar': '40017359:55323',
    'Toggle': '40015525:22363',
    'Progress Circle': '40000054:23550',
    'Avatar': '40019054:169935',
    'Consumer NavBar': '40019054:170805',
    'Footer': '40006816:22081',
    'User Profile Menu / Consumer': '40019054:170681',
    'Checkbox List': '40006598:90371',
    'Action List / No-selection': '40006598:71903',
    'Alert / inpage': '40007190:39217',
    'Alert / top': '40009097:47558',
}

tier1_ids = set(tier1.values())

# Token system mapping
new_semantic = {'Button', 'Text Input', 'Accordion', 'Select', 'Badge', 'Action List', 'Link', 'Checkbox', 'Profile Menu'}
mixed = {'Tabs', 'Chip', 'Modal', 'Navigation', 'Cards', 'Training Center', 'Progress Bar', 'Brand Container'}
legacy = {'Side Nav', 'Footer', 'Tabs Selectors', 'Live Events'}

def get_token_system(name):
    n = name.lower()
    for kw in ['button', 'text input', 'accordion', 'select', 'badge', 'action list', 'link -', 'checkbox', 'profile menu']:
        if kw in n:
            return 'New', 'status-good'
    for kw in ['tab', 'chip', 'modal', 'navigation', 'card', 'training', 'progress', 'brand container']:
        if kw in n:
            return 'Mixed', 'status-gap'
    for kw in ['side nav', 'footer', 'tabs selector', 'live event', 'yellow']:
        if kw in n:
            return 'Legacy', 'status-drift'
    return '—', ''

def get_tier(item):
    if item['id'] in tier1_ids:
        return 1
    if item['variants'] > 0:
        return 2
    return 3

# Build HTML
lines = []
lines.append('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Components — AMI Design System Audit</title>
<link rel="stylesheet" href="style.css">
<style>
  .tier-badge { display:inline-block; padding:2px 8px; border-radius:4px; font-size:11px; font-weight:600; }
  .tier-1 { background:#f1e5e2; color:#9a6b5e; }
  .tier-2 { background:#e3f2fd; color:#1565c0; }
  .tier-3 { background:#f7f6f5; color:#b3b0ae; }
  .cat-header td { background:#f7f6f5; font-weight:600; font-size:12px; text-transform:uppercase; letter-spacing:0.05em; color:#787676; padding:12px 16px !important; border-bottom:2px solid #ece9e5 !important; }
  .bar-chart { display:flex; flex-direction:column; gap:8px; margin-top:16px; }
  .bar-row { display:flex; align-items:center; gap:12px; }
  .bar-label { width:120px; font-size:12px; font-weight:500; text-align:right; flex-shrink:0; }
  .bar-track { flex:1; height:24px; background:#f7f6f5; border-radius:4px; overflow:hidden; }
  .bar-fill { height:100%; background:#9a6b5e; border-radius:4px; display:flex; align-items:center; justify-content:flex-end; padding-right:8px; font-size:11px; color:#fff; font-weight:600; min-width:30px; }
</style>
</head>
<body>

<nav class="site-nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand">AMI Design System</a>
    <div class="nav-links">
      <a href="index.html">Overview</a>
      <a href="tokens.html">Tokens</a>
      <a href="components.html" class="active">Components</a>
      <a href="screens.html">Screens</a>
      <a href="assets.html">Assets</a>
      <a href="architecture.html">Architecture</a>
      <a href="patterns.html">Patterns</a>
      <a href="remediation.html">Remediation</a>
    </div>
  </div>
</nav>

<div class="page">
  <div class="page-header">
    <h1>Component Inventory</h1>
    <p class="subtitle">Master inventory of all 774 elements from the Internal Only Canvas page. Components are categorized by function and tiered by documentation depth.</p>
    <div class="meta">
      <strong>Source:</strong> Page 0:2 — Internal Only Canvas (component library)<br>
      <strong>Total:</strong> 774 elements (522 frames + 252 symbols) · <strong>Tier 1:</strong> ~25 fully documented · <strong>Tier 2:</strong> screenshot + summary · <strong>Tier 3:</strong> listed
    </div>
  </div>
''')

# Stat cards
totals = data['totals']
total_variants = sum(c['variants'] for cat_items in data['categories'].values() for c in cat_items)
lines.append(f'''
  <div class="stat-row">
    <div class="stat-card"><div class="stat-number">774</div><div class="stat-label">Total Elements</div></div>
    <div class="stat-card"><div class="stat-number">522</div><div class="stat-label">Frames</div></div>
    <div class="stat-card"><div class="stat-number">252</div><div class="stat-label">Symbols</div></div>
    <div class="stat-card"><div class="stat-number">9</div><div class="stat-label">Categories</div></div>
    <div class="stat-card"><div class="stat-number">{len(tier1)}</div><div class="stat-label">Tier 1 Components</div></div>
  </div>
''')

# Category breakdown bar chart
max_count = max(totals.values())
cat_order = ['Icons', 'Brand / Logos', 'Navigation', 'Form Controls', 'Data Display', 'Layout', 'Feedback', 'Other', 'Media']
lines.append('''
  <div class="section">
    <h2 class="section-title">Category Breakdown</h2>
    <p class="section-desc">Distribution of elements across functional categories.</p>
    <div class="card" style="padding:24px">
      <div class="bar-chart">
''')
for cat in cat_order:
    count = totals.get(cat, 0)
    pct = int(count / max_count * 100)
    lines.append(f'        <div class="bar-row"><div class="bar-label">{cat}</div><div class="bar-track"><div class="bar-fill" style="width:{pct}%">{count}</div></div></div>')
lines.append('      </div>\n    </div>\n  </div>')

# Tier 1 Components
lines.append('''
  <div class="section">
    <h2 class="section-title">Tier 1 Components <span class="status-badge status-new">Full Documentation</span></h2>
    <p class="section-desc">Core components targeted for full documentation with screenshots, anatomy diagrams, variant tables, and token usage.</p>
    <div class="nav-card-grid">
''')

tier1_info = [
    # Batch 1 — Verified with real Figma token data
    ('Button', '40006598:72259', '308+', 'Form Controls', 'Mixed'),        # New + legacy coexist
    ('Text Input', '40006598:70760', '36', 'Form Controls', 'New semantic'),
    ('Select', '40006598:84030', '72', 'Form Controls', 'New semantic'),
    ('Accordion', '40006598:90126', '15', 'Form Controls', 'New semantic'),
    ('Chip', '40006598:71720', '10', 'Form Controls', 'New semantic'),      # Reclassified from Mixed
    ('Badge', '40003841:33610', '30', 'Data Display', 'New semantic'),
    ('Link - Standalone', '40008110:15068', '96', 'Navigation', 'New semantic'),
    ('Checkbox', '40006598:81360', '12', 'Form Controls', 'New semantic'),
    ('Tabs', '40008120:29000', '32', 'Navigation', 'New semantic'),         # Reclassified from Mixed
    ('Tooltip', '40003841:33483', '4', 'Feedback', 'New semantic'),
    ('Action Menu', '40006598:82298', '6', 'Navigation', 'New semantic'),
    ('Counter Badge', '40006598:71412', '2', 'Form Controls', 'New semantic'),
    ('Button Group', '40006598:81018', '36', 'Form Controls', 'New semantic'),
    ('Toggle', '40015525:22363', '2', 'Form Controls', 'Legacy'),           # Zero tokens = legacy
    ('Progress Circle', '40000054:23550', '2', 'Data Display', 'Mixed'),
    ('Avatar', '40019054:169935', '3', 'Data Display', 'New semantic'),
    ('Snackbar', '40017359:55323', '3', 'Feedback', 'Legacy'),              # Roboto + /Primary
    ('Alert / inpage', '40007190:39217', '3', 'Feedback', 'Legacy'),        # Text & Icons + Color/Utility
    ('Alert / top', '40009097:47558', '1', 'Feedback', 'Mixed'),
    ('Action List', '40006598:71903', '5', 'Form Controls', 'New semantic'),
    ('Checkbox List', '40006598:90371', '2', 'Form Controls', 'New semantic'),
    # Batch 2 — New Figma token data extracted
    ('Consumer NavBar', '40019054:170805', '24+', 'Navigation', 'New semantic'),
    ('NavDrawer', '40019054:169025', '16+', 'Navigation', 'Mixed'),         # Has LEGACY reference
    ('Footer', '40019515:57329', '6+', 'Navigation', 'Legacy'),             # 2 legacy tokens only
    ('Profile Menu', '40019054:170681', '4+', 'Navigation', 'New semantic'), # 33 tokens, richest
    ('Modal', '40006598:91459', '12+', 'Feedback', 'New semantic'),
    ('Bottom Sheet', '40009097:47982', '8+', 'Navigation', 'Mixed'),        # Has LEGACY reference
    ('Search', '72:37300', '8+', 'Form Controls', 'Legacy'),                # Zero tokens
    ('ISI', '40000195:43952', '6', 'Layout', 'Legacy'),                     # Fully legacy
    ('Brand Container', '40006816:21702', '6', 'Brand / Logos', 'Legacy'),  # 4 legacy tokens
    ('Card (Product)', '40006816:21739', '20+', 'Data Display', 'Legacy'),  # Fully legacy
    ('Progress Bar', '40007190:39151', '4+', 'Data Display', 'Legacy'),     # AMIO/Primary (oldest)
]

slug_map = {
    'Button': 'button', 'Text Input': 'text-input', 'Select': 'select',
    'Accordion': 'accordion', 'Chip': 'chip', 'Badge': 'badge',
    'Link - Standalone': 'link', 'Checkbox': 'checkbox', 'Tabs': 'tabs',
    'Tooltip': 'tooltip', 'Action Menu': 'action-menu',
    'Counter Badge': 'counter-badge', 'Button Group': 'button-group',
    'Toggle': 'toggle', 'Progress Circle': 'progress-circle',
    'Avatar': 'avatar', 'Snackbar': 'snackbar',
    'Alert / inpage': 'alert-inpage', 'Action List': 'action-list',
    'Checkbox List': 'checkbox-list', 'Consumer NavBar': 'navbar',
    'Footer': 'footer', 'Profile Menu': 'profile-menu', 'Alert / top': 'alert-top',
    'Modal': 'modal', 'Bottom Sheet': 'bottom-sheet',
    'NavDrawer': 'navdrawer', 'Search': 'search',
    'ISI': 'isi', 'Brand Container': 'brand-container',
    'Card (Product)': 'card', 'Progress Bar': 'progress-bar',
}

for name, nid, variants, cat, system in tier1_info:
    sys_class = 'status-good' if 'New' in system else ('status-gap' if 'Mixed' in system else 'status-drift')
    slug = slug_map.get(name, '')
    link_open = f'<a href="components/{slug}.html" style="text-decoration:none;color:inherit">' if slug else ''
    link_close = '</a>' if slug else ''
    lines.append(f'''      {link_open}<div class="card" style="padding:16px 20px;cursor:pointer;transition:border-color 0.15s" onmouseover="this.style.borderColor='var(--brand)'" onmouseout="this.style.borderColor=''">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div>
            <strong style="font-size:14px">{name}</strong>
            <div style="font-size:11px;color:var(--text-support);margin-top:2px">{cat} · {variants} variants</div>
          </div>
          <span class="status-badge {sys_class}" style="margin-left:8px">{system}</span>
        </div>
        <div style="font-size:10px;font-family:var(--mono);color:var(--text-disabled);margin-top:4px">{nid}</div>
      </div>{link_close}''')

lines.append('    </div>\n  </div>')

# Token System Coverage
lines.append('''
  <div class="section">
    <h2 class="section-title">Token System Coverage</h2>
    <p class="section-desc">Which naming system each audited component uses. "New" = semantic system, "Mixed" = both old and new, "Old" = legacy only.</p>

    <div class="subsection">
      <h3 class="subsection-title">New Semantic System (9 components)</h3>
      <div class="component-grid">
        <div class="component-tag new"><strong>Button</strong><div class="system">New semantic</div></div>
        <div class="component-tag new"><strong>Text Input</strong><div class="system">New semantic</div></div>
        <div class="component-tag new"><strong>Accordion</strong><div class="system">New semantic</div></div>
        <div class="component-tag new"><strong>Select</strong><div class="system">New semantic</div></div>
        <div class="component-tag new"><strong>Badge</strong><div class="system">New semantic</div></div>
        <div class="component-tag new"><strong>Action List</strong><div class="system">New semantic</div></div>
        <div class="component-tag new"><strong>Link</strong><div class="system">New semantic</div></div>
        <div class="component-tag new"><strong>Checkbox</strong><div class="system">New semantic</div></div>
        <div class="component-tag new"><strong>Profile Menu</strong><div class="system">New semantic</div></div>
      </div>
    </div>

    <div class="subsection">
      <h3 class="subsection-title">Mixed Systems (8 components)</h3>
      <div class="component-grid">
        <div class="component-tag mixed"><strong>Tabs</strong><div class="system">Mixed old+new</div></div>
        <div class="component-tag mixed"><strong>Chip</strong><div class="system">Mixed old+new</div></div>
        <div class="component-tag mixed"><strong>Modal</strong><div class="system">Mixed old+new</div></div>
        <div class="component-tag mixed"><strong>Navigation</strong><div class="system">Mixed (Text & Icons)</div></div>
        <div class="component-tag mixed"><strong>Cards</strong><div class="system">Mixed (Text & Icons)</div></div>
        <div class="component-tag mixed"><strong>Training Center</strong><div class="system">Mixed (Text & Icons)</div></div>
        <div class="component-tag mixed"><strong>Progress Bar</strong><div class="system">Mixed (AMIO naming)</div></div>
        <div class="component-tag mixed"><strong>Brand Containers</strong><div class="system">Mixed (Color/Black)</div></div>
      </div>
    </div>

    <div class="subsection">
      <h3 class="subsection-title">Legacy Only (4 components)</h3>
      <div class="component-grid">
        <div class="component-tag old"><strong>Side Nav</strong><div class="system">Old (Color/White, Text & Icons)</div></div>
        <div class="component-tag old"><strong>Footer</strong><div class="system">Old (/Primary, Roboto)</div></div>
        <div class="component-tag old"><strong>Tabs Selectors</strong><div class="system">Old (Tertiary, Roboto)</div></div>
        <div class="component-tag old"><strong>Live Events</strong><div class="system">Old (YELLOW)</div></div>
      </div>
    </div>
  </div>
''')

# Master Inventory Table
lines.append('''
  <div class="section">
    <h2 class="section-title">Master Inventory Table</h2>
    <p class="section-desc">Complete list of all 774 elements from the Internal Only Canvas, grouped by category.</p>

    <table class="data-table">
      <thead>
        <tr><th>Name</th><th>Type</th><th>Variants</th><th>Node ID</th><th>Tier</th></tr>
      </thead>
      <tbody>
''')

for cat in cat_order:
    items = data['categories'].get(cat, [])
    if not items:
        continue

    # For Icons and Brand/Logos, deduplicate by base name
    if cat in ('Icons', 'Brand / Logos'):
        seen = {}
        for item in items:
            base = item['name'].split('/')[0].strip().lstrip('_').lstrip('.')
            if base not in seen or item['variants'] > seen[base]['variants']:
                seen[base] = item
        display_items = sorted(seen.values(), key=lambda x: x['name'])
    else:
        display_items = sorted(items, key=lambda x: (-x['variants'], x['name']))

    lines.append(f'        <tr class="cat-header"><td colspan="5">{cat} ({len(items)} elements{", " + str(len(display_items)) + " unique shown" if len(display_items) < len(items) else ""})</td></tr>')

    for item in display_items:
        tier = get_tier(item)
        tier_class = f'tier-{tier}'
        v_display = str(item['variants']) if item['variants'] > 0 else '—'
        lines.append(f'        <tr><td><strong>{item["name"]}</strong></td><td>{item["type"]}</td><td>{v_display}</td><td><span class="token-name">{item["id"]}</span></td><td><span class="tier-badge {tier_class}">T{tier}</span></td></tr>')

lines.append('''      </tbody>
    </table>
  </div>
</div>

<footer class="site-footer">
  AMI Design System Audit — Generated February 27, 2026 — <a href="https://github.com/d999ss/AMI-Design-System">GitHub</a>
</footer>

</body>
</html>
''')

html = '\n'.join(lines)
with open('/Users/donnysmith/Projects/cloud/AMI-Design-System/components.html', 'w') as f:
    f.write(html)

print(f"Generated components.html ({len(html)} bytes)")
