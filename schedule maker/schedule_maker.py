import prettytable as prettytable
import random as rnd
import numpy as np
import sys

POPULATION_SIZE = 15
NUMB_OF_ELITE_SCHEDULES = 1
# Number of Selected Schedules evey Generation
TOURNAMENT_SELECTION_SIZE = 6
MUTATION_RATE = 0.1
# class to define the day of the class
class Day:
    def __init__(self, day):
        self._day = day

    def get_day(self): return self._day
# Data used to be scheduled
class Data:
    ROOMS = [["R1", 120], ["R2", 120], ["R3", 120], ["R4", 120], ["R5", 120], ["R6", 120], ["R7", 120], ["R8", 120],
             ["R9", 120], ["A1", 40],
             ["A2", 40], ["A3", 40], ["A4", 40], ["B1", 40],
             ["B2", 40], ["B3", 40], ["B4", 40], ["C1", 40], ["C2", 40], ["C3", 40],
             ["C4", 40]]  # Lecture Halls ,labs and capcity for it
    DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    MEETING_TIMES = ["8-10", "10-12", "12-2", "2-4",
                     "4-6"]  # assuming that all durations will be 2hours Starting from 8 to 2
    INSTRUCTORS = [["G1", "Dr/Fathy Hesham"],
                   ["G2", "Eng/Nemat"],
                   ["CS1", "Dr/Mamdouh Farouk"],
                   ["G3", "Dr/Mohamed Soliman"],
                   ["G4", "Dr/Hesham Elatar"],
                   ["Ins1", "Eng/Nourhan"],
                   ["G5", "Dr/Mohamed Reffat"],  # 6
                   ["G6", "Dr/Osama Rashed"],
                   ["G7", "Eng/Omaima"],
                   ["IS1", "Dr/Ebrahim Elawdy"],
                   ["IS2", "Eng/Fooly"],
                   ["CS2", "Dr/Mostafa Mekky"],
                   ["CS3", "Eng/Abdelrahman Nashaat"],  # 12
                   ["CS4", "Dr/Marghny Hassan"],
                   ["CS5", "Eng/Ebrahim Saad"],
                   ["CS6", "Dr/Khaled Fathy"],
                   ["CS7", "Eng/Sohair"],
                   ["CS8", "Eng/Asaad NasrAllah"],
                   ["CS9", "Eng/Mahmud Essam"],
                   ["CS10", "Dr/Mohamed Mostafa Darweesh"],
                   ["CS11", "Eng/Amal"],
                   ["CS12", "Dr/Mostafa Abo Baker"],  # 21
                   ["IT1", "Eng/Alaa Adel"],
                   ["CS13", "Dr/Mostafa Kamel"],
                   ["CS14", "Eng/Ahmed Hosny"],
                   ["IS3", "Eng/Gehad"],
                   ["IT2", "Dr/Ali Hussien"],
                   ["IT3", "Eng/Salma Osama"],
                   ["Cs15", "Dr/Abdelrahman Hedar"],
                   ["Cs16", "Eng/Khaled Gamal"],
                   ["Cs17", "Dr/Mohamed Yousef Basiony"],
                   ["Cs18", "Dr/Sara tarek"],
                   ["Cs19", "Eng/Rasha"],  # 32
                   ["IS3", "Eng/Manal"],
                   ["IS4", "Eng/Sara Salah"],
                   ["IS5", "Eng/Kotb"],
                   ["IT4", "DR/ISLAM TAG"],
                   ["Cs19", "Eng/Abdo Gamal"],  # 37
                   ["IS5", "DR/Tarek"],
                   ["IS6", "Eng/Sahar"],
                   ["IS7", "Eng/Ghada"],
                   ["IT5", "Dr/Dalia"],
                   ["IT6", "Eng/Fatma"],  # 42
                   ["IT7", "Dr/Nagwa"],
                   ["IT8", "Eng/El Kady"],
                   ["IT9", "Eng/Abdelrahman Sayed"]]

    def __init__(self):
        self._rooms = []
        self._meetingTimes = []
        self._instructors = []
        self._days = []
        for i in range(0, len(self.ROOMS)):  # define the rooms by its class
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.INSTRUCTORS)):  # define the instructors by its class
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):  # define the times by its class
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i]))
        for i in range(0, len(self.DAYS)):  # define the days by its class
            self._days.append(Day(self.DAYS[i]))
        # Append courses Data
        # for grade 1
        course1 = Course("G1-1", "Math 2", [self._instructors[0]], 100, "1st")
        course2 = Course("G1-10", "Math 2 S01", [self._instructors[1]], 35, "1st", True)
        course3 = Course("G1-11", "Math 2 S02", [self._instructors[1]], 35, "1st", True)
        #course4 = Course("G1-12", "Math 2 S03", [self._instructors[1]], 35, "1st", True)

        course5 = Course("G1-2", "Programming Fundamentals", [self._instructors[2]], 100, "1st")
        course6 = Course("G1-20", "Programming Fundamentals S01", [self._instructors[5]], 35, "1st", True)
        course7 = Course("G1-21", "Programming Fundamentals S02", [self._instructors[5]], 35, "1st", True)
        #course8 = Course("G1-22", "Programming Fundamentals S03", [self._instructors[5]], 35, "1st", True)

        course9 = Course("G1-3", "Social Context of programming", [self._instructors[3]], 100, "1st")

        course10 = Course("G1-4", "Physics 2", [self._instructors[4]], 100, "1st")

        # for grade 2
        course11 = Course("G2-1", "Computers and Ethics", [self._instructors[6]], 100, "2nd")

        course12 = Course("G2-2", "Math 3", [self._instructors[7]], 100, "2nd")
        course13 = Course("G2-20", "Math 3 S01", [self._instructors[8]], 35, "2nd", True)
        course14 = Course("G2-21", "Math 3 S02", [self._instructors[8]], 35, "2nd", True)
        #course15 = Course("G2-22", "Math 3 S03", [self._instructors[8]], 35, "2nd", True)

        course16 = Course("G2-3", "Database Systems", [self._instructors[9]], 100, "2nd")
        course17 = Course("G2-30", "Database Systems S01", [self._instructors[10]], 35, "2nd", True)
        course18 = Course("G2-31", "Database Systems S02", [self._instructors[10]], 35, "2nd", True)
        #course19 = Course("G2-32", "Database Systems S03", [self._instructors[10]], 35, "2nd", True)

        course20 = Course("G2-4", "Computer Architecture", [self._instructors[11]], 100, "2nd")
        course21 = Course("G2-40", "Computer Architecture S01", [self._instructors[12]], 35, "2nd", True)
        course22 = Course("G2-41", "Computer Architecture S02", [self._instructors[12]], 35, "2nd", True)
       # course23 = Course("G2-42", "Computer Architecture S03", [self._instructors[12]], 35, "2nd", True)

        course24 = Course("G2-5", "Data Structures", [self._instructors[13]], 100, "2nd")
        course25 = Course("G2-50", "Data Structures S01", [self._instructors[14]], 35, "2nd", True)
        course26 = Course("G2-51", "Data Structures S02", [self._instructors[14]], 35, "2nd", True)
        #course27 = Course("G2-52", "Data Structures S03", [self._instructors[14]], 35, "2nd", True)

        # for grade 3
        course28 = Course("CSIT1", "Computer Vision", [self._instructors[15]], 100, "3rd")
        course29 = Course("CSIT10", "Computer Vision S01", [self._instructors[16]], 35, "3rd", True)
        course30 = Course("CSIT12", "Computer Vision S02", [self._instructors[16]], 35, "3rd", True)
        #course31 = Course("CSIT13", "Computer Vision S03", [self._instructors[16]], 35, "3rd", True)

        course32 = Course("CSITIS1", "Operating Systems", [self._instructors[15]], 100, "3rd")
        course33 = Course("CSITIS10", "Operating Systems S01", [self._instructors[17]], 35, "3rd", True)
        course34 = Course("CSITIS11", "Operating Systems S02", [self._instructors[17]], 35, "3rd", True)
        #course35 = Course("CSITIS12", "Operating Systems S03", [self._instructors[17]], 35, "3rd", True)

        #course36 = Course("CS1", "Artificial Intelligence", [self._instructors[13]], 100, "3rd")
        #course37 = Course("CS10", "Artificial Intelligence S01", [self._instructors[18]], 35, "3rd", True)
        #course38 = Course("CS11", "Artificial Intelligence S02", [self._instructors[18]], 35, "3rd", True)
        #course39 = Course("CS12", "Artificial Intelligence S03", [self._instructors[18]], 35, "3rd", True)

        course40 = Course("CSIT2", "Image Processing", [self._instructors[19]], 100, "3rd")
        course41 = Course("CSIT20", "Image Processing S01", [self._instructors[20]], 35, "3rd", True)
        course42 = Course("CSIT21", "Image Processing S02", [self._instructors[20]], 35, "3rd", True)
        #course43 = Course("CSIT22", "Image Processing S03", [self._instructors[20]], 35, "3rd", True)

        course44 = Course("CSITIS2", "Software Engineering", [self._instructors[21]], 100, "3rd")
        course45 = Course("CSITIS20", "Software Engineering S01", [self._instructors[22]], 35, "3rd", True)
        course46 = Course("CSITIS21", "Software Engineering S02", [self._instructors[22]], 35, "3rd", True)
       # course47 = Course("CSITIS22", "Software Engineering S03", [self._instructors[22]], 35, "3rd", True)

        course48 = Course("CS2", "Algorithms Design", [self._instructors[23]], 100, "3rd")
        course49 = Course("CS20", "Algorithms Design S01", [self._instructors[24]], 35, "3rd", True)
        course50 = Course("CS21", "Algorithms Design S02", [self._instructors[24]], 35, "3rd", True)
        #course51 = Course("CS22", "Algorithms Design S03", [self._instructors[24]], 35, "3rd", True)
        # is only
        course72 = Course("IS1", "DSS", [self._instructors[19]], 100, "3rd")
        course73 = Course("IS2", "DSS S01", [self._instructors[33]], 35, "3rd", True)
        course74 = Course("IS3", "DSS S02", [self._instructors[33]], 35, "3rd", True)
       # course75 = Course("IS4", "DSS S03", [self._instructors[33]], 35, "3rd", True)

        course76 = Course("IS11", "GIS", [self._instructors[34]], 100, "3rd")
        course77 = Course("IS12", "GIS S01", [self._instructors[35]], 35, "3rd", True)
        course78 = Course("IS13", "GIS S02", [self._instructors[35]], 35, "3rd", True)
        #course79 = Course("IS14", "GIS S03", [self._instructors[35]], 35, "3rd", True)

        course80 = Course("IS21", "Strategy", [self._instructors[36]], 100, "3rd")
        course81 = Course("IS22", "Strategy S01", [self._instructors[37]], 35, "3rd", True)
        course82 = Course("IS23", "Strategy S02", [self._instructors[37]], 35, "3rd", True)
        #course83 = Course("IS24", "Strategy S03", [self._instructors[37]], 35, "3rd", True)

        # IT
        course92 = Course("IT1", "Network Management", [self._instructors[36]], 100, "3rd")
        course93 = Course("IT2", "Network Management S01", [self._instructors[17]], 35, "3rd", True)
        course94 = Course("IT3", "Network Management S02", [self._instructors[17]], 35, "3rd", True)
        #course95 = Course("IT4", "Network Management S03", [self._instructors[17]], 35, "3rd", True)

        course96 = Course("IT11", "Network Security", [self._instructors[26]], 100, "3rd")
        course97 = Course("IT12", "Network Security S01", [self._instructors[17]], 35, "3rd", True)
        course98 = Course("IT13", "Network Security S02", [self._instructors[17]], 35, "3rd", True)
       # course99 = Course("IT14", "Network Security S03", [self._instructors[17]], 35, "3rd", True)

        # ISIT
        course104 = Course("ISIT1", "Web Programing", [self._instructors[43]], 100, "3rd")
        course105 = Course("ISIT2", "Web Programing S01", [self._instructors[44]], 35, "3rd", True)
        course106 = Course("ISIT3", "Web Programing S02", [self._instructors[44]], 35, "3rd", True)
       # course107 = Course("ISIT4", "Web Programing S03", [self._instructors[44]], 35, "3rd", True)

        # for grade 4
        course52 = Course("CSITIS3", "Distributed Databases", [self._instructors[9]], 100, "4th")
        course53 = Course("CSITIS30", "Distributed Databases S01", [self._instructors[25]], 35, "4th", True)
        course54 = Course("CSITIS31", "Distributed Databases S02", [self._instructors[25]], 35, "4th", True)
       # course55 = Course("CSITIS32", "Distributed Databases S03", [self._instructors[25]], 35, "4th", True)

        course56 = Course("CSIT3", "Network Programming", [self._instructors[26]], 100, "4th")
        course57 = Course("CSIT30", "Network Programming S01", [self._instructors[27]], 35, "4th", True)
        course58 = Course("CSIT31", "Network Programming S02", [self._instructors[27]], 35, "4th", True)
       # course59 = Course("CSIT32", "Network Programming S03", [self._instructors[27]], 35, "4th", True)

        course60 = Course("CS4", "Intelligent Systems", [self._instructors[28]], 100, "4th")
        course61 = Course("CS40", "Intelligent Systems S01", [self._instructors[16]], 35, "4th", True)
        course62 = Course("CS41", "Intelligent Systems S02", [self._instructors[16]], 35, "4th", True)
       # course63 = Course("CS42", "Intelligent Systems S03", [self._instructors[16]], 35, "4th", True)

        course64 = Course("CS5", "Parallel Programming", [self._instructors[30]], 100, "4th")
        course65 = Course("CS50", "Parallel Programming S01", [self._instructors[29]], 35, "4th", True)
        course66 = Course("CS51", "Parallel Programming S02", [self._instructors[29]], 35, "4th", True)
        #course67 = Course("CS52", "Parallel Programming S03", [self._instructors[29]], 35, "4th", True)

        #course68 = Course("CS6", "Information Security", [self._instructors[31]], 100, "4th")
        #course69 = Course("CS60", "Information Security S01", [self._instructors[32]], 35, "4th", True)
        #course70 = Course("CS61", "Information Security S02", [self._instructors[32]], 35, "4th", True)
       # course71 = Course("CS62", "Information Security S03", [self._instructors[32]], 35, "4th", True)

        # is only
        course84 = Course("IS31", "Quality", [self._instructors[38]], 100, "4th")
        course85 = Course("IS32", "Quality S01", [self._instructors[39]], 35, "4th", True)
        course86 = Course("IS33", "Quality S02", [self._instructors[39]], 35, "4th", True)
        #course87 = Course("IS34", "Quality S03", [self._instructors[39]], 35, "4th", True)

        course88 = Course("IS41", "SIS", [self._instructors[9]], 100, "4th")
        course89 = Course("IS42", "SIS S01", [self._instructors[40]], 35, "4th", True)
        course90 = Course("IS43", "SIS S02", [self._instructors[40]], 35, "4th", True)
       # course91 = Course("IS44", "SIS S03", [self._instructors[40]], 35, "4th", True)

        # it
        course100 = Course("IT21", "Wireless", [self._instructors[41]], 100, "4th")
        course101 = Course("IT22", "Wireless S01", [self._instructors[42]], 35, "4th", True)
        course102 = Course("IT23", "Wireless S02", [self._instructors[42]], 35, "4th", True)
        #course103 = Course("IT24", "Wireless S03", [self._instructors[42]], 35, "4th", True)

        # ISIT
        course108 = Course("ISIT31", "E-Commerce", [self._instructors[36]], 100, "4th")
        course109 = Course("ISIT32", "E-Commerce S01", [self._instructors[45]], 35, "4th", True)
        course110 = Course("ISIT33", "E-Commerce S02", [self._instructors[45]], 35, "4th", True)
        #course111 = Course("ISIT34", "E-Commerce S03", [self._instructors[45]], 35, "4th", True)

        self._courses = [course1, course2, course3, course5, course6, course7, course9, course10,
                         course11, course12, course13, course14, course16, course17, course18,
                         course20, course21, course22, course24, course25, course26, course28,
                         course29, course30,  course32, course33, course34,
                          course40, course41, course42,  course44, course45, course46,
                          course48, course49, course50,  course52, course53, course54,
                         course56, course57, course58,  course60, course61, course62,  course64,
                         course65, course66, course72, course73,
                         course74, course76, course77, course78, course80, course81, course82,
                          course84, course85, course86, course88, course89, course90,
                         course92, course93, course94, course96, course97, course98,  course100,
                         course101, course102,  course104, course105, course106,  course108,
                         course109, course110]  # intial courses to be printed
        # Define the Departments
        CS = Department(["CS"],
                        [ course48, course49, course50, course60,
                         course61, course62, course64, course65, course66])
        IS = Department(["IS"],
                        [course72, course73, course74, course76, course77, course78, course80,
                         course81, course82, course84, course85, course86, course88, course89,
                         course90])
        IT = Department(["IT"],
                        [course92, course93, course94, course96, course97, course98, course100,
                         course101, course102])
        CS_IT = Department(["CS", "IT"],
                           [course28, course29, course30, course40, course41, course42, course56,
                            course57, course58])
        # CS_IS = Department(["CS", "IS"], [])
        IS_IT = Department(["IS", "IT"],
                           [course104, course105, course106, course108, course109, course110])
        General = Department(["CS", "IT", "IS"],
                             [course1, course2, course3, course5, course6, course7, course9, course10,
                              course11, course12, course13, course14, course16, course17, course18,
                              course20, course21, course22, course24, course25, course26, course32,
                              course33, course34, course44, course45, course46, course52, course53,
                              course54,])
        self._depts = [CS,IS,IT,IS_IT, CS_IT, General]  # Define the Departments that is looped on
        #self._depts = [CS, CS_IT, General]
        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())

    def get_rooms(self):
        return self._rooms

    def get_instructors(self):
        return self._instructors

    def get_courses(self):
        return self._courses

    def get_depts(self):
        return self._depts

    def get_meetingTimes(self):
        return self._meetingTimes

    def get_days(self):
        return self._days

    def get_numberOfClasses(self):
        return self._numberOfClasses


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self):
        return self._numbOfConflicts

    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):  # Define the classes objects Data
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(data.get_meetingTimes()))])
                newClass.set_day(data.get_days()[rnd.randrange(0, len(data.get_days()))])
                newClass.set_room(data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))])
                newClass.set_instructor(
                    courses[j].get_instructors()[rnd.randrange(0, len(courses[j].get_instructors()))])
                self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):  # calculate the number of conflicts
            # check if the Capacity of the hall is more or equal than the number of student for the course if not there will be conflicts
            if classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbOfStudents():
                self._numbOfConflicts += 1
            for j in range(i, len(classes)):
                # check if there is a class has the same time ,the same day and the same grade
                if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and classes[i].get_day() == classes[
                    j].get_day() and classes[i].get_id() != classes[j].get_id() and classes[
                    i].get_course().get_grade() == classes[j].get_course().get_grade()):
                    # check if the class have the same department and the both classes are not Labs
                    if (np.any(np.in1d(classes[i].get_dept().get_name(), classes[j].get_dept().get_name())) and not (
                            classes[i].get_course().get_isLab() == True and classes[
                        j].get_course().get_isLab() == True)): self._numbOfConflicts += 1
                    # check if the classes have the same Hall
                    if classes[i].get_room() == classes[j].get_room(): self._numbOfConflicts += 1
                # check if there is a class has the same time ,the same day
                if classes[i].get_meetingTime() == classes[j].get_meetingTime() and classes[i].get_day() == classes[
                    j].get_day() and classes[i].get_id() != classes[j].get_id():
                    # check if the both classes have the same instructors
                    if classes[i].get_instructor() == classes[j].get_instructor(): self._numbOfConflicts += 1
        # Calculate the fitness value
        return 1 /((1.0 * self._numbOfConflicts + 1))

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes) - 1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule().initialize())

    def get_schedules(self): return self._schedules


