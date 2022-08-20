import re
from typing import List

from dao import DnfRoleInfo, MobileGameRoleInfo


def parse_role_list(jsonRes) -> List[DnfRoleInfo]:
    role_reg = r"\d+ [^ ]+ \d+ \d+"
    rolemap = {}

    for item in jsonRes["data"].split("|"):
        if re.match(role_reg, item):
            roleid, rolename, forceid, level = item.split(" ")
            if roleid not in rolemap:
                rolemap[roleid] = DnfRoleInfo(roleid, rolename, forceid, level)

    return list(rolemap.values())


def parse_mobile_game_role_list(jsonRes):
    jx3_role_reg = r"\w+ [^ ]+"
    rolemap = {}

    for item in jsonRes["data"].split("|"):
        if re.match(jx3_role_reg, item):
            item = item.strip().split(" ")
            if len(item) == 2:
                roleid, rolename = item
                if roleid not in rolemap:
                    rolemap[roleid] = MobileGameRoleInfo(roleid, rolename)

    return list(rolemap.values())
