build:
	docker build -t receiver -f ./Dockerfile.receiver .
	docker build -t sender -f ./Dockerfile.sender .

run: build
	docker run --name sender -p 5000:5000 --rm -d sender
	docker run --name receiver -p 5001:5001 --rm -d receiver

startup: run
	docker network create homework_4
	docker network connect homework_4 sender
	docker network connect homework_4 receiver

disconnect:
	docker network disconnect homework_4 sender
	docker network disconnect homework_4 receiver

stop:
	docker stop receiver
	docker stop sender

cleanup: disconnect stop
	docker network rm homework_4