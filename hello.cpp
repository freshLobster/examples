#include <iostream>
#include <iomanip>
#include <ctime>

using namespace std;

string phrase;
char cont = 'y';

void politeResponse(){
			 switch(rand()%3){
                case 0:
                        cout << "hello"<< endl;
                        break;
                case 1:
                        cout << "hey" << endl;
                        break;
                case 2:
                        cout << "hi" << endl;
                        break;
                default: break;
            }
}

int add(int a, int b){
	return a+b;
}

int main(){
	while (cont == 'y'){
	srand(time(0));
	//add(a, b);
	//cout << "Hello" << endl; //output
	cin >> phrase;
	cout << "response to: " << phrase << endl;
	if ( phrase == "hello" || phrase=="hi" || phrase == "hey"){
		politeResponse();
	}else{
		cout << "go die in a hole";	
	}
	cout << "continue?:";
	cin >> cont;
	cout << endl;
}
	return 1;

}


