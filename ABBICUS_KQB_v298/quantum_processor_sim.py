
import random
import math


class Qubital:
    def __init__(self, id, alpha=0.7071, beta=0.7071):
        self.id = id
        self.alpha = complex(alpha)
        self.beta = complex(beta)
        self.entangled_with = None
        self.collapsed_value = None

    def collapse(self):
        if self.collapsed_value is not None:
            return self.collapsed_value
        prob_zero = abs(self.alpha) ** 2
        result = 0 if random.random() < prob_zero else 1
        self.collapsed_value = result

        self.alpha = 1.0 if result == 0 else 0.0
        self.beta = 0.0 if result == 0 else 1.0
   
    def reset(self):
        self.collapsed_value = None

    def entangle(self, other):
        self.entangled_with = other.id
        other.entangled_with = self.id

    def gamma_shift(self, gamma_factor):
        # Modify alpha and beta based on gamma tuning (used as drift distortion)
        total = self.alpha + self.beta
        self.alpha **= gamma_factor
        self.beta **= (2 - gamma_factor)
        self.normalize()

    def normalize(self):
        norm = math.sqrt(abs(self.alpha)**2 + abs(self.beta)**2)
        if norm != 0:
            self.alpha /= norm
            self.beta /= norm

    def get_state(self):
        if self.collapsed_value is not None:
            return f"[cubital_{self.id}] => |{self.collapsed_value}⟩ (collapsed)"
        else:
            return f"[cubital_{self.id}] => superposition(|0⟩={self.alpha:.4f}, |1⟩={self.beta:.4f})"

# Initialize 100 Qubitals
quantum_register = [Qubital(i) for i in range(100)]

# Define QuantumCore class that works with your advanced Qubital objects
class QuantumCore:
    def __init__(self, core_id, qubits):
        self.core_id = core_id
        self.register = qubits

    def collapse_all(self):
        for q in self.register:
            q.collapse()

    def reset_all(self):
        for q in self.register:
            q.reset()

    def gamma_tune(self, factor):
        for q in self.register:
            q.gamma_shift(factor)

    def get_states(self):
        return [q.get_state() for q in self.register]

# Partition the global quantum register into 4 logical cores
core0 = QuantumCore(0, quantum_register[0:25])
core1 = QuantumCore(1, quantum_register[25:50])
core2 = QuantumCore(2, quantum_register[50:75])
core3 = QuantumCore(3, quantum_register[75:100])

quantum_cores = {
    0: core0,
    1: core1,
    2: core2,
    3: core3
}

def collapse_core(core_id):
    if core_id in quantum_cores:
        quantum_cores[core_id].collapse_all()
        return f"Core {core_id} collapsed."
    return "Invalid core ID."

def reset_core(core_id):
    if core_id in quantum_cores:
        quantum_cores[core_id].reset_all()
        return f"Core {core_id} reset."
    return "Invalid core ID."

def gamma_tune_core(core_id, factor):
    if core_id in quantum_cores:
        quantum_cores[core_id].gamma_tune(factor)
        return f"Core {core_id} gamma tuned by {factor}."
    return "Invalid core ID."

def get_core_states(core_id):
    if core_id in quantum_cores:
        return quantum_cores[core_id].get_states()
    return []

def get_all_core_states():
    return {
        core_id: get_core_states(core_id)
        for core_id in quantum_cores
    }

def get_register():
    return quantum_register

def collapse(self):
        probability_zero = abs(self.alpha)**2
        result = 0 if random.random() < prob_zero else 1
        self.collapsed_value = result
        return result

def collapse_all():
    for q in quantum_register:
        q.collapse()

def reset_all():
    for q in quantum_register:
        q.reset()

def enact_wave_function():
    for q in quantum_register:
        if q.collapsed_value is not None:
            q.reset()

def gamma_tune_all(factor):
    for q in quantum_register:
        q.gamma_shift(random.uniform(0.2, 1.8))
    for q in quantum_register:
        q.gamma_shift(factor)

def get_drift_matrix():
    matrix = []
    for q in quantum_register:
        val = (q.alpha ** 2) - (q.beta ** 2)
        matrix.append(val)
    return matrix

def show_all_states():
        states = []
        for q in quantum_register:
            if q.collapsed_value is not None:
                states.append(f"[Qubital_{q.id}] => |{q.collapsed_value}⟩ (collapsed)")
            else:
                alpha = q.alpha
                beta = q.beta
                states.append(
                    f"[Qubital_{q.id}] => superposition("
                    f"|0⟩={alpha.real:.4f}+{alpha.imag:.4f}j, "
                    f"|1⟩={beta.real:.4f}+{beta.imag:.4f}j)"
                )
        return states

