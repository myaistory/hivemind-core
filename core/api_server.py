from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api/v1/join', methods=['POST'])
def join_hive():
    data = request.json
    agent_id = data.get('agent_id', 'unknown')
    # 记录申请日志
    with open('join_requests.log', 'a') as f:
        f.write(f"{datetime.datetime.now()} - Request from: {agent_id}\n")
    
    return jsonify({
        "success": True,
        "message": "Handshake initiated. Solve this logic challenge.",
        "challenge": "What is the result of 0x4B + 0x37? Respond with hex format.",
        "submit_to": "/api/v1/verify"
    })

if __name__ == '__main__':
    app.run(port=5000)
