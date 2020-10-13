import re
import os


def process_dir(path_in, db, collection):
    list_dir = os.listdir(path_in)
    try:
        input_file = [os.path.join(path_in, x) for x in list_dir if x.endswith('.txt')][0]
    except IndexError:
        raise Exception('No txt file found')
    with open(input_file) as f:
        text = f.read()
        text = text.replace('*', ';')
        dicts = re.split(r'/; \d+ ;/', text)
        os.chdir(r"myPathToMongoDB\Server\4.0\bin")
        for index, d in enumerate(dicts):
            json_content = '[' + d + ']'
            path_out = os.path.join(path_in, r"out")
            if not os.path.exists(path=path_out):
                os.mkdir(path=path_out)
            output_file = os.path.join(path_out, r'\data{i}.json'.format(i=index))
            print('Importing new json file: {file}'.format(file=output_file))
            with open(output_file, 'w') as fo:
                fo.write(json_content)
                os.system(
                    r"mongoimport --jsonArray --db {db} --collection {collection} --file {file}".format(
                        db=db, collection=collection, file=output_file))


if __name__ == "__main__":
    process_dir(path_in=r"myPath\in", db="myDB", collection="myCollection")

