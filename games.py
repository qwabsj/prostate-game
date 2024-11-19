import pygame
import random

# Initialize pygame and sound mixer
pygame.init()
pygame.mixer.init()

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 10
CELL_SIZE = 45
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Define snakes and ladders with positions
snakes = {11: 10, 48: 28, 41: 23, 64: 44, 68: 31, 88: 72, 91: 71, 94: 87, 98: 83}
ladders = {1: 20, 2: 19, 4: 16, 13: 35, 18: 75, 21: 39, 38: 61, 36: 54, 50: 69, 70: 90, 67: 73, 75: 96, 76: 84, 80: 82, 63: 77, 85: 100, 58: 100}

# Sample questions for the game
questions = [
     {"question": "The prostate is a small gland in men that produces seminal fluid. TRUE or FALSE?", "answer": "True"},
    {"question": "Prostate cancer is most commonly diagnosed in Black men over 55 and White men over 65. TRUE or FALSE?", "answer": "True"},
    {"question": "Prostate cancer can often be asymptomatic in its early stages. TRUE or FALSE?", "answer": "True"},
    {"question": "PSA stands for Prostate-Specific Antigen, a protein produced by the prostate. TRUE or FALSE?", "answer": "True"},
    {"question": "A PSA test measures prostate-specific antigen levels to help detect cancer. TRUE or FALSE?", "answer": "True"},
    {"question": "A digital rectal exam (DRE) involves a doctor examining the prostate through the rectum. TRUE or FALSE?", "answer": "True"},
    {"question": "Difficulty urinating can be a symptom of prostate cancer. TRUE or FALSE?", "answer": "True"},
    {"question": "Having a family history of prostate cancer does not affect your risk. TRUE or FALSE?", "answer": "False"},
    {"question": "Surgery to remove the prostate is a common treatment option. TRUE or FALSE?", "answer": "True"},
    {"question": "Active surveillance involves closely monitoring prostate cancer without immediate treatment. TRUE or FALSE?", "answer": "True"},
    {"question": "A diet high in red meat and dairy may increase the risk of prostate cancer. TRUE or FALSE?", "answer": "True"},
    {"question": "The Gleason score grades prostate cancer based on its microscopic appearance. TRUE or FALSE?", "answer": "True"},
    {"question": "Hormone therapy for prostate cancer blocks the production of hormones that fuel growth. TRUE or FALSE?", "answer": "True"},
    {"question": "The most common type of prostate cancer is adenocarcinoma. TRUE or FALSE?", "answer": "True"},
    {"question": "African American men have a lower risk of prostate cancer compared to other races. TRUE or FALSE?", "answer": "False"},
    {"question": "Men with a positive family history of prostate cancer are at higher risk. TRUE or FALSE?", "answer": "True"},
    {"question": "Men with a positive family history of breast cancer may have a higher risk of prostate cancer. TRUE or FALSE?", "answer": "True"},
    {"question": "Prostate cancer screenings are recommended for men over 50. TRUE or FALSE?", "answer": "True"},
    {"question": "MRI can help detect and stage prostate cancer. TRUE or FALSE?", "answer": "True"},
    {"question": "A prostate biopsy involves taking small samples of prostate tissue to check for cancer. TRUE or FALSE?", "answer": "True"},
    {"question": "Healthy lifestyle changes can improve quality of life for prostate cancer patients. TRUE or FALSE?", "answer": "True"},
    {"question": "Cryotherapy uses cold-freeze therapy to destroy cancerous tissue in the prostate. TRUE or FALSE?", "answer": "True"},
    {"question": "Some men with prostate cancer may have normal PSA levels. TRUE or FALSE?", "answer": "True"},
    {"question": "Some men without prostate cancer may have high PSA levels. TRUE or FALSE?", "answer": "True"},
    {"question": "Watchful waiting involves monitoring prostate cancer symptoms without active treatment. TRUE or FALSE?", "answer": "True"},
    {"question": "Prostate cancer and its treatments can affect sexual function. TRUE or FALSE?", "answer": "True"},
    {"question": "Obesity is linked to a higher risk of aggressive prostate cancer. TRUE or FALSE?", "answer": "False"},
    {"question": "Genetic mutations like BRCA1/2 can increase prostate cancer risk. TRUE or FALSE?", "answer": "True"},
    {"question": "Prostate cancer is more common in North America than other regions. TRUE or FALSE?", "answer": "True"},
    {"question": "Regular exercise may help reduce prostate cancer risk. TRUE or FALSE?", "answer": "True"},
    {"question": "External beam radiation uses high-energy rays to target and destroy prostate cancer cells. TRUE or FALSE?", "answer": "True"},
    {"question": "Smoking is linked to an increased risk of prostate cancer progression. TRUE or FALSE?", "answer": "True"},
    {"question": "Chemotherapy is used for advanced prostate cancer. TRUE or FALSE?", "answer": "True"},
    {"question": "Prostatitis can cause elevated PSA levels. TRUE or FALSE?", "answer": "True"},
    {"question": "BPH is a malignant tumor of the prostate. TRUE or FALSE?", "answer": "False"},
    {"question": "Moderate alcohol consumption is not clearly associated with prostate cancer risk. TRUE or FALSE?", "answer": "True"},
    {"question": "Managing stress can improve well-being for prostate cancer patients. TRUE or FALSE?", "answer": "True"},
    {"question": "The TNM staging system classifies prostate cancer by tumor size, lymph nodes, and metastasis. TRUE or FALSE?", "answer": "True"},
    {"question": "Surgery and radiation can cause erectile dysfunction in prostate cancer patients. TRUE or FALSE?", "answer": "True"},
    {"question": "ADT is a treatment that increases androgen levels. TRUE or FALSE?", "answer": "False"},
    {"question": "Immunotherapy helps the immune system target prostate cancer cells. TRUE or FALSE?", "answer": "True"},
    {"question": "Bone pain can occur if prostate cancer spreads to the bones. TRUE or FALSE?", "answer": "True"},
    {"question": "Fatigue is a common side effect of radiation therapy for prostate cancer. TRUE or FALSE?", "answer": "True"},
    {"question": "A healthy diet can improve prostate cancer treatment outcomes. TRUE or FALSE?", "answer": "True"},
    {"question": "Prostate cancer treatments cannot cause urinary incontinence. TRUE or FALSE?", "answer": "False"},
    {"question": "A urologist specializes in diseases of the urinary tract and male reproductive organs. TRUE or FALSE?", "answer": "True"},
    {"question": "Regular screening helps detect prostate cancer early. TRUE or FALSE?", "answer": "True"},
    {"question": "Phytochemicals in plants may help lower prostate cancer risk. TRUE or FALSE?", "answer": "True"},
]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LUDU LITE PROSTATE CANCER")

