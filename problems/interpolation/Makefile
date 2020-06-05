CFLAGS = -Wall

plots: lin_plot.svg 

lin_plot.svg: out_lin.txt lin_plot.gpi
	gnuplot lin_plot.gpi

out_lin.txt: linear.py
	python3 $< > $@

clean:
	$(RM) *.txt *.svg
