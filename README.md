# adventofcode
http://adventofcode.com/

http://adventofcode.com/day/1
gcc day1.c
./a.out

http://adventofcode.com/day/2
g++ -std=c++0x wrapping.cpp -o a.out
./a.out

http://adventofcode.com/day/3 with LLVM
clang day3.c -o a.out
./a.out

scan-build gcc -c day3.c
scan-build: Using '/bin/clang' for static analysis
scan-build: Removing directory '/var/folders/rj/6d72t70j18v3_73j79s8gl7m0000gn/T/scan-build-2015-12-06-014752-3685-1' because it contains no reports.
scan-build: No bugs found.

