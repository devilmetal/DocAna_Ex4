import sys
import os
from subprocess import call
import random

array = ['25,2','50,25,10','25,25','25,15','25,5','25,10','25']
for stuff in array:
	call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 784 -n " +str(stuff)+" -o 10 -l 0.001 -e 25 train_pv.txt test_pv.txt my_train_output.txt my_test_output.txt", shell=True)
for stuff in array:
	call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 784 -n " +str(stuff)+" -o 10 -l 0.001 -e 50 train_pv.txt test_pv.txt my_train_output.txt my_test_output.txt", shell=True)
