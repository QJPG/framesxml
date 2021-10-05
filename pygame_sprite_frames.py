import pygame
from xml.dom import minidom as XML

pygame.init()

class PygameSpriteFrames(object):
	def __init__(self, xml_filename: str):
		self.frames = {}
		self.frame_index = 0
		self.xml_sprites = XML.parse(xml_filename).getElementsByTagName('sprite')
		self.fps = 32
		self.count = 0
		self.playing = False
		self.frame = '<???>'
		self.stopped = False

		for sprite in self.xml_sprites:
			if not self.frames.get(sprite.attributes['name'].value):
				self.frames[sprite.attributes['name'].value] = []
				
				for frame in sprite.getElementsByTagName('frame'):
					frame_data = []
					frame_data.append(int(frame.attributes['x'].value))
					frame_data.append(int(frame.attributes['y'].value))
					frame_data.append(int(frame.attributes['w'].value))
					frame_data.append(int(frame.attributes['h'].value))
					frame_data.append(frame.attributes['image'].value)

					self.frames[sprite.attributes['name'].value].append(self.load_image(frame_data[0], frame_data[1], frame_data[2], frame_data[3], frame_data[4]))
		pass

	def load_image(self, x, y, w, h, filename):
		image = pygame.image.load(filename)
		region = [x, y, w, h]

		"""if len(region) != 4:
			img_rect = [0,0,0,0]
			img_rect[0] = 0
			img_rect[1] = 0
			img_rect[2] = image.get_width()
			img_rect[3] = image.get_height()"""

		new_image = pygame.Surface((region[2], region[3]), pygame.SRCALPHA, 32).convert_alpha()
		#new_image.fill((255,255,255))
		new_image.blit(image, (0, 0), region)
		#new_image.set_alpha(10)
		#new_image.set_colorkey()
		#new_image = pygame.transform.scale(new_image, (new_image.get_rect().w * scale_x, new_image.get_rect().h * scale_y))

		return new_image
		
		#return "<image_object {} {} {} {} {}>".format(x, y, w, h, filename)
		pass

	def play(self, sprite_name: str, repeat = True):
		for spr_name in self.frames.keys():
			if spr_name == sprite_name:
				if self.frame == sprite_name:
					if self.frame_index < len(self.frames[spr_name]) - 1:
						if self.count < self.fps:
							self.count += 6.0
						else:
							self.count = 0
							self.frame_index += 1
					else:
						if self.count < self.fps:
							self.count += 6.0
						else:
							self.count = 0
							if repeat:
								self.frame_index = 0
				else:
					self.frame = spr_name
					self.frame_index = 0
					self.count = 0
		pass

	def image(self):
		if self.frames.get(self.frame) and self.frame_index < len(self.frames[self.frame]):
			return self.frames[self.frame][self.frame_index]
		pass


