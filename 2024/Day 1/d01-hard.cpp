#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <unordered_map>

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



    // Count occurrences of each number in r
    std::unordered_map<int, int> r_count;
    for (const auto& num : r) {
        r_count[num]++;
    }

    // Calculate the total similarity score
    int s = 0;
    for (const auto& num : l) {
        s += num * r_count[num]; // Multiply the number by its count in r
    }

    std::cout << s << std::endl;

    return 0;

}
