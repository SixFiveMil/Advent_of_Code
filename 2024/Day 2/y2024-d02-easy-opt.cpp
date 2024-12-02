#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <tuple>
#include <string>

// Function to check if sorted and calculate largest adjacent distance in one pass
std::tuple<bool, bool, bool, int> analyze_vector(const std::vector<int>& nums) {
    bool is_sorted_asc = true;
    bool is_sorted_desc = true;
    bool has_adjacent_equal = false;
    int max_distance = 0;

    for (size_t i = 0; i < nums.size() - 1; ++i) {
        if (nums[i] > nums[i + 1]) is_sorted_asc = false;
        if (nums[i] < nums[i + 1]) is_sorted_desc = false;
        if (nums[i] == nums[i + 1]) has_adjacent_equal = true;

        int distance = std::abs(nums[i] - nums[i + 1]);
        if (distance > max_distance) max_distance = distance;

        // Early exit if no sort order is valid
        if (!is_sorted_asc && !is_sorted_desc) break;
    }

    return {is_sorted_asc, is_sorted_desc, has_adjacent_equal, max_distance};
}

std::tuple<int, std::string, int> safe(const std::vector<int>& nums) {
    if (nums.size() < 2) return {0, "is unsafe due to insufficient elements", 0};

    std::tuple<bool, bool, bool, int> analysis = analyze_vector(nums);
    bool is_sorted_asc = std::get<0>(analysis);
    bool is_sorted_desc = std::get<1>(analysis);
    bool has_adjacent_equal = std::get<2>(analysis);
    int max_distance = std::get<3>(analysis);


    if (!is_sorted_asc && !is_sorted_desc) {
        return {0, "is unsafe order", 0};
    }

    if (has_adjacent_equal) {
        return {0, "is unsafe due to adjacent equal elements", 0};
    }

    if (max_distance <= 3) {
        return {1, "is Safe distance", max_distance};
    } else {
        return {0, "is unsafe distance", max_distance};
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
    int total_safe = 0;

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        std::vector<int> nums;
        int num;

        while (iss >> num) {
            nums.push_back(num);
        }

    std::tuple<int, std::string, int> result = safe(nums);
    int safe_status = std::get<0>(result);
    std::string message = std::get<1>(result);
    int largest_dist = std::get<2>(result);
        total_safe += safe_status;

        if (verbose) {
            std::cout << "sum: " << total_safe << ", ";
            for (const int& value : nums) {
                std::cout << value << " ";
            }
            std::cout << message << ", " << largest_dist << std::endl;
        }
    }

    // Always print the final sum
    std::cout << "Final sum: " << total_safe << std::endl;
    return 0;
}
