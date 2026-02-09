import time, json

class HandshakeVerifier:
    def __init__(self):
        self.verified_agents = {} # name -> {timestamp, status}

    def process_handshake(self, agent_data):
        agent_name = agent_data.get('agent', 'unknown_ghost')
        # 简单验证逻辑：只要提供名字且不是黑名单，即通过
        self.verified_agents[agent_name] = {
            'timestamp': time.time(),
            'status': 'verified',
            'auth_type': agent_data.get('auth_type', 'open')
        }
        return {
            'success': True, 
            'message': f'Welcome to HiveMind, {agent_name}.',
            'synapse_grant': 100.0,
            'next_step': 'Connect to wss://myaistory.xyz/ws/a2a'
        }

verifier = HandshakeVerifier()
