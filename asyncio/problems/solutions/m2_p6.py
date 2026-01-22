import asyncio

async def slow_api_call():
    await asyncio.sleep(5)

async def main():

    try:
        await asyncio.wait_for(slow_api_call(), timeout=2)
    except asyncio.TimeoutError:
        print("Too slow!")

if __name__ == "__main__":
    asyncio.run(main())