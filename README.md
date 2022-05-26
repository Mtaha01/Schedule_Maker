# Schedule_Maker

COURSE TIMETABLE SCHEDULER
with Genetic Algorithm
May, 2022
Prepared By
1-Mostafa Ahmed
2-Mohamed Taha
3-Eslam Zanaty
4-Mollar Magdy

INTRODUCTION
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






METHODOLOGY
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
7. Ending the algorithm when the best solution obtained has not changed 
after a preset number of generations




 ADVANTAGES OF GENETIC ALGORITHM
As compared to genetic algorithms, other optimization algorithms look for 
solutions in a serial manner (in one direction) in the search field at a given time. 
The disadvantage of a serial search is that if the solution obtained is not 
favorable, the work carried out thus far has to be abandoned and a new search 
must be started. Genetic algorithms, which have multiple offspring on the other 
hand, are able to look for solutions in many directions at a given time, 
abandoning the paths which lead to suboptimal solutions. Thus, the opportunity
of finding a favorable solution in a genetic algorithm is high during each run.



HOW THE ALGORITHM CAN SOLVE THE SCHEDULE PROBLEM.
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
 





EXPERIMENTAL SIMULATION
Programing language: Python 
IDE: Visual Studio
Data needed: 
 Days available for the faculty
 Meeting hours available
 Halls or Rooms available for the classes and the capacity of it 
 Instructors that will teach the courses
 The courses data with instructor data and number of students
 The departments and the courses that it belongs to 
Note: if we have a course included in more than one department then we 
will create a virtual department to include this course
We are using OOP in python to organize the code as much as we can
Implementation of the Classes
1. Class for the days
It defines the available days for the faculty or university
2. Class for the Meeting Times
It defines the available Meeting hours for the faculty
3. Class for the Instructors
It defines the instructors data (name and id )
4. Class for the Halls and Rooms
It Defines the Capacity of it and the name of it
5. Class for the Course
It defines the course class with data for it
6. Class for the Classes
to include the data of the course, its time, hall, instructor, and department

7. Class for the Schedule
It generates the chromosomes, calculates its fitness function for each 
chromosome by using the number of conflicts
 Fitness function = 1/(1*number of conflicts+1)
 Number of conflicts is increased when:
 When two classes have the same meeting time, the same day, 
the same department, same grade, and they are not both a lab 
 When two classes have the same meeting time, the same day, 
and the same instructor
 When two classes have the same meeting time, the same day,
and the same Hall or Room
 When the capacity of the hall or the room is less than the max 
number of students for this class


8. Class for the Population
Define the population that includes the schedules(chromosomes) 
9. Class For the data we want to schedule:
 We create a list for each element in the class table 
 The lists consists of :all the halls and labs in faculty , all the days of 
weak that faculty works and all times in the day, all INSTRUCTORS in 
the faculty, all courses and all department related to the courses


10. Class for the Genetic Algorithm
 The evolve function perform the algorithm
 The crossover_Population function performs:
 Select elite schedules
 Selecting the two schedules by using the 
select_tournament_population (using random selection)
 selection of the chromosomes (schedules) to cross over 
between them in the crossover_schedule function (uniform 
crossover) 
 The mutate_population looping on the schedules and call the mutate_sechule 
function for it that perform the mutation between the classes inside the 
schedule 
11. Class for the display manager 
It is used to help displaying the tables of the schedules using library pretty 
Table
 



RESULTS AND TECHNICAL DISCUSSION
The hard constraints were tested to ensure that all the solutions obtained were
valid. The optimized solution for the timetable consisted of the following factors 
and their values. The population size was 15 with a mutation rate of 0.1, the 
number of elite individuals was 1 and the tournament size was 6. With these
values the resulting timetable had zero number of conflicts with the fitness value
of 1.


The output:
Print by two methods (Console, File)
For ex: Data:
 Frist we print all generation untill reach to the goal.
 In this test we reach to the goal after 80 generation.
 We take the best solution(the Schedule that has fitness (1)) and print 
it.
 We split it by grade and sort it by week days.




CONCLUSION
The course scheduler using genetic algorithms finds the best solution that satisfies 
a number of hard constraints. Also, the mutation technique used guarantees that
the mutated chromosomes remain valid. This was done by creating a known valid 
random individual, swapping genes with it similar to uniform crossover. Use of 
uniform crossover and tournament selection completed the algorithm. Also, the 
effect of mutation rate and the population size were studied for the course 
scheduler.




REFERENCES
https://link.springer.com/article/10.1007/s11042-020-10139-6
https://towardsdatascience.com/using-genetic-algorithms-to-scheduletimetables-27f132c9e280
https://andreweast.net/wp-content/uploads/2019/06/Timetable-Scheduling-viaGenetic-Algorithm-Andrew-Reid-East.pdf
https://en.wikipedia.org/wiki/Genetic_algorithm
https://prototypeprj.blogspot.com/2020/07/class-scheduling-w-geneticalgorithms.html

