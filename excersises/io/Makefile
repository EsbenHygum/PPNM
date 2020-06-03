all: out-cmdline.txt out-stdout.txt out-fileio.txt out-stderr.txt

INPUT=input.txt

out-cmdline.txt: cmdline.exe $(INPUT) Makefile
	mono $< 1 2 3 > $@              # overwrite the file with stdout
	mono $< $$(cat $(INPUT)) >> $@  # append, not overwrite

out-fileio.txt: fileio.exe $(INPUT) Makefile
	mono $< $(INPUT) $@


out-stdout.txt out-stderr.txt: stdinouterr.exe $(INPUT) Makefile
	mono $< <$(INPUT) >out-stdout.txt 2>out-stderr.txt
	cat $(INPUT) | mono $< >>out-stdout.txt  2>>out-stderr.txt

cmdline.exe     : cmdline.cs     ; mcs $<
stdinouterr.exe : stdinouterr.cs ; mcs $<
fileio.exe      : fileio.cs      ; mcs $<

clean:
	$(RM) *.exe out* input.txt

$(INPUT): Makefile
	/bin/echo -e '0.5\n2.5\n3.5' > $@

