"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------

class SystemManager (object):

    # Fields -----------------------------------------------------------------------------
    IsPlaying = False
    systems = []
    PG = None
    inputEvent = None
    inputPressed = None
    configuration = None


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
        for system in self.systems:
            if (isinstance(system, systemType)):
                return system;
        pass

    def InitializeSystems(self):

        self.PG.init()
        self.PG.display.set_mode((self.configuration.screenWidth,
                                  self.configuration.screenHeight))


        for system in self.systems:
            print("init for " + str(system))
            system.OnInitialize()

    def Play(self):

        clock = self.PG.time.Clock()

        self.IsPlaying = True

        while self.IsPlaying:

            # event.get() can only be called once per tick,
            # so store it for reuse
            self.inputEvent = self.PG.event.get()
            self.inputPressed = self.PG.key.get_pressed();
            for event in self.inputEvent:
                if event.type == self.PG.QUIT:
                    self.IsPlaying = False

            self.UpdateSystems();

            clock.tick(self.configuration.frameRate)
        pass

    def UpdateSystems(self):

        for system in self.systems:
            #print("init for " + str(system))
            system.OnUpdate(10)

    # Event Handlers ---------------------------------------------------------------------


