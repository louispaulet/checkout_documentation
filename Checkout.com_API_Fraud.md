# Checkout.com Fraud Detection and Risk Management

## Overview
Checkout.com's Fraud Detection solution helps merchants control the types of payments accepted to reduce fraud risk. It provides configurable risk strategies, rules, decline lists, and outcomes to manage transaction risk effectively.

## Risk Strategies
- **Pre-auth**: Applied before payment authorization.
- **Post-auth**: Applied after payment authorization.

## Rules
- Rules are expressions that evaluate transaction data and return true or false.
- Examples:
  - Transaction amount over 100 USD.
  - Billing address is valid.
  - Same card used more than 3 times in the last hour.

## Rule Categories
- **Address Verification Service (AVS)**: Verifies billing address with issuer.
- **Decline List Management**: Blocklists for cards, IPs, emails, phone numbers.
- **High-risk Countries**: Custom list of countries with higher fraud risk.
- **Machine-learning Score**: Scores transactions 0-100 based on fraud risk.
- **Mismatch**: Detects mismatches in transaction details.
- **Threshold**: Triggers actions based on transaction value.
- **Velocity**: Triggers based on frequency of transactions.
- **Verified Information**: Validates customer data like email and address.

## Decline Lists vs Decline Rules
- Decline lists block specific attributes immediately.
- Decline rules are formulas that determine outcomes based on conditions.

## Outcomes
- **Accept**: Low risk transactions.
- **Decline**: High risk transactions.
- **3DS Frictionless**: Medium risk, no customer challenge.
- **3DS Challenge**: High risk, customer must authenticate.
- **Void**: Post-auth high risk.
- **Flag**: Post-auth medium risk.
- **Capture**: Post-auth low risk.

## Risk Profiles (Pro Only)
- Collections of rules with scoring and decision thresholds.
- Scores range from 0 (low risk) to 100 (high risk).
- Define outcomes based on score bands.

## Machine Learning Threshold
- Default threshold is 70; transactions scoring above are high risk.
- Custom thresholds can be set.

## Metadata in Rules
- Custom fields can be added to payment requests and used in rules.
- Metadata keys and values are case-insensitive.

## Troubleshooting
- Be cautious with NULL values in rules.
- Understand case sensitivity in comparisons.
- Use EXISTS and IS_MISSING operators for NULL checks.

---

*This document provides comprehensive guidance on configuring and managing fraud detection with Checkout.com.*
