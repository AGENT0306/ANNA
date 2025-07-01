from STT import STT
from Chat_Intergration import ChatInt
from Tool_Setup import ToolKit
import re
from flask import Flask, request

voice = STT()
chat = ChatInt()
tk = ToolKit()

chat.init_agent(tk.get_tools())
while True:
    query = voice.start_stt()
    raw = re.sub(r'[^a-zA-Z0-9]', '', query).lower()
    if raw == "exit":
        break
    chat.agent_call(query)


'''app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/aireq', methods=['GET', 'POST'])
def aireq():
    query = request.args.get('query')
    res = AICall(query)
    return f'<h1> Your query is:  {query}</h1> <br/> <p> Your response was {res} </p>'''
