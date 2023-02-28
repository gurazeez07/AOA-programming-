all: 

run1:
	python3 Strat1.py

run2:
	python3 Strat2.py

run3:
	python3 Strat3.py

run4:
	python3 Strat4.py

time1:
	python Strat1.py < strat1_input_1000.txt
	python Strat1.py < strat1_input_2000.txt
	python Strat1.py < strat1_input_3000.txt
	python Strat1.py < strat1_input_4000.txt
	python Strat1.py < strat1_input_5000.txt

time2:
	python Strat2.py < strat2_input_1000.txt
	python Strat2.py < strat2_input_2000.txt
	python Strat2.py < strat2_input_3000.txt
	python Strat2.py < strat2_input_4000.txt
	python Strat2.py < strat2_input_5000.txt

time3:
	python Strat3.py < strat3_input_1000.txt
	python Strat3.py < strat3_input_2000.txt
	python Strat3.py < strat3_input_3000.txt
	python Strat3.py < strat3_input_4000.txt
	python Strat3.py < strat3_input_5000.txt

time4:
	python Strat4.py < strat4_input_1000.txt > time4.txt
	python Strat4.py < strat4_input_2000.txt > time4.txt
	python Strat4.py < strat4_input_3000.txt > time4.txt
	python Strat4.py < strat4_input_4000.txt > time4.txt
	python Strat4.py < strat4_input_5000.txt > time4.txt

clean:
	rm -f output*.txt
