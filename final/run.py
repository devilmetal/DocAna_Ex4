import sys
import os
from subprocess import call
import random


neurons = [1,2,5,10,25,50,100, 200, 500, 800, 1000, 1500]
epochs = [1, 2, 5, 8, 10, 25, 50, 100]
learning_rate = [0.8,0.5,0.2,0.1,0.08,0.05,0.01,0.008,0.005,0.001,0.0001]
training_samples = [20, 100, 1000, 2000, 5000, 10000, 60000]
# training_samples = [10000]
runs = 2


# # VARYING THE NUMBER OF NEURONS
for neuron in neurons:
    for run in range(1):
        fn = "results/neurons/"+str(neuron)+ "n_10_l_001_e10_r"+str(run+1)
        call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 112 -n " +str(neuron)+ " -o 10 -l 0.001 -e 10 train.txt test.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt", shell=True)
        print "-----------------------------------------------------------------------------"
        print "   run " +str(run+1)+ " with " +str(neuron)+ " neurons DONE."
        print "-----------------------------------------------------------------------------"

# # VARYING THE NUMBER OF EPOCHS
for epoch in epochs:
    for run in range(runs):
        fn = "results/epochs/500n_10_l_001_e" +str(epoch)+ "_r"+str(run+1)
        call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 112 -n 500 -o 10 -l 0.001 -e " +str(epoch)+ " train.txt test.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt", shell=True)
        print "-----------------------------------------------------------------------------"
        print "   run " +str(run+1)+ " with " +str(epoch)+ " epochs DONE"
        print "-----------------------------------------------------------------------------"
#
# # VARYING THE LEARNING RATE
for lr in learning_rate:
    for run in range(runs):
        fn = "results/learning_rate/500n_10_l_"+str(lr).split('.')[1]+"_e10_r"+str(run+1)
        call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 112 -n 500 -o 10 -l "+str(lr)+" -e 10 train.txt test.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt", shell=True)
        print "-----------------------------------------------------------------------------"
        print "   run " +str(run+1)+ " with learning rate of " +str(lr)+ " DONE"
        print "-----------------------------------------------------------------------------"

# VARYING THE NUMBER OF TRAINING SAMPLES
#count = [5923, 6742, 5958, 6131, 5842, 5421, 5918, 6265, 5851, 5949]#total sample per digit (0-9)

'''Gather features per digit'''
count = [0,0,0,0,0,0,0,0,0,0]
file = open('train.txt','rb')
for i, line in enumerate(file):
    if line.startswith('0'):
        count[0] += 1
        new_digit_file = open('train_d_0.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('1'):
        count[1] += 1
        new_digit_file = open('train_d_1.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('2'):
        count[2] += 1
        new_digit_file = open('train_d_2.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('3'):
        count[3] += 1
        new_digit_file = open('train_d_3.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('4'):
        count[4] += 1
        new_digit_file = open('train_d_4.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('5'):
        count[5] += 1
        new_digit_file = open('train_d_5.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('6'):
        count[6] += 1
        new_digit_file = open('train_d_6.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('7'):
        count[7] += 1
        new_digit_file = open('train_d_7.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('8'):
        count[8] += 1
        new_digit_file = open('train_d_8.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
    elif line.startswith('9'):
        count[9] += 1
        new_digit_file = open('train_d_9.txt','ab')
        new_digit_file.write(line)
        new_digit_file.close()
file.close()
# print count


for ts in training_samples:
    if ts != 60000:
        new_file = open('train_'+str(ts)+'.txt','wb')
        ts_per_digit = ts/10
        for d in range(10):
            df = open('train_d_' +str(d)+ '.txt','rb')
            lines = random.sample(xrange(count[d]), ts_per_digit)
            for i, line in enumerate(df):
                if i in lines:
                    new_file.write(line)
            df.close()
        new_file.close()

    for run in range(runs):
        fn = "results/samples/25n_10_l_001_e10_s" +str(ts)+ "_r"+str(run+1)
        if ts != 60000:
            call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 112 -n 25 -o 10 -l 0.001 -e 10 train_" +str(ts)+ ".txt test.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt", shell=True)
        else:
            call("java -jar -Xmx1024m NN_Tool.jar -a SIGMOID -f 112 -n 25 -o 10 -l 0.001 -e 10 train.txt test.txt " +fn+ "_train_output.txt " +fn+ "_test_output.txt", shell=True)
        print "-----------------------------------------------------------------------------"
        print "   run " +str(run+1)+ " with " +str(ts)+ " training samples DONE"
        print "-----------------------------------------------------------------------------"
