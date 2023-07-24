from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mininet.topo import Topo

class CustomTopology(Topo):
    def build(self):
        #c0 = self.net.addController('c0', controller=Controller)

        root = self.addSwitch('s0')

        # Adiciona quatro switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Adiciona dez hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')

        # Conecta hosts ao switch central (controlador)
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s2)
        self.addLink(h4, s3)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)
        self.addLink(h8, s4)
        self.addLink(h9, s4)
        self.addLink(h10, s4)
        
        #Conecta switches aos switches
        self.addLink(root, s1)
        self.addLink(root, s2)
        self.addLink(root, s3)
        self.addLink(root, s4)

topos = { 'customtopology': CustomTopology }


