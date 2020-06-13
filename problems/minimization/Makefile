all: out.txt

out.txt: main.py
	python3 $< > $@

clean: 
	$(RM) -r __pycache__ *.txt
