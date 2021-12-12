# kill the device and storage
for x in range(0, 10000):
  open("str{}.txt".format(x), "w").close()
