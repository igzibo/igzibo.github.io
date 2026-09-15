# Repository Instructions

## General

- Inspect the existing repository before making changes.
- Preserve existing functionality unless the requested change explicitly requires modifying it.
- Prefer small, focused changes over broad refactoring.
- Do not modify unrelated files.
- Follow existing project conventions for naming, formatting, structure, and architecture.
- Do not introduce new dependencies unless they are necessary and justified.
- Do not duplicate existing functionality.
- Reuse existing components, styles, utilities, and configuration where appropriate.
- Use Test-Driven Development (TDD) whenever possible. Only update existing test modules when absolutely necessary; otherwise, always update the code to pass failing tests. 
- When provided an output file, do not delete or overwrite it during troubleshooting or validation. Instead, simply create a new output file and provide the path to it when ready to share the results.

## GitHub Pages

- Ensure all changes remain compatible with GitHub Pages.
- Respect the repository's existing GitHub Pages deployment configuration.
- Do not change the deployment workflow unless specifically requested.
- Verify that links and asset paths work when the site is served from its GitHub Pages base path.
- Avoid assumptions that the site is hosted at `/`.
- Preserve relative-path and base-path conventions already used by the project.

## HTML / Accessibility

- Use semantic HTML.
- Provide appropriate `alt` text for meaningful images.
- Maintain logical heading hierarchy.
- Ensure interactive elements are keyboard accessible.
- Use labels for form controls.
- Do not use color as the only means of communicating information.

## CSS / UI

- Preserve the existing visual design unless a redesign is requested.
- Prefer existing CSS variables, classes, and components.
- Maintain responsive behavior.
- Check mobile, tablet, and desktop layouts when modifying UI.
- Avoid unnecessary inline styles.
- Do not introduce arbitrary colors, spacing, or typography when existing design tokens are available.

## JavaScript

- Follow the existing JavaScript architecture.
- Avoid unnecessary client-side JavaScript.
- Handle errors explicitly where appropriate.
- Do not silently swallow errors.
- Avoid global variables unless the existing architecture requires them.

## Content

- Preserve existing content unless the request specifically changes it.
- Do not invent factual claims, credentials, statistics, testimonials, or external links.
- Check external links for obvious errors when modifying them.

## Validation

After making changes:

1. Inspect the final diff.
2. Run available tests.
3. Run the project's build command when available.
4. Run linting or formatting checks when available.
5. Check for broken references and missing assets.
6. Fix problems introduced by the change.
7. Do not modify unrelated files.

## Scope Control

Do not:
- refactor unrelated code;
- rewrite working components unnecessarily;
- change dependencies without justification;
- rename files or variables without a reason related to the requested change;
- reformat unrelated files;
- replace existing libraries or frameworks;
- redesign the UI unless explicitly requested;
- "clean up" unrelated code;
- make speculative improvements.

If an unrelated problem is discovered, mention it in the final response rather than fixing it automatically.

## Commit

Each commit should:

- Represent one logical change.
- Use a concise conventional commit message when appropriate.
- Avoid unrelated formatting or refactoring.
- Clearly describe what changed.
- Report validation performed.
- Provide your commit message in a plain text block with no file hyperlinks.