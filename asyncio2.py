import asyncio # use asyncio to run non blocking code and run blocking code in thread
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor # make thread pool executor and run blocking code in thread
import time # use time to measure execution time and sleep for simulating blocking code

#CPU heavy task
def heavy_compute(x): # use a function to simulate heavy computation
    print(f"processing {x}...")
    time.sleep(2) # simulate heavy computation
    return x * x # return the result of heavy computation

#async I/O task
async def fetch_data(x): #use a function to simulate fetching data asynchronously
    await asyncio.sleep(1) # simulate Input/Output operation 
    return x

async def main(): # use a main function to run the async code   
    loop = asyncio.get_running_loop() # use the current event loop to run blocking code in process pool
    
    with ProcessPoolExecutor () as executor: # create a process pool executor
        #step1 : fetch concurrent data(non blocking)
        data = await asyncio.gather(*(fetch_data(i) for i in range(5))) # fetch data concurrently and wait for all to complete  
       
        #step2: Process in parallel
        results = await asyncio.gather(*
        (loop.run_in_executor(executor, heavy_compute, d) for d in data)) # run blocking code in process pool and wait for all to complete
       
        print(results) # print the results

if __name__ == "__main__": 
    asyncio.run(main()) # run the main function


