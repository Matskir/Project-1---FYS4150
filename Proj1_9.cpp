#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
#include <iomanip>
#include <chrono>

int main(){
  auto t1 = std::chrono::high_resolution_clock::now();
  double n = 1000000;
  double h = 1/n;

  std::vector<double> g_vector;
  std::vector<double> x_values;

  double x_min = 0;
  double x_max = 1;

  for (int i = 0; i < n; i++){
    double x_new = x_min + i*((x_max-x_min)/n);
    x_values.push_back(x_new);
    g_vector.push_back(h*h*100*exp(-10*x_new));
  }

  std::vector<double> b_tilde(n,0);
  std::vector<double> g_tilde(n,0);

  std::vector<double> v_vector(n,0);

  b_tilde[0] = 2;
  g_tilde[0] = g_vector[0];

  for (int i = 1; i < n; i++){
    //Fill b_tilde and g_tilde
    b_tilde[i] = 2 - 1/(b_tilde[i-1]);
    g_tilde[i] = g_vector[i] + g_tilde[i-1]/b_tilde[i-1];

  }
  v_vector[n-1] = g_tilde[n-1]/b_tilde[n-1];

  std::ofstream myfile;
  myfile.open ("output_spec_n1000000.txt");
  std::cout << std::setprecision(3) << std::fixed;
  myfile << std::scientific;
  myfile << "     x             u(x)    \n";
  myfile << "=============================\n";


  for (int i = n-1; i > 0; i--){
    v_vector[i] = (g_tilde[i]+v_vector[i+1])/b_tilde[i];
  }

  for (int i = 0; i < n; i++){
      myfile << x_values[i] << "     " << v_vector[i] <<"\n";
  }
  myfile.close();
  auto t2 = std::chrono::high_resolution_clock::now();
  double durations_seconds = std::chrono::duration<double>(t2-t1).count();
  std::cout << durations_seconds << "\n";
  return 0;
}
