import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    infile = open(filename)
    infile.readline(); infile.readline()
    x = []; u = []

    for line in infile:
        elements = line.split()
        x.append(float(elements[0]))
        u.append(float(elements[1]))
    x = np.array(x)
    u = np.array(u)
    infile.close()

    return x,u


x_n10, u_n10 = read_file("exact_n10.txt")
x_n100, u_n100 = read_file("exact_n100.txt")
x_n1000, u_n1000 = read_file("exact_n1000.txt")
x_n10000, u_n10000 = read_file("exact_n10000.txt")
x_n100000, u_n100000 = read_file("exact_n100000.txt")
#x_n1000000, u_n1000000 = read_file("exact_n1000000.txt")
#x_n10000000, u_n10000000 = read_file("exact_n10000000.txt")

plt.figure(0)
plt.plot(x_n1000,u_n1000)
plt.xlabel('x')
plt.ylabel('u(x)')
plt.savefig('exact.pdf')

x_num_n10, u_num_n10 = read_file("output_n10.txt")
x_num_n100, u_num_n100 = read_file("output_n100.txt")
x_num_n1000, u_num_n1000 = read_file("output_n1000.txt")
x_num_n10000, u_num_n10000 = read_file("output_n10000.txt")
x_num_n100000, u_num_n100000 = read_file("output_n100000.txt")
#x_num_n1000000, u_num_n1000000 = read_file("output_n1000000.txt")
#x_num_n10000000, u_num_n10000000 = read_file("output_n10000000.txt")

plt.figure(1)
plt.plot(x_n100,u_n100,label='u(x)')
plt.plot(x_num_n10, u_num_n10,label='Num n=10')
plt.plot(x_num_n100, u_num_n100,label='Num n=100')
plt.plot(x_num_n1000, u_num_n1000,label='Num n=1000')
plt.plot(x_num_n10000, u_num_n10000,label='Num n=10000')
plt.xlabel("x"); plt.ylabel("u(x)")
plt.grid()
plt.legend()
plt.savefig("solutions.pdf")

#8
Delta_n10 = np.abs(u_n10-u_num_n10)
Delta_n100 = np.abs(u_n100-u_num_n100)
Delta_n1000 = np.abs(u_n1000-u_num_n1000)
Delta_n10000 = np.abs(u_n10000-u_num_n10000)

plt.figure(2)
plt.plot(x_n10[1:],Delta_n10[1:],label='n=10')
plt.plot(x_n100[1:],Delta_n100[1:],label='n=100')
plt.plot(x_n1000[1:],Delta_n1000[1:],label='n=1000')
plt.plot(x_n10000[1:],Delta_n10000[1:],label='n=10000')
plt.yscale('log')
plt.xlabel('x')
plt.grid()
plt.ylabel('Absolute error')
plt.legend()
plt.savefig('abs_err.pdf')

plt.figure(3)
Epsilon_n10 = np.abs((u_n10-u_num_n10)/u_n10)
Epsilon_n100 = np.abs((u_n100-u_num_n100)/u_n100)
Epsilon_n1000 = np.abs((u_n1000-u_num_n1000)/u_n1000)
Epsilon_n10000 = np.abs((u_n10000-u_num_n10000)/u_n10000)
Epsilon_n100000 = np.abs((u_n100000-u_num_n100000)/u_n100000)
#Epsilon_n1000000 = np.abs((u_n1000000-u_num_n1000000)/u_n1000000)
#Epsilon_n10000000 = np.abs((u_n10000000-u_num_n10000000)/u_n10000000)


plt.plot(x_n10[1:],Epsilon_n10[1:],label='n=10')
plt.plot(x_n100[1:],Epsilon_n100[1:],label='n=100')
plt.plot(x_n1000[1:],Epsilon_n1000[1:],label='n=1000')
plt.plot(x_n10000[1:],Epsilon_n10000[1:],label='n=10000')

print('n=10',np.max(Epsilon_n10[1:]))
print('n=100',np.max(Epsilon_n100[1:]))
print('n=1000',np.max(Epsilon_n1000[1:]))
print('n=10000',np.max(Epsilon_n10000[1:]))
print('n=100000',np.max(Epsilon_n100000[1:]))
#print('n=1000000',np.max(Epsilon_n1000000[1:]))
#print('n=10000000',np.max(Epsilon_n10000000[1:]))
plt.yscale('log')
plt.xlabel('x')
plt.ylabel('Relative error')
plt.savefig('rel_err.pdf')
plt.show()
