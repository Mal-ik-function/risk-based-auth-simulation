# Authentication Risk Requirements

## Functional Requirements

1. The system shall evaluate login attempts in real time.
2. The system shall assign a risk score based on predefined rules.
3. The system shall trigger MFA when risk exceeds the threshold.

## Non-Functional Requirements

- Risk calculation must complete within 200ms.
- Rules must be configurable.
- Risk scoring logic must be auditable.
