"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
from pygame.color import Color
from pygame.rect import Rect

from RMC.Scripts.Projects.EventDispatcher.EventDispatcher import EventDispatcher
from RMC.Scripts.Projects.PyGameSystemManager.Systems.AudioSystem import AudioSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.InputSystem import InputSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.RenderSystem import RenderSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.System import System

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class CustomGameSystem (System):

    # Fields -----------------------------------------------------------------------------
    inputSystem = None
    renderSystem = None
    audioSystem = None
    guiSystem = None
    scoreTextEntity = None
    restartTextEntity = None
    coins = []
    score = 0
    characterSpeed = 30
    OnScoreChanged = EventDispatcher()
    OnGameStarted = EventDispatcher()

    # Properties -------------------------------------------------------------------------
    def SetScore(self, value):
        self.score = value
        self.OnScoreChanged.DispatchEvent(self.score)
        pass

    def GetScore(self):
        return self.score

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ----------------------------------------------------------------------------
    def OnAdded(self, systemManager):
        super(CustomGameSystem, self).OnAdded(systemManager)
        pass

    def OnInitialize(self):

        # Input
        self.inputSystem = self.systemManager.GetSystem(InputSystem)
        self.inputSystem.OnInput += self.InputSystem_OnInput

        # Render
        self.renderSystem = self.systemManager.GetSystem(RenderSystem)

        # Audio
        self.audioSystem = self.systemManager.GetSystem(AudioSystem)


        pass

    def OnStart(self):
        self.StartGame()
        pass

    def OnUpdate(self, deltaTime):

        for coin in self.coins[:]:
            if coin.GetBoundsRect().colliderect(self.CustomCharacter.GetBoundsRect()):
                # Reward points
                self.SetScore(self.GetScore() + 10)

                # Play Sound
                self.audioSystem.PlaySound("RMC/Audio/CoinCollected.wav")

                # Remove coin from rendering list
                self.renderSystem.DestroyEntity(coin)

                # Remove coin from my list
                self.coins.remove(coin)
        pass

    def OnRemoved(self):
        pass

    def StartGame(self):

        self.renderSystem.DestroyAllEntities()

        # Main Character
        self.CustomCharacter = self.renderSystem.CreateRect(60, 60, Color(0, 0, 255, 255));
        self.CustomCharacter.SetPosition(100, 100)

        # Gold Coins
        self.coins = []
        for i in range(5):
            coin = self.renderSystem.CreateAnimatedImage(0, 0, "RMC/Images/Coin.png")
            coin.SetPosition(50 + i * 75, 200)
            self.coins.append(coin)

        self.OnGameStarted.DispatchEvent(None)
        pass

    def RestartGame(self):
        self.audioSystem.PlaySound("RMC/Audio/StartGame.wav")
        self.StartGame()
        pass

    # Event Handlers ---------------------------------------------------------------------
    def InputSystem_OnInput(self, event):

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

        self.MoveCharacterBy(deltaX * self.characterSpeed, deltaY * self.characterSpeed)


    def MoveCharacterBy(self, deltaX, deltaY):

        if deltaX == 0 and deltaY == 0:
            return;

        # Play Sound
        self.audioSystem.PlaySound("RMC/Audio/Move.wav")

        # Move
        self.CustomCharacter.x += deltaX
        self.CustomCharacter.y += deltaY
        pass
