#!/usr/bin/env python3
"""Generate individual component detail pages for Tier 1 components using real Figma token data."""
import json
import os

with open('/Users/donnysmith/Projects/cloud/AMI-Design-System/token_data.json') as f:
    token_data = json.load(f)

# Component definitions with real Figma data
components = [
    {
        'name': 'Button',
        'slug': 'button',
        'node_id': '40006598:72259',
        'variants': '308+',
        'category': 'Form Controls',
        'token_system': 'New semantic + legacy coexist',
        'token_class': 'status-gap',
        'description': 'Primary interactive element for triggering actions. The most variant-rich component in the system with 308+ configurations. Uses 3 sizes, 4+ color schemes (Neutral, Brand, Mute, Destructive), 5 states, solid/ghost/outline styles. Both new semantic and legacy color/surface tokens coexist on this component.',
        'anatomy': ['Container (auto-layout)', 'Label text (Graphik)', 'Leading icon (optional)', 'Trailing icon (optional)', 'Loading spinner (optional)'],
        'states': ['Enable', 'Hover', 'Pressed', 'Disabled', 'Loading'],
        'figma_variants': [
            ('Size', 'Small (48px), Medium, Large'),
            ('Color', 'Action (Neutral), Brand, Mute, Destructive (Error)'),
            ('Solid', 'Yes (filled) / No (ghost)'),
            ('Outline', 'Yes (bordered) / No'),
            ('isDisabled', 'Yes / No'),
            ('isLoading', 'Yes / No'),
            ('State', 'Enable / Hover / Pressed / Disabled / Loading'),
        ],
        'sizes': ['Small (height: 48px)', 'Medium', 'Large'],
        'real_tokens': [
            ('Container (Neutral)', 'Color/Container/Neutral/Interactive/Enable', '#090909'),
            ('Container (Neutral Hover)', 'Color/Container/Neutral/Interactive/Hover', '#787676'),
            ('Container (Brand)', 'Color/Container/Brand/Interactive/Enable', '#9a6b5e'),
            ('Container (Brand Hover)', 'Color/Container/Brand/Interactive/Hover', '#7d574d'),
            ('Container (Mute)', 'Color/Container/Neutral/Interactive/Mute enable', '#f7f6f5'),
            ('Container (Destructive)', 'Color/Container/Status/Interactive/Enable negative', '#de3b2d'),
            ('Container (Disabled)', 'Color/Container/Neutral/Disabled/Default', '#ece9e5'),
            ('Text (Inverted)', 'Text/Neutral/Inverted', '#ffffff'),
            ('Text (Default)', 'Text/Neutral/Default', '#090909'),
            ('Text (Brand)', 'Color/Text/Brand/Default', '#9a6b5e'),
            ('Text (Disabled)', 'Text/Neutral/Disabled/Default', '#b3b0ae'),
            ('Border (Neutral)', 'Color/Border/Neutral/Default', '#090909'),
            ('Border (Brand)', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Focus Ring', 'Color/Border/Brand/Focus ring/Default', '#c08676'),
            ('Corner Radius', 'Corner/Small', '8px'),
            ('Font', 'font family/graphik', 'Graphik'),
            ('Font Size (S)', 'font size/04', '14px'),
            ('Font Size (M)', 'font size/05', '16px'),
            ('Font Size (L)', 'font size/06', '18px'),
        ],
        'legacy_note': 'IMPORTANT: Button also contains legacy <code>color/surface/interactive/</code> tokens that map to the same values. These should be removed during migration.',
    },
    {
        'name': 'Text Input',
        'slug': 'text-input',
        'node_id': '40006598:70760',
        'variants': '36',
        'category': 'Form Controls',
        'token_system': 'New semantic (PascalCase)',
        'token_class': 'status-good',
        'description': 'Standard text field for user input. Uses PascalCase token naming (Font/Font size/5, Space/8) — the target convention for the system. Includes label, placeholder, helper text, and error state configurations.',
        'anatomy': ['Container (Corner/Small: 8px)', 'Label (Body/Medium/Medium)', 'Input field (Stroke width/Extra light: 1px border)', 'Placeholder text (#787676)', 'Helper text (Body/Small/Regular)', 'Error message (dc3426)', 'Icon slots'],
        'states': ['Default', 'Hover (black border)', 'Focused (brand focus ring)', 'Filled', 'Error (red border + message)', 'Disabled (muted bg)'],
        'figma_variants': [
            ('State', 'Default / Hover / Focus / Error / Disabled'),
            ('Label', 'Yes / No'),
            ('Helper Text', 'Yes / No'),
            ('Leading Icon', 'Yes / No'),
            ('Trailing Icon', 'Yes / No'),
        ],
        'sizes': ['Medium (Body/Small)', 'Large (Body/Medium)'],
        'real_tokens': [
            ('Background', 'Color/Container/Neutral/Base', '#ffffff'),
            ('Background (Filled)', 'Color/Container/Neutral/Mute 1', '#fafafa'),
            ('Border (Default)', 'Color/Border/Neutral/Text field/Enable', '#b3b0ae'),
            ('Border (Hover)', 'Color/Border/Neutral/Text field/Hover', '#090909'),
            ('Border (Error)', 'Color/Border/Status/Error medium 3', '#dc3426'),
            ('Border (Disabled)', 'Color/Border/Neutral/Disabled/Default', '#b3b0ae'),
            ('Focus Ring', 'Color/Border/Brand/Focus ring/Default', '#c08676'),
            ('Label Text', 'Text/Neutral/Default', '#090909'),
            ('Placeholder', 'Text/Neutral/Placeholder', '#787676'),
            ('Helper Text', 'Text/Neutral/Support', '#787676'),
            ('Error Text', 'Text/Status/Error medium 3', '#dc3426'),
            ('Disabled Text', 'Text/Neutral/Disabled/Default', '#b3b0ae'),
            ('Corner Radius', 'Corner/Small', '8px'),
            ('Corner (Grouped)', 'Corner/Medium small', '12px'),
            ('Border Width', 'Stroke width/Extra light', '1px'),
            ('Focus Border', 'Stroke width/Bold', '4px'),
            ('Font', 'Font/Families/Graphik', 'Graphik'),
            ('Padding', 'Space/4, Space/8, Space/12, Space/16', '4-16px scale'),
        ],
        'legacy_note': 'Error color is #dc3426 here vs #de3b2d in Button/Select — inconsistency to resolve.',
    },
    {
        'name': 'Select',
        'slug': 'select',
        'node_id': '40006598:84030',
        'variants': '72',
        'category': 'Form Controls',
        'token_system': 'New semantic (lowercase)',
        'token_class': 'status-good',
        'description': 'Dropdown selection component using lowercase token naming (spacing/08, font size/05). Includes Elevation 2 shadow on the dropdown, Circle corners for avatars/pills. Shares Text field border tokens with Text Input.',
        'anatomy': ['Container (Corner/Small: 8px)', 'Label', 'Selected value', 'Caret icon (Corner/Circle for pill items)', 'Dropdown panel (Elevation 2)', 'Option list', 'Search field (optional)'],
        'states': ['Default', 'Hover (black border)', 'Open (Elevation 2 shadow)', 'Selected', 'Error', 'Disabled'],
        'figma_variants': [
            ('State', 'Default / Hover / Open / Error / Disabled'),
            ('Selection', 'Single / Multi'),
            ('Search', 'Yes / No'),
            ('Label', 'Yes / No'),
        ],
        'sizes': ['Medium', 'Large'],
        'real_tokens': [
            ('Background', 'Color/Container/Neutral/Base', '#ffffff'),
            ('Dropdown Bg', 'Color/Container/Neutral/Mute 1', '#fafafa'),
            ('Border (Default)', 'Color/Border/Neutral/Text field/Enable', '#b3b0ae'),
            ('Border (Hover)', 'Color/Border/Neutral/Text field/Hover', '#090909'),
            ('Border (Divider)', 'Color/Border/Neutral/Subtle 2', '#dedad7'),
            ('Border (Error)', 'Color/Border/Status/Error medium 3', '#de3b2d'),
            ('Selected Accent', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Text', 'Text/Neutral/Default', '#090909'),
            ('Placeholder', 'Text/Neutral/Placeholder', '#787676'),
            ('Support', 'Text/Neutral/Support', '#787676'),
            ('Error', 'Text/Status/Error medium 3', '#de3b2d'),
            ('Elevation', 'Elevation 2/Cast down', '4-layer shadow'),
            ('Corner', 'Corner/Small', '8px'),
            ('Pill Corner', 'Corner/Circle', '999px'),
            ('Font', 'font family/graphik', 'Graphik'),
        ],
        'legacy_note': 'Error color is #de3b2d here vs #dc3426 in Text Input — inconsistency in the same system.',
    },
    {
        'name': 'Accordion',
        'slug': 'accordion',
        'node_id': '40006598:90126',
        'variants': '15',
        'category': 'Form Controls',
        'token_system': 'New semantic (mixed case)',
        'token_class': 'status-gap',
        'description': 'Expandable/collapsible sections using BOTH naming conventions — lowercase (spacing/08) AND PascalCase (Font/Families/Petersburg). Notably uses Petersburg serif font for headlines, making it unique among form components.',
        'anatomy': ['Container', 'Header (auto-layout)', 'Title (Headline/Small/Secondary — Petersburg 24px)', 'Expand/collapse chevron', 'Content area (Body/Medium/Regular — Graphik 16px)', 'Divider (Subtle 2 border)'],
        'states': ['Collapsed', 'Expanded', 'Hover', 'Active'],
        'figma_variants': [
            ('State', 'Collapsed / Expanded'),
            ('Style', 'Default / Bordered'),
            ('Header Style', 'Primary (Graphik) / Secondary (Petersburg)'),
        ],
        'sizes': [],
        'real_tokens': [
            ('Background', 'Color/Container/Neutral/Base', '#ffffff'),
            ('Divider', 'Color/Border/Neutral/Subtle 2', '#dedad7'),
            ('Active Border', 'Color/Border/Brand/Medium 2', '#c08676'),
            ('Focus Ring', 'Color/Border/Brand/Focus ring/Default', '#c08676'),
            ('Icon (Default)', 'Color/Icon/Neutral/Interactive/Enable support', '#787676'),
            ('Icon (Active)', 'Color/Icon/Neutral/Interactive/Active support', '#090909'),
            ('Title (Default)', 'Text/Neutral/Interactive/Enable support', '#787676'),
            ('Title (Active)', 'Text/Neutral/Interactive/Active support', '#090909'),
            ('Headline Font', 'Font/Families/Petersburg', 'Petersburg (serif)'),
            ('Body Font', 'font family/graphik', 'Graphik (sans)'),
            ('Headline Size', 'Font/Font size/8', '24px'),
            ('Body Size', 'font size/05', '16px'),
            ('Spacing', 'spacing/04 through spacing/24', '4-24px scale'),
        ],
        'legacy_note': 'Mixes PascalCase (Font/Families/Petersburg, Font/Font size/8) and lowercase (font size/05, spacing/08) token naming.',
    },
    {
        'name': 'Badge',
        'slug': 'badge',
        'node_id': '40003841:33610',
        'variants': '30',
        'category': 'Data Display',
        'token_system': 'New semantic (lowercase)',
        'token_class': 'status-good',
        'description': 'Status indicator using complete semantic token system with all status colors mapped to consistent token paths. The most comprehensive status color usage in the system — 5 status variants with matching border, background, and text tokens.',
        'anatomy': ['Container (Corner/Small: 8px)', 'Label text (Footnote/Regular: Graphik 12px)', 'Leading dot/icon (optional)'],
        'states': ['Default'],
        'figma_variants': [
            ('Status', 'Neutral / Success / Warning / Error / Brand'),
            ('Style', 'Filled subtle / Outline'),
            ('Leading', 'None / Dot / Icon'),
        ],
        'sizes': ['Small', 'Medium'],
        'real_tokens': [
            ('Bg (Neutral)', 'Color/Container/Neutral/Mute 2', '#f7f6f5'),
            ('Bg (Success)', 'Color/Container/Status/Success subtle 1', '#d9eddd'),
            ('Bg (Error)', 'Color/Container/Status/Error subtle 1', '#fee1de'),
            ('Bg (Warning)', 'Color/Container/Status/Warning subtle 1', '#ffe5aa'),
            ('Bg (Brand)', 'Color/Container/Brand/Subtle 1', '#f1e5e2'),
            ('Border (Success)', 'Color/Border/Status/Positive medium 3', '#0b8923'),
            ('Border (Warning)', 'Color/Border/Status/Warning medium 3', '#ef8f00'),
            ('Border (Error)', 'Color/Border/Status/Error medium 3', '#de3b2d'),
            ('Border (Brand)', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Text (Neutral)', 'Text/Neutral/Default', '#090909'),
            ('Text (Success)', 'Text/Status/Success bold 1', '#065a18'),
            ('Text (Error)', 'Text/Status/Error medium 3', '#961307'),
            ('Text (Warning)', 'Text/Status/Warning bold 2', '#863300'),
            ('Text (Brand)', 'Color/Text/Brand/Bold 1', '#7d574d'),
            ('Corner', 'Corner/Small', '8px'),
            ('Font', 'font family/graphik', 'Graphik 12px'),
        ],
        'legacy_note': 'Badge error text uses #961307 vs #de3b2d (border) vs #dc3426 (Text Input) — three different "error reds".',
    },
    {
        'name': 'Link - Standalone',
        'slug': 'link',
        'node_id': '40008110:15068',
        'variants': '96',
        'category': 'Navigation',
        'token_system': 'New semantic (lowercase)',
        'token_class': 'status-good',
        'description': 'Standalone navigation link with comprehensive interactive state tokens. Has dedicated underline font variants (Body/Medium/Reg underline). Three complete color tracks: Brand, Neutral, and Inverted for dark backgrounds.',
        'anatomy': ['Link text (with underline variant)', 'Leading icon (optional)', 'Trailing icon (optional)'],
        'states': ['Enable', 'Hover', 'Pressed', 'Focused'],
        'figma_variants': [
            ('Color', 'Brand / Neutral / Inverted'),
            ('Size', 'Footnote (12px) / Body Small (14px) / Body Medium (16px)'),
            ('Weight', 'Regular / Medium'),
            ('Underline', 'Yes / No'),
            ('State', 'Enable / Hover / Pressed'),
            ('Icon', 'None / Leading / Trailing'),
        ],
        'sizes': ['Footnote (12px)', 'Body Small (14px)', 'Body Medium (16px)'],
        'real_tokens': [
            ('Text (Brand Enable)', 'Text/Brand/Interactive/Enable', '#9a6b5e'),
            ('Text (Brand Hover)', 'Text/Brand/Interactive/Hover', '#60433b'),
            ('Text (Brand Pressed)', 'Text/Brand/Interactive/Pressed', '#30211e'),
            ('Text (Neutral Enable)', 'Text/Neutral/Interactive/Enable', '#090909'),
            ('Text (Neutral Hover)', 'Text/Neutral/Interactive/Hover', '#787676'),
            ('Text (Inverted Enable)', 'Color/Text/Neutral/Interactive/Inverted enable', '#ffffff'),
            ('Text (Inverted Hover)', 'Color/Text/Neutral/Interactive/Inverted hover', '#ece9e5'),
            ('Focus Ring', 'Color/Border/Brand/Focus ring/Default', '#c08676'),
            ('Font', 'font family/graphik', 'Graphik'),
        ],
        'legacy_note': None,
    },
    {
        'name': 'Checkbox',
        'slug': 'checkbox',
        'node_id': '40006598:81360',
        'variants': '12',
        'category': 'Form Controls',
        'token_system': 'New semantic (PascalCase)',
        'token_class': 'status-good',
        'description': 'Binary selection control with minimal token bindings — only icon colors and focus ring. Uses PascalCase naming (Space/8). Error indicator uses #dc3426 matching Text Input.',
        'anatomy': ['Checkbox box', 'Checkmark icon (Color/Icon/Neutral/Black)', 'Label text', 'Description (optional)'],
        'states': ['Unchecked', 'Checked', 'Indeterminate', 'Hover', 'Focused', 'Disabled', 'Error'],
        'figma_variants': [
            ('Checked', 'Yes / No / Indeterminate'),
            ('State', 'Default / Hover / Focus / Disabled / Error'),
            ('Label', 'Yes / No'),
        ],
        'sizes': [],
        'real_tokens': [
            ('Checkmark', 'Color/Icon/Neutral/Black', '#090909'),
            ('Icon (alt)', 'Icon/Neutral/Black', '#090909'),
            ('Icon Default', 'Color/Icon/Neutral/Default', '#090909'),
            ('Icon Disabled', 'Color/Icon/Neutral/Disabled/Default', '#b3b0ae'),
            ('Icon Error', 'Color/Icon/Status/Error medium 3', '#dc3426'),
            ('Focus Ring', 'Color/Border/Brand/Focus ring/Default', '#c08676'),
            ('Spacing', 'Space/8', '8px'),
        ],
        'legacy_note': 'Uses same error red (#dc3426) as Text Input, different from Button/Select (#de3b2d).',
    },
    {
        'name': 'Tabs',
        'slug': 'tabs',
        'node_id': '40008120:29000',
        'variants': '32',
        'category': 'Navigation',
        'token_system': 'New semantic (lowercase)',
        'token_class': 'status-good',
        'description': 'Horizontal tab navigation with brand-colored active indicator. Uses semantic interactive tokens for text/icon states. Includes headline font size (20px) for larger tab variants.',
        'anatomy': ['Tab bar container (transparent bg)', 'Tab item (auto-layout)', 'Tab label (Body/Medium or Headline/Extra small)', 'Active indicator (Brand/Medium 3 underline)', 'Badge (optional)', 'Icon (optional)', 'Bottom divider (Subtle 2)'],
        'states': ['Enable (support color)', 'Active (default color)', 'Hover', 'Focused'],
        'figma_variants': [
            ('State', 'Default / Active / Hover'),
            ('Size', 'Small (16px) / Large (20px)'),
            ('Icon', 'None / Leading'),
            ('Badge', 'None / Count'),
        ],
        'sizes': ['Standard (font size 16px)', 'Large (font size 20px)'],
        'real_tokens': [
            ('Background', 'Color/Container/Transparent/Clear', 'transparent'),
            ('Divider', 'Color/Border/Neutral/Subtle 2', '#dedad7'),
            ('Active Indicator', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Icon (Default)', 'Color/Icon/Neutral/Interactive/Enable support', '#787676'),
            ('Icon (Active)', 'Color/Icon/Neutral/Interactive/Active support', '#090909'),
            ('Text (Default)', 'Text/Neutral/Interactive/Enable support', '#787676'),
            ('Text (Active)', 'Text/Neutral/Interactive/Active support', '#090909'),
            ('Font', 'font family/graphik', 'Graphik'),
            ('Font Size', 'font size/05 / font size/07', '16px / 20px'),
            ('Spacing', 'spacing/04 through spacing/24', '4-24px'),
        ],
        'legacy_note': 'Initially categorized as "Mixed" but actually uses full new semantic system.',
    },
    {
        'name': 'Tooltip',
        'slug': 'tooltip',
        'node_id': '40003841:33483',
        'variants': '4',
        'category': 'Feedback',
        'token_system': 'New semantic (lowercase)',
        'token_class': 'status-good',
        'description': 'Contextual popup with dark background (#272625 — not pure black) and Elevation 2 shadow. Uses smallest corner radius in the system (corner/extra_small: 4px).',
        'anatomy': ['Container (corner/extra_small: 4px)', 'Content text (Inverted: #ffffff)', 'Arrow/pointer', 'Trigger element'],
        'states': ['Hidden', 'Visible'],
        'figma_variants': [
            ('Position', 'Top / Bottom / Left / Right'),
        ],
        'sizes': [],
        'real_tokens': [
            ('Background', 'Color/Container/Neutral/Strong 1', '#272625'),
            ('Text', 'Text/Neutral/Inverted', '#ffffff'),
            ('Icon', 'Color/Icon/Neutral/Default', '#090909'),
            ('Trigger Border', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Shadow', 'Elevation 2/Cast down', '4-layer drop shadow'),
            ('Corner Radius', 'corner/extra_small', '4px'),
            ('Spacing', 'spacing/02, spacing/08', '2px, 8px'),
            ('Font', 'font family/graphik', 'Graphik 14px'),
        ],
        'legacy_note': None,
    },
    {
        'name': 'Chip',
        'slug': 'chip',
        'node_id': '40006598:71720',
        'variants': '10',
        'category': 'Form Controls',
        'token_system': 'New semantic (lowercase)',
        'token_class': 'status-good',
        'description': 'Compact interactive element using full semantic token system. Originally categorized as "Mixed" but Figma extraction reveals it uses the new Color/ token paths consistently. Pill shape via Corner/Circle: 999.',
        'anatomy': ['Container (pill shape: Corner/Circle 999)', 'Label text (Footnote: Graphik 12px)', 'Brand icon (optional)', 'Close/remove icon (optional)'],
        'states': ['Enable', 'Hover', 'Pressed', 'Disabled', 'Error'],
        'figma_variants': [
            ('Style', 'Brand / Neutral / Mute'),
            ('State', 'Enable / Hover / Pressed / Disabled / Error'),
            ('Close Icon', 'Yes / No'),
        ],
        'sizes': [],
        'real_tokens': [
            ('Text (Brand)', 'Text/Brand/Default', '#9a6b5e'),
            ('Text (Default)', 'Text/Neutral/Default', '#090909'),
            ('Text (Disabled)', 'Text/Neutral/Disabled/Default', '#b3b0ae'),
            ('Text (Error)', 'Text/Status/Error medium 3', '#de3b2d'),
            ('Icon (Brand)', 'Color/Icon/Brand/Default', '#9a6b5e'),
            ('Container (Brand)', 'Color/Container/Brand/Transparent interactive/Enable', 'transparent'),
            ('Container (Brand Hover)', 'Color/Container/Brand/Transparent interactive/Hover', '#c0867633'),
            ('Container (Mute)', 'Color/Container/Neutral/Transparent interactive/Mute enable', 'transparent'),
            ('Border (Brand)', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Border (Neutral)', 'Color/Border/Neutral/Black/Alpha 100', '#090909'),
            ('Border (Error)', 'Color/Border/Status/Error medium 3', '#de3b2d'),
            ('Corner', 'Corner/Circle', '999px (pill)'),
            ('Font', 'font family/graphik', 'Graphik 12px'),
        ],
        'legacy_note': 'Reclassified from "Mixed" to "New semantic" after Figma token extraction confirmed semantic paths.',
    },
    {
        'name': 'Toggle',
        'slug': 'toggle',
        'node_id': '40015525:22363',
        'variants': '2',
        'category': 'Form Controls',
        'token_system': 'No tokens',
        'token_class': 'status-drift',
        'description': 'Binary on/off switch with ZERO variable bindings in Figma. This component has no token connections whatsoever — all values are hardcoded. Requires full token binding before engineering handoff.',
        'anatomy': ['Track', 'Thumb', 'Label (optional)'],
        'states': ['Off', 'On', 'Hover', 'Focused', 'Disabled'],
        'figma_variants': [
            ('State', 'On / Off'),
        ],
        'sizes': [],
        'real_tokens': [],
        'legacy_note': 'CRITICAL: This component has zero Figma variable bindings. All colors, sizes, and spacing are hardcoded values. Must be fully tokenized before implementation.',
    },
    {
        'name': 'Snackbar',
        'slug': 'snackbar',
        'node_id': '40017359:55323',
        'variants': '3',
        'category': 'Feedback',
        'token_system': 'Legacy (/Primary + Roboto)',
        'token_class': 'status-drift',
        'description': 'Temporary notification bar using legacy /Primary color system and Roboto font — the only component still on Roboto in the core set. Requires full migration to semantic tokens and Graphik font.',
        'anatomy': ['Container (black)', 'Message text (Roboto 16px)', 'Action button (optional)', 'Close icon (optional)'],
        'states': ['Visible', 'Dismissing'],
        'figma_variants': [
            ('Style', 'Default / With Action / Error'),
        ],
        'sizes': [],
        'real_tokens': [
            ('Background', '/Primary / 000000', '#000000'),
            ('Font', 'Desktop/P2', 'Roboto 16px Regular'),
        ],
        'legacy_note': 'LEGACY SYSTEM: Uses /Primary color naming and Roboto font. Only 2 token bindings total. Must migrate to semantic tokens and Graphik font.',
    },
    {
        'name': 'Avatar',
        'slug': 'avatar',
        'node_id': '40019054:169935',
        'variants': '3',
        'category': 'Data Display',
        'token_system': 'New semantic (mixed)',
        'token_class': 'status-good',
        'description': 'User profile avatar with circle shape and brand border accent. Minimal but correct token bindings — uses size tokens and Corner/Circle for circular shape.',
        'anatomy': ['Container (circle: Corner/Circle 999)', 'Image/initials', 'Border (Brand/Medium 3 or Neutral/Medium 2)', 'Status indicator (optional)'],
        'states': ['With Image', 'With Initials', 'Fallback'],
        'figma_variants': [
            ('Content', 'Image / Initials / Icon'),
        ],
        'sizes': ['32px (size/32)'],
        'real_tokens': [
            ('Size', 'size/32', '32px'),
            ('Shape', 'Corner/Circle', '999px'),
            ('Background', 'Color/Container/Transparent/Clear', 'transparent'),
            ('Border (Neutral)', 'Color/Border/Neutral/Medium 2', '#9b9997'),
            ('Border (Brand)', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
        ],
        'legacy_note': None,
    },
    {
        'name': 'Alert - Inpage',
        'slug': 'alert-inpage',
        'node_id': '40007190:39217',
        'variants': '3',
        'category': 'Feedback',
        'token_system': 'Legacy (Text & Icons + Color/Utility)',
        'token_class': 'status-drift',
        'description': 'Inline alert banner using legacy "Text & Icons" color system, hardcoded Color/Utility colors (#ff0000 for red, #74cc4f for green, #ffc32a for yellow), and a THIRD spacing naming convention (Spacing/8 vs spacing/08 vs Space/8).',
        'anatomy': ['Container', 'Icon', 'Title (optional)', 'Message text (Graphik 16px)', 'Close button (optional)', 'Action link (optional)'],
        'states': ['Default', 'Dismissible'],
        'figma_variants': [
            ('Status', 'Info / Warning / Error / Success'),
        ],
        'sizes': [],
        'real_tokens': [
            ('Text', 'Text & Icons/Default', '#090909'),
            ('Background (Base)', 'Color/White/100', '#ffffff'),
            ('Warning Color', 'Color/Utility/Yellow', '#ffc32a'),
            ('Error Color', 'Color/Utility/Red', '#ff0000'),
            ('Success Color', 'Color/Utility/Green', '#74cc4f'),
            ('Spacing', 'Spacing/8', '8px'),
            ('Spacing (Large)', 'Spacing/16', '16px'),
        ],
        'legacy_note': 'LEGACY SYSTEM: Uses "Text & Icons" naming, Color/Utility colors (raw hex like #ff0000), and a third spacing convention (Spacing/8). Three separate systems to migrate.',
    },
    {
        'name': 'Action Menu',
        'slug': 'action-menu',
        'node_id': '40006598:82298',
        'variants': '6',
        'category': 'Navigation',
        'token_system': 'New semantic (PascalCase)',
        'token_class': 'status-good',
        'description': 'Contextual menu with minimal but correct token bindings. Uses Elevation 2 shadow for the floating panel and brand border accent.',
        'anatomy': ['Trigger button', 'Menu container (Elevation 2)', 'Menu item', 'Divider', 'Icon (optional)'],
        'states': ['Closed', 'Open'],
        'figma_variants': [
            ('State', 'Closed / Open'),
            ('Items', '3 / 4 / 5+'),
        ],
        'sizes': [],
        'real_tokens': [
            ('Background', 'Color/Container/Neutral/Base', '#ffffff'),
            ('Brand Accent', 'Color/Border/Brand/Medium 3', '#9a6b5e'),
            ('Shadow', 'Elevation 2/Cast down', '4-layer drop shadow'),
            ('Corner', 'Corner/Extra small', '4px'),
            ('Spacing', 'Space/8', '8px'),
        ],
        'legacy_note': None,
    },
    {
        'name': 'Counter Badge',
        'slug': 'counter-badge',
        'node_id': '40006598:71412',
        'variants': '2',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Numeric indicator showing count values on navigation elements and notification icons.',
        'anatomy': ['Container (circle)', 'Count text'],
        'states': ['Default', 'Overflow (99+)'],
        'figma_variants': [('Style', 'Number / Dot')],
        'sizes': ['Small (16px)', 'Medium (20px)'],
        'real_tokens': [],
        'legacy_note': None,
    },
    {
        'name': 'Button Group',
        'slug': 'button-group',
        'node_id': '40006598:81018',
        'variants': '36',
        'category': 'Form Controls',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Set of related buttons as a single visual unit for toggle options and segmented controls.',
        'anatomy': ['Container', 'Button items', 'Active indicator', 'Dividers'],
        'states': ['Default', 'One Active', 'Multi Active', 'Disabled'],
        'figma_variants': [('Style', 'Outlined / Filled'), ('Count', '2 / 3 / 4')],
        'sizes': ['Small', 'Medium', 'Large'],
        'real_tokens': [],
        'legacy_note': None,
    },
    {
        'name': 'Progress Circle',
        'slug': 'progress-circle',
        'node_id': '40000054:23550',
        'variants': '2',
        'category': 'Data Display',
        'token_system': 'New semantic',
        'token_class': 'status-good',
        'description': 'Circular progress indicator for course completion and achievement tracking.',
        'anatomy': ['Track circle', 'Progress arc', 'Center text (percentage)', 'Label (optional)'],
        'states': ['Empty (0%)', 'In Progress', 'Complete (100%)'],
        'figma_variants': [('Style', 'Default / With Label')],
        'sizes': ['Small (40px)', 'Medium (64px)', 'Large (96px)'],
        'real_tokens': [],
        'legacy_note': None,
    },
]

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
    <p class="section-desc">Token bindings extracted from Figma via <code>get_variable_defs</code>. Token naming system: <strong>{comp['token_system']}</strong>.</p>
    {tokens_html}
    {legacy_html}
  </div>

  <div class="section">
    <h2 class="section-title">Engineering Notes</h2>
    <div class="card" style="padding:24px">
      <ul style="margin:0;padding-left:20px;line-height:2;color:var(--text-support)">
        <li>Figma component node: <span class="token-name">{comp['node_id']}</span></li>
        <li>Token system: <strong>{comp['token_system']}</strong></li>
        <li>{comp['variants']} total variant configurations in Figma</li>
        <li>{'Tokens verified via Figma MCP extraction — ready for CSS mapping' if comp.get('real_tokens') else 'No token bindings — all values must be manually extracted or tokenized before implementation'}</li>
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
for comp in components:
    html = build_page(comp)
    path = os.path.join(OUT_DIR, f'{comp["slug"]}.html')
    with open(path, 'w') as f:
        f.write(html)
    print(f'  {comp["slug"]}.html ({len(html):,} bytes) — {comp["token_system"]}')

print(f'\nRegenerated {len(components)} component detail pages with real Figma token data')
