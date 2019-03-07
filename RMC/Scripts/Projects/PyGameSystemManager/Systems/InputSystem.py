"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from RMC.Scripts.Projects.EventDispatcher.EventDispatcher import EventDispatcher
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class InputSystem (System):

    # Fields -----------------------------------------------------------------------------
    inputPressed = None
    OnInput = EventDispatcher()

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(InputSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize (self):
        pass

    def OnUpdate(self, deltaTime):

        for event in self.systemManager.inputEvent:

            if event.type == self.PG.KEYDOWN:
                print("ok")
                self.inputPressed = self.systemManager.inputPressed
                self.OnInput.DispatchEvent()
        pass

    def OnRemoved(self):
        pass

    # Event Handlers ---------------------------------------------------------------------


