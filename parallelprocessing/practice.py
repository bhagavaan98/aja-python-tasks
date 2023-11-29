import asyncio

async def coroutine_one():
    print("Coroutine One: Start")
    await asyncio.sleep(2)
    print("Coroutine One: End")

async def coroutine_two():
    print("Coroutine Two: Start")
    await asyncio.sleep(1)
    print("Coroutine Two: End")

async def main():
    
    # Run coroutines concurrently
    await asyncio.gather(coroutine_one(), coroutine_two())

# Run the event loop with the main coroutine
asyncio.run(main())



# import concurrent.futures

# def my_task(arg):
#     # Task logic
#     print(f"Task {arg} executed")

# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     # Submit tasks to the thread pool
#     tasks = [executor.submit(my_task, i) for i in range(5)]
    
#     # Wait for all tasks to complete
#     concurrent.futures.wait(tasks)