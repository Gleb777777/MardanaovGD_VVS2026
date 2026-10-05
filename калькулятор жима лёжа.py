class BenchPressCalculator:
    def __init__ (self, weight, reps):
        self.weight = weight
        self.reps = reps
    def calculete_1repmax (self):
        one_repmax = self.weight * (1 + self.reps / 30)
        return one_repmax

weight = float(input("Введите вес штанги: "))
reps = float(input("Введите количество повторений: "))
bench = BenchPressCalculator (weight, reps)
result = bench.calculete_1repmax()
print ("Твой примерный жим на раз: ", round (result, 1), "кг") 


