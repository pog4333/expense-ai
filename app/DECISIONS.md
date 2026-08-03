# Architecture Decision Records

## ADR-001

Decision

Use uv.

Status

Accepted

Reason

- Modern Python workflow.
- Single tool replacing multiple utilities.
- Better reproducibility.
- Faster onboarding.
- Lock files improve reliability.

Alternatives

- pip
- venv
- poetry

Trade-offs

- Newer ecosystem.
- Requires learning a new CLI.

---

## ADR-002

Decision

Prefer deterministic solutions before AI.

Status

Accepted

Reason

- Easier testing.
- Lower cost.
- Faster.
- More reliable.

AI is introduced only when deterministic solutions become unreliable.

## ADR-003

Decision:
Adopt AI-assisted development as the default workflow.

Reason:
Modern AI engineers spend more time designing, reviewing, testing, and integrating than writing every line manually.

Trade-offs:
Developers must still understand the generated code and be able to debug, test, and maintain it.