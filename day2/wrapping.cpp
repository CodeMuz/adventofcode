#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

const vector<string> explode(const string& s, const char& c)
{
    string buff = "";
    vector<string> v;
    
    for(auto n:s)
    {
        if(n != c) buff+=n; else
        if(n == c && buff != "") { v.push_back(buff); buff = ""; }
    }
    if(buff != "") v.push_back(buff);
    
    return v;
}

int getWrappingQuanitity(int length, int width, int height){
    
    int areas[3];
    int smallest = INT_MAX;
    int paper = 0;
    
    areas[0] = (length * width);
    areas[1] = (length * height);
    areas[2] = (height * width);    

    for(int i = 0; i <= 2; i++){
        if(areas[i] < smallest){
            smallest = areas[i];
        }
        paper += (areas[i] * 2);
    }
    
    paper += smallest;
    
    return paper;
}

int getRibbonLength(int length, int width, int height){

  int ribbon = 0;
  int bow = 0;

  int d[3];
  d[0] = length;
  d[1] = width;
  d[2] = height;

  std::sort(std::begin(d), std::end(d));

  ribbon += (2 * d[0]) + (2 * d[1]);

  bow += (length * width * height);

  ribbon += bow;

  return ribbon;
}

int main () {
    string line;
    ifstream myfile ("input.txt");
    if (myfile.is_open())
    {
        int totalPaper = 0;        
        int totalRibbon = 0;
        while ( getline (myfile,line) )
        {

            string l = line;

            vector<string> v = explode(l, 'x');
            int count = 0;
            int length;
            int width;
            int height;
            
            for(auto n:v){
                switch(count){
                    case(0):
                    length = std::stoi(n);
                    break;
                    case(1):
                    width = std::stoi(n);
                    break;
                    case(2):
                    height = std::stoi(n);
                    break;
                }
                
                count++;
                
            }
            
            totalPaper += getWrappingQuanitity(length, width, height);
            totalRibbon += getRibbonLength(length, width, height);
        }
        cout << "totalPaper = ";
        cout << totalPaper << endl;
        cout << "totalRibbon = ";
        cout << totalRibbon << endl;

        myfile.close();
    }
    
    else cout << "Unable to open file";
    
    return 0;
}
