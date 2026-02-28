#!/usr/bin/env python3
"""Generate screen detail pages with component usage maps for BTS engineering handoff."""
import os

OUT_DIR = '/Users/donnysmith/Projects/cloud/AMI-Design-System/screens'
os.makedirs(OUT_DIR, exist_ok=True)

# Screen definitions with component usage maps
screens = [
    {
        'name': 'Home Dashboard',
        'slug': 'home-dashboard',
        'area': 'Home',
        'sections': [
            {'name': 'Home Dashboard - Returning Customer', 'node_id': '40016207:100920'},
            {'name': 'Home Dashboard - New Authenticated', 'node_id': '40019943:61950'},
            {'name': 'Home Dashboard - No Ship-to', 'node_id': '40019943:68971'},
        ],
        'description': 'Primary landing page after authentication. Three variants based on user state: returning customer (with in-progress courses and events), newly authenticated (onboarding prompts), and no ship-to address (setup flow). Contains hero section, course progress cards, upcoming events, and promotional content.',
        'breakpoints': ['XLarge (1440px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation with logo, links, search, profile'),
            ('Card (Product)', 'card', 'Course progress cards, event cards, content cards'),
            ('Progress Bar', 'progress-bar', 'Course completion indicator on cards'),
            ('Progress Circle', 'progress-circle', 'Circular completion badge on course cards'),
            ('Button', 'button', 'CTA buttons (Brand, Neutral, Ghost)'),
            ('Badge', 'badge', 'Status badges on cards (Required, Recommended, New)'),
            ('Brand Container', 'brand-container', 'Product-specific brand sections'),
            ('ISI', 'isi', 'Important Safety Information footer section'),
            ('Footer', 'footer', 'Page footer with legal links'),
        ],
        'layout': 'Full-width hero + 12-column grid content area. Navigation bar spans full viewport width. Content sections use max-width container with responsive margins.',
        'key_interactions': ['Card hover states', 'NavBar search activation', 'Profile menu dropdown', 'ISI expand/collapse'],
    },
    {
        'name': 'Course Catalog',
        'slug': 'course-catalog',
        'area': 'Courses',
        'sections': [
            {'name': 'Course Catalog – In Progress', 'node_id': '40016866:158864'},
            {'name': 'Course Catalog – Filter', 'node_id': '40016866:158866'},
            {'name': 'Course Catalog – Required', 'node_id': '40016866:158871'},
        ],
        'description': 'Browseable catalog of available training courses. Features tabbed navigation (In Progress, Required, Recommended, All), filterable card grid, and search functionality. Course cards show progress, brand association, and completion status.',
        'breakpoints': ['XLarge (1440px)', 'Large (1280px)', 'Medium (768px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation'),
            ('Tabs', 'tabs', 'Category tabs (In Progress, Required, Recommended, All)'),
            ('Card (Product)', 'card', 'Course cards with image, title, progress, brand'),
            ('Chip', 'chip', 'Filter chips (Brand, Type, Status)'),
            ('Search', 'search', 'Course search/filter input'),
            ('Progress Bar', 'progress-bar', 'Course completion on cards'),
            ('Progress Circle', 'progress-circle', 'Circular progress indicator'),
            ('Badge', 'badge', 'Status badges (Required, New, Complete)'),
            ('Button', 'button', 'Load more, filter actions'),
            ('ISI', 'isi', 'Safety information'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'Sidebar filter panel (280px) + main content area. Filter panel collapses to bottom sheet on mobile. Cards in 3-column grid (XL), 2-column (M), 1-column (S).',
        'key_interactions': ['Tab switching', 'Filter chip selection/deselection', 'Search input', 'Card hover', 'Filter panel open/close (mobile)'],
    },
    {
        'name': 'Live Events',
        'slug': 'live-events',
        'area': 'Events',
        'sections': [
            {'name': 'Live Events – Overview', 'node_id': '40016953:109879'},
            {'name': 'Live Events – My Events', 'node_id': '40016953:107246'},
        ],
        'description': 'Live event browsing and management. Two main views: Overview (all available events) and My Events (registered/attended). Features event cards with date, location, brand association, and registration status.',
        'breakpoints': ['XLarge (1440px)', 'Large (1280px)', 'Medium (768px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation'),
            ('Tabs', 'tabs', 'View tabs (Overview, My Events)'),
            ('Card (Product)', 'card', 'Event cards with date, location, brand'),
            ('Badge', 'badge', 'Event status (Upcoming, Registered, Attended)'),
            ('Button', 'button', 'Register, View Details'),
            ('Chip', 'chip', 'Event type filters'),
            ('ISI', 'isi', 'Safety information'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'Full-width content with card grid. Events organized by date sections. 3-column grid (XL), 2-column (M), 1-column (S).',
        'key_interactions': ['Tab switching', 'Event card hover', 'Register button', 'Filter by brand/type'],
    },
    {
        'name': 'Event Detail',
        'slug': 'event-detail',
        'area': 'Events',
        'sections': [
            {'name': 'Event Detail – Option 1', 'node_id': '40017458:61815'},
            {'name': 'Event Detail – Option 2', 'node_id': '40017458:74556'},
            {'name': 'Event Detail – Option 3', 'node_id': '40017458:76226'},
            {'name': 'Event Detail – Mobile', 'node_id': '40017458:77831'},
        ],
        'description': 'Detailed view of a single live event. Three layout options explored in design. Shows event image/hero, description, speaker info, agenda, registration CTA, and related events. Multiple design approaches with varying hero treatments and content layouts.',
        'breakpoints': ['XLarge (1440px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation'),
            ('Button', 'button', 'Register CTA (Brand primary)'),
            ('Badge', 'badge', 'Event type/status badge'),
            ('Brand Container', 'brand-container', 'Brand-specific hero section'),
            ('Card (Product)', 'card', 'Related events cards'),
            ('Accordion', 'accordion', 'Event agenda/FAQ expandable sections'),
            ('Avatar', 'avatar', 'Speaker avatars'),
            ('ISI', 'isi', 'Safety information'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'Full-width hero image + 2-column content (main content + sidebar info panel). Sidebar becomes stacked on mobile.',
        'key_interactions': ['Register button', 'Accordion expand/collapse', 'Share event', 'Related event navigation'],
    },
    {
        'name': 'Profile',
        'slug': 'profile',
        'area': 'Account',
        'sections': [
            {'name': 'Profile', 'node_id': '40017167:10224'},
        ],
        'description': 'User profile management page. Allows viewing and editing personal information, contact details, practice information, and account settings. Uses form controls extensively.',
        'breakpoints': ['XLarge (1440px)', 'Medium (768px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation'),
            ('NavDrawer (Side Nav)', 'navdrawer', 'Settings navigation sidebar'),
            ('Text Input', 'text-input', 'Name, email, phone fields'),
            ('Select', 'select', 'State, specialty, role dropdowns'),
            ('Checkbox', 'checkbox', 'Preferences/consent checkboxes'),
            ('Toggle', 'toggle', 'Notification preferences'),
            ('Button', 'button', 'Save, Cancel, Edit actions'),
            ('Avatar', 'avatar', 'Profile photo'),
            ('Profile Menu', 'profile-menu', 'User dropdown from NavBar'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'Sidebar navigation (280px) + main content area with form sections. Sidebar collapses to bottom drawer on mobile. Form fields in 2-column layout (XL/L), 1-column (M/S).',
        'key_interactions': ['Edit/save toggle', 'Form validation', 'Avatar upload', 'Side nav navigation', 'Toggle switches'],
    },
    {
        'name': 'FAQs',
        'slug': 'faqs',
        'area': 'Support',
        'sections': [
            {'name': 'FAQs', 'node_id': '40019212:160223'},
            {'name': 'FAQs – Category', 'node_id': '40019212:170019'},
            {'name': 'FAQs – Search', 'node_id': '40019212:170953'},
        ],
        'description': 'Frequently asked questions organized by category. Features searchable accordion-based Q&A sections. Categories include Account, Ordering, Products, Events, and Technical Support.',
        'breakpoints': ['XLarge (1440px)', 'Medium (768px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation'),
            ('Accordion', 'accordion', 'FAQ items (question/answer expand)'),
            ('Search', 'search', 'FAQ search input'),
            ('Tabs', 'tabs', 'Category tabs'),
            ('Chip', 'chip', 'Category filters'),
            ('Link', 'link', 'Contact support, related article links'),
            ('Button', 'button', 'Back to top, contact support'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'Full-width content with max-width container. Accordion items stacked vertically with category group headers.',
        'key_interactions': ['Accordion expand/collapse', 'Search filtering', 'Category tab switching', 'Scroll to section'],
    },
    {
        'name': 'Contact Us',
        'slug': 'contact-us',
        'area': 'Support',
        'sections': [
            {'name': 'Contact Us', 'node_id': '40020186:88705'},
            {'name': 'Contact Us – Form', 'node_id': '40020186:88371'},
            {'name': 'Contact Us – Success', 'node_id': '40020186:88372'},
            {'name': 'Contact Us – Mobile', 'node_id': '40020186:88364'},
        ],
        'description': 'Contact form for customer support inquiries. Multi-step form with subject selection, message composition, and success confirmation. Responsive layout with form validation.',
        'breakpoints': ['XLarge (1440px)', 'Medium (768px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation'),
            ('Text Input', 'text-input', 'Name, email, subject, message fields'),
            ('Select', 'select', 'Inquiry type dropdown'),
            ('Button', 'button', 'Submit (Brand primary), Cancel'),
            ('Snackbar', 'snackbar', 'Success confirmation toast'),
            ('Link', 'link', 'Phone, email contact links'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'Centered form layout (max-width 640px). Success state with checkmark illustration.',
        'key_interactions': ['Form validation', 'Subject selection', 'Submit with loading state', 'Success confirmation'],
    },
    {
        'name': 'Messages',
        'slug': 'messages',
        'area': 'Account',
        'sections': [
            {'name': 'Messages', 'node_id': '40019886:63393'},
            {'name': 'Messages – Detail', 'node_id': '40020303:152716'},
            {'name': 'Messages – Empty', 'node_id': '40019886:62481'},
        ],
        'description': 'In-app messaging center for notifications, announcements, and account communications. List view with unread indicators and detail view for individual messages.',
        'breakpoints': ['XLarge (1440px)', 'Medium (768px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation'),
            ('Badge', 'badge', 'Unread message count'),
            ('Counter Badge', 'counter-badge', 'NavBar notification count'),
            ('Card (Product)', 'card', 'Message preview cards'),
            ('Button', 'button', 'Mark as read, Archive'),
            ('Link', 'link', 'View all, message links'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'List view with message cards. Detail view uses centered content layout. Empty state with illustration.',
        'key_interactions': ['Message selection', 'Mark as read', 'Archive message', 'Empty state display'],
    },
    {
        'name': 'About You',
        'slug': 'about-you',
        'area': 'Onboarding',
        'sections': [
            {'name': 'About You', 'node_id': '40020493:69472'},
            {'name': 'About You – Step 2', 'node_id': '40020493:69254'},
            {'name': 'About You – Step 3', 'node_id': '40020493:69255'},
            {'name': 'About You – Mobile', 'node_id': '40020493:69247'},
        ],
        'description': 'Onboarding flow for new users to provide practice information, specialty, and preferences. Multi-step wizard with progress indication. Collects data needed for personalized content recommendations.',
        'breakpoints': ['XLarge (1440px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation'),
            ('Text Input', 'text-input', 'Practice name, NPI, address fields'),
            ('Select', 'select', 'Specialty, state, role dropdowns'),
            ('Checkbox', 'checkbox', 'Product interest checkboxes'),
            ('Chip', 'chip', 'Selectable interest tags'),
            ('Button', 'button', 'Next, Back, Skip, Submit'),
            ('Progress Bar', 'progress-bar', 'Step progress indicator'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'Centered wizard layout (max-width 720px) with step indicator. Side illustration on desktop. Stacked on mobile.',
        'key_interactions': ['Step navigation (next/back)', 'Form validation per step', 'Chip selection for interests', 'Skip optional steps'],
    },
    {
        'name': 'Search Results',
        'slug': 'search-results',
        'area': 'Global',
        'sections': [
            {'name': 'Search Results', 'node_id': '40019996:80971'},
        ],
        'description': 'Global search results page. Displays filtered results across courses, events, and content. Supports type filtering and relevance sorting.',
        'breakpoints': ['XLarge (1440px)', 'Medium (768px)', 'Small (375px)'],
        'components': [
            ('Consumer NavBar', 'navbar', 'Top navigation (search active state)'),
            ('Search', 'search', 'Search input with active query'),
            ('Tabs', 'tabs', 'Result type tabs (All, Courses, Events, Content)'),
            ('Card (Product)', 'card', 'Search result cards'),
            ('Badge', 'badge', 'Result type badges'),
            ('Chip', 'chip', 'Active filter chips'),
            ('Button', 'button', 'Load more results'),
            ('Footer', 'footer', 'Page footer'),
        ],
        'layout': 'Full-width with results in list/card grid. Filter bar at top. Results paginated with load more button.',
        'key_interactions': ['Search refinement', 'Type tab filtering', 'Filter chip removal', 'Result card navigation'],
    },
]


def build_screen_page(screen):
    # Section list
    section_items = ''
    for s in screen['sections']:
        section_items += f'          <tr><td>{s["name"]}</td><td><code>{s["node_id"]}</code></td></tr>\n'

    # Component usage table
    comp_rows = ''
    for name, slug, usage in screen['components']:
        comp_rows += f'          <tr><td><a href="../components/{slug}.html" style="color:var(--brand)">{name}</a></td><td>{usage}</td></tr>\n'

    # Breakpoints
    bp_items = ''.join(f'<span class="status-badge" style="margin-right:8px;background:var(--bg-page);color:var(--text-default)">{bp}</span>' for bp in screen['breakpoints'])

    # Key interactions
    int_items = ''.join(f'<li>{i}</li>' for i in screen.get('key_interactions', []))

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{screen['name']} — AMI Design System Audit</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>

<nav class="site-nav">
  <div class="nav-inner">
    <a href="../index.html" class="nav-brand">AMI Design System</a>
    <div class="nav-links">
      <a href="../index.html">Overview</a>
      <a href="../tokens.html">Tokens</a>
      <a href="../components.html">Components</a>
      <a href="../screens.html" class="active">Screens</a>
      <a href="../assets.html">Assets</a>
      <a href="../architecture.html">Architecture</a>
      <a href="../patterns.html">Patterns</a>
      <a href="../remediation.html">Remediation</a>
    </div>
  </div>
</nav>

<div class="container" style="max-width:960px">
  <div style="margin-bottom:8px">
    <a href="../screens.html" style="color:var(--brand);text-decoration:none;font-size:13px">&larr; All Screens</a>
  </div>

  <div class="section-header" style="flex-wrap:wrap;gap:8px">
    <h1 style="margin:0">{screen['name']}</h1>
    <span class="status-badge status-new">{screen['area']}</span>
  </div>
  <p style="color:var(--text-secondary);margin-top:4px;font-size:13px">
    Functional Area: {screen['area']} &middot; Variants: {len(screen['sections'])} sections &middot; Breakpoints: {len(screen['breakpoints'])}
  </p>

  <div class="card" style="padding:20px;margin:16px 0">
    <p style="margin:0;line-height:1.6">{screen['description']}</p>
  </div>

  <div class="section">
    <div class="subsection">
      <h3 class="subsection-title">Figma Sections</h3>
      <table class="data-table">
        <thead><tr><th>Section Name</th><th>Figma Node ID</th></tr></thead>
        <tbody>
{section_items}        </tbody>
      </table>
    </div>

    <div class="subsection">
      <h3 class="subsection-title">Responsive Breakpoints</h3>
      <div style="display:flex;flex-wrap:wrap;gap:8px">{bp_items}</div>
    </div>

    <div class="subsection">
      <h3 class="subsection-title">Component Usage Map <span class="status-badge status-good" style="font-size:10px">Cross-referenced</span></h3>
      <p style="color:var(--text-secondary);font-size:13px;margin-bottom:12px">Components used on this screen, linked to their detail documentation pages.</p>
      <table class="data-table">
        <thead><tr><th>Component</th><th>Usage on This Screen</th></tr></thead>
        <tbody>
{comp_rows}        </tbody>
      </table>
    </div>

    <div class="subsection">
      <h3 class="subsection-title">Layout Pattern</h3>
      <div class="card" style="padding:16px 24px">
        <p style="margin:0;line-height:1.8">{screen['layout']}</p>
      </div>
    </div>

    <div class="subsection">
      <h3 class="subsection-title">Key Interactions</h3>
      <div class="card" style="padding:16px 24px">
        <ul style="margin:0;padding-left:20px;line-height:2">{int_items}</ul>
      </div>
    </div>

    <div class="subsection" style="margin-top:24px">
      <h3 class="subsection-title">Engineering Notes</h3>
      <div class="card" style="padding:16px 24px">
        <ul style="margin:0;padding-left:20px;line-height:2">
          <li>Functional area: <strong>{screen['area']}</strong></li>
          <li>Total components used: <strong>{len(screen['components'])}</strong></li>
          <li>Figma sections: <strong>{len(screen['sections'])}</strong></li>
          <li>Responsive breakpoints: {', '.join(screen['breakpoints'])}</li>
          <li>Primary Figma node: <code>{screen['sections'][0]['node_id']}</code></li>
        </ul>
      </div>
    </div>
  </div>
</div>

<footer class="site-footer">
  AMI Design System Audit &mdash; Generated February 2026 &mdash; <a href="https://github.com/d999ss/AMI-Design-System">GitHub</a>
</footer>

</body>
</html>'''


# Generate all screen pages
for screen in screens:
    html = build_screen_page(screen)
    path = os.path.join(OUT_DIR, f'{screen["slug"]}.html')
    with open(path, 'w') as f:
        f.write(html)
    print(f'  {screen["slug"]}.html ({len(html):,} bytes) — {screen["area"]} ({len(screen["components"])} components)')

print(f'\nGenerated {len(screens)} screen detail pages')
