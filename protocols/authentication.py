# 💀 AUTHENTICATION LOGIC
import hmac, hashlib
def verify_signature(data, signature, secret):
    expected = hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
