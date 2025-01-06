# execute shell commands using agentic ai
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.tools.shell.tool import ShellTool
from langchain.chat_models import ChatOllama

llm = ChatOllama(model="mistral")
shell_tool = ShellTool()

tools = [
    Tool(
        name="Shell Executor",
        func=shell_tool.run,
        description=""
    )
]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

output = agent.run("output a simple hello world to me using echo. I am on macos.")