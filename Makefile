
TARGET=npuzzle
NAME=n-puzzle

.PHONY: all

all: dockerbuild dockerrun

dockerbuild:
	@echo Docker build NPUZZLE image
	@docker build --no-cache -t ${TARGET} .

dockerrun:
	@echo Docker run NPUZZLE container
	@docker run --rm -ti --name=${NAME} -t ${TARGET}