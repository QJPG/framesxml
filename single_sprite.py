import os
import pygame, sys

pygame.init()


class SingleSprite(object):
	def __init__(self, filename: str):
		self.filename = filename
		self.image = None
		self.frames = []
		self.image_index = 0
		self.frame_index = 0
		self.time = 0

		lines = None
		data = None

		with open(self.filename, "r") as f:
			lines = f.readlines()

			for i in range(len(lines)):
				if lines[i].endswith("\n") == True:
					lines[i] = lines[i].replace("\n", "")
				
				if len(lines[i]) > 0:
					if lines[i][0] != "@":
						lines[i] = lines[i].replace(" ", "").split("x")
			print(lines)

		for i in range(len(lines)):
			if len(lines[i]) > 0:
				if lines[i][0] == "@":
					if os.path.isfile(lines[i][1:]):
						self.image = pygame.image.load(lines[i][1:])
						data = []
					else:
						print("ERROR -> IMAGE NOT FOUND")
						data = None
				
				if data != None:
					__data = []	
					if type(lines[i]) == list:
						for j in range(len(lines[i])):
							__data.append(int(lines[i][j]))
						data.append(__data)
					
						self.frames.append(__data)
		
		#print(self.images)
		print(self.frames)
		pass

	def play(self, delay = 15, repeat = True):
		if self.frame_index < len(self.frames) - 1:
			if self.time < delay:
				self.time += 0.360
			else:
				#print("tick")
				self.time = 0
				self.frame_index += 1
		else:
			if repeat:
				self.frame_index = 0
		pass

	def get_image_index(self):
		#print(self.image_index, self.frame_index)

		image = self.image
		rect = self.frames[self.frame_index]
		region = [rect[0], rect[1], rect[2], rect[3]]

		new_image = pygame.Surface((region[2], region[3]), pygame.SRCALPHA, 32).convert_alpha()
		new_image.blit(image, (0, 0), region)

		return new_image
		pass

"""
w = pygame.display.set_mode([1024, 600])
spr = SingleSprite("spr_test_test.txt")

while True:
	w.fill((0,0,0))
	spr.play()
	w.blit(spr.get_image_index(), (100, 100))

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			break
	
	pygame.display.flip()
	"""