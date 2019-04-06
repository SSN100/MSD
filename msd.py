import numpy as np
f = open ("com_200.xvg", 'r')
g = open("msd_200.xvg", "w+")
#h = open("diffusion.xvg", "w+")
timestep=0.02
nfreq=5000
dt=nfreq*timestep
#conv_length=0.1 # Angstrom to nm
conv_time=0.001 # ps to ns
com = np.genfromtxt(f, usecols=(1, 2, 3))
#print com
n = eval(input("Enter number of frames :"))
net_frame=int((n-1)/2)
msd = np.empty(net_frame)
d = np.empty(3)
#print(np.size(com, axis=0))--11002 for 2ms run.
for i in range(net_frame):
	sum = 0.0
	for j in range(1, (n-i)):
		d[:] = com[j, :]-com[i+j, :]
		sum = sum + np.dot(d, d)
	msd[i] = sum/(n-i)

	print("msd is done for %s frame.." %i)
	a = i*dt*conv_time
	b = msd[i]
#	c = 6.0*i*dt*conv_time
	g.write("%10.3f %14.5f\n" % (a, b))
	#h.write("%10.3f %14.5f\n" % (a, b/c))
#print msd
