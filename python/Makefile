SHELL := /bin/bash
.PHONY: setup test
setup:
	rm -rf env
	python3 -m venv env
	source ./env/bin/activate
test:
	source ./env/bin/activate && python3 -m unittest test_roman_numerals.py
