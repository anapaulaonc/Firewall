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
$git clone https://github.com/mininet/mininet
$ mininet/util/install.sh -fw
```

# Before Project Run

clear mininet cash
`sudo mn -c`

# Run Project

in another terminal run:

```
$ cd Pox
$ python3 ./pox.py forwarding.l2_learning
```

inside the project folder run:
`$ sudo mn --custom topology.py --topo customtopology --controller=remote,ip=127.0.0.1,port=6633`

# References

- [walkthrough mininet](http://mininet.org/walkthrough/)
- [drive document](https://docs.google.com/document/d/1f0QPhMonsCHjrotPNxG3TVrlpLRyDazT0nE1HL6KgOM/edit)
- [install python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-22-04-server)
- [videos Reference](https://www.youtube.com/playlist?list=PLpherdrLyny8YN4M24iRJBMCXkLcGbmhY)
