import sys
import os
from subprocess import call

neurons = [100, 200, 500, 800, 1000, 1500]
epochs = [1, 2, 5, 8, 10, 25, 50, 100]
learning_rate = [0.0001, 0.001, 0.01, 0.1]
training_samples = [20, 100, 1000, 2000, 5000, 10000]
runs = 2


# VARYING THE NUMBER OF NEURONS
for neuron in neurons:
    for run in range(runs):
        fn = "results_pv/neurons/"+str(neuron)+ "n_10_l_001_e10_r"+str(run+1)
        # print "java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 784 -n " +str(neuron)+ " -o 10 -l 0.001 -e 10 train_pv.txt test_pv.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt"
        call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 784 -n " +str(neuron)+ " -o 10 -l 0.001 -e 10 train_pv.txt test_pv.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt", shell=True)
        print "-----------------------------------------------------------------------------"
        print "   run " +str(run+1)+ " with " +str(neuron)+ " neurons DONE."
        print "-----------------------------------------------------------------------------"

# VARYING THE NUMBER OF EPOCHS
for epoch in epochs:
    for run in range(runs):
        fn = "results_pv/epochs/500n_10_l_001_e" +str(epoch)+ "_r"+str(run+1)
        # print "java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 784 -n 500 -o 10 -l 0.001 -e " +str(epoch)+ " train_pv.txt test_pv.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt"
        call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 784 -n 500 -o 10 -l 0.001 -e " +str(epoch)+ " train_pv.txt test_pv.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt", shell=True)
        print "-----------------------------------------------------------------------------"
        print "   run " +str(run+1)+ " with " +str(epoch)+ " epochs DONE"
        print "-----------------------------------------------------------------------------"

# VARYING THE LEARNING RATE
for lr in learning_rate:
    for run in range(runs):
        fn = "results_pv/learning_rate/500n_10_l_"+str(lr).split('.')[1]+"_e10_r"+str(run+1)
        # print "java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 784 -n 500 -o 10 -l "+str(lr)+" -e 10 train_pv.txt test_pv.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt"
        call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 784 -n 500 -o 10 -l "+str(lr)+" -e 10 train_pv.txt test_pv.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt", shell=True)
        print "-----------------------------------------------------------------------------"
        print "   run " +str(run+1)+ " with learning rate of " +str(lr)+ " DONE"
        print "-----------------------------------------------------------------------------"
