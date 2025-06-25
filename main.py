from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_community import CalendarToolkit
from langchain_google_community.calendar.create_event import CalendarCreateEvent
from flask import Flask, request


model = init_chat_model("gpt-4.1-mini", model_provider="openai")

#creates memory thread for AI
memory = MemorySaver()

#initilzes Tavily Search API
search = TavilySearch(max_results=2)

#init Google Calendar toolkit
create_calendar_event, search_calendar_events, update_calendar_event, get_calendar_info, move_calendar_event, delete_calendar_event, get_current_date_time = CalendarToolkit().get_tools()
#create_cal_event = CalendarCreateEvent()

tools = [search, create_calendar_event, search_calendar_events, update_calendar_event, get_calendar_info, move_calendar_event, delete_calendar_event, get_current_date_time]
agent_executor = create_react_agent(model, tools, checkpointer=memory)
config = {"configurable" : {"thread_id" : "abc123"}}
query = None

def AICall(query):
    input_messages = {"role": "user", "content": query}

    for step in agent_executor.stream({"messages": [input_messages]}, config, stream_mode="values"):
        step["messages"][-1].pretty_print()


def main():
    while True:
        query = input("Enter your query:")
        if query == "exit":
            break
        AICall(query)

'''app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/aireq', methods=['GET', 'POST'])
def aireq():
    query = request.args.get('query')
    res = AICall(query)
    return f'<h1> Your query is:  {query}</h1> <br/> <p> Your response was {res} </p>'''


if __name__ == '__main__':
    main()







