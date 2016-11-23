import os
import xlwt
__author__ = 'David "Towels" Sheridan'

input_directory = "C:\\" + raw_input("name of folder to evaluate?  ")
print("evaluating \"" + input_directory + "\"")
# input_directory = "C:\\DL"
output_spreadsheet = xlwt.Workbook(encoding="utf-8")
x_cell = 0
y_cell = 0
sheet1 = output_spreadsheet.add_sheet("Sheet 1")
sheet1.write(x_cell, y_cell, "Weld_ID")
sheet1.write(x_cell, y_cell + 1, "SDR")


class DataLogFile:
    def __init__(self):
        self.weld_id = ""
        self.diam_sdr = ""
        self.raw_dl_file = open(input_directory + "\\" + data_logger_file, 'r')
        self.weld_information = []

    def print_data_file(self):
        raw_dl_file = open(input_directory + "\\" + data_logger_file, 'r')
        is_word = 0
        this_word = []
        this_character = chr(0)
        last_character = chr(0)
        LS2 = LS3 = chr(0)
        while True:
            LS3 = LS2
            LS2 = last_character
            last_character = this_character
            this_character = raw_dl_file.read(1)
            if not this_character:
                break
            if ord(LS3) == 0:
                if ord(this_character) == 255:
                    is_word = 1

            if is_word == 1:
                if ord(this_character) == 255:
                    this_word.append(chr(255 - ord(last_character)))

                if ord(bytes(this_character)) == 0:
                    is_word = 0
                    self.weld_information.append(''.join(this_word))
                    this_word = []

        # TODO this does not work.
        for x in self.weld_information:
            x = x.replace("\r\n      ", " ")

        # self.weld_id = self.weld_information[5]
        self.weld_id = data_logger_file[:-4]
        self.diam_sdr = self.weld_information[10]
        self.diam_sdr = self.diam_sdr.split(" ")
        self.diam_sdr = self.diam_sdr[-1]
        return self.weld_information

for data_logger_file in os.listdir(input_directory):
    if data_logger_file[:-4] == ".DL4":
        try:
            x_cell += 1
            DATA_LOG = DataLogFile()
            DATA_LOG.print_data_file()
            sheet1.write(x_cell, y_cell, DATA_LOG.weld_id)
            sheet1.write(x_cell, y_cell+1, DATA_LOG.diam_sdr)
        except Exception as e:
            "something went wrong with " + data_logger_file

    # print(DATA_LOG.print_data_file())

filename = raw_input("what you want call the output file?  ")
output_spreadsheet.save(input_directory + "\\" + filename + ".xls")
raw_input(input_directory + "\\" + filename + ".xls saved. Job done boss. Enter to exit")
