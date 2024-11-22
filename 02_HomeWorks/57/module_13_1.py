import asyncio


async def start_strongman(name: str, power: int):
    balls_qty = 5
    balls_use = 0
    print(f'Силач {name} начал соревнования.')
    
    while balls_qty > 0:
        balls_use += 1
        await asyncio.sleep(float((balls_qty / power) * 10))  # умножение на десятку что-бы в консоли не мелькало и было видно что это какой-то процесс всё таки а не мгновение.
        print(f'Силач {name} поднял {balls_use}')
        balls_qty -= 1
    
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Thor', 15))
    task2 = asyncio.create_task(start_strongman('Loki', 10))
    task3 = asyncio.create_task(start_strongman('Thanos', 20))
    
    await task1
    await task2
    await task3
    
    print('\n Турнир окончен.')


asyncio.run(start_tournament())
