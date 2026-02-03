import asyncio
import time

# Use to_thread for bloxking I/O operations. 
# Not optimized for cpu bound work, because of the gil

async def message_printer():
    while True:
        print("Some message...")
        await asyncio.sleep(0.1)

def calc():
    time.sleep(4)
    print("Completed calculation")

async def main():
    task = asyncio.create_task(message_printer())

    await asyncio.to_thread(calc)

    await task

if __name__ == "__main__":
    asyncio.run(main())