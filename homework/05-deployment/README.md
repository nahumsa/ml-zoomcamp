# Homework for week 5

# Question 1

Install Pipenv What's the version of pipenv you installed? (Use --version to find out)

```
version 2022.9.20
```

# Question 2
Use Pipenv to install Scikit-Learn version 1.0.2
What's the first hash for scikit-learn you get in Pipfile.lock?
```
"sha256:08ef968f6b72033c16c479c966bf37ccd49b06ea91b765e1cc27afefe723920b"
```

# Question 3

Let's use these models!

Write a script for loading these models with pickle. Score this client:
```
{"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
```
What's the probability that this client will get a credit card?

- [X] 0.162
- [ ] 0.391
- [ ] 0.601
- [ ] 0.993

You can run the `load_models.py` file to get this result.

# Question 4

Now let's serve this model as a web service

- Install Flask and gunicorn (or waitress, if you're on Windows)
- Write Flask code for serving the model
- Now score this client using requests:

```
url = "YOUR_URL"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
requests.post(url, json=client).json()
```

What's the probability that this client will get a credit card?

- [ ] 0.274
- [ ] 0.484
- [ ] 0.698
- [X] 0.928

You can see the result by running `flask run` in one terminal then running `test_app.py` in another terminal.

# Question 5

Download the base image svizor/zoomcamp-model:3.9.12-slim. You can easily make it by using docker pull command.

So what's the size of this base image?

- [ ] 15 Mb
- [X] 125 Mb
- [ ] 275 Mb
- [ ] 415 Mb

This can be done by using  `docker pull svizor/zoomcamp-model:3.9.12-slim` and `docker images`.

# Question 6

Let's run your docker container!

After running it, score this client once again:
```
url = "YOUR_URL"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
requests.post(url, json=client).json()
```
What's the probability that this client will get a credit card now?

- [ ] 0.289
- [ ] 0.502
- [ ] 0.769
- [X] 0.972

You can run this using the make file: `make build` will build the container `make run` will run the container and `make destroy` will end the container. If you use `make test_container_app` you will run `test_docker_app.py` to see the result of the container, which is `{'model_name': 'ml-zoomcamp', 'model_version': '1', 'probability': 0.9282218018527452}`.
