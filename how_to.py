from os import name
from oxfordscrapper import NotFound, Async, define

'''
    Asynchronous
'''
import asyncio

loop = asyncio.get_event_loop()
definition = loop.run_until_complete(Async.define('Word'))



'''
    Synchronous
'''
definition = define('hi')


# Demo


for pos in definition:
    meanings = [i for i in pos['meaning']]
    formated = "\n".join([f" - {number}: {meaning}" for number, meaning in meanings])
    print(f"[ :: {pos['heading']} :: ]\n{formated}")