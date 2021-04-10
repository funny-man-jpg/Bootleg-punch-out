# Import the rest of the classes and a couple other things I need

import random
import pygame
from drawable import Drawable
from player import Player
from pygame.locals import (
  K_a,
  K_s,
  K_z,
  K_x,
  KEYDOWN,
)

# Initialize a new class. In this case, it's going to be the game class
class Game:
  # Initializing the game class, which consists of screen parameters, and creating
  # new players.
  def __init__(self, screen_w, screen_h):
    super().__init__()
    pygame.init()
    self.screen_w = screen_w
    self.screen_h = screen_h
    size = [screen_w, screen_h]
    font = pygame.font.SysFont("comicsans", 30)
    self.winText = font.render("WIN", 1, (0,0,0))
    self.loseText = font.render("LOSE", 1, (0,0,0))
    pygame.display.set_caption('punch in')
    self.screen = pygame.display.set_mode(size)
    self.player = Player(100, 50, 200, 200)
    self.player.loadFile('assets/p1Idle.png','idle')
    self.player.loadFile('assets/p1HeadPunch.png','headpunch')
    self.player.loadFile('assets/p1BodyPunch.png','bodypunch')
    self.player.loadFile('assets/p1HeadBlock.png','headblock')
    self.player.loadFile('assets/p1BodyBlock.png','bodyblock')
    self.player.loadFile('assets/p1Staggered.png','staggered')
    self.player.setCurrentSurface('idle')
    self.player.setIdleActionName('idle')
    self.enemy = Player(200, 50, 200, 200)
    self.enemy.loadFile('assets/p2Idle.png','idle')
    self.enemy.loadFile('assets/p2HeadPunch.png','headpunch')
    self.enemy.loadFile('assets/p2BodyPunch.png','bodypunch')
    self.enemy.loadFile('assets/p2HeadBlock.png','headblock')
    self.enemy.loadFile('assets/p2BodyBlock.png','bodyblock')
    self.enemy.loadFile('assets/p2Staggered.png','staggered')
    self.enemy.setCurrentSurface('idle')
    self.enemy.setIdleActionName('idle')
    self.players = []
    self.players.append(self.player)
    self.players.append(self.enemy)

  
# This function will do everything regarding key presses, and the quit function which
# Allows the program to close.
  def process_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return True
      # If a key is pressed
      if event.type == KEYDOWN:
        # Check if the key pressed is one in this if statement
        if event.key == K_a:
          # Perform the action if it is.
          # Check to see if the opponent is blocking or not, to activate the staggered state or
          # Remove health.
          # COMMENT ABOVE SUBJECT TO CHANGE
          if self.enemy.currentName == "headblock":
            self.player.performAction('staggered', 2)
          else:
            self.player.performAction('headpunch')
        # The rest of the function is the same as above but different actions/keys
        if event.key == K_s:
          if self.enemy.currentName == "bodyblock":
            self.player.performAction('staggered', 2)
          else:
            self.player.performAction('bodypunch')
        if event.key == K_z:
          self.player.performAction('headblock')
        if event.key == K_x:
          self.player.performAction('bodyblock')
    # DELETE THIS PRINT STATMENT LATER
    print(self.player.health)
    # If health is 0 then quit
    if self.player.health == 0 or self.enemy.health == 0:
      #if self.player.health == 0:
        #display_surface.blit(text, textRect)
      return True
    else:
      return False

  # This function is used to detect hits
  def hit_detection(self):
    # Just a bunch of checks, each either causeing a stagger or losing hp
    if self.enemy.currentName == "headblock" and self.player.currentName == "headpunch":
      self.player.performAction('staggered', 2)
    elif self.enemy.currentName != "headblock" and self.player.currentName == "headpunch":
      self.player.hit_detection()
    if self.enemy.currentName == "bodyblock" and self.player.currentName == "bodypunch":
      self.player.performAction('staggered', 2)
    elif self.enemy.currentName != "bodyblock" and self.player.currentName == "bodypunch":
      self.player.hit_detection()
    if self.player.currentName == "headblock" and self.enemy.currentName == "headpunch":
      self.enemy.performAction('staggered', 2)
    elif self.player.currentName != "headblock" and self.enemy.currentName == "headpunch":
      self.enemy.hit_detection()
    if self.player.currentName == "bodyblock" and self.enemy.currentName == "bodypunch":
      self.enemy.performAction('staggered', 2)
    elif self.player.currentName == "bodyblock" and self.enemy.currentName == "bodypunch":
      self.enemy.hit_detection()

  def p2_ai(self):
    #if not self.enemy.staggered:
    attack = random.randint(0, 3)
    if attack == 0:
      if self.player.currentName == "bodyblock":
        self.enemy.performAction('staggered', 2)
      else:
        self.enemy.performAction('bodypunch')
    if attack == 1:
      self.enemy.performAction('bodyblock')
    if attack == 2:
      if self.player.currentName == "headblock":
        self.enemy.performAction('staggered', 2)
      else:
        self.enemy.performAction('headpunch')
    if attack == 3:
      self.enemy.performAction('headblock')


  def display_frame(self, screen):
    screen.fill((255, 255, 255))

    for player in self.players:
      if isinstance(player, Drawable):
        player.draw(screen)
    
    pygame.display.flip()


  def run(self):
    done = False
    font = pygame.font.SysFont("comicsans", 30)
    clock = pygame.time.Clock()
    while not done:
      done = self.process_events()
      self.p2_ai()
      self.display_frame(self.screen)
      self.hit_detection()
      playerHealth = font.render("HP: " + str(self.player.health), 1, (0,0,0))
      enemyHealth = font.render("HP: " + str(self.enemy.health), 1, (0,0,0))
      for player in self.players:
        player.update()
      clock.tick(60)

    pygame.quit()