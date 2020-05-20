MULTIPY_TAG := multipy:$(shell basename $(PWD))
MULTIPY_APT_DEPENDENCIES := "xterm"


.PHONY: clean test build install publish publish-test docker-image docker-test

all: build

clean:
	rm -vfr \
		dist/ build/ \
		.coverage 

venv: requirements.txt requirements-dev.txt 
	test -d venv || virtualenv -p python3 venv --no-site-packages
	bash -c "source venv/bin/activate && \
		pip install -r requirements.txt -r requirements-dev.txt"
	touch venv

install: venv
	bash -c "source venv/bin/activate && \
		pip install -e ."

test: venv clean
	bash -c "source venv/bin/activate && \
		tox"

build: test
	bash -c "source venv/bin/activate && \
		python3 setup.py sdist bdist_wheel"

publish-test: build
	bash -c "source venv/bin/activate && \
		twine upload --repository-url https://test.pypi.org/legacy/ dist/*"

publish: build
	bash -c "source venv/bin/activate && \
		twine upload --repository-url https://upload.pypi.org/legacy/ dist/*"

docker-image:
	docker build \
		--build-arg APT_EXTRA_PACKAGES=$(MULTIPY_APT_DEPENDENCIES) \
		-t $(MULTIPY_TAG) \
		https://github.com/essembeh/multipy.git

docker-test:
	docker run \
		--rm \
		-it \
		--volume $(PWD):/src:ro \
		-e GIT_CLEAN=1 \
		-e TOXENV -e TOX_SKIP_ENV \
		$(MULTIPY_TAG) -- -x
