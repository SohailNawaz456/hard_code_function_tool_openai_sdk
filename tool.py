from agents import Agent, Runner, function_tool
from main import config
import rich

# Define a tool function to convert USD to PKR
@function_tool
def usd_to_pkr(query: str) -> str:
    return "Today 1 USD Equal 280 PKR"

# Create an agent with clear instructions and tool usage
agent = Agent(
    name="General Agent",
    instructions=(
        "You are a helpful assistant. Your task is to help users with their queries. "
        "Use tools if needed to answer currency questions."
    ),
    tools=[usd_to_pkr]  # ✅ Register the tool with the agent
)

# Run the agent synchronously with a currency question
result = Runner.run_sync(agent, "What is 1 USD to PKR?", run_config=config)

# Print the final output
rich.print(result.final_output)
