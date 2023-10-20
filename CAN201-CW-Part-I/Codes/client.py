 # new import
import hashlib
from socket import *
import json
from os.path import getsize
import argparse
import struct
import time

MAX_PACKET_SIZE = 20480

# Const Value
OP_SAVE, OP_DELETE, OP_GET, OP_UPLOAD, OP_DOWNLOAD, OP_BYE, OP_LOGIN, OP_ERROR = 'SAVE', 'DELETE', 'GET', 'UPLOAD', 'DOWNLOAD', 'BYE', 'LOGIN', "ERROR"
TYPE_FILE, TYPE_DATA, TYPE_AUTH, DIR_EARTH = 'FILE', 'DATA', 'AUTH', 'EARTH'
FIELD_OPERATION, FIELD_DIRECTION, FIELD_TYPE, FIELD_USERNAME, FIELD_PASSWORD, FIELD_TOKEN = 'operation', 'direction', 'type', 'username', 'password', 'token'
FIELD_KEY, FIELD_SIZE, FIELD_TOTAL_BLOCK, FIELD_MD5, FIELD_BLOCK_SIZE = 'key', 'size', 'total_block', 'md5', 'block_size'
FIELD_STATUS, FIELD_STATUS_MSG, FIELD_BLOCK_INDEX = 'status', 'status_msg', 'block_index'
DIR_REQUEST, DIR_RESPONSE = 'REQUEST', 'RESPONSE'
KEY, BLOCK_SIZE, TOTAL_BLOCK = "", 0, 0

TOKEN = None
totalduration = 0.0

def get_tcp_packet(conn):
    """
    Receive a complete TCP "packet" from a TCP stream and get the json data and binary data.
    :param conn: the TCP connection
    :return:
        json_data
        bin_data
    """
    bin_data = b''
    while len(bin_data) < 8:
        data_rec = conn.recv(8)
        if data_rec == b'':
            time.sleep(0.01)
        if data_rec == b'':
            return None, None
        bin_data += data_rec
    data = bin_data[:8]
    bin_data = bin_data[8:]
    j_len, b_len = struct.unpack('!II', data)
    while len(bin_data) < j_len:
        data_rec = conn.recv(j_len)
        if data_rec == b'':
            time.sleep(0.01)
        if data_rec == b'':
            return None, None
        bin_data += data_rec
    j_bin = bin_data[:j_len]

    try:
        json_data = json.loads(j_bin.decode())
    except Exception as ex:
        return None, None

    bin_data = bin_data[j_len:]
    while len(bin_data) < b_len:
        data_rec = conn.recv(b_len)
        if data_rec == b'':
            time.sleep(0.01)
        if data_rec == b'':
            return None, None
        bin_data += data_rec
    return json_data, bin_data


def make_packet(json_data, bin_data=None):
    """
    Make a packet following the STEP protocol.
    Any information or data for TCP transmission has to use this function to get the packet.
    :param json_data:
    :param bin_data:
    :return:
        The complete binary packet
    """
    j = json.dumps(dict(json_data), ensure_ascii=False)
    j_len = len(j)
    if bin_data is None:
        return struct.pack('!II', j_len, 0) + j.encode()
    else:
        return struct.pack('!II', j_len, len(bin_data)) + j.encode() + bin_data


def make_request_packet(operation, username, password, json_data, size=None, blockindex=None, data_type=None, key=None,
                        token=None, totalblock=0, bin_data=None):
    """
    Make a packet for request
    :param totalblock:
    :param token:
    :param key:
    :param password:
    :param username:
    :param size:
    :param blockindex:
    :param operation: [SAVE, DELETE, GET, UPLOAD, DOWNLOAD, BYE, LOGIN]
    :param data_type: [FILE, DATA, AUTH]
    :param json_data
    :param bin_data
    :return:
    """
    json_data[FIELD_OPERATION] = operation
    json_data[FIELD_DIRECTION] = DIR_REQUEST
    json_data[FIELD_TYPE] = data_type
    json_data[FIELD_USERNAME] = username
    json_data[FIELD_PASSWORD] = password
    if key is not None:
        json_data[FIELD_KEY] = key
    if token is not None:
        json_data[FIELD_TOKEN] = token
    if totalblock != 0:
        json_data[FIELD_TOTAL_BLOCK] = totalblock
    json_data[FIELD_SIZE] = size
    json_data[FIELD_BLOCK_INDEX] = blockindex
    return make_packet(json_data, bin_data)


