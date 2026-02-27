#!/usr/bin/env python3
"""Parse Figma metadata to generate component inventory."""
import json, sys, re

# Read the metadata file
with open(sys.argv[1]) as f:
    data = json.load(f)

text = data[0]['text']
lines = text.split('\n')

# Extract top-level elements
components = []
for line in lines:
    stripped = line.lstrip()
    indent = len(line) - len(stripped)
    if indent == 2:
        if stripped.startswith('<frame') or stripped.startswith('<symbol'):
            name_match = re.search(r'name="([^"]+)"', stripped)
            id_match = re.search(r'id="([^"]+)"', stripped)
            type_match = re.search(r'^<(\w+)', stripped)
            if name_match and id_match:
                components.append({
                    'name': name_match.group(1),
                    'id': id_match.group(1),
                    'type': type_match.group(1),
                    'self_closing': stripped.rstrip().endswith('/>')
                })

# Count child symbols for frames
frame_children = {}
current_frame = None
count = 0

for line in lines:
    stripped = line.lstrip()
    indent = len(line) - len(stripped)

    if indent == 2:
        if current_frame:
            frame_children[current_frame] = count
        if stripped.startswith('<frame') and not stripped.rstrip().endswith('/>'):
            id_m = re.search(r'id="([^"]+)"', stripped)
            current_frame = id_m.group(1) if id_m else None
            count = 0
        else:
            current_frame = None
            count = 0
    elif indent == 4 and current_frame:
        if stripped.startswith('<symbol') or stripped.startswith('<instance') or stripped.startswith('<frame'):
            count += 1

if current_frame:
    frame_children[current_frame] = count

# Categorize
def categorize(name):
    n = name.lower()

    # Icons first (most specific)
    icon_kw = ['.↪️ icon', 'icon/', 'icon ', 'direction/', 'system/', 'action/', 'objects/', 'maps/',
               'preference/', 'education/', 'like/', 'calendar/', 'syringe/', 'clock/', 'team/',
               'location/', 'check /', 'remix-icons', 'arrow', 'caret', 'pencil', 'download',
               'confetti', 'mappin', 'warningcircle', 'plus']
    for kw in icon_kw:
        if kw in n:
            return 'Icons'

    # Brand/Logos
    brand_kw = ['logo', 'brand', 'product logo', 'alle ', '_primary options', '_secondary options',
                '_seal options', '_logo options', '_logotype options', '_emblem options', '_monogram options',
                '_brand options', '_indication options', '_default options', 'latisse']
    for kw in brand_kw:
        if kw in n:
            return 'Brand / Logos'

    # Navigation
    nav_kw = ['nav', 'tab', 'link', 'menu', 'breadcrumb', 'pagination', 'header button', 'footer',
              'sidebar', 'drawer', 'top bar', 'bottom sheet']
    for kw in nav_kw:
        if kw in n:
            return 'Navigation'

    # Feedback
    fb_kw = ['alert', 'tooltip', 'snackbar', 'modal', 'dialog', 'toast', 'banner', 'annotation']
    for kw in fb_kw:
        if kw in n:
            return 'Feedback'

    # Form Controls
    form_kw = ['button', 'input', 'select', 'checkbox', 'toggle', 'chip', 'accordion', 'dropdown',
               'radio', 'counter badge', 'counter filter', 'search', 'filter', 'validate',
               'text input', 'text button', 'header button', 'button group', 'cta']
    for kw in form_kw:
        if kw in n:
            return 'Form Controls'

    # Data Display
    dd_kw = ['card', 'badge', 'tag', 'avatar', 'progress', 'medal', 'stamp', 'status',
             'indicator', 'count', 'title']
    for kw in dd_kw:
        if kw in n:
            return 'Data Display'

    # Media
    med_kw = ['image', 'video', 'placeholder', 'carousel']
    for kw in med_kw:
        if kw in n:
            return 'Media'

    # Layout
    lay_kw = ['container', 'spacer', 'slot', 'view port', 'section', 'responsive', 'grid',
              'xlarge', 'small', 'medium', 'large', 'marketing', 'isi', 'training center',
              'training portal', 'live events']
    for kw in lay_kw:
        if kw in n:
            return 'Layout'

    return 'Other'

# Build categorized output
cats = {}
for c in components:
    cat = categorize(c['name'])
    if cat not in cats:
        cats[cat] = []
    variants = frame_children.get(c['id'], 0)
    c['variants'] = variants
    cats[cat].append(c)

# Print summary
print("COMPONENT INVENTORY SUMMARY")
print("=" * 60)
total = 0
for cat in ['Form Controls', 'Navigation', 'Data Display', 'Feedback', 'Layout', 'Media', 'Icons', 'Brand / Logos', 'Other']:
    items = cats.get(cat, [])
    total += len(items)
    print(f"  {cat}: {len(items)}")
print(f"  TOTAL: {total}")

# Print key components (non-icon, non-brand, non-layout)
print("\n\nKEY COMPONENTS (Form Controls + Navigation + Data Display + Feedback)")
print("=" * 60)
for cat in ['Form Controls', 'Navigation', 'Data Display', 'Feedback']:
    items = cats.get(cat, [])
    print(f"\n--- {cat} ({len(items)}) ---")
    for c in items:
        v = f" [{c['variants']}v]" if c['variants'] > 0 else ""
        print(f"  {c['id']:>20}  {c['name']}{v}")

# Output JSON for HTML generation
output = {
    'categories': {},
    'totals': {}
}
for cat, items in cats.items():
    output['categories'][cat] = [{'name': c['name'], 'id': c['id'], 'type': c['type'], 'variants': c['variants']} for c in items]
    output['totals'][cat] = len(items)

with open('/tmp/ami_inventory.json', 'w') as f:
    json.dump(output, f, indent=2)
print("\n\nJSON saved to /tmp/ami_inventory.json")
