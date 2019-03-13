"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class RenderSystem (System):

    # Fields -----------------------------------------------------------------------------

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(RenderSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize(self):
        pass

    def OnUpdate(self, deltaTime):
        pass

    def OnRemoved(self):
        pass

    def PrepareRenderFrame(self):
        self.systemManager.PG.screen.fill((0, 0, 0))
        pass

    def RenderFrame(self):
        self.systemManager.PG.display.flip()
        pass

    # Event Handlers ---------------------------------------------------------------------


