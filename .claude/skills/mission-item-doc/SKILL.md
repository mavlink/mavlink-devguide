---
name: mission-item-doc
description: Add or review a MAV_CMD section in en/services/mission_item_detail.md. Invoke with the MAV_CMD name to document (e.g. "MAV_CMD_NAV_TAKEOFF"). If the command already has a section, review it; otherwise add a new one. Use for requests like "document MAV_CMD_DO_SET_ROI in mission item detail" or "review the MAV_CMD_NAV_LOITER_TIME section".
---

# Mission item doc

Adds or reviews the documentation section for one `MAV_CMD` in `en/services/mission_item_detail.md`, the page that gives mission items ("MAV_CMD"s used in plans) clarifications and detail beyond what the XML spec text carries.

Invoked with a single `MAV_CMD_*` name. Resolve which mode to run **first**:

```
grep -n "^### MAV_CMD_<NAME>" en/services/mission_item_detail.md
```

- Match found → **Review** (below).
- No match → **Add** (below).

If the argument isn't a valid `MAV_CMD_*` name, or doesn't exist in any dialect (see Sources of truth), stop and say so rather than guessing.

## Sources of truth

- **XML content** (description, params, units, value ranges, enum types): `en/messages/*.md`, the auto-generated per-dialect message reference. These files are generated from the upstream `mavlink/mavlink` XML definitions and are the authoritative record of what the spec actually says — never take the description or param text from memory or from mavlink.io.
  Find the command with:
  ```
  grep -rn "^### MAV_CMD_<NAME> " en/messages/*.md
  ```
  Check `common.md` first; most mission-item MAV_CMDs live there. If not found there, check the dialect-specific files (`ardupilotmega.md`, `cubepilot.md`, etc.) — skip `all.md`, `index.md`, and `dialects.md`, which are indexes, not definitions. If the command is defined in more than one dialect with different text, flag this to the user before proceeding rather than picking one silently.
