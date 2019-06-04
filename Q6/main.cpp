#include<iostream>
#include<cmath>
#include<iomanip>
#include <chrono>
#include <ctime>
#include "CGaussSolver.h"

using namespace std;

long double aFunction(const long double&);

int main(int argc, char* argv[]) {

  long double a{ 0 }, b{ 1 };
  int n{ atoi(argv[1])};
//  int n{ 9 };
  long double(*pf)(const long double&);
  pf = aFunction; // Pointer initialized

  auto start = std::chrono::system_clock::now();
  CGaussSolver aSolver(pf, a, b, n);
  aSolver.exec(); // Calculate the integral
  long double result = aSolver.getResult();
  auto end = std::chrono::system_clock::now();
  cout.precision(20);
  cout << "Result of C++ code (n = "<< setw(2) << n << "): "<< result << endl;

    std::chrono::duration<double> elapsed_seconds = end - start;
    std::cout << "elapsed time of C++ code: " << elapsed_seconds.count()*1000 << " ms\n";
    return 0;

}

long double aFunction(const long double& x){
  long double xN = 0.5 * x + 0.5;
  return (pow(xN, 3) / (xN + 1))*cos(pow(xN, 2));
}