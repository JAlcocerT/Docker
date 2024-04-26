import os
from crewai import Agent, Task, Crew, Process

### OLLAMA (THANKS TO LANGCHAIN)
from langchain.llms import Ollama
ollama_model = Ollama(model="openhermes")


### OPENAI
# os.environ["OPENAI_API_KEY"] = "Your Key"
#export OPENAI_API_KEY=sk-blablabla # on Linux/Mac


# Define your agents with roles and goals
researcher = Agent(
  role='Researcher',
  goal='Discover new insights',
  backstory="You're a world class researcher working on a major data science company",
  verbose=True,
  allow_delegation=False,
  llm=ollama_model, ### OLLAMA VERSION!!
  # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4 ### OPENAI VERSION!!
)
writer = Agent(
  role='Writer',
  goal='Create engaging content',
  backstory="You're a famous technical writer, specialized on writing data related content",
  verbose=True,
  allow_delegation=False,
  llm=ollama_model ### OLLAMA VERSION!!
)

# Create tasks for your agents
task1 = Task(description='Investigate the latest AI trends', agent=researcher)
task2 = Task(description='Write a blog post on AI advancements', agent=writer)

# Instantiate your crew with a sequential process - TWO AGENTS!
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  llm=ollama_model, ### OLLAMA VERSION!!
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()