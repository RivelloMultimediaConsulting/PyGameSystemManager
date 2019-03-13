"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------
from types import ModuleType

from RMC.Scripts.Projects.PyGameSystemManager.Systems.RenderSystem import RenderSystem


class SystemManager (object):

    # Fields -----------------------------------------------------------------------------
    IsInitialized = False
    IsPlaying = False
    systems = []
    PG = None
    inputEvents = None
    configuration = None
    renderSystem = None

    # Initialization ---------------------------------------------------------------------

    def __init__(self, pygame, systemManagerConfiguration):
        self.PG = pygame
        self.configuration = systemManagerConfiguration;
        pass

    # Methods ----------------------------------------------------------------------------

    def AddSystem(self, system):
        self.systems.append(system)
        system.OnAdded(self)
        pass

    def GetSystem(self, systemType):

        # I noticed if the scope using this method
        # has improper import statements, a module (package?) is passed
        # instead of the required type
        if isinstance(systemType, ModuleType):
            raise Exception("GetSystem() cannot accept module as argument. Ensure you import and pass a type instead.")
            return None

        if self.systems is not None:
            for system in self.systems:
                if isinstance(system, systemType):
                    return system

        return None

    def InitializeSystems(self):

        self.PG.init()
        self.PG.screen = self.PG.display.set_mode(
            (self.configuration.screenWidth, self.configuration.screenHeight))

        for system in self.systems:
            system.OnInitialize()

        # Depend directly on system(s). TODO: Remove?
        self.renderSystem = self.GetSystem(RenderSystem)

        if self.renderSystem is not None:
            self.IsInitialized = True

        return

    def Play(self):

        if self.IsInitialized is False:
            raise Exception("Play() cannot be called when self.IsInitialized is False")
            return

        clock = self.PG.time.Clock()

        self.IsPlaying = True

        while self.IsPlaying:

            # event.get() can only be called once per tick,
            # so store it for reuse
            self.inputEvents = self.PG.event.get()

            # We do exactly ONE input check here. To keep the window open
            for event in self.inputEvents:
                if event.type == self.PG.QUIT:
                    self.IsPlaying = False

            self.renderSystem.PrepareRenderFrame()
            self.UpdateSystems()
            self.renderSystem.RenderFrame()

            clock.tick(self.configuration.frameRate)
        pass

    def UpdateSystems(self):

        for system in self.systems:
            system.OnUpdate(10)

    # Event Handlers ---------------------------------------------------------------------


