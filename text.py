import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

#make colors
red = pygame.Color(255, 0, 0)
teal = pygame.Color(0, 204, 204)
bday = pygame.Color(90, 30, 30)

# create font object
font = pygame.font.SysFont("Garamond", 50)
# create text
text = font.render("Jordan", True, teal)

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        print(event)
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    screen.fill(0, 0)
    screen.blit(text, pygame.mouse.get_pos())
    #fill screen with color
    pygame.display.flip()
