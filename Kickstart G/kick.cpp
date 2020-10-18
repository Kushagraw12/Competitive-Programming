// KUSHAGRA WADHWA
#include <iostream>
using namespace std;

int solution(string x)
{
    int kc = 0, fc = 0;

    for (int j = 0; j < x.length(); j++)
    {
        if (x[j] == 'K' && x[j + 1] == 'I' && x[j + 2] == 'C' && x[j + 3] == 'K')
        {

            kc++;
            continue;
        }

        if (x[j] == 'S' && x[j + 1] == 'T' && x[j + 2] == 'A' && x[j + 3] == 'R' && x[j + 4] == 'T')
        {

            fc = fc + kc;
        }
    }

    return fc;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int testcase;
    cin >> testcase;
    int test_case = 1;
    while (testcase--)
    {
        string st;
        cin >> st;

        int ans = solution(st);

        cout << "Case #" << test_case++ << ": " << ans << "\n";
    }
    return 0;
}