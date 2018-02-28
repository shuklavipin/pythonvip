def fswebcam(x,y)
import pygame.camera
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
import pygame.image
pygame.image.save(img, "photo.jpg")
pygame.camera.quit()
fswebcam(1280,270)
