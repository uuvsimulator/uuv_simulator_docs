# uuv_auv_actuator_interface

# uuv_auv_actuator_interface.actuator_manager

## ActuatorManager
```python
ActuatorManager(self)
```

### MAX_FINS
int(x=0) -> int or long
int(x, base=10) -> int or long

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is floating point, the conversion truncates towards zero.
If x is outside the integer range, the function returns a long instead.

If x is not a number or if base is given, then x must be a string or
Unicode object representing an integer literal in the given base.  The
literal can be preceded by '+' or '-' and be surrounded by whitespace.
The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
### find_actuators
```python
ActuatorManager.find_actuators(self)
```
Calculate the control allocation matrix, if one is not given.
# uuv_auv_actuator_interface.fin_model

