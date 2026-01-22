import asyncio
from multiprocessing import Value

async def success():
    return "Ok"

async def fail():
    raise ValueError

async def main():
    tasks = [
        success(),
        fail(),
        success()
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    print(results)

if __name__ == "__main__":
    asyncio.run(main())

