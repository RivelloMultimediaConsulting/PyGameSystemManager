"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import pygame

from RMC.Scripts.Projects.PyGameSystemManager.Entities.ImageEntity import ImageEntity

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------


class AnimatedImageEntity (ImageEntity):

    # Fields -----------------------------------------------------------------------------
    timeSinceLastFrame = 0
    imageIndex = 0
    maxImageIndex = 7

    # Initialization ---------------------------------------------------------------------
    def __init__(self, x, y, width, height, relativePath, imageIndex):
        super(AnimatedImageEntity, self).__init__(x, y, width, height, relativePath)
        self.SetImageIndex(imageIndex)
        pass

    # Methods ----------------------------------------------------------------------------
    def SetImageIndex(self, imageIndex):
        self.imageIndex = imageIndex
        pass

    def OnUpdate (self, deltaTime):

        self.timeSinceLastFrame += deltaTime

        if self.timeSinceLastFrame > 100:
            self.timeSinceLastFrame = 0
            self.imageIndex = self.imageIndex + 1
            if self.imageIndex > self.maxImageIndex:
                self.imageIndex = 0
        pass

    def Blit (self, screen):
        top = 0
        left = self.imageIndex * self.width
        screen.blit(self.blittable, (self.x, self.y), (left, top, self.width, self.height))
        pass

    # Event Handlers ---------------------------------------------------------------------
