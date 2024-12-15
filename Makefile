%.ics: %.csv csv_to_ics.py
	python3 ./csv_to_ics.py < $< > $@
