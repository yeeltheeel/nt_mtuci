from math import log2, ceil
from ipaddress import IPv4Address

address = IPv4Address('10.0.0.0')
prefix = 16
hosts = [150, 700, 30]
hosts.sort(reverse=True)
print('address={}/{}, hosts={}\n'.format(address, prefix, hosts))

n = []
for k in hosts:
	nk = log2(k + 2)
	np = ceil(nk)
	n.append(np)
	print('n={} ({:.4f}) for hosts={}'.format(np, nk, k))
print()

i = 0
masks = []
for k in n:
	p = 32 - k
	mb = '1' * p + '0' * k
	m = IPv4Address(int(mb, 2))
	masks.append(m)
	print('mask={}/{} for hosts={}'.format(m, p, hosts[i]))
	i += 1
print()

i = 0
ip = address
for m in masks:
	p = bin(int(m)).count('1')
	hb = 32 - p
	sn = 2 ** hb
	na = IPv4Address((int(ip) // sn) * sn)
	f = IPv4Address(int(na) + 1)
	bc = IPv4Address(int(na) + sn - 1)
	l = IPv4Address(int(bc) - 1)
	print('net={} for mask={}/{}: \n\tfirst={}, \n\tlast={}, \n\tbroadcast={}'.format(na, m, p, f, l, bc))
	ip = IPv4Address(int(bc) + 1)
	i += 1
