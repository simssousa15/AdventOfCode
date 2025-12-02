#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

vector<int> run(long long A, vector<int> prog){

    vector<long long> reg = {A, 0, 0};
    vector<int> out;

    int idx = 0;
    bool done = false;
    do{
        //check if any reg negative
        for(auto i : reg){
            if(i < 0){
                cout << "NEGATIVE" << endl;
            }
        }

        long long lit = prog[idx+1];
        long long combo = lit;
        if(combo > 3){
            combo = reg[combo%4];
        }

        switch (prog[idx])
        {
        case 0:
            reg[0] /= static_cast<long long>(std::pow(2,combo));
            // reg[0] /= pow(2,combo);
            break;
        case 1:
            reg[1] ^= lit;
            break;
        case 2:
            reg[1] = combo%8;
            break;
        case 3:
            if(reg[0] != 0){ idx = lit; idx-=2;}
            break;
        case 4:
            reg[1] ^= reg[2];
            break;
        case 5:
            out.push_back(combo%8);
            break;
        case 6:
            reg[1] = reg[0] / static_cast<long long>(std::pow(2,combo));
            // reg[1] = reg[0] / pow(2,combo);
            break;
        case 7:
            reg[2] = reg[0] / static_cast<long long>(std::pow(2,combo));
            // reg[2] = reg[0] / pow(2,combo);
            break;
        default:
            cout << "command not recognized" << endl;
            break;
        }

        idx+=2;
    }while(idx < prog.size() && !done);

    return out;
}

long long dfs(vector<int> prog, long long A){
    vector<int> out;
    A <<= 3;
    for(int i = 0; i < 8; i++){
        out = run(A+i, prog);
        if(equal(prog.end()-out.size(), prog.end(), out.begin())){
            //cout << "found: " << oct << A+i << endl;
            if(out.size() == prog.size()){
                return A+i;
            }
            
            long long ans = dfs(prog, A+i);
            if(ans != -1){
                return ans;
            }
        }
    }
    return -1;
}

int main()
{

    ifstream inputFile("real.txt");
    if (!inputFile)
    {
        cerr << "Unable to open the file!" << std::endl;
        return 1;
    }

    vector<string> text;
    string line;

    while (getline(inputFile, line)){ text.push_back(line); }

    // Close the file
    inputFile.close();

    vector<long long> reg;

    for(int i = 0; i < 3; i++){
        reg.push_back(stoll(text[i].substr(text[i].find(':')+1)));

        cout << *reg.rbegin() << " ";
    }
    cout << endl;

    vector<int>prog;

    string lin = text[4];
    lin = lin.substr(lin.find(':')+2);

    for(int i = 0; i < lin.length(); i+=2){
        prog.push_back(lin[i]-'0');
        cout << *prog.rbegin() << " ";
    }
    cout << endl;


    
    vector<int> out = run(reg[0], prog);
    for(int i = 0; i < out.size(); i++){
        cout << out[i] << ",";
    }
    cout << endl << endl ;

    long long ans = dfs(prog, 0);
    cout << "Ans: " << ans << endl;

    return 0;
}

/*


6562550454257155

*/