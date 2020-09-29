MAS_VERSION := v$(shell grep -oP '(?<=define config.version = ").+(?=")' ./game/options.rpy)
PATCH_VERSION := $(shell git describe --tags)
ARTIFACT_NAME := DDLC_MAS_JP_$(PATCH_VERSION).zip
ARTIFACT_PATH := $(ARTIFACT_NAME)

all: build

install: ## Install Ren'Py SDK
	./tools/dependencies.sh $(MAS_VERSION)

build: install ## Build and package mods (Default)
	./tools/distribute.sh
	@echo '::set-env name=ARTIFACT_NAME::$(ARTIFACT_NAME)'
	@echo '::set-env name=ARTIFACT_PATH::$(ARTIFACT_PATH)'
	@echo '::set-env name=MAS_VERSION::$(MAS_VERSION)'
	@echo '::set-env name=PATCH_VERSION::$(PATCH_VERSION)'

dialogue: dialogue.tab ## Extract dialogue
dialogue.tab: install
	./tools/dialogue.sh $(MAS_VERSION)

check: dialogue.tab ## Check translation
	@python3 ./tools/check_translate.py

clean: ## Remove artifacts
	-rm error_report.tab

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: \
	all \
	install \
	build \
	dialogue \
	check \
	clean \
	help
