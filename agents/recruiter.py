from crewai import Agent


recruiter = Agent(
    role="Recruiter",
    goal="Evaluate candidate suitability",
    backstory="HR expert",
    llm="ollama/llama3",   # ✅ FIX
    verbose=True
)