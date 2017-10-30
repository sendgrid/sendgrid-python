# import deploy config
deployfile=deploy.env
ifdef dpl
deployfile=$(dpl)
endif
include $(deployfile)
export $(shell sed 's/=.*//' $(deployfile))

stop:
	docker-compose stop

rm: stop
	docker-compose stop -fvs

clean:
	docker rmi %(docker images -aq)

clean_untagged:
	docker rmi $(docker images --quiet --filter "dangling=true") 2>/dev/null

build:
	docker-compose up -d

build-build:
	docker-compose up --build -d

up: rm clean build-build
	echo "Sendgrid dev environment is alive :D"
