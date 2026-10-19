## Summary

## Related issue

## Testing performed

- [ ] `ruff check . && ruff format --check .`
- [ ] `pytest -q`

## Checklist

- [ ] No secrets, credentials or real personal data (synthetic data only)
- [ ] New or changed tools are allowlisted, narrow, and validate inputs
- [ ] Write actions are gated behind human approval
- [ ] No new outbound network access or telemetry
- [ ] Security docs updated if the threat surface changed
