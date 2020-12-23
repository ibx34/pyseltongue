from pyseltoungue import client
import asyncio

async def main():
    return await client.get_wss()

print(asyncio.run(main=main()))