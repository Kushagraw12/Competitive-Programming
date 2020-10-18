//KUSHAGRA WADHWA
#include <iostream>
using namespace std;

int kush;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int testcase;
    cin >> testcase;

    int test_case = 1;

    while (testcase--)
    {

        cin >> ::kush;

        int a[::kush][::kush];

        for (int i = 0; i < ::kush; i++)
            for (int k = 0; k < ::kush; k++)
                cin >> a[i][k];

        int ms = 0, s = 0;
        int i, k;

        //for rows
        for (int x = 0; x < ::kush; x++)
        {
            s = 0;
            i = x;
            k = 0;
            while (i < ::kush && k < ::kush)
            {
                s += a[i++][k++];
            }

            if (s > ms)
                ms = s;
        }

        //for columns
        for (int y = 0; y < ::kush; y++)
        {
            s = 0;
            i = 0;
            k = y;
            while (i < ::kush && k < ::kush)
            {
                s += a[i++][k++];
            }

            if (s > ms)
                ms = s;
        }

        cout << "Case #" << test_case++ << ": " << ms << "\n";
    }
    return 0;
}