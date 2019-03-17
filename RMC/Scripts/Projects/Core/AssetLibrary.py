"""---------------------------------------------------------------------------------------
    CONTRIBUTORS
        NAME - EMAIL
---------------------------------------------------------------------------------------"""

# Imports --------------------------------------------------------------------------------
import pygame

# Namespace ------------------------------------------------------------------------------
_image_library = {}

# Class ----------------------------------------------------------------------------------

# Keep previously loaded assets in arrays
# A recommended best practice from https://nerdparadise.com/programming/pygame/part2
class AssetLibrary (object):

    # Fields -----------------------------------------------------------------------------

    # Initialization ---------------------------------------------------------------------
    def __init__(self):
        pass

    # Methods ---------------------------)-------------------------------------------------
    @staticmethod
    def LoadImage (fullPath):

        global _image_library

        image = _image_library.get(fullPath)

        if image == None:
            image = pygame.image.load(fullPath)
            _image_library[fullPath] = image

        return image
        pass

    # Event Handlers ---------------------------------------------------------------------




