LIB_NAME = library_name
SRC = $(LIB_NAME).c
HEADER = $(LIB_NAME).h
SO_FILE = $(LIB_NAME).so
WRAPPER_SCRIPT = generate_wrapper.py
PY_WRAPPER = $(LIB_NAME)_wrapper.py

all: $(SO_FILE) $(PY_WRAPPER)

$(SO_FILE): $(SRC)
	@gcc -shared -fPIC -o $(SO_FILE) $(SRC) -lm
	@echo "Compiled shared library: $(SO_FILE)"

$(PY_WRAPPER): $(HEADER) $(SO_FILE) $(WRAPPER_SCRIPT)
	@python $(WRAPPER_SCRIPT)
	@echo "Generated Python wrapper: $(PY_WRAPPER)"

clean:
	@rm -f $(SO_FILE) $(PY_WRAPPER)
	@echo "Cleaned up build files"
