from crewai import Agent

developer = Agent(
    role="Developer",
    goal="Write clean code",
    backstory="Senior engineer",
    llm="ollama/llama3",   # ✅ FIX
    verbose=True
)