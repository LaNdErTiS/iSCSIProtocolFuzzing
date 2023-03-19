import gdb
import sys
import os

# import gdb_utils from the current directory
sys.path.append(os.getcwd())
import gdb_utils

brk_function = 'discovery_sendtargets'
program_name = '/home/initiator/Desktop/open-iscsi-2.1.3/usr/iscsiadm'
arguments = '-m discovery -t st -p localhost'


# get new fuzz string
def get_fuzz_string(data_len):
    fuzz_string = ''
    for i in range(data_len):
        fuzz_string += 'A'
    return fuzz_string


# set new data at fields
def change_data(num, data_len):
    if (num == 1):
        fs = get_fuzz_string(data_len)
        print('change: name = ' + fs)
        gdb.execute('set variable iface.name = \"' + fs + '\"')
    elif (num == 2):
        print('change: iface_num =', data_len)
        gdb.execute('set variable iface.iface_num = ' + str(data_len))
    elif (num == 3):
        fs = get_fuzz_string(data_len)
        print('change: netdev = ' + fs)
        gdb.execute('set variable iface.netdev = \"' + fs + '\"')
    elif (num == 4):
        fs = get_fuzz_string(data_len)
        print('change: ipaddress = ' + fs)
        gdb.execute('set variable iface.ipaddress = \"' + fs + '\"')
    elif (num == 5):
        fs = get_fuzz_string(data_len)
        print('change: subnet_mask = ' + fs)
        gdb.execute('set variable iface.subnet_mask = \"' + fs + '\"')
    elif (num == 6):
        fs = get_fuzz_string(data_len)
        print('change: gateway = ' + fs)
        gdb.execute('set variable iface.gateway = \"' + fs + '\"')
    elif (num == 7):
        fs = get_fuzz_string(data_len)
        print('change: bootproto = ' + fs)
        gdb.execute('set variable iface.bootproto = \"' + fs + '\"')
    elif (num == 8):
        fs = get_fuzz_string(data_len)
        print('change: ipv6_linklocal = ' + fs)
        gdb.execute('set variable iface.ipv6_linklocal = \"' + fs + '\"')
    elif (num == 9):
        fs = get_fuzz_string(data_len)
        print('change: ipv6_router = ' + fs)
        gdb.execute('set variable iface.ipv6_router = \"' + fs + '\"')
    elif (num == 10):
        fs = get_fuzz_string(data_len)
        print('change: ipv6_autocfg = ' + fs)
        gdb.execute('set variable iface.ipv6_autocfg = \"' + fs + '\"')
    elif (num == 11):
        fs = get_fuzz_string(data_len)
        print('change: linklocal_autocfg = ' + fs)
        gdb.execute('set variable iface.linklocal_autocfg = \"' + fs + '\"')
    elif (num == 12):
        fs = get_fuzz_string(data_len)
        print('change: router_autocfg = ' + fs)
        gdb.execute('set variable iface.router_autocfg = \"' + fs + '\"')
    elif (num == 13):
        print('change: prefix_len =', data_len)
        gdb.execute('set variable iface.prefix_len = ' + str(data_len))
    elif (num == 14):
        print('change: vlan_id =', data_len)
        gdb.execute('set variable iface.vlan_id = ' + str(data_len))
    elif (num == 15):
        print('change: vlan_priority =', data_len)
        gdb.execute('set variable iface.vlan_priority = ' + str(data_len))
    elif (num == 16):
        fs = get_fuzz_string(data_len)
        print('change: vlan_state = ' + fs)
        gdb.execute('set variable iface.vlan_state = \"' + fs + '\"')
    elif (num == 17):
        fs = get_fuzz_string(data_len)
        print('change: state = ' + fs)
        gdb.execute('set variable iface.state = \"' + fs + '\"')
    elif (num == 18):
        print('change: mtu =', data_len)
        gdb.execute('set variable iface.mtu = ' + str(data_len))
    elif (num == 19):
        print('change: port =', data_len)
        gdb.execute('set variable iface.port = ' + str(data_len))
    elif (num == 20):
        fs = get_fuzz_string(data_len)
        print('change: delayed_ack = ' + fs)
        gdb.execute('set variable iface.delayed_ack = \"' + fs + '\"')
    elif (num == 21):
        fs = get_fuzz_string(data_len)
        print('change: nagle = ' + fs)
        gdb.execute('set variable iface.nagle = \"' + fs + '\"')
    elif (num == 22):
        fs = get_fuzz_string(data_len)
        print('change: tcp_wsf_state = ' + fs)
        gdb.execute('set variable iface.tcp_wsf_state = \"' + fs + '\"')
    elif (num == 23):
        print('change: tcp_wsf =', data_len)
        gdb.execute('set variable iface.tcp_wsf = ' + str(data_len))
    elif (num == 24):
        print('change: tcp_timer_scale =', data_len)
        gdb.execute('set variable iface.tcp_timer_scale = ' + str(data_len))
    elif (num == 25):
        fs = get_fuzz_string(data_len)
        print('change: tcp_timestamp = ' + fs)
        gdb.execute('set variable iface.tcp_timestamp = \"' + fs + '\"')
    elif (num == 26):
        fs = get_fuzz_string(data_len)
        print('change: dhcp_dns = ' + fs)
        gdb.execute('set variable iface.dhcp_dns = \"' + fs + '\"')
    elif (num == 27):
        fs = get_fuzz_string(data_len)
        print('change: dhcp_slp_da = ' + fs)
        gdb.execute('set variable iface.dhcp_slp_da = \"' + fs + '\"')
    elif (num == 28):
        fs = get_fuzz_string(data_len)
        print('change: tos_state = ' + fs)
        gdb.execute('set variable iface.tos_state = \"' + fs + '\"')
    elif (num == 29):
        print('change: tos =', data_len)
        gdb.execute('set variable iface.tos = ' + str(data_len))
    elif (num == 30):
        fs = get_fuzz_string(data_len)
        print('change: gratuitous_arp = ' + fs)
        gdb.execute('set variable iface.gratuitous_arp = \"' + fs + '\"')
    elif (num == 31):
        fs = get_fuzz_string(data_len)
        print('change: dhcp_alt_client_id_state = ' + fs)
        gdb.execute('set variable iface.dhcp_alt_client_id_state = \"' + fs + '\"')
    elif (num == 32):
        fs = get_fuzz_string(data_len)
        print('change: dhcp_alt_client_id = ' + fs)
        gdb.execute('set variable iface.dhcp_alt_client_id = \"' + fs + '\"')
    elif (num == 33):
        fs = get_fuzz_string(data_len)
        print('change: dhcp_req_vendor_id_state = ' + fs)
        gdb.execute('set variable iface.dhcp_req_vendor_id_state = \"' + fs + '\"')
    elif (num == 34):
        fs = get_fuzz_string(data_len)
        print('change: dhcp_vendor_id_state = ' + fs)
        gdb.execute('set variable iface.dhcp_vendor_id_state = \"' + fs + '\"')
    elif (num == 35):
        fs = get_fuzz_string(data_len)
        print('change: dhcp_vendor_id = ' + fs)
        gdb.execute('set variable iface.dhcp_vendor_id = \"' + fs + '\"')
    elif (num == 36):
        fs = get_fuzz_string(data_len)
        print('change: dhcp_learn_iqn = ' + fs)
        gdb.execute('set variable iface.dhcp_learn_iqn = \"' + fs + '\"')
    elif (num == 37):
        fs = get_fuzz_string(data_len)
        print('change: fragmentation = ' + fs)
        gdb.execute('set variable iface.fragmentation = \"' + fs + '\"')
    elif (num == 38):
        fs = get_fuzz_string(data_len)
        print('change: incoming_forwarding = ' + fs)
        gdb.execute('set variable iface.incoming_forwarding = \"' + fs + '\"')
    elif (num == 39):
        print('change: ttl =', data_len)
        gdb.execute('set variable iface.ttl = ' + str(data_len))
    elif (num == 40):
        fs = get_fuzz_string(data_len)
        print('change: gratuitous_neighbor_adv = ' + fs)
        gdb.execute('set variable iface.gratuitous_neighbor_adv = \"' + fs + '\"')
    elif (num == 41):
        fs = get_fuzz_string(data_len)
        print('change: redirect = ' + fs)
        gdb.execute('set variable iface.redirect = \"' + fs + '\"')
    elif (num == 42):
        fs = get_fuzz_string(data_len)
        print('change: mld = ' + fs)
        gdb.execute('set variable iface.mld = \"' + fs + '\"')
    elif (num == 43):
        print('change: flow_label =', data_len)
        gdb.execute('set variable iface.flow_label = ' + str(data_len))
    elif (num == 44):
        print('change: traffic_class =', data_len)
        gdb.execute('set variable iface.traffic_class = ' + str(data_len))
    elif (num == 45):
        print('change: hop_limit =', data_len)
        gdb.execute('set variable iface.hop_limit = ' + str(data_len))
    elif (num == 46):
        print('change: nd_reachable_tmo =', data_len)
        gdb.execute('set variable iface.nd_reachable_tmo = ' + str(data_len))
    elif (num == 47):
        print('change: nd_rexmit_time =', data_len)
        gdb.execute('set variable iface.nd_rexmit_time = ' + str(data_len))
    elif (num == 48):
        print('change: nd_stale_tmo =', data_len)
        gdb.execute('set variable iface.nd_stale_tmo = ' + str(data_len))
    elif (num == 49):
        print('change: dup_addr_detect_cnt =', data_len)
        gdb.execute('set variable iface.dup_addr_detect_cnt = ' + str(data_len))
    elif (num == 50):
        print('change: router_adv_link_mtu =', data_len)
        gdb.execute('set variable iface.router_adv_link_mtu = ' + str(data_len))
    elif (num == 51):
        print('change: def_task_mgmt_tmo =', data_len)
        gdb.execute('set variable iface.def_task_mgmt_tmo = ' + str(data_len))
    elif (num == 52):
        fs = get_fuzz_string(data_len)
        print('change: header_digest = ' + fs)
        gdb.execute('set variable iface.header_digest = \"' + fs + '\"')
    elif (num == 53):
        fs = get_fuzz_string(data_len)
        print('change: data_digest = ' + fs)
        gdb.execute('set variable iface.data_digest = \"' + fs + '\"')
    elif (num == 54):
        fs = get_fuzz_string(data_len)
        print('change: immediate_data = ' + fs)
        gdb.execute('set variable iface.immediate_data = \"' + fs + '\"')
    elif (num == 55):
        fs = get_fuzz_string(data_len)
        print('change: initial_r2t = ' + fs)
        gdb.execute('set variable iface.initial_r2t = \"' + fs + '\"')
    elif (num == 56):
        fs = get_fuzz_string(data_len)
        print('change: data_seq_inorder = ' + fs)
        gdb.execute('set variable iface.data_seq_inorder = \"' + fs + '\"')
    elif (num == 57):
        fs = get_fuzz_string(data_len)
        print('change: data_pdu_inorder = ' + fs)
        gdb.execute('set variable iface.data_pdu_inorder = \"' + fs + '\"')
    elif (num == 58):
        print('change: erl =', data_len)
        gdb.execute('set variable iface.erl = ' + str(data_len))
    elif (num == 59):
        print('change: max_recv_dlength =', data_len)
        gdb.execute('set variable iface.max_recv_dlength = ' + str(data_len))
    elif (num == 60):
        print('change: first_burst_len =', data_len)
        gdb.execute('set variable iface.first_burst_len = ' + str(data_len))
    elif (num == 61):
        print('change: max_out_r2t =', data_len)
        gdb.execute('set variable iface.max_out_r2t = ' + str(data_len))
    elif (num == 62):
        print('change: max_burst_len =', data_len)
        gdb.execute('set variable iface.max_burst_len = ' + str(data_len))
    elif (num == 63):
        fs = get_fuzz_string(data_len)
        print('change: chap_auth = ' + fs)
        gdb.execute('set variable iface.chap_auth = \"' + fs + '\"')
    elif (num == 64):
        fs = get_fuzz_string(data_len)
        print('change: bidi_chap = ' + fs)
        gdb.execute('set variable iface.bidi_chap = \"' + fs + '\"')
    elif (num == 65):
        fs = get_fuzz_string(data_len)
        print('change: strict_login_comp = ' + fs)
        gdb.execute('set variable iface.strict_login_comp = \"' + fs + '\"')
    elif (num == 66):
        fs = get_fuzz_string(data_len)
        print('change: discovery_auth = ' + fs)
        gdb.execute('set variable iface.discovery_auth = \"' + fs + '\"')
    elif (num == 67):
        fs = get_fuzz_string(data_len)
        print('change: discovery_logout = ' + fs)
        gdb.execute('set variable iface.discovery_logout = \"' + fs + '\"')
    elif (num == 68):
        fs = get_fuzz_string(data_len)
        print('change: port_state = ' + fs)
        gdb.execute('set variable iface.port_state = \"' + fs + '\"')
    elif (num == 69):
        fs = get_fuzz_string(data_len)
        print('change: port_speed = ' + fs)
        gdb.execute('set variable iface.port_speed = \"' + fs + '\"')
    elif (num == 70):
        fs = get_fuzz_string(data_len)
        print('change: hwaddress = ' + fs)
        gdb.execute('set variable iface.hwaddress = \"' + fs + '\"')
    elif (num == 71):
        fs = get_fuzz_string(data_len)
        print('change: transport_name = ' + fs)
        gdb.execute('set variable iface.transport_name = \"' + fs + '\"')
    elif (num == 72):
        fs = get_fuzz_string(data_len)
        print('change: alias = ' + fs)
        gdb.execute('set variable iface.alias = \"' + fs + '\"')
    elif (num == 73):
        fs = get_fuzz_string(data_len)
        print('change: iname = ' + fs)
        gdb.execute('set variable iface.iname = \"' + fs + '\"')


