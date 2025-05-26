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
- Standardized response codes (10xxx to 50xxx) indicate request status.
- Common HTTP status codes include 200, 201, 401, 403, 404, 429, 500, etc.

## API Rate Limits and Idempotency
- Read and write operations limited to 100 RPS.
- Idempotency supported via `Cko-Idempotency-Key` header to prevent duplicate processing.

## Private Connections and API Changes
- Supports Mutual TLS (mTLS) and AWS PrivateLink for secure connections.
- Backward-compatible API changes are common; breaking changes are communicated in advance.

## Additional Features
- Supports Payment Links and Hosted Payments Page for flexible payment acceptance.
- Provides Identity Verification and Card Issuing services for compliance and card management.
- Offers comprehensive Payouts API for global fund transfers.

---

*This overview provides a high-level understanding of the Checkout.com API platform and its core features.*

*This overview provides a high-level understanding of the Checkout.com API platform and its core features.*