# Steps of genetic algorith
class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population)) #p*c*P*6*c*c == 6*p^2 C^3

    def _crossover_population(self, pop):      #p*6*c^2
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]          #6*c^2
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population):         #p *c
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if (rnd.random() > 0.5):
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if (MUTATION_RATE > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)   #t*c^2
        return tournament_pop


# Define Course
class Course:
    def __init__(self, number, name, instructors, maxNumbOfStudents, grade, isLab=False):
        self._number = number
        self._name = name
        self._maxNumbOfStudents = maxNumbOfStudents
        self._instructors = instructors
        self._grade = grade
        self._isLab = isLab

    def get_number(self): return self._number

    def get_name(self): return self._name

    def get_instructors(self): return self._instructors

    def get_maxNumbOfStudents(self): return self._maxNumbOfStudents

    def get_grade(self): return self._grade

    def get_isLab(self): return self._isLab

    def __str__(self): return self._name


# Define instructor
class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self): return self._id

    def get_name(self): return self._name

    def __str__(self): return self._name


# Define Halls of lectures and Sections Labs
class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity

    def get_number(self): return self._number

    def get_seatingCapacity(self): return self._seatingCapacity


# Define the durations of the classes
class MeetingTime:
    def __init__(self, time):
        self._time = time

    def get_time(self): return self._time
    # Define the Departments in the faculty


