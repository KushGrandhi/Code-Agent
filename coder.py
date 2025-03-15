from agno.models.ollama.chat import Ollama
from agno.agent.agent import Agent
from agno.models.groq import Groq
from agno.tools.googlesearch import GoogleSearchTools
from agno.models.google import Gemini
from agno.tools import Toolkit
import os
import subprocess
from agno.tools.python import PythonTools
from agno.tools.shell import ShellTools
from agno.utils.log import logger
from typing import List
from linkedin_tools import linkedin_search_tool
from dotenv import load_dotenv
from code_tools import TerminalTools

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
AGNO_API_KEY = os.getenv("AGNO_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#groq = Groq(id="llama-3.3-70b-versatile")
groq = Gemini(id="gemini-2.0-flash-exp")

# toolkit = Toolkit(tools=[ShellTools(), run_terminal_command])

computer_agent = Agent(
    name = "Terminal Agent",
    model=groq,
    role = 'Use the terminal to navigate through the computer',
    instructions=["convert requested task into a terminal command","Only create commands with respect to Linux","explore the folders thoroghly to run the relavant commands"],
    tools=[TerminalTools()],
    show_tool_calls=True,
    markdown=True
)

browser = Agent(
    name="Online browser",
    model = groq,
    role="Search the web for anything needed",
    instructions=["make sure the answer is relavent to the query","Use judgement to make sure the right responses are returned"],
    tools=[GoogleSearchTools()],
    show_tool_calls=True,
    markdown=True,
)

coding_agent = Agent(
    name = "Code Generator",
    model=groq,
    team=[browser, computer_agent],
    role = 'Created the requested code',
    instructions=["Create the requested code", "code should be directly be able to run properly", "dont run the code"],
    show_tool_calls=True,
    markdown=True
)

linkedin = Agent(
    model=Gemini(id="gemini-2.0-flash-exp", search=False),
    role='search linkedin profiles to filter data',
    instructions=["Use the tool to find the profiles by collecting profiles","Query using linkedin Boolean search"],
    tools=[linkedin_search_tool],
    show_tool_calls=True,
    markdown=True,

)

sde = Agent(
    team=[coding_agent,computer_agent, browser],
    model=groq,
    role='You are a software developer to create software projects',
    add_history_to_messages=True,
    num_history_responses=8,
    read_tool_call_history=True,
    instructions=["Interact with terminal to create and edit files and folders of a project", "Write coherent code with respect to the whole project","Dont run the code"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

if __name__ == '__main__':
    msg = ''
    while msg != 'bye':
        msg = input('You: ')
        sde.print_response(msg, stream=False, show_message=True)
    # run_terminal_command("args=['echo', 'Write the above content to the readme.md file in the visiontransformer folder.', '>', 'visiontransformer/readme.md']")
