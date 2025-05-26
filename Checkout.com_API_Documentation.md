# Checkout.com API Documentation

## Overview
Checkout.com provides a comprehensive payments platform with a suite of products and services including global payments network, payins and payouts, fraud detection, authentication, identity verification, card issuing, and more. The platform offers a unified API to connect and process payments seamlessly.

For a high-level overview of the platform and its core features, see [Checkout.com API Overview](Checkout.com_API_Overview.md).

## Products and Features
- **Connect**: Accept online payments via Unified Payments API, Hosted Payment Page, Mobile SDK, Payment Links, and Plugins.
- **Move**: Acquiring, Payment Methods, Issuing, Payouts.
- **Protect**: Fraud Detection, Authentication, Identity Verification, Disputes, Vault.
- **Boost**: Intelligent Acceptance, Network Tokens, Real-Time Account Updater.
- **Manage**: Dashboard, Treasury & FX.

## API Response Codes
Checkout.com uses standardized response codes to indicate the status of API requests:

- **10xxx**: Approved (successful requests)
- **20xxx**: Soft declines (declined but may succeed on retry)
- **30xxx**: Hard declines (require issuer/cardholder action)
- **4xxxx**: Risk responses (triggered by risk settings)
- **50xxx**: Card payout declines

Each response code includes a response text and additional information. For example, `10000` means Approved, `20005` means Declined - Do not honour, and `20051` means Insufficient funds.

## Overview
Checkout.com provides a comprehensive payments platform with a suite of products and services including global payments network, payins and payouts, fraud detection, authentication, identity verification, card issuing, and more. The platform offers a unified API to connect and process payments seamlessly.

For a high-level overview of the platform and its core features, see [Checkout.com API Overview](Checkout.com_API_Overview.md).

## Products and Features
- **Connect**: Accept online payments via Unified Payments API, Hosted Payment Page, Mobile SDK, Payment Links, and Plugins.
- **Move**: Acquiring, Payment Methods, Issuing, Payouts.
- **Protect**: Fraud Detection, Authentication, Identity Verification, Disputes, Vault.
- **Boost**: Intelligent Acceptance, Network Tokens, Real-Time Account Updater.
- **Manage**: Dashboard, Treasury & FX.

## API Response Codes
Checkout.com uses standardized response codes to indicate the status of API requests:

- **10xxx**: Approved (successful requests)
- **20xxx**: Soft declines (declined but may succeed on retry)
- **30xxx**: Hard declines (require issuer/cardholder action)
- **4xxxx**: Risk responses (triggered by risk settings)
- **50xxx**: Card payout declines

Each response code includes a response text and additional information. For example, `10000` means Approved, `20005` means Declined - Do not honour, and `20051` means Insufficient funds.

