"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from RMC.Scripts.Projects.PyGameSystemManager.Systems.InputSystem import InputSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class MovementSystem (System):

    # Fields -----------------------------------------------------------------------------
    inputSystem = None

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(MovementSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize (self):
        self.inputSystem = self.systemManager.GetSystem(InputSystem)
        self.inputSystem.OnInput += self.InputSystem_OnInput
        pass

    def OnUpdate(self, deltaTime):
        pass

    def OnRemoved(self):
        pass

    # Event Handlers ---------------------------------------------------------------------
    def InputSystem_OnInput (self, *argv):
        print("yes")
        for arg in argv:
            print("found: " + str(arg))
        pass

