using System;
using static System.Console;
class epsilon{
	static void Main(){
		int i=1; while(i+1>i) {i++;}
		Write("my max int = {0}\n",i);
		int n = int.MaxValue;
		Write("int.MaxValue = {0}\n",n);

		int j=1; while(j-1<j) {j--;}
		Write("my min int = {0}\n",j);
		int m = int.MinValue;
		Write("int.MinValue = {0}\n",m);

		double x=1; while(1+x!=1){x/=2;} x*=2;
		float y=1F; while((float)(1F+y) != 1F){y/=2F;} y*=2F;
		Write("machine epsilon double = {0}\n",x);
		double t = System.Math.Pow(2, -52);
		Write("2 raised by -52 = {0}\n",t);
		System.Console.Write("machine epsilon float = {0}\n",y);
		double r = System.Math.Pow(2, -23);
		Write("2 raised by -23 = {0}\n",r);			
				
	}
}
