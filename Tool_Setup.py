from langchain_google_community import CalendarToolkit

from langchain_tavily import TavilySearch

class ToolKit(object):
    def __init__(self):
        self.search = TavilySearch(max_results=2)
        self.create_calendar_event, self.search_calendar_events, self.update_calendar_event, self.get_calendar_info, self.move_calendar_event, self.delete_calendar_event, self.get_current_date_time = CalendarToolkit().get_tools()
        self.tools = [self.search, self.create_calendar_event, self.search_calendar_events, self.update_calendar_event, self.get_calendar_info, self.move_calendar_event, self.delete_calendar_event, self.get_current_date_time]

    def get_tools(self):
        return self.tools