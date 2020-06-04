CSFLAGS = -optimize+ -platform:anycpu
.PHONEY:all
all: out.txt
	cat out.txt

out.txt : main.exe
	mono main.exe > out.txt
main.exe : main.cs
	mcs $(CSFLAGS) -out:main.exe -reference:cmath.dll main.cs 
cmath.dll: complex.cs cmath.cs
	mcs -target:library -out:cmath.dll cmath.cs complex.cs
clean:
	rm --force out.txt main.exe
