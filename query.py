#!/usr/bin/env python

import json
import os


def get_build_number():
    l = []
    m = None
    number = ""

    os.system(
        "wget --no-check-certificate https://cloudci.esbu.smartmatic.net/linux/job/{}/api/json?pretty=true".format(job_name))
    json_file = os.path.join(os.getcwd() + "/json?pretty=true")
    with open(json_file, "r") as f:
        data = json.load(f)
        for x in data["builds"]:
            l.append(x["number"])
    os.system("rm -rf json?pretty=true")
    for j in l:
        os.system(
            "wget --no-check-certificate https://cloudci.esbu.smartmatic.net/linux/job/{}/{}/api/json?pretty=true".format(job_name, j))
        json_file_build_number = os.path.join(os.getcwd() + "/json?pretty=true")
        with open(json_file_build_number, "r") as f:
            d = json.load(f)
            name = d["actions"][0]["parameters"][2]["value"]
            if str(name) == "develop":
                m = True
            os.system("rm -rf json?pretty=true")
        if m is True:
            number = j
            break

    f = open("build_number.txt", "w+")
    f.write("DEVELOP_BUILD_SUCCESS={}".format(number))
    f.close()


if __name__ == "__main__":
    get_build_number()
