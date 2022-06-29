# Setup with docker-compose

`For development only`

## Pre-install

- Docker Engine >= 18.06.0 (`docker --version`)
- Docker compose (`docker-compose --version`)

## Steps

- Copy `.env.sample`

```bash
cp .env.sample .env
```

- Run the containers:

```bash
make run-dev
```

or

```bash
docker-compose -f docker-compose.dev.yml up -d
```

If there are new packages installed:

```bash
docker-compose -f docker-compose.dev.yml up -d --build --force-recreate
```

- go to `http://127.0.0.1:8888/`
- admin page `http://127.0.0.1:8888/admin/`

- Run tests

```bash
docker-compose exec web pytest
```

- Create admin user

```bash
docker-compose exec web python manage.py createsuperuser
```

- DB GUI

  You may use [pgAdmin](https://www.pgadmin.org/) or [DBeaver](https://dbeaver.io/) and the connection would be like the following. <br />
  Make sure the port is in consistant with `DISFACTORY_BACKEND_DEFAULT_DB_DEV_PORT` in `.env` and set the database to `disfactory_data` or check the setting `Show all databases` in the PostgreSQL tab ![image](https://i.imgur.com/8V1nDia.png)

- Stop containers

```bash
docker-compose -f docker-compose.dev.yml down
```

If you want to also purge your testing database, stop the containers and remove the corresponding volumes in the host

```bash
docker-compose -f docker-compose.dev.yml down --rmi all --volumes
rm -rf /tmp/disfactory_d*
```

## Other commands

- See logs

```bash
docker-compose logs --tail 100 -f web

```

- Go into the running container

```bash
docker-compose exec web bash

```


# (Optional) Use IDEs

You may want to use IDEs to boost your productivity. This session collects how we set up our IDEs.

Tips: It will help a lot if you know how to set up your development via command line when you switch between different 
IDEs. For example, from PyCharm to VS Code, or in the other way around. Make sure you understand each set-up step 
of your IDE, and try to reproduce it with commands in command line.

## PyCharm

PyCharm support npm and django runners together. This fits our project very much since our project uses vue.js for 
frontend and django for backend.

### Setting npm debugger for Frontend

- Run --> Edit Configurations --> + (Add New Configuration) --> npm
- Fill in necessary information required to launch frontend
  - tip: In "Before launch", add "Open Browser" so PyCharm will open the browser with JavaScript debugger of 
    PyCharm. This is very handy!
  - See [this reference](https://www.jetbrains.com/help/pycharm/run-debug-configuration-npm.html) if you need more detailed instructions
- Use "Run" to launch frontend if you simply want to run the frontend
- Use "Debug" to launch frontend if you want to use breakpoints to debug interactively.

#### Source Entry Points

Put your breakpoints in the functions you are interested in.

- On creating ohshown event
  - See `CreateFactorySteps.vue` --> `createComponent` --> `setup()`
- Select location
  - See function `chooseLocation` in `CreateFactorySteps.vue` --> `createComponent`
- On clicking "Next step" of page 3
  - `CreateFactorySteps.vue` --> `createComponent` --> `setup()`
- Submit
  - `index.ts` --> `createFactory`

#### Troubleshooting

- Many feature is only supported by PyCharm Pro
- Necessary PyCharm plugins
  - [JavaScript Debugger](https://www.jetbrains.com/help/pycharm/configuring-javascript-debugger.html)
- Optional PyCharm plugins but may be handy
  - [Live Edit in Node.js applications](https://www.jetbrains.com/help/pycharm/live-editing-in-node-js-applications.html)
- Chrome is supported for debugging of JavaScript code with PyCharm Pro. See the details of ["Configuring JavaScript 
  debugger"](https://www.jetbrains.com/help/pycharm/configuring-javascript-debugger.html)

### Setting Django debugger for Backend

When launching Django, I use docker-compose in this case.

- Run --> Edit Configurations --> + (Add New Configuration) --> Django
  - Setting docker-compose
    - You need to tell PyCharm where is your docker daemon
    - You need to tell PyCharm where is your docker-compose yaml
    - You need to tell PyCharm which service of docker-compose you want to launch
      - I launched all services in command line, and then let PyCharm to take care of the following "web service" 
        up and down.
- Fill in necessary information required to launch backend
- Use "Run" to launch process if you simply want to run the process
- Use "Debug" to launch process if you want to use breakpoints to debug interactively.

#### Source Entry Points

- On submitting ohshown event
  - see `backend/api/views/factories_cr.py`
  - `cr` means `crud`. So you will find `factories_u.py` as well.
  - Refactoring work is waiting for your contribution! Refactoring from `factories_` to `ohshown_events_`.
- Edit the django admin console
  - see `ohshown_event.py`

#### Troubleshooting

- Many feature is only supported by PyCharm Pro
- Setup docker-compose is a bit tricky. The key is to tell PyCharm where if your docker-compose execute and mapping 
  the path inside/outside the container correctly.
