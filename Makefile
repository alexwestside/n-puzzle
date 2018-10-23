
TARGET=npuzzle

.PHONY: all

all: dockerbuild dockerrun

dockerbuild:
	docker build --no-cache -t ${TARGET} .

dockerrun:
	docker run -t ${TARGET}