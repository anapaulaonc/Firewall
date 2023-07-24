from pox.core import core
import pox.openflow.libopenflow_01 as of


def block_handler (event):
    # Endereços IP suspeitos que queremos bloquear
    suspicious_ips = [ '10.0.0.5', '10.0.0.7']
    ipv4 = event.parsed.find('ipv4')
    #
    if not ipv4: return
    #
    if ipv4.srcip in suspicious_ips or ipv4.dstip in suspicious_ips:
      core.getLogger("blocker").debug("Blocked IP %s <-> %s", ipv4.srcip, ipv4.dstip)

      event.halt = True

def launch ():

  # Listen to packet events
  core.openflow.addListenerByName("PacketIn", block_handler)
