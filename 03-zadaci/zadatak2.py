import asyncio
import numpy as np
import psutil

async def afunc1():
    for i in range(10):
        np.random.normal(loc=0, scale=1, size=1000000)
        await asyncio.sleep(0.9)

async def afunc2():
    return psutil.cpu_percent(interval=(1))

async def main():
    await afunc1()
    print(await afunc2())
    
if __name__ =="__main__":
    asyncio.run(main())
