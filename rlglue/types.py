# 
# Copyright (C) 2007, Mark Lee
# 
#http://rl-glue-ext.googlecode.com/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#  $Revision: 446 $
#  $Date: 2009-01-22 20:20:21 -0700 (Thu, 22 Jan 2009) $
#  $Author: brian@tannerpages.com $
#  $HeadURL: http://rl-glue-ext.googlecode.com/svn/trunk/projects/codecs/Python/src/rlglue/types.py $


import copy
import os

class RL_Abstract_Type:
	def __init__(self,numInts=None,numDoubles=None,numChars=None):
		self.intArray = []
		self.doubleArray = []
		self.charArray = []
		if numInts != None:
			self.intArray = [0]*numInts
		if numDoubles != None:
			self.doubleArray = [0.0]*numDoubles
		if numChars != None:
			self.charArray = ['']*numChars

	def sameAs(self,otherAbstractType):
		return self.intArray==otherAbstractType.intArray and self.doubleArray==otherAbstractType.doubleArray and self.charArray==otherAbstractType.charArray

	#this coolness added by btanner sept 30/2008
	#it allows the subclasses to be used like myAction=Action.fromAbstractType(someAbstractType)
	@classmethod
	def fromAbstractType(cls, theAbstractType):	
		retStruct=cls()
		retStruct.intArray=copy.deepcopy(theAbstractType.intArray)
		retStruct.doubleArray=copy.deepcopy(theAbstractType.doubleArray)
		retStruct.charArray=copy.deepcopy(theAbstractType.charArray)
		return retStruct



class Action(RL_Abstract_Type):
	def __init__(self,numInts=None,numDoubles=None,numChars=None):
		RL_Abstract_Type.__init__(self,numInts,numDoubles,numChars)
	
	    

class Observation(RL_Abstract_Type):
	def __init__(self,numInts=None,numDoubles=None,numChars=None):
		RL_Abstract_Type.__init__(self,numInts,numDoubles,numChars)



class Observation_action:
	def __init__(self,theObservation=None,theAction=None):
		if theObservation != None:
			self.o = theObservation
		else:
			self.o = Observation()
		if theAction != None:
			self.a = theAction
		else:
			self.a = Action()



class Reward_observation_terminal:
	def __init__(self,reward=None, theObservation=None, terminal=None):
		if reward != None:
			self.r = reward
		else:
			# BEGIN: change made by: Akshay Narayan (06-01-2015:1427)
			# self.r = 0.0
			self.r = Reward()
			# END: change made by: Akshay Narayan (06-01-2015:1427)
		if theObservation != None:
			self.o = theObservation
		else:
			self.o = Observation()
		if terminal != None:
			self.terminal = terminal
		else:
			self.terminal = False



class Reward_observation_action_terminal:
	def __init__(self,reward=None, theObservation=None, theAction=None, terminal=None):
		if reward != None:
			self.r = reward
		else:
			# BEGIN: change made by: Akshay Narayan (06-01-2015:1428)
			# self.r = 0.0
			self.r = Reward()
			# END: change made by: Akshay Narayan (06-01-2015:1428)
		if theObservation != None:
			self.o = theObservation
		else:
			self.o = Observation()
		if theAction != None:
			self.a = theAction
		else:
			self.a = Action()
		if terminal != None:
			self.terminal = terminal
		else:
			self.terminal = False



# BEGIN: change made by: Akshay Narayan (05-01-2015:1750)

class Reward(RL_Abstract_Type):
	def __init__(self, numInts=None, numDoubles=None, numChars=None):
		RL_Abstract_Type.__init__(self, numInts, numDoubles, numChars)

	def duplicate(self):
		result = copy.deepcopy(self)

		return result

	@staticmethod
	def getNumRewards():
		numRewards = 1 # the default case if nothing is specified, only one objective is given
		envNumRewards = os.getenv("RLGLUE_NUM_REWARDS")

		if envNumRewards is not None:
			numRewards = int(envNumRewards)

		return numRewards


	# method to add individual rewards
	def plusEquals(self, otherReward):
		for i in range(len(self.doubleArray)):
			if i < len(otherReward.doubleArray):
				self.doubleArray[i] += otherReward.doubleArray[i]


	# method to subtract individual rewards
	def minusEquals(self, otherReward):
		for i in range(len(self.doubleArray)):
			if i < len(otherReward.doubleArray):
				self.doubleArray[i] -= otherReward.doubleArray[i]

	# method to add 2 rewards (I guess); this one is only defined, never used in java codec
	def plus(self, other):
		result = self.duplicate()

		for i in range(len(self.doubleArray)):
			if i < len(otherReward.doubleArray):
				result.doubleArray[i] += otherReward.doubleArray[i]

		return  result

	# method to subtract 2 rewards (I guess); this is only defined but never used in java codec
	def minus(self, other):
		result = self.duplicate()

		for i in range(len(self.doubleArray)):
			if i < len(otherReward.doubleArray):
				result.doubleArray[i] -= otherReward.doubleArray[i]

		return  result

# END: change made by: Akshay Narayan (05-01-2015:1750)