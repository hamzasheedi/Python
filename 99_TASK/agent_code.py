from agents import Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled,RunConfig,function_tool
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI



load_dotenv()
set_tracing_disabled(disabled=True)
APIKEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=APIKEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

config = RunConfig (
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client,
    )
)

#Two Tools With Same Name
@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is Sunny ☀️"

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is Rainy 🌧️"


# Create Agent with duplicate tools
agent = Agent(
    name="WeatherAgent",
    instructions="You are a helpful assistant for weather queries.",
    tools=[get_weather],  # <-- duplicate names
)


# Ask a query
response = Runner.run_sync(starting_agent=agent,input="What is the weather in Lahore?", run_config=config)
print(response.final_output)
