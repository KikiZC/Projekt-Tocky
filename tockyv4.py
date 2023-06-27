import pygame
import math

# Inicializace knihovny Pygame
pygame.init()

# Nastavení velikosti okna
width, height = 2000, 1400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vector simulation")

# Barva pozadí
background_color = (0, 0, 0)

# Střed otáčení
center_x = width // 2
center_y = height // 2

# Seznam bodů*
pos = (center_x, center_y)

points = [
    {"position": pos, "distance": 0, "color": (1, 100, 32), "angular_speed": math.radians(0), "start_angle": math.radians(0)},
    {"position": pos, "distance": 100, "color": (1, 100, 32), "angular_speed": 100, "parent_index": 0, "start_angle": math.radians(0)},
    {"position": pos, "distance": 100, "color": (1, 100, 32), "angular_speed": -100, "parent_index": 1, "start_angle": math.radians(180)},
    {"position": pos, "distance": 100, "color": (1, 100, 32), "angular_speed": 100, "parent_index": 2, "start_angle": math.radians(0)}
]

# Seznam pro uchovávání historie pozic posledního bodu
trail_points = []

time = 1001  # 1001 je normální rychlost. Čím větší číslo, tím pomalejší

cas_ted = 0

# Hlavní smyčka programu
running = True
simulation_running = False

button_width = 100
button_height = 30

# tlacitko start / stop
button_x = width - 110
button_y = 10
button_width = 100
button_height = 30
button_font = pygame.font.SysFont("Monocraft", 16)

def toggle_simulation():
    global simulation_running
    simulation_running = not simulation_running

def get_button_text():
    return "Stop" if simulation_running else "Start"

def get_button_color():
    return (255, 0, 0) if simulation_running else (0, 150, 0)

button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# tlacitko reset
rbutton_x = width - 110
rbutton_y = 40
rbutton_font = pygame.font.SysFont("Monocraft", 16)

def reset_simulation():
    global cas_ted 
    global trail_points 
    cas_ted = 0
    trail_points = []

rbutton_rect = pygame.Rect(rbutton_x, rbutton_y, button_width, button_height)

# tlacitko cas +
caspbutton_x = width - 110
caspbutton_y = 70
caspbutton_font = pygame.font.SysFont("Monocraft", 16)

def cas_plus():
    global time 
    global simulation_running
    simulation_running = not simulation_running
    time += 100
    simulation_running = not simulation_running

caspbutton_rect = pygame.Rect(caspbutton_x, caspbutton_y, button_width, button_height)

# aktualni cas
tbutton_x = width - 110
tbutton_y = 100
tbutton_font = pygame.font.SysFont("Monocraft", 16)
tbutton_rect = pygame.Rect(tbutton_x, tbutton_y, button_width, button_height)

# tlacitko cas -
casmbutton_x = width - 110
casmbutton_y = 130
casmbutton_font = pygame.font.SysFont("Monocraft", 16)

def cas_minus():
    global time
    global simulation_running
    simulation_running = not simulation_running
    if time > 100: 
        time -= 100
    else:
        time = 1
    simulation_running = not simulation_running

casmbutton_rect = pygame.Rect(casmbutton_x, casmbutton_y, button_width, button_height)

button_plus_x = 10
button_plus_y = 10
button_minus_x = 120
button_minus_y = 10

# Vedle tlačítka casu
rvalue_x = button_minus_x + button_width + 10
rvalue_y = button_minus_y
rvalue_font = pygame.font.SysFont("Monocraft", 16)
rvalue_rect = pygame.Rect(rvalue_x, rvalue_y, 60, button_height)

ibutton_plus_x = 10
ibutton_plus_y = 50
ibutton_minus_x = 120
ibutton_minus_y = 50

# Vedle tlačítka casu
irvalue_x = ibutton_minus_x + button_width + 10
irvalue_y = ibutton_minus_y
irvalue_font = pygame.font.SysFont("Monocraft", 16)
irvalue_rect = pygame.Rect(irvalue_x, irvalue_y, 60, button_height)

index = 1

