ARGUMENTS=$(filter-out $@,$(MAKECMDGOALS)) $(filter-out --,$(MAKEFLAGS))
include *.mk

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete
	-find . -type f -name "behave.log" -delete
	-find ./results/ -type f -not -name '.gitignore' -delete
	-find ./reports/ -type f -not -name '.gitignore' -delete
	-rm -fr ./allure_report/
	-rm -fr ./tests/smoke/reports/*.xml

pep8:
	flake8 .

format:
	@isort --recursive .
	@black .

TEST_ENV ?= DEV

smoke_tests:
	behave --format=allure_behave.formatter:AllureFormatter --outfile=results --no-skipped --format progress3 --logging-filter=-root --stop --tags=~@wip --tags=~@skip --tags=~@fixme tests/smoke/features ${TAGS}

smoke_tests_feature:
	behave --format=allure_behave.formatter:AllureFormatter --outfile=results_${FEATURE_DIR}/ --junit --junit-directory=./reports/ --no-skipped --format pretty --logging-filter=-root --tags=~@wip ./tests/smoke/features/${FEATURE_DIR}.feature || true
requirements_smoke:
	pip install -r requirements_smoke.txt

requirements_tests_shared:
	pip install -r ./requirements.txt

compile_requirements_smoke:
	@rm -fr requirements_smoke.txt
	python3 -m piptools compile --quiet requirements_smoke.in
	@sed -i 's/^\-e file.*/\-e ./' requirements_smoke.txt

compile_requirements_test_tools:
	@rm -fr requirements_test_tools.txt
	python3 -m piptools compile --quiet requirements_test_tools.in

compile_requirements_tests_shared:
	@rm -fr ./requirements.txt
	python3 -m piptools compile --quiet --no-annotate --output-file ./requirements.txt ./requirements.in

compile_all_requirements: compile_requirements_tests_shared compile_requirements_smoke compile_requirements_test_tools

find_duplicated_scenario_names: SHELL:=/usr/bin/env bash  # set shell for this target to bash
find_duplicated_scenario_names:
	@diff -u <(behave $(ARGUMENTS) --dry --no-source --no-summary --no-snippets | grep 'Scenario' | sort) \
		<(behave $(ARGUMENTS) --dry --no-source --no-summary --no-snippets | grep 'Scenario' | sort -u)

serve:
	@echo Allure
	@allure --version
	@allure serve results/

report:
	@echo Allure
	@allure --version
	@allure generate --clean --output ./allure_report results/

.PHONY: build clean smoke_tests report
