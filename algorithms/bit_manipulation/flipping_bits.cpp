#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	unsigned int x;
	int count;

	cin >> count;

	for( int i = 0; i < count; ++i ) {
		cin >> x;
		cout << ~x << endl;
	}

	return 0;
}
