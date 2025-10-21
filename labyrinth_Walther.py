
#Gruppe: Hannah Schmidt; Collien Walther

import pygame

pygame.init() 
pygame.display.set_caption("Mini Pygame-Programm")  # Fenstertitel

# Laden der Bilder
try:
    image1 = pygame.image.load("herz.jpg")  # Bild für die Spielfigur
    image1.set_colorkey((255, 0, 255))  # Transparente Farbe festlegen
    wand_img = pygame.image.load("pink.jpg")  # Bild für die Wand
    weg_img = pygame.image.load("weg.jpg")   # Bild für den Weg
    ziel_img = pygame.image.load("kreis.jpg") #Bild Ziel
    pfeil_img = pygame.image.load("Pfeil.jpg") #Bild Pfeil
    symbol_img = pygame.image.load("Pfeilrechts.jpg")
    
except:
    print("Fehler beim Laden der Bilder:")
    pygame.quit()
    exit()

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#Startposition
spieler_position=[1,1]
#Zielposition
ziel_position = [23,23]
#Pfeilposition
pfeil1_position=[2,1]
pfeil2_position=[22,23]
pfeil3_position=[23,22]


# Berechnung der Zellengröße
fensterbreite = 800
fensterhöhe = 600
anzahl_spalten = len(maze[0])
anzahl_zeilen = len(maze)
zellengröße = min(fensterbreite // anzahl_spalten, fensterhöhe // anzahl_zeilen)
fensterbreite = anzahl_spalten * zellengröße
fensterhöhe = anzahl_zeilen * zellengröße
screen = pygame.display.set_mode((fensterbreite, fensterhöhe))
wand_img = pygame.transform.scale(wand_img, (zellengröße, zellengröße))
weg_img = pygame.transform.scale(weg_img, (zellengröße, zellengröße))
image1 = pygame.transform.scale(image1, (zellengröße, zellengröße))
ziel_img = pygame.transform.scale(ziel_img, (zellengröße, zellengröße))
symbol_img = pygame.transform.scale(symbol_img, (zellengröße, zellengröße))
pfeil_img = pygame.transform.scale(pfeil_img, (zellengröße, zellengröße))

# Schriftart und Größe definieren
font = pygame.font.Font(None, 50)  # Standard-Schriftart, Größe 50

def zeichne_labyrinth(matrix, wand_img, weg_img):
    #Zeichnet das Labyrinth einmal auf den Bildschirm
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            x = col_index * zellengröße
            y = row_index * zellengröße
            if cell == 1:  # Wand
                screen.blit(wand_img, (x, y))
            else:  # Weg
                screen.blit(weg_img, (x, y))


def zeichne_ziel(position):
    #Ziel an Zielposition zeichnen
    x = position[1]*zellengröße
    y = position[0]*zellengröße
    screen.blit(ziel_img, (x,y))

def zeichne_pfeil1(position):
    #Pfeil an Zielposition zeichnen
    x = position[1]*zellengröße
    y = position[0]*zellengröße
    screen.blit(pfeil_img, (x,y))

def zeichne_pfeil2(position):
    x = position[1]*zellengröße
    y = position[0]*zellengröße
    screen.blit(pfeil_img, (x,y))

def zeichne_pfeil3(position):
    x = position[1]*zellengröße
    y = position[0]*zellengröße
    screen.blit(symbol_img, (x,y))

def zeichne_spielfigur(position):
    #Zeichnet die Spielfigur an der aktuellen Position
    x = position[1] * zellengröße  # Spalte -> x
    y = position[0] * zellengröße  # Zeile -> y
    screen.blit(image1, (x, y))

def zeichne_box(text,x, y, breite, hoehe, hintergrund=(255, 255, 255), schriftfarbe=(0, 0, 0)):
    #Rechteck für die Box
    textbox_rect = pygame.Rect(x, y, breite, hoehe)
    pygame.draw.rect(screen, hintergrund, textbox_rect)  # Hintergrund zeichnen
    pygame.draw.rect(screen, (0, 0, 0), textbox_rect, 2)  # Rahmen zeichnen
    # Text rendern und zentrieren
    text_surface = font.render(text, True, schriftfarbe)
    text_rect = text_surface.get_rect(center=textbox_rect.center)
    screen.blit(text_surface, text_rect)

# Siegbedingung überprüfen
ziel_erreicht = False  # Status, ob Ziel erreicht wurde


def zeichne_gewonnen_text():
    #Boxgröße und Position
    box_breite, box_hoehe = 300, 100
    box_x = (fensterbreite - box_breite)//2
    box_y = (fensterhöhe - box_hoehe)//2
    #Text in der Mte der Box
    zeichne_box(
        "Ziel erreicht!",
        box_x,
        box_y,
        box_breite,
        box_hoehe,
        hintergrund=(255, 192, 203),
        schriftfarbe=(255, 255, 255)
    )

# Hintergrund nur einmal zeichnen
zeichne_labyrinth(maze, wand_img, weg_img)
zeichne_ziel(ziel_position)
pygame.display.flip()

#Bewegung
running = True
ziel_erreicht=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            neue_position = list(spieler_position)
            if event.key == pygame.K_w or event.key == pygame.K_UP:  # Hoch
                neue_position[0] -= 1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  # Runter
                neue_position[0] += 1
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  # Links
                neue_position[1] -= 1
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # Rechts
                neue_position[1] += 1

            # Überprüfen, ob die neue Position gültig ist
            if (
                0 <= neue_position[0] < anzahl_zeilen and
                0 <= neue_position[1] < anzahl_spalten and
                maze[neue_position[0]][neue_position[1]] == 0
            ):
                spieler_position = neue_position

 #Überprüfen ob Ziel erreicht wurde
    if spieler_position == ziel_position:
        ziel_erreicht=True
        running=False
    if ziel_erreicht:
        zeichne_gewonnen_text()
        pygame.display.flip()
        pygame.time.wait(10000)  # 2 Sekunden warten, bevor das Spiel beendet wird
        running = False  # Spiel beenden

    # Hintergrund und Figur aktualisieren
    screen.fill((0, 0, 0))  # Bildschirm löschen
    zeichne_labyrinth(maze, wand_img, weg_img)  # Labyrinth erneut zeichnen
    zeichne_ziel(ziel_position)
    zeichne_pfeil1(pfeil1_position)
    zeichne_pfeil2(pfeil2_position)
    zeichne_pfeil3(pfeil3_position)
    zeichne_spielfigur(spieler_position)  # Spielfigur zeichnen #Änderung damit Figur über Pfeil
    pygame.display.flip()  # Alle Änderungen auf dem Bildschirm anzeigen

   

pygame.quit()

