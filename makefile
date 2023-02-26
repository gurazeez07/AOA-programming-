CC=g++
CFLAGS=-std=c++11 -Wall -Wextra -O2
PYTHON=python3

all: Strat1 Strat2 Strat3 Strat4

Strat1: Strat1.py
	$(PYTHON) Strat1.py < input.txt > output1.txt

Strat2: Strat2.py
	$(PYTHON) Strat2.py < input.txt > output2.txt

Strat3: Strat3.py
	$(PYTHON) Strat3.py < input.txt > output3.txt

Strat4: Strat4.py
	$(PYTHON) Strat4.py < input.txt > output4.txt

clean:
	rm -f Strat1 Strat2 Strat3 Strat4 output*.txt

