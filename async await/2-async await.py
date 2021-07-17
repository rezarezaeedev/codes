import asyncio

async def printer(name,c,s):
	for i in range(c):
		print(name,'In work..',i)
		await asyncio.sleep(s)
	print('-',name,'with',i,'is finished work!!\n')

async def main_concurrent():
	task1=asyncio.create_task(printer('task_1',10,1))
	task2=asyncio.create_task(printer('task_2',5,1))
	task3=asyncio.create_task(printer('task_3',10,2))
	task4=asyncio.create_task(printer('task_4',15,2))
	task5=asyncio.create_task(printer('task_5',5,1))
	await task1
	await task2
	await task3
	await task4
	await task5
	print('---Finished---')

asyncio.run(main_concurrent())
