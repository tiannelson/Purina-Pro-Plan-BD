---
name: bd-market-memo
description: Turns raw Business Development (BD) meeting notes into a memo that connects what happened in the meeting with what is currently happening in the market. Use this skill whenever the user provides notes from a BD meeting (attendees, discussion points, action items, where things were left) and wants that combined with current market or competitive research — even if they don't use the words "memo" or "market research" explicitly. Trigger on phrases like "BD notes," "sales call notes," "meeting notes + market context," "what should we do given this meeting," or any request to turn meeting notes into a strategic brief. Covers one meeting per memo. Requires live web search — do not substitute prior knowledge for current market data.
---

# BD Market Memo

Produces a single memo (.docx) that fuses one BD meeting's notes with live market/competitive research, ending in concrete recommended actions — not a meeting summary and a news digest stapled together.

## Workflow

### Step 1: Get the meeting notes
Accept notes as pasted text or an uploaded file (docx/txt/md). If a file is uploaded, read the `docx` skill first (`/mnt/skills/public/docx/SKILL.md`) before touching any .docx input or output.

If notes are missing key basics (who was in the meeting, what was discussed, where things were left), ask the user to fill the gaps before proceeding — don't guess at facts.

### Step 2: Extract search-relevant entities
From the notes, pull out:
- Company/organization names mentioned (the prospect, their competitors, partners)
- Product lines, market segments, or technologies discussed
- Any explicit concerns, objections, or competitive comparisons raised by the other side
- Open questions or unresolved items that hinge on external facts (pricing, funding, market conditions)

### Step 3: Research
Formulate 3–6 targeted web searches from the entities above. Prioritize:
- Recent news (last 1–3 months) on the prospect and named competitors
- Funding, leadership changes, product launches, or market shifts relevant to the discussion
- Anything that would change the accuracy of a claim made in the meeting (e.g. if someone claimed "we're the only vendor doing X," verify that)

Do not skip this step or rely on background knowledge — the value of the memo is current information the meeting notes don't already contain.

### Step 4: Write the memo
Structure, in this order:

1. **Meeting Recap** — brief, factual. Who was there, what was discussed, where it was left. No market context here.
2. **Market Signals** — what's currently happening externally that's relevant. Cite what you found; don't editorialize yet.
3. **Implications** — explicitly connect Recap to Signals. For each significant market signal, state what it means for this specific deal/relationship. This is the section that makes it a memo and not two reports glued together.
4. **Recommended Actions** — concrete, short, ideally attributable (who should do what). Avoid vague advice like "stay competitive."

Keep it tight. This is a working memo, not a report — bullet points over paragraphs, no filler.

### Step 5: Produce the .docx
Read `/mnt/skills/public/docx/SKILL.md` and follow its process to generate a clean, professionally formatted Word document. Save to `/mnt/user-data/outputs/` and present it to the user with `present_files`.

## Notes
- One meeting per memo — if the user has multiple meetings, run this once per meeting rather than combining.
- If web search turns up nothing relevant for a given entity, say so in Market Signals rather than omitting silently — the user should know research was attempted.
