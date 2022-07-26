label = "{}, {}".format(gender, age)
cv.putText(frameFace, label, (bbox[0], bbox[1]-20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 3, cv.LINE_AA)
cv.imshow("Age Gender Demo", frameFace)
