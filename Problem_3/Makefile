build:
	docker build -t receiver -f ./Dockerfile.receiver .
	docker build -t sender -f ./Dockerfile.sender .
	docker build -t receiver1 -f ./Dockerfile.receiver1 .

run: build
	docker run --name sender -p 5000:5000 --rm -d sender
	docker run --name receiver -p 5001:5001 --rm -d receiver
	docker run --name receiver1 -p 5002:5002 --rm -d receiver1
	docker network create homework_4
	docker network connect homework_4 sender
	docker network connect homework_4 receiver
	docker network connect homework_4 receiver1

disconnect:
	docker network disconnect homework_4 sender
	docker network disconnect homework_4 receiver
	docker network disconnect homework_4 receiver1

stop: disconnect
	docker stop receiver
	docker stop sender
	docker stop receiver1
	docker network rm homework_4