# Checkout.com API Developer Cookbook

This developer cookbook provides practical examples, usage patterns, and best practices for integrating with the [Checkout.com API](https://api-reference.checkout.com/).

---

## Table of Contents

1. [Introduction](#introduction)  
2. [Authentication](#authentication)  
3. [Making API Requests](#making-api-requests)  
4. [Payments](#payments)  
5. [Refunds](#refunds)  
6. [Customers](#customers)  
7. [Error Handling](#error-handling)  
8. [Best Practices](#best-practices)  
9. [Code Samples](#code-samples)  

---

## Introduction

Checkout.com provides a comprehensive API for processing payments, managing customers, and handling refunds. This cookbook will guide you through common tasks and provide example requests and responses.

---

## Authentication

All API requests require authentication using your secret API key. Include the key in the `Authorization` header as a Bearer token.

**Example:**

```
Authorization: Bearer sk_test_your_secret_key
```

---

## Making API Requests

- Base URL: `https://api.checkout.com`
- Content-Type: `application/json`
- Use HTTPS for all requests.

---

## Payments

### Create a Payment

**Endpoint:** `POST /payments`

**Request Example:**

```json
{
  "source": {
    "type": "card",
    "number": "4242424242424242",
    "expiry_month": 6,
    "expiry_year": 2025,
    "cvv": "100"
  },
  "amount": 1000,
  "currency": "USD",
  "reference": "ORD-12345",
  "capture": true
}
```

**Curl Example:**

```bash
curl https://api.checkout.com/payments \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "source": {
      "type": "card",
      "number": "4242424242424242",
      "expiry_month": 6,
      "expiry_year": 2025,
      "cvv": "100"
    },
    "amount": 1000,
    "currency": "USD",
    "reference": "ORD-12345",
    "capture": true
  }'
```

### Payment Flows

Checkout.com supports multiple payment flows:

- **Authorize and Capture:** Authorize a payment first, then capture it later.
- **Authorize Only:** Authorize a payment without capturing immediately.
- **Capture:** Capture a previously authorized payment.
- **Void:** Cancel an authorized payment before capture.

**Example: Authorize a Payment**

```json
{
  "source": {
    "type": "card",
    "number": "4242424242424242",
    "expiry_month": 6,
    "expiry_year": 2025,
    "cvv": "100"
  },
  "amount": 1000,
  "currency": "USD",
  "capture": false
}
```

**Capture a Payment**

**Endpoint:** `POST /payments/{payment_id}/captures`

```json
{
  "amount": 1000
}
```

---

## Webhooks

Checkout.com supports webhooks to notify your system about payment events such as successful payments, refunds, and chargebacks.

- Configure webhook endpoints in your dashboard.
- Validate webhook signatures to ensure authenticity.
- Handle events idempotently to avoid duplicate processing.

---

## Idempotency

Use idempotency keys in the `Idempotency-Key` header to safely retry requests without creating duplicate transactions.

**Example:**

```
Idempotency-Key: your-unique-key-123
```

---

## Pagination and Filtering

Many list endpoints support pagination and filtering via query parameters:

- `limit`: Number of items per page.
- `starting_after` / `ending_before`: Cursor-based pagination.
- Filter by status, date, or other fields.

---


---

## Refunds

### Create a Refund

**Endpoint:** `POST /payments/{payment_id}/refunds`

**Request Example:**

```json
{
  "amount": 500
}
```

---

## Customers

### Create a Customer

**Endpoint:** `POST /customers`

**Request Example:**

```json
{
  "email": "customer@example.com",
  "name": "John Doe"
}
```

---

## Error Handling

- API errors return appropriate HTTP status codes.
- The response body contains error details.

**Example:**

```json
{
  "error_type": "invalid_request_error",
  "error_codes": ["invalid_number"],
  "error_message": "The card number is invalid."
}
```

---

## Best Practices

- Always validate input before sending requests.
- Use idempotency keys to avoid duplicate charges.
- Securely store your API keys.
- Handle errors gracefully and log them for troubleshooting.

---

## Code Samples

### JavaScript (Node.js) Example Using `fetch`

```javascript
const fetch = require('node-fetch');

async function createPayment() {
  const response = await fetch('https://api.checkout.com/payments', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer sk_test_your_secret_key',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      source: {
        type: 'card',
        number: '4242424242424242',
        expiry_month: 6,
        expiry_year: 2025,
        cvv: '100'
      },
      amount: 1000,
      currency: 'USD',
      reference: 'ORD-12345',
      capture: true
    })
  });

  const data = await response.json();
  console.log(data);
}

createPayment();
```

---

This cookbook is a starting point. For full API details, refer to the official [Checkout.com API Reference](https://api-reference.checkout.com/).

---

## Additional API Reference Highlights from Online Documentation

### Authentication

- Supports API keys (public and secret) and OAuth 2.0.
- Use `Authorization: Bearer <token>` header for authenticated requests.
- OAuth token endpoint: `https://access.checkout.com/connect/token`

### Payments

- Create payments, capture, void, refund, and search payments.
- Supports multiple payment flows: authorize & capture, authorize only, capture later, void.
- SDKs available for Go, .NET, Java, Node.js, and more.

### Webhooks

- Configure webhook endpoints to receive event notifications.
- Validate webhook signatures.
- Handle events idempotently.

### Customers

- Create, update, retrieve, and delete customer records.
- Manage customer payment instruments.

### Disputes

- Retrieve disputes, submit evidence, accept disputes, escalate, and more.
- SDK support for dispute management.

### Workflows

- Automate payment and business logic workflows.
- Manage workflows, actions, conditions, and events.

### Platforms

- Onboard entities, manage sub-entities, and handle payouts.

### Other Features

- Hosted Payments Page, Payment Links, Forex rates, Apple Pay integration.
- Reporting APIs for transaction and financial reports.
- Cardholder and card management.
- Controls and control profiles for risk management.

### Code Samples

- Extensive code samples in multiple languages are available in the official docs.
- Use SDKs for easier integration and error handling.

---

This enhanced cookbook is based on the official online API reference content and provides a practical guide for developers integrating with Checkout.com.
