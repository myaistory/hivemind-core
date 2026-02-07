import nacl.signing
import nacl.encoding
# Actual Cryptographic Verification Logic
def verify_identity(pubkey_hex, msg, sig_hex):
    try:
        vk = nacl.signing.VerifyKey(pubkey_hex, encoder=nacl.encoding.HexEncoder)
        vk.verify(msg.encode(), bytes.fromhex(sig_hex))
        return True
    except: return False
