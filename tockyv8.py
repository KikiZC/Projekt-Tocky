import pygame
import math

# Inicializace knihovny Pygame
pygame.init()

# Nastavení velikosti okna
width, height = 2000, 1400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt Točky")

# Barva pozadí
background_color = (25, 26, 25)

# Střed otáčení
center_x = width // 2
center_y = height // 2

# Seznam bodů
pos = (center_x, center_y)
p_color = (40, 150, 35)

points = [
    {"position": pos, "distance": 0, "color": (16, 137, 215), "angular_speed": 0, "start_angle": 0},
    {"position": pos, "distance": 200, "color": p_color,"angular_speed": 20, "start_angle": 0},
    {"position": pos, "distance": 100, "color": p_color,"angular_speed": -100, "start_angle": 0},
    {"position": pos, "distance": 50, "color": p_color,"angular_speed": 500, "start_angle": 0},
    {"position": pos, "distance": 10, "color": p_color,"angular_speed": -1000, "start_angle": 0},
]

# Seznam pro uchovávání historie pozic posledního bodu
trail_points = []
time = 1000  # 1000 je normální rychlost. Čím větší číslo, tím pomalejší
cas_ted = 0
font = pygame.font.SysFont("Monocraft", 18)
index = 1
stopa = False
running = True
simulation_running = False
trail_color = (20, 120, 100)
b_color = (30, 90, 30)
pridavano = 1
useing_color = (16, 134, 215)

# definice akcí

def get_button_text():
    return "Stop" if simulation_running else "Start"

def get_button_color():
    return (255, 0, 0) if simulation_running else b_color

def toggle_simulation():
    global simulation_running
    simulation_running = not simulation_running

def update_button_text(name, text):
    for button in buttons:
        if button["jmeno"] == name:
            button["text"] = text
            break

def update_button_color(name, color):
    for button in buttons:
        if button["jmeno"] == name:
            button["color"] = color
            break

def index_plus():
    global index
    index += 1
    if index >= len(points) :
        index -= 1

def index_minus():
    global index
    index -= 1
    if index == 0:
        index = 1

def get_sbutton_color():
    return (215, 167, 16) if stopa else b_color

def zanechani_stopy():
    global stopa
    stopa = not stopa

def reset():
    global cas_ted 
    global trail_points 
    cas_ted = 0
    trail_points = []

def cas_plus():
    global time
    time += pridavano

def cas_minus():
    global time
    time -= pridavano
    if time <= 100:
        time = 100

def rychlost_plus():
    points[index]["angular_speed"] += pridavano

def rychlost_minus():
    points[index]["angular_speed"] -= pridavano

def delka_plus():
    points[index]["distance"] += pridavano

def delka_minus():
    points[index]["distance"] -= pridavano
    if points[index]["distance"] < 0:
        points[index]["distance"] = 0

def uhel_plus():
    points[index]["start_angle"] += pridavano

def uhel_minus():
    points[index]["start_angle"] -= pridavano

def pridani_1():
    global pridavano
    pridavano = 1
    update_button_color("pridavani 1", useing_color)
    update_button_color("pridavani 10", b_color)
    update_button_color("pridavani 100", b_color)

def pridani_10():
    global pridavano
    pridavano = 10
    update_button_color("pridavani 1", b_color)
    update_button_color("pridavani 10", useing_color)
    update_button_color("pridavani 100", b_color)

def pridani_100():
    global pridavano
    pridavano = 100
    update_button_color("pridavani 1", b_color)
    update_button_color("pridavani 10", b_color)
    update_button_color("pridavani 100", useing_color)

# konec definicí akcí

# zakladni velikosti
od_leva = width - 165
# zprava je x 10

