# HTTPS Deployment Configuration

To serve this Django application securely over HTTPS, the web server (e.g., Nginx or Apache) must be configured with SSL/TLS certificates.

## Example Nginx Configuration

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}
