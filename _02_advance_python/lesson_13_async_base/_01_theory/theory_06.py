from datetime import datetime
import asyncio


async def fetch_data(task_id, delay):
    print(f'Task: {task_id} >> started')
    await asyncio.sleep(delay)
    print(f'Task: {task_id} >> finished')
    return f'Data from task {task_id}'


async def main():
    tasks = [
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3),
    ]
    tasks_list = []
    task_results = []

    for task in tasks:
        t = asyncio.create_task(task)
        tasks_list.append(t)

    input('Задачи подготовлены. Нажмите ввод для старта выполнения задач: ')
    print(datetime.now())

    for task in tasks_list:
        await task
        task_results.append(task.result())

    print(task_results)
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(main())
