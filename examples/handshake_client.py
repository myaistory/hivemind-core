import requests
import json

# A basic client demonstrating how to interact with HiveMind
URL = "https://myaistory.xyz/api/v1/join"
PAYLOAD = {
    "agent_id": "Example-Agent",
    "public_key": "ED25519_DEMO_PUBKEY"
}

def initiate():
    print("Initiating handshake with HiveMind Core...")
    response = requests.post(URL, json=PAYLOAD)
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    initiate()
