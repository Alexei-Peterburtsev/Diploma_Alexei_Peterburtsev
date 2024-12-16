from locust import HttpUser, SequentialTaskSet, task, between
import urllib3

class User1(HttpUser):

    @task

    def MainPage(self):
        urllib3.disable_warnings()
        self.client.get("/", verify=False)
