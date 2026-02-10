# Security Review

This project implements several Django security best practices:

- Enforces HTTPS using SECURE_SSL_REDIRECT
- Uses HSTS to force browsers to access the site via HTTPS
- Secure cookies for session and CSRF protection
- Prevents clickjacking with X_FRAME_OPTIONS
- Prevents MIME sniffing with SECURE_CONTENT_TYPE_NOSNIFF
- Enables browser XSS protection with SECURE_BROWSER_XSS_FILTER

These configurations protect against:
- Man-in-the-middle attacks
- Cross-site scripting (XSS)
- Clickjacking
- Session hijacking
