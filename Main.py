# Imports --------------------------------------------------------------------------------
import pygame
from RMC.Scripts.Projects.PyGameSystemManager.Systems.EventSystem import EventSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.GuiSystem import GuiSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.InputSystem import InputSystem
from RMC.Scripts.Projects.PyGameSystemManager.Systems.MovementSystem import MovementSystem
from RMC.Scripts.Projects.PyGameSystemManager.SystemManager import SystemManager
from RMC.Scripts.Projects.PyGameSystemManager.SystemManagerConfiguration import SystemManagerConfiguration
from RMC.Scripts.Projects.PyGameSystemManager.Systems.RenderSystem import RenderSystem

configuration = SystemManagerConfiguration()
configuration.frameRate = 60

systemManager = SystemManager(pygame, configuration)
systemManager.AddSystem(RenderSystem())
systemManager.AddSystem(InputSystem())
systemManager.AddSystem(EventSystem())
systemManager.AddSystem(MovementSystem())
systemManager.AddSystem(GuiSystem())
systemManager.InitializeSystems()
systemManager.Play()