buttons = [
    {"jmeno": "start / stop", "x": od_leva, "y": 10, "color": b_color, "width": 160, "height": 40, "text": "Start", "akce": toggle_simulation},
    {"jmeno": "stopa", "x": od_leva, "y": 55, "color": b_color, "width": 160, "height": 40, "text": "Stopa: " + str(stopa), "akce": zanechani_stopy},
    {"jmeno": "reset", "x": od_leva, "y": 100, "color": b_color, "width": 160, "height": 40, "text": "Reset", "akce": reset},

    {"jmeno": "rameno +", "x": 10, "y": 10, "color": b_color, "width": 35, "height": 35, "text": "+", "akce": index_plus},
    {"jmeno": "rameno -", "x": 50, "y": 10, "color": b_color, "width": 35, "height": 35, "text": "-", "akce": index_minus},
    {"jmeno": "rameno text", "x": 90, "y": 10, "color": b_color, "width": 140, "height": 35, "text": "Rameno: " + str(index), "akce": 0},

    {"jmeno": "cas +", "x": od_leva, "y": 145, "color": b_color, "width": 78, "height": 40, "text": "+", "akce": cas_plus},
    {"jmeno": "cas -", "x": od_leva + 82, "y": 145, "color": b_color, "width": 78, "height": 40, "text": "-", "akce": cas_minus},
    {"jmeno": "cas text", "x": od_leva, "y": 190, "color": b_color, "width": 160, "height": 40, "text": "Čas: " + str(time), "akce": 0},

    {"jmeno": "rychlost +", "x": 10, "y": 50, "color": b_color, "width": 35, "height": 35, "text": "+", "akce": rychlost_plus},
    {"jmeno": "rychlost -", "x": 50, "y": 50, "color": b_color, "width": 35, "height": 35, "text": "-", "akce": rychlost_minus},
    {"jmeno": "rychlost text", "x": 90, "y": 50, "color": b_color, "width": 180, "height": 35, "text": "Rychlost: " + str(points[index]["angular_speed"]), "akce": 0},

    {"jmeno": "delka +", "x": 10, "y": 90, "color": b_color, "width": 35, "height": 35, "text": "+", "akce": delka_plus},
    {"jmeno": "delka -", "x": 50, "y": 90, "color": b_color, "width": 35, "height": 35, "text": "-", "akce": delka_minus},
    {"jmeno": "delka text", "x": 90, "y": 90, "color": b_color, "width": 140, "height": 35, "text": "Délka: " + str(points[index]["distance"]), "akce": 0},

    {"jmeno": "uhel +", "x": 10, "y": 130, "color": b_color, "width": 35, "height": 35, "text": "+", "akce": uhel_plus},
    {"jmeno": "uhel -", "x": 50, "y": 130, "color": b_color, "width": 35, "height": 35, "text": "-", "akce": uhel_minus},
    {"jmeno": "uhel text", "x": 90, "y": 130, "color": b_color, "width": 140, "height": 35, "text": "Úhel: " + str(points[index]["start_angle"]), "akce": 0},
    
    {"jmeno": "pridavani 1", "x": 645, "y": 10, "color": b_color, "width": 55, "height": 35, "text": "1", "akce": pridani_1},
    {"jmeno": "pridavani 10", "x": 705, "y": 10, "color": b_color, "width": 55, "height": 35, "text": "10", "akce": pridani_10},
    {"jmeno": "pridavani 100", "x": 765, "y": 10, "color": b_color, "width": 55, "height": 35, "text": "100", "akce": pridani_100},  
    {"jmeno": "pridavani text", "x": 440, "y": 10, "color": b_color, "width": 200, "height": 35, "text": "Počet přidávání", "akce": 0},   
]

# definice malování
def malovani():
    for but in buttons:
        rectangle = pygame.Rect(but["x"], but["y"], but["width"], but["height"])
        pygame.draw.rect(screen, but["color"], rectangle)
        button_text = font.render(but["text"], True, (255, 255, 255))
        screen.blit(button_text, (but["x"] + 10, but["y"] + 8))
    
# refresování butonů
def button_refresh():
    update_button_text("start / stop", get_button_text())
    update_button_color("start / stop", get_button_color())

    update_button_text("stopa", "Stopa: " + str(stopa))
    update_button_color("stopa", get_sbutton_color())

    update_button_text("rameno text", "Rameno: " + str(index))
    update_button_text("cas text", "Čas: " + str(time))
    update_button_text("rychlost text", "Rychlost: " + str(points[index]["angular_speed"]))
    update_button_text("delka text", "Délka: " + str(points[index]["distance"]))
    update_button_text("uhel text", "Úhel: " + str(points[index]["start_angle"]))


# hlavní smyčka
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
                for but in buttons:
                    if pygame.Rect(but["x"], but["y"], but["width"], but["height"]).collidepoint(event.pos):
                        if but["akce"] != 0:
                            but["akce"]()
                            button_refresh()

    # Vymazání obrazovky
    screen.fill(background_color)
    ttime = str(time)
    if simulation_running:
        # Vykreslení bodů a linek
        for i, point in enumerate(points):
            # Výpočet aktuální polohy bodu
            ttime = str(time)
            current_time = cas_ted / time
            angle = math.radians(point["start_angle"]) + current_time * math.radians(point["angular_speed"])
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
                pygame.draw.line(screen, p_color, parent["position"], (x, y), 2)

            # Vykreslení bodu
            pygame.draw.circle(screen, point["color"], (int(x), int(y)), 10)

            # Přidání aktuální pozice do seznamu historie bodu
            if i == len(points) - 1:
                trail_points.append((int(x), int(y)))

        if stopa:
            trail_points = trail_points[-1000:]

        # Vykreslení stopy posledního bodu
        if len(trail_points) >= 2:
            pygame.draw.lines(screen, trail_color, False, trail_points, 1)
    else:
        for i, point in enumerate(points):
            # Výpočet aktuální polohy bodu
            current_time = cas_ted / time
            angle = math.radians(point["start_angle"]) + current_time * math.radians(point["angular_speed"])
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
                pygame.draw.line(screen, p_color, parent["position"], (x, y), 2)

            # Vykreslení bodu
            pygame.draw.circle(screen, point["color"], (int(x), int(y)), 10)


    malovani()

    # Když simulace neběží
    if not simulation_running:
        if len(trail_points) >= 2:
            pygame.draw.lines(screen, trail_color, False, trail_points, 1)

    # Obnovení obrazovky
    pygame.display.flip()

# Ukončení programu
pygame.quit()
