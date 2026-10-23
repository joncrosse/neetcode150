# Practice Notes

Shared progress log for NeetCode 150 / LeetCode prep. Both Jon and Claude edit this file.
Commit and push after each session so it stays in sync across computers and web sessions.

## Problems

| Problem | Pattern | Status | Time / Space | Date | Notes |
|---|---|---|---|---|---|
| Contains Duplicate | Arrays & Hashing | Solved with hints | O(n) / O(n) | 2026-10-23 | Brute force double loop is O(n²). Track seen values in a set for average O(1) lookups. Came up with the "have I seen it?" idea and picked a set on my own; Claude's questions led to the bottleneck and the list-vs-set lookup cost. |

Status: In progress · Solved · Solved with hints · Revisit

## Patterns

How confident I am with each technique, and what to remember about it.

| Pattern | Confidence | Key takeaways |
|---|---|---|
| Arrays & Hashing | Medium | Use a set for "have I seen this?" checks: average O(1) lookups, but O(n) extra space. `x in list` is O(n). |
| Two Pointers | | |
| Sliding Window | | |
| Stack | | |
| Binary Search | | |
| Linked List | | |
| Trees | | |
| Heap / Priority Queue | | |
| Backtracking | | |
| Graphs (BFS/DFS) | | |
| Dynamic Programming | | |
| SQL | | |

Confidence: Low · Medium · High

## Review List

Problems or concepts to come back to.

- Cost of membership checks: `in` on a list vs. a set vs. a dict, and why set lookups are only O(1) on average.
- Contains Duplicate: know the alternative approaches (sorting, `len(set(...))`) and their tradeoffs.

## Session Log

Newest first. What was worked on, what clicked, what to do next.

### 2026-10-23
- Set up mentor mode (CLAUDE.md) and this notes file.
- Reset containsDuplicate.py (old solution from ~3 years ago) to a fresh stub to redo from scratch.
- Solved Contains Duplicate: worked from the O(n²) brute force to a set-based O(n) solution.
- Turned off inline/Copilot suggestions for Python in this repo (.vscode/settings.json).
- Next: answer the interview follow-ups on Contains Duplicate, then move on to Valid Anagram.
