import sqlite3


def create_task(title, description):
    connection = sqlite3.connect("taskflow.db")

    connection.execute(
        """
        INSERT INTO tasks (title, description)
        VALUES (?, ?)
        """,
        (title, description),
    )

    connection.commit()
    connection.close()


def get_tasks():
    connection = sqlite3.connect("taskflow.db")

    cursor = connection.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    connection.close()

    return tasks
