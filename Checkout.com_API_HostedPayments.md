# Checkout.com Hosted Payments Page

## Overview
Hosted Payments Page (HPP) is a secure, hosted payment solution that allows customers to complete payments on a Checkout.com hosted page. It supports multiple payment methods and provides a seamless checkout experience.

## Getting Started
- Register to use Hosted Payments Page by contacting your Solution Engineer or support.
- Create your secret and public API keys in the Dashboard.
- Set up webhooks to receive payment approval notifications.

## Creating a Hosted Payments Page Session

**Endpoint:**
```
POST https://api.checkout.com/hosted-payments
```

**Request Example:**
```json
{
  "amount": 1000,
  "currency": "GBP",
  "payment_type": "Regular",
  "billing": {
    "address": {
      "country": "GB"
    }
  },
  "reference": "ORD-123A",
  "customer": {
    "name": "Ali Farid",
    "email": "ali@example.com",
    "phone": {
      "country_code": "+44",
      "number": "79460000"
    }
  },
  "success_url": "https://example.com/payments/success",
  "failure_url": "https://example.com/payments/failure",
  "cancel_url": "https://example.com/payments/cancel"
}
```

## Redirecting Customers
After creating the session, redirect customers to the URL provided in `_links.redirect.href` to complete the payment.

## Hosted Payments Page Statuses
- **Payment Pending**: The page can accept payments.
- **Payment Received**: Payment successfully completed.
- **Expired**: The page is no longer accessible.

## Payment Method Field Requirements
Some payment methods require additional fields or specific values. Refer to the API reference for details.

Examples:
- Apple Pay requires supported currency and billing country.
- Alipay CN requires customer email or ID and product details.
- Klarna requires product list and customer name.

## Checking Hosted Payments Page Status

**Endpoint:**
```
GET https://api.checkout.com/hosted-payments/{id}
```

**Response Example:**
```json
{
  "id": "hpp_xGQBg0AXl3cM",
  "status": "Payment Pending",
  "payment_id": null,
  "amount": 200,
  "currency": "GBP",
  "reference": "ORD-123A",
  "description": "Payment for Gold Necklace",
  "expires_on": "2021-08-20T20:25:28+08:00",
  "customer": {
    "name": "John Smith",
    "email": "john@example.com"
  },
  "_links": {
    "self": {
      "href": "https://api.sandbox.checkout.com/hosted-payments/hpp_xGQBg0AXl3cM"
    },
    "redirect": {
      "href": "https://pay.sandbox.checkout.com/page/hpp_xGQBg0AXl3cM"
    }
  }
}
```

## Notes
- Hosted Payments Pages cannot be embedded within iframes.
- Use `http://localhost/` only for testing URLs, not in production.

---

*This document provides detailed guidance on creating and managing Hosted Payments Pages with Checkout.com.*
