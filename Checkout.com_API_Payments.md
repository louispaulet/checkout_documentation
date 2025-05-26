# Checkout.com Payments API

## Currency Codes and Amount Formatting
- Supports ISO 4217 currency codes (e.g., USD, EUR, JPY, GBP).
- Amount formatting varies by currency:
  - Full amount for currencies like JPY.
  - Amount divided by 1000 for currencies like BHD.
  - Amount divided by 100 for most others like USD.
- Amount must be greater than zero, no decimals, max 9 digits.

## Payment Types
- **Regular**: Standard payments.
- **Installment**: Payments in parts.
- **Recurring**: Scheduled repeat payments.
- **Unscheduled**: Payments without fixed schedule.
- **Merchant-Initiated Transactions (MITs)**: Subsequent payments using stored card details.

## Stored Card Payments
- Store card details during initial transaction with `"store_for_future_use": true`.
- Use stored card's `"source.id"` for future payments.
- Enable 3D Secure (3DS) in SCA regions.

## Recurring and Unscheduled Payments
- Initial transaction must specify `"payment_type": "Installment"` or `"Recurring"` and `"merchant_initiated": false`.
- Subsequent MITs set `"merchant_initiated": true` and provide `"previous_payment_id"`.
- MITs are exempt from SCA; 3DS can be disabled or omitted.

## Account Funding Transactions (AFT)
- AFTs pull funds from an account to fund non-merchant accounts (e.g., prepaid cards, wallets).
- Set `"processing.aft": true` and provide `"recipient"` and `"sender"` information.
- Requirements vary by region and transaction category.
- Supported for Visa and Mastercard with specific data requirements.
- Contact your account manager to enable AFTs.

## Scheduled Retries for Payments
- Configure automated retry schedules for recurring or unscheduled MITs that are soft declined.
- Supported decline response codes: 20005, 20051, 20061, 20078.
- Retry schedules specify max attempts and retry duration with exponential backoff.
- Enable automatic downtime retries for network timeouts.
- Webhook notifications sent for retry events.
- Custom retry schedules can be tested in sandbox.

## Code Examples

### Example: Create a Recurring Payment with Stored Card
```bash
curl https://api.checkout.com/payments \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "source": {
      "type": "card",
      "number": "4242424242424242",
      "expiry_month": 10,
      "expiry_year": 2026,
      "store_for_future_use": true
    },
    "amount": 5000,
    "currency": "USD",
    "payment_type": "Recurring",
    "merchant_initiated": false,
    "3ds": {
      "enabled": true,
      "challenge_indicator": "challenge_requested_mandate"
    }
  }'
```

### Example: Subsequent Merchant-Initiated Transaction (MIT)
```bash
curl https://api.checkout.com/payments \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "source": {
      "type": "card",
      "stored": true
    },
    "amount": 5000,
    "currency": "USD",
    "payment_type": "Recurring",
    "merchant_initiated": true,
    "previous_payment_id": "pay_123456789"
  }'
```

### Example: Configure Retry Schedule
```bash
curl https://api.checkout.com/payments \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "source": {
      "type": "card",
      "number": "4242424242424242",
      "expiry_month": 12,
      "expiry_year": 2029,
      "cvv": "422"
    },
    "amount": 100,
    "currency": "GBP",
    "capture": false,
    "merchant_initiated": true,
    "payment_type": "Recurring",
    "retry": {
      "dunning": {
        "enabled": true,
        "end_after_days": 21,
        "max_attempts": 4
      }
    }
  }'
```

---

*This document provides detailed guidance on payments processing with the Checkout.com API.*
