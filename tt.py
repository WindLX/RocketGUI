def msg_slice(raw_msg):
    msg = raw_msg.split(",")
    msg_dict = {msg[i].split("=")[0]: msg[i].split("=")[1] for i in range(len(msg))}
    return msg_dict

raw_msg = "A=1,Lat="

print(msg_slice(raw_msg))

print(msg_slice(raw_msg)['Lat'])