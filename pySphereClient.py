import pysphere
from pysphere import VIServer

username = ""
password = ""
vCenter = ""
vmname = ""

def viConnect(vCenter,username,password,vmname):
	server = VIServer()
	server.connect(vCenter,username,password)
	#print "vCenter: {} User: {} Pass: {}".format(vCenter,username,password)
	#return server
	#print viConnect("192.168.219.129","root","vmware")
	return getVm(server,vmname)
	
def getVm(server,vmname):
	vm = server.get_vm_by_name(vmname)
	properties = vm.get_properties()
	return properties

