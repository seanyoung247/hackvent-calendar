# hackvent-calendar

Hackvent calendar is a website providing interview style coding challenges each day over the course of Decemeber in an Advent calendar style.

In late 2021 I was involved in a hackathon with a theme of the festive holidays. My team produced a coding advent calendar that can be seen deployed here: [hackvent calendar](https://manni8436.github.io/hackvent-calendar/), which went on to get first place in the hackathon. It was a great achievement by all involved, and a great idea well executed, especially since it was written over the course of a weekend.

This project is to continue that one and take it further.

The intention is to provide a fun community project, and provide an opportunity to learn and try something new with Code Institute community members building the site. Plus offering a bit of friendly competition with leaderboards for the challenges.

Shared under the GPL3 licence.

## Planned Features
Ideally the site should provide interview style coding challenges, one per day between 1st and 25th of December, in different difficulty levels (easy, medium, and hard) and completable in the two languages CI teaches as part of it's fullstack course: Python and JavaScript. There should be leaderboards for each challenge in each language and for different aspects. For instance quickest to complete, code golf (fewest lines/characters), most performant etc.

An MVP should hopefully aim provide the bare minimum features:
- Easy challenges
- JavaScript language support
- Safe in browser code execution
- Top ten first to complete leaderboard for each challenge
- An overall top ten leaderboard

## Design
### UI
TBD
### System
The current design uses a modular pluggable Python-Flask server and API backend with a React frontend. User code execution will be on the users browser. To protect against malicious code, user submissions are injected into a sandboxed iframe to prevent access to the enclosing page, cookies and other user data. The code is then further encapsulated into a webworker, seperating it entirely from the DOM and running it in it's own thread to prevent DoS style attacks (such as infinite loops). Workers are killed after 2 seconds without responce. 

## Contributing
For outstanding issues please see: TBC

TBC
Format etc.
### Environment setup
As a React/Flask app the project has certain build and runtime dependencies and requirements:

#### Overview
- Root Directory: The root directory holds the main flask server file (app.py), deployment files, README.md and helper scripts
  - requirements.txt: Python dependencies list
  - runtime.txt: The targeted python runtime
Server modules:
- challenges: holds files for the challenges server API module.
- reactsrv: holds files for serving the react frontend files.
Front end:
- react-src: React source code
  - package.json: React/NPM dependecies list and build settings
- frontend: Compiled frontend code

#### Setup
To setup the environment for development both python and Javascript environments must be prepared using Pip and NPM respectively.
The general procedure for this on Unix/like systems (MacOS, Linux, Gitpod, etc):
- Setup python environment:
  - From the project root, create a new python environment with venv: `python3 -m venv venv`
  - Activate the python environment: `. venv/bin/activate`
  - Install python dependencies: python `pip install -r requirements.txt`
- Setup frontend environment:
  - Go to the react source folder: `cd react-arc`
  - Install dependencies with NPM: `npm install`
  - Return to root: `cd ..`

These steps are incorporated into the setupEnv.sh script for convienience. You can run it from the project root with the command: `./setupEnv.sh`.
You may need to make the script executable on your system, which can be achieved with the following command: `chmod +x setupEnv.sh`

### Running in development
#### Server and API
The server and API is a flask based python app. Once dependencies are installed and the python environment activated it can be started using the command `flask run` from the root directory. The compiled version of the frontend UI can then be accessed from port 5000 on the localhost.
#### Frontend
Further a live testing React environment for the react frontend can be run. To do this, after starting the flask API as above, navigate to the react source folder from another terminal window and type the command: `npm start`. A React live test will then be available from port 3000, and will automatically communicate with the already started flask API.

## Deployment
### Project Build
Prior to deployment the current project state must be built for deployment.
#### Frontend
Prior to deployment the current frontend state should be compiled to the frontend folder. This can be achieved by:
- Navigate to the react source folder (react-src)
- Run the build command: `npm run build`
The latest frontend state will now be compiled and saved to the frontend folder.

#### Backend
TBD
### Deployment
TBC