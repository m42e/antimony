import base
import datum

class FloatVariable(base.Node3D):
    def __init__(self, name, x, y, z):
        super(FloatVariable, self).__init__(name, x, y, z)
        self.add_datum('value', datum.FloatDatum(self, 0))

    def get_control(self):
        import control.variable
        return control.variable.FloatVariableControl