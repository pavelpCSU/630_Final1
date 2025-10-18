
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>
#include <random>
#include <numeric>
#include <algorithm>
#include <iomanip>
#include <nlohmann/json.hpp>
#include "solution.hpp"

using json = nlohmann::json;
using namespace std::chrono;

struct TestCase {
    std::vector<int> nums1;
    std::vector<int> nums2;
    double expected;
};

struct TestResult {
    bool passed;
    double result;
    double expected;
    std::vector<double> times;
    size_t total_size;
};

TestCase load_test_case(const std::string& input_file, const std::string& output_file) {
    std::string base_dir = "/workspaces/630-final-project-Bob12345/";
    std::ifstream input(base_dir + input_file);
    std::ifstream output(base_dir + output_file);
    if (!input || !output) {
        throw std::runtime_error("Failed to open test files: " + base_dir + input_file);
    }
    json input_json, output_json;
    input >> input_json;
    output >> output_json;
    TestCase test;
    test.nums1 = input_json["nums1"].get<std::vector<int>>();
    test.nums2 = input_json["nums2"].get<std::vector<int>>();
    test.expected = output_json["median"].get<double>();
    return test;
}

TestCase generate_test_case(size_t size1, size_t size2, const std::string& case_type) {
    TestCase test;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(-1000000, 1000000);
    if (case_type == "random") {
        test.nums1.resize(size1);
        test.nums2.resize(size2);
        std::generate(test.nums1.begin(), test.nums1.end(), [&]() { return dis(gen); });
        std::generate(test.nums2.begin(), test.nums2.end(), [&]() { return dis(gen); });
        std::sort(test.nums1.begin(), test.nums1.end());
        std::sort(test.nums2.begin(), test.nums2.end());
    }
    // ...other case types omitted for brevity...
    std::vector<int> merged;
    merged.insert(merged.end(), test.nums1.begin(), test.nums1.end());
    merged.insert(merged.end(), test.nums2.begin(), test.nums2.end());
    std::sort(merged.begin(), merged.end());
    size_t total = merged.size();
    if (total % 2 == 0) {
        test.expected = (merged[total/2 - 1] + merged[total/2]) / 2.0;
    } else {
        test.expected = merged[total/2];
    }
    return test;
}

TestResult run_test(Solution& solution, const TestCase& test, int test_num, const std::string& test_type) {
    TestResult result;
    result.total_size = test.nums1.size() + test.nums2.size();
    std::cout << "Running Test " << test_num << std::endl;
    std::cout << "Input sizes: " << test.nums1.size() << " and " << test.nums2.size() << std::endl;
    const int iterations = 10;
    const int repeat_per_sample = 1000000;
    for (int w = 0; w < 3; ++w) {
        volatile double warm = solution.findMedianSortedArrays(test.nums1, test.nums2);
        (void)warm;
    }
    for (int i = 0; i < iterations; ++i) {
        auto start = high_resolution_clock::now();
        double last_result = 0.0;
        for (int r = 0; r < repeat_per_sample; ++r) {
            last_result = solution.findMedianSortedArrays(test.nums1, test.nums2);
        }
        auto end = high_resolution_clock::now();
        result.result = last_result;
        double avg_time_ns = duration_cast<nanoseconds>(end - start).count() / static_cast<double>(repeat_per_sample);
        result.times.push_back(avg_time_ns);
    }
    auto min_time = *std::min_element(result.times.begin(), result.times.end());
    auto max_time = *std::max_element(result.times.begin(), result.times.end());
    auto avg_time = std::accumulate(result.times.begin(), result.times.end(), 0.0) / iterations;
    std::vector<double> sorted_times = result.times;
    std::sort(sorted_times.begin(), sorted_times.end());
    double med_time = sorted_times[sorted_times.size() / 2];
    if (sorted_times.size() % 2 == 0)
        med_time = (sorted_times[sorted_times.size()/2 - 1] + sorted_times[sorted_times.size()/2]) / 2.0;
    double mean = avg_time;
    double sq_sum = std::inner_product(result.times.begin(), result.times.end(), result.times.begin(), 0.0);
    double std_time = std::sqrt(sq_sum / result.times.size() - mean * mean);
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Min: " << min_time << " ns" << std::endl;
    std::cout << "Max: " << max_time << " ns" << std::endl;
    std::cout << "Avg: " << avg_time << " ns" << std::endl;
    std::cout << "Med: " << med_time << " ns" << std::endl;
    std::cout << "Std: " << std_time << " ns" << std::endl;
    std::cout << "(Each timing sample is averaged over " << repeat_per_sample << " repetitions)" << std::endl;
    result.expected = test.expected;
    result.passed = std::abs(result.result - result.expected) < 1e-6;
    std::cout << (result.passed ? "\u2705" : "\u274c") << " Test " << test_num << (result.passed ? " PASSED" : " FAILED") << std::endl;
    return result;
}

int main() {
    Solution solution;
    int test_num = 1;
    std::vector<std::pair<std::string, std::string>> test_cases = {
        {"data/p3/input_1.json", "data/p3/output_1.json"},
        {"data/p3/input_2.json", "data/p3/output_2.json"},
        {"data/p3/input_3.json", "data/p3/output_3.json"}
    };
    for (const auto& [input_file, output_file] : test_cases) {
        auto test = load_test_case(input_file, output_file);
        run_test(solution, test, test_num++, "file");
    }
    std::vector<std::tuple<size_t, size_t, std::string>> generated_cases = {
        {50000, 50000, "random"},
        {100000, 100000, "random"},
        {200000, 200000, "random"},
        {400000, 400000, "random"},
        {800000, 800000, "random"}
    };
    for (const auto& [size1, size2, case_type] : generated_cases) {
        auto test = generate_test_case(size1, size2, case_type);
        run_test(solution, test, test_num++, case_type);
    }
    return 0;
}
