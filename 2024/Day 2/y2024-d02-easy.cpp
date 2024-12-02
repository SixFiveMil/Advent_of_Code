#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <tuple> // For std::tuple and std::make_tuple
#include <string> // For std::string

int largest_adjacent_distance(const std::vector<int>& nums) {
    if (nums.size() < 2) {
        return 0; // No adjacent elements to compare
    }
    int max_distance = 0;
    for (size_t i = 0; i < nums.size() - 1; ++i) {
        int distance = std::abs(nums[i] - nums[i + 1]);
        if (distance > max_distance) {
            max_distance = distance;
        }
    }
    return max_distance;
}

std::tuple<int, std::string, int> safe(const std::vector<int>& f) {
    int ld = 0;

    // Check if the list is sorted (ascending or descending)
    bool is_sorted_asc = std::is_sorted(f.begin(), f.end());
    bool is_sorted_desc = std::is_sorted(f.rbegin(), f.rend());

    if (is_sorted_asc || is_sorted_desc) {
        // Check for adjacent equality
        for (size_t i = 0; i < f.size() - 1; ++i) {
            if (f[i] == f[i + 1]) {
                return std::make_tuple(0, std::string("is unsafe due to adjacent equal elements"), ld);
            }
        }

        ld = largest_adjacent_distance(f);
        if (ld <= 3) {
            return std::make_tuple(1, std::string("is Safe distance"), ld);
        } else {
            return std::make_tuple(0, std::string("is unsafe distance"), ld);
        }
    } else {
        return std::make_tuple(0, std::string("is unsafe order"), ld);
    }
}

int main(int argc, char* argv[]) {
    bool verbose = false;
    // Check for the verbose flag in command-line arguments
    for (int i = 1; i < argc; ++i) {
        if (std::string(argv[i]) == "--verbose") {
            verbose = true;
            break;
        }
    }

    std::ifstream infile("input.txt");
    if (!infile) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    std::string line;
    int s = 0;

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        std::vector<int> floors;
        int num;

        while (iss >> num) {
            floors.push_back(num);
        }

        auto result = safe(floors);
        int sr = std::get<0>(result);
        std::string msg = std::get<1>(result);
        int ld = std::get<2>(result);

        s += sr;
        if (verbose){
            std::cout << "sum: " << s << ", ";
            for (const int& floor : floors) {
                std::cout << floor << " ";
            }
            std::cout << msg.c_str() << ", " << ld << std::endl; // Use c_str() to disambiguate
        }
    }

    std::cout << "Final sum: " << s << std::endl;
    return 0;
}
