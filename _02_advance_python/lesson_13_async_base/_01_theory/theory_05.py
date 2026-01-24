import asyncio


async def my_coroutine():
    print(f'Start')
    await asyncio.sleep(2)
    print(f'End')
    return 'Done'


async def main():
    task = asyncio.create_task(my_coroutine())
    print(f'Task done: {task.done()}')
    await task
    print(f'Task result: {task.result()}')
    print(f'Task done: {task.done()}')


if __name__ == '__main__':
    asyncio.run(main())

"""
В каких случаях использовать Tasks?

Параллельное выполнение задач — когда нам нужно выполнить несколько асинхронных операций одновременно.

Управление задачами — когда нам нужно отслеживать состояние выполнения задач или отменять их.

Фоновые задачи — когда нам нужно запустить задачу в фоновом режиме, не дожидаясь её завершения.
"""