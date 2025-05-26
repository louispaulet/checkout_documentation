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

For a high-level overview, see [Checkout.com API Overview](Checkout.com_API_Overview.md).

---

## Authentication

All API requests require authentication using your secret API key or OAuth 2.0 tokens. Include the key in the `Authorization` header as a Bearer token.

**Example: Using API Key**

```
Authorization: Bearer sk_test_your_secret_key
```

For OAuth 2.0 authentication details, see [Authentication and Authorization](Checkout.com_API_Authentication.md).

---

## Making API Requests

- Base URL: `https://api.checkout.com`
- Content-Type: `application/json`
- Use HTTPS for all requests.
- Use idempotency keys to safely retry requests without duplicates (see [API Overview](Checkout.com_API_Overview.md#idempotency)).

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

For more payment options and details, see [Payments API](Checkout.com_API_Payments.md).

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
- Use the [Fraud Detection and Risk Management](Checkout.com_API_Fraud.md) features to reduce fraud risk.

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

For more code examples and integration guides, see [Flow Integration](Checkout.com_API_Flow.md).

---

This cookbook is a starting point. For full API details, refer to the official [Checkout.com API Reference](https://api-reference.checkout.com/).

---