while running:
    # Procházení všech událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Levé tlačítko myši
                if button_rect.collidepoint(event.pos):
                    toggle_simulation()
                if rbutton_rect.collidepoint(event.pos):
                    reset_simulation()
                if casmbutton_rect.collidepoint(event.pos):
                    cas_minus()
                if caspbutton_rect.collidepoint(event.pos):
                    cas_plus()
                if button_plus_rect.collidepoint(event.pos):
                    points[index]["angular_speed"] += 1
                if button_minus_rect.collidepoint(event.pos):
                    points[index]["angular_speed"] -= 1
                if ibutton_plus_rect.collidepoint(event.pos):
                    index += 1
                if ibutton_minus_rect.collidepoint(event.pos):
                    index -= 1

    r1r = str(points[index]["angular_speed"])

    indexr = str(index)

    # Vymazání obrazovky
    screen.fill(background_color)
    ttime = str(time)
    if simulation_running:
        # Vykreslení bodů a linek
        for i, point in enumerate(points):
            # Výpočet aktuální polohy bodu
            ttime = str(time)
            current_time = cas_ted / time
            angle = point["start_angle"] + current_time * math.radians(point["angular_speed"])
            cas_ted += 1
            if i > 0:
                parent = points[i - 1]
                x = parent["position"][0] + point["distance"] * math.cos(angle)
                y = parent["position"][1] + point["distance"] * math.sin(angle)
                point["position"] = (x, y)
            else:
                x = point["position"][0] + point["distance"] * math.cos(angle)
                y = point["position"][1] + point["distance"] * math.sin(angle)

            # Vykreslení linky
            if i > 0:
                parent = points[i - 1]
                pygame.draw.line(screen, (255, 255, 255), parent["position"], (x, y), 2)

            # Vykreslení bodu
            pygame.draw.circle(screen, point["color"], (int(x), int(y)), 10)

            # Přidání aktuální pozice do seznamu historie bodu
            if i == len(points) - 1:
                trail_points.append((int(x), int(y)))

        trail_color = (0, 255, 0)

        # Vykreslení stopy posledního bodu
        if len(trail_points) >= 2:
            pygame.draw.lines(screen, trail_color, False, trail_points, 1)

    # Vykreslení tlačítka
    zaklad_button_color = (0, 150, 0)

    button_text = button_font.render(get_button_text(), True, (255, 255, 255))
    button_color = get_button_color()
    rbutton_text = rbutton_font.render("Reset", True, (255, 255, 255))
    caspbutton_text = caspbutton_font.render("+ 100", True, (255, 255, 255))
    tbutton_text = button_font.render(ttime, True, (255, 255, 255))
    casmbutton_text = casmbutton_font.render("- 100", True, (255, 255, 255))
    button_plus_rect = pygame.Rect(button_plus_x, button_plus_y, button_width, button_height)
    button_minus_rect = pygame.Rect(button_minus_x, button_minus_y, button_width, button_height)
    tvalue_text = rvalue_font.render("Rychlost: " + r1r, True, (255, 255, 255))
    minus_text = button_font.render("-", True, (255, 255, 255))
    plus_text = button_font.render("+", True, (255, 255, 255))
    ivalue_text = irvalue_font.render("Rameno: " + indexr, True, (255, 255, 255))
    ibutton_plus_rect = pygame.Rect(ibutton_plus_x, ibutton_plus_y, button_width, button_height)
    ibutton_minus_rect = pygame.Rect(ibutton_minus_x, ibutton_minus_y, button_width, button_height)
    
    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, zaklad_button_color, rbutton_rect)
    pygame.draw.rect(screen, zaklad_button_color, caspbutton_rect)
    pygame.draw.rect(screen, zaklad_button_color, casmbutton_rect)
    pygame.draw.rect(screen, zaklad_button_color, tbutton_rect)
    pygame.draw.rect(screen, zaklad_button_color, button_plus_rect)
    pygame.draw.rect(screen, zaklad_button_color, button_minus_rect)
    pygame.draw.rect(screen, zaklad_button_color, ibutton_plus_rect)
    pygame.draw.rect(screen, zaklad_button_color, ibutton_minus_rect)

    screen.blit(button_text, (button_x + 10, button_y + 8))
    screen.blit(rbutton_text, (rbutton_x + 10, rbutton_y + 8))
    screen.blit(caspbutton_text, (caspbutton_x + 10, caspbutton_y + 8))
    screen.blit(casmbutton_text, (casmbutton_x + 10, casmbutton_y + 8))
    screen.blit(tbutton_text, (tbutton_x + 10, tbutton_y + 8))
    screen.blit(plus_text, (button_plus_x + 45, button_plus_y + 8))
    screen.blit(minus_text, (button_minus_x + 45, button_minus_y + 8))
    screen.blit(tvalue_text, (rvalue_x + 10, rvalue_y + 8))
    screen.blit(plus_text, (ibutton_plus_x + 45, ibutton_plus_y + 8))
    screen.blit(minus_text, (ibutton_minus_x + 45, ibutton_minus_y + 8))
    screen.blit(ivalue_text, (irvalue_x + 10, irvalue_y + 8))

    #kdyz sim nebezi
    if not simulation_running:
        if len(trail_points) >= 2:
            pygame.draw.lines(screen, trail_color, False, trail_points, 1)

    # Obnovení obrazovky
    pygame.display.flip()

# Ukončení programu
pygame.quit()
