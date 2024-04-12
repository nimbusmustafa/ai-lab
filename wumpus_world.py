import random
class WumpusWorld:
    def __init__(self, size):


        self.size = size
        self.grid = [['-' for _ in range(size)] for _ in range(size)]
        self.agent_location = (0, 0)
        self.gold_location = None
        self.wumpus_location = None
        self.pit_locations = set()
        self.generate_world()


    def generate_world(self):


        self.gold_location = (random.randint(0, self.size-1),
                            random.randint(0, self.size-1))
        while True:
            self.wumpus_location = (random.randint(0, self.size-1),
                                    random.randint(0, self.size-1))
            if self.wumpus_location != self.gold_location:
                break
            while True:
                pit_location = (random.randint(0, self.size-1), random.randint(0, self.size-1))
                if pit_location != self.gold_location and pit_location != self.wumpus_location:
                    self.pit_locations.add(pit_location)
                    break
    def is_valid_location(self, location):


        x, y = location
        return 0 <= x < self.size and 0 <= y < self.size
    def adjacent_locations(self, location):


        x, y = location
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [loc for loc in neighbors if self.is_valid_location(loc)]
    def check_perceptions(self):


        perceptions = []
        x, y = self.agent_location
        # Check for pits
        if (x, y) in self.pit_locations:
            perceptions.append("Breeze")
        # Check for Wumpus
        if (x, y) == self.wumpus_location:
            perceptions.append("Stench")
        # Check for gold
        if (x, y) == self.gold_location:
            perceptions.append("Glitter")
            return perceptions
    def move(self, direction):


        x, y = self.agent_location
        if direction == "UP" and x > 0:
            self.agent_location = (x-1, y)
        elif direction == "DOWN" and x < self.size-1:
            self.agent_location = (x+1, y)
        elif direction == "LEFT" and y > 0:
            self.agent_location = (x, y-1)
        elif direction == "RIGHT" and y < self.size-1:
            self.agent_location = (x, y+1)
    def play_game(self):


        print("Wumpus World Game\n")
        while True:
            perceptions = self.check_perceptions()
            print(f"Current location: {self.agent_location}")
            print("Perceptions:", ", ".join(perceptions))
            if "Glitter" in perceptions:
                print("You found the gold!")
                break
            action = input("Enter action(UP, DOWN, LEFT, RIGHT, SHOOT, GRAB, or QUIT):").upper()
            if action == "QUIT":
                print("Exiting the game.")
                break
            elif action in ["UP", "DOWN", "LEFT", "RIGHT"]:
                self.move(action)
            elif action == "SHOOT":
                print("You shoot an arrow.")
            elif action == "GRAB" and "Glitter" in self.check_perceptions():
                print("You grab the gold.")
                print()
# Take manual input for the size of the Wumpus World
size = int(input("Enter the size of the Wumpus World (square matrix): "))
# Create and play the Wumpus World game
game = WumpusWorld(size)
game.play_game()
