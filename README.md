1. Download the project from GitHub.
2. Add to the file c:\Windows\System32\Drivers\etc\hosts(Windows) or /etc/hosts (Nginx) the string `127.0.0.1 matiushyn.dev.run`
3. From the project folder need to run two commands to build docker container  
  a) `docker build --tag=hello_world .`  
  b) `docker run -p 80:80 --rm --name=hello_world -it hello_world`
4. To run python test send a command from the project folder: `python3 hello_world_test.py`
