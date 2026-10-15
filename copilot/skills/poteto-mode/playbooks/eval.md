### Eval

**You own the experiment design. Plan, blind, run, synthesize.**

**Non-negotiables for blinding:**

- No `eval`, `test`, `judge`, `experiment`, `rubric`, `score`, `compare`, `benchmark`, `candidate`, or `arena` in any directory, file, or prompt the candidate sees.
- The candidate prompt looks like an organic user request. State the goal, not the meta.
- No chain-eliciting cues. Don't ask the candidate to list which skills, principles, or files they applied. Ask for design notes generally and grade chain-following from code shape, not self-report.
- Sanitize directory and slug names. Use project-shaped names a user might pick.
- Don't tell the candidate other candidates exist.
- The judge can know it's judging but sees outputs by sanitized label only, never by model name.
- Comparing two variants: one judge scores both sets in a single pass on one scale, blind to which set each came from.

**Steps:**

1. **Frame.** State what variant is under test and what behavior counts as success. Write the rubric (3-6 concrete criteria) for the judge only. Hold it back from candidates.
2. **Set up sanitized environments.** Per-candidate working dir with the variant in place. Plant any context an organic task would have: a project skeleton, the skills the candidate would naturally read.
3. **Author one organic prompt.** What a user would type. No leakage of what's being measured.
4. **Run N isolated candidates**, sequentially by default, with the same organic prompt and sanitized environments. Use distinct supported invocations only when the host actually offers them. Never claim independent contexts, different models, or a blind comparison from one contaminated session. If isolation is unavailable, label this a non-blind rehearsal rather than a valid eval.
5. **Use one blinded judge** with outputs labeled anonymously and the rubric. Prefer an actually available different model family, selected explicitly through the host. If no independent judge is available, report the missing gate instead of fabricating it.
6. **Verify from authorized run records, not self-report.** Use explicit transcript exports or artifacts for these runs only. Do not assume an `agent-transcripts/` directory or discover private application caches. Look at which files candidates actually opened and the code shape. If records are absent, mark chain-following unverified.
7. **Read every candidate output yourself** end to end. Compare to the judge's verdict. Disagreement means a model is biased or the rubric is ambiguous. Synthesize.

**Reply:** variant under test, rubric, per-candidate notes, judge's verdict, your synthesis, and a recommendation for whether to promote the variant.
