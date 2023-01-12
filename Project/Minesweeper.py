import pygame
from pygame.locals import *
import sys
import random

"""
Game setup and file imports
"""
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
t = 0
minesLeft = 0

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
MINES = 0


def game_loop():
    i = 11


def reset_game():
    i = 11


def run_menu():
    i = 11


# Draw text function
def drawText(txt, s, yOff=0):
    """
    Draw text on the screen with a given size and y offset
    :param txt:
    :param s:
    :param yOff:
    :return:
    """
    screen_text = pygame.font.SysFont("Calibri", s, True).render(txt, True, (0, 0, 0))
    rect = screen_text.get_rect()
    rect.center = (game_w * grid_size / 2 + top_border, game_h * grid_size / 2 + borders + yOff)
    gameDisplay.blit(screen_text, rect)


# Create a grid class
class Grid:

    def __init__(self, x, y, type):
        """
        :param x:
        :param y:
        :param type:
        """
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
        """
        Draw the grid accprding to type and state
        :return:
        """
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
        """
        Update the value of the grid
        :return:
        """
        # When grid generated, update the value
        if self.val != -1:
            for i in range(-1, 2):
                if self.x + i >= 0 and self.x + i < game_w:
                    for j in range(-1, 2):
                        if self.y + j >= 0 and self.y + j < game_h:
                            if grid[self.x + i][self.y + j].val == -1:
                                self.val += 1

    def revealGrid(self):
        """
        Reveal the grid and all the grids around it
        :return:
        """
        self.clicked = True
        # If it's 0 reveal the grids around it
        if self.val == 0:
            for i in range(-1, 2):
                if self.x + i >= 0 and self.x + i < game_w:
                    for j in range(-1, 2):
                        if self.y + j >= 0 and self.y + j < game_h:
                            if not grid[self.x + i][self.y + j].clicked:
                                grid[self.x + i][self.y + j].revealGrid()


def run_menu():
    """
    Run the menu loop and handle events
    :return:
    """
    global game_w, game_h, MINE_NUM, MINES
    global stop_game_loop
    input_grid_w = ""
    input_grid_h = ""
    input_mine_num = ""
    input_grid_w_rect = pygame.Rect(115, 230, 120, 30)
    input_grid_h_rect = pygame.Rect(115, 290, 120, 30)
    input_mine_num_rect = pygame.Rect(115, 350, 120, 30)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.unicode.isdigit():
                    if input_grid_w_rect.collidepoint(pygame.mouse.get_pos()):
                        input_grid_w += event.unicode
                    elif input_grid_h_rect.collidepoint(pygame.mouse.get_pos()):
                        input_grid_h += event.unicode
                    elif input_mine_num_rect.collidepoint(pygame.mouse.get_pos()):
                        input_mine_num += event.unicode
                elif event.key == K_BACKSPACE:
                    if input_grid_w_rect.collidepoint(pygame.mouse.get_pos()):
                        input_grid_w = input_grid_w[:-1]
                    elif input_grid_h_rect.collidepoint(pygame.mouse.get_pos()):
                        input_grid_h = input_grid_h[:-1]
                    elif input_mine_num_rect.collidepoint(pygame.mouse.get_pos()):
                        input_mine_num = input_mine_num[:-1]
                elif event.key == K_RETURN:
                    game_w = int(input_grid_w)
                    game_h = int(input_grid_h)
                    MINE_NUM = int(input_mine_num)
                    MINES = MINE_NUM
                    reset_game()
                    stop_game_loop = False
                    game_loop()
                    return
        gameDisplay.fill(bg_color)
        pygame.draw.rect(gameDisplay, (255, 255, 255), input_grid_w_rect)
        pygame.draw.rect(gameDisplay, (255, 255, 255), input_grid_h_rect)
        pygame.draw.rect(gameDisplay, (255, 255, 255), input_mine_num_rect)
        drawText("Grid Width:", 20, -40)
        drawText("Grid Height:", 20, 20)
        drawText("Number of Mines:", 20, 80)
        drawText(input_grid_w, 20, -15)
        drawText(input_grid_h, 20, 45)
        drawText(input_mine_num, 20, 105)
        pygame.display.update()
        timer.tick(30)


# Run the menu
run_menu()


# Restet the game state
def reset_game():
    """
    Reset the game state
    :return:
    """
    global grid, mines
    global t
    global minesLeft
    global stop_game_loop
    global MINES
    stop_game_loop = False
    minesLeft = MINES
    t = 0
    grid = []
    mines = []
    for i in range(game_w):
        grid.append([])
        for j in range(game_h):
            grid[i].append(Grid(i, j, 0))
    for i in range(MINES):
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
    """
    Run the game loop and handle events
    :return:
    """
    isPlaying = "Playing"  # Game state (Playing, Win, Game Over, Exit)
    global grid  # Grid list
    grid = []
    global mines
    global t
    global MINE_NUM
    global MINES
    minesLeft = MINE_NUM  # Number of mines left
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
    pygame.display.flip()
    # Main game loop
    while isPlaying != "Exit":
        # Reset the screen
        gameDisplay.fill((bg_color))
        if t // 15 > 40:
            isPlaying = "Game Over"
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
                        isPlaying = "Playing"
                        reset_game()
                        minesLeft = MINE_NUM
                        run_menu()
                    elif event.key == pygame.K_r:
                        isPlaying = "Playing"
                        reset_game()
                        minesLeft = MINE_NUM
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
        # Time Limit
        time_lim = pygame.font.SysFont("Calibri", 50).render("Time40", True, (0, 0, 0))
        gameDisplay.blit(time_lim, (display_w - top_border - 270, top_border))
        pygame.display.flip()
        pygame.display.update()  # Update screen

        timer.tick(15)  # Tick fps


gameLoop()
pygame.quit()
quit()
