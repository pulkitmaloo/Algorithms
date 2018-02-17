#include<iostream>
using namespace std;

class Rectangle
{
	public:
		int b, h;
		Rectangle(int br, int he)
		{
			b = br;
			h = he;
		}
		int area()
		{
			return b * h;
		}
};

int main()
{
	Rectangle rect = Rectangle(5, 10);
	cout<<rect.area()<<endl;
	return 0;
}