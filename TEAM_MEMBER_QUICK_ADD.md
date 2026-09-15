# Quick Reference: Adding Team Members

## Adding a New Engineer

### Step 1: Create Directory
Create folder: `team/engineers/[kebab-case-name]/`

Example: `team/engineers/sarah-johnson/`

### Step 2: Copy Template
Copy file from: `team/engineers/john-doe/index.html`
Paste as: `team/engineers/[name]/index.html`

### Step 3: Update Profile Content

In the profile file, update:

```html
<!-- Page Title -->
<title>Name | Job Title | Igzibo</title>

<!-- Meta Description -->
<meta name="description" content="...description...">

<!-- Profile Header -->
<h1>Name</h1>
<div class="member-role">Job Title</div>

<!-- Professional Summary -->
<p>Biography and overview...</p>

<!-- Experience -->
Update all sections with specific achievements

<!-- Technical Skills -->
List relevant technologies and expertise

<!-- Certifications -->
Education, certifications, years of experience
```

### Step 4: Add to Engineers Directory

Edit: `team/engineers/index.html`

Add this card to the grid:

```html
<div class="member-card">
  <div class="member-photo">Photo Coming Soon</div>
  <div class="member-info">
    <h3>Engineer Name</h3>
    <div class="member-role">Job Title</div>
    <div class="member-bio">
      Brief description of expertise (2-3 sentences)
    </div>
    <a href="/team/engineers/kebab-case-name/" class="member-link">View Profile →</a>
  </div>
</div>
```

### Step 5: Test
- Navigate to `/team/engineers/[name]/` in browser
- Verify all links work
- Check mobile responsiveness

---

## Adding a New Leader

### Step 1: Create Directory
Create folder: `team/leadership/[kebab-case-name]/`

Example: `team/leadership/executive-name/`

### Step 2: Copy Template
Copy file from: `team/leadership/ryan-schostag/index.html`
Paste as: `team/leadership/[name]/index.html`

### Step 3: Update Profile Content

Same as engineer profile, but emphasize:
- Executive role and responsibilities
- Strategic initiatives and impact
- Organization building and team leadership
- Business acumen and results

### Step 4: Add to Leadership Directory

Edit: `team/leadership/index.html`

Add this card to the grid:

```html
<div class="member-card">
  <div class="member-photo">Photo Coming Soon</div>
  <div class="member-info">
    <h3>Executive Name</h3>
    <div class="member-role">Executive Title</div>
    <div class="member-bio">
      Brief description of leadership role and expertise
    </div>
    <a href="/team/leadership/kebab-case-name/" class="member-link">View Profile →</a>
  </div>
</div>
```

### Step 5: Test
- Navigate to `/team/leadership/[name]/` in browser
- Verify all links work
- Check layout and formatting

---

## Common Updates

### Update Contact Information
- Find and replace phone number in all HTML files
- Update email in footer
- Verify Calendly link

### Update Company Info
- Search for company name in all files
- Update mission and values if changed
- Review meta descriptions for accuracy

### Add New Service Page

1. Create folder: `services/[service-name]/`
2. Create file: `services/[service-name]/index.html`
3. Use existing service pages as template
4. Update links in:
   - `services/index.html` (main services page)
   - `index.html` (homepage)
   - Navigation menus across site

---

## SEO Checklist

When adding new content, ensure:

- [ ] Unique, descriptive title tag (50-60 characters)
- [ ] Meta description (150-160 characters)
- [ ] Relevant keywords in description
- [ ] H1 heading on page
- [ ] Descriptive headings (H2, H3)
- [ ] Natural keyword usage in content
- [ ] Links to related pages
- [ ] Open Graph tags filled in
- [ ] Clear call-to-action buttons
- [ ] Contact information present

---

## Naming Conventions

### File/Folder Names
- Use kebab-case (lowercase with hyphens)
- Examples: `john-smith`, `senior-engineer`, `cloud-architect`

### CSS Classes
- Already defined in `assets/css/styles.css`
- Use existing classes: `.card`, `.member-card`, `.btn`, etc.

### IDs
- Use semantic names: `#services`, `#about`, `#contact`

---

## Common Components

### Button (Primary)
```html
<a href="/" class="btn">Button Text</a>
```

### Button (Outline)
```html
<a href="/" class="btn-outline">Button Text</a>
```

### Card
```html
<div class="card">
  <h3>Card Title</h3>
  <p>Card content...</p>
</div>
```

### Section Title
```html
<div class="section-title">
  <h2>Section Heading</h2>
  <p>Subtitle or description</p>
</div>
```

### Member Card
```html
<div class="member-card">
  <div class="member-photo">Photo Coming Soon</div>
  <div class="member-info">
    <h3>Name</h3>
    <div class="member-role">Role</div>
    <div class="member-bio">Bio...</div>
    <a href="/link/" class="member-link">View Profile →</a>
  </div>
</div>
```

---

## Testing Checklist

Before publishing changes:

- [ ] All links work correctly
- [ ] Page loads quickly
- [ ] Mobile view looks good
- [ ] All images display properly
- [ ] Contact information is current
- [ ] CTAs are visible and working
- [ ] No typos or broken text
- [ ] Calendly link works
- [ ] Phone links dial correctly (tel:)
- [ ] Email links open correctly (mailto:)

---

## File Locations Reference

| Type | Location |
|------|----------|
| Styles | `assets/css/styles.css` |
| Scripts | `assets/js/main.js` |
| Engineer Profile Template | `team/engineers/john-doe/index.html` |
| Leader Profile Template | `team/leadership/jane-smith/index.html` |
| Homepage | `index.html` |
| Main Services | `services/index.html` |
| Main Team | `team/index.html` |

---

## Quick Commands

### View site locally (if using Python)
```bash
python -m http.server 8000
# Visit http://localhost:8000
```

### View site locally (if using Node)
```bash
npx http-server
# Visit http://localhost:8080
```

### Find and replace across files
Use VS Code:
- Ctrl+H (or Cmd+H on Mac)
- Enter search term
- Enter replacement
- Replace All

---

## Need Help?

- **Phone:** 971-236-1374
- **Email:** support@igzibo.com
- **Calendly:** https://calendly.com/igzibo-support

For detailed documentation, see [WEBSITE_GUIDE.md](WEBSITE_GUIDE.md)

---

**IGZIBO | Engineering Solutions. Building What's Next.**