# Fonts
font = pygame.font.Font(None, 28)
small_font = pygame.font.Font(None, 20)

# Game variables
dice_value = 1
player_positions = [0, 0]
current_player = 0
game_over = False
question_active = False
question_text = ""
correct_answer = ""
position_queried = None
player_names = ["Player 1", "Player 2"]
player_inputs = ["", ""]
current_input_index = 0
game_started = False

# Load images and sounds (update paths as needed)
board_image = pygame.image.load('assets/game.jpg')
board_image = pygame.transform.scale(board_image, (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
dice_images = [pygame.transform.scale(pygame.image.load(f'assets/dice{i+1}.png'), (40, 40)) for i in range(6)]
player_images = [
    pygame.transform.scale(pygame.image.load('assets/favicon1111.ico'), (CELL_SIZE, CELL_SIZE)),
    pygame.transform.scale(pygame.image.load('assets/favicon22.ico'), (CELL_SIZE, CELL_SIZE))
]
dice_sound = pygame.mixer.Sound('assets/dice_roll.mp3')
win_sound = pygame.mixer.Sound('assets/win.mp3')

# Display the rules and input names screen
def display_intro():
    screen.fill(WHITE)
    rules = [
        "Game Rules:",
        "1. Players: 2 players with different color counters.",
        "2. Start: Roll a six to begin. Move forward by dice roll.",
        "3. Ladders advance you. Snakes send you back.",
        "4. Answer questions to avoid snakes and climb ladders.",
    ]
    y = 50
    for line in rules:
        rule_text = font.render(line, True, BLACK)
        screen.blit(rule_text, (50, y))
        y += 20
    
    # Display name prompt
    input_prompt = font.render(f"Enter name for {player_names[current_input_index]}:", True, BLACK)
    screen.blit(input_prompt, (50, y + 30))
    input_text = font.render(player_inputs[current_input_index], True, BLUE)
    screen.blit(input_text, (50, y + 60))
    
    if current_input_index == 1 and player_inputs[1]:
        start_text = font.render("Press ENTER to start the game.", True, GREEN)
    else:
        start_text = font.render("Press ENTER to confirm each name.", True, GREEN)
    screen.blit(start_text, (50, SCREEN_HEIGHT - 50))

# Draw board, players, question, and dashboard
def draw_board():
    screen.fill(WHITE)
    screen.blit(board_image, (CELL_SIZE * 2, 0))

def draw_players():
    for i in range(2):
        x, y = get_position_coordinates(player_positions[i])
        screen.blit(player_images[i], (x, y))

def draw_question():
    max_width = SCREEN_WIDTH - 100
    lines = []
    words = question_text.split()
    line = ""
    for word in words:
        test_line = f"{line} {word}".strip()
        if font.size(test_line)[0] < max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    lines.append(line)  # Add the last line

    y_offset = SCREEN_HEIGHT - 150
    for line in lines:
        question_surface = font.render(line, True, BLACK)
        screen.blit(question_surface, (50, y_offset))
        y_offset += font.get_height() + 5

def draw_dashboard():
    pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))
    turn_text = small_font.render(f"Turn: {player_names[current_player]}", True, BLACK)
    screen.blit(turn_text, (10, SCREEN_HEIGHT - 90))
    dice_img = dice_images[dice_value - 1]
    screen.blit(dice_img, (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 90))

