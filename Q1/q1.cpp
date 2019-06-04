#include<iostream>
#include<vector>
#include<string>
#include <iterator>
#include <algorithm>
#include <chrono>
//#include <execution>

template<typename T>
void display(const T& v);

int main() {
    //first part: initializing vectors
    std::vector<int> vec1(100);
    int n{1};
    std::for_each(vec1.begin(), vec1.end(), [&n](int& a){a = (n++);});
    std::cout << "vec1 is: ";
    display(vec1);

    std::vector<int> vec2(10);
    n = 1;
    std::for_each(vec2.begin(), vec2.end(), [&n](int& a){a = (n++);});
    std::cout << "vec2 is: ";
    display(vec2);

    // second part: adding vec1 to the end of vec2
    vec2.insert(vec2.end(), vec1.begin(), vec1.end());
    std::cout << "vec2 after pushing vec1: ";
    display(vec2);

    // third part: finding odd elements of vector
    std::vector<int> odd_vec(50);
    auto oit = std::copy_if(begin(vec1), end(vec1), begin(odd_vec), [](int& a){return a%2 != 0;});
    odd_vec.erase(oit, odd_vec.end());
    std::cout << "odd_vec(vect1 odd elements): ";
    display(odd_vec);

    // forth part reversing vector
    std::vector<int> reverse_vec(100);
    std::reverse_copy (begin(vec1), end(vec1), reverse_vec.begin());
    std::cout << "reverse_vec(reverse of vec1): ";
    display(reverse_vec);

    std::vector<int> sorted_vec{vec2};
    const auto startTime {std::chrono::high_resolution_clock::now()};
    std::sort(sorted_vec.begin(), sorted_vec.end());
    const auto endTime {std::chrono::high_resolution_clock::now()};
    std::cout << "sorted vector normal version: ";
    display(sorted_vec);
    std::cout << "time for normal sort: " << std::chrono::duration_cast<std::chrono::duration<double, std::micro>>(endTime - startTime).count() << std::endl;

    /*sorted_vec = vec2;
    const auto startTime = std::chrono::high_resolution_clock::now();
    std::sort(std::execution::par, sorted_vec.begin(), sorted_vec.end());
    const auto endTime = std::chrono::high_resolution_clock::now();
    std::cout << "sorted vector parallel version: \t";
    std::cout << "time for normal sort: " << std::chrono::duration_cast<std::chrono::duration<double, std::micro>>(endTime - startTime).count() << std::endl;
    */
    return 0;
}

template<typename T>
void  display(const T& v) {
    std::copy(v.begin(), v.end(), std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;
    std::cout << std::endl;
}