#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	long n;
	long result = 0;

	cin >> n;

	while( n > 0 ) {
		if( 0 == ( n & 0x1 ) ) {
			++result;
		}

		n >>= 1;
	}

	cout << ( 1L << result ) << endl;
	return 0;
}
