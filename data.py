#!/usr/bin/python
import json


class Data(object):
    def __init__(self, file_name="db.json"):
        self.file_name = file_name

    def try_open_json_file(self):
        print "try_open_json_file"
        try:
            print "try open the json file ..."
            self.open_json_file()
            print "json file open with sucess"
        except IOError:
            self.create_a_new_file_from_scrath(self.file_name)

    def open_json_file(self):
        f = open(self.file_name, "r")
        self.db = json.load(f)

    def create_a_new_file_from_scrath(self):
        print "\ncreate a new file from scrath"
        self.db = {}
        self.save_json_file(self.file_name, self.db)

    def save_json_file(self):
        print "saving %s ..." % self.file_name
        f = open(self.file_name, "w")
        json.dump(self.db, f)
        print "%s saved" % self.file_name
