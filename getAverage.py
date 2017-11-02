import re


result = """
1  gateway (137.73.113.1)  1.347 ms  1.607 ms  1.658 ms  1.790 ms  2.035 ms  2.136 ms  2.367 ms  2.461 ms  2.660 ms
 2  192.168.190.1 (192.168.190.1)  0.445 ms  0.505 ms  0.480 ms  0.458 ms  0.422 ms  0.386 ms  0.329 ms  0.232 ms  0.241 ms
 3  192.168.210.2 (192.168.210.2)  0.127 ms  0.158 ms  0.200 ms  0.154 ms  0.154 ms  0.302 ms * * *
 4  192.168.210.6 (192.168.210.6)  0.327 ms  0.340 ms  0.373 ms  0.351 ms  0.391 ms  0.360 ms  0.408 ms  0.379 ms  0.369 ms
 5  xe-5-0-0.londpg-ban1.ja.net (146.97.137.37)  0.920 ms  0.904 ms  0.877 ms  0.845 ms  0.786 ms  0.848 ms  0.825 ms  0.793 ms  0.804 ms
 6  ae26.londpg-sbr2.ja.net (146.97.35.233)  1.033 ms  1.011 ms  0.983 ms  0.963 ms  1.015 ms  1.035 ms  1.011 ms  0.979 ms  0.933 ms
 7  ae30.londtw-sbr2.ja.net (146.97.33.6)  1.569 ms  1.572 ms  1.695 ms  1.458 ms  1.512 ms  1.481 ms  1.504 ms  1.478 ms  1.424 ms
 8  ae28.londtt-sbr1.ja.net (146.97.33.61)  1.570 ms  1.582 ms  1.554 ms  1.511 ms  1.689 ms  1.662 ms  1.639 ms  1.628 ms  1.521 ms
 9  ae0.londtn-ban3.ja.net (146.97.35.170)  1.918 ms  1.889 ms  1.849 ms  1.606 ms  2.032 ms  2.003 ms  1.969 ms  1.934 ms  1.434 ms
10  linx-lon1.as13335.net (195.66.225.179)  1.836 ms  1.771 ms  1.793 ms  1.807 ms  1.823 ms  1.802 ms  1.870 ms  1.871 ms  1.653 ms
11  104.20.70.198 (104.20.70.198)  1.641 ms  1.608 ms  1.640 ms  1.586 ms  1.629 ms  1.594 ms  1.607 ms  1.636 ms  1.619 ms
"""

listOfResult = result.splitlines()

for node in listOfResult:
    if node != "": 
        raw = node.split(")",1)
        nodeName = raw[0] + ")"
        nodeInfo = raw[1]
        numbers = re.findall(r"(\d+\.\d+) ms", nodeInfo)
        numbersInt = map(float, numbers)
        intlist = [float(x) for x in numbers]

        avg = float(sum(intlist))/len(intlist)
        print ("Average Latency for " + nodeName + " is: " + str(avg/2) )
        #print ("Too laze to read? just copy this -_-  ->      " + str(avg/2))
        print ("")

