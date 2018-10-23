
TARGET=npuzzle
NAME=n-puzzle

.PHONY: all

all:
	pip3 install .

clean:
	pip3 uninstall npuzzle -y

docker: dockerbuild dockerrun

dockerbuild:
	@echo Docker build NPUZZLE image
	@docker build --no-cache -t ${TARGET} .

dockerrun:
	@echo Docker run NPUZZLE container
	@docker run --rm -ti --name=${NAME} -t ${TARGET}