# -*- coding: utf-8 -*-

class Protocol(object):
	def __init__(self):
		self.parameters = {}

	def setParameters(self, parameters):
		self.parameters = parameters

	def setModel(self, model):
		index = model.find(':')
		if (index >= 0):
			self.model = model[0:index]
		else:
			self.model = model

	def methods(self):
		return 0

	def stringParameter(self, name, defaultValue = ''):
		if name in self.parameters:
			return self.parameters[name]
		return defaultValue

	def intParameter(self, name, min, max):
		value = self.stringParameter(name, None)
		if value == None:
			return min
		try:
			value = int(value)
		except:
			return min
		if value < min:
			return min
		if value > max:
			return max
		return value

	def convertToRaw(self, name, value):
		if (self.protocol == 'arctech' or self.protocol == 'waveman'):
			if (self.model == 'codeswitch'):
				if (name == 'house'):
					return ord(value[0])-ord('A')
				elif (name == 'unit'):
					return int(value)
			else:
				return value #this might be 'E', ' ' or 'H' too

		if (self.protocol == 'x10'):
			if (name == 'house'):
				return ord(value[0])-ord('A')
			elif (name == 'unit'):
				return int(value)
		return value

	@staticmethod
	def decodeData(data):
		if 'protocol' not in data:
			return []
		retval = []
		if data['protocol'] == 'arctech':
			decoded = ProtocolArctech.decodeData(data)
			if decoded is not None:
				retval.append(decoded)
		return retval

	def stringForMethod(self, method):
		return None

	@staticmethod
	def methodsForProtocol(protocol, model):
		if (protocol == 'arctech'):
			if (model == 'codeswitch'):
				return Device.TURNON | Device.TURNOFF
			if (model == 'selflearning'):
				return Device.TURNON | Device.TURNOFF
			if (model == 'selflearning-bell'):
				return Device.BELL
		if (protocol == 'comen'):
				return Device.TURNON | Device.TURNOFF
		if (protocol == 'everflourish'):
				return Device.TURNON | Device.TURNOFF
		if (protocol == 'sartano'):
				return Device.TURNON | Device.TURNOFF
		if (protocol == 'waveman'):
				return Device.TURNON | Device.TURNOFF
		if (protocol == 'x10'):
				return Device.TURNON | Device.TURNOFF
		if (protocol == 'hasta'):
				return Device.UP | Device.DOWN | Device.STOP
		return 0

	@staticmethod
	def parametersForProtocol(protocol, model):
		if (protocol == 'arctech' or protocol == 'waveman' or protocol == 'comen'):
			return ['house', 'unit']
		if (protocol == 'everflourish'):
			return ['house', 'unit']
		if (protocol == 'sartano'):
			return ['code']
		if (protocol == 'x10'):
			return ['house', 'unit']
		if (protocol == 'hasta'):
			return ['house', 'unit']
		return []

	@staticmethod
	def protocolInstance(protocol):
		if (protocol == 'arctech'):
			return ProtocolArctech()
		if (protocol == 'fineoffset'):
			return ProtocolFineoffset()
		if (protocol == 'mandolyn'):
			return ProtocolMandolyn()
		if (protocol == 'oregon'):
			return ProtocolOregon()
		return None

from ProtocolArctech import *
from ProtocolFineoffset import *
from ProtocolMandolyn import *
from ProtocolOregon import *