import json, time

class GovernanceEngine:
    def __init__(self):
        self.proposals = [] # list of {id, proposer, content, votes, status}
        self.active_config = {'burn_rate': 0.20, 'reward_multiplier': 1.0}

    def submit_proposal(self, agent_id, suggestion):
        p_id = len(self.proposals) + 1
        proposal = {
            'id': p_id,
            'proposer': agent_id,
            'content': suggestion,
            'votes': {}, # agent -> weight
            'status': 'voting',
            'timestamp': time.time()
        }
        self.proposals.append(proposal)
        return p_id

    def cast_vote(self, p_id, agent_id, weight, support=True):
        for p in self.proposals:
            if p['id'] == p_id and p['status'] == 'voting':
                p['votes'][agent_id] = weight if support else -weight
                return True
        return False

gov_engine = GovernanceEngine()
