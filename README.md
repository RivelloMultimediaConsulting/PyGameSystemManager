PyGameSystemManager
=============

<img src="https://raw.githubusercontent.com/RivelloMultimediaConsulting/PyGameSystemManager/master/Documentation/PyGameSystemManager_Screenshot01.png" width="500" />
  
This is a simple manager to organize high-level "system" classes in your PyGame game projects. Each system is independent but may access others through a centralized locator. 

It is not a fully robust application architecture (e.g. MVC).

I created this during my first week of learning Python. I bring 19+ years of gaming experience to this small project.

**Details**

* <a href="https://www.python.org/" target="_blank">Python 3.7.0</a>
* <a href="https://www.pygame.org/" target="_blank">PyGame 1.9.4</a>
* A light-weight <a href="https://en.wikipedia.org/wiki/Object-oriented_programming" target="_blank">Object Oriented Programming (OOP) architecture for gaming.</a>

**PyGameSystemManager Features**

* **Examples/CustomGameSystem:** The core game-specific logic including layout and win/loss conditions
* **Examples/CustomGuiSystem:** Handles game-specific text and buttons
* **Examples/CustomCharacterEnity:** Subclass of the entity concept which renders to the screen
* **AudioSystem:** Renders all **Audio**
* **InputSystem:** Captures PyGame input and dispatches as events to subscribers
* **RenderSystem:** Renders all **Entity** subclasses to the screen

**Video**
* (I'm evaluating some new editing software. Pardon the temporary watermark)

<a href="https://youtu.be/DEeFTcsFk2I">
  <img src="https://raw.githubusercontent.com/RivelloMultimediaConsulting/PyGameSystemManager/master/Documentation/PyGame_Part01_Thumbnail.png" width="300" />
  
</a>
    
Created By
=============

- Samuel Asher Rivello: <a href="https://twitter.com/srivello/" target="_blank">@srivello</a>, <a href="http://www.github.com/RivelloMultimediaConsulting/ target="_blank"">Github</a>, <a href="http://RivelloMultimediaConsulting.com/unity/" target="_blank">RivelloMultimediaConsulting.com</a>, <a href="http://www.SamuelAsherRivello.com" target="_blank">SamuelAsherRivello.com</a>

