from asteroid import Asteroid
import json

class ScoreManager():

    def __init__(self):
        self.score = 0


    def sum_points(self, asteroid :Asteroid):
        if asteroid.radius == 60:
            points = 100
        elif asteroid.radius == 40:
            points = 200
        else: points = 300

        self.score += points
    

    def get_score(self):
        return self.score

    def save(self, name):
        
        new_score = {
            "name": name,
            "score": self.score
        }

        scores_path = "scores.json"

        try:
            with open(scores_path, "r") as f:
                data = json.load(f)
            data.append(new_score)
            with open(scores_path, "w") as f:
                json.dump(data,f, indent=4)

        except (FileNotFoundError, json.JSONDecodeError):
            data = []
            data.append(new_score)
            with open(scores_path, "w") as f:
                    json.dump(data,f, indent=4)