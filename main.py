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
        pygame.display.set_caption("Typing Game - 1 Minute Challenge")
        self.clock = pygame.time.Clock()
        self.current_sentence = ""
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
        self.new_sentence()

    def new_sentence(self):
        self.current_sentence = random.choice(SENTENCES)
        self.user_input = ""
        self.start_time = time.time()

    def update_accuracy(self):
        total = self.correct_characters + self.wrong_characters
        if total > 0:
            self.accuracy = int((self.correct_characters / total) * 100)

    def draw_game(self):
        self.screen.fill(BLACK)
        
        # Draw current sentence with highlighting
        x = WINDOW_WIDTH // 2 - (len(self.current_sentence) * FONT_SIZE // 4)
        y = WINDOW_HEIGHT // 2 - 50
        
        for i, char in enumerate(self.current_sentence):
            color = GRAY  # Default color for untyped letters
            if i < len(self.user_input):
                if self.user_input[i] == char:
                    color = GREEN  # Correct letter
                else:
                    color = RED  # Wrong letter
            
            char_text = FONT.render(char, True, color)
            self.screen.blit(char_text, (x, y))
            x += FONT_SIZE // 2

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
        instructions = FONT.render("Type the sentence above, Press Enter to submit, Escape to quit", True, WHITE)
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
        self.current_sentence = ""
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
        self.new_sentence()

    def run(self):
        while self.game_active:
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
                            self.user_input = self.user_input[:-1]
                        elif event.key == pygame.K_RETURN:
                            if self.user_input == self.current_sentence:
                                self.score += 1
                                self.new_sentence()
                        else:
                            if event.unicode.isprintable():
                                self.user_input += event.unicode
                                self.total_characters += 1
                                # Check if the typed character is correct
                                if len(self.user_input) <= len(self.current_sentence):
                                    if self.user_input[-1] == self.current_sentence[len(self.user_input)-1]:
                                        self.correct_characters += 1
                                    else:
                                        self.wrong_characters += 1
                                    self.update_accuracy()

            if not self.game_over:
                # Check if time is up
                elapsed_time = time.time() - self.start_time
                if elapsed_time >= 60:
                    self.game_over = True
                else:
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
