import numpy as np
import control as ctrl

# Przykładowe parametry dla VELEX OFF-ROAD X2
# https://velex.pl/produkt/velex-off-road-x2/
m1 = 50.0  # masa wózka [kg]
m2 = 4.0  # masa pręta [kg]
l = 0.6  # długość pręta [m]
g = 9.81  # przyspieszenie ziemskie [m/s^2]
b = 0.2  # współczynnik tłumienia [kg/s] (przybliżona wartość)


# Definiowanie funkcji transferowej G(s)
def create_system():
    # Licznik i mianownik funkcji transferowej (przybliżenie liniowe)
    num = [m2 * l]
    den = [(m1 + m2) * l ** 2, b * (m1 + m2), m2 * g * l]
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
    ise = np.sum(e ** 2) * (t[1] - t[0])  # Aproksymacja całki
    return ise


# Funckja fitness - całkowity błąd z wartości bezwzględnej uchybu (IAE) - mniej wrażliwe na duże błędy, ponieważ nie stosuje się tutaj podnoszenia błędu do kwadratu
def fitness_IAE(Kp, Ki, Kd, system):
    pid = pid_controller(Kp, Ki, Kd)
    t, y = closed_loop_response(system, pid)
    e = 1 - y  # Uchyb
    iae = np.sum(np.abs(e)) * (t[1] - t[0])  # Aproksymacja całki
    return iae


# Funckja fitness - całkowity błąd z wartości bezwzględnej uchybu (ITAE) uwzględniający wagę czasu - lepsze dla rozwiązań, gdzie system ma być stabilny przez dłuższy okres czasu
def fitness_ITAE(Kp, Ki, Kd, system):
    pid = pid_controller(Kp, Ki, Kd)
    t, y = closed_loop_response(system, pid)
    e = 1 - y  # Uchyb
    itae = np.sum(t * np.abs(e)) * (t[1] - t[0])  # Aproksymacja całki
    return itae


# Funckja fitness - średni błąd kwadratowy (MSE) - porównanie regulacji w zależności od średniej dokładniości
def fitness_MSE(Kp, Ki, Kd, system):
    pid = pid_controller(Kp, Ki, Kd)
    t, y = closed_loop_response(system, pid)
    e = 1 - y  # Uchyb
    mse = np.mean(e ** 2)  # Średnia kwadratów błędów
    return mse


# Połączenie ITAE z czasem ustalania - dobre dla układów, które muszą osiągać szybko stan ustalony bez oscylacji
def fitness_ITAE_settling(Kp, Ki, Kd, system):
    pid = pid_controller(Kp, Ki, Kd)
    t, y = closed_loop_response(system, pid)
    e = 1 - y  # Uchyb
    itae = np.sum(t * np.abs(e)) * (t[1] - t[0])  # Aproksymacja całki ITAE

    # Wyznaczanie czasu ustalania (czas, w którym odpowiedź przekroczy 2% od stanu ustalonego)
    settle_time = t[np.where(np.abs(y - 1) < 0.02)[0][-1]]

    # Funkcja fitness łącząca ITAE i czas ustalania
    fitness_value = itae + 0.1 * settle_time  # Współczynnik wagowy
    return fitness_value


# Podejście łączone, które bierze pod uwagę IAE, czas ustalania oraz przeregulowanie systemu z uwzględnieniem wag dla każdego członu
def fitness_multi_objective(Kp, Ki, Kd, system, w1=1.0, w2=0.1, w3=0.1):
    pid = pid_controller(Kp, Ki, Kd)
    t, y = closed_loop_response(system, pid)
    e = 1 - y  # Uchyb

    iae = np.sum(np.abs(e)) * (t[1] - t[0])  # IAE
    settle_time = t[np.where(np.abs(y - 1) < 0.02)[0][-1]]  # Czas ustalania
    overshoot = np.max(y) - 1.0  # Przeregulowanie
    overshoot = max(0, overshoot)

    # Łączenie funkcji fitness z wagami
    fitness_value = w1 * iae + w2 * settle_time + w3 * overshoot
    return fitness_value
