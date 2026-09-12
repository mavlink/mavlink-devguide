# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

This is the **MAVLink Developer Guide** — a VitePress-based documentation site for the MAVLink drone messaging protocol. Source content lives in `en/` (English), with translations in `zh/` (Chinese) and `ko/` (Korean) managed via Crowdin. The published site is at mavlink.io.

## Commands

```bash
# Install dependencies
npm ci         # or: yarn install

# Local dev server with hot reload
yarn start     # alias for: yarn docs:dev

# Production build (Linux)
yarn docs:build

# Production build (Windows)
yarn docs:buildwin

# Preview the built site
yarn docs:preview

# Check links
yarn linkcheck
```

CI (`.github/workflows/docs_deploy.yml`) uses `npm ci` + `npm run docs:build` on Node 20, then deploys to the `mavlink/mavlink.io` repo.

## Architecture

### Directory Layout

- `en/` — primary English source; all editing happens here
- `zh/`, `ko/` — machine/community translations synced from Crowdin (do not edit directly)
- `.vitepress/config.mjs` — VitePress site config; sidebars are generated dynamically from `SUMMARY.md` files rather than hard-coded
- `.vitepress/get_sidebar.js` — parses `SUMMARY.md` GitBook-style files to generate VitePress sidebar config
- `.vitepress/theme/` — custom theme overrides

### Navigation / Sidebar

The sidebar for each language is built by reading that language's `en/SUMMARY.md` (and equivalent). This file is the authoritative table of contents — adding a new page requires both creating the `.md` file **and** adding it to `SUMMARY.md`.

### Content Structure (`en/`)

- `messages/` — auto-generated message reference docs (one per XML dialect: `common.md`, `ardupilotmega.md`, etc.)
- `services/` — microservice protocol docs (mission, command, camera, gimbal, FTP, etc.)
- `guide/` — protocol internals (serialization, routing, MAVLink 2, signing, etc.)
- `mavgen_c/`, `mavgen_python/` — language-specific library usage guides
- `contributing/` — contributor guides
- `about/`, `getting_started/`, `file_formats/` — introductory and reference content

### Excluded from Build

Files matching `**/_*.md` are excluded from the VitePress build (used as includes/partials). Several language folders (`de`, `ja`, `ru`, `tr`, `uk`) are also excluded — only `en`, `zh`, and `ko` are active.

## Authoring Conventions

- VitePress callout syntax: `::: info`, `::: tip`, `::: warning`, `::: danger` (not `> **Note**` or `> **Tip**`)
- Math is supported via `markdown-it-mathjax3` — use `$...$` inline and `$$...$$` for blocks
- Tabs component is available via `@red-asuka/vitepress-plugin-tabs`
- Internal links use relative paths to `.md` files (e.g., `../services/mission.md`)
- The `EDITOR` environment variable enables "Open in your editor" links during local dev; omit it to get GitHub edit links instead

## Documentation Accuracy Rules

- Every claim about a `MAV_CMD`/message param — its existence, number, name, description, units, range — must agree with the corresponding entry in `en/messages/*.md` (mirrors the XML). If existing prose or a proposed change conflicts with the XML, don't silently override it — flag the conflict and propose fixing the XML (`mavlink/mavlink`) instead of the doc, if the XML is what's wrong.
- Never state what a specific autopilot (ArduPilot, PX4, ...) actually does without a citable source: a file/line in that project's own repo, a linked test, or a linked issue/PR discussion. No citation → omit the claim, or mark it explicitly unverified rather than asserting it as fact.
- Keep new prose as terse as the surrounding section; don't rewrite already-accepted wording for style alone.
- A change that reorganizes or moves existing content must do so with zero wording changes; any wording change (correction, addition, clarification) belongs in its own separate, clearly-labeled commit.
- See the `mavlink-command-review` Claude Code skill for the full checklist when reviewing or authoring pages about specific commands/messages (e.g. `en/services/mission_item_detail.md`).

## Translation Workflow

- Crowdin config (`crowdin.yml`) maps `en/**/*.md` → `{lang}/**/{filename}.md`
- Only edit English source in `en/`; translation PRs come from the Crowdin bot
- New pages need to be in `en/SUMMARY.md` before Crowdin will pick them up
