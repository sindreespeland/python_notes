import asyncio

async def hello_async():
    print("Hello, Asyncio!")

if "__main__" == __name__:
    asyncio.run(hello_async())