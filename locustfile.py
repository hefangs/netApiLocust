from locust import HttpUser, task, between


class StressTestUser(HttpUser):
    wait_time = between(0.5, 1)  # 每个请求后等待时间：0.5到1秒之间随机

    @task
    def catlist_page(self):
        self.client.get("/playlist/catlist")

    @task
    def hot_page(self):
        self.client.get("/playlist/hot")
