This is a prototype for a lightweight RESTful API for PolicyBrain.

The Django rest framework is in the `policybrainrest` directory, and the worker
app that takes care of coordinating long-running asynchronous tasks is in
the `worker_app` directory.

Set up your local environment with the following steps:
1. `conda env create`
2. `export DATABASE_USER=your_local_postgres_username`
3. `createdb policybrainrestdb -U $DATABASE_USER`
4. `cd policybrainrest`
5. `python manage.py migrate`
6. `python manage.py runserver`

Everything is working OK if you run:

```
$ curl http://localhost:8000/taxbrainrest/ -d input_specs='{"policy": {"_STD_single": {"2020": [20000.0]}}}'
```

and get output:
```
{"input_specs":"{\"policy\": {\"_STD_single\": {\"2020\": [20000.0]}}}","specs":{"policy":{"2020":{"_STD":[[20000.0,24981.84,12490.92,18736.38,24981.84]]}},"consumption":{},"behavior":{},"growdiff_baseline":{},"growdiff_response":{}},"errors_warnings":{"warnings":"","errors":""}}
```
