from tqdm import tqdm


def show_header():
    train_filepath = "./data/train_v2.csv/train_v2.csv"
    with open(train_filepath) as ifile:
        for i, line in enumerate(ifile):
            # print(i, line)
            len_o = len(line)
            line = line.replace("not available in demo dataset",
                                "nad").replace("(not set)", "ns")
            len_a = len(line)
            print(i, len_o, len_a)
            print(line)
            if i > 50:
                break


def get_header(src_filepath, tar_filepath, n=10000):
    lines = []
    with open(src_filepath, encoding="utf-8") as ifile:
        for i in tqdm(range(n)):
            line = ifile.readline()
            lines.append(line)
    with open(tar_filepath, "w", encoding="utf-8") as ofile:
        ofile.writelines(lines)


def train_test_v2_header():
    train_filepath = "./data/train_v2.csv/train_v2.csv"
    train_header_filepath = "./data/train_v2_header.csv"
    get_header(train_filepath, train_header_filepath, 50000)
    test_filepath = "./data/test_v2.csv"
    test_header_filepath = "./data/test_v2_header.csv"
    get_header(test_filepath, test_header_filepath, 50000)


def main():
    train_test_v2_header()


if __name__ == '__main__':
    main()
