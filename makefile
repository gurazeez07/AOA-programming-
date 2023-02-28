all: 

run1:
	python3 Strat1.py > output1.txt

run2:
	python3 Strat2.py > output2.txt

run3:
	python3 Strat3.py > output3.txt

run4:
	python3 Strat4.py > output4.txt

clean:
	rm -f output*.txt
