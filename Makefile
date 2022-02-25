install:
	poetry install

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc

brain-even:
	poetry run brain-even

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
