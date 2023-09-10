# 备份 imgur 的图片, 防寄
import os
import argparse
import re
import base64
import requests

# local storage should has similar name, so it's easier to map
# TODO: download from host to local
# TODO: upload from local to host
# TODO: replace url


# dir -> file -> url
def make_url_iter(dirname, filter, extracter):
    # dfs to get all root?
    for dirname, ds, fs in os.walk(dirname):
        for basename in fs:
            if basename.endswith(".md"):
                fullname = os.path.join(dirname, basename)
                for url in extracter(fullname):
                    yield url


def extract_imageurls_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        # pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        pattern = r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\))+(?:\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))"""
        all_urls = re.findall(pattern, content)

        image_pattern = r"\.(?:jpg|jpeg|png|gif|bmp|svg)"
        imageurls = [url for url in all_urls if re.search(image_pattern, url)]
        return imageurls

        # test_path = "/home/phan/course_archive/12-lab/report1/report1.md"
        # for urls in extract_urls_from_file(test_path):
        #     print(urls)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # not support single file
    parser.add_argument("-s", "--srcdir", help="markdown file directory")
    parser.add_argument("-d", "--dstdir", help="local storage path")
    args = parser.parse_args()

    # path = os.environ.get('HOME') + "/notes/"
    src_dirname = args.srcdir
    dst_dirname = args.dstdir

    extracter = extract_imageurls_from_file
    url_iter = make_url_iter(
        src_dirname, lambda s: s.endwith(".md"), extracter)
    for url in url_iter:
        print(url)