For more details, see [Payments API](Checkout.com_API_Payments.md#api-response-codes).

## HTTP Status Codes
Common HTTP status codes returned by the API include:
- `200 OK`
- `201 Created`
- `202 Accepted`
- `401 Unauthorized`
- `403 Not allowed`
- `404 Not found`
- `409 Conflict`
- `422 Invalid data`
- `429 Too many requests`
- `500 Internal server error`
- `502 Bad gateway`

For more information, see [Payments API](Checkout.com_API_Payments.md#http-status-codes).

## API Rate Limits
- Read operations (GET) are limited to 100 requests per second (RPS).
- Write operations (POST/PUT/DELETE) are limited to 100 RPS.
- Rate limits are applied at the account level across all APIs.
- When rate limits are exceeded, HTTP 429 is returned. Retry with incremental backoff and jitter is recommended.

See [API Overview](Checkout.com_API_Overview.md#api-rate-limits) for details.

## Idempotency
- Certain endpoints support idempotent requests to safely retry without duplicate processing.
- Use the `Cko-Idempotency-Key` HTTP header with a unique key (recommended V4 UUID).
- Idempotency keys expire after 24 hours by default.
- Concurrent requests with the same key result in one processed request and others returning HTTP 409 Conflict.

See [API Overview](Checkout.com_API_Overview.md#idempotency) for more.

## Private Connections
- Checkout.com supports private connections for enhanced security:
  - Mutual TLS (mTLS)
  - AWS PrivateLink
- Contact your account manager to enable private connections.

See [API Overview](Checkout.com_API_Overview.md#private-connections).

## API Changes
- Backward-compatible changes include adding optional request fields, new response fields, new headers, and new webhook event types.
- Breaking changes are communicated in advance to allow integration updates.

See [API Overview](Checkout.com_API_Overview.md#api-changes).

## Currency Codes and Amount Formatting
Checkout.com supports a wide range of currencies following the ISO 4217 standard. Each currency has a three-letter code, name, and associated country. Examples include USD, EUR, JPY, GBP, and AUD.

Amount formatting depends on the currency:
- Full amount for currencies like JPY.
- Amount divided by 1000 for currencies like BHD.
- Amount divided by 100 for most others like USD.

The amount must be greater than zero, contain no decimals, and not exceed 9 digits.

See [Payments API](Checkout.com_API_Payments.md#currency-codes-and-amount-formatting).

## Recurring Payments and Stored Card Details
- Store card details during the initial transaction by setting `"payment_type": "Installment"` or `"Recurring"` and `"merchant_initiated": false`.
- Enable 3D Secure (3DS) authentication in SCA regions by setting `"3ds.enabled": true` and `"3ds.challenge_indicator": "challenge_requested_mandate"`.
- Use stored card details for subsequent merchant-initiated transactions (MITs) by setting `"payment_type": "Installment"` or `"Recurring"`, `"merchant_initiated": true`, and providing `"previous_payment_id"`.
- MITs are exempt from SCA; 3DS can be disabled or omitted.

See [Payments API](Checkout.com_API_Payments.md#recurring-and-unscheduled-payments).

## Pay with Stored Card Details
- Customers can save card details during a transaction for future payments.
- Use `"store_for_future_use": true` to enable storing card details.
- For payments with stored cards, use the card's `"source.id"` instead of full card details.
- Enable 3D Secure authentication in SCA regions.
- The `"store_for_future_use"` flag signals the scheme to add the card.

See [Payments API](Checkout.com_API_Payments.md#stored-card-payments).

## Account Funding Transactions (AFT)
- AFTs pull funds from an account to fund non-merchant accounts (e.g., prepaid cards, wallets).
- To perform an AFT, set `"processing.aft": true` and provide `"recipient"` and `"sender"` information.
- Requirements vary by region and transaction category.
- Supported for Visa and Mastercard with specific data requirements.
- Contact your account manager to enable AFTs.

See [Payments API](Checkout.com_API_Payments.md#account-funding-transactions-aft).

## Regulatory Compliance for Financial Institutions
- Businesses categorized as financial institutions (MCC 6012) must provide additional recipient information for Europe domestic transactions.
- Required fields include date of birth, account number, postcode, and last name.
- Applies differently for Visa and Mastercard.
- Example request provided.

See [Payments API](Checkout.com_API_Payments.md#regulatory-compliance-for-financial-institutions).

## Scheduled Retries for Payments
- Configure automated retry schedules for recurring or unscheduled MITs that are soft declined.
- Supported decline response codes include 20005, 20051, 20061, and 20078.
- Retry schedules specify max attempts and retry duration with exponential backoff.
- Enable automatic downtime retries for network timeouts.
- Webhook notifications are sent for retry events.
- Custom retry schedules can be tested in sandbox environments.

See [Payments API](Checkout.com_API_Payments.md#scheduled-retries-for-payments).

## Fraud Detection and Risk Management
- Fraud Detection solution allows control over accepted payments to reduce fraud risk.
- Risk strategies include pre-auth and post-auth routing with rules, outcomes, and decline lists.
- Rules evaluate transaction data, contextual info, and statistical patterns.
- Decline lists block specific cards, IPs, emails, and phone numbers.
- Outcomes determine transaction handling based on risk level.
- Risk profiles score transactions and define decision thresholds.
- Machine learning models score transactions from 0 (low risk) to 100 (high risk).
- Metadata can be used in custom rules.
- Troubleshooting tips for common errors are provided.

See [Fraud Detection and Risk Management](Checkout.com_API_Fraud.md).

## Authentication and Authorization (OAuth 2.0)
Checkout.com uses OAuth 2.0 for API authentication and authorization, following the RFC 6749 standard.

### OAuth 2.0 Roles
- **Resource Owner**: Entity granting access to protected resources.
- **Client**: Application requesting access on behalf of the resource owner.
- **Authorization Server**: Issues access tokens after authenticating the resource owner.
- **Resource Server**: Hosts protected resources and validates access tokens.

### Authorization Flows
- **Authorization Code Grant**: Recommended for confidential clients; involves redirecting the user-agent to obtain an authorization code, then exchanging it for an access token.
- **Implicit Grant**: Optimized for public clients (e.g., browser-based apps); access token is issued directly without an authorization code.
- **Resource Owner Password Credentials Grant**: Suitable for trusted clients; uses resource owner credentials to obtain an access token.
- **Client Credentials Grant**: Used when the client accesses resources under its own control.

### Access Tokens
- Tokens represent authorization with specific scopes and lifetimes.
- Tokens must be kept confidential and transmitted over TLS.
- Refresh tokens may be issued to obtain new access tokens without reauthorization.

### Security Considerations
- Use TLS for all OAuth endpoints.
- Protect against CSRF, clickjacking, phishing, and token guessing attacks.
- Validate redirect URIs strictly to prevent open redirector vulnerabilities.
- Use the `state` parameter to prevent CSRF attacks.
- Avoid using implicit grant without additional security mechanisms.

See [Authentication and Authorization](Checkout.com_API_Authentication.md).

## Additional Resources
- [Checkout.com Dashboard](https://dashboard.checkout.com)
- [API Reference](https://docs.checkout.com/api-reference)
- [Test Account](https://docs.checkout.com/test-account)
- [Support](https://docs.checkout.com/support)

---

*This documentation is based on the parsed content of Checkout.com API reference pages and the OAuth 2.0 RFC 6749 standard.*
