import asyncio
import time
from concurrent.futures import ProcessPoolExecutor


async def message_printer():
    while True:
        print("Some message...")
        await asyncio.sleep(0.1)

def calc():
    time.sleep(4)
    print("Completed calculation")

async def main():
    task = asyncio.create_task(message_printer())

    with ProcessPoolExecutor(max_workers=1) as executor:
        loop = asyncio.get_running_loop()

        await loop.run_in_executor(executor, calc)

    await task

if __name__ == "__main__":
    asyncio.run(main())