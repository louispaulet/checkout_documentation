# Checkout.com API Authentication and Authorization

## Overview
Checkout.com uses OAuth 2.0 for API authentication and authorization, following the RFC 6749 standard. This ensures secure access to protected resources and APIs.

## OAuth 2.0 Roles
- **Resource Owner**: Entity granting access to protected resources.
- **Client**: Application requesting access on behalf of the resource owner.
- **Authorization Server**: Issues access tokens after authenticating the resource owner.
- **Resource Server**: Hosts protected resources and validates access tokens.

## Authorization Flows
### Authorization Code Grant
- Recommended for confidential clients.
- Involves redirecting the user-agent to obtain an authorization code.
- The code is exchanged for an access token.

### Implicit Grant
- Optimized for public clients (e.g., browser-based apps).
- Access token is issued directly without an authorization code.
- Does not support refresh tokens.

### Resource Owner Password Credentials Grant
- Suitable for trusted clients.
- Uses resource owner credentials to obtain an access token.
- Should be minimized due to security risks.

### Client Credentials Grant
- Used when the client accesses resources under its own control.
- No user involvement required.

## Access Tokens
- Represent authorization with specific scopes and lifetimes.
- Must be kept confidential and transmitted over TLS.
- Refresh tokens may be issued to obtain new access tokens without reauthorization.

## Security Considerations
- Use TLS for all OAuth endpoints.
- Protect against CSRF, clickjacking, phishing, and token guessing attacks.
- Validate redirect URIs strictly to prevent open redirector vulnerabilities.
- Use the `state` parameter to prevent CSRF attacks.
- Avoid using implicit grant without additional security mechanisms.

## Example: Authorization Code Grant Flow

### Step 1: Redirect User to Authorization Endpoint
```
GET /authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&scope=read&state=xyz HTTP/1.1
Host: authorization-server.com
```

### Step 2: Receive Authorization Code
```
HTTP/1.1 302 Found
Location: YOUR_REDIRECT_URI?code=AUTH_CODE&state=xyz
```

### Step 3: Exchange Authorization Code for Access Token
```
POST /token HTTP/1.1
Host: authorization-server.com
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=AUTH_CODE&redirect_uri=YOUR_REDIRECT_URI&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET
```

### Step 4: Receive Access Token Response
```json
{
  "access_token": "ACCESS_TOKEN",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "REFRESH_TOKEN",
  "scope": "read"
}
```

---

*This document provides detailed guidance on authenticating and authorizing API requests using OAuth 2.0 with Checkout.com.*
