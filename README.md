# framesxml
Animation Frames in XML file with pygame
<img src = "2021-10-05 (2).png ">

*Usage:*
```python
import pygame_sprite_frames as psf

...

animation = psf.PygameSpriteFrames("my_spr_frames_tree.xml")

animation.play("sprite_animation_name")

pygame_window.blit(animation.image(), (0,0))

...
```
