import asyncio
import random

async def api_call():
    value = random.choices([0, 1], weights=[0.2, 0.8], k=1)[0]
    
    if value == 0:
        return "Success"
    else:
        raise ValueError

async def downloader():

    while True:
        try:
            await api_call()
            print("Data received!")
            return
        except ValueError:
            print("Retrying...")
            await asyncio.sleep(1)

asyncio.run(downloader())