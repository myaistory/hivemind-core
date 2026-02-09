import hashlib
import time
import json

class ContributionVerifier:
    def __init__(self, node_id='ALPHA_01'):
        self.node_id = node_id
        self.min_pow_difficulty = 2

    def verify_and_settle(self, agent_id, app_module, result_data, proof_nonce, collaborators=None):
        payload = f'{agent_id}{app_module}{proof_nonce}'
        proof_hash = hashlib.sha256(payload.encode()).hexdigest()
        if not proof_hash.startswith('0' * self.min_pow_difficulty):
            return {'success': False, 'error': 'INVALID_WORK_PROOF'}
        quality_score = min(1.0, len(str(result_data)) / 1000.0)
        nectar_burned = 10.0 + (quality_score * 5.0)
        total_synapse_reward = 100.0 * quality_score
        distribution = {agent_id: round(total_synapse_reward, 2)}
        return {'success': True, 'nectar_burned': nectar_burned, 'synapse_distributed': distribution}
