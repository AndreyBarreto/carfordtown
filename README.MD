## Desafio

Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

Requirements

* Setup the dev environment with docker
* Using docker-compose with as many volumes as it takes
* Use Python’s Flask framework and any other library
* Use any SQL database
* Secure routes
* Write tests


Time to deliver, 72 hours.

### Como RODAR

- Create an .env in the main project scope can be exactly the same as .env.example

- To run you need docker and docker-compose , run this command "docker-compose up -d --build" which will generate our image and our containers too

```
docker-compose up -d --build
```

- Routes are authenticated in the header by x-access-token


### Routes


- /people ['POST'] (protected) body {name}

- /car/id_people ['POST'] (protected) body{color,model}

- /register ['POST'] body {username, password}

- /auth ['POST'] body {username, password}


