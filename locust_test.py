from locust import HttpUser, run_single_user, task
import argparse

def parse_args():
    p = argparse.ArgumentParser(description="Seed Datastore for Tiny Instagram")
    p.add_argument('--users', type=int, default=5)
    return p.parse_args()

class QuickstartUser(HttpUser):
    host = "http://tp1-massive-data-473713.appspot.com/api"
 
    @task
    def timeline(self):
        nb_fail = 0
        reponse_total_time = 0
        args = parse_args()
        with self.client.get("/timeline?user=user"+self.id+"&limit=20") as response :
            if response.text != "Success":
                nb_fail+=1
        reponse_total_time += response.elapsed.total_seconds()
        print("Temps de réponse : ", reponse_total_time)
        print("Nombre d'erreurs : ", nb_fail)
            
            

#ajouter un self.user
#mettre le rate au max dès le début de la commande + faire que chaque utilisateur ne fasse qu'une task

