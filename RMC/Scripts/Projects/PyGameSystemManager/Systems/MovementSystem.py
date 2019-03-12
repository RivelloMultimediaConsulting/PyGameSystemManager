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
    speed = 5
    x = 0
    y = 0

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
        self.PG.draw.rect(self.PG.screen, (0, 128, 255), self.PG.Rect(self.x, self.y, 60, 60))
        pass

    def OnRemoved(self):
        pass

    def Move (self, deltaX, deltaY):
        self.x += deltaX * self.speed
        self.y += deltaY * self.speed
        print("Move (%s,%s)" % (self.x, self.y))

    # Event Handlers ---------------------------------------------------------------------
    def InputSystem_OnInput (self, event):

        deltaX = 0
        deltaY = 0

        if event.type == self.systemManager.PG.KEYDOWN:

            if event.key == self.systemManager.PG.K_UP:
                deltaY = -1
            elif event.key == self.systemManager.PG.K_DOWN:
                deltaY = 1

            if event.key == self.systemManager.PG.K_RIGHT:
                deltaX = 1
            elif event.key == self.systemManager.PG.K_LEFT:
                deltaX = -1

            self.Move(deltaX, deltaY)
