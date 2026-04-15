from crewai import Crew, Task
from agents.recruiter import recruiter


def run_hiring(resume):

    task = Task(
        description=f"Evaluate this resume: {resume}",
        expected_output="Candidate evaluation with score and decision",
        agent=recruiter
    )

    crew = Crew(
        agents=[recruiter],
        tasks=[task]
    )

    return crew.kickoff()