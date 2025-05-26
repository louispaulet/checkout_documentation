# Checkout.com Identity Verification and Card Issuing

## Identity Verification

### Overview
Checkout.com provides Identity Verification services to help businesses verify the identity of their customers, comply with KYC and AML regulations, and reduce fraud.

### Key Features
- Create and manage applicants.
- Create and manage identity verifications.
- Create face authentications.
- Submit and retrieve verification attempts.
- Retrieve PDF reports of verifications.
- Anonymize identity verification data.

### Example: Create an Applicant
```json
POST /applicants
{
  "external_applicant_id": "ext_123456",
  "email": "john.doe@example.com"
}
```

### Example: Create an Identity Verification
```json
POST /identity-verifications
{
  "applicant_id": "aplt_123456",
  "declared_data": {
    "name": "John Doe"
  },
  "redirect_url": "https://example.com/verification-complete"
}
```

### Example: Create a Face Authentication
```json
POST /face-authentications
{
  "user_journey_id": "usj_123456",
  "applicant_id": "aplt_123456"
}
```

## Card Issuing

### Overview
Checkout.com offers card issuing capabilities to create and manage physical and virtual cards, cardholders, controls, and cardholder access tokens.

### Key Features
- Create and manage cardholders.
- Issue physical and virtual cards.
- Manage card controls and control profiles.
- Enroll cards in 3D Secure (3DS).
- Activate, suspend, revoke, renew, and schedule revocation of cards.
- Retrieve card credentials securely.
- Simulate card transactions for testing.
- Manage card disputes.

### Example: Create a Cardholder
```bash
curl https://api.checkout.com/issuing/cardholders \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "individual",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "date_of_birth": "1985-05-15",
    "billing_address": {
      "address_line1": "123 Main St",
      "city": "London",
      "country": "GB"
    }
  }'
```

### Example: Issue a Virtual Card
```bash
curl https://api.checkout.com/issuing/cards \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "virtual",
    "cardholder_id": "crh_123456",
    "card_product_id": "pro_123456",
    "lifetime": {
      "unit": "Months",
      "value": 12
    },
    "display_name": "John\'s Virtual Card"
  }'
```

### Example: Enroll Card in 3DS
```bash
curl https://api.checkout.com/issuing/cards/{cardId}/3ds-enrollment \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "security_pair": {
      "question": "What is your pet\'s name?",
      "answer": "Fluffy"
    },
    "phone_number": {
      "country_code": "+1",
      "number": "4155552671"
    },
    "locale": "en-US"
  }'
```

---

*This document provides detailed guidance on Identity Verification and Card Issuing features of Checkout.com.*
