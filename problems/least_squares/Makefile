all: out_ls.txt plot_ls.svg
	cat out_ls.txt

out_ls.txt: main.py least_squares.py qr_decomp.py 
	python3 $< > $@

plot_ls.svg: plot_ls.gpi data.txt out_ls.txt
	gnuplot $<

clean:
	$(RM) data_exp.txt out_ls.txt *.svg
	$(RM) -r __pycache__
