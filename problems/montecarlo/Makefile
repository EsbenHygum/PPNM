all: out.txt plot.svg
	cat $<


plot.svg: plot.gpi convergence.txt
	gnuplot plot.gpi

out.txt: main.py montecarlo.py
	python3 $< > $@


clean:
	$(RM) out.txt convergence.txt conv.svg
	rm -rf __pycache__
