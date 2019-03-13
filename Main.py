# Imports --------------------------------------------------------------------------------
import pygame

from RMC.Scripts.Projects.PyGameSystemManager.Examples.CustomGameSystem import CustomGameSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.EventSystem import EventSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.InputSystem import InputSystem
from RMC.Scripts.Projects.PyGameSystemManager.SystemManager import SystemManager
from RMC.Scripts.Projects.PyGameSystemManager.SystemManagerConfiguration import SystemManagerConfiguration
from RMC.Scripts.Projects.PyGameSystemManager.Systems.RenderSystem import RenderSystem

configuration = SystemManagerConfiguration()
configuration.frameRate = 60

# Setup the Manager
systemManager = SystemManager(pygame, configuration)

# Add Common Core Systems
# Typically you don't code within here...
systemManager.AddSystem(RenderSystem())
systemManager.AddSystem(InputSystem())
systemManager.AddSystem(EventSystem())

# Add One game-specific system
# Typically you do all your coding within here...
systemManager.AddSystem(CustomGameSystem())

# Start it up!
systemManager.InitializeSystems()
systemManager.Play()




