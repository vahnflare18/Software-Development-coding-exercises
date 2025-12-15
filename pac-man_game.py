"""
Author:  Ivanloe L. Manuel
Date written: 12/14/2025
Assignment:   Module 8: Assignment - Python Development - Pac-Man
Short Desc:   This program is a simplified Pac‑Man–style game built with Pygame.
It generates a grid‑based maze with walls and pellets, places Pac‑Man in the center, and spawns a
ghost at a random free location.
"""
import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 600, 660
CELL = 30
GRID_W, GRID_H = WIDTH // CELL, (HEIGHT - 60) // CELL  # leave space for HUD
FPS = 60

WALL = 1
PELLET = 2
EMPTY = 0

YELLOW = (255, 215, 0)
BLUE = (30, 144, 255)
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
GREY = (40, 40, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 26)

def make_maze(w, h):
    grid = [[EMPTY for _ in range(w)] for _ in range(h)]
    # Border walls
    for x in range(w):
        grid[0][x] = WALL
        grid[h-1][x] = WALL
    for y in range(h):
        grid[y][0] = WALL
        grid[y][w-1] = WALL
    # Inner pillars
    for x in range(3, w-3, 4):
        for y in range(2, h-2, 4):
            grid[y][x] = WALL
    # Pellets
    for y in range(1, h-1):
        for x in range(1, w-1):
            if grid[y][x] == EMPTY:
                grid[y][x] = PELLET
    return grid

def draw_grid(grid):
    screen.fill(BLACK)
    # HUD
    pygame.draw.rect(screen, GREY, (0, HEIGHT - 60, WIDTH, 60))
    # Cells
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            rx, ry = x * CELL, y * CELL
            if cell == WALL:
                pygame.draw.rect(screen, BLUE, (rx, ry, CELL, CELL))
            elif cell == PELLET:
                pygame.draw.circle(screen, WHITE, (rx + CELL//2, ry + CELL//2), 4)

def draw_entity(pos, color, radius=12):
    x, y = pos
    rx, ry = x * CELL + CELL//2, y * CELL + CELL//2
    pygame.draw.circle(screen, color, (rx, ry), radius)

def find_free(grid):
    while True:
        x = random.randint(1, GRID_W-2)
        y = random.randint(1, GRID_H-2)
        if grid[y][x] in (EMPTY, PELLET):
            return (x, y)

def move_try(pos, dx, dy, grid):
    x, y = pos
    nx, ny = x + dx, y + dy
    if 0 <= nx < GRID_W and 0 <= ny < GRID_H and grid[ny][nx] != WALL:
        return (nx, ny)
    return pos

def pellets_left(grid):
    return sum(row.count(PELLET) for row in grid)

def ghost_step(ghost, pac, grid):
    gx, gy = ghost
    px, py = pac
    candidates = []
    if px > gx: candidates.append((1, 0))
    if px < gx: candidates.append((-1, 0))
    if py > gy: candidates.append((0, 1))
    if py < gy: candidates.append((0, -1))
    # Try prioritized moves
    for dx, dy in candidates:
        if grid[gy + dy][gx + dx] != WALL:
            return (gx + dx, gy + dy)
    # Fallback random
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx, ny = gx + dx, gy + dy
        if grid[ny][nx] != WALL:
            return (nx, ny)
    return ghost

def main():
    grid = make_maze(GRID_W, GRID_H)
    pac = (GRID_W//2, GRID_H//2)
    ghost = find_free(grid)
    score = 0
    lives = 3
    speed_accum = 0.0
    ghost_accum = 0.0

    # Ensure starting tile is empty
    x, y = pac
    if grid[y][x] == PELLET:
        grid[y][x] = EMPTY

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Input
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]: dx = -1
        if keys[pygame.K_RIGHT]: dx = 1
        if keys[pygame.K_UP]: dy = -1
        if keys[pygame.K_DOWN]: dy = 1

        # Pac movement throttled a bit to feel grid-based
        speed_accum += dt
        if speed_accum >= 0.12:
            pac = move_try(pac, dx, dy, grid)
            px, py = pac
            if grid[py][px] == PELLET:
                grid[py][px] = EMPTY
                score += 10
            speed_accum = 0.0

        # Ghost movement
        ghost_accum += dt
        if ghost_accum >= 0.18:
            ghost = ghost_step(ghost, pac, grid)
            ghost_accum = 0.0

        # Collision
        if pac == ghost:
            lives -= 1
            pac = (GRID_W//2, GRID_H//2)
            ghost = find_free(grid)
            if lives <= 0:
                # Game over splash
                screen.fill(BLACK)
                txt = font.render("Game Over", True, WHITE)
                screen.blit(txt, (WIDTH//2 - 60, HEIGHT//2 - 13))
                pygame.display.flip()
                pygame.time.wait(1200)
                running = False

        # Win check
        if pellets_left(grid) == 0:
            screen.fill(BLACK)
            txt = font.render("You Win!", True, WHITE)
            screen.blit(txt, (WIDTH//2 - 50, HEIGHT//2 - 13))
            pygame.display.flip()
            pygame.time.wait(1200)
            running = False

        # Draw
        draw_grid(grid)
        draw_entity(pac, YELLOW, radius=12)
        draw_entity(ghost, (255, 64, 64), radius=12)
        hud = font.render(f"Score: {score}  Lives: {lives}  Pellets: {pellets_left(grid)}", True, WHITE)
        screen.blit(hud, (10, HEIGHT - 40))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()