app_name = hw_05

build:
	docker build -t $(app_name) .

run:
	docker run --detach -p 8000:8000 $(app_name)

destroy:
	echo "Ending the container"
	docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker stop

test_container_app:
	python test_docker_app.py
