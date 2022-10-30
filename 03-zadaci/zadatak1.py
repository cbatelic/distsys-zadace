import asyncio
import os

async def afun1(fileNamesList):
    await asyncio.sleep(0.2)
    return [{"naziv": name, "velicina":os.path.getsize(os.path.dirname(os.path.realpath(__file__))+ "\\")+ name} for name in fileNamesList]

def fun2(fileNamesList):
    for name in fileNamesList:
        file= open(os.path.dirname(os.path.realpath(__file__))+ "\\"+name,'a')
        for i in range(1,10001):
            file.write(str(i)+"")
            file.close()

async def main():
    pathDir= os.path.dirname(os.path.realpath(__file__))
    files=["datoteka1.txt", "datoteka2.txt", "datoteka3.txt"]
    for name in files:
        open(pathDir+"\\"+name,'a').close()
        fun2(files)
        print(await afun1(files))
        
if __name__=="__main__":
    asyncio.run(main())
