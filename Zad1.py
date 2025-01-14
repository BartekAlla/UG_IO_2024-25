from simpful import *

FS = FuzzySystem()

food_lv = LinguisticVariable([
    FuzzySet(function=Triangular_MF(a=0, b=0, c=5), term="poor"),
    FuzzySet(function=Triangular_MF(a=0, b=5, c=10), term="average"),
    FuzzySet(function=Triangular_MF(a=5, b=10, c=10), term="good")
], concept="Food", universe_of_discourse=[0, 10])
FS.add_linguistic_variable("Food", food_lv)
food_lv.plot()

service_lv = LinguisticVariable([
    FuzzySet(function=Triangular_MF(a=0, b=0, c=5), term="poor"),
    FuzzySet(function=Triangular_MF(a=0, b=5, c=10), term="average"),
    FuzzySet(function=Triangular_MF(a=5, b=10, c=10), term="good")
], concept="Service", universe_of_discourse=[0, 10])
FS.add_linguistic_variable("Service", service_lv)
service_lv.plot()

tip_lv = LinguisticVariable([
    FuzzySet(function=Triangular_MF(a=0, b=0, c=10), term="low"),
    FuzzySet(function=Triangular_MF(a=5, b=15, c=25), term="medium"),
    FuzzySet(function=Triangular_MF(a=20, b=30, c=30), term="high")
], concept="Tip", universe_of_discourse=[0, 30])
FS.add_linguistic_variable("Tip", tip_lv)
tip_lv.plot()

rule1 = "IF (Food IS poor) OR (Service IS poor) THEN (Tip IS low)"
rule2 = "IF (Food IS average) THEN (Tip IS medium)"
rule3 = "IF (Food IS good) AND (Service IS good) THEN (Tip IS high)"
FS.add_rules([rule1, rule2, rule3])

inputs = [
    {"Food": 3, "Service": 4},
    {"Food": 7, "Service": 8},
    {"Food": 5, "Service": 5},
    {"Food": 9, "Service": 10},
]

for i, input_data in enumerate(inputs):
    FS.set_variable("Food", input_data["Food"])
    FS.set_variable("Service", input_data["Service"])
    tip = FS.inference()["Tip"]
    print(f"Test {i + 1}: Input: {input_data}, Suggested Tip: {tip:.2f}%")
