import sys
import math
import random
import statistics

def generatePop(xl,xu):          # Generate a population by random number generation given the upper and the lower bound specified in the last                              
    pop = []
    for individual in range(ind):
        a = round(random.uniform(xl,xu),l)
        pop.append(a)
    return pop
    

def selection(pop):              # Stochastic Remainder Roulette wheel selection
    random.shuffle(pop)
    selected = []
    fitness = []

    for i in range(ind):
        fitness.append(1+math.sin(pop[i])) # Since the fitness can also be negative a constant is used '1' which is added to all the values so as to evalute the number of copies.

    meanfit = statistics.mean(fitness)
    
    for i in range(ind):
        
        intfit =int(fitness[i]/meanfit)
        for j in range(intfit):
            selected.append(pop[i])
        
    fractionfit =[]

    for i in range(ind):
        fractionfit.append(fitness[i]- int(fitness[i]))
   
    while(len(selected) !=ind):
        a = random.randint(0,ind-1)
        b = random.randint(0,ind-1)       
        if (fractionfit[a])>(fractionfit[b]):
            selected.append(pop[a])
             
        else:
            selected.append(pop[b])
   
    return selected


def realspace(pop):                            #This is the function for converting the population set to integer values with the help of given precision value 
    value = pop
    
    for i in range(ind):
        decimal = pop[i]/precision - int(pop[i]/precision)  
        if decimal>=0.5:                       # As sangam told there is a little bug over here which is kind of conceptual mistake
            value[i] = int(value[i]/precision)+1
        else:
            value[i] = int(value[i]/precision)
    return value


def workspace(pop):                            # This is a code to convert the integer value back to the population
    output =[]
    for i in range(ind):
        a = pop[i]*precision
        output.append(a)
    return output


            
def binary(e):                                  #This is the function to convert the integers to the corresponding binary values
    binary =[]
    for i in range(ind):
        binary.append('{0:07b}'.format(e[i]))   # Here we specify the length of the binary
    return binary 
    
def crossoverfunc(f):                           # This is a function which determines the number of times the crossover will occur by a random number generation
    value=f
    a = random.randint(1,ind-1)
    for i in range(a):
        value =crossover(value)
    output = value
    
    return output 
    
     

def crossover(f):                               #This is the Uniform crossover type function
    crossed =[]
    binary = []
    valuefirst = []
    valuesecond = []
    lob = l
    a = random.randint(0,ind-1)
    b = random.randint(0,ind-1)
    first = f[a]
    second = f[b]
    for length in range(lob):
        prob = random.uniform(0,1)
        if prob <= pc:
            valuesecond.append(first[length])
            valuefirst.append(second[length])
        else:
            valuefirst.append(first[length])
            valuesecond.append(second[length])
    
    output = []
    valuefirst =''.join(valuefirst)
    valuesecond = ''.join(valuesecond)

    
    for num in range(ind):
        if num==a:
            output.append(valuefirst)
        elif num==b:
            output.append(valuesecond)
        else:
            output.append(f[num])
    
    return output

def mutationfunc(g):                      #This function determines the number of times the mutation will occur by a random number generation
    value=g
    a = random.randint(1,ind-1)
    for i in range(a):
        value =mutation(value)
    output = value
    
    return output

def mutation(g):                          #This is the least significant bit mutation type with probability given in the end
    mut =[]  
    a = random.randint(0,ind-1)
    value = g[a]
    prob = random.uniform(0,1)
    for i in range(0,l):
        if i==(l-1):
            if prob<=pm:
                if value[l-1] == 0:
                       mut.append('1')
                else:
                       mut.append('0')
            else:
                if value[l-1] == 0:
                       mut.append('0')
                else:
                       mut.append('1')
        else:
            mut.append(value[i])
 
    output =[]
 
    mut = ''.join(mut)
    
    for i in range(ind):
        if i==a:
           output.append(mut)
        else:
           output.append(g[i])
    return output

def binarytoint(h):                           #This is a function to convert the binary to the corresponding decimal value
    output =[]
    for i in range(ind):
        output.append(int(h[i],2))
    return output
    

def fitness(pop):                             #This is the function to assign the fitness value to the population
    fit =[]
    for i in range(ind):
        fit.append(math.sin(pop[i]))
    return fit

def Geneticalgo(xu,xl):                       # This is the main function which performs all of the operations in respective sequence
    #First step is to have a random popolation say of size 'ind' individuals
    print("We generate a random population of size", ind)
    i = generatePop(xl,xu)
    print(i)

    iteration = 1
    fmax = -1
    while(fmax<=0.9999 and iteration<=100):
        print("The Iteration number is", iteration)
        c = selection(i)
        print("The selected values are") 
        print(c)

        e = realspace(c)
        print("The encoded value with precision is")
        print(e)

        f = binary(e)
        print("The binary value of the selected value is")
        print(f)
        g = crossoverfunc(f)
        print("The binary value after crossover is")
        print(g)

        k = binarytoint(g)
        print("The encoded value with precision is")
        print(k)

        h = mutationfunc(g)
        print("The binary value after mutation is")
        print(h)

        j = binarytoint(h)
        print("The binary value with precision is")
        print(j)
        
        i = workspace(j)
        print("The real value after mutation is")
        print(i)
        maxfit = max(fitness(i))
        print("The maximum fitness found after", iteration,"iteration is found to be",maxfit, '\n', '\n')
        fmax=maxfit
        iteration = iteration + 1

    print("The maximum value of sine function in range", xl, "and", xu, "is found to be", fmax)



# say the length of the bit used is 8

l=7                      #When changing this length remenber to change the value in the definition of binary() also.
pm = 0.8
pc = 0.8
xl =0
xu =2*3.14
precision = (xu-xl)/(2**l-1)
ind =20
Geneticalgo(xu,xl)




