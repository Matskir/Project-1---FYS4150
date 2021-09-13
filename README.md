create_exact.cpp is the C++ program used for outputting the values of the exact solution u(x) as well as the corresponding x to an output file "exact_n<number of n>.txt". Note that for each value of n the program has to be modified by changing the variable n as well as the filename of the output. The program should be linked, compiled and run in the following way:
       g++ create_exact.cpp -o create_exact.exe
       ./create_exact.exe
  
Proj1_7.cpp is the C++ program where the general algorithm is implemented, and returs the numerically estimated v and the corresponding x to an output file "output_n<number of n>.txt". As before the value of n (+ filename) needs to be manually changed to create all necessary output files for plotting. The program should be linked, compiled and run in the following way:
       g++ Proj1_7.cpp -o proj17.exe
       ./proj17.exe
  
  
Proj1_9.cpp implements the specific algorithm and is very similar to Proj1_7.cpp. As before the value of n (+ filename) needs to be changed manually each time. The program should be linked, compiled and run in the following way:
       g++ Proj1_9.cpp -o proj19.exe
       ./proj19.exe
  
read_file.py is the Python script used for all plotting tasks in this project, and includes a read_file()-function that reads the format of all output files from create_exact.cpp, Proj1_7.cpp and Proj1_9.cpp and plots the needed graphs. NB!!!: All output files from the three C++ programs for n = 10,10^2,10^3,10^4,10^5,10^6,10^7 are needed for the Python script to actually run, but because of the size of the files for 10^6 and 10^7 the parts of the code needing them has been commented out. If you want to verify these parts you'll have to generate these files manually. The needed output files are also provided as generating all output files takes time and effort. 
