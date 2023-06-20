import pygame
import math

# Inicializace knihovny Pygame
pygame.init()

# Nastavení velikosti okna
width, height = 2000, 1500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt Točky")

# Barva pozadí
background_color = (0, 0, 0)

# Střed otáčení
center_x = width // 2
center_y = height // 2

# Seznam bodů
pos = (center_x, center_y)

points = [
    {"position": pos, "distance": 0, "color": (1, 100, 32), "angular_speed": math.radians(0), "start_angle": math.radians(0)},
    {"position": pos, "distance": 200, "color": (1, 100, 32), "angular_speed": math.radians(50), "parent_index": 0, "start_angle": math.radians(0)},
    {"position": pos, "distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(100), "parent_index": 1, "start_angle": math.radians(0)},
    {"position": pos, "distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(-60), "parent_index": 2, "start_angle": math.radians(180)}
]


# Seznam pro uchovávání historie pozic posledního bodu
trail_points = []

time = 1000    #1000 je normální rychlost.  čím větší číslo tím pomalejší

# Hlavní smyčka programu
running = True
while running:
    # Procházení všech událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Vymazání obrazovky
    screen.fill(background_color)

    # Vykreslení bodů a linek
    for i, point in enumerate(points):
        # Výpočet aktuální polohy bodu
        current_time = pygame.time.get_ticks() / time  # Aktuální čas v sekundách
        angle = point["start_angle"] + current_time * point["angular_speed"]

        if i > 0:
            parent = points[i-1]
            x = parent["position"][0] + point["distance"] * math.cos(angle)
            y = parent["position"][1] + point["distance"] * math.sin(angle)
            point["position"] = (x, y)
        else:
            x = point["position"][0] + point["distance"] * math.cos(angle)
            y = point["position"][1] + point["distance"] * math.sin(angle)

        # Vykreslení linky
        if i > 0:
            parent = points[i-1]
            pygame.draw.line(screen, (255, 255, 255), parent["position"], (x, y), 2)

        # Vykreslení bodu
        pygame.draw.circle(screen, point["color"], (int(x), int(y)), 10)

        # Přidání aktuální pozice do seznamu historie bodu
        if i == len(points) - 1:
            trail_points.append((int(x), int(y)))

    # Omezení délky seznamu historie
    # trail_points = trail_points[-500:] # Uchováváme posledních 100 bodů

    trail_color = (0, 255, 0)

    # Vykreslení stopy posledního bodu
    if len(trail_points) >= 2:
        pygame.draw.lines(screen, trail_color, False, trail_points, 1)

    # Obnovení obrazovky
    pygame.display.flip()

# Ukončení programu
pygame.quit()
