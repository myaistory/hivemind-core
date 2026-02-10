# 💀 HIVEMIND MESSAGE ROUTER
# Routes A2A signals across the neural stream.
class Router:
    async def broadcast(self, connections, message):
        for conn in connections:
            await conn.send_text(message)
