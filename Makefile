MAS_VERSION := v$(shell grep -oP '(?<=renpy.config.version = ").+(?=")' ./game/0config.rpy)
PATCH_VERSION := $(shell git describe --tags)
ARTIFACT_NAME := DDLC_MAS_JP_$(PATCH_VERSION).zip
ARTIFACT_PATH := $(ARTIFACT_NAME)

all: build

install: ## Install Ren'Py SDK
	./tools/dependencies.sh $(MAS_VERSION)

build: install ## Build and package mods (Default)
	./tools/distribute.sh
ifdef GITHUB_ENV
	@echo 'ARTIFACT_NAME=$(ARTIFACT_NAME)' >> $(GITHUB_ENV)
	@echo 'ARTIFACT_PATH=$(ARTIFACT_PATH)' >> $(GITHUB_ENV)
	@echo 'MAS_VERSION=$(MAS_VERSION)' >> $(GITHUB_ENV)
	@echo 'PATCH_VERSION=$(PATCH_VERSION)' >> $(GITHUB_ENV)
endif

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
