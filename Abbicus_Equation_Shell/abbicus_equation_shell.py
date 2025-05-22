import time
import random
from equation_module import calculate_drift
from prediction_module import predict_next_state
from state_log import log_state, read_log

print(">> ABBICUS EQUATION SHELL v1.0")
print("Type 'track [value]', 'predict', or 'log' to proceed. Type 'exit' to quit.")

current_state = None

while True:
    user_input = input("@abbicus(eq)> ").strip().lower()

    if user_input.startswith("track"):
        try:
            _, val = user_input.split()
            val = float(val)
            drift = calculate_drift(val)
            current_state = {"input": val, "drift": drift}
            log_state(current_state)
            print(f"[DRIFT] => {drift:.4f}")
        except ValueError:
            print("Invalid format. Use: track [number]")

    elif user_input == "predict":
        prediction = predict_next_state()
        print(f"[PREDICTED NEXT INPUT] => {prediction:.4f}")

    elif user_input == "log":
        for entry in read_log():
            print(entry.strip())

    elif user_input == "exit":
        print("Goodbye.")
        break

    else:
        print("Unknown command.")
