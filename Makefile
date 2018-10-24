
TARGET=npuzzle
NAME=n-puzzle

.PHONY: all

all: build

build: test
	pip3 install .

docker: dockerbuild dockerrun

dockerbuild:
	@echo Docker build NPUZZLE image
	@docker build --no-cache -t ${TARGET} .

dockerrun:
	@echo Docker run NPUZZLE container
	@docker run --rm -ti --name=${NAME} -t ${TARGET}

test: clean
	cd tests && pytest -v test.py && cd ..

clean:
	pip3 uninstall npuzzle -y
	rm -rf  rm -rf tests/__pycache__/
	rm -rf  rm -rf .pytest_cache