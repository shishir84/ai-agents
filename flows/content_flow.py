from crewai import Crew, Task
from agents.planner import planner
from agents.developer import developer


def run_content(topic):

    task1 = Task(
        description=f"Create content plan for {topic}",
        expected_output="Structured content outline",
        agent=planner
    )

    task2 = Task(
        description="Write detailed blog",
        agent=developer
    )

    crew = Crew(
        agents=[planner, developer],
        tasks=[task1, task2]
    )

    return crew.kickoff()