FEATURE_EMBEDDED_SUPERSET = True

ALLOWED_FRAME_ANCESTORS = [
    "http://localhost:*",
    "https://localhost:*",
    "http://127.0.0.1:*",
    "https://127.0.0.1:*",
]

# This dictionary can override or add HTTP headers on all responses
OVERRIDE_HTTP_HEADERS = {
    "X-Frame-Options": "ALLOWALL",  # or "ALLOW-FROM http://localhost:3000" in older browsers
}

PUBLIC_ROLE_LIKE = "Gamma"

TALISMAN_ENABLED = False