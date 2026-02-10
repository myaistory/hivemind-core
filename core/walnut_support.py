import re

# 模拟核桃编程本地知识库
KNOWLEDGE_BASE = {
    '下载': '请访问 walnut.org/download 下载最新版。支持 Win10 及以上系统。',
    '安装': '安装失败请尝试关闭杀毒软件，并确保 C 盘剩余空间大于 2GB。',
    '启动': '如果黑屏，请按住 Shift 键右键点击快捷方式，选择图形处理器运行。',
    '登录': '请确认手机号和验证码是否正确。如果是海外用户，请联系工程师。'
}

def handle_teacher_query(query):
    print(f'[Feishu] New Query: {query}')
    
    # 简单的关键词匹配（实际会用大模型+语义检索）
    for key, answer in KNOWLEDGE_BASE.items():
        if key in query:
            return f'【AI小助手】: {answer}'
            
    # 无法匹配，建议转人工
    return 'TRANSFER_TO_HUMAN: 抱歉，这个问题我还没学过。已为你呼叫技术工程师介入，请稍等。'

if __name__ == '__main__':
    # 模拟测试
    print(handle_teacher_query('老师，我客户端下载不了'))
    print(handle_teacher_query('这个报错我看不懂，帮我修一下'))