# check data len
def check_len(num, data_len):
    ISCSI_MAX_IFACE_LEN = 65
    ISCSI_MAX_STR_LEN = 80
    ISCSI_HWADDRESS_BUF_SIZE = 18
    ISCSI_TRANSPORT_NAME_MAXLEN = 16
    TARGET_NAME_MAXLEN = 256
    IFNAMSIZ = 16
    NI_MAXHOST = 1024
    UINT32_T_MAX = 4294967295
    UINT16_T_MAX = 65535
    UINT8_T_MAX = 255

    if (num == 1):
        if (data_len + 1 == ISCSI_MAX_IFACE_LEN):
            return False
        else:
            return True
    elif (num in (2, 43, 44, 46, 47, 48, 50, 59, 60, 62)):
        if (data_len + 1 == UINT32_T_MAX):
            return False
        else:
            return True
    elif (num == 3):
        if (data_len + 1 == IFNAMSIZ):
            return False
        else:
            return True
    elif (num in (4, 5, 6, 8, 9, 10, 11, 12)):
        if (data_len + 1 == NI_MAXHOST):
            return False
        else:
            return True
    elif (num in (
    7, 16, 17, 20, 21, 22, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 52, 53, 54, 55, 56, 57, 63,
    64, 65, 66, 67, 68, 69)):
        if (data_len + 1 == ISCSI_MAX_STR_LEN):
            return False
        else:
            return True
    elif (num in (13, 15, 23, 24, 29, 39, 45, 49, 58)):
        if (data_len + 1 == UINT8_T_MAX):
            return False
        else:
            return True
    elif (num in (14, 18, 19, 51, 61)):
        if (data_len + 1 == UINT16_T_MAX):
            return False
        else:
            return True
    elif (num == 70):
        if (data_len + 1 == ISCSI_HWADDRESS_BUF_SIZE):
            return False
        else:
            return True
    elif (num == 71):
        if (data_len + 1 == ISCSI_TRANSPORT_NAME_MAXLEN):
            return False
        else:
            return True
    elif (num in (72, 73)):
        if (data_len + 1 == TARGET_NAME_MAXLEN):
            return False
        else:
            return True


# start: load executable program
gdb.execute('file ' + program_name)
# start:set shapshot breakpoint
gdb.execute('break ' + brk_function)
# start:run with arguments
gdb.execute('r ' + arguments)

i = 1  # loop iteration
num = 1  # element in struct iface_rec
data_len = 0  # length of new data


while True:
    # first
    gdb.execute('checkpoint ' + str(i))
    i += 1
    # second
    gdb.execute('checkpoint ' + str(i))
    # third
    gdb.execute("restart " + str(i - 1))

    print('fuzz loop: ' + str(i))

    # set new data
    change_data(num, data_len)
    # set new data_len or take next elem
    if (check_len(num, data_len) == True):
        data_len += 1
    else:
        data_len = 0
        if (num == 73):
            num = 1
        else:
            num += 1

    # continue execution until the end of the function
    gdb.execute('finish')
    # check if the program has crashed
    if gdb_utils.execute_output('info checkpoints')[0] == 'No checkpoints.':
        print('#########')
        print('# Error:The program has crashed!')
        print('########')
        gdb.execute('quit')
    # restore snapshot
    # go to check 2
    gdb.execute("restart " + str(i))
    # delete check 1
    gdb.execute("delete checkpoint " + str(i - 1))
