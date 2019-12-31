import csv
import pdb
import sqlite3 as lite

# TODO: change it to dynamic path further
grid_path = './griddata/grid-2019-12-10'


class InstitutionMatcher():
    def __init__(self):
        conn = lite.connect('./griddata/grid.sqlite')
        self.c = conn.cursor()

    def update(self):
        # TODO: download and update current ./griddata/grid.sqlite db
        pass

    def match(self, inst_string):
        matched = _match_raw_str(inst_string, self.c)  # exact match of name
        if matched != None:
            return matched
        else:
            # TODO: if exact match fails, perform fuzzy match as well
            matched = _fuzzy_match(inst_string, self.c)


def _capitalize(tk):
    conj_list = ['of', 'in', 'at', 'and']
    return tk.capitalize() if tk not in conj_list else tk


def _match_raw_str(inst_string, cursor):
    "match a raw institution string with a connection cursor"
    inst_str = ' '.join(map(_capitalize, inst_string.split(' ')))
    arg = (inst_str,)
    r = cursor.execute("SELECT * FROM grid WHERE Name = ?;", arg).fetchone()
    # pdb.set_trace()
    return r


def _fuzzy_match(inst_str, cursor):
    # TODO: ???
    return r


def main():
    im = InstitutionMatcher()
    pdb.set_trace()
    # im.match('sjaf;ljsf;lj')


if __name__ == "__main__":
    main()
