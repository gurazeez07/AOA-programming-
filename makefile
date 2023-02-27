all: 

run1:
	python Strat1.py > output1.txt

run2:
	python Strat2.py > output2.txt

run3:
	python Strat3.py > output3.txt

run4:
	python Strat4.py > output4.txt

clean:
	rm -f output*.txt
