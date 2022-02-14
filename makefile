
FORCE:

dev:
	pip install -r requirements-dev.txt

tests: FORCE
	pytest

prod: tests
	git commit -a
	git push origin main
