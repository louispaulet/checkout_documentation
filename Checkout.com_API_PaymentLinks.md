# Checkout.com Payment Links

## Overview
Payment Links allow you to create a payment session that can be sent to customers via email, SMS, social media, or any preferred channel. Customers complete their payment on a hosted page and are redirected to a confirmation page upon completion.

## Getting Started
- Register to use Payment Links by contacting your Solution Engineer or support.
- Create your secret and public API keys in the Dashboard.
- Set up webhooks to receive payment approval notifications.

## Creating a Payment Link

### Step 1: Create a Payment Link Session

**Endpoint:**
```
POST https://api.checkout.com/payment-links
```

**Request Example:**
```json
{
  "amount": 1000,
  "currency": "GBP",
  "reference": "ORD-123A",
  "billing": {
    "address": {
      "country": "GB"
    }
  },
  "customer": {
    "name": "Ali Farid",
    "email": "ali@example.com",
    "phone": {
      "country_code": "+44",
      "number": "79460000"
    }
  },
  "return_url": "https://example.com/payments/return"
}
```

### Step 2: Send the Link to Your Customer
Retrieve the Payment Link URL from `_links.redirect.href` in the response and send it to your customer via their preferred communication channel.

## Payment Link Statuses
- **Active**: Link can accept payments.
- **Payment Received**: Payment successfully completed.
- **Expired**: Link is no longer accessible.

## Payment Method Field Requirements
Some payment methods require additional fields or specific values. Refer to the API reference for details.

Examples:
- Apple Pay requires supported currency and billing country.
- Alipay CN requires customer email or ID and product details.
- Klarna requires product list and customer name.

## Checking Payment Link Status

**Endpoint:**
```
GET https://api.checkout.com/payment-links/{id}
```

**Response Example:**
```json
{
  "id": "pl_ELqQJXdXzabU",
  "status": "Active",
  "payment_id": "pay_mbabizu24mvu3mela5njyhpit4",
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
      "href": "https://api.sandbox.checkout.com/payment-links/pl_ELqQJXdXzabU"
    },
    "redirect": {
      "href": "https://pay.sandbox.checkout.com/link/pl_ELqQJXdXzabU"
    },
    "payment": {
      "href": "https://api.sandbox.checkout.com/payments/pay_mbabizu24mvu3mela5njyhpit4"
    }
  }
}
```

## Notes
- Payment Links cannot be embedded within iframes.
- Use `http://localhost/` only for testing URLs, not in production.

---

*This document provides detailed guidance on creating and managing Payment Links with Checkout.com.*
