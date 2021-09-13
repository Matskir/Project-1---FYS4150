#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
#include <iomanip>

int main(){
  int n = 1000;
  double x_min = 0.0;
  double x_max = 1.0;

  std::vector<double> x_values;
  std::vector<double> u_values;

  std::ofstream myfile;
  myfile.open ("exact_n1000.txt");

  std::cout << std::setprecision(3) << std::fixed;
  myfile << std::scientific;

  myfile << "     x             u(x)    \n";
  myfile << "=============================\n";

  for (int i = 0; i < n; i++){
    double x_new = x_min + i*((x_max-x_min)/n);
    x_values.push_back(x_new);
    double u_new = 1 - (1-exp(-10))*x_new - exp(-10*x_new);
    u_values.push_back(u_new);
    myfile << x_new  << "    " << u_new << "\n";
  }

  std::cout << x_values[100] << "\n";
  std::cout << u_values[100] << "\n";
  myfile.close();

  return 0;

}
