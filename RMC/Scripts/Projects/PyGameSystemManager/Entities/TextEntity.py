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
    __textColor = (128, 0, 0, 0)
    textSize = 30

    # Properties -------------------------------------------------------------------------
    def SetTextColor(self, textColor):
        self.__textColor = textColor
        self.__Refresh()
        pass

    def GetTextColor(self):
        return self.__textColor;

    # Initialization ---------------------------------------------------------------------
    def __init__(self, text):
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
        font = pygame.font.SysFont("arial", self.textSize)
        self.SetBlittable(font.render(str(self.text), True, self.__textColor))
        pass
    # Event Handlers ---------------------------------------------------------------------



