from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def get_price(self):
        # Testing the endpoint every second
        self.client.get("/get?topic=price&origin=edgenative")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # Sets the time between requests; here it's 1 second
    wait_time = between(1, 1)

