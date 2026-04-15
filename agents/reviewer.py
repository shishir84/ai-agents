from crewai import Agent


reviewer = Agent(
    role="Code Reviewer",
    goal="Review code and suggest improvements",
    backstory="Strict reviewer",
    llm="ollama/llama3",   # ✅ FIX
    verbose=True
)