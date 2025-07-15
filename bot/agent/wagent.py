from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
import requests
from weather_bot import settings
import openai 
from bot.agent.prompts import beaches_nearer, agent_prompt

def weather_info(location: str) -> str:
    weather_api = settings.OPEN_WEATHER_KEY
    # TODO: Move this to yaml config or const
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={weather_api}"
    response = requests.get(url)
    return response.json()

def most_hot_city() -> str:
    candidates = ['Amsterdam', 'Paris', 'London', 'Berlin', 'Palermo', 'Madrid']
    print('I was indeed called')
    weather_info_city = []
    for city in candidates:
        weather_json = weather_info(city)
        temp_in_city = weather_json['main']['temp']
        weather_info_city.append( (temp_in_city, city) )

    weather_info_city.sort(reverse=True)
    return weather_info_city[0][1]  

def beaches_near(location: str) -> str:
    client = openai.OpenAI(
        api_key=settings.OPENAI_KEY  # Use the key from settings or environment variable
    )
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
            {"role": "user", "content": beaches_nearer.format(location=location)}
        ]
    )
    return str(completion.choices[0].message)

# Create an agent workflow with our calculator tool
def build_agent():
    agent = FunctionAgent(
        tools=[weather_info, most_hot_city, beaches_near],
        llm=OpenAI(api_key=settings.OPENAI_KEY, model="gpt-4o-mini"),
        system_prompt = agent_prompt,
    )
    return agent

async def query_agent(input):
    # Run the agent
    response = await build_agent().run(input)
    return str(response)
