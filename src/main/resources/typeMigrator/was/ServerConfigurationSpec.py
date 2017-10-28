#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from com.xebialabs.deployit.plugin.api.reflect import Type

def mapProperties(old, new):
  new.setType(Type.valueOf("was.JavaProcessDefinitionSpec"))
  if old.JavaVirtualMachine_classpath is not None:    	
    new.setProperty('JavaVirtualMachine_classpath', old.JavaVirtualMachine_classpath)
  if old.JavaVirtualMachine_bootClasspath is not None:
  	new.setProperty('JavaVirtualMachine_bootClasspath', old.JavaVirtualMachine_bootClasspath)
  if old.JavaVirtualMachine_verboseModeClass is not None:
  	new.setProperty('JavaVirtualMachine_verboseModeClass', old.JavaVirtualMachine_verboseModeClass)
  if old.JavaVirtualMachine_verboseModeGarbageCollection is not None:
  	new.setProperty('JavaVirtualMachine_verboseModeGarbageCollection', old.JavaVirtualMachine_verboseModeGarbageCollection)
  if old.JavaVirtualMachine_verboseModeJNI is not None:
  	new.setProperty('JavaVirtualMachine_verboseModeJNI', old.JavaVirtualMachine_verboseModeJNI)
  if old.JavaVirtualMachine_initialHeapSize is not None:
  	new.setProperty('JavaVirtualMachine_initialHeapSize', old.JavaVirtualMachine_initialHeapSize)
  if old.JavaVirtualMachine_maximumHeapSize is not None:
  	new.setProperty('JavaVirtualMachine_maximumHeapSize', old.JavaVirtualMachine_maximumHeapSize)
  if old.JavaVirtualMachine_genericJvmArguments is not None:
    new.setProperty('JavaVirtualMachine_genericJvmArguments', old.JavaVirtualMachine_genericJvmArguments)
  if old.JavaVirtualMachine_disableJIT is not None:
    new.setProperty('JavaVirtualMachine_disableJIT', old.JavaVirtualMachine_disableJIT)
# TODO: 
  if old.jvmCustomProperties is not None:
    map = {}
#   parse the custom properties
#   Example:
#   map['newtestkey'] = 'newtestvalue'
    new.setProperty('JavaVirtualMachine_customProperties', map)

