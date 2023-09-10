# image-transfer

a helper to transfer image in markdown

## usage

```
usage: image-transferr.py [-h] [-s SRCDIR]
                          [-d DSTDIR] [-t THREAD]

options:
  -h, --help            show this help message and
                        exit
  -s SRCDIR, --srcdir SRCDIR
                        markdown file directory
  -d DSTDIR, --dstdir DSTDIR
                        local storage path
  -t THREAD, --thread THREAD
                        number of thread
```
![img:usage](https://i.imgur.com/icGpjyz.png)

## todo

- [x] download from host to local
- [ ] upload from local to host
- [ ] replace url
- [x] multithread
- [ ] downloader: chuck by chunk?
- [ ] rename: use base64 to map full url name to local name

> downloader part: credit to <https://gist.github.com/chandlerprall/1017266>
