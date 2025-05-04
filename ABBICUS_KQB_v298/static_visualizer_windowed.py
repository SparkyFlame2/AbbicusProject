
import pygame
import threading
import random
import time
import quantum_processor_sim as qps

# Window dimensions (bar-style)
WIDTH, HEIGHT = 1280, 180
TITLE_IMAGE_PATH = "./Media/Images/ABBICUS Title Image.png"
JUMP_IMAGE_PATH = "./Media/Images/Jump Screen.png"
FPS = 30

show_jump = False
jump_flash_duration = 1.5
jump_flash_timer = 0

def get_gamma_mean():
    gamma_values = []
    for q in qps.quantum_register:
        if q.collapsed_value is not None:
            gamma_values.append(float(q.collapsed_value))
        else:
            gamma_values.append(abs(q.alpha.real))
    return sum(gamma_values) / len(gamma_values)

def draw_particles(surface, gamma):
    num_particles = int(gamma * 200)
    for _ in range(num_particles):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(1, 3)
        hue_shift = int(255 * gamma)
        color = (hue_shift % 255, 255 - hue_shift % 255, 200)
        pygame.draw.circle(surface, color, (x, y), radius)

def load_and_scale_image(image_path):
    try:
        img = pygame.image.load(image_path).convert_alpha()
        img = scale_image_aspect(img, WIDTH, HEIGHT)
        return img
    except Exception as e:
        print(f"[VISUALIZER] Error loading image {image_path}: {e}")
        return None

def scale_image_aspect(image, max_w, max_h):
    img_w, img_h = image.get_size()
    ratio = min(max_w / img_w, max_h / img_h)
    new_size = (int(img_w * ratio), int(img_h * ratio))
    scaled = pygame.transform.smoothscale(image, new_size)
    return scaled

def trigger_jump_flash():
    global show_jump, jump_flash_timer
    show_jump = True
    jump_flash_timer = time.time()

def launch_visualizer():
    def visualizer_thread():
        global show_jump
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ABBICUS Visualizer")
        clock = pygame.time.Clock()

        title_img = load_and_scale_image(TITLE_IMAGE_PATH)
        jump_img = load_and_scale_image(JUMP_IMAGE_PATH)
        title_display_time = 3
        title_start = time.time()

        running = True
        while running:
            screen.fill((0, 0, 0))
            now = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if now - title_start < title_display_time and title_img:
                rect = title_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(title_img, rect)
            elif show_jump and jump_img:
                rect = jump_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(jump_img, rect)
                if time.time() - jump_flash_timer > jump_flash_duration:
                    show_jump = False
            else:
                gamma = get_gamma_mean()
                draw_particles(screen, gamma)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    threading.Thread(target=visualizer_thread, daemon=True).start()