class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def get_name(self): return self._name

    def get_courses(self): return self._courses


# Define the class
class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._day = None
        self._room = None

    def get_id(self): return self._id

    def get_dept(self): return self._dept

    def get_course(self): return self._course

    def get_instructor(self): return self._instructor

    def get_meetingTime(self): return self._meetingTime

    def get_room(self): return self._room

    def get_day(self): return self._day

    def set_instructor(self, instructor): self._instructor = instructor

    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime

    def set_day(self, day): self._day = day

    def set_room(self, room): self._room = room

    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + \
               str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(
            self._meetingTime.get_time()) + "," + str(self._day.get_day())


# class used to print the data of all schdules and all the data avalible using prettyTables
class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()
        self.print_days()

    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(
            ['id', 'course #', 'max # of students', 'instructors', 'grade', 'IsLab'])
        courses = data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ", "
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row(
                [courses[i].get_number(), courses[i].get_name(), str(courses[i].get_maxNumbOfStudents()), tempStr,
                 courses[i].get_grade(), str(courses[i].get_isLab())])
        print(availableCoursesTable)

    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(['id', 'instructor'])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(['Meeting Time'])
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row([meetingTimes[i].get_time()])  # comment
        print(availableMeetingTimeTable)

    def print_days(self):
        availableDaysTable = prettytable.PrettyTable(['day'])
        days = data.get_days()
        for i in range(0, len(days)):
            availableDaysTable.add_row([days[i].get_day()])
        print(availableDaysTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            ['schedule #', 'fitness', '# of conflicts', 'classes [dept,class,room,instructor,meeting-time,day]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row([str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_numbOfConflicts(),
                            schedules[i].__str__()])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(
            ['Class #', 'grade', 'Dept', 'Course (number, max # of students)', 'Is Lab', 'Room (Capacity)',
             'Instructor (Id)', 'Meeting Time', 'day'])
        for i in range(0, len(classes)):
            table.add_row([str(i), classes[i].get_course().get_grade(), classes[i].get_dept().get_name(),
                           classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_number() + ", " +
                           str(classes[i].get_course().get_maxNumbOfStudents()) + ")",
                           str(classes[i].get_course().get_isLab()),
                           classes[i].get_room().get_number() + " (" + str(
                               classes[i].get_room().get_seatingCapacity()) + ")",
                           classes[i].get_instructor().get_name() + " (" + str(
                               classes[i].get_instructor().get_id()) + ")",
                           classes[i].get_meetingTime().get_time(), classes[i].get_day().get_day()])
        print(table)

    def print_classes_as_table(self, classes):
        table = prettytable.PrettyTable(
            ['Class #', 'grade', 'Dept', 'Course (number, max # of students)', 'Is Lab', 'Room (Capacity)',
             'Instructor (Id)', 'Meeting Time', 'day'])
        for i in range(0, len(classes)):
            table.add_row([str(i), classes[i].get_course().get_grade(), classes[i].get_dept().get_name(),
                           classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_number() + ", " +
                           str(classes[i].get_course().get_maxNumbOfStudents()) + ")",
                           str(classes[i].get_course().get_isLab()),
                           classes[i].get_room().get_number() + " (" + str(
                               classes[i].get_room().get_seatingCapacity()) + ")",
                           classes[i].get_instructor().get_name() + " (" + str(
                               classes[i].get_instructor().get_id()) + ")",
                           classes[i].get_meetingTime().get_time(), classes[i].get_day().get_day()])
        print(table)


