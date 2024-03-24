from gameclass import *

# Initialize Pygame
pygame.init()

# Récupérer la taille de l'écran
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
CARD_WIDTH = WIDTH // 15
CARD_HEIGHT = CARD_WIDTH * 3 // 2
BUTTON_WIDTH, BUTTON_HEIGHT = CARD_WIDTH*2, CARD_HEIGHT / 3 *2

# Créer une fenêtre en plein écran
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

# Adjust the 'Quit' button dimensions
QUIT_BUTTON_WIDTH, QUIT_BUTTON_HEIGHT = int(BUTTON_WIDTH / 2), int(BUTTON_HEIGHT / 2)

# Create a surface
surface = pygame.Surface((WIDTH, HEIGHT))

# Set the color key
surface.set_colorkey((0, 255, 0))

# On charge les images
arrow_image = pygame.image.load("arrow.png")
GAMEBG = pygame.image.load('backgroundblackjack2.png')

# Get the size of the original image
original_width, original_height = arrow_image.get_size()

# Calculate the aspect ratio
aspect_ratio = original_width / original_height

# Calculate the new width and height keeping aspect ratio constant and making it 1.5 times bigger
new_width = int(QUIT_BUTTON_HEIGHT * aspect_ratio * 1.5)
new_height = int(QUIT_BUTTON_HEIGHT * 1.5)

# Scale the image
arrow_image = pygame.transform.scale(arrow_image, (new_width, QUIT_BUTTON_HEIGHT))
game_background = pygame.transform.scale(GAMEBG, (WIDTH, HEIGHT))

button_y = HEIGHT - CARD_HEIGHT

# Load card images
from imageload import *

def draw_player_card(screen, card, i, y, game):
    """Draw a card on the screen at the given position."""
    # Calculate the position to draw the card
    x = WIDTH / 2 + i * (CARD_WIDTH * 1.5) - (len(game.playercard) * CARD_WIDTH * 1.5) / 2

    # Use the dictionary to look up the image to blit
    screen.blit(CARD_IMAGES[card.forme][card.nbr], (x, y))


def draw_dealer_card(screen, card, i, y, game, face_up=True):
    """Draw a card on the screen at the given position."""
    # Calculate the position to draw the card
    x = WIDTH / 2 + i * (CARD_WIDTH * 1.5) - (len(game.dealercard) * CARD_WIDTH * 1.5) / 2

    # Use the dictionary to look up the image to blit
    if face_up:
        screen.blit(CARD_IMAGES[card.forme][card.nbr], (x, y))
    else:
        screen.blit(CARD_BACK, (x, y))


def draw_button(screen, text, x, y, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=(0, 255, 0), alpha=256):
    """Draw a button on the screen at the given position."""
    # Create a surface for the button
    button_surface = pygame.Surface((width, height))

    # Fill the surface with the button color
    button_surface.fill(color)

    # Set the transparency level (alpha value)
    button_surface.set_alpha(alpha)

    # Draw the surface onto the screen
    screen.blit(button_surface, (x, y))

    # Calculate the font size based on the button's dimensions
    font_size = int(min(width, height) / 1.25)

    # Draw the text
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, (0, 0, 0))

    # Calculate the position: horizontally centered and vertically centered
    text_x = x + (width - text_surface.get_width()) / 2
    text_y = y + (height - text_surface.get_height()) / 2

    screen.blit(text_surface, (text_x, text_y))

