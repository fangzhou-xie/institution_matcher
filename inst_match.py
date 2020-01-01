import csv
import pdb
import sqlite3 as lite

from fuzzywuzzy import fuzz, process

# TODO: change it to dynamic path further
grid_path = './griddata/grid-2019-12-10'


class InstitutionMatcher():
    def __init__(self):
        conn = lite.connect('./griddata/grid.sqlite')
        self.c = conn.cursor()
        self.inst_list = list(
            zip(*self.c.execute("SELECT Name FROM grid;").fetchall()))[0]

    def update(self):
        # TODO: download and update current ./griddata/grid.sqlite db
        pass

    def match(self, inst_string):
        matched = _match_raw_str(inst_string, self.c)  # exact match of name
        if matched == None:
            # TODO: if exact match fails, perform fuzzy match as well
            # pdb.set_trace()
            most_likely, score = _fuzzy_match(inst_string, self.c)
            matched = _match_raw_str(most_likely, self.c)
        return matched


def _capitalize(tk):
    conj_list = ['of', 'in', 'at', 'and']
    return tk.capitalize() if tk not in conj_list else tk


def _match_raw_str(inst_string, cur):
    "match a raw institution string with a connection cursor"
    inst_str = ' '.join(map(_capitalize, inst_string.split(' ')))
    arg = (inst_str,)
    r = cur.execute("SELECT * FROM grid WHERE Name = ?;", arg).fetchone()
    # pdb.set_trace()
    return r


def _fuzzy_match(inst_str, cur):
    # TODO: ???
    inst_list = list(zip(*cur.execute("SELECT Name FROM grid;").fetchall()))[0]
    # pdb.set_trace()
    most_likely, score = process.extractOne(inst_str, inst_list)
    return most_likely, score


def main():
    im = InstitutionMatcher()
    im.match('sjaf;ljsf;lj')
    # pdb.set_trace()


if __name__ == "__main__":
    main()
