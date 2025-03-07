build:
	docker build -t newsimp .

run: build
	docker run --name simp -p 5000:5000 -d --rm newsimp

stop:
	docker stop simp