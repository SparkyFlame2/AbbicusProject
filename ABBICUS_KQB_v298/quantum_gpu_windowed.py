
import pygame
import threading
import time
import sys

class QGPUWindowed:
    def __init__(self, width=1200, height=600, interval=10):
        self.width = width
        self.height = height
        self.interval = interval
        self.running = False
        self.thread = None

    def start_visualizer(self, register):
        if self.running:
            print("[QGPU-W] Visualizer already running.")
            return
        self.running = True
        self.thread = threading.Thread(target=self._visualizer_loop, args=(register,), daemon=True)
        self.thread.start()
        print("[QGPU-W] Visualizer window started.")

    def stop_visualizer(self):
        self.running = False
        print("[QGPU-W] Visualizer window stopped.")

    def _visualizer_loop(self, register):
        pygame.init()
        font = pygame.font.SysFont("Consolas", 16)
        screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("QGPU Visualizer v0.4")

        while self.running:
            screen.fill((0, 0, 0))
            column_width = self.width // 3
            max_rows = (self.height - 40) // 20
            num_columns = max(1, (len(register) + max_rows - 1) // max_rows)
            columns = [[] for _ in range(num_columns)]

            for i, q in enumerate(register[:100]):
                a = q.alpha
                b = q.beta
                a_val = abs(a)
                b_val = abs(b)
                collapsed = q.collapsed_value

                # Choose color based on dominance
                if abs(a_val - b_val) < 0.05:
                    alpha_color = beta_color = (170, 170, 170)  # gray
                elif a_val > b_val:
                    alpha_color = (0, 255, 170)  # teal-green
                    beta_color = (255, 85, 119)  # salmon
                else:
                    alpha_color = (255, 85, 119)
                    beta_color = (0, 255, 170)

                collapsed_color = (0, 255, 0) if collapsed else (255, 68, 68)
                alpha = f"{a.real:.3f}+{a.imag:.3f}j"
                beta = f"{b.real:.3f}+{b.imag:.3f}j"
                col_index = i // max_rows
                columns[col_index].append({
                    "index": i,
                    "alpha": alpha,
                    "beta": beta,
                    "collapsed": "✅" if collapsed else "❌",
                    "alpha_color": alpha_color,
                    "beta_color": beta_color,
                    "collapsed_color": collapsed_color
                })

            for col_idx, column in enumerate(columns):
                x_offset = col_idx * column_width + 10
                y_offset = 10
                header = font.render("#   Alpha                Beta                 Collapsed", True, (200, 200, 200))
                screen.blit(header, (x_offset, y_offset))
                y_offset += 20
                for q in column:
                    index_txt = font.render(f"{q['index']:<3}", True, (255, 255, 255))
                    alpha_txt = font.render(q["alpha"], True, q["alpha_color"])
                    beta_txt = font.render(q["beta"], True, q["beta_color"])
                    collapsed_txt = font.render(q["collapsed"], True, q["collapsed_color"])

                    screen.blit(index_txt, (x_offset, y_offset))
                    screen.blit(alpha_txt, (x_offset + 40, y_offset))
                    screen.blit(beta_txt, (x_offset + 190, y_offset))
                    screen.blit(collapsed_txt, (x_offset + 370, y_offset))
                    y_offset += 20

            pygame.display.flip()

            start_time = time.time()
            while self.running and time.time() - start_time < self.interval:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.VIDEORESIZE:
                        self.width, self.height = event.size
                        screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                time.sleep(0.1)

        pygame.quit()
