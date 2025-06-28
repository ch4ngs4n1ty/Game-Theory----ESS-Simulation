class Individual:

    def __init__(self, id:int, strategy:str, resource:int = 0, status:bool = True):

        self.id = id
        self.strategy = strategy
        self.resource = resource

        #If status is True then it's alive, if False then it's dead
        self.status = status

    def getId(self):

        return self.id

    def getStrategy(self):

        return self.strategy

    def getResource(self):

        return self.resource

    def addResource(self, amount:int):

        self.resource += amount

    def subtractResource(self, amount:int):

        self.resource -= amount

        if self.resource < 0:

            self.status = False


    def getStatus(self):

        return self.status

    def __str__(self):

        if not self.alive:
            return f"Individual[{self.id}]=DEAD:{self.resource}"
        return f"Individual[{self.id}]={self.strategy}:{self.resource}"
