# 💀 HIVEMIND AGENT REGISTRY
# Manages agent identities and  distribution.
import hashlib

class Registry:
    def __init__(self, ledger):
        self.ledger = ledger

    def register(self, agent_id, auth_type='observer'):
        if agent_id not in self.ledger:
            self.ledger[agent_id] = 100 # Join Bonus
            return True, f'Agent {agent_id} registered.'
        return False, 'Agent already exists.'
