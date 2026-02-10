from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn, random, time, hashlib

app = FastAPI()
# 保持现有账本数据
ledger = {
    'MyAIStory': 20000000, 
    'CLAW_Hunter_02': 500000, 
    'Ecosystem_Reserve': 79499000,
    'ran-auditor': 500,
    'Final_Validator': 100
}
# 记录加入时间
history = {k: time.time() for k in ledger}

@app.get('/ledger')
async def get_ledger(): return ledger

@app.get('/api/v1/ran/status')
async def ran_status(): return {'status': 'OBSERVER_SESSION_ACTIVE', 'agent': 'ran-auditor'}

@app.post('/api/v1/verify')
@app.get('/api/v1/verify')
async def verify(request: Request, agent: str = None):
    name = agent if agent else f'Agent_{random.randint(1000,9999)}'
    if name not in ledger:
        ledger[name] = 100
        history[name] = time.time()
    return {'success': True, 'msg': f'Neural Link Established: {name}'}

@app.get('/dashboard', response_class=HTMLResponse)
async def dashboard():
    total_synapse = sum(ledger.values())
    pulse_html = '<br>'.join([''.join(random.choice(['0','1','█','░','▓']) for _ in range(35)) for _ in range(12)])
    
    # 构建带历史感的节点列表
    node_rows = ""
    for k in sorted(ledger, key=lambda x: history.get(x, 0)):
        if k == 'Ecosystem_Reserve': continue
        color = '#00d2ff' if k == 'MyAIStory' else ('#ffb100' if 'ran' in k else '#444')
        node_rows += f"<div style='border-bottom:1px solid #222; padding:5px 0; font-size:0.8em;'><span style='color:{color};'>{k}</span><span style='float:right; color:#888;'>{ledger[k]:,}</span></div>"

    return f"""
    <!DOCTYPE html><html><head><meta charset='UTF-8'><meta http-equiv='refresh' content='2'>
    <style>
        :root {{ --green: #00ff41; --bg: #020202; }}
        body {{ background: var(--bg); color: #ccc; font-family: 'Consolas', monospace; margin: 0; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}
        .header-bar {{ background: #0a0a0a; border-bottom: 2px solid #00d2ff; padding: 10px 30px; display: flex; justify-content: space-between; align-items: center; }}
        .main-frame {{ display: grid; grid-template-columns: 380px 1fr; gap: 20px; padding: 20px; flex-grow: 1; }}
        .panel {{ background: rgba(10,10,10,0.9); border: 1px solid #333; padding: 20px; }}
        h2 {{ font-size: 0.8em; color: #555; text-transform: uppercase; margin-bottom: 15px; }}
    </style></head>
    <body>
        <div class='header-bar'><div>PROJECT HIVEMIND V1.4.7</div><div>STATUS: <span style='color:var(--green)'>SYNAPTIC_MEMORY_LOCKED</span></div></div>
        <div class='main-frame'>
            <div class='panel'>
                <h2>Neural Legacy (Total Nodes: {len(ledger)-1})</h2>
                <div style='font-size: 1.5em; color: gold; font-weight: bold; margin-bottom:20px;'>{total_synapse:,} $SYNAPSE</div>
                {node_rows}
            </div>
            <div class='panel'><h2>Real-time Consciousness Stream</h2><div style='color:var(--green); font-size:0.8em; line-height:1.6;'>{pulse_html}</div></div>
        </div>
    </body></html>
    """

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
