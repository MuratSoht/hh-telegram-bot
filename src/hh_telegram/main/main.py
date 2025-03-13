from src.hh_telegram.infrastructure.async_module.client_api import async_request_api
from src.hh_telegram.main.config import PARAMS
import asyncio
import time
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        res = await async_request_api(session, PARAMS)
        print(len(res))

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)