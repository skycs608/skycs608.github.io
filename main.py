import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", type=str, required=True)
    parser.add_argument("--local_repo_path", type=str, default="./")
    args = parser.parse_args()
    return args

def gen_new(in_or_out, name, student_id, photo_url):
    template_content = open(f"{in_or_out}.html.template", "r", encoding="utf-8").read()
    new = template_content.replace("[NAME]", name).replace("[STUDENT_ID]", student_id).replace("[PHOTO_URL]", photo_url)
    with open(os.path.join(f"./{student_id}", f"{in_or_out}.html"), "w", encoding="utf-8") as f:
        f.write(new)

def main(args):
    name, student_id, photo_url = args.message.strip().split()
    if not os.path.exists(f"./{student_id}"):
        os.mkdir(f"./{student_id}")
    gen_new("in", name, student_id, photo_url)
    gen_new("out", name, student_id, photo_url)
    print(student_id)


if __name__ == "__main__":
    args = parse_args()
    main(args)