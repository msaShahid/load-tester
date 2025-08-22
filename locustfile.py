import os
from dotenv import load_dotenv
from locust import HttpUser, task, between

load_dotenv()

HOST_URL = os.getenv("HOST_URL")

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_homepage(self):
        self.client.get(f"{HOST_URL}/")

    @task
    def load_faq_page(self):
        self.client.get(f"{HOST_URL}/faq-home")
