# Importing other classes and things I need
from drawable import Drawable
from datetime import datetime, timedelta

# Initialize the class
class Player(Drawable):
  def __init__(self, pos_x, pos_y, width, height):
    super().__init__(pos_x, pos_y, width, height)
    self.actionTime = datetime.now()
    self.idleAction = "idle"
    self.cooldown = False
    self.staggered = False
    self.hitDetection = False
    self.actionName = "idle"
    self.health = 50
    self.hitTime = datetime.now()

  def setIdleActionName(self,name):
    self.idleAction = name
    
  # Sets the surface to name for drawing with an expiry time in seconds.
  def performAction(self,name,expires_in_seconds=1):
    #print(f'performAction {name} cooldown {self.cooldown}')

    if name == self.idleAction:
      self.cooldown = False
      self.setCurrentSurface(name)
    elif self.cooldown == False:
      self.cooldown = True
      self.setCurrentSurface(name)
      # Record exactly now + seconds as the action time expiry
      if name != self.idleAction:
        self.actionTime = datetime.now() + timedelta(seconds=expires_in_seconds)
        print(f'setting actionTime {self.actionTime}')

  def hit_detection(self):
    if self.hitDetection == False:
      self.health -= 1
      self.hitDetection = True
    
    self.hitTime = datetime.now() + timedelta(seconds=1)

  def update(self):
    now = datetime.now()

    if now > self.actionTime and self.currentName != self.idleAction:
      print(f'setting back to idle {self.currentName}')
      self.cooldown = False
      print(f'player update action expiry now: {now}, actionTime: {self.actionTime}')
      self.performAction(self.idleAction);
    if now > self.hitTime:
      self.hitDetection = False
