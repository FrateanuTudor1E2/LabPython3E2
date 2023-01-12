import time
import pygame
from pygame.locals import *
import sys
import random

pygame.init()
bg_color = (192, 192, 192)
grid_color = (128, 128, 128)

menu_w = 200
menu_h = 200
game_w = 10
game_h = 10
MINE_NUM = 11
grid_size = 32
top_border = 16
borders = 100
display_w = grid_size * game_w + top_border * 2  # Display width
display_h = grid_size * game_h + top_border + borders  # Display height
gameDisplay = pygame.display.set_mode((display_w, display_h))  # Create display
timer = pygame.time.Clock()  # Create timer
pygame.display.set_caption("Minesweeper")  # Set the caption of window

# Import the files for sprites
spr_emptyGrid = pygame.image.load("Sprites/empty.png")
spr_flag = pygame.image.load("Sprites/flag.png")
spr_grid = pygame.image.load("Sprites/Grid.png")
spr_grid1 = pygame.image.load("Sprites/grid1.png")
spr_grid2 = pygame.image.load("Sprites/grid2.png")
spr_grid3 = pygame.image.load("Sprites/grid3.png")
spr_grid4 = pygame.image.load("Sprites/grid4.png")
spr_grid5 = pygame.image.load("Sprites/grid5.png")
spr_grid6 = pygame.image.load("Sprites/grid6.png")
spr_grid7 = pygame.image.load("Sprites/grid7.png")
spr_grid8 = pygame.image.load("Sprites/grid8.png")
spr_mine = pygame.image.load("Sprites/mine.png")
spr_mineClicked = pygame.image.load("Sprites/mineClicked.png")
spr_mineFalse = pygame.image.load("Sprites/mineFalse.png")

# Global variables
grid = []  # Grid of cells
mines = []  # Mines coordinates
stop_game_loop = False  # Stop the game loop


def game_loop():
    i = 11


def reset_game():
    i = 11


def run_menu():
    i = 11


# Draw text function
def drawText(txt, s, yOff=0):
    screen_text = pygame.font.SysFont("Calibri", s, True).render(txt, True, (0, 0, 0))
    rect = screen_text.get_rect()
    rect.center = (game_w * grid_size / 2 + top_border, game_h * grid_size / 2 + borders + yOff)
    gameDisplay.blit(screen_text, rect)


# Create a grid class
class Grid:
    def __init__(self, x, y, type):
        self.x = x  # X coordinate
        self.y = y  # Y coordinate
        self.clicked = False  # check if the grid is clicked
        self.mineFalse = False  # check if the grid is a false flag
        self.mineClicked = False  # check if the clicked grid is a mine
        self.flag = False  # check if the grid is flagged
        self.minesAround = 0  # number of mines around
        # Handle drawing and collision
        self.rect = pygame.Rect(top_border + self.x * grid_size, borders + self.y * grid_size, grid_size,
                                grid_size)
        self.val = type  # -1 mine, 0 empty, 1+ number of mines around

    def drawGrid(self):
        # Draw the grid accprding to type and state
        if self.mineFalse:
            gameDisplay.blit(spr_mineFalse, self.rect)
        else:
            if self.clicked:
                if self.val == -1:
                    if self.mineClicked:
                        gameDisplay.blit(spr_mineClicked, self.rect)
                    else:
                        gameDisplay.blit(spr_mine, self.rect)
                else:
                    if self.val == 0:
                        gameDisplay.blit(spr_emptyGrid, self.rect)
                    elif self.val == 1:
                        gameDisplay.blit(spr_grid1, self.rect)
                    elif self.val == 2:
                        gameDisplay.blit(spr_grid2, self.rect)
                    elif self.val == 3:
                        gameDisplay.blit(spr_grid3, self.rect)
                    elif self.val == 4:
                        gameDisplay.blit(spr_grid4, self.rect)
                    elif self.val == 5:
                        gameDisplay.blit(spr_grid5, self.rect)
                    elif self.val == 6:
                        gameDisplay.blit(spr_grid6, self.rect)
                    elif self.val == 7:
                        gameDisplay.blit(spr_grid7, self.rect)
                    elif self.val == 8:
                        gameDisplay.blit(spr_grid8, self.rect)

            else:
                if self.flag:
                    gameDisplay.blit(spr_flag, self.rect)
                else:
                    gameDisplay.blit(spr_grid, self.rect)

    def updateVal(self):
        # When grid generated, update the value
        if self.val != -1:
            for i in range(-1, 2):
                if self.x + i >= 0 and self.x + i < game_w:
                    for j in range(-1, 2):
                        if self.y + j >= 0 and self.y + j < game_h:
                            if grid[self.x + i][self.y + j].val == -1:
                                self.val += 1

    def revealGrid(self):
        # Reveal the grid
        self.clicked = True
        # If it's 0 reveal the grids around it
        if self.val == 0:
            for i in range(-1, 2):
                if self.x + i >= 0 and self.x + i < game_w:
                    for j in range(-1, 2):
                        if self.y + j >= 0 and self.y + j < game_h:
                            if not grid[self.x + i][self.y + j].clicked:
                                grid[self.x + i][self.y + j].revealGrid()


