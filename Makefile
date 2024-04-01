.PHONY: docs

# Define a required environment variable
SIEVE_SERVER_PATH ?=

# Check if the required variable is set
ifeq ($(SIEVE_SERVER_PATH),)
    $(error Required environment variable SIEVE_SERVER_PATH is not set)
endif

docs:
	python3 $(SIEVE_SERVER_PATH)/api/app/generate_openapi.py docs > docs/openapi.json
	cd docs/ && npx @mintlify/scraping@latest openapi-file openapi.json -o reference-v2/api --overwrite
