"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from pygame.color import Color
from pygame.rect import Rect

from RMC.Scripts.Projects.PyGameSystemManager.Examples.CustomGameSystem import CustomGameSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.AudioSystem import AudioSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.InputSystem import InputSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.RenderSystem import RenderSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class CustomGuiSystem (System):

    # Fields -----------------------------------------------------------------------------
    customGameSystem = None
    inputSystem = None
    renderSystem = None
    scoreTextEntity = None
    restartTextEntity = None

    # Properties -------------------------------------------------------------------------

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(CustomGuiSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize(self):

        # Input
        self.inputSystem = self.systemManager.GetSystem(InputSystem)
        self.inputSystem.OnInput += self.InputSystem_OnInput

        # Game
        self.customGameSystem = self.systemManager.GetSystem(CustomGameSystem)
        self.customGameSystem.OnScoreChanged += self.CustomGameSystem_OnScoreChanged
        self.customGameSystem.OnGameStarted += self.CustomGameSystem_OnGameStarted

        # Render
        self.renderSystem = self.systemManager.GetSystem(RenderSystem)

        pass

    def OnStart(self):
        pass

    def OnUpdate(self, deltaTime):
        pass

    def OnRemoved(self):
        pass

    def SetScore(self, value):
        self.score = value
        self.scoreTextEntity.SetText("Score: " + str(self.score))

    # Event Handlers ---------------------------------------------------------------------
    def CustomGameSystem_OnScoreChanged(self, value):
        self.SetScore(value)
        pass

    def CustomGameSystem_OnGameStarted(self, value):

        screenRect = self.systemManager.PG.screen.get_rect()

        # Score Text
        self.scoreTextEntity = self.renderSystem.CreateTextEntity("")
        self.scoreTextEntity.x = 10
        self.scoreTextEntity.y = 0
        self.SetScore(0)

        # Restart Button Text
        self.restartTextEntity = self.renderSystem.CreateTextEntity("Restart?")
        self.restartTextEntity.x = screenRect.width - self.restartTextEntity.width - 10
        self.restartTextEntity.y = 0
        pass

    def InputSystem_OnInput(self, event):

        if event.type == self.systemManager.PG.MOUSEBUTTONDOWN:
            mouse = self.systemManager.PG.mouse.get_pos()
            if self.restartTextEntity.GetBoundsRect().contains(Rect(mouse[0], mouse[1], 1, 1)):
                self.customGameSystem.RestartGame()
                pass
