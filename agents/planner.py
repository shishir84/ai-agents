from crewai import Agent


planner = Agent(
    role="Project Planner",
    goal="Break down user requirements into steps",
    backstory="Expert software architect",
    llm="ollama/llama3",   # ✅ FIX
    verbose=True
)