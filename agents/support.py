from crewai import Agent


support = Agent(
    role="Support Agent",
    goal="Analyze issues and escalate if needed",
    backstory="Customer support expert",
    llm="ollama/llama3",   # ✅ FIX
    verbose=True
)