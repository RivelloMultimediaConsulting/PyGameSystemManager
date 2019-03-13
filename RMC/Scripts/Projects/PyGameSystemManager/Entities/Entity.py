"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------

# Namespace ------------------------------------------------------------------------------

# Class ----------------------------------------------------------------------------------
class Entity (object):

    # Fields -----------------------------------------------------------------------------
    x = 0
    y = 0
    width = None
    height = None
    blittable = None

    # Initialization ---------------------------------------------------------------------
    def __init__(self, blittable):
        if type(self) == Entity:
            raise Exception("<Entity> class must be subclassed before use.")

        self.blittable = blittable
        self.width = self.blittable.get_width()
        self.height = self.blittable.get_height()

        pass

    # Methods ----------------------------------------------------------------------------
    def Blit(self, screen):
        screen.blit(self.blittable, (self.x, self.y))
        pass

    # Event Handlers ---------------------------------------------------------------------


