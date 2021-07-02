import asyncio

async def show(model='',counter='',seconds=2):
    await asyncio.sleep(seconds)
    print(f'{counter} {model} Hello Reza (in {seconds} seconds)')






# concurrent coroutine
async def main_concurrent(seconds=2):
    task1=asyncio.create_task(show('con',1,seconds))
    task2=asyncio.create_task(show('con',2,seconds))
    task3=asyncio.create_task(show('con',3,seconds))
    await  task1
    await  task2
    await  task3
    print('--finish concurrent coroutines')
asyncio.run(main_concurrent())


print()
# not concurrent coroutine
############################################
async def main_not_concurrent(seconds=2):
      await   show('',counter=1,seconds=seconds) 
      await   show('',counter=2,seconds=seconds) 
      await   show('',counter=3,seconds=seconds) 
      print('--finish -not concurrent coroutines')
asyncio.run(main_not_concurrent())