# class used to print the output in file and the console
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("result.txt", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger()


# function to split the Schedules to the four grades and sort it by the days
def sort_print_final_result(data):
    final_schedule = data
    _1st = [];
    _2nd = [];
    _3rd = [];
    _4th = []
    for i in range(0, len(final_schedule)):
        if (final_schedule[i].get_day().get_day() == "Sunday"):
            if (final_schedule[i].get_course().get_grade() == "1st"):
                _1st.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "2nd":
                _2nd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "3rd":
                _3rd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "4th":
                _4th.append(final_schedule[i])
    for i in range(0, len(final_schedule)):
        if final_schedule[i].get_day().get_day() == "Monday":
            if final_schedule[i].get_course().get_grade() == "1st":
                _1st.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "2nd":
                _2nd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "3rd":
                _3rd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "4th":
                _4th.append(final_schedule[i])
    for i in range(0, len(final_schedule)):
        if final_schedule[i].get_day().get_day() == "Tuesday":
            if final_schedule[i].get_course().get_grade() == "1st":
                _1st.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "2nd":
                _2nd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "3rd":
                _3rd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "4th":
                _4th.append(final_schedule[i])
    for i in range(0, len(final_schedule)):
        if final_schedule[i].get_day().get_day() == "Wednesday":
            if final_schedule[i].get_course().get_grade() == "1st":
                _1st.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "2nd":
                _2nd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "3rd":
                _3rd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "4th":
                _4th.append(final_schedule[i])
    for i in range(0, len(final_schedule)):
        if final_schedule[i].get_day().get_day() == "Thursday":
            if final_schedule[i].get_course().get_grade() == "1st":
                _1st.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "2nd":
                _2nd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "3rd":
                _3rd.append(final_schedule[i])
            elif final_schedule[i].get_course().get_grade() == "4th":
                _4th.append(final_schedule[i])
    print("Frist Grade schedule : ")
    displayMgr.print_classes_as_table(_1st)
    print("Second Grade schedule : ")
    displayMgr.print_classes_as_table(_2nd)
    print("Third Grade schedule : ")
    displayMgr.print_classes_as_table(_3rd)
    print("Fourth Grade schedule : ")
    displayMgr.print_classes_as_table(_4th)


data = Data()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # " + str(generationNumber))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
geneticAlgorithm = GeneticAlgorithm()
while population.get_schedules()[0].get_fitness() != 1.0:
    generationNumber += 1
    print("\n> Generation # " + str(generationNumber))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])
final_schedule = population.get_schedules()[0].get_classes()
sort_print_final_result(final_schedule)

print("\n\n")
