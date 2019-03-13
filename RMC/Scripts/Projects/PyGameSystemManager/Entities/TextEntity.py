"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import pygame

from RMC.Scripts.Projects.PyGameSystemManager.Entities.Entity import Entity

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class TextEntity (Entity):

    # Fields -----------------------------------------------------------------------------
    text = None

    # Initialization ---------------------------------------------------------------------
    def __init__(self, text):
        font = pygame.font.SysFont("arial", 30)
        self.SetText(text)
        pass

    # Methods ----------------------------------------------------------------------------
    def SetText(self, text):
        self.text = text
        self.__Refresh()
        pass

    def Blit(self, screen):
        screen.blit(self.blittable, (self.x, self.y))
        pass

    def __Refresh(self):
        font = pygame.font.SysFont("arial", 30)
        self.SetBlittable(font.render(str(self.text), True, (0, 128, 0)))
        pass
    # Event Handlers ---------------------------------------------------------------------



