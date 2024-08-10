import pygame
import numpy as np

class springsim():
    def __init__(self, k, surface, amount, width, height) -> None:
        self.k = k
        self.surface = surface
        self.amount = amount
        self.width = width
        self.height = height
    def runsim(self) -> None:
        mouse = pygame.mouse
        running = True
        dragging = False
        index = -1
        ypositions = []
        xpositions = []
        displacements = [0 for i in range(self.amount)]
        velocities = [0 for i in range(self.amount)]
        for i in range(1, self.amount, 1):
            xpositions.append((self.height/self.amount)*i)
            ypositions.append(self.height/2)
        # game loop 
        while running: 
            mousepos = mouse.get_pos()
            
        # for loop through the event queue 
            self.surface.fill((0,0,0))
            for i in range(len(xpositions)):
                try:
                    pygame.draw.circle(self.surface, pygame.Color(52, 58, 235, 100), (xpositions[i], ypositions[i]), self.width/(self.amount * 3))
                    pygame.draw.line(self.surface, pygame.Color(52, 58, 235, 100), (xpositions[i], ypositions[i]), (xpositions[i + 1], ypositions[i + 1]), int(self.width/(self.amount * 4)))
                    pygame.draw.polygon(self.surface, pygame.Color(52, 58, 235, 100), ((xpositions[i], ypositions[i]), (xpositions[i + 1], ypositions[i + 1]), (xpositions[i], self.height), (xpositions[i + 1], self.height)), int(self.width/(self.amount * .8)))
                    if i > 0:
                        pygame.draw.line(self.surface, pygame.Color(52, 58, 235, 100), (xpositions[i], ypositions[i]), (xpositions[i - 1], ypositions[i - 1]), int(self.width/(self.amount * 4)))
                        pygame.draw.polygon(self.surface, pygame.Color(52, 58, 235, 100), ((xpositions[i], ypositions[i]), (xpositions[i - 1], ypositions[i - 1]), (xpositions[i], self.height), (xpositions[i - 1], self.height)), int(self.width/(self.amount * .8)))
                except:
                    pass
            for event in pygame.event.get(): 
            
                # Check for QUIT event	 
                if event.type == pygame.QUIT: 
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragging = True
                if event.type == pygame.MOUSEBUTTONUP:
                    dragging = False
                    index = -1
            if dragging:
                leader = 5000
                if index == -1:
                    for i in range(len(xpositions)):
                        if np.abs(xpositions[i] - mousepos[0]) < leader: 
                            leader = np.abs(xpositions[i] - mousepos[0])
                            index = i
                for i in range(index, self.amount -1, 1):
                    ypositions[i] = (mousepos[1] / ((np.abs(index - i) + 1)/.5)) + (self.height/2)
                    displacements[i] = (ypositions[i] - (self.height/2))
                for i in range(0, index, 1):
                    ypositions[i] = (mousepos[1] / ((np.abs(index - i) + 1)/.5)) + (self.height/2)
                    displacements[i] = (ypositions[i] - (self.height/2))
            else:
            
                for i in range(len(ypositions)):
                    force = 0
                    try:
                        force += -self.k * (displacements[i] - displacements[i-1])
                        force += -self.k * (displacements[i] - displacements[i+1])
                    except:
                        pass

                    # Update displacements and velocities
                    displacements[i] += .01 * velocities[i]
                    velocities[i] += .01 * force
                    velocities[i] *= .99 # Apply damping

                    # Update ypositions
                    ypositions[i] = (self.height/2) + displacements[i]
                

            pygame.display.update()

# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((1000, 1000)) 

# Set the caption of the screen 
pygame.display.set_caption('Geeksforgeeks') 

# Fill the background colour to the screen 
screen.fill(background_colour) 

# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
sim = springsim(21.5, screen, 100, 1000, 1000)
sim.runsim()
