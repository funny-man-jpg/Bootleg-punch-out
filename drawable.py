import pygame

# Initialize the class
class Drawable:
  def __init__(self, pos_x, pos_y, width, height):
    super().__init__()
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.width = width
    self.height = height
    # Contains "name" to "surface" for each image
    self.surfaces = {}
    # Current surface with an image to draw
    self.surface = None
    # Current name of the surface to draw
    self.currentName = ""
    

  # Loads files and gives them a nickname
  def loadFile(self, file, name):
    if file is not None:
      self.file = file
      image = pygame.image.load(file)
      self.surfaces[name] = pygame.transform.smoothscale(image, (self.width, self.height))
  
  # Sets which image to draw
  def setCurrentSurface(self,name):
    self.surface = self.surfaces[name]
    self.currentName = name

  # Actually draws the image
  def draw(self, surface):
    if self.surface is not None:
        surface.blit(self.surface,(self.pos_x, self.pos_y))