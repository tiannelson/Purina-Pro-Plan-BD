# BD Market Memo — Purina Pro Plan

Turns raw BD meeting notes into a memo that fuses what was discussed/decided
with live market and competitive research, ending in concrete recommended
actions tied to that research — not a meeting summary and a news digest
stapled together.

## Contents

| Path | What it is |
|---|---|
| `skill/SKILL.md` | The Claude skill definition (`bd-market-memo`) that drives the research + drafting workflow. |
| `batch_script/extract_notes.py` | Pulls plain text out of raw `.docx` meeting notes so they can be fed to the skill. |
| `batch_script/build_memos.py` | Renders one formatted `.docx` memo per meeting **in a single run**, reading structured content from `memos.json`. |
| `batch_script/memos.json` | The structured recap / market signals / implications / recommended actions for each meeting, produced by running the skill. |
| `grasp_briefs/` | GRASP briefs (to be added). |
| `validation_note.md` | Notes on how the skill's output was checked (to be filled in). |
| `example_output/` | One full example memo, showing the meeting-to-market connection the skill is meant to produce. |

## What the skill does

`bd-market-memo` (see `skill/SKILL.md`) takes one meeting's notes and:

1. Extracts the companies, products, and open questions worth researching.
2. Runs live web searches — it does not rely on background knowledge, since
   the whole point is *current* market context.
3. Writes a memo with four sections: **Meeting Recap**, **Market Signals**,
   **Implications** (explicitly connecting the two), and **Recommended
   Actions**. The Implications section is what makes it a memo instead of
   two reports glued together — every notable market signal is tied back to
   what it means for that specific meeting.
4. Produces a clean `.docx`.

It covers **one meeting per memo** by design.

## Why a batch step

Running the skill by hand once per meeting works, but doesn't scale past a
couple of meetings. `build_memos.py` is the batch step: give it a single
`memos.json` containing every meeting's already-researched content, and it
renders every meeting's `.docx` memo in one run instead of repeating the
document-formatting work by hand each time.

Note: the *research* itself (Step 2/3 in `SKILL.md`) still has to be done by
running the skill against each meeting's notes, because it depends on live
web search — that can't be pre-scripted. `build_memos.py` batches the
mechanical part (turning finished recap/signals/implications/actions content
into a formatted Word document), not the research itself.

## How to run it

1. If your notes are raw `.docx` files, extract their text:
   ```bash
   python3 batch_script/extract_notes.py path/to/meeting_notes.docx
   ```
2. Run the `bd-market-memo` skill against each meeting's notes (via Claude)
   to produce that meeting's recap / market signals / implications /
   recommended actions.
3. Add each meeting's content as an entry in `batch_script/memos.json`
   (see the existing entries for the expected shape).
4. Generate every memo in one run:
   ```bash
   pip3 install python-docx
   cd batch_script
   python3 build_memos.py
   ```
   This writes one `.docx` per meeting listed in `memos.json`.

## Example output

`example_output/Memo_3_Veterinary_Channel_Partnership.docx` shows the format:
a clinic's inventory-storage objection and staff-training gap, tied to live
research on a named competitor's clinically-marketed rival product and
Purina's own home-delivery program — with recommended actions that follow
directly from that link, not from the meeting notes or the market research
in isolation.
