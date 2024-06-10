from django.urls import path
from .views import StartScraping, ScrapingStatus

urlpatterns = [
    path('taskmanager/start_scraping/', StartScraping.as_view(), name='start_scraping'),
    path('taskmanager/scraping_status/<uuid:job_id>/', ScrapingStatus.as_view(), name='scraping_status'),
]
