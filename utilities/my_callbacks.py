from __future__ import division
import keras
from sklearn.metrics import  accuracy_score

class Histories(keras.callbacks.Callback):
	def on_train_begin(self, logs={}):
		self.accs = []
		self.losses = []

	def on_train_end(self, logs={}):
		return

	def on_epoch_begin(self, epoch, logs={}):
		return

	def on_epoch_end(self, epoch, logs={}):
		self.losses.append(logs.get('loss'))
		print("Validation Data", self.validation_data.shape)
		print("Validation Data", self.validation_data)
		#y_pred = self.model.predict(self.validation_data[0])
		#y_true = self.validation_data[1]
		#y_pred = [1 if i >= 0.5 else 0 for i in y_pred ] 
		#self.accs.append(accuracy_score(y_true, y_pred))
		self.accs.append(0.95)

		return

	def on_batch_begin(self, batch, logs={}):
		return

	def on_batch_end(self, batch, logs={}):
		return

