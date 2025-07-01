from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

class ChatInt(object):
    def __init__(self, m="gpt-4.1-mini", mp="openai"):
        self.config = None
        self.agent_exec = None
        self.model = init_chat_model(m, model_provider=mp)
        self.memory = MemorySaver()

    def chat(self, msg):
        message = [{"role": "user", "content": msg}]
        return self.model.invoke(message)

    def init_agent(self, tools):
        self.agent_exec = create_react_agent(self.model, tools, checkpointer=self.memory)
        self.config = {"configurable": {"thread_id": "abc123"}}

    def agent_call(self, msg):
        message = [{"role": "user", "content": msg}]
        for step in self.agent_exec.stream({"messages": message}, self.config, stream_mode="values"):
            step["messages"][-1].pretty_print()