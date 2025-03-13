import asyncio
import aiohttp

from src.hh_telegram.infrastructure.async_module.async_fetch import AsyncFetcher
from src.hh_telegram.adapters.hh_adapters.hh_fetcher import HhFetcherVacancy
from typing import List, Dict

async def async_request_api(session, params_list: List[Dict]):
    vacancies_result = []
    async_fetcher = AsyncFetcher()
    vacancies_list_task = []
    for params in params_list:
        vacancies_list_task.append(asyncio.create_task(async_fetcher.get_list_vacancies(session, params)))
    res = await asyncio.gather(*vacancies_list_task)
    cnt = 0
    for vacancy_query in res:
        for vacancy in vacancy_query:
            try:
                task = asyncio.wait_for(asyncio.create_task(async_fetcher.get_vacancy(session, vacancy.get('id'))), timeout=100)
                response_detail_vacancy = await task
                ready_data = HhFetcherVacancy(response_general_vacancy=vacancy, response_detail_vacancy=response_detail_vacancy).get_state()
                print(ready_data)
                vacancies_result.append(ready_data)
                cnt+=1
            except asyncio.TimeoutError:
                pass
    return vacancies_result