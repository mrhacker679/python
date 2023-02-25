import platform

Get the name of the operating system
```
** os_name = platform.system() **
** print(os_name) **
```
Get the release version of the operating system
** ```os_release = platform.release()
print(os_release) ``` **

Get the version of the operating system
** ```os_version = platform.version()
print(os_version)

Get the machine architecture
** ```machine_arch = platform.machine()
print(machine_arch)

Get the processor type
** ```processor_type = platform.processor()
print(processor_type)

Get the Python version
** ```python_version = platform.python_version()
print(python_version)

Get the Python implementation
** ```python_implementation = platform.python_implementation()
print(python_implementation)

Get the platform identifier
** ```platform_id = platform.platform()
print(platform_id)

Get the tuple of the operating system name, version, and release
** ```os_tuple = platform.uname()
print(os_tuple)
