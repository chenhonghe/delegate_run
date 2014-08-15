#!/usr/bin/python

import requests
import json
import time
import os
import logging

safetime = 120  # safe time, 120 seconds is safe to restart client
auth = ('hehe', 'hic98372p~s0817s') ## user/pass for rpc service
url = "http://localhost:9989/rpc"  ## rpc url

LOG_FILENAME="/tmp/bc_log.txt"
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

def main() :
    headers = {'content-type': 'application/json'}
    info = {
        "method": "get_info",
        "params": [],
        "jsonrpc": "2.0",
        "id": 1
    }

    while True:
        try :
            info_res = requests.post(url, data=json.dumps(info), headers=headers, auth=auth)
        except :
            logging.info("http error...")
            return

        info_json = json.loads(vars(info_res)["_content"])

        if not "result" in info_json:
            return

        timestamp = time.strftime("%Y%m%dT%H%M%S", time.localtime(time.time()))
        block_production_timestamp = info_json["result"]["wallet_next_block_production_timestamp"]
        safe_timestamp = time.strftime("%Y%m%dT%H%M%S", time.localtime(time.time()+safetime))

        if block_production_timestamp > safe_timestamp or block_production_timestamp==None :
            break;

        logging.info("wait... "+timestamp)
        time.sleep(10)

    logging.info("kill... "+timestamp)
    os.system("killall -9 bitshares_client");


if __name__ == '__main__':
    main()
