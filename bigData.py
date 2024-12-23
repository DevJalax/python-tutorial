import aiohttp
import asyncio
import logging
import json
from sqlalchemy import create_engine, text

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AsyncRequestStreamer:
    def __init__(self, url, db_url):
        self.url = url
        self.db_url = db_url

    async def send_request(self, session, request_data):
        try:
            async with session.post(self.url, json=request_data) as response:
                response_data = await response.text()
                logging.info(f"Sent: {request_data}, Received: {response.status}, Response: {response_data}")
        except Exception as e:
            logging.error(f"Error sending request {request_data}: {e}")

    async def stream_requests(self):
        async with aiohttp.ClientSession() as session:
            engine = create_engine(self.db_url)
            async with engine.connect() as conn:
                result = await conn.execute(text("SELECT * FROM requests_table"))
                requests_list = [row._mapping for row in result]

            tasks = [self.send_request(session, request_data) for request_data in requests_list]
            await asyncio.gather(*tasks)

def main():
    url = "http://example.com/api"  # Replace with your target URL
    db_url = "postgresql://username:password@host:port/database"  # Replace with your database URL

    streamer = AsyncRequestStreamer(url, db_url)
    asyncio.run(streamer.stream_requests())

if __name__ == "__main__":
    main()
