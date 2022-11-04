import sys
import inspect

print(callable(sys))
print(inspect.ismodule(sys))
for module in dir(sys):
    print(module)
print(callable(sys.colorama))
for module in dir(sys.colorama):
    print(module)
print(sys.colorama)
