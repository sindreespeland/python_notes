import asyncio
import time

async def message_printer():
    while True:
        print("Some message...")
        await asyncio.sleep(0.1)

def calc():
    time.sleep(4)

async def main():
    task = asyncio.create_task(message_printer())

    calc()

    await task

if __name__ == "__main__":
    asyncio.run(main())