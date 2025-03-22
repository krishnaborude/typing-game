import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FONT_SIZE = 32
FONT = pygame.font.Font(None, FONT_SIZE)
SCROLL_SPEED = 2  # Base scroll speed
TYPING_SCROLL_SPEED = 4  # Faster scroll speed when typing

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Sample sentences for the game
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language for beginners.",
    "Practice makes perfect when learning to type.",
    "Coding is fun and helps solve real problems.",
    "The weather is beautiful outside today.",
    "Learning to program opens many opportunities.",
    "Typing speed improves with regular practice.",
    "Computer science is an exciting field to study.",
    "Programming games can be both fun and educational.",
    "The best way to learn is by doing."
]

class TypingGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Typing Game - Scrolling Sentences")
        self.clock = pygame.time.Clock()
        self.sentences = []  # List of (sentence, x_position) tuples
        self.user_input = ""
        self.score = 0
        self.start_time = 0
        self.wpm = 0
        self.accuracy = 100
        self.game_active = True
        self.game_over = False
        self.total_characters = 0
        self.correct_characters = 0
        self.wrong_characters = 0
        self.current_sentence_index = 0
        self.last_typing_time = 0
        self.initialize_sentences()

    def initialize_sentences(self):
        # Create initial set of sentences with their x positions
        x = WINDOW_WIDTH
        for _ in range(5):  # Start with 5 sentences
            sentence = random.choice(SENTENCES)
            self.sentences.append((sentence, x))
            x += len(sentence) * FONT_SIZE // 2 + 100  # Add space between sentences

    def add_new_sentence(self):
        # Add a new sentence when needed
        if self.sentences[-1][1] < WINDOW_WIDTH:
            sentence = random.choice(SENTENCES)
            x = self.sentences[-1][1] + len(self.sentences[-1][0]) * FONT_SIZE // 2 + 100
            self.sentences.append((sentence, x))

    def update_accuracy(self):
        total = self.correct_characters + self.wrong_characters
        if total > 0:
            self.accuracy = int((self.correct_characters / total) * 100)

    def check_sentence_complete(self):
        if not self.sentences:  # Check if there are any sentences
            return False
            
        if len(self.user_input) == len(self.sentences[0][0]):
            if self.user_input == self.sentences[0][0]:
                self.score += 1
            self.user_input = ""
            self.sentences.pop(0)  # Remove completed sentence
            self.add_new_sentence()  # Add new sentence at the end
            return True
        return False

    def draw_game(self):
        self.screen.fill(BLACK)
        
        # Draw all sentences
        for sentence, x_pos in self.sentences:
            # Only draw if sentence is visible on screen
            if x_pos + len(sentence) * FONT_SIZE // 2 > 0:
                y = WINDOW_HEIGHT // 2 - 50
                current_x = x_pos
                
                for i, char in enumerate(sentence):
                    color = GRAY  # Default color for untyped letters
                    if i < len(self.user_input) and sentence == self.sentences[0][0]:
                        if self.user_input[i] == char:
                            color = GREEN  # Correct letter
                        else:
                            color = RED  # Wrong letter
                    
                    char_text = FONT.render(char, True, color)
                    self.screen.blit(char_text, (current_x, y))
                    current_x += FONT_SIZE // 2

        # Draw user input below the sentences
        if self.user_input:
            input_y = WINDOW_HEIGHT // 2 + 50
            input_x = WINDOW_WIDTH // 2 - (len(self.user_input) * FONT_SIZE // 4)
            input_text = FONT.render(self.user_input, True, WHITE)
            self.screen.blit(input_text, (input_x, input_y))

        # Draw score and stats
        score_text = FONT.render(f"Score: {self.score}", True, WHITE)
        wpm_text = FONT.render(f"WPM: {self.wpm}", True, WHITE)
        accuracy_text = FONT.render(f"Accuracy: {self.accuracy}%", True, WHITE)
        
        # Calculate and display remaining time
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, 60 - elapsed_time)
        time_text = FONT.render(f"Time: {int(remaining_time)}s", True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(wpm_text, (10, 50))
        self.screen.blit(accuracy_text, (10, 90))
        self.screen.blit(time_text, (WINDOW_WIDTH - 150, 10))

        # Draw instructions
        instructions = FONT.render("Type the sentences as they scroll, Escape to quit", True, WHITE)
        self.screen.blit(instructions, (WINDOW_WIDTH // 2 - instructions.get_width() // 2, WINDOW_HEIGHT - 50))

        pygame.display.flip()

    def draw_results(self):
        self.screen.fill(BLACK)
        
        # Calculate final statistics
        final_wpm = int((self.correct_characters / 5) / 1)  # WPM for the full minute
        final_accuracy = int((self.correct_characters / max(1, self.total_characters)) * 100)
        
        # Draw results
        title = FONT.render("Game Over! Final Results", True, WHITE)
        score_text = FONT.render(f"Final Score: {self.score}", True, WHITE)
        wpm_text = FONT.render(f"Final WPM: {final_wpm}", True, WHITE)
        accuracy_text = FONT.render(f"Final Accuracy: {final_accuracy}%", True, WHITE)
        restart_text = FONT.render("Press SPACE to play again or ESC to quit", True, WHITE)
        
        # Position all text elements
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
        wpm_rect = wpm_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        accuracy_rect = accuracy_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT * 3 // 4))
        
        # Draw all text elements
        self.screen.blit(title, title_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(wpm_text, wpm_rect)
        self.screen.blit(accuracy_text, accuracy_rect)
        self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()

    def reset_game(self):
        self.sentences = []
        self.user_input = ""
        self.score = 0
        self.start_time = time.time()
        self.wpm = 0
        self.accuracy = 100
        self.game_active = True
        self.game_over = False
        self.total_characters = 0
        self.correct_characters = 0
        self.wrong_characters = 0
        self.current_sentence_index = 0
        self.last_typing_time = 0
        self.initialize_sentences()

    def run(self):
        while self.game_active:
            current_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_active = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_active = False
                    elif event.key == pygame.K_SPACE and self.game_over:
                        self.reset_game()
                    elif not self.game_over:
                        if event.key == pygame.K_BACKSPACE:
                            if self.user_input:  # Only remove if there's input
                                self.user_input = self.user_input[:-1]
                        else:
                            if event.unicode.isprintable():
                                self.user_input += event.unicode
                                self.total_characters += 1
                                self.last_typing_time = current_time
                                # Check if the typed character is correct
                                if self.sentences and self.user_input and len(self.user_input) <= len(self.sentences[0][0]):
                                    current_char = self.user_input[-1]
                                    target_char = self.sentences[0][0][len(self.user_input)-1]
                                    if current_char == target_char:
                                        self.correct_characters += 1
                                        # Check if sentence is complete
                                        self.check_sentence_complete()
                                    else:
                                        self.wrong_characters += 1
                                    self.update_accuracy()

            if not self.game_over:
                # Check if time is up
                elapsed_time = time.time() - self.start_time
                if elapsed_time >= 60:
                    self.game_over = True
                else:
                    # Determine scroll speed based on typing
                    current_scroll_speed = TYPING_SCROLL_SPEED if current_time - self.last_typing_time < 0.5 else SCROLL_SPEED
                    
                    # Scroll sentences
                    for i in range(len(self.sentences)):
                        sentence, x = self.sentences[i]
                        self.sentences[i] = (sentence, x - current_scroll_speed)
                    
                    # Calculate WPM
                    if elapsed_time > 0:
                        self.wpm = int((len(self.user_input) / 5) / (elapsed_time / 60))
                    self.draw_game()
            else:
                self.draw_results()

            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = TypingGame()
    game.run()
