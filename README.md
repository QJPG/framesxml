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

```xml
<?xml version="1.0" encoding="utf-8"?>
<sprites>
  <sprite name = "spr_category_name">
    <frame x = "0" y = "0" w = "32" h = "32" image = "my_spritesheet.png"/>
  </sprite>
</sprites>
```

# Single Sprite
Create an animated sprite object

```
@my_image_001.png  <-----image filename

0x0x32x32 <-----image regions X, Y, W, H
0x32x32x32
0x64x32x32
```

```python
import single_sprite as sp

...

my_sprite = sp.SingleSprite("spr_file.txt")
my_sprite.play(delay = 15, repeat = True)

pygame_window.blit(my_sprite.get_image_index(), (x, y))

...
```
