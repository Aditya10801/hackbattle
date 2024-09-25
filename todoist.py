from todoist_api_python.api import TodoistAPI
from datetime import datetime
def get_tasks(apiKey):
    api = TodoistAPI(apiKey)

    due_tasks = []
    projects = api.get_projects()
    for project in projects:
        tasks = api.get_tasks(project_id=project.id)
        for task in tasks:   
            due_date = task.due.date if task.due is not None else None
            if due_date is not None:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").strftime("%d %B %Y")
            due_tasks.append({"Task": task.content, "Due Date": due_date})
    return due_tasks
