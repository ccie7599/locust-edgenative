from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    host = "https://workshop.connected-cloud.io/"
    @task(2)
    def get_price_edgenative(self):
        self.client.headers.update({"User-Agent": "edgenative"})
        # Testing the endpoint every second
        self.client.get("/get?topic=price&origin=edgenative")
    @task(1)
    def get_price_legacy(self):
        self.client.headers.update({"User-Agent": "legacy"})
        # Testing the endpoint every second
        self.client.get("/getlegacy?topic=price&origin=legacy")
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # Sets the time between requests; here it's 1 second
    wait_time = between(1, 1)

