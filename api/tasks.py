# api/tasks.py
from celery import shared_task
from .models import Job, Task
from .coinmarketcap import CoinMarketCap
import logging

logger = logging.getLogger(__name__)

@shared_task
def scrape_coin_data(job_id, coin):
    try:
        logger.info(f"Starting to scrape data for {coin}")
        data = CoinMarketCap.get_coin_data(coin)
        if data is None:
            logger.warning(f"No data found for {coin}")
            return
        
        job = Job.objects.get(id=job_id)
        Task.objects.create(job=job, coin=coin, output=data)
        logger.info(f"Completed scraping data for {coin} with data: {data}")
    except Exception as e:
        logger.error(f"Error while scraping data for {coin}: {str(e)}")
        # Optionally, update the job or task with the error status
