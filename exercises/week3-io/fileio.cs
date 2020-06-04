using System;
using System.IO;
class fileio{
static int Main(string[] args){
	if(args.Length < 2)return 1;
	string infile  = args[0];
	string outfile = args[1];
	StreamReader instream  = new StreamReader(infile);
	StreamWriter outstream = new StreamWriter(outfile,append:false);
	outstream.WriteLine("# x sin(x)");
	do{
		string line=instream.ReadLine();
		if(line==null)break;
		string[] words=line.Split(' ',',','\t');
		foreach(var word in words){
			double x=double.Parse(word);
			outstream.WriteLine(
				"{0} {1}",x,Math.Sin(x)
				);	
			}
		}while(true);
	outstream.Close();
	instream.Close();
return 0;
}//Main
}//class
