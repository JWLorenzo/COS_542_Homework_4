build:
	docker build -t receiver -f ./Dockerfile_receiver .
	docker build -t sender -f ./Dockerfile_sender .

run: build
	docker run --name sender -p 5000:5000 --rm -d sender
	docker run --name receiver -p 5001:5001 --rm -d receiver

startup: run
	docker network create homework_4
	docker network connect homework_4 sender
	docker network connect homework_4 receiver

build_alt:
	docker build -t receiver1 -f ./Dockerfile_receiver1 .

run_alt: run build_alt
	docker run --name receiver1 -p 5002:5002 --rm -d receiver1

startup_alt: startup run_alt
	docker network connect homework_4 receiver1

disconnect:
	docker network disconnect homework_4 sender
	docker network disconnect homework_4 receiver

disconnect_alt: disconnect
	docker network disconnect homework_4 receiver1

stop:
	docker stop receiver
	docker stop sender

stop_alt: stop
	docker stop receiver1

cleanup: disconnect stop
	docker network rm homework_4

cleanup_alt: disconnect_alt stop_alt
	docker network rm homework_4