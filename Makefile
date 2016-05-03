# GabbiExample Makefile
## Test and run all examples that are automated and build documents
#### &copy Martyn Bristow 2016

## Requires
### markdown: sudo pip install markdown

GABBI_TESTS 	:= api.py samples.py webapp.py
UNITTESTS       := test_server.py
BUILD_DIR		:= _build

SOURCES			:= $(wildcard *.md)
OUTPUTS		    := $(SOURCES:.md=.html)

REQUIREPIP      := markdown

README          := README.md

.PHONY: all docs install clean help debug tests

all: clean docs readme tests

$(OUTPUTS): %.html: %.md 
	@echo "Compiling:" $<
	python -m markdown $< > $@          

buildlocation:
	@echo "Create Build Directory:"
	@echo $(BUILD_DIR)
	@mkdir -p $(BUILD_DIR)

docs: testmd buildlocation $(OUTPUTS)
	@echo "Documentation Built"

readme: testmd
	@echo "Compiling readme to README.html"
	python -m markdown $(README) > README.html

help:
	@echo "Help: gabbi-examples"
	@echo " testmd    - Compile Documents"
	@echo " clean     - Remove built documents"
	@echo " debug     - See what will get compiled"
	@echo " install   - Install dependancies locally"

clean:
	@echo "Cleaning localy built files:"
	@rm -rf $(BUILD_DIR)
	@rm -rf $(SOURCE_DIR)/*.html # This is a bit OTT but I have had html files built here by mistake
	@rm -rf *.html
	@rm -rf *.log

debug:
	@echo "INPUT_DOCS"
	@echo $(SOURCES)
	@echo "BUILD_INSTRUCTION"
	@echo $(OUTPUTS)

install:
	@echo "Installing dependancies to user directory"
	pip install markdown --user
	pip install gabbi --user

testmd:
	@echo "Test Markdown is installed"
	python -c "import markdown"

unittests:
	python $(UNITTESTS)

%.py:
	@echo ""

$(GABBI_TESTS):%.py
	python $@

tests: $(GABBI_TESTS)
	