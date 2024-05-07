 # Memento
class PlayerMemento:
    def __init__(self, name, score):
        self.name = name
        self.score = score


# Originator
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def update_score(self, new_score):
        self.score = new_score

    def display_state(self):
        print(f"Player: {self.name}")
        print("Score:", self.score)


    def save_state(self):
        return PlayerMemento(self.name, self.score)

    def restore_state(self, memento):
        self.name = memento.name
        self.score = memento.score




# Client
if __name__ == "__main__":
  
    player = Player(name="Magdy", score=0)
    player.update_score(100)

    
    print("Current state:")
    player.display_state()

    
    saved_state = player.save_state()
    player.update_score(200)
    saved_state=player.save_state()

    # Display current state
    print("Current state after additional actions:")
    player.display_state()

    # Restore saved state
    print("Restoring saved state:")
    player.restore_state(saved_state)
    player.display_state()
 