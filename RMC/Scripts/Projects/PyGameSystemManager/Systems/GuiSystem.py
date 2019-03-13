"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from RMC.Scripts.Projects.PyGameSystemManager.Entities.TextEntity import TextEntity
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class GuiSystem (System):

    # Fields -----------------------------------------------------------------------------

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(GuiSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize(self):
        pass

    def OnUpdate(self, deltaTime):
        screenRect = self.systemManager.PG.screen.get_rect()

        textEntity = TextEntity( "Hello World!")
        textEntity.x = screenRect.width/2 - textEntity.width / 2
        textEntity.y = screenRect.height/2 - textEntity.height / 2
        textEntity.Blit(self.systemManager.PG.screen)

        print(textEntity.x)
        print(textEntity.y)
        print(textEntity.blittable)




        pass

    def OnRemoved(self):
        pass

    # Event Handlers ---------------------------------------------------------------------


