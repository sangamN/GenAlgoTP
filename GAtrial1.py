import sys
import math
import random
import statistics

xl=0
xu=2
n=10

def initpop(xl,xu):
	pop=[]
	for i in range(n):
		a=random.uniform(xl,xu)
		pop.append(a)
	return pop

def fitness(pop):
	fit=[]
	for i in range(n):
		fit.append(-(pop[i])**2+2*(pop[i]))
	return fit	

def selectpop(pop):
	random.shuffle(pop)
	fitness=[]
	selected=[]
	for i in range(n):
		fitness.append(-(pop[i])**2+2*(pop[i]))

	meanfit=statistics.mean(fitness)
	for i in range(n):
		intfit=int(fitness[i]/meanfit)
		for j in range(intfit):
			selected.append(pop[i])
	fractionfit=[]
	for i in range(n):
		fractionfit.append(fitness[i]-int(fitness[i]))
	while(len(selected)!=n):
		a=random.randint(0,n-1)
		b=random.randint(0,n-1)
		if (fractionfit[a]>fractionfit[b]):
			selected.append(pop[a])
		else:
			selected.append(pop[b])				
	return selected

def GenAlgo(xl,xu,n):
	print("We generate a population of size",n)
	i=initpop(xl,xu)
	print(i)
	iteration=1
	fmax=-1
	c=[]
	while (fmax<=0.98):
		print("This is iteration",iteration)
		c=selectpop(i)
		print("The selected values are")
		print(c)
		maxfit=max(fitness(i))
		print("The maximum fitness found after iteration",iteration,"is",maxfit,'\n','\n')
		fmax=maxfit
		iteration=iteration+1

GenAlgo(xl,xu,n)				