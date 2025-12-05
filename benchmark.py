from locust import HttpUser, task, constant, events
from locust.exception import StopUser


user_ids = [i for i in range(1,51)]


class MyUser(HttpUser):
    host = "https://tp1-massive-data-473713.appspot.com"
    wait_time = constant(0)
    my_id = None

    def on_start(self):
        if len(user_ids) > 0:
            self.my_id = user_ids.pop(0)
            #print("User : "+str(self.my_id))
        else:
            # Sécurité si la liste est vide
            #print("Plus d'ID disponibles !")
            self.environment.runner.quit()

    @task
    def action(self):
        if self.my_id:
            # 3. Utilisation de l'ID
            self.client.get(f"/api/timeline?user=user{self.my_id}&limit=20")
        
        
        raise StopUser()
    

##locust -f locustfile.py --headless -u 50 -r 50 --iterations 50


