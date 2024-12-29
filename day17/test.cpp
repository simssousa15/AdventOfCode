#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long A = 6;  // Ensure A is initialized to the value 6
    cout << A << " ";  // Should print 6
    A = A << 3;        // Shifts A left by 3 positions, should multiply A by 8
    cout << A << endl; // Should print 48
    return 0;
}
