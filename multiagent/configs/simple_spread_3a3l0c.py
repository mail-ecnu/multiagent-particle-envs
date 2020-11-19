class Config():
    def __init__(self):
        self.num_agents = 3
        self.num_landmarks = 3
        self.collision_free = True

    def get_config(self):
        config = {'num_agents': self.num_agents,
                  'num_landmarks': self.num_landmarks,
                  'collision_free': self.collision_free}
        return config