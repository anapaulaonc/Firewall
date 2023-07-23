from pox.core import core
import pox.openflow.libopenflow_01 as of

class SecurityApp(object):
    def __init__(self):
        core.openflow.addListeners(self)

    def _handle_ConnectionUp(self, event):
        # Endereços IP suspeitos que queremos bloquear
        suspicious_ips = ['192.168.0.100', '10.0.0.5']

        # Cria uma regra para bloquear todo o tráfego ICMP (ping)
        icmp_msg = of.ofp_flow_mod()
        icmp_msg.match.dl_type = 0x0800  # IP packets
        icmp_msg.match.nw_proto = 1      # ICMP protocol
        icmp_msg.actions.append(of.ofp_action_output(port=of.OFPP_NONE))  # Drop packet
        event.connection.send(icmp_msg)

        # Cria regras para bloquear tráfego dos endereços IP suspeitos
        for suspicious_ip in suspicious_ips:
            block_msg = of.ofp_flow_mod()
            block_msg.match.dl_type = 0x0800  # IP packets
            block_msg.match.nw_src = suspicious_ip
            block_msg.actions.append(of.ofp_action_output(port=of.OFPP_NONE))  # Drop packet
            event.connection.send(block_msg)

def launch():
    core.registerNew(SecurityApp)