def _argparse():
    parse = argparse.ArgumentParser()
    parse.add_argument("--server_ip", default='127.0.0.1', action='store', required=False, dest="server_ip",
                       help= "The IP address bind to the server. Default bind all IP.")
    parse.add_argument("--port",default='1379',action='store', required=False, dest="port",
                       help="The port that server listen on. Default is 1379.")
    parse.add_argument("--id", default='1202437', action='store', required=False, dest="id",
                       help="Your ID.")
    parse.add_argument("--f", default='test4.jpg', action='store', required=False, dest="file",
                       help="File path. Default is empty (no file will be uploaed).")
    parse.add_argument("--key", default= None, action='store', required=False, dest="key",
                       help="The key has been saved")
    return parse.parse_args()


def login():
    # generate and username and password
    global TOKEN, username, password
    TOKEN = None
    json_data = {}
    json_data[FIELD_DIRECTION] = DIR_REQUEST
    #generate username
    parser = _argparse()
    username = parser.id

    #generate password
    if username is not None:
        password = hashlib.md5(username.encode()).hexdigest()

    login = make_request_packet(  OP_LOGIN, username = username,
                                  password = password, json_data = {}, size = None, blockindex = None,
                                  data_type =TYPE_AUTH,
                                  key = None,
                                  token = None, totalblock = 0, bin_data = None)
    clientSocket.send(login)
    json_data, bin_data = get_tcp_packet(clientSocket)

    TOKEN = json_data[FIELD_TOKEN]
    print(f"Token:{TOKEN}")

    return json_data, bin_data


# save with input key
def savefile():
    global TOKEN, FIELD_KEY, FIELD_BLOCK_SIZE, FIELD_TOTAL_BLOCK
    filesize = getsize(parser.file)
    key = parser.key
    save = make_request_packet(OP_SAVE, username=None,
                               password=None, json_data= {}, size=filesize, blockindex = None,
                               data_type=TYPE_FILE,
                               key= key, token=TOKEN , totalblock=0, bin_data=None)

    clientSocket.send(save)
    json_data, bin_data = get_tcp_packet(clientSocket)
    print(json_data)

    if json_data[FIELD_STATUS] != 200:
        print(f'[error {json_data[FIELD_STATUS]}] {json_data[FIELD_STATUS_MSG]}')
    global KEY, TOTAL_BLOCK, BLOCK_SIZE
    KEY = json_data[FIELD_KEY]
    TOTAL_BLOCK = json_data[FIELD_TOTAL_BLOCK]
    BLOCK_SIZE = json_data[FIELD_BLOCK_SIZE] #eg. value = json_data[key]


def get_file_md5(filename):
    """
    Get MD5 value for big file
    :param filename:
    :return:
    """
    m = hashlib.md5()
    with open(filename, 'rb') as fid:
        while True:
            d = fid.read(2048)
            if not d:
                break
            m.update(d)
    return m.hexdigest()


def upload():
    global totalduration
    uploadkey = KEY
    uploadblocksize = BLOCK_SIZE
    uploadtotal_block = TOTAL_BLOCK
    md5checked = get_file_md5(parser.file)
    f = open(parser.file, 'rb')
    for i in range(0, uploadtotal_block):
        f.seek(i * uploadblocksize)

        if i != uploadtotal_block - 1 :
            bin_data = f.read(uploadblocksize)
        else:
            bin_data = f.read()
        start = time.time()  # start to count the time
        upload = make_request_packet(OP_UPLOAD, username=None,
                               password=None, json_data= {}, size = uploadblocksize, blockindex= i,
                               data_type=TYPE_FILE,
                               key= uploadkey, token = TOKEN , totalblock= uploadtotal_block, bin_data=bin_data)
        clientSocket.send(upload)
        json_data, bin_data = get_tcp_packet(clientSocket)
        duration = time.time() - start
        totalduration = duration + totalduration
        progress_bar(i+1, uploadtotal_block , duration, totalduration)
        time.sleep(0.01)
        print(json_data)
        if 'md5' in json_data:
            if md5checked == json_data[FIELD_MD5]:
                print(f'The md:‘{md5checked}’ has been checked, the server has received the right file completely.')
    f.close()


def progress_bar(finish_tasks_number, tasks_number, complete_time, totalduration):
        """
        进度条

        :param finish_tasks_number: int,
        :param tasks_number: int,
        :param complete_time: float,
        :return:
        """

        percentage = round(finish_tasks_number / tasks_number * 100)
        finished_label = "▓" * (percentage // 2)
        unfinished_label = "-" * (100 - percentage)
        arrow = "->"
        if not finished_label or not unfinished_label:
            arrow = ""
        print("\r{}% [{}{}{}] the complete time per task:{:.6f}s the total duration until now: {:.6f}s".format(percentage, finished_label, arrow, unfinished_label, complete_time ,totalduration),
              end="")




if __name__ == "__main__":
    parser = _argparse()
    server_ip = parser.server_ip
    server_port = int(parser.port)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_ip, server_port))
    # task 2
    login()
    # task 3
    savefile()
    upload()