- **Target doc**: `en/services/mission_item_detail.md`.
- **Diagrams**: `assets/protocols/mission_item_detail/` (SVG) and `assets/protocols/mission_loiter/` (PNG, legacy). The XML never contains diagrams, so if a command's behavior benefits from one, this skill creates a new inline SVG in `assets/protocols/mission_item_detail/` (see step 7 in Add). Its *design* may draw on wider knowledge of the command's behavior than the XML alone provides, but it must never contradict the XML — only illustrate/extend it. Use the existing SVGs in that directory (e.g. `gate_crossing.svg`, `waypoint_accept_radius.svg`) as the style template: same `viewBox`/font conventions, `#2563eb` for the primary path, `#6b7280` for secondary/reference elements. When different param values drive genuinely different behavior (not just different numbers along the same path), one diagram per variation is fine — see `waypoint_accept_radius.svg` (default path) vs. `waypoint_yaw.svg` (the Yaw param's effect) on `MAV_CMD_NAV_WAYPOINT`. The same no-contradiction rule applies to each.

## Add

1. **Locate the section group.** Sections are grouped by command prefix under a `## \`PREFIX_\` Items` heading (e.g. `## \`NAV_\` Items`, `## \`CONDITION_\` Items`). Find the group matching the new command's prefix (the part of the name between `MAV_CMD_` and the next `_`, e.g. `NAV`, `CONDITION`, `DO`). If no group exists yet for that prefix, add a new `##` heading in a sensible position relative to the existing groups (roughly the order commands appear in the XML). Place the new `###` heading alphabetically/logically within its group, near related commands (e.g. keep the `LOITER_*` commands together).

2. **Add the heading and skeleton**, matching this shape exactly (anchor matches the command name):

   ```markdown
   ### MAV_CMD_<NAME> {#MAV_CMD_<NAME>}

   <description — see step 3>

   #### Params

   <params table — see step 4>

   #### Autopilot Support

   Untested
   ```

3. **Description text — verbatim first pass.** Paste the description exactly as it appears in the XML source (`en/messages/*.md`), unedited. This is a placeholder for step 6, not the final text — do not paraphrase or add anything here yet.

4. **Params table.** Build a table with exactly these headers: `Param (:Label)`, `Description`, `Units`. Source rows from the XML table (`Param (Label) | Description | Values | Units`, though the `Values` column is only present for some commands). Use `MAV_CMD_NAV_LOITER_TURNS` and `MAV_CMD_CONDITION_GATE` in the target file as the canonical formatting templates:
   - `Param (:Label)`: `<n>: <Label>` (e.g. `3: Radius`), or just the bare number with no colon/label if the XML labels it "Empty"/gives no label.
   - `Description`: the XML description, verbatim. If the XML `Values` column names an enum type (e.g. `MAV_BOOL`), don't add a separate column — link the specific enum value inline within the description text where it's named, e.g. `[MAV_BOOL_TRUE](../messages/common.md#MAV_BOOL)`, following the `CONDITION_GATE` param 2 example. A reserved/empty param gets `-` as its description.
   - `Units`: the XML units. If the XML `Values` column instead gives a numeric range/increment (not an enum), fold it into this column as `min:X max:Y increment:Z`, appending the unit after if there is one — see `LOITER_TURNS` param 2 (`min:0 max:1 increment:1`) for the exact style.

5. **Format.** Run prettier and markdownlint scoped to just the file(s) you touched — `npx prettier --write en/services/mission_item_detail.md` and `npx markdownlint-cli2 --fix en/services/mission_item_detail.md` — and confirm the diff only covers the section you added. **Do not run the repo-wide `yarn format`/`yarn lint`**: it reformats every file matching `en/**/*.md`, including the auto-generated `en/messages/*.md` dialect references, which aren't prettier-clean as committed — a full run produces thousands of lines of unrelated whitespace churn across those files.

   Also run `npx cspell en/services/mission_item_detail.md` (scoped, not the full-tree command). New vocabulary the command introduces (a vehicle type, an acronym, a param name) may not be in the dictionary yet — the pre-commit hook runs cspell too and will otherwise block the commit in step 6. Add any missing word to `cspell.json`'s `words` array, alphabetically among entries of the same case convention, rather than working around the check.

6. **Commit the structural addition.** Create a new branch off the current branch, named `<short-name>_mission_item_docs` where `<short-name>` is the command name lowercased with the `MAV_CMD_` prefix stripped (e.g. `MAV_CMD_NAV_TAKEOFF` → `nav_takeoff_mission_item_docs`). Commit with a message in this repo's established style: `Mission item detail: add MAV_CMD_<NAME> section`. Do not push — leave that to the user.

7. **Revise the description.** Now rewrite the placeholder from step 3 into real docs prose, applying the Style rules below. In particular:
   - Open with a sentence of the form `[MAV_CMD_<NAME>](../messages/common.md#MAV_CMD_<NAME>) causes a vehicle to <effect>.` — link to the XML definition rather than restating it as freestanding prose.
   - **Lead with the default/normal-usage behavior**: what happens with sentinel values (`NaN`, `0`, whatever the XML defines as "use default"/unset) or unused params, or simply the most common way the command is used. Param-driven variations come after, not first — a reader who never touches the non-default params should get a complete picture from the opening paragraph alone.
   - Add any known frame-specific behavior (e.g. multicopter vs. fixed-wing differences), stated tersely (see Style).
   - **Param variations go in their own `####` subsections**, one per distinct behavior a param (or param combination) triggers, each with its own anchor — follow `MAV_CMD_NAV_WAYPOINT`'s `#### Yaw (heading at the waypoint) {#yaw}` and `MAV_CMD_NAV_LOITER_TIME`'s `#### Exit Conditions {#loiter_exit}` as templates. Don't fold a param variation into the main description paragraph.
   - If a variation's behavior is spatial/geometric (paths, trigger points, headings, radii — the kind of thing a picture clarifies faster than prose), create a new SVG diagram under `assets/protocols/mission_item_detail/` (see Diagrams in Sources of truth) for that subsection, referenced with an `![alt](...)` line. Base the diagram's design on wider knowledge of how the command actually behaves, not just the XML text, but don't let it depict anything the XML contradicts. Skip the diagram if the behavior is simple enough that prose alone is clear.
   - **Must not contradict or semantically change** what the XML says — extend and clarify only. This applies to the diagrams as much as the prose.

8. **Autopilot Support.** Replace the `Untested` placeholder with real implementation notes only if you have a verified source for them (e.g. a linked issue, changelog, or code reference) — otherwise leave it as `Untested`. Follow the `CONDITION_GATE` section's format (a short bullet list per autopilot).

9. **Self-review.** Before finishing, re-read your own diff against the Review checklist below, as if reviewing someone else's PR.

Commit steps 7–9 separately from step 6 (e.g. `Mission item detail: refine MAV_CMD_<NAME> description`), so the mechanical addition and the editorial pass are distinguishable in history.

## Review

Read the existing `### MAV_CMD_<NAME>` section in `en/services/mission_item_detail.md` and its XML source in `en/messages/*.md`, then check:

- **No meaning change.** The section may extend the XML (add detail, examples, frame-specific behavior) but must never contradict it or narrow/widen what a param does.
- **Params match.** Every param row's description and units are consistent with the XML — same semantics, not necessarily identical wording, but no dropped constraints (ranges, enum values, "ignored by X" caveats).
- **Default behavior comes first.** The opening description should cover sentinel-value/unused-param/normal-usage behavior; param-driven variations belong later, in their own `####` subsections (following the `Yaw`/`Exit Conditions` pattern), not folded into the opening paragraph.
- **Diagrams match.** A diagram's content may go beyond the XML (it's necessarily drawn from wider knowledge, since the XML has no diagrams) but must not contradict it or the section text — flag anything the diagram shows that the XML rules out, or that the text doesn't support. Flag a missing diagram only when the command is clearly spatial/geometric and prose alone is hard to follow.
- **Style — terse, no contrastive filler.** Prefer stating each case plainly over contrasting it against the other. For example:
  - Bad: "Multicopters fly to altitude X and hover — not to a specific parameter. Fixed wing vehicles ignore the param and ascend to a system-specified height: unlike multicopters."
  - Good: "Multicopters fly to altitude X and hover. Fixed wing fly to a parameter set height."
  Watch for "unlike", "whereas", "in contrast", "not X but Y", and similar constructions that spend words contrasting instead of just stating the fact.

Report findings as a list of concrete edits (file, location, current text, suggested text), don't rewrite the file yourself unless asked to apply the fixes.
