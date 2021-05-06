import sys
import numpy
from scipy import stats

class UnclassifiedPlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')

        line = self.infile.readline()
        contents = line.strip().split(',')
        self.indices = []
        for i in range(len(contents)):
           if ((contents[i].find("Kingdom") != -1) or
              (contents[i].find("Phylum") != -1) or
              (contents[i].find("Class") != -1) or
              (contents[i].find("Order") != -1) or
              (contents[i].find("Family") != -1)):
                  self.indices.append(i)
    def run(self):
        self.a = []
        for line in self.infile:
           contents = line.strip().split(',')
           unclassified = 0
           for i in self.indices:
                  unclassified += float(contents[i])
           self.a.append(unclassified)


    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write("Mean Unclassified Reads: "+str(numpy.mean(self.a))+"\n")
       outfile.write("Standard Deviation: "+str(stats.sem(self.a))+"\n")
#print(numpy.array(a))
#print(numpy.mean(a))
#print(stats.sem(a))
