
import threading
import time
import os

class QGPU:
    def __init__(self, update_interval=5):
        self.interval = update_interval
        self.running = False
        self.thread = None

    def start_visualizer(self, register):
        if self.running:
            print("[QGPU] Visualizer already running.")
            return
        self.running = True
        self.thread = threading.Thread(target=self._visualizer_loop, args=(register,), daemon=True)
        self.thread.start()
        print("[QGPU] Visualizer started.")

    def stop_visualizer(self):
        self.running = False
        print("[QGPU] Visualizer stopped.")

    def _visualizer_loop(self, register):
        while self.running:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[QGPU STATE VISUALIZER v0.1]")
            print("=" * 40)
            print(f"{'#':<3} {'α':<15} {'β':<15} {'COLLAPSED'}")
            print("-" * 40)
            for i, q in enumerate(register):
                alpha = f"{q.alpha.real:.3f}+{q.alpha.imag:.3f}j"
                beta = f"{q.beta.real:.3f}+{q.beta.imag:.3f}j"
                status = "✅" if q.collapsed_value else "❌"
                print(f"{i:<3} {alpha:<15} {beta:<15} {status}")
            print("=" * 40)
            print(f"[Updating in {self.interval} seconds...]")
            time.sleep(self.interval)
