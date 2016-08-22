import time
class PositionProccesser(object):

	def __init__(self, calibration_forces):

		self.calibration_forces = calibration_forces
		self.last_mouse_change = time.time()

		self.x_pos = 0.0
		self.y_pos = 0.0

		self.x_velocity = 0.0
		self.y_velocity = 0.0

	def calculate_movement_from_force(self, x, y):
		time_diff = time.time() - self.last_mouse_change

		self.x_velocity += (x - self.calibration_forces[0]) * time_diff
		self.y_velocity += (y - self.calibration_forces[1]) * time_diff

		self.x_pos += self.x_velocity * time_diff
		self.y_pos += self.y_velocity * time_diff

		self.last_mouse_change = time.time()

		return [self.x_pos, self.y_pos]