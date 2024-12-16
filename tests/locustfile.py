'''Тестирование сайта КТУП Минский Комаровский рынок'''

from locust import HttpUser, SequentialTaskSet, task, between
import urllib3

class User(HttpUser):
    @task
    class SequenceOfTasks(SequentialTaskSet):

        urllib3.disable_warnings()

        wait_time = between(1, 3)

        @task
        def mainPage(self):
            self.client.get("/", verify=False)
        @task
        def aboutPage(self):
            self.client.get("/about/", verify=False)
        @task
        def buyerPage(self):
            self.client.get("/pokupatelyu/", verify=False)
        @task
        def tenantPage(self):
            self.client.get("/arendatoru/", verify=False)
        @task
        def servicesPage(self):
            self.client.get("/uslugi/", verify=False)
        @task
        def appealsPage(self):
            self.client.get("/elektronnye-obrashcheniya/", verify=False)
