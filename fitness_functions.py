# fitness_module.py

import numpy as np
import control as ctrl

# Definiowanie funkcji transferowej G(s)
def create_system():
    num = [1]  # Licznik
    den = [1, 2, 1]  # Mianownik
    system = ctrl.TransferFunction(num, den)
    return system

def pid_controller(Kp, Ki, Kd):
    # Regulator PID w domenie Laplace'a
    pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
    return pid

def closed_loop_response(system, pid):
    closed_loop = ctrl.feedback(pid * system, 1)  # Połączenie sprzężenia zwrotnego
    t, y = ctrl.step_response(closed_loop)  # Odpowiedź skokowa
    return t, y
# Funckja fitness - całkowity błąd kwadratowy (ISE)
def fitness_ISE(Kp, Ki, Kd, system):
    pid = pid_controller(Kp, Ki, Kd)
    t, y = closed_loop_response(system, pid)
    e = 1 - y  # Uchyb (zakładamy, że sygnał referencyjny to 1)
    ise = np.sum(e**2) * (t[1] - t[0])  # Aproksymacja całki
    return ise
