# Risk-based Authentication Simulation

This is a demonstration of how a risk-based authentication model can be structured using basic business rules.

The goal is not to build an entire production security engine, but to show how risk logic can be translated into technical implementation.

---

## Business Context

Traditional authentication relies on passwords alone, while modern systems use risk scoring to determine when additional verification (such as MFA) must be triggered.

This simulation assigns risk scores based on:

- Failed login attempts
- Geographical mismatch
- Unusual login time

---

## How this works

Each login attempt is evaluated against predefined rules.

If the risk score exceeds a threshold, additional verification would be required.

---

## Why this matters

Risk-based authentication:
- Improves user experience
- Reduces unnecessary MFA friction
- Focuses controls where risk is highest
