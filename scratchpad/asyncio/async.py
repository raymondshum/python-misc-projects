import aiohttp
import asyncio

BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINTS = [
    "/posts",
    "/comments",
    "/albums",
    "/photos",
    "/todos",
    "/users"
]

async def get_responses(urls: list[str]):
    async with aiohttp.ClientSession() as session:
        pass
        
async def get_response(session: aiohttp.ClientSession, url: str):
    async with session.get(url=url) as resp:
        print(url + ":", resp.status)

            
async def main():
    
    
    urls = [BASE_URL + endpoint for endpoint in ENDPOINTS]
    
    # await get_response(urls=urls)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())