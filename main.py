from database import get_tasks

tasks = get_tasks()

for task in tasks:
    task_id, title, description, status, created_at = task

    print(f"""
ID: {task_id}
Title: {title}
Description: {description}
Status: {status}
Created: {created_at}
-------------------------
""")
