# Checkout.com Flow Integration

## Overview
Flow is a pre-built, customizable payment user interface that can be embedded directly into your website or mobile app. It enables you to accept payments using Checkout.com's global network of payment methods with a single integration.

## Key Features
- Built-in support for 3D Secure (3DS)
- Input masking and validation
- Dynamic display of payment methods
- Add payment methods without additional development
- UI customization and responsive design
- Remember Me feature for saving card details across merchants

## Supported Payment Methods
- Card payments
- Apple Pay
- Google Pay
- Alipay CN & HK
- Alma
- Bancontact
- Benefit Payment Gateway
- Dana
- EPS
- GCash
- iDEAL
- Kakao Pay
- Klarna
- KNET
- MB WAY
- Multibanco
- PayPal (Pay Now and Pay Later)
- Przelewy24
- QPay
- SEPA Direct Debit
- stc pay
- Tabby
- Tamara
- Touch 'n Go
- TrueMoney
- Venmo

## Supported Browsers
- Google Chrome (desktop, Android, iOS)
- Safari (desktop, iOS)
- Mozilla Firefox (desktop)
- Microsoft Edge (desktop)

## Integration Steps

### 1. Create a Payment Session (Server-side)
Send a request to create a `PaymentSession` object containing all necessary payment flow information.

**Endpoint:**
```
POST https://api.checkout.com/payment-sessions
```

**Example Request:**
```json
{
  "amount": 1000,
  "currency": "GBP",
  "reference": "ORD-123A",
  "display_name": "Online shop",
  "billing": {
    "address": {
      "country": "GB"
    }
  },
  "customer": {
    "name": "Jia Tsang",
    "email": "jia@example.com"
  },
  "success_url": "https://example.com/payments/success",
  "failure_url": "https://example.com/payments/failure"
}
```

### 2. Initialize and Mount Flow (Client-side)
Use the `@checkout.com/checkout-web-components` package to create and mount the Flow component.

**Installation:**
```bash
npm install @checkout.com/checkout-web-components --save
```

**Mounting Flow:**
```javascript
import CheckoutWebComponents from '@checkout.com/checkout-web-components';

const checkout = await CheckoutWebComponents({
  publicKey: '{your_public_key}',
  environment: 'sandbox',
  locale: 'en-GB',
  paymentSession: paymentSessionData,
  onReady: () => console.log('Flow is ready'),
  onPaymentCompleted: (component, paymentResponse) => {
    console.log('Payment completed:', paymentResponse.id);
  },
  onError: (component, error) => {
    console.error('Payment error:', error);
  }
});

const flowComponent = checkout.create('flow');
flowComponent.mount('#flow-container');
```

### 3. Handle Payment Responses
- Asynchronous payments may redirect customers to success or failure URLs.
- Webhooks notify your server of payment status changes.
- Synchronous payments trigger `onPaymentCompleted` event.

## Flow Library Reference

### Methods
- `submit()`: Submit the FlowComponent (not available for digital wallets).
- `tokenize()`: Tokenize card payments, returns a Promise with tokenization result.
- `isValid()`: Check if all required details are captured.
- `isAvailable()`: Check if the component can be rendered.
- `mount(selector)`: Mount the component to a DOM element.
- `unmount()`: Unmount the component and remove lifecycle events.

### Events
- `onReady`: Raised when component is ready.
- `onChange`: Raised on customer interaction.
- `onSubmit`: Raised on submission.
- `onPaymentCompleted`: Raised on synchronous payment completion.
- `onError`: Raised on errors.
- `onCardBinChanged`: Raised when card BIN changes.
- `onTokenized`: Raised when card details are tokenized.

### Callbacks
- `handleClick`: Triggered when wallet payment button clicked.
- `handleSubmit`: Triggered on form submission.

## Example: Mounting Flow and Handling Events
```javascript
const flowComponent = checkout.create('flow', {
  onReady: () => console.log('Flow ready'),
  onChange: (component) => {
    if (component.isValid()) {
      submitButton.removeAttribute('disabled');
    } else {
      submitButton.setAttribute('disabled', true);
    }
  },
  onPaymentCompleted: async (_self, paymentResponse) => {
    await completeOrder(paymentResponse.id);
  },
  onError: (_self, error) => {
    if (error.code === 'payment_request_failed') {
      showErrorMessage('Payment could not be processed. Please try again.');
    }
  }
});

flowComponent.mount('#flow-container');
```

---

*This document provides detailed guidance on integrating and using the Checkout.com Flow payment UI.*
