# Checkout.com Payouts API

## Overview
The Payouts API allows you to send funds to bank accounts or cards globally. It supports various payout types including bank payouts and card payouts, with detailed formatting requirements per country.

## Bank Payouts

### Payout Formatting
- Use the `get bank account field formatting` endpoint to retrieve required formatting for bank accounts based on country and currency.
- Different countries have specific requirements for beneficiary information, bank details, and account types.
- Supported countries include Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Monaco, Netherlands, Norway, Poland, Portugal, Romania, San Marino, Slovakia, Slovenia, Spain, Sweden, Switzerland, United Kingdom, United States, and more.

### Example: Bank Payout Request (Austria)
```bash
curl https://api.checkout.com/payouts \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "source": {
      "type": "currency_account",
      "id": "ca_pt5kvurrlmrube2crzaqdhqbdm"
    },
    "amount": 10,
    "destination": {
      "type": "bank_account",
      "account_type": "current",
      "iban": "AT611904300234573201",
      "country": "AT",
      "account_holder": {
        "type": "individual",
        "first_name": "John",
        "last_name": "Smith",
        "billing_address": {
          "address_line1": "123 Example St.",
          "city": "Vienna",
          "zip": "1010",
          "country": "AT"
        }
      }
    },
    "currency": "EUR",
    "reference": "Payouts - AT Testing",
    "billing_descriptor": {
      "reference": "CKO - payouts - AT Testing"
    },
    "instruction": {
      "purpose": "Payouts - sbox Testing"
    },
    "processing_channel_id": "pc_ru45af4clzpeffww6fd5bqlvje"
  }'
```

## Card Payouts
- Supports sending funds directly to cards.
- Requires card details and appropriate authorization.

## Additional Features
- Retrieve payout schedules for sub-entities.
- Manage reserve rules for sub-entities.
- Create and manage payment instruments for payouts.

## Related Endpoints
- `GET /validation/bank-accounts/{country}/{currency}`: Retrieve bank account field formatting.
- `POST /payouts`: Initiate a payout.
- `GET /payouts/{id}`: Retrieve payout details.
- `GET /accounts/entities/{id}/payout-schedules`: Retrieve payout schedules.
- `POST /accounts/entities/{id}/reserve-rules`: Create reserve rules.

---

*This document provides detailed guidance on managing payouts with the Checkout.com API.*
