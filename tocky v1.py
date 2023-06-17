import pygame
import math

# Inicializace knihovny Pygame
pygame.init()

# Nastavení velikosti okna
width, height = 2000, 1400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt Točky")

# Barva pozadí
background_color = (0, 0, 0)

# Střed otáčení
center_x = width // 2
center_y = height // 2

# Seznam bodů
points = [
    {"position": (center_x, center_y), "distance": 0, "color": (1, 100, 32), "angular_speed": math.radians(90)},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(10), "parent_index": 0},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(20), "parent_index": 1},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(30), "parent_index": 2},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(40), "parent_index": 3},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(50), "parent_index": 4},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(60), "parent_index": 5},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(70), "parent_index": 6},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(80), "parent_index": 7},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(90), "parent_index": 8},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(100), "parent_index": 9},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(110), "parent_index": 10},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(120), "parent_index": 11},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(130), "parent_index": 12},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(140), "parent_index": 13},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(150), "parent_index": 14},
    {"distance": 50, "color": (1, 100, 32), "angular_speed": math.radians(160), "parent_index": 15},
]


# Seznam pro uchovávání historie pozic posledního bodu
trail_points = []

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
        current_time = pygame.time.get_ticks() / 1000  # Aktuální čas v sekundách
        angle = current_time * point["angular_speed"]
        
        if "parent_index" in point:
            parent = points[point["parent_index"]]
            x = parent["position"][0] + point["distance"] * math.cos(angle)
            y = parent["position"][1] + point["distance"] * math.sin(angle)
            point["position"] = (x, y)
        
        else:
            x = point["position"][0] + point["distance"] * math.cos(angle)
            y = point["position"][1] + point["distance"] * math.sin(angle)

        # Vykreslení linky
        if "parent_index" in point:
            pygame.draw.line(screen, (255, 255, 255), parent["position"], (x, y), 2)
        
        # Vykreslení bodu
        pygame.draw.circle(screen, point["color"], (int(x), int(y)), 10)

        # Přidání aktuální pozice do seznamu historie bodu
        if i == len(points) - 1:
            trail_points.append((int(x), int(y)))

    # Omezení délky seznamu historie
    #trail_points = trail_points[-500:] # Uchováváme posledních 100 bodů

    #trail_color = (1, 255, 32)
    trail_color = (255, 255, 0)

    # Vykreslení stopy posledního bodu
    if len(trail_points) >= 2:
        pygame.draw.lines(screen, (trail_color), False, trail_points, 3)

    # Obnovení obrazovky
    pygame.display.flip()

# Ukončení programu
pygame.quit()
