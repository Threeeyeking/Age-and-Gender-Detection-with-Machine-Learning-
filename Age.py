ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"
ageNet = cv.dnn.readNet(ageModel, ageProto)

ageList = ['(0 - 2)', '(4 - 6)', '(8 - 12)', '(15 - 20)', '(25 - 32)', '(38 - 43)', '(48 - 53)', '(60 - 100)']

ageNet.setInput(blob)
agePreds = ageNet.forward()
age = ageList[agePreds[0].argmax()]
print("Gender Output : {}".format(agePreds))
print("Gender : {}".format(age))
