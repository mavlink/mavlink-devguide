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
- **Diagrams**: `assets/protocols/mission_item_detail/` (SVG) and `assets/protocols/mission_loiter/` (PNG, legacy). This skill does not generate diagrams. If the command needs one and none exists, say so and continue without it — don't invent a diagram or block the rest of the workflow on it.

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

5. **Format.** Run `yarn format` (prettier + markdownlint --fix over `en/**/*.md`) and confirm it only touched the section you added.

6. **Commit the structural addition.** Create a new branch off the current branch, named `<short-name>_mission_item_docs` where `<short-name>` is the command name lowercased with the `MAV_CMD_` prefix stripped (e.g. `MAV_CMD_NAV_TAKEOFF` → `nav_takeoff_mission_item_docs`). Commit with a message in this repo's established style: `Mission item detail: add MAV_CMD_<NAME> section`. Do not push — leave that to the user.

7. **Revise the description.** Now rewrite the placeholder from step 3 into real docs prose, applying the Style rules below. In particular:
   - Open with a sentence of the form `[MAV_CMD_<NAME>](../messages/common.md#MAV_CMD_<NAME>) causes a vehicle to <effect>.` — link to the XML definition rather than restating it as freestanding prose.
   - Add any known frame-specific behavior (e.g. multicopter vs. fixed-wing differences), stated tersely (see Style).
   - If a diagram exists for this command (see Sources of truth), use it as the basis for any expanded explanation — don't describe behavior the diagram doesn't support.
   - **Must not contradict or semantically change** what the XML says — extend and clarify only.

8. **Autopilot Support.** Replace the `Untested` placeholder with real implementation notes only if you have a verified source for them (e.g. a linked issue, changelog, or code reference) — otherwise leave it as `Untested`. Follow the `CONDITION_GATE` section's format (a short bullet list per autopilot).

9. **Self-review.** Before finishing, re-read your own diff against the Review checklist below, as if reviewing someone else's PR.

Commit steps 7–9 separately from step 6 (e.g. `Mission item detail: refine MAV_CMD_<NAME> description`), so the mechanical addition and the editorial pass are distinguishable in history.

## Review

Read the existing `### MAV_CMD_<NAME>` section in `en/services/mission_item_detail.md` and its XML source in `en/messages/*.md`, then check:

- **No meaning change.** The section may extend the XML (add detail, examples, frame-specific behavior) but must never contradict it or narrow/widen what a param does.
- **Params match.** Every param row's description and units are consistent with the XML — same semantics, not necessarily identical wording, but no dropped constraints (ranges, enum values, "ignored by X" caveats).
- **Diagrams match.** Any referenced diagram must depict what the text and XML actually describe — flag anything the diagram shows that the text doesn't support, or vice versa.
- **Style — terse, no contrastive filler.** Prefer stating each case plainly over contrasting it against the other. For example:
  - Bad: "Multicopters fly to altitude X and hover — not to a specific parameter. Fixed wing vehicles ignore the param and ascend to a system-specified height: unlike multicopters."
  - Good: "Multicopters fly to altitude X and hover. Fixed wing fly to a parameter set height."
  Watch for "unlike", "whereas", "in contrast", "not X but Y", and similar constructions that spend words contrasting instead of just stating the fact.

Report findings as a list of concrete edits (file, location, current text, suggested text), don't rewrite the file yourself unless asked to apply the fixes.
