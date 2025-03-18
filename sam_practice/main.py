
class cell():
    #TODO
    def __init__(self):
        self.grid = [[], []]
        self.is_alive = ...

    def check_neighbours(self) -> bool:
        # Does it have fewer than 2 neighbours - kill it
        # Does it have 2 or 3 neighbours - lives
        # Does it have more than 3 neighbours - kill it
        # Is it empty - is_alive = True
        ...
    
    def kill_cell(self) -> None:
        #TODO
        ...
    
    def revive_cell(self) -> None:
        #TODO
        ...
    
