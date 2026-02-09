.PHONY: install run eval

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

run: install
	python3 -m src.pipeline
	python3 -m src.evaluation

eval: install
	python3 -m src.evaluation
