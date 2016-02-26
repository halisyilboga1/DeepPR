#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import dataset, models
from keras.callbacks import ModelCheckpoint

basepath = os.path.dirname(__file__)

print "loading data...",
X, y = dataset.load_as_nparray()
X_train, y_train = X[:800,:,:], y[:800,:]
X_test, y_test = X[800:,:,:], y[800:,:]
print "done"

print "compiling model...",
model = models.VGG()
print "done"

checkpoint = ModelCheckpoint(filepath=os.path.join(basepath, 'checkpoint.hdf5'), verbose=1, save_best_only=True)
model.fit(X_train, y_train, batch_size=50, nb_epoch=30, verbose=2, validation_data=(X_test, y_test), callbacks=[checkpoint])