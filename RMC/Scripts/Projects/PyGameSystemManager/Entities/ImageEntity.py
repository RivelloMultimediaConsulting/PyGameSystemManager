"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import pygame
from pygame.color import Color
from pygame.rect import Rect

from RMC.Scripts.Projects.PyGameSystemManager.Entities.Entity import Entity

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class ImageEntity (Entity):

    # Fields -----------------------------------------------------------------------------
    relativePath = None

    # Initialization ---------------------------------------------------------------------
    def __init__(self, x, y, width, height, relativePath):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.relativePath = relativePath
        self.LoadImage()

        pass

    # Methods ----------------------------------------------------------------------------
    def LoadImage (self):
        self.blittable = pygame.image.load(self.relativePath)
        pass

    def Blit (self, screen):
        screen.blit(self.blittable, (self.x, self.y))
        pass

    def __Refresh(self):
        pass
    # Event Handlers ---------------------------------------------------------------------




