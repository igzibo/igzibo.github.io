# Igzibo Engineering Solutions - GitHub Pages

A comprehensive website for Igzibo Engineering Solutions, showcasing services, team expertise, and thought leadership.

## Project Structure

```
igzibo.github.io/
├── index.html                          # Homepage
├── assets/
│   ├── css/
│   │   └── styles.css                 # Shared styles
│   └── js/
│       └── main.js                    # Shared JavaScript
├── about/
│   └── index.html                     # About page with mission and values
├── services/
│   ├── index.html                     # Services overview
│   ├── resource-placement/
│   │   └── index.html                 # Resource placement service
│   └── rd/
│       └── index.html                 # R&D service
├── team/
│   ├── index.html                     # Team overview
│   ├── engineers/
│   │   ├── index.html                 # Engineers listing
│   │   └── [engineer-name]/
│   │       └── index.html             # Individual engineer profile
│   └── leadership/
│       ├── index.html                 # Leadership team listing
│       └── [leader-name]/
│           └── index.html             # Individual leader profile
├── policies/
│   ├── index.html                     # Policies landing page
│   ├── client-services/               # Client Services policy category
│   ├── corporate/                     # Corporate policy category
│   ├── governance/                    # Governance policy category
│   ├── privacy/                       # Privacy policy category
│   ├── recruiting/                    # Recruiting policy category
│   ├── security/                      # Security policy category
│   └── website/                       # Website policy category
├── scripts/
│   └── build_policies.py              # Generates policy HTML from Markdown
└── README.md                          # This file
```

## Page Descriptions

### Main Pages

- **index.html** - Homepage featuring company overview, services, and call-to-action
- **about/** - Company mission, values, and story
- **services/** - Main services page with overview of all offerings

### Service Pages

- **services/resource-placement/** - Resource placement and staffing services
- **services/rd/** - Research & Development initiatives

### Team Pages

- **team/** - Team overview and statistics
- **team/engineers/** - Engineers listing and directory
- **team/leadership/** - Leadership team and executives

### Policy Pages

- **policies/** - Policies landing page with links to every category
- **policies/[category]/** - Category page listing policies by their Markdown title
- **policies/[category]/[policy].html** - Generated, styled HTML policy document

All site pages include a Policies dropdown in the top navigation. The dropdown links to the seven category pages: Client Services, Corporate, Governance, Privacy, Recruiting, Security, and Website.

## Managing Policy Documents

Policy source files are Markdown documents stored in their category folder under `policies/`. Do not edit generated policy HTML directly. Add or update the Markdown source, ensuring it has a level-one heading for the document title, then run the generator from the repository root:

```powershell
& "..\venvs\igzibo-github-io\Scripts\python.exe" scripts\build_policies.py
```

The generator:

- Converts each Markdown file to an HTML document.
- Uses the Markdown level-one heading as the display name and page title.
- Rebuilds each category index and the parent Policies page.
- Applies the shared stylesheet and standard site navigation.
- Includes the standard phone, email, and Calendly contact details.

The generator requires the `markdown` package listed in `requirements-dev.txt`. Install development dependencies with:

```powershell
& "..\venvs\igzibo-github-io\Scripts\python.exe" -m pip install -r requirements-dev.txt
```

## Adding New Team Members

### Adding a New Engineer

1. Create a new directory under `team/engineers/` with the engineer's name in kebab-case:
   ```
   team/engineers/john-smith/
   ```

2. Copy the content from `team/engineers/boukhalfa-ouhamouche/index.html` as a template

3. Update the following sections:
   - `<title>` and meta tags
   - Profile name, role, and bio
   - Professional summary and achievements
   - Technical skills
   - Certifications and education
   - Any other relevant information

4. Update `team/engineers/index.html` to add the engineer to the listing:
   ```html
   <div class="member-card">
     <div class="member-photo">Photo Coming Soon</div>
     <div class="member-info">
       <h3>John Smith</h3>
       <div class="member-role">Senior Backend Engineer</div>
       <div class="member-bio">
         Brief bio describing expertise and experience.
       </div>
       <a href="/team/engineers/john-smith/" class="member-link">View Profile →</a>
     </div>
   </div>
   ```

### Adding a New Leader

1. Create a new directory under `team/leadership/` with the leader's name in kebab-case:
   ```
   team/leadership/executive-name/
   ```

2. Copy the content from `team/leadership/ryan-schostag/index.html` as a template

3. Update all relevant sections with the leader's information

4. Update `team/leadership/index.html` to add the leader to the listing

## Styling

All pages use a unified styling system defined in `assets/css/styles.css`. Key design elements:

- **Color Scheme:**
  - Primary: #0F172A (dark blue)
  - Secondary: #1E293B (lighter blue)
  - Accent: #06B6D4 (cyan)
  - Success: #10B981 (green)
  - Background: #F8FAFC (light gray)

- **Components:**
  - Hero sections with gradients
  - Card-based layouts
  - Consistent navigation
  - Responsive design (mobile-first)
  - Call-to-action buttons

## JavaScript Functionality

`assets/js/main.js` provides:

- Active navigation link detection
- Policies dropdown injection for legacy pages without static navigation markup
- Smooth scroll behavior for anchor links

## SEO Optimization

Each page includes:

- Descriptive `<title>` tags
- Meta descriptions
- Relevant keywords
- Open Graph tags
- Semantic HTML structure
- Structured data ready (can be enhanced)

## Contact Information

All pages include consistent contact information:

- **Phone:** 971-236-1374
- **Email:** support@igzibo.com
- **Calendly:** https://calendly.com/igzibo-support

## Color Palette & Design

The site uses a professional technology company color scheme:

- Dark blues and grays for primary sections
- Cyan accent color for highlights and CTAs
- Clean, modern typography using Google Fonts (Inter)
- Generous whitespace and clear visual hierarchy

## Content Guidelines

### Writing Style

- Clear, professional, and accessible
- Focus on benefits and outcomes
- Highlight expertise and experience
- Include specific examples and achievements
- Call-to-action oriented

### SEO Best Practices

- Use relevant keywords naturally in headings and content
- Include descriptive meta tags
- Structure content with clear headings
- Add alt text to images (when images are added)
- Internal linking between related pages

## Future Enhancements

Consider adding:

1. Blog section for thought leadership
2. Case studies showcasing project success
3. Client testimonials
4. Career/hiring page
5. Event calendar
6. Newsletter signup
7. Image assets for team members
8. PDF download for service offerings
9. Integration with email newsletter service
10. Analytics tracking

## Maintenance

### Regular Updates

- Update team member information as needed
- Refresh service offerings and case studies
- Update contact information if it changes
- Review and update meta tags for SEO
- Test responsive design on new devices

### Performance Tips

- Optimize images when added
- Minimize CSS/JS if needed
- Implement lazy loading for images
- Consider CDN for static assets

## Brand Voice

The site should maintain:

- Professional but approachable tone
- Focus on technical excellence
- Emphasis on practical solutions
- Commitment to customer success
- Innovation and continuous learning

## Contact & Support

For questions or updates to this website, contact:

- **Phone:** 971-236-1374
- **Email:** support@igzibo.com
- **Calendly:** https://calendly.com/igzibo-support

---

**IGZIBO | Engineering Solutions. Building What's Next.**

© 2024 Igzibo Engineering Solutions, Inc. All rights reserved.
