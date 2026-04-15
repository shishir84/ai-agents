from crewai import Crew, Task
from agents.planner import planner
from agents.developer import developer
from agents.reviewer import reviewer
from common.memory import save_memory, get_memory


def run_dev_team(user_input, max_retries=2):

    memory_context = get_memory()

    for attempt in range(max_retries):

        task1 = Task(
            description=f"""
            Break down requirement: {user_input}
            Context: {memory_context}
            """,
            expected_output="A detailed step-by-step development plan",
            agent=planner
        )

        task2 = Task(
            description="""
            Write production-ready code based on the plan.
            Use best practices.
            """,
            expected_output="Complete working code with explanation",
            agent=developer
        )

        task3 = Task(
            description="""
            Review the code.
            If issues exist, respond with FIX_NEEDED and explain issues.
            """,
            expected_output="Reviewed code with improvements or FIX_NEEDED",
            agent=reviewer
        )

        crew = Crew(
            agents=[planner, developer, reviewer],
            tasks=[task1, task2, task3],
            verbose=True
        )

        result = crew.kickoff()

        save_memory(str(result))

        # 🔁 Feedback loop
        if "FIX_NEEDED" not in str(result):
            return result
        else:
            print(f"Retrying... Attempt {attempt+1}")

    return result