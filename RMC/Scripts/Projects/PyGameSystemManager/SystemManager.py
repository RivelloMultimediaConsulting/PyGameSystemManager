"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------
from RMC.Scripts.Projects.PyGameSystemManager.Systems import RenderSystem, InputSystem


class SystemManager (object):

    # Fields -----------------------------------------------------------------------------
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

        if self.systems is not None:
            for system in self.systems:
                if (isinstance(system, systemType)):
                    return system;
        pass

    def InitializeSystems(self):

        self.PG.init()
        self.PG.screen = self.PG.display.set_mode(
            (self.configuration.screenWidth, self.configuration.screenHeight))

        for system in self.systems:
            system.OnInitialize()

        # Depend directly on system(s). TODO: Remove?
        self.renderSystem = self.GetSystem(type(RenderSystem))
        print(self.renderSystem)
        print("can't seem to access renderSystem")


    def Play(self):

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

            #self.renderSystem.PrepareRenderFrame()
            self.UpdateSystems()
           # self.renderSystem.RenderFrame()

            clock.tick(self.configuration.frameRate)
        pass

    def UpdateSystems(self):

        for system in self.systems:
            system.OnUpdate(10)

    # Event Handlers ---------------------------------------------------------------------


