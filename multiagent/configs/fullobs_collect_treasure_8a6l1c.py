class Config():
    def __init__(self):
        self.num_agents = 8
        self.num_collectors = 6
        self.collision_free = False

    def get_config(self):
        config = {'num_agents': self.num_agents,
                  'num_collectors': self.num_collectors,
                  'collision_free': self.collision_free}
        return config