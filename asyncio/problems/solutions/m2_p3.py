import asyncio

async def print_a():
    await asyncio.sleep(1)
    print("A")

async def print_b():
    await asyncio.sleep(2)
    print("B")

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(print_b())
        task2 = tg.create_task(print_a())

    print("All tasks complete!")

if __name__ == "__main__":
    asyncio.run(main())