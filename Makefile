################ INITIALISATION ################

data/iris.csv:
	wget -P data/ https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv;
	dvc add data -f pipeline/data.dvc;

## Get the IRIS dataset
get-data: data/iris.csv

outputs/:
	mkdir outputs;

TAGS = $(shell git tag;)
remote/: outputs/ get-data
	for tag in $(TAGS); do \
		make -s recreate-experiment-$$tag; \
		git checkout master; \
    done

## Create a local folder as if it was an external remote
create-remote: remote/

recreate-experiment-%:
	@echo $(*:recreate-experiment-%=%) ; \
    git checkout $(*:recreate-experiment-%=%); \
	dvc repro; \
	git add .; \
	git commit -m "$(*:recreate-experiment-%=%)"; \
	git tag -d $(*:recreate-experiment-%=%); \
	git tag -a $(*:recreate-experiment-%=%) -m "commitMessage"; \
	dvc push;

################ EXPERIMENT HANDLING ################

file-sending:
	git add model/*.py pipeline/*.dvc Dvcfile;
	git status;
	read -p "[tagName] Enter the experiment name: " tagName; \
	read -p "[commitMessage] Explain what you actually did: " commitMessage; \
	git commit -a -m "$$commitMessage"; \
	git tag -a "$$tagName" -m "$$commitMessage";

data-sending: file-sending
	dvc push;

DATA_CONSISTENCY = $(shell dvc status | grep "Nothing to reproduce.";)
data-consistency-check:
ifeq ($(DATA_CONSISTENCY),)
		@echo "Aborting the creation of a new experiment... Run 'dvc repro' to generate data associated with the current source code";
		exit 0;
else
		make -s data-sending;
endif

## Create a new experiment
experiment: data-consistency-check

## Visualize all experiments
visualize: create-remote
	@dvc pull -T pipeline/evaluate.dvc;
	@dvc metrics show -T;

## Go back to an experiment
goback-%: create-remote
	@git checkout $(*:goback-%=%);
	@dvc pull;

################ HELP ################

help:
	@echo "Available rules:"
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=20 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}'

