setup:
	pipenv install --dev
	pipenv run pre-commit install


style:
	pipenv run nox -s style

test: style
	pipenv run nox -s tests

fmt:
	pipenv run nox -s fmt

download_data:
	sh download_datasets.sh
