import cli

cmd2 = '''
ip dhcp excluded-add 192.168.102.1 192.168.102.50
ip dhcp pool DHGI2
network 192.168.102.0 255.255.255.0
default-router 192.168.102.17
domain-name rivancorp.com
dns-server 1.1.1.1
end
'''
cli.configure(cmd2)