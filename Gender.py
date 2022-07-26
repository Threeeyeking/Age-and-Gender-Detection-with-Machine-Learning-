genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"
ageNet = cv.dnn.readNet(ageModel, ageProto)

genderList = ['Male', 'Female']

blob = cv.dnn.blobFromImage(face, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
genderNet.setInput(blob)
genderPreds = genderNet.forward()
gender = genderList[genderPreds[0].argmax()]
print("Gender Output : {}".format(genderPreds))
print("Gender : {}".format(gender))
