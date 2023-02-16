#Copyright 2023 Hudson Rocke
import pygame, sys, keyboard, settings
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()
clock = pygame.time.Clock()



'''Startup functions'''

def screen():
    size = settings.SIZE
    full_screen = settings.FULLSCREEN
    if size == None:
        if not full_screen:
            #Get the size of the user's screen
            width = pygame.display.Info().current_w
            height = pygame.display.Info().current_h
            screen = pygame.display.set_mode((width, height - 70), RESIZABLE)
            return screen
        else:
            screen = pygame.display.set_mode((100, 100), FULLSCREEN)
            return screen
    if size != None:
        screen = pygame.display.set_mode((size[0], size[1]), RESIZABLE)
        return screen
            
def fill(color = (0, 0, 0)):
    screen_display.fill(color)
        
def kill(key = None):
    if key == None:
        pygame.quit()
        sys.exit()
    else:
        key = Sense().sense_key(key)
        if key:
            pygame.quit()
            sys.exit()
        
def run(color = (0, 0, 0), flip = False):
    global clock
    icon()
    caption()
    sense_exit()
    if not flip:
        pygame.display.update()
    else:
        pygame.display.flip()
    clock.tick(settings.FPS)
    fill(color)
    
def icon(icon = settings.ICON):
    icon = pygame.image.load(icon)
    pygame.display.set_icon(icon)
    
def caption(caption = settings.CAPTION):
    pygame.display.set_caption(caption)
        
global screen_display
screen_display = screen()    


'''Sense events'''

def sense_key(key):
    key_rec = False
    key_rec = keyboard.is_pressed(key)
    return key_rec
    
def sense_exit(kill = True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if kill:
                pygame.quit()
                sys.exit()
            else:
                return 0
                
def sense_press(key, pressed):
    if sense_key(key):
        if pressed == False:
            pressed = True
            return pressed
    if not sense_key(key):
        pressed = False
        return pressed
            
'''Render Images'''
def display(img, input_coords = [0, 0], outline = False,  scale = [1, 1], rotation = 0, outline_width = 1, outline_color = (255, 255, 255)):
    global screen_display
    x_scale = scale[0]
    y_scale = scale[1]
    x_pos = input_coords[0]
    y_pos = input_coords[1]
    img_load = pygame.image.load(img)
    coords = (x_pos + (img_load.get_width()*x_scale)/1.3, y_pos + (img_load.get_height()*y_scale)/1.3)
    coords = [coords[0], coords[1]]
    scale = (x_scale*50, y_scale*50)
    img_load = pygame.transform.scale(img_load, scale)
    img_load = pygame.transform.rotate(img_load, rotation)
    mask = pygame.mask.from_surface(img_load)
    mask_surf = mask.to_surface()
    screen_display.blit(img_load, (coords[0] - int(img_load.get_width() / 2), coords[1] - int(img_load.get_height() / 2)))
    if outline:
        for point in mask.outline():
            x = (point[0] + x_pos) -x_scale/3.5
            y = (point[1] + y_pos)-y_scale/3.5
            pygame.draw.circle(screen_display, outline_color, (x, y), outline_width)
        
        
'''Easy Gui'''
    
def backdrop(darkness = 125, color = (0, 0, 0)):
    global screen_display
    dark = pygame.Surface((pygame.display.Info().current_w, pygame.display.Info().current_h))
    dark.set_alpha(darkness)
    dark.fill(color)
    screen_display.blit(dark, (0, 0))

def button(coords, size, text, color = (100, 100, 100), outline_color = (200, 200, 200), font = "freesansbold.ttf", text_size = 20, text_color = "black"):
    button = pygame.Rect((coords[0], coords[1]), (size[0], size[1]))
    pygame.draw.rect(screen_display, color, button, 100, 15)
    if button.collidepoint(pygame.mouse.get_pos()):
        button_outline = pygame.Rect((coords[0], coords[1]), (size[0], size[1]))
        pygame.draw.rect(screen_display, outline_color, button_outline, 100, 15)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(pygame.mouse.get_pos()):
                return True
        if event.type == pygame.QUIT:
            kill()
    
    font_comp = pygame.font.Font(font, text_size)
    text = font_comp.render(text, True, text_color)
    textRect = text.get_rect()
    size = list(size)
    coords = list(coords)
    textRect.center = (coords[0]+size[0]//2, coords[1]+size[1]//2)
    screen_display.blit(text, textRect)
    return False

def text(coords, text, size = 20, color = "black", font = "freesansbold.ttf"):
    font = pygame.font.Font(font, size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    coords = list(coords)
    textRect.center = (coords[0], coords[1])
    screen_display.blit(text, textRect)
    
    
'''Play sounds'''
   
def play_music(file, volume = 1):
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play(-1)

def play_sound(sound, volume = 1, channels = 10):
    mixer.set_num_channels(channels)
    mixer.Sound(sound).play()
    mixer.Sound(sound).set_volume(volume)

if __name__ != "__main__":
    screen()