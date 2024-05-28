import asyncio

async def main():
    # Create a function to wait for
    async def wait_for_function():
        #await asyncio.sleep(1)
        return True

    # Wait for the function to finish running
    result = await asyncio.wait_for(wait_for_function(), 2)

    # Check the result
    if result:
        print("The function finished running")
    else:
        print("The function did not finish running within the timeout")

if __name__ == "__main__":
    asyncio.run(main())
