all: run plt_orbit.svg plt_sir.svg plt_sir2.svg

run: main.py sir_model.py solver.py
	python3 $< > $@
	python3 sir_model.py >> $@
	python3 sir_model2.py >> $@

plt_orbit.svg: plt_orbit.gpi run
	gnuplot $<

plt_sir.svg: plt_sir.gpi run
	gnuplot $<

plt_sir2.svg: plt_sir2.gpi run
	gnuplot $<

clean: 
	$(RM) -r __pycache__ *.svg
