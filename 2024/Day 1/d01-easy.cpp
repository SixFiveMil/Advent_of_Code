#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath> // For std::abs

int main() {
    std::ifstream inputFile("input.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open the file!" << std::endl;
        return 1;
    }

    std::vector<int> l, r;
    std::string line;

    // Read each line from the file
    while (std::getline(inputFile, line)) {
        std::istringstream lineStream(line);
        int num1, num2;
        
        // Parse two numbers separated by whitespace
        if (lineStream >> num1 >> num2) {
            l.push_back(num1);
            r.push_back(num2);
        }
    }

    inputFile.close();

    // Sort both lists
    std::sort(l.begin(), l.end());
    std::sort(r.begin(), r.end());

    // Calculate the total difference
    int d = 0;
    for (size_t i = 0; i < l.size(); ++i) {
        d += std::abs(l[i] - r[i]);
    }

    std::cout << d << std::endl;

    return 0;
}
