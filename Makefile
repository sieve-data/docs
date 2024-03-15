.PHONY: docs

docs:
	curl $$SIEVE_API_URL/openapi.json > docs/openapi.json
	cd docs/ && npx @mintlify/scraping@latest openapi-file openapi.json -o reference-v2/api --overwrite
