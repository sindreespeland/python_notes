import asyncio

from m1_p2 import greet_after_delay

async def main():
    await greet_after_delay("Alice", 1)
    await greet_after_delay("Bob", 1)

if "__main__" == __name__:
    asyncio.run(main())