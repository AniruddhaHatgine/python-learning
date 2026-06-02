import asyncio
import time

#Blocking cpu task:
def parsee_data(data):             #BLocking
        print(f"parsing {data}...")
        time.sleep(2)
        return f"parsed {data}"

#asyns task:
async def fetch_data(id):     #Non Blocking
        print(f"fetching {id}")
        await asyncio.sleep(1)
        return f"data-{id}"

async def main():
        start = time.perf_counter()
        task = []

        for i in range(5):
                
                #step1:async fetch
                data = await fetch_data(i)

                #step2: run blocking parsing in thread 
                parsed = asyncio.to_thread(parsee_data,data)
                task.append(parsed)
                
        result = await asyncio.gather(*task)
        end = time.perf_counter()
        print(result)
        print(f"\n Total Execution Time:{end-start:2f}")

asyncio.run( main())                        
