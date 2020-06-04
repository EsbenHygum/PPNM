using System;
using static System.Console;
using static System.Math;
using static cmath;
class main{
	static int Main(){
		complex I = new complex(0,1);
		Write($"sqrt(2)={sqrt(2)}\n");
		Write($"exp(I)={exp(I)}\n");
		Write($"exp(I*PI)={exp(I*PI)}\n");
		complex ipowi = I.pow(I);
		Write($"I.pow(I)={ipowi}\n");
		Write($"sin(I*PI)={sin(I*PI)}\n");
	return 0;
	}
}
