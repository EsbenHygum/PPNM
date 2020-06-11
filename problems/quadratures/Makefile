CFLAGS = -Wall

out.txt: main.py integrater.py
	python3 $< > $@

clean:
	$(RM) *.txt
	$(RM) -r __pycache__
