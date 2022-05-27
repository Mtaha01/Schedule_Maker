# Timetabling-Schedule-System

Genetic Algorithm For University Course Timetabling Problem 💻⌚🏫



## INTRODUCTION and why we made this project

In the university, college students must be register for their classes, creating 
timetables for institutes which deal with sections and lectures scheduling is a 
complex problem. It is difficult and time consuming to solve due to many 
constraints. A feasible course timetable could be described as a plan for the 
movement of students and staff from one classroom to another, without
conflicts. Being an NP-complete problem, many attempts have been made using 
varying computational methods to obtain optimal solutions to the timetabling 
problem. Genetic algorithms, based on Darwin's theory of evolution is one such 
method. The aim of this study is to optimize a general university course 
scheduling process based on genetic algorithms using some defined constraints.
AIM OF THE PROJECT
The aim of this work is to demonstrate the usefulness of genetic algorithm usage 
to obtain optimal solutions in general timetable scheduling. Although much 
commercial scheduling software is available, its lack of generality rarely meets the 
demands of various institutions.
Therefore, the requirement of specific coding as per respective universities is the 
biggest hurdle to overcome.


## Abstraction:
The course scheduler using genetic algorithms finds the best solution that satisfies 
a number of hard constraints. Also, the mutation technique used guarantees that
the mutated chromosomes remain valid. This was done by creating a known valid 
random individual, swapping genes with it similar to uniform crossover. Use of 
uniform crossover and tournament selection completed the algorithm. Also, the 
effect of mutation rate and the population size were studied for the course 
scheduler.


## METHODOLOGY 
Genetic algorithms are heuristic methods used to solve computational problems
which require large search areas for possible solutions. They very often depend 
on adaptive systems to perform well in changing environments. 
A genetic algorithm (GA) is a powerful problem-solving programming technique. It
is in a category of evolutionary algorithms which is a subset of evolutionary 
computation in artificial intelligence. It was developed in 1960 by Professor John 
Holland of the University of Michigan. His book, Adaptation in Natural and 
Artificial Systems pioneered genetic algorithm (GA) research in the 1970s. This 
technique was inspired by the Darwinian theory of natural evolution. In this 
technique the fittest will survive. The fittest are those with favorable variations, 
the accumulation of which lead to the evolution of species. The chances for the
survival of organisms with injurious variations are rather slim. Thus, evolution is a 
process of natural selection
HOW GENETIC ALGORITHMS WORK
In a genetic algorithm, a population of chromosomes consisting of a given random
collection of genes is initiated according to the following steps.
1. Generating an initial population of chromosomes.
2. Evaluating the suitability of each chromosome (individual) that forms the 
population.
3. Selecting the chromosomes for mating based on the above results.
4. Producing offspring by mating (cross over) the selected chromosomes.
5. Mutating genes randomly.
6. Repeating steps 3-5 until a new population is generated.
7. Ending the algorithm when the best solution obtained has not changed  after a preset number of generations


## HOW THE ALGORITHM CAN SOLVE THE SCHEDULE PROBLEM :
1. Generate the initial population (The Schedules) with size of 15
2. Calculate the fitness function for each schedule 
(Fitness Function = 1 / (1* Number of conflicts + 1))
3. Selecting the Schedules for mating by selecting randomly number of 
Schedules that equals to the tournament selection size and return the 
schedule that has the maximum fitness function or less conflicts.
4. Producing offspring by mating (uniform crossover) the selected Schedules 
5. Mutating the classes in the schedules (genes) randomly with mutation rate 
0.1
6. Repeating steps 3-5 until a new Schedules (Population) is generated.
7. Ending the algorithm when the best solution obtained (Schedule that has 
no conflicts)
 The Time Complexity of the Algorithm is:𝑶(𝑵 ∗ (𝑻 ∗ 𝑷𝟐∗ 𝑪𝟑))
N: Number of Generations
T: Tournament selection size
P: Size of population 
C: Number of Classes
 


## RESULTS AND TECHNICAL DISCUSSION :
The hard constraints were tested to ensure that all the solutions obtained were
valid. The optimized solution for the timetable consisted of the following factors 
and their values. The population size was 15 with a mutation rate of 0.1, the 
number of elite individuals was 1 and the tournament size was 6. With these
values the resulting timetable had zero number of conflicts with the fitness value
of 1.


## The output:
**Print by two methods (Console, File)**
For ex: Data:
- Frist we print all generation untill reach to the goal.
- In this test we reach to the goal after 80 generation.
- We take the best solution(the Schedule that has fitness (1)) and print 
it.
- We split it by grade and sort it by week days.



## Prepared By
- Mostafa Ahmed
- Mohamed Taha
- Eslam Zanaty
- Mollar Magdy







## REFERENCES : 
- https://link.springer.com/article/10.1007/s11042-020-10139-6
- https://towardsdatascience.com/using-genetic-algorithms-to-schedule-timetables-27f132c9e280
- https://andreweast.net/wp-content/uploads/2019/06/Timetable-Scheduling-via-Genetic-Algorithm-Andrew-Reid-East.pdf
- https://en.wikipedia.org/wiki/Genetic_algorithm
- https://prototypeprj.blogspot.com/2020/07/class-scheduling-w-genetic-algorithms.html

