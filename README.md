## Powered by Mintlify


# Sieve Documentation
[Docs](https://docs.sievedata.com)
[Mintlify](https://mintlify.com)

## Developing
```bash
npm i -g mintlify@latest
cd docs && mintlify dev
```

API docs are generated from our OpenAPI spec. Run `make docs` with `SIEVE_API_URL` set to regenerate API documentation.

## TODO
* Add some docs about `yield` vs `return`
    * We currently `yield` in many of the walkthroughs, but no detailed explanations 
* Potentially add some more details about default values and `kwargs`
* Add more detail to autoscaling section after redesign (@wizgrao)
* Add section on file caching behavior (@aupadhyay)
* Describe error handling / split out function lifecycle when implemented (@aupadhyay)
* Fix error codes section once consolidated in code
* Webhook structure is confusing (2 sections)
