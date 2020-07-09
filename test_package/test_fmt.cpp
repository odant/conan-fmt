#include <fmt/core.h>

#include <string>
#include <cstdlib>


int main() {
    const std::string result = fmt::format("The answer is {}.\n", 42);
    fmt::print(result);
    return EXIT_SUCCESS;
}
