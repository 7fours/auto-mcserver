# auto-mcserver

- Deprecated Python script for Minecraft server. Repos for asset files are down but if the files are hosted manually, script still should work.
- I had just started learning classes at this point it seems

### Auto Minecraft Server:
Auto generate a vanilla, paper, fabric, or a premade paper server with plugins preinstalled.

```
usage: generate.py [-h] [-a] [-g] [-v] [-p] [-f] [-c] [-l] [-pb] [-ap] [-vr VERSION]

options:
  -h, --help            show this help message and exit
  -a, --auto-start      auto-start minecraft server after generated
  -g, --gui             enable gui for auto-start (BY DEFAULT OFF, ONLY USE FLAG IF WANTED)
  -v, --vanilla         create vanilla mc server
  -p, --paper           create papermc server
  -f, --fabric          create fabric mc server
  -c, --custom          create premade custom server
  -l, --local           Local server
  -pb, --public         Public server
  -ap, --add-plugins    add custom plugins set without the whole server file
  -vr VERSION, --version VERSION
                        desired version. by default, set to newest available.
```