# Position calculation for each cell
def get_position_coordinates(position):
    if position == 0:
        start_x = CELL_SIZE // 2 + CELL_SIZE // 2
        start_y = SCREEN_HEIGHT - (GRID_SIZE * CELL_SIZE) // 2
        return start_x, start_y
    else:
        row = (position - 1) // GRID_SIZE
        col = (position - 1) % GRID_SIZE
        if row % 2 == 1:
            col = GRID_SIZE - 1 - col
        x = col * CELL_SIZE + CELL_SIZE * 2
        y = (GRID_SIZE - 1 - row) * CELL_SIZE
        return x, y

# Roll dice with random value
def roll_dice():
    global dice_value
    dice_value = random.randint(1, 6)
    dice_sound.play()
    print(f"{player_names[current_player]} rolled a {dice_value}")

# Animation for smooth player movement
def animate_movement(start_pos, end_pos):
    start_x, start_y = get_position_coordinates(start_pos)
    end_x, end_y = get_position_coordinates(end_pos)
    steps = 20
    for step in range(steps):
        current_x = start_x + (end_x - start_x) * (step / steps)
        current_y = start_y + (end_y - start_y) * (step / steps)
        draw_board()
        draw_dashboard()
        draw_players()
        screen.blit(player_images[current_player], (current_x, current_y))
        pygame.display.flip()
        pygame.time.delay(30)

# Move player to new position and ask question if landing on snake or ladder
def move_player():
    global current_player, game_over, question_active, question_text, correct_answer, position_queried

    if player_positions[current_player] == 0 and dice_value != 6:
        current_player = (current_player + 1) % 2
        return
    elif player_positions[current_player] == 0:
        player_positions[current_player] = 1
    else:
        new_position = min(player_positions[current_player] + dice_value, 100)
        animate_movement(player_positions[current_player], new_position)
        player_positions[current_player] = new_position

        if new_position in ladders or new_position in snakes:
            position_queried = new_position
            ask_question(new_position)
        else:
            # If no snake or ladder, end the turn
            current_player = (current_player + 1) % 2

    if player_positions[current_player] == 100:
        win_sound.play()
        game_over = True
        print(f"{player_names[current_player]} wins!")

# Ask question when landing on a snake or ladder
def ask_question(position):
    global question_active, question_text, correct_answer
    question = random.choice(questions)
    question_text = question["question"]
    correct_answer = question["answer"]
    question_active = True

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    if not game_started:
        display_intro()
    else:
        draw_board()
        draw_dashboard()
        draw_players()

        if question_active:
            draw_question()

        if game_over:
            restart_button = pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, 40))
            screen.blit(small_font.render("Restart", True, BLACK), restart_button.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif not game_started and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                player_inputs[current_input_index] = player_inputs[current_input_index][:-1]
            elif event.key == pygame.K_RETURN:
                if player_inputs[current_input_index]:
                    player_names[current_input_index] = player_inputs[current_input_index]
                    if current_input_index == 1:
                        game_started = True
                    else:
                        current_input_index += 1
            elif event.unicode.isprintable():
                player_inputs[current_input_index] += event.unicode

        elif question_active and event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_t and correct_answer == "True") or (event.key == pygame.K_f and correct_answer == "False"):
                print("Correct answer!")
                if position_queried in ladders:
                    player_positions[current_player] = ladders[position_queried]
                elif position_queried in snakes:
                    pass  # Avoid the snake penalty
            else:
                print("Incorrect answer.")
                if position_queried in ladders:
                    pass  # No ladder benefit if wrong
                elif position_queried in snakes:
                    player_positions[current_player] = snakes[position_queried]
            
            question_active = False
            current_player = (current_player + 1) % 2

        elif not question_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                roll_dice()
                move_player()

        elif game_over and event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button.collidepoint(event.pos):
                # Reset the game
                player_positions = [0, 0]
                current_player = 0
                game_over = False
                game_started = False
                player_inputs = ["", ""]
                current_input_index = 0
                print("Game restarted!")

    pygame.display.update()

pygame.quit()
