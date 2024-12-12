from locust import HttpUser, SequentialTaskSet, task, between

class User1(HttpUser):

    @task

    def MainPage(self):
        self.client.get("")