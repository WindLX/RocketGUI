import time


def data_slice(raw_data):
    data = raw_data.split("&")
    data_dict = {data[i].split("=")[0]: data[i].split("=")[1] for i in range(len(data))}
    if 'msg' in data_dict.keys():
        data_dict['msg'] = data[-1][4:]
    return data_dict


def msg_slice(raw_msg):
    if raw_msg[:3] == "Err":
        return {}
    msg = raw_msg.split(",")
    msg_dict = {msg[i].split("=")[0]: msg[i].split("=")[1] for i in range(len(msg))}
    msg_dict["UTC"] = str(int(time.time()))
    msg_dict["Lon"] = "E10356.35266"
    msg_dict["Lat"] = "N3045.78318"
    return msg_dict
