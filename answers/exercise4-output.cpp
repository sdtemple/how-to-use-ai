// Use Ctrl + I to translate some Python code into R code
// Notice that in this script, we do not have the same linter coloring
// as in Python scripts because these are Python code snippets inside
// a C++ script. However, the chatbot will be able to translate the code.

// Your instruction to the chatbot will be
// I am an experienced Python programmer, and therefore implemented my code in Python.
// However, I have collaborators who prefer C++ because it can be faster or more memory efficient.
// Please translate the following Python code into C++ code.

// Translated from the provided Python into modern C++ (C++17+)

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>

int isqrt_int(int n) {
    if (n <= 0) return 0;
    int r = static_cast<int>(std::sqrt(static_cast<double>(n)));
    while ((long long)(r + 1) * (r + 1) <= n) ++r;
    while ((long long)r * r > n) --r;
    return r;
}

std::vector<int> sieve_eratosthenes(int limit) {
    if (limit < 2) return {};
    std::vector<unsigned char> sieve(limit + 1, 1);
    sieve[0] = sieve[1] = 0;
    int r = isqrt_int(limit);
    for (int p = 2; p <= r; ++p) {
        if (sieve[p]) {
            for (int j = p * p; j <= limit; j += p)
                sieve[j] = 0;
        }
    }
    std::vector<int> primes;
    primes.reserve(limit / 10 + 10);
    for (int i = 2; i <= limit; ++i)
        if (sieve[i]) primes.push_back(i);
    return primes;
}

std::vector<int> sieve_atkin(int limit) {
    if (limit < 2) return {};
    std::vector<unsigned char> sieve(limit + 1, 0);
    int r = isqrt_int(limit);
    for (int x = 1; x <= r; ++x) {
        int xx = x * x;
        for (int y = 1; y <= r; ++y) {
            int yy = y * y;
            int n = 4 * xx + yy;
            if (n <= limit) {
                int m = n % 12;
                if (m == 1 || m == 5) sieve[n] = !sieve[n];
            }
            n = 3 * xx + yy;
            if (n <= limit && (n % 12) == 7) sieve[n] = !sieve[n];
            n = 3 * xx - yy;
            if (x > y && n <= limit && (n % 12) == 11) sieve[n] = !sieve[n];
        }
    }

    std::vector<int> primes;
    if (limit >= 2) primes.push_back(2);
    if (limit >= 3) primes.push_back(3);

    // Eliminate squares of primes
    for (int i = 5; i <= r; ++i) {
        if (sieve[i]) {
            int step = i * i;
            for (int k = step; k <= limit; k += step)
                sieve[k] = 0;
        }
    }
    for (int i = 5; i <= limit; ++i)
        if (sieve[i]) primes.push_back(i);

    return primes;
}

std::vector<int> first_ten_primes_eratosthenes() {
    int limit = 30;
    auto primes = sieve_eratosthenes(limit);
    while ((int)primes.size() < 10) {
        limit *= 2;
        primes = sieve_eratosthenes(limit);
    }
    primes.resize(10);
    return primes;
}

std::vector<int> first_ten_primes_atkin() {
    int limit = 30;
    auto primes = sieve_atkin(limit);
    while ((int)primes.size() < 10) {
        limit *= 2;
        primes = sieve_atkin(limit);
    }
    primes.resize(10);
    return primes;
}

int main() {
    auto erat_primes = first_ten_primes_eratosthenes();
    auto atkin_primes = first_ten_primes_atkin();

    std::cout << "Eratosthenes first ten primes: [";
    for (size_t i = 0; i < erat_primes.size(); ++i) {
        if (i) std::cout << ", ";
        std::cout << erat_primes[i];
    }
    std::cout << "]\n";

    std::cout << "Atkin       first ten primes: [";
    for (size_t i = 0; i < atkin_primes.size(); ++i) {
        if (i) std::cout << ", ";
        std::cout << atkin_primes[i];
    }
    std::cout << "]\n";

    bool match = (erat_primes == atkin_primes);
    std::cout << "Match: " << (match ? "true" : "false") << "\n";

    // Optional: fail if they differ
    assert(match && "The two sieves produced different results");

    return match ? 0 : 1;
}