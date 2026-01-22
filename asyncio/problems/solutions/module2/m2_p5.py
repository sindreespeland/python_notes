import asyncio

async def work():
    await asyncio.sleep(2)

async def heartbeat():
    while True:
        print("Alive...")
        await asyncio.sleep(0.5)

async def main():

    heartbeat_task = asyncio.create_task(heartbeat())
    task = asyncio.create_task(work())

    await task

    heartbeat_task.cancel()

    try:
        await heartbeat_task
    except asyncio.CancelledError:
        pass

    print("Main task finished...")



if __name__ == "__main__":
    asyncio.run(main())