# Game Menu Function
def run_menu():
    # Create the menu window
    global stop_game_loop
    menu_window = pygame.display.set_mode((menu_w, menu_h))
    pygame.display.set_caption('Minesweeper Menu')

    # Set the menu background color
    menu_bg_color = pygame.Color('white')

    # Set the font for displaying menu options
    menu_font = pygame.font.SysFont('Arial', 24)

    # Create the menu options
    play_option = menu_font.render('Play', True, (0, 0, 0))
    quit_option = menu_font.render('Quit', True, (0, 0, 0))

    # Set the menu option positions
    play_option_pos = (menu_w // 2 - play_option.get_width() // 2, 100)
    quit_option_pos = (menu_h // 2 - quit_option.get_width() // 2, 150)

    # Main menu loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if the play option was clicked
                if play_option_pos[0] <= mouse_x <= play_option_pos[0] + play_option.get_width() and \
                        play_option_pos[1] <= mouse_y <= play_option_pos[1] + play_option.get_height():
                    # Start the game
                    reset_game()
                    time.sleep(1)
                    stop_game_loop = False
                    game_loop()
                    return
                # Check if the quit option was clicked
                elif quit_option_pos[0] <= mouse_x <= quit_option_pos[0] + quit_option.get_width() and \
                        quit_option_pos[1] <= mouse_y <= quit_option_pos[1] + quit_option.get_height():
                    pygame.quit()
                    sys.exit()

        # Clear the menu window
        menu_window.fill(menu_bg_color)

        # Draw the menu options
        menu_window.blit(play_option, play_option_pos)
        menu_window.blit(quit_option, quit_option_pos)

        # Update the menu window
        pygame.display.update()


# Run the menu
run_menu()


# Restet the game state
def reset_game():
    global grid, mines
    grid = []
    mines = []
    for i in range(game_w):
        grid.append([])
        for j in range(game_h):
            grid[i].append(Grid(i, j, 0))
    for i in range(MINE_NUM):
        mineX = random.randint(0, game_w - 1)
        mineY = random.randint(0, game_h - 1)
        while (mineX, mineY) in mines or grid[mineX][mineY].val == -1:
            mineX = random.randint(0, game_w - 1)
            mineY = random.randint(0, game_h - 1)
        grid[mineX][mineY].val = -1
        mines.append((mineX, mineY))
    for mineX, mineY in mines:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= mineX + i < game_w and 0 <= mineY + j < game_h and grid[mineX + i][mineY + j].val != -1:
                    grid[mineX + i][mineY + j].val += 1


def gameLoop():
    isPlaying = "Playing"  # Game state (Playing, Win, Game Over, Exit)
    minesLeft = MINE_NUM  # Number of mines left
    global grid  # Grid list
    grid = []
    global mines
    t = 0  # Time set to 0
    pygame.event.clear()  # Clear all events
    # Generate mines
    mines = [random.randrange(0, game_w), random.randrange(0, game_h)]
    global stop_game_loop
    for z in range(MINE_NUM - 1):
        pos = [random.randrange(0, game_w), random.randrange(0, game_h)]
        same = True  # Check if the position is the same as the previous one
        while same:
            for i in range(len(mines)):
                if pos == mines[i]:
                    same = True
                    pos = [random.randrange(0, game_w), random.randrange(0, game_h)]
                if i == len(mines) - 1:
                    same = False
        mines.append(pos)

    # Generate grid
    for i in range(game_h):
        line = []  # Line list
        for j in range(game_w):
            if [i, j] in mines:
                line.append(Grid(i, j, -1))
            else:
                line.append(Grid(i, j, 0))
        grid.append(line)

    # Update the value of the grid
    for i in grid:
        for j in i:
            j.updateVal()

    gameDisplay = pygame.display.set_mode((display_w, display_h))

    reset_game()
    # Main game loop
    while isPlaying != "Exit":
        # Reset the screen
        gameDisplay.fill((bg_color))
        if stop_game_loop:
            break

        # Handle user input
        for event in pygame.event.get():
            # Check for quit event
            if event.type == pygame.QUIT:
                stop_game_loop = True
                isPlaying = "Exit"
            # Look for restart
            if isPlaying == "Win" or isPlaying == "Game Over":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        isPlaying = "Exit"
                        stop_game_loop = True
                        reset_game()
                        run_menu()
                    elif event.key == pygame.K_r:
                        isPlaying = "Playing"
                        reset_game()
                        game_loop()

            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in grid:
                        for j in i:
                            if j.rect.collidepoint(event.pos):
                                if event.button == 1:
                                    # If left click on grid
                                    j.revealGrid()
                                    if j.flag:
                                        minesLeft += 1
                                        j.flag = False
                                    # Check if mine
                                    if j.val == -1:
                                        isPlaying = "Game Over"
                                        j.mineClicked = True
                                elif event.button == 3:
                                    # If right click on grid
                                    if not j.clicked:
                                        j.flag = not j.flag
                                        if j.flag:
                                            minesLeft -= 1
                                        else:
                                            minesLeft += 1

        # Win condition
        win = True
        for i in grid:
            for j in i:
                j.drawGrid()
                if j.val != -1 and not j.clicked:
                    win = False
        if win and isPlaying != "Exit":
            isPlaying = "Win"

        # Draw Texts
        if isPlaying != "Game Over" and isPlaying != "Win":
            t += 1
        elif isPlaying == "Game Over":
            drawText("Game Over", 50)
            drawText("M for menu", 35, 50)
            drawText("R to restart", 35, 100)
            for i in grid:
                for j in i:
                    if j.flag and j.val != -1:
                        j.mineFalse = True
        else:
            drawText("You Win!", 50)
            drawText("M for menu", 35, 50)
            drawText("R to restart", 35, 100)

        # Draw time
        s = str(t // 15)
        screen_text = pygame.font.SysFont("Calibri", 50).render(s, True, (0, 0, 0))
        gameDisplay.blit(screen_text, (top_border, top_border))
        # Draw mine left
        screen_text = pygame.font.SysFont("Calibri", 50).render(minesLeft.__str__(), True, (0, 0, 0))
        gameDisplay.blit(screen_text, (display_w - top_border - 50, top_border))

        pygame.display.update()  # Update screen

        timer.tick(15)  # Tick fps


gameLoop()
pygame.quit()
quit()
