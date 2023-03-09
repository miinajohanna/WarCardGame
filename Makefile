PYTHON = python

#--------------------------------------------------------
# Setup a venv and install packages
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
		$(PYTHON) -m pip install -r requirements.txt

installed:
		$(PYTHON) -m pip list

# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

# -----------------------------------------------------
# Test all code at once
#
pylint:
		$(call FOREACH, pylint)

flake8:
		$(call FOREACH, flake8)

lint: flake8 pylint

test:
		$(call FOREACH, test)