def game_loop():
    """The main game loop."""
    clock = pygame.time.Clock()

    # Create a smaller font object
    small_font = pygame.font.Font(None, 30)

    # Initialize two variables to track if the 'Hit', 'Stand' and 'Next' buttons should be shown
    show_hit_button = False
    show_stand_button = False
    show_next_button = False
    show_rules_button = False
    show_rules = False

    # Initialize a variable to track if the dealer's second card should be face up
    dealer_second_card_face_up = False

    # Create a deck of cards
    deck = Jeu_Carte()

    # Create a game of Blackjack
    game = BlackJack("Player", deck)

    # Game state
    game_started = False

    # Create a font object
    font = pygame.font.Font(None, 36)

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Check if the 'Blackjack' button is clicked
                if WIDTH - (WIDTH // 3)*2 <= x <= WIDTH - (WIDTH // 3)  and 0 <= y <= HEIGHT:
                    game_started = True
                    show_hit_button = True
                    show_stand_button = True
                    show_rules_button = True

                # Check if the 'Hit' button is clicked
                if show_hit_button and x >= WIDTH / 2 - 2 * BUTTON_WIDTH and y >= button_y / 2 + BUTTON_HEIGHT / 2 and x <= WIDTH / 2 - 1 * BUTTON_WIDTH and y <= button_y / 2 + BUTTON_HEIGHT * 1.5:                    
                    if not game.Hit():
                        show_hit_button = False
                        show_stand_button = False
                        dealer_second_card_face_up = True
                        show_next_button = True
                # Check if the 'Stand' button is clicked
                elif show_stand_button and x >= WIDTH / 2 + 1 * BUTTON_WIDTH and y >= button_y / 2 + BUTTON_HEIGHT / 2 and x <= WIDTH / 2 + 2 * BUTTON_WIDTH and y <= button_y / 2 + BUTTON_HEIGHT * 1.5:
                    game.Stand()
                    show_stand_button = False
                    show_hit_button = False
                    dealer_second_card_face_up = True
                    show_next_button = True
                # Check if the 'Next' button is clicked
                elif show_next_button and x >= WIDTH / 2 + BUTTON_WIDTH * 2 and y >= button_y / 2 + BUTTON_HEIGHT / 2 and x <= WIDTH / 2 + BUTTON_WIDTH * 3 and y <= button_y / 2 + BUTTON_HEIGHT * 1.5:
                    game.Next()
                    show_next_button = False
                    show_hit_button = True
                    show_stand_button = True
                    dealer_second_card_face_up = False
                elif show_rules_button and x >= BUTTON_WIDTH / 4 and y >= BUTTON_HEIGHT / 4 and x <= BUTTON_WIDTH / 4 + BUTTON_WIDTH and y >= BUTTON_HEIGHT / 4 + BUTTON_WIDTH :
                    game_started = False
                    show_rules = True
                # Add a condition to check if the quit button is clicked
                elif x >= WIDTH - CARD_WIDTH / 2 and y >= 0 and x <= WIDTH and y <= BUTTON_HEIGHT:
                    game.Next()
                    show_next_button = False
                    show_hit_button = False
                    show_stand_button = False
                    dealer_second_card_face_up = False
                    show_rules_button = False
                    game_started = False

        # Clear the screen
        screen.fill((75, 143, 69))

        if game_started:
            # Draw the game background
            screen.blit(game_background, (0, 0))

            # Draw the dealer's hand
            for i, card in enumerate(game.dealercard):
                if i == 1 and not dealer_second_card_face_up:
                    draw_dealer_card(screen, card, i, HEIGHT / 2 - CARD_HEIGHT*2, game, face_up=False)
                else:
                    draw_dealer_card(screen, card, i, HEIGHT / 2 - CARD_HEIGHT*2, game)

            # Draw the player's hand
            for i, card in enumerate(game.playercard):
                draw_player_card(screen, card, i, HEIGHT / 3*2, game)

            # Draw the total value of the player's hand
            player_total = sum(card.value for card in game.playercard)
            player_total_text = small_font.render(f"{player_total}", True, (0, 0, 0))
            screen.blit(player_total_text, (WIDTH / 2 - (len(game.playercard) * CARD_WIDTH * 1.5 + (len(game.playercard) - 1) * 10) / 2 - player_total_text.get_width() - 10, HEIGHT / 3*2 + CARD_HEIGHT / 2))

            # Draw the total value of the dealer's face-up cards
            if dealer_second_card_face_up:
                dealer_total = sum(card.value for card in game.dealercard)
            else:
                dealer_total = game.dealercard[0].value  # Only the first card is face up
            dealer_total_text = small_font.render(f"{dealer_total}", True, (0, 0, 0))
            screen.blit(dealer_total_text, (WIDTH / 2 - (len(game.dealercard) * CARD_WIDTH * 1.5 + (len(game.dealercard) - 1) * 10) / 2 - dealer_total_text.get_width() - 10, HEIGHT / 2 - CARD_HEIGHT*1.5))  

            # Draw the labels
            label_dealer1 = small_font.render("Dealer's", True, (255, 255, 255))
            label_dealer2 = small_font.render("hand", True, (255, 255, 255))
            label_player1 = small_font.render("Your", True, (255, 255, 255))
            label_player2 = small_font.render("cards", True, (255, 255, 255))
            screen.blit(label_dealer1, (10, HEIGHT / 2 - CARD_HEIGHT - 50))
            screen.blit(label_dealer2, (10, HEIGHT / 2 - CARD_HEIGHT - 30))
            screen.blit(label_player1, (10, HEIGHT / 2 + 20))
            screen.blit(label_player2, (10, HEIGHT / 2 + 40))

            # Draw the 'Hit', 'Stand', and 'Next' buttons below the player's cards
            if show_hit_button:
                draw_button(screen, "Hit", WIDTH / 2 - 2 * BUTTON_WIDTH, button_y / 2 + BUTTON_HEIGHT / 2)
            if show_stand_button:
                draw_button(screen, "Stand", WIDTH / 2 + BUTTON_WIDTH, button_y / 2 + BUTTON_HEIGHT / 2)
            if show_next_button:
                draw_button(screen, "Next", WIDTH / 2 + BUTTON_WIDTH * 2, button_y / 2 + BUTTON_HEIGHT / 2)
            if show_rules_button:
                draw_button(screen, "Rules", BUTTON_WIDTH / 4, BUTTON_HEIGHT / 4)

            # Draw the game result between the player's and dealer's hands
            if not show_hit_button and not show_stand_button:
                result = game.Check()

                # Increase the font size for the result text
                result_font_size = 50
                result_font = pygame.font.Font(None, result_font_size)
                result_text = result_font.render(result, True, (255, 255, 255))
                y_offset = 50
                screen.blit(result_text, (WIDTH / 2 - result_text.get_width() / 2, HEIGHT / 2 - result_text.get_height() / 0.7 + y_offset))

            # Draw the arrow image in the top right corner, moved a bit more to the left
            screen.blit(arrow_image, (WIDTH - CARD_WIDTH / 2, BUTTON_HEIGHT / 3))
        elif show_rules:
            draw_button(screen,"Back", WIDTH - CARD_WIDTH, HEIGHT - CARD_HEIGHT / 2)
            label_rules1 = small_font.render("Règles :", True, (255, 255, 255))
            label_rules2 = small_font.render("Le but est d'avoir plus de point que son adversaire sans dépasser 21", True, (255, 255, 255))
            label_rules3 = small_font.render("Pour cela, on doit soit 'Hit', donc prendre une carte, soit 'Stand', donc arrêter le jeu et voir qui a gagné", True, (255, 255, 255))
            label_rules4 = small_font.render("Chaque cartes valent leur valeurs respective, à l'exception de l'As, Valet, Dame et Roi", True, (255, 255, 255))
            label_rules5 = small_font.render("Le Valet, la Dame et le Roi valent tous les trois 10, et l'As peut soit valoir 11, soit valoir 1 (cela est calculé automatiquement)", True, (255, 255, 255))
            screen.blit(label_rules1, (10, HEIGHT / 2 - CARD_HEIGHT - 50))
            screen.blit(label_rules2, (10, HEIGHT / 2 - CARD_HEIGHT - 50))
            screen.blit(label_rules3, (10, HEIGHT / 2 - CARD_HEIGHT - 50))
            screen.blit(label_rules4, (10, HEIGHT / 2 - CARD_HEIGHT - 50))
            screen.blit(label_rules5, (10, HEIGHT / 2 - CARD_HEIGHT - 50))
        else:
            # Draw the 'Blackjack' button
            draw_button(screen, "Blackjack", (WIDTH - BUTTON_WIDTH) / 2, 0, BUTTON_WIDTH, BUTTON_HEIGHT, alpha = 0)

            # Draw vertical lines down the screen
            pygame.draw.line(screen, (0, 0, 0), (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), 1)
            pygame.draw.line(screen, (0, 0, 0), (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), 1)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Run the game
game_loop()