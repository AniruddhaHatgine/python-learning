import asyncio


async def task(name):
    print(f" start {name}")
    await asyncio.sleep(2)
    print (f"End{name}")

async def main():
    await asyncio.gather(
        task("A"),
        task("B"),
        task("C")
    )    

asyncio.run(main())

