#!/usr/bin/python
import numpy
from random import randint
mu, sigma = randint(1,12), randint(1,5)
samples = numpy.random.normal(mu, sigma, 1000)
file = open("normSamples.csv", "w")
for s in samples:
    file.write(str(s).replace(".",",")+"\n")