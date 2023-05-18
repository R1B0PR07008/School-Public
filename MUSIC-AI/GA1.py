import pygad
import numpy

print(pygad.__version__)

inputs = [0.4,1,0,7,8,1,2,3,4,5,6,7,8,9,0,12,23,34,45,5667,67,78,95678,456,23,234,456,9,0,9,54,213,]
desired_output = 32

def fitness_func(ga_instance, solution, solution_idx):
    output = numpy.sum(solution*inputs)
    fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001)

    return fitness

ga_instance = pygad.GA(num_generations=1000,
                       sol_per_pop=10,
                       num_genes=len(inputs),
                       num_parents_mating=2,
                       fitness_func=fitness_func,
                       mutation_type="random",
                       mutation_probability=0.6,
                       save_best_solutions=True)

ga_instance.run()

ga_instance.plot_fitness()

print(ga_instance.best_solution())
print("########################################################")

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

