"""将CHANGELOG.MD中的本次更新信息提取出来，供github release流程使用"""

import os.path

from log import logger
from update import get_update_info_from_local_file
from util import make_sure_dir_exists


def gen_changelog():
    update_info = get_update_info_from_local_file("README.MD", "CHANGELOG.MD")

    github_release_dir = os.path.realpath("./releases/_github_action_artifact")
    make_sure_dir_exists(github_release_dir)

    github_change_path = os.path.join(github_release_dir, "changelog-github.txt")
    logger.info(f"将更新信息写入临时文件，供github release使用: {github_change_path}")
    with open(github_change_path, "w", encoding="utf-8") as output_file:
        output_file.write(update_info.update_message)


if __name__ == '__main__':
    gen_changelog()
