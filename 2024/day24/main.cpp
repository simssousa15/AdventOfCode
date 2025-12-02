#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

struct Operation{
    string el1, el2, op, ans;
};

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

    map<string, bool> wires;
    
    // Create a random number generator
    random_device rd; // Random device to seed the generator
    mt19937 gen(rd()); // Mersenne Twister generator
    uniform_int_distribution<> dis(0, 1); // Distribution between 0 and 1

    int i = 0;
    for(auto l : text){
        if(l.length() < 5){ break; }
        wires[l.substr(0,3)] = dis(gen);
        i++;
    }

    // find z
    long long x = 0;
    long long y = 0;
    for(int i = 0; i < wires.size() / 2; i++){
        string num = to_string(i);
        if(num.length() == 1){ num = "0" + num; }

        if(wires["x" + num]){ x += pow(2, i); }
        if(wires["y" + num]){ y += pow(2, i); }
    }
    
    /*
    Swap z06 and jmq
    Swap z13 and gmh
    Swap z38 and qrh
    Swap rqf and cbd

    // cbd,gmh,jmq,qrh,rqf,z06,z13,z38
    // 
     */

    map<string, string> swaps;
    swaps["z06"] = "jmq";
    swaps["jmq"] = "z06";

    swaps["z13"] = "gmh";
    swaps["gmh"] = "z13";

    swaps["z38"] = "qrh";
    swaps["qrh"] = "z38";

    swaps["rqf"] = "cbd";
    swaps["cbd"] = "rqf";



    queue<Operation>q;
    for(int j = i+1; j < text.size(); j++){
        Operation op;
        auto  l = text[j];

        op.el1 = l.substr(0,3);
        l = l.substr(4);
        op.op = l.substr(0, l.find(' '));
        l = l.substr(l.find(' ')+1);
        op.el2 = l.substr(0,3);
        op.ans = l.substr(7,3);

        if(swaps.find(op.ans) != swaps.end()){
            cout << "Swapping " << op.ans << endl;

            op.ans = swaps[op.ans];
        }

        q.push(op);
    }


    int count = 0;
    while(!q.empty()){

        cout << q.size() << endl;
        auto op = q.front();
        q.pop();

        if(wires.find(op.el1) != wires.end()
        && wires.find(op.el2) != wires.end() ){
            if(op.op == "AND"){
                wires[op.ans] = wires[op.el1] && wires[op.el2];
            }else if(op.op == "XOR"){
                wires[op.ans] = wires[op.el1] != wires[op.el2];
            }else if(op.op == "OR"){
                wires[op.ans] = wires[op.el1] || wires[op.el2];
            }else{
                cout << "Unrecognized operation: " << op.op << endl;
            }

            // cout << op.el1 << " " << op.op << " " << op.el2 << " = " << op.ans << endl;
        }else{
            // cout << "Pushing " << op.el1 << " " << op.op << " " << op.el2 << " = " << op.ans << endl;
            q.push(op);
        }
    }

    long long dec = 0;
    for(auto item : wires){
        // cout << item.first << ": " << item.second << endl;
        if(item.first[0] == 'z' && item.second){
            dec += pow(2, stoll(item.first.substr(1,2)));
        }
    }

    cout << "Part1: " << dec << endl;
    
    //sum x and y
    long long x_dec = 0;
    long long y_dec = 0;
    for(auto item : wires){
        if(item.first[0] == 'x' && item.second){
            x_dec += pow(2, stoll(item.first.substr(1,2)));
        }
        if(item.first[0] == 'y' && item.second){
            y_dec += pow(2, stoll(item.first.substr(1,2)));
        }
    }
    cout << "x+y: " << x_dec + y_dec << endl;

    cout << "----------------" << endl;
    cout << "Part2" << endl;
    cout << "G: " << bitset<50>(x_dec+y_dec).to_string() << endl;  
    cout << "Z: " << bitset<50>(dec).to_string() << endl;

    cout << "diffs" << endl;
    string g = bitset<50>(x_dec+y_dec).to_string();
    string z = bitset<50>(dec).to_string();

    for(int i = 0; i < g.length(); i++){
        if(g[i] != z[i]){
            cout << g.length() - i - 1 << " ";
        }
    }
    cout << endl;

    return 0;
}