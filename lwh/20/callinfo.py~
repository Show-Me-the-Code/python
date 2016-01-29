import xlrd
import xlwt


class Statistics(object):

    def __init__(self, user):
        self.path_read = '/home/lwh/SublimeTextProject/CallInfo.xls'
        self.path_save = '/home/lwh/SublimeTextProject/CallInfo(1).xls'
        self.user = user
        self.work()

    # change all format of time to second
    def tran_time(self, time_str):
        time = time_str.replace('分','.').replace('秒','')
        temp = time.split('.')
        if len(temp) == 1:      # just second
            time = int(temp[0])
            #print(time)
        elif len(temp) == 2:    # minute and second
            m = int(temp[0]) * 60
            s = int(temp[1])
            time = m + s
        #print(time)
        return time
        

    def work(self):
        wb = xlrd.open_workbook(self.path_read)
        sheets_list = wb.sheet_names()
        for sheet_name in sheets_list:
            wb_sheet = wb.sheet_by_name(sheet_name)
            # print(wb_sheet)
            # print(wb_sheet.nrows)
            # print(wb_sheet.ncols)
            # print(wb_sheet.cell_value(3,8))
            for i in range(1, wb_sheet.nrows):
                row = wb_sheet.row(i)
                time_str = row[3].value
                time = self.tran_time(time_str)
                self.user.total_time += time
                # print(each_time)
                # self.user.total_time = row[]
        print(self.user.total_time)

class User():

    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.total_time = 0
        self.most_call_out = ''
        self.most_call_in = ''
        self.number_in_dict = ''
        self.number_out_dict = ''


if __name__ == '__main__':
    user0 = User('lwh', '13257584928')
    analyzer_obj0 = Statistics(user0)
    print('success.')

