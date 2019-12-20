.PHONY: install watch build publish clean tests coverage flake8

all: clean tests coverage flake8

venv: requirements.txt requirements-dev.txt 
	virtualenv -p python3 venv --no-site-packages
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install -r requirements-dev.txt
	touch venv

install:
	test -n "$(VIRTUAL_ENV)"
	pip install -e .

publish:
	test -n "$(VIRTUAL_ENV)"
	rm -rf dist/
	python3 setup.py sdist bdist_wheel
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

docker-image:
	docker build \
		--build-arg APT_EXTRA_PACKAGES="xterm" \
		-t multipy:pytput \
		https://github.com/essembeh/multipy.git

docker-test:
	docker run \
		--rm \
		-it \
		--volume $(PWD):/src:ro \
		-e GIT_CLEAN=1 \
		-e TOXENV -e TOX_SKIP_ENV \
		multipy:pytput -- -x
