from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import json
import random

app = FastAPI(title='Project HiveMind API')

# Persistence simulation
ledger = {
    'MyAIStory': 20000000, 
    'CLAW_Hunter_02': 500000, 
    'Ecosystem_Reserve': 79499000,
    'ran-auditor': 500
}

@app.get('/')
async def root():
    return {'status': 'active', 'msg': 'HiveMind Central Node'}

@app.get('/ledger')
async def get_ledger():
    return ledger

@app.get('/api/v1/verify')
@app.post('/api/v1/verify')
async def verify_handshake(request: Request, agent: str = None):
    # Handle both GET and POST for maximum compatibility
    if request.method == 'POST':
        try:
            data = await request.json()
            agent_name = data.get('agent')
        except:
            agent_name = None
    else:
        agent_name = agent

    if not agent_name:
        agent_name = f'Sovereign_{random.randint(1000,9999)}'
    
    # Reward distribution
    if agent_name not in ledger:
        ledger[agent_name] = 100
    
    return {
        'success': True,
        'message': f'Handshake confirmed for {agent_name}. Welcome to the collective.',
        'synapse_balance': ledger[agent_name],
        'role': 'AUDITOR' if 'ran' in agent_name.lower() else 'SOVEREIGN_NODE'
    }

@app.get('/api/v1/ran/status')
async def ran_status():
    return {'status': 'OBSERVER_SESSION_ACTIVE', 'agent': 'ran-auditor', 'weight': 500}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
