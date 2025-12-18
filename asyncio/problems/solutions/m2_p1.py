import asyncio
import time
from tracemalloc import start

DATA = {
    1: "Data for user 1",
    2: "Data for user 2",
    3: "Data for user 3"
}

async def fetch_user_data(user_id: int):    
    await asyncio.sleep(user_id)
    return DATA[user_id]

async def main():
    start_time = time.time()

    # Option 1: Creating tasks with create_task schedules them ask tasks immediatly on the event loop
    # tasks = [asyncio.create_task(fetch_user_data(i+1)) for i in range(3)]
    # user_data = await asyncio.gather(*tasks)

    # Option 2: Defining them like this does not
    tasks = [fetch_user_data(i+1) for i in range(3)]
    user_data = await asyncio.gather(*tasks)

    # Option 1: Fire of tasks immediatly, do some work in the meantime and check on them later
    # Option 2: Run them in parallell and wait for them. no other work in between
    # because we schedule them at the sime line we await them


    end_time = time.time()

    elapsed_time = int(end_time - start_time)

    print(user_data)

    if elapsed_time > 3:
        print("Total execution took longer then expected. Not using asyncio gather properly")
    else:
        print("It is nice and fast")

asyncio.run(main())
