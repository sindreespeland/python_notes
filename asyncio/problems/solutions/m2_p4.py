import asyncio

async def worker_a():
    await asyncio.sleep(1)
    raise ValueError

async def worker_b():
    await asyncio.sleep(5)
    print("Finished")

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(worker_a())
        task2 = tg.create_task(worker_b())

    print("All tasks finished")

if __name__ == "__main__":
    asyncio.run(main())
