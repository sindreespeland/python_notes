import asyncio

async def save_to_db():
    await asyncio.sleep(3)
    print("Saved to db")

async def main():
    task = asyncio.create_task(save_to_db())

    shielded_task = asyncio.shield(task)

    try:
        await asyncio.wait_for(shielded_task, timeout=1)
    except asyncio.TimeoutError:
        print("Shielded task cancelled, main task still running")
    
    await task



    

if __name__ == "__main__":
    asyncio.run(main())