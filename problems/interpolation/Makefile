CFLAGS = -Wall

plots: lin_plot.svg quad_plot.svg

lin_plot.svg: out_lin.txt lin_plot.gpi
	gnuplot lin_plot.gpi

quad_plot.svg: quad.py out_quad.txt quad_plot.gpi
	gnuplot quad_plot.gpi

out_lin.txt: linear.py
	python3 $< > $@

out_quad.txt: quad.py
	python3 $< > $@

clean:
	$(RM) *.txt *.svg
