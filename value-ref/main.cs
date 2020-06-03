class main{
	static int Main(){
	sprint.print();
	var y=new writer();
	var x=y;
	y.s="new string\n";	
	x.print();
	y.print();
	return 0;
	}
}

public static class sprint{
	static string s="Hello from print\n";
	static public void print(){
		System.Console.Write(s);
	}
}

public struct swriter{
	public string s;
	public swriter(string input){s=input;}
	public void print(){
		System.Console.Write(s);
	}
}

public class writer{
	public string s="Hello from write\n";
	public void print(){
		System.Console.Write(s);
	}
}


