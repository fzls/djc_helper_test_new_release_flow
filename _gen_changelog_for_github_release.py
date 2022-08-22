"""将CHANGELOG.MD中的本次更新信息提取出来，供github release流程使用"""

import os.path

from log import logger
from update import get_update_info_from_local_file
from util import make_sure_dir_exists


def gen_changelog():
    update_info = get_update_info_from_local_file("README.MD", "CHANGELOG.MD")

    logger.info("移除末尾固定的两个更新条目")
    fixed_items = [
        "如需购买自动更新DLC或按月付费，请在配置工具的【付费相关】标签页自助购买，具体流程请查阅目录中【付费指引.docx】",
        "其他改动及上述功能具体用法，详见README.MD和CHANGELOG.MD以及使用教程/使用文档.docx和教程视频",
    ]
    message_list = []
    for message in update_info.update_message.split("\n"):
        filtered = False
        for item in fixed_items:
            if item in message:
                filtered = True
                break

        if not filtered:
            message_list.append(message)

    update_info.update_message = "\n".join(message_list)

    github_release_dir = os.path.realpath("./releases/_github_action_artifact")
    make_sure_dir_exists(github_release_dir)

    github_change_path = os.path.join(github_release_dir, "changelog-github.txt")
    logger.info(f"将更新信息写入临时文件，供github release使用: {github_change_path}")
    with open(github_change_path, "w", encoding="utf-8") as output_file:
        output_file.write(update_info.update_message)


if __name__ == '__main__':
    gen_changelog()
