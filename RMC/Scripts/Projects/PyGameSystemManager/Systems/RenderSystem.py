"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import os

from RMC.Scripts.Projects.PyGameSystemManager.Entities.AnimatedImageEntity import AnimatedImageEntity
from RMC.Scripts.Projects.PyGameSystemManager.Entities.ImageEntity import ImageEntity
from RMC.Scripts.Projects.PyGameSystemManager.Entities.RectEntity import RectEntity
from RMC.Scripts.Projects.PyGameSystemManager.Entities.TextEntity import TextEntity
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class RenderSystem (System):

    # Fields -----------------------------------------------------------------------------
    entities = []

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(RenderSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize(self):
        pass

    def OnStart(self):
        pass

    def OnUpdate(self, deltaTime):
        for entity in self.entities:
            if callable(getattr(entity, "OnUpdate", None)):
                entity.OnUpdate(deltaTime)

            self.Blit(entity)
        pass

    def OnRemoved(self):
        pass

    def CreateText(self, message):
        entity = TextEntity(message)
        self.AddEntity(entity)
        return entity

    def CreateRect(self, width, height, color):
        entity = RectEntity(0, 0, width, height, color)
        self.AddEntity(entity)
        return entity

    def CreateAnimatedImage(self, x, y, relativePath):
        fullPath = os.path.join(self.systemManager.configuration.projectPath, relativePath)
        entity = AnimatedImageEntity(200, 400, 32, 32, fullPath, 0)
        self.AddEntity(entity)
        return entity

    def CreateImage(self, x, y, relativePath):
        fullPath = os.path.join(self.systemManager.configuration.projectPath, relativePath)
        entity = ImageEntity(200, 400, 32, 32, fullPath)
        self.AddEntity(entity)
        return entity

    def AddEntity(self, entity):
        self.entities.append(entity)
        pass

    def DestroyEntity(self, entity):
        self.entities.remove(entity)
        pass

    def DestroyAllEntities(self):
        self.entities.clear()
        pass

    def Blit (self, entity):
        entity.Blit(self.systemManager.PG.screen)
        pass

    def PrepareRenderFrame(self):
        self.systemManager.PG.screen.fill((0, 0, 0))
        pass

    def RenderFrame(self):
        self.systemManager.PG.display.flip()
        pass

    # Event Handlers ---------------------------------------------------------------------


