#! /usr/bin/python

import os
import article
import ConfigParser


def main(config):
    bs = config.get("blogkit", "backstage")
    s = config.get("blogkit", "stage")
    if prepare_new_posts(bs, s):
        pass
    else:
        pass


def prepare_new_posts(backstage, stage):
    os.chdir(backstage)
    cur_val = len(os.listdir(stage))
    new_posts = os.listdir(".")
    if new_posts:
        posts = []
        for post in new_posts:
            posts.append(article.Article(os.path.join(".", post)))
        posts.sort()
        for post in posts:
            os.rename(post.filename,
                      os.path.join(stage, '{}.md'.format(cur_val)))
            cur_val += 1
        return True
    else:
        return False


if __name__ == "__main__":
    import sys

    config = ConfigParser.RawConfigParser()
    config.read(sys.argv[1])
    main(config)