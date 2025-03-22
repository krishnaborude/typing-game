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
YELLOW = (255, 255, 0)

# Sample words for the game
WORDS = [
    "about", "above", "accept", "accident", "according", "account", "across", "action", "actually", "address",
    "admit", "adopt", "adult", "after", "afternoon", "again", "against", "agree", "ahead", "air",
    "alarm", "album", "alive", "allow", "almost", "alone", "along", "already", "also", "always",
    "among", "amount", "anger", "angle", "angry", "animal", "answer", "anxiety", "anxious", "any",
    "apart", "appear", "apple", "apply", "area", "argue", "around", "arrive", "article", "artist",
    "aside", "asleep", "aspect", "assume", "attack", "attend", "attention", "attitude", "author", "avoid",
    "aware", "away", "baby", "back", "background", "balance", "ball", "band", "bank", "bar",
    "base", "basic", "battle", "beach", "beauty", "become", "before", "begin", "behind", "believe",
    "below", "beneath", "benefit", "beside", "between", "beyond", "birth", "black", "blame", "blank",
    "blind", "block", "blood", "board", "body", "border", "bottle", "bottom", "brain", "branch",
    "break", "breath", "bridge", "brief", "bright", "bring", "broad", "brown", "build", "burn",
    "business", "button", "camera", "campaign", "cancel", "cancer", "candidate", "capital", "capture", "care",
    "career", "carry", "catch", "cause", "center", "central", "century", "certain", "chair", "challenge",
    "chance", "change", "character", "charge", "check", "child", "choice", "choose", "church", "circle",
    "citizen", "city", "civil", "claim", "class", "clean", "clear", "climb", "clock", "close",
    "coast", "color", "come", "comfort", "command", "common", "company", "compare", "computer", "concern",
    "condition", "connect", "consider", "contain", "control", "cost", "could", "count", "country", "course",
    "court", "cover", "create", "crime", "cross", "crowd", "current", "custom", "damage", "danger",
    "dark", "daughter", "dead", "deal", "death", "debate", "decade", "decide", "decision", "deep",
    "defense", "degree", "depend", "describe", "design", "desire", "detail", "determine", "develop", "difference",
    "difficult", "dinner", "direct", "direction", "discover", "discuss", "disease", "doctor", "dollar", "door",
    "double", "doubt", "down", "draw", "dream", "drive", "drop", "drug", "during", "early",
    "earth", "east", "economy", "edge", "effect", "effort", "eight", "either", "election", "else",
    "employee", "energy", "enjoy", "enough", "enter", "entire", "environment", "error", "even", "event",
    "every", "everyone", "everything", "evidence", "exact", "example", "except", "exchange", "exist", "expect",
    "experience", "expert", "explain", "express", "extend", "extra", "extreme", "eye", "face", "fact",
    "factor", "fail", "fall", "family", "famous", "farm", "father", "fear", "federal", "feel",
    "feeling", "field", "fight", "figure", "fill", "film", "final", "financial", "find", "fine",
    "finger", "finish", "fire", "firm", "first", "fish", "five", "floor", "focus", "follow",
    "food", "force", "foreign", "forget", "form", "former", "forward", "four", "free", "friend",
    "front", "full", "fund", "future", "game", "garden", "general", "generation", "girl", "give",
    "glass", "goal", "good", "government", "great", "green", "ground", "group", "grow", "growth",
    "guess", "guy", "hair", "half", "hand", "handle", "hang", "happen", "happy", "hard",
    "head", "health", "hear", "heart", "heat", "heavy", "help", "high", "history", "hold",
    "home", "hope", "hospital", "hot", "hotel", "house", "however", "human", "hundred", "husband",
    "idea", "identify", "image", "imagine", "impact", "important", "improve", "include", "including", "increase",
    "indeed", "indicate", "individual", "industry", "information", "inside", "instead", "institution", "interest", "international",
    "interview", "into", "investment", "involve", "issue", "item", "itself", "join", "just", "keep",
    "kill", "kind", "kitchen", "know", "knowledge", "land", "language", "large", "last", "late",
    "later", "laugh", "law", "leader", "learn", "least", "leave", "left", "legal", "less",
    "let", "letter", "level", "life", "light", "like", "likely", "line", "list", "listen",
    "little", "live", "local", "long", "look", "lose", "loss", "love", "low", "machine",
    "magazine", "main", "maintain", "major", "majority", "make", "manage", "management", "manager", "many",
    "market", "marriage", "material", "matter", "maybe", "mean", "measure", "media", "medical", "meet",
    "meeting", "member", "memory", "mention", "message", "method", "middle", "might", "military", "million",
    "mind", "minute", "miss", "mission", "model", "modern", "moment", "money", "month", "more",
    "morning", "most", "mother", "mouth", "move", "movement", "movie", "music", "must", "name",
    "nation", "national", "nature", "near", "nearly", "necessary", "need", "network", "never", "news",
    "newspaper", "next", "nice", "night", "none", "north", "note", "nothing", "notice", "number",
    "occur", "offer", "office", "officer", "official", "often", "once", "only", "onto", "open",
    "operation", "opportunity", "option", "order", "organization", "other", "others", "outside", "over", "own",
    "owner", "page", "pain", "painting", "paper", "parent", "part", "participant", "particular", "partner",
    "party", "pass", "past", "patient", "pattern", "pay", "peace", "people", "perform", "performance",
    "period", "person", "personal", "phone", "physical", "pick", "picture", "piece", "place", "plan",
    "plant", "play", "player", "point", "police", "policy", "political", "politics", "poor", "popular",
    "population", "position", "positive", "possible", "power", "practice", "prepare", "present", "president", "pressure",
    "pretty", "prevent", "price", "private", "probably", "problem", "process", "produce", "product", "production",
    "professional", "professor", "program", "project", "property", "protect", "prove", "provide", "public", "pull",
    "purpose", "push", "quality", "question", "quick", "quite", "race", "radio", "raise", "range",
    "rate", "rather", "reach", "read", "ready", "real", "reality", "realize", "really", "reason",
    "receive", "recent", "recently", "recognize", "record", "red", "reduce", "reflect", "region", "relate",
    "relationship", "religious", "remain", "remember", "remove", "report", "represent", "republican", "require", "research",
    "resource", "respond", "response", "responsibility", "rest", "result", "return", "reveal", "rich", "right",
    "rise", "risk", "road", "rock", "role", "room", "rule", "safe", "same", "save",
    "scene", "school", "science", "scientist", "score", "sea", "season", "seat", "second", "section",
    "security", "see", "seek", "seem", "sell", "send", "senior", "sense", "series", "serve",
    "service", "set", "seven", "several", "shake", "share", "she", "shoot", "short", "should",
    "shoulder", "show", "side", "sign", "significant", "similar", "simple", "simply", "since", "sing",
    "single", "sister", "sit", "site", "situation", "six", "size", "skill", "skin", "small",
    "smile", "social", "society", "soldier", "some", "somebody", "someone", "something", "sometimes", "song",
    "soon", "sort", "sound", "source", "south", "space", "speak", "special", "specific", "speech",
    "spend", "sport", "spring", "staff", "stage", "stand", "standard", "star", "start", "state",
    "statement", "station", "stay", "step", "still", "stock", "stop", "store", "story", "street",
    "strong", "structure", "student", "study", "stuff", "style", "subject", "success", "such", "suddenly",
    "suffer", "suggest", "summer", "support", "sure", "surface", "system", "table", "take", "talk",
    "task", "tax", "teach", "teacher", "team", "technology", "television", "tell", "ten", "tend",
    "term", "test", "than", "thank", "that", "their", "them", "themselves", "then", "theory",
    "there", "these", "they", "thing", "think", "third", "this", "those", "though", "thought",
    "thousand", "threat", "three", "through", "throughout", "throw", "thus", "time", "today", "together",
    "tonight", "total", "tough", "toward", "town", "trade", "traditional", "training", "travel", "treat",
    "treatment", "tree", "trial", "trip", "trouble", "true", "truth", "try", "turn", "type",
    "under", "understand", "unit", "university", "unless", "until", "upon", "usually", "value", "various",
    "very", "victim", "view", "violence", "visit", "voice", "vote", "wait", "walk", "wall",
    "want", "war", "watch", "water", "way", "we", "weapon", "wear", "week", "weight",
    "well", "west", "whatever", "when", "where", "whether", "which", "while", "white", "whole",
    "whose", "wide", "wife", "will", "wind", "window", "wish", "with", "within", "without",
    "woman", "wonder", "word", "work", "worker", "world", "worry", "would", "write", "writer",
    "wrong", "yard", "yeah", "year", "yes", "yet", "young", "your", "yourself"
]

class TypingGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Typing Game - Words")
        self.clock = pygame.time.Clock()
        self.available_words = WORDS.copy()
        self.current_word = ""
        self.user_input = ""
        self.score = 0
        self.start_time = time.time()
        self.game_duration = 60  # 1 minute game
        self.wpm = 0
        self.accuracy = 100
        self.game_active = True
        self.game_over = False
        self.total_characters = 0
        self.correct_characters = 0
        self.wrong_characters = 0
        self.cursor_visible = True
        self.last_cursor_toggle = 0
        self.completed_words = 0  # Total words attempted
        self.correct_words = 0    # Words typed correctly
        self.wrong_words = 0      # Words typed incorrectly
        self.new_word()

    def new_word(self):
        if self.available_words:  # If there are still words available
            self.current_word = random.choice(self.available_words)
            self.available_words.remove(self.current_word)  # Remove the word from available words
            self.user_input = ""
        else:
            self.game_over = True  # End game if no more words

    def update_accuracy(self):
        total_words_attempted = self.correct_words + self.wrong_words
        if total_words_attempted > 0:
            self.accuracy = int((self.correct_words / total_words_attempted) * 100)

    def check_word_complete(self):
        if len(self.user_input) == len(self.current_word):
            self.completed_words += 1
            if self.user_input == self.current_word:
                self.score += 1
                self.correct_words += 1
            else:
                self.wrong_words += 1
            self.new_word()  # Get new word regardless of correctness
            return True
        return False

    def draw_game(self):
        self.screen.fill(BLACK)
        
        # Draw timer
        time_left = max(0, self.game_duration - (time.time() - self.start_time))
        timer_text = FONT.render(f"Time: {int(time_left)}s", True, WHITE)
        self.screen.blit(timer_text, (WINDOW_WIDTH - 150, 50))
        
        if time_left <= 0:
            self.game_over = True
        
        # Draw current word with proper letter spacing
        letter_spacing = FONT_SIZE // 4  # Reduced spacing between letters
        word_total_width = sum(FONT.size(char)[0] for char in self.current_word) + letter_spacing * (len(self.current_word) - 1)
        word_x = WINDOW_WIDTH // 2 - word_total_width // 2
        word_y = WINDOW_HEIGHT // 2 - 30
        
        x_offset = word_x
        for i, char in enumerate(self.current_word):
            color = GRAY
            if i < len(self.user_input):
                if self.user_input[i] == char:
                    color = GREEN
                else:
                    color = RED
            
            char_surface = FONT.render(char, True, color)
            self.screen.blit(char_surface, (x_offset, word_y))
            x_offset += char_surface.get_width() + letter_spacing

        # Draw input box background
        input_box_height = 50
        input_box_y = WINDOW_HEIGHT // 2 + 10
        pygame.draw.rect(self.screen, GRAY, (50, input_box_y, WINDOW_WIDTH - 100, input_box_height))
        pygame.draw.rect(self.screen, WHITE, (50, input_box_y, WINDOW_WIDTH - 100, input_box_height), 2)

        # Draw user input with proper letter spacing
        if self.user_input:
            x_offset = 60
            for i, char in enumerate(self.user_input):
                char_surface = FONT.render(char, True, WHITE)
                self.screen.blit(char_surface, (x_offset, input_box_y + 12))
                x_offset += char_surface.get_width() + letter_spacing
            
            # Draw cursor at correct position
            if self.cursor_visible:
                cursor_x = x_offset
                pygame.draw.line(self.screen, YELLOW, 
                               (cursor_x, input_box_y + 8),
                               (cursor_x, input_box_y + input_box_height - 8), 3)
        else:
            # Draw placeholder text
            placeholder = FONT.render("Type here...", True, (200, 200, 200))
            self.screen.blit(placeholder, (60, input_box_y + 12))
            
            # Draw cursor at start
            if self.cursor_visible:
                pygame.draw.line(self.screen, YELLOW, 
                               (60, input_box_y + 8),
                               (60, input_box_y + input_box_height - 8), 3)

        # Draw stats
        score_text = FONT.render(f"Score: {self.score}", True, WHITE)
        wpm_text = FONT.render(f"WPM: {self.wpm}", True, WHITE)
        accuracy_text = FONT.render(f"Accuracy: {self.accuracy}%", True, WHITE)
        completed_text = FONT.render(f"Correct Words: {self.completed_words}", True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(wpm_text, (10, 50))
        self.screen.blit(accuracy_text, (10, 90))
        self.screen.blit(completed_text, (10, 130))

        # Draw instructions
        instructions = FONT.render("Type the word shown above, Escape to quit", True, WHITE)
        self.screen.blit(instructions, (WINDOW_WIDTH // 2 - instructions.get_width() // 2, WINDOW_HEIGHT - 50))

        pygame.display.flip()

    def draw_results(self):
        self.screen.fill(BLACK)
        
        # Calculate final statistics
        elapsed_minutes = 1  # Since game duration is 60 seconds
        total_words = self.correct_words + self.wrong_words
        final_wpm = int(total_words / elapsed_minutes)  # Words per minute based on total words typed
        final_accuracy = int((self.correct_words / max(1, total_words)) * 100)  # Accuracy based on correct words
        
        # Draw results
        title = FONT.render("Game Over! Final Results", True, WHITE)
        correct_text = FONT.render(f"Correct Words: {self.correct_words}", True, GREEN)
        wrong_text = FONT.render(f"Wrong Words: {self.wrong_words}", True, RED)
        wpm_text = FONT.render(f"Final WPM: {final_wpm}", True, WHITE)
        accuracy_text = FONT.render(f"Accuracy: {final_accuracy}%", True, WHITE)
        restart_text = FONT.render("Press SPACE to play again or ESC to quit", True, WHITE)
        
        # Position all text elements
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        correct_rect = correct_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
        wrong_rect = wrong_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        wpm_rect = wpm_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
        accuracy_rect = accuracy_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 120))
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT * 3 // 4))
        
        # Draw all text elements
        self.screen.blit(title, title_rect)
        self.screen.blit(correct_text, correct_rect)
        self.screen.blit(wrong_text, wrong_rect)
        self.screen.blit(wpm_text, wpm_rect)
        self.screen.blit(accuracy_text, accuracy_rect)
        self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()

    def reset_game(self):
        self.available_words = WORDS.copy()
        self.current_word = ""
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
        self.cursor_visible = True
        self.last_cursor_toggle = 0
        self.completed_words = 0
        self.correct_words = 0
        self.wrong_words = 0
        self.new_word()

    def run(self):
        while self.game_active:
            current_time = time.time()
            
            # Update cursor blink
            if current_time - self.last_cursor_toggle >= 0.5:
                self.cursor_visible = not self.cursor_visible
                self.last_cursor_toggle = current_time
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_active = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_active = False
                    elif event.key == pygame.K_SPACE:
                        if self.game_over:
                            self.reset_game()
                        else:
                            # Check if the current word matches before moving to next
                            if self.user_input == self.current_word:
                                self.score += 1
                                self.correct_words += 1
                                self.completed_words += 1
                            else:
                                self.wrong_words += 1
                            self.new_word()  # Get new word when space is pressed
                    elif not self.game_over:
                        if event.key == pygame.K_BACKSPACE:
                            if self.user_input:  # Only remove if there's input
                                self.user_input = self.user_input[:-1]
                        else:
                            if event.unicode.isprintable() and event.unicode != ' ':  # Ignore space as input
                                self.user_input += event.unicode
                                self.total_characters += 1
                                # Check if the typed character is correct
                                if len(self.user_input) <= len(self.current_word):
                                    current_char = self.user_input[-1]
                                    target_char = self.current_word[len(self.user_input)-1]
                                    if current_char == target_char:
                                        self.correct_characters += 1
                                    else:
                                        self.wrong_characters += 1
                                    self.update_accuracy()

            if not self.game_over:
                # Calculate WPM
                elapsed_time = time.time() - self.start_time
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
