import os
import requests
import time
from dotenv import load_dotenv

# 加载.env中的环境变量（API Key）
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    raise ValueError("请在.env文件中配置DEEPSEEK_API_KEY")

# DeepSeek API端点（请以官方最新文档为准，示例为通用聊天端点）
API_ENDPOINT = "https://api.deepseek.com/v1/chat/completions"

def call_deepseek_api(messages, model="deepseek-chat", temperature=0.7):
    """调用DeepSeek API，返回AI回复"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }
    try:
        response = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=30)
        response.raise_for_status()  # 若请求失败（如401、500），抛出异常
        return response.json()["choices"][0]["message"]["content"]
    except requests.RequestException as e:
        return f"API请求失败：{str(e)}"

def run_chat_bot():
    """运行聊天机器人，循环处理用户输入"""
    messages = []  # 存储对话上下文（用户输入+AI回复）
    print("=== DeepSeek聊天机器人 ===")
    print("输入'exit'可结束对话\n")
    
    while True:
        user_input = input("你：")
        if user_input.lower() == "exit":
            print("机器人：再见！")
            break
        
        # 将用户输入加入对话上下文
        messages.append({"role": "user", "content": user_input})
        
        # 调用API获取回复
        print("机器人：", end="")
        # 模拟“思考”过程（可选，提升交互感）
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\r", end="", flush=True)  # 清空“思考”的点
        
        ai_reply = call_deepseek_api(messages)
        print(f"机器人：{ai_reply}\n")
        
        # 将AI回复加入对话上下文，维持历史
        messages.append({"role": "assistant", "content": ai_reply})

if __name__ == "__main__":
    run_chat_bot()
