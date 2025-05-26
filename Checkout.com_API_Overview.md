# Checkout.com API Overview

## Introduction
Checkout.com offers a unified payments platform that enables businesses to accept and manage payments globally. The platform includes a wide range of products and services such as payment processing, fraud detection, identity verification, card issuing, and more.

## Key Products and Features
- **Connect**: Unified Payments API, Hosted Payment Page, Mobile SDK, Payment Links, Plugins.
- **Move**: Acquiring, Payment Methods, Issuing, Payouts.
- **Protect**: Fraud Detection, Authentication, Identity Verification, Disputes, Vault.
- **Boost**: Intelligent Acceptance, Network Tokens, Real-Time Account Updater.
- **Manage**: Dashboard, Treasury & FX.

## API Response and Status Codes
- Standardized response codes (10xxx to 50xxx) indicate request status. See [Payments API - Response Codes](Checkout.com_API_Payments.md#api-response-codes).
- Common HTTP status codes include 200, 201, 401, 403, 404, 429, 500, etc. See [Payments API - HTTP Status Codes](Checkout.com_API_Payments.md#http-status-codes).

## API Rate Limits and Idempotency
- Read and write operations limited to 100 RPS. See [API Overview - Rate Limits](Checkout.com_API_Overview.md#api-rate-limits).
- Idempotency supported via `Cko-Idempotency-Key` header to prevent duplicate processing. See [API Overview - Idempotency](Checkout.com_API_Overview.md#idempotency).

## Private Connections and API Changes
- Supports Mutual TLS (mTLS) and AWS PrivateLink for secure connections. See [API Overview - Private Connections](Checkout.com_API_Overview.md#private-connections).
- Backward-compatible API changes are common; breaking changes are communicated in advance. See [API Overview - API Changes](Checkout.com_API_Overview.md#api-changes).

## Additional Features
- Supports [Payment Links](Checkout.com_API_PaymentLinks.md) and [Hosted Payments Page](Checkout.com_API_HostedPayments.md) for flexible payment acceptance.
- Provides [Identity Verification and Card Issuing](Checkout.com_API_IdentityVerification_Issuing.md) services for compliance and card management.
- Offers comprehensive [Payouts API](Checkout.com_API_Payouts.md) for global fund transfers.
- Includes [Fraud Detection and Risk Management](Checkout.com_API_Fraud.md) to reduce payment fraud.
- Uses [OAuth 2.0 Authentication and Authorization](Checkout.com_API_Authentication.md) for secure API access.
- Integrates with [Flow](Checkout.com_API_Flow.md), a customizable payment UI for seamless checkout experiences.

---

*This overview provides a high-level understanding of the Checkout.com API platform and its core features.*
