#Make a LIFO stack to reverse a string
#https://www.codewars.com/kata/5682e72eb7354b2f39000021/train/python

# ------------------------ Olesia ------------------------
class SiegeState:
    def __init__(self):
        self.can_move = False
        self.damage = 20
class TankState:
    def __init__(self):
        self.can_move = True
        self.damage = 5
class Tank:
    def __init__(self):
        self.state = TankState()
    def set_state(self, state):
        self.state = state
    def can_move(self):
        return self.state.can_move
    def damage(self):
        return self.state.damage
    

# ------------------------ Mariia ------------------------
class SiegeState:
    def __init__(self):
        self.can_move = False
        self.damage = 20

class TankState:
    def __init__(self):
        self.can_move = True
        self.damage = 5

class Tank:
    def __init__(self):
        self.state = TankState()

    def can_move(self):
        return self.state.can_move
  
    def damage(self):
        return self.state.damage
