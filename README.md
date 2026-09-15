# Igzibo Engineering Solutions - GitHub Pages

Welcome to the Igzibo Engineering Solutions website repository. This is a comprehensive, professional website showcasing our engineering consulting services, team expertise, and thought leadership.

## Website Overview

**Live Site:** [igzibo.github.io](https://igzibo.github.io)

**Our Mission:** To deliver reliable, customized, and creative solutions to the world.

**Our Values:**
- Leave ourselves better than how we found ourselves
- Leave others better than how we found them
- Leave the world better than how we found it

## Features

### 📄 Pages Included

- **Homepage** - Overview of services and company overview
- **About** - Company mission, values, and story
- **Services** - Engineering consulting, software development, cloud architecture, data solutions, DevOps, and system modernization
- **Resource Placement** - Engineering talent placement and staffing services
- **Research & Development** - Cutting-edge R&D initiatives and innovation
- **Team** - Team overview and structure
- **Engineers** - Directory of engineering professionals with individual profiles
- **Leadership** - Technical leaders and executives with individual profiles

### 🎨 Design Features

- Professional, modern design with clean typography
- Responsive design optimized for mobile, tablet, and desktop
- Consistent color scheme and branding
- Smooth navigation and fast loading
- SEO optimized for search engines and AI research tools

### 📱 SEO & AI Optimization

Each page includes:
- Descriptive titles and meta descriptions
- Relevant keywords for search engines and AI tools (ChatGPT, Claude, Copilot)
- Structured content with clear headings
- Call-to-action elements encouraging contact

### 🔗 Easy Navigation

- Sticky header with navigation menu
- Clear page hierarchy
- Breadcrumb-like structure
- Quick links to key pages
- Calendly integration for scheduling

## Quick Links

- **Phone:** 971-236-1374
- **Email:** support@igzibo.com
- **Calendly:** https://calendly.com/igzibo-support

## Project Structure

```
├── index.html                 # Homepage
├── about/                     # About page
├── services/                  # Main services page
│   ├── resource-placement/   # Resource placement service
│   └── rd/                   # Research & Development
├── team/                      # Team pages
│   ├── engineers/            # Engineers directory
│   │   └── [engineer-name]/  # Individual engineer profiles
│   └── leadership/           # Leadership directory
│       └── [leader-name]/    # Individual leader profiles
├── assets/
│   ├── css/styles.css        # Unified styling
│   └── js/main.js            # Shared functionality
├── README.md                 # This file
└── WEBSITE_GUIDE.md          # Detailed maintenance guide
```

## Adding Team Members

The website is designed for easy team member management:

### Adding an Engineer

1. Create a new folder: `team/engineers/[engineer-name]/`
2. Copy template from `team/engineers/john-doe/index.html`
3. Update engineer information (name, role, bio, skills, etc.)
4. Add to `team/engineers/index.html` listing

### Adding a Leader

1. Create a new folder: `team/leadership/[leader-name]/`
2. Copy template from `team/leadership/jane-smith/index.html`
3. Update leader information
4. Add to `team/leadership/index.html` listing

See [WEBSITE_GUIDE.md](WEBSITE_GUIDE.md) for detailed instructions.

## Technology Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS variables and Grid/Flexbox
- **JavaScript** - Vanilla JS for smooth interactions
- **Google Fonts** - Inter font family
- **Responsive Design** - Mobile-first approach

## Customization

### Styling

All colors and styles are defined in `assets/css/styles.css`. Key CSS variables:
- `--primary` - Main dark blue
- `--accent` - Cyan highlights
- `--bg` - Light backgrounds
- `--text` - Text color

### Content

Update company information in any HTML file:
- Contact details
- Service descriptions
- Team member information
- Mission and values

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Responsive design for all screen sizes

## Performance

- Lightweight static HTML (no build process needed)
- Minimal CSS and JS
- Fast page load times
- Mobile optimized

## Maintenance

### Regular Tasks

- Update team member profiles as needed
- Refresh service descriptions
- Add new case studies or achievements
- Monitor and update SEO keywords
- Test on new devices/browsers

### Content Updates

All content can be updated directly in HTML files:
- Edit in any text editor
- Use VS Code for enhanced experience
- Test locally before deploying

## Git Workflow

```bash
# Clone the repository
git clone https://github.com/yourusername/igzibo.github.io.git

# Create a feature branch for changes
git checkout -b feature/add-team-member

# Make changes to HTML files
# Test locally

# Commit changes
git add .
git commit -m "Add new engineer profile"

# Push to GitHub
git push origin feature/add-team-member

# Create pull request and merge to main
```

## Regression Tests

A pytest suite covers broken links/assets, HTML validity, accessibility (axe-core), and visual regression (screenshot diffing). See [tests/README.md](tests/README.md) for setup and run instructions. Quick start:

```powershell
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python -m pytest -v
```

## Deployment

This site is automatically deployed to GitHub Pages:

1. Changes pushed to `main` branch trigger deployment
2. Site updates within minutes
3. No build process needed
4. All files served as static content

## Future Enhancements

Consider adding:
- Blog/news section
- Case studies with results
- Client testimonials
- Career opportunities page
- Team photos
- Service pricing (optional)
- Email newsletter integration
- Dynamic team member loading
- Multi-language support

## Contact & Support

For website updates or questions:

- **Phone:** 971-236-1374
- **Email:** support@igzibo.com
- **Calendly:** https://calendly.com/igzibo-support

---

## Detailed Documentation

For complete documentation on:
- Adding new pages
- Updating styles
- SEO optimization
- Team member management

See [WEBSITE_GUIDE.md](WEBSITE_GUIDE.md)

---

**IGZIBO | Engineering Solutions. Building What's Next.**

© 2024 Igzibo Engineering Solutions, Inc. All rights reserved.
