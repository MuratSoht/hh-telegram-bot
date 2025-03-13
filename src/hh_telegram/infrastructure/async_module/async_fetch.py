from aiohttp import ClientSession
from src.hh_telegram.main.config import HH_API_URL
from typing import Dict
from src.hh_telegram.infrastructure.async_module.base_async_client import BaseAsyncClient


class AsyncFetcher(BaseAsyncClient):
    base_url = HH_API_URL

    async def get_list_vacancies(self, session: ClientSession, params: Dict):
        async with session.get(self.base_url + 'vacancies', params=params) as response:
            vacancy_list_json = await response.json()
            vacancy_list_json = vacancy_list_json.get('items', [])
            return vacancy_list_json

    async def get_vacancy(self, session: ClientSession, vacancy_id: str):
        vacancy = {}
        while vacancy.get('description') is None:
            async with session.get(self.base_url + 'vacancies/' + vacancy_id) as response:
                vacancy = await response.json()
                if vacancy.get('description') is not None:
                    return vacancy