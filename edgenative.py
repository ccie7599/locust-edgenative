from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(2)
    def get_price_edgenative(self):
        # Testing the endpoint every second
        self.client.get("/get?topic=price&origin=edgenative")
    @task(2)
    def get_price_legacy(self):
        # Testing the endpoint every second
        self.client.get("/get?topic=price&origin=legacy")
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # Sets the time between requests; here it's 1 second
    wait_time = between(1, 1)

