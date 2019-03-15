# Imports --------------------------------------------------------------------------------
import pygame
from RMC.Scripts.Projects.PyGameSystemManager.Examples.CustomGameSystem import CustomGameSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.EventSystem import EventSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.InputSystem import InputSystem
from RMC.Scripts.Projects.PyGameSystemManager.SystemManager import SystemManager
from RMC.Scripts.Projects.PyGameSystemManager.SystemManagerConfiguration import SystemManagerConfiguration
from RMC.Scripts.Projects.PyGameSystemManager.Systems.RenderSystem import RenderSystem

# Config ----------------------------------------------------------------------------------
configuration = SystemManagerConfiguration()
configuration.frameRate = 60

# Create Manager --------------------------------------------------------------------------
systemManager = SystemManager(pygame, configuration)

# Add Core Systems ------------------------------------------------------------------------
systemManager.AddSystem(RenderSystem())
systemManager.AddSystem(InputSystem())
systemManager.AddSystem(EventSystem())

# Add Custom Systems ----------------------------------------------------------------------
systemManager.AddSystem(CustomGameSystem())

# Start -----------------------------------------------------------------------------------
systemManager.InitializeSystems()
systemManager.Play()




