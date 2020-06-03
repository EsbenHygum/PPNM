CSFLAGS = -optimize+ -platform:arm
.PHONEY:all
all: out.txt
	cat out.txt

out.txt : hello.exe
	mono hello.exe > out.txt
main.exe : hello.cs
	mcs $(CSFLAGS) -out:hello.exe hello.cs
clean:
	rm --force out.txt hello.exe
