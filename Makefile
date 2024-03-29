install:
	poetry install

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

brain-prime:
	poetry run brain-prime

brain-progression:
	poetry run brain-progression

build:  clean install
	poetry build

publish:
	poetry publish --dry-run

package-install: build
	python3 -m pip install --user dist/*.whl

lint:   install
	poetry run flake8 brain_games

clean:
	-rm dist/*.tar.gz dist/*.whl
