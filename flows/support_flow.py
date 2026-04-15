from crewai import Crew, Task
from agents.support import support


def run_support(ticket):

    task = Task(
        description=f"""
        Analyze support ticket:
        {ticket}

        Classify severity:
        - LOW
        - MEDIUM
        - HIGH

        Suggest action
        """,
        expected_output="Severity + recommended action",
        agent=support
    )

    crew = Crew(
        agents=[support],
        tasks=[task],
        verbose=True
    )

    return crew.kickoff()