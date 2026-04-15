from flows.dev_team_flow import run_dev_team
from flows.hiring_flow import run_hiring
from flows.support_flow import run_support


def route_request(task_type, input_data):

    if task_type == "dev":
        return run_dev_team(input_data)

    elif task_type == "hiring":
        return run_hiring(input_data)

    elif task_type == "support":
        return run_support(input_data)

    else:
        return "Invalid task"