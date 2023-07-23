from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI

class CustomTopology:
    def __init__(self):
        self.net = Mininet(controller=Controller, switch=OVSSwitch)
        self.create_topology()

    def create_topology(self):
        c0 = self.net.addController('c0', controller=Controller)

        # Adiciona quatro switches
        s1 = self.net.addSwitch('s1', protocols='OpenFlow13')
        s2 = self.net.addSwitch('s2', protocols='OpenFlow13')
        s3 = self.net.addSwitch('s3', protocols='OpenFlow13')
        s4 = self.net.addSwitch('s4', protocols='OpenFlow13')

        # Adiciona dez hosts
        h1 = self.net.addHost('h1')
        h2 = self.net.addHost('h2')
        h3 = self.net.addHost('h3')
        h4 = self.net.addHost('h4')
        h5 = self.net.addHost('h5')
        h6 = self.net.addHost('h6')
        h7 = self.net.addHost('h7')
        h8 = self.net.addHost('h8')
        h9 = self.net.addHost('h9')
        h10 = self.net.addHost('h10')

        # Conecta hosts ao switch central (controlador)
        self.net.addLink(h1, s1)
        self.net.addLink(h2, s2)
        self.net.addLink(h3, s2)
        self.net.addLink(h4, s3)
        self.net.addLink(h5, s3)
        self.net.addLink(h6, s3)
        self.net.addLink(h7, s4)
        self.net.addLink(h8, s4)
        self.net.addLink(h9, s4)
        self.net.addLink(h10, s4)

        # Conecta os switches à controladora
        self.net.addLink(s1, c0)
        self.net.addLink(s2, c0)
        self.net.addLink(s3, c0)
        self.net.addLink(s4, c0)

    def start_topology(self):
        self.net.start()
        CLI(self.net)

    def stop_topology(self):
        self.net.stop()

if __name__ == '__main__':
    custom_topology = CustomTopology()
    custom_topology.start_topology()
