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
    def __init__(self, blittable=None):
        if type(self) == Entity:
            raise Exception("<Entity> class must be subclassed before use.")

        if blittable is not None:
            self.SetBlittable(blittable)
        pass

    # Methods ----------------------------------------------------------------------------
    def SetBlittable(self, blittable):
        self.blittable = blittable
        self.width = self.blittable.get_width()
        self.height = self.blittable.get_height()
        pass

    def Blit(self):
        if type(self) == Entity:
            raise Exception("Blit() method must overridden before use.")
        pass

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        pass

    # Event Handlers ---------------------------------------------------------------------


