# Decision Notes template

Fill this shape exactly. Use **section headings and all narrative text in the criteria pack `locale`** (see locale label map below). Keep checklist `result` codes machine-stable: `pass` | `fail` | `insufficient_data` | `not_applicable` | `skipped` (`skipped` = not evaluated after hard-fail short-circuit).

## Locale label map

| key | `id` | `en` |
|---|---|---|
| title | Catatan Keputusan | Decision Notes |
| summary | Ringkasan | Summary |
| checklist | Checklist kriteria | Criteria checklist |
| strengths | Kekuatan | Strengths |
| weaknesses | Kelemahan / Risiko | Weaknesses / Risks |
| data_gaps | Kesenjangan data | Data gaps |
| suggestion | Saran keputusan | Suggestion |
| next_action | Langkah berikutnya | Next action |
| confidence | Keyakinan | Confidence |
| criterion | Kriteria | Criterion |
| result | Hasil | Result |
| evidence | Bukti | Evidence |

### Suggestion labels

| code | `id` | `en` |
|---|---|---|
| approve | Setujui | Approve |
| reject | Tolak | Reject |
| request_more_info | Minta data tambahan | Request more info |
| escalate | Eskalasi | Escalate |

### Confidence labels

| code | `id` | `en` |
|---|---|---|
| high | Tinggi | High |
| medium | Sedang | Medium |
| low | Rendah | Low |

### Result codes

| code | `id` (evidence hint) | meaning |
|---|---|---|
| pass | — | Criterion satisfied |
| fail | — | Criterion violated |
| insufficient_data | — | Needed facts missing |
| not_applicable | — | Criterion does not apply |
| skipped | dihentikan setelah hard fail | Not evaluated (`stop_on_hard_fail`) |

---

## Output shape

```markdown
# {title} — {reference_code}

**Context:** {danacita|bukas} | {product_or_status_if_known}
**Pack:** `{pack.id}` v{pack.version} | locale={pack.locale}
**{suggestion}:** {localized suggestion label} (`{suggestion_code}`)
**{confidence}:** {localized confidence label} (`{high|medium|low}`)

## {summary}
{1–3 sentences in pack locale}

## {checklist}
| {criterion} | {result} | {evidence} |
|---|---|---|
| {criterion.prompt} | pass\|fail\|insufficient_data\|not_applicable\|skipped | {short evidence in pack locale} |

## {strengths}
- ...

## {weaknesses}
- ...

## {data_gaps}
- ...

## {next_action}
{Human decides. Do not change application status from this skill.}
```
