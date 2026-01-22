import asyncio

async def process_string(string: str):
    await asyncio.sleep(1)

    return f"{string} Processed"

async def save_string(string: str):
    await asyncio.sleep(1)

    return f"{string} Saved"

async def pipeline():
    str_input = input("Write a string: ")

    str_processed = await process_string(str_input)
    str_saved = await save_string(str_processed)

    print(str_saved)

asyncio.run(pipeline())