# Description

Projeto 2 de Disciplina TeleInformática e Redes.
Utilizar simulador para SDN com suporte para Openflow - Mininet e criar topologia habilitada para openflow no mininet e fornecer aplicativo que incrementa a segurança em uma rede.
Requisitos mínimos topologia:

- Conter pelo menos um controlador
- 4 switches habilidades para fluxo aberto
- 10 hosts

### aluno

- Ana Paula Nóbrega - 190142120
- Gabriel Cruz Vaz Santos - 200049038
- Nicolas Paulin Benatto - 200025627

# Install Dependencies

To run this project you will need

- Pox

```
$ git clone http://github.com/noxrepo/pox
```

- pip & pyhton3

```
$ sudo apt install -y python3-pip
$ python3 -V
```

- mininet

```
$ sudo apt-get install mininet
$ #mn
```

- confirm if vsswitch is installed with mininet

```
$ sudo apt-get install openvswitch-switch
$ sudo service openvswitch-switch start
```

- if wireshark not installed and references controllers and switches

```
$ git clone https://github.com/mininet/mininet
$ mininet/util/install.sh -fw
```

# Before Project Run

clear mininet cash
`sudo mn -c`

# Run Project

in another terminal run, but inside this project directorry run:

```
$ git clone https://github.com/noxrepo/pox
$ cd pox
$ python3 ./pox.py forwarding.l2_learning
```

inside the project folder run for without security app rules:
`$ sudo mn --custom topology.py --topo customtopology`

inside the project folder run for security app rules remote controller:
`$ sudo mn --custom topology.py --topo customtopology --controller=remote,ip=127.0.0.1,port=6633`

inside the project folder run for use security app rules:

`$ sudo mn --custom topology.py,security_app.py --topo customtopology --controller=securityapp`

another way to run is running as python script:
`sudo python3 topology.py``

# References

- [walkthrough mininet](http://mininet.org/walkthrough/)
- [drive document](https://docs.google.com/document/d/1f0QPhMonsCHjrotPNxG3TVrlpLRyDazT0nE1HL6KgOM/edit)